"""
resolve_suspects.py — TVSRC-2's named remedy for a FAILING name-check gate.

    cd custom
    python resolve_suspects.py            # dry run: classify only, no writes
    python resolve_suspects.py --apply    # persist verdicts to a SIDECAR + rewrite
                                          # .pine only for true wrong-PUB rows

WHY THIS EXISTS
The name-check gate is the only validation of the n=1 "first PUB in document
order is the target script" hypothesis. When it FAILS (>5% SUSPECT), TVSRC-2
requires re-resolving those rows rather than lowering the threshold.

⚠ WHAT THE GATE ACTUALLY COMPARES — this is the root of most SUSPECTs.
pine-facade's `scriptName` is the Pine `title=` argument. The CSV `title` is the
TradingView PUBLICATION name. **They are different fields and authors routinely
set them differently.** Worked example, verified on disk: both
`dj78jmEN-Zeefreaks-Predator-Mask-Crypto.pine` and `n7OXjXv8-ZFT-Classic.pine`
open `indicator(title="MAs", shorttitle=...)` — facade reports `MAs` for both,
while the CSV carries the publication names "Zeefreaks Predator Mask Crypto" and
"ZFT Classic", the latter being literally that file's own `shorttitle`. Neither
is a wrong capture. So a name mismatch is NOT prima facie evidence of a mis-pick,
and the SUSPECT rate measures publication-vs-title drift at least as much as it
measures capture error. That is why this script exists and why the raw rate is
not the number to act on.

VERDICTS — written to `testfolder/tv_source_verdicts.json`, keyed by url.
⚠ **NOT to `pub_selection` in the jsonl**, which TVSRC-2's spec asked for. Recorded
deviation: writing verdicts into the jsonl means truncate-rewriting an append-only
audit log whose duplicate rows are the only forensic record of the concurrent-crawler
operator error. The sidecar keeps both. **`pub_selection` in the jsonl stays `'first'`
for every captured row and is therefore NOT the verdict field — read the sidecar.**
Every verdict persists the ids it was decided on, so all of it is re-derivable offline
by joining the sidecar against the jsonl's `pub_id`, with zero requests.

  first_sole    page carries exactly ONE PUB id AND it is the id we captured
                -> no alternative existed at re-fetch time. Capture stands.
                ⚠ NOT "a mis-pick was impossible" — see the temporal caveat below.
  first_best    several ids; the one we captured still scores highest AND clears
                the score floor. Capture stands.
  title_match   the CSV title matches the .pine's own `title=` or `shorttitle=`
                -> settled from local source, no fetch needed. Capture stands.
  by_name       several ids; a DIFFERENT one scores higher -> TRUE WRONG-PUB.
                .pine is rewritten under --apply.
  id_changed    page now carries one id and it is NOT the one we captured.
                Cannot conclude either way -> needs review.
  unresolved    several ids but the winner is below the score floor. "Best of a
                bad set" is not evidence; flagged, not cleared.
  indeterminate page returned no PUB id at all (interstitial, re-render, changed
                embed). ⚠ NEVER treated as a rename.

⚠ TEMPORAL CAVEAT, stated because it cannot be engineered away here: the pick was
made against the crawl-time page; this script re-fetches hours later and no
crawl-time HTML was retained (`HTML_Files/` is empty). "One id NOW" is therefore
not proof of "one id THEN". A future run should persist hop-1 HTML for flagged
rows so the discriminator is replayable offline.

⚠ NAME MATCHING NEVER INSPECTS BEHAVIOUR. A row cleared here can still be the
wrong script if the author reused a title. The source-level spot-check in
TVSRC-2's acceptance is a separate obligation and this script does not discharge
it — see the `needs_eye` flag in report_tv_source.py.

Rate limited to match the spider (5 s), single-threaded, utf-8 throughout.
"""
import argparse
import csv
import importlib.util
import json
import re
import sys
import time
import urllib.request
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

JSONL   = ROOT / "testfolder" / "tv_source.jsonl"
SIDECAR = ROOT / "testfolder" / "tv_source_verdicts.json"
WORKLIST = ROOT / "datastore" / "tv_urls.csv"
PINE_DIR = ROOT / "datastore" / "pine"

FACADE = "https://pine-facade.tradingview.com/pine-facade/get/PUB%3B{}/last"
PUB_RE = re.compile(r"PUB(?:;|%3B|\\u003[Bb])([0-9a-fA-F]{32})")
TITLE_RE = re.compile(r"""^\s*(?:indicator|strategy|library)\s*\(\s*(?:title\s*=\s*)?["']([^"']+)""", re.M)
SHORT_RE = re.compile(r"""shorttitle\s*=\s*["']([^"']+)""")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
DELAY = 5

_spec = importlib.util.spec_from_file_location("rep", Path(__file__).parent / "report_tv_source.py")
rep = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rep)
SCORE_FLOOR = rep.BENIGN_RATIO          # same bar the gate uses; no private threshold


def get(url: str) -> str:
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en"})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")


def score(a: str, b: str) -> float:
    return SequenceMatcher(None, rep.norm(a), rep.norm(b)).ratio()


def local_title_match(row, csv_title):
    """Settle from the captured source before spending a request.

    facade scriptName == Pine `title=`. If the CSV publication name matches the
    file's own title= or shorttitle=, the capture is demonstrably the right file
    and the gate was comparing the wrong two fields.
    """
    p = ROOT / row["source_path"]
    if not p.exists():
        return None
    txt = p.read_text(encoding="utf-8")
    names = TITLE_RE.findall(txt)[:1] + SHORT_RE.findall(txt)[:1]
    for n in names:
        if rep.classify(n, csv_title) in ("exact", "benign"):
            return n
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="persist verdicts (default: dry run)")
    args = ap.parse_args()

    rows = {}
    for line in open(JSONL, encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            rows[r["url"]] = r
    titles = {r["slug"]: r["title"]
              for r in csv.DictReader(open(WORKLIST, encoding="utf-8", newline=""))}
    captured = [r for r in rows.values() if r.get("source_available")]

    suspects = [r for r in captured
                if rep.classify(r.get("script_name"), titles.get(r["slug"], "")) == "SUSPECT"]
    print(f"{len(suspects)} SUSPECT row(s) of {len(captured)} captured\n")

    verdicts, out = Counter(), {}

    # --- pass 1: settle locally, no network -------------------------------
    remaining = []
    for r in suspects:
        t = titles.get(r["slug"], "")
        hit = local_title_match(r, t)
        if hit:
            verdicts["title_match"] += 1
            out[r["url"]] = {"verdict": "title_match", "matched_field": hit, "score": None}
            print(f"  title_match  csv={t!r}\n               matches source field {hit!r} "
                  f"(facade title= {r['script_name']!r})")
        else:
            remaining.append(r)
    print(f"\npass 1 settled {verdicts['title_match']} locally; {len(remaining)} need a fetch\n")

    # --- pass 2: re-fetch the page, count ids -----------------------------
    for i, r in enumerate(remaining, 1):
        t = titles.get(r["slug"], "")
        captured_id = (r.get("pub_id") or "").removeprefix("PUB;")
        try:
            ids = list(dict.fromkeys(PUB_RE.findall(get(r["url"]))))
        except Exception as e:
            verdicts["fetch_error"] += 1
            out[r["url"]] = {"verdict": "fetch_error", "detail": type(e).__name__}
            print(f"[{i}/{len(remaining)}] fetch_error {r['slug']}: {type(e).__name__}")
            time.sleep(DELAY)
            continue

        if not ids:
            # ⚠ NOT a rename. Zero ids means the page did not render what we parsed
            # at crawl time (interstitial / changed embed) — no conclusion available.
            verdicts["indeterminate"] += 1
            out[r["url"]] = {"verdict": "indeterminate", "ids": 0}
            print(f"[{i}/{len(remaining)}] indeterminate (0 ids on page) {r['slug']}")
            time.sleep(DELAY)
            continue

        if len(ids) == 1:
            if ids[0].lower() == captured_id.lower():
                verdicts["first_sole"] += 1
                out[r["url"]] = {"verdict": "first_sole", "ids": 1,
                                 "id": ids[0], "captured": captured_id}
                print(f"[{i}/{len(remaining)}] first_sole (1 id, == captured) "
                      f"facade={r['script_name']!r} csv={t!r}")
            else:
                verdicts["id_changed"] += 1
                out[r["url"]] = {"verdict": "id_changed", "was": captured_id, "now": ids[0]}
                print(f"[{i}/{len(remaining)}] ⚠ id_changed {r['slug']}: "
                      f"captured {captured_id[:8]} but page now serves {ids[0][:8]}")
            time.sleep(DELAY)
            continue

        cands = []
        for pid in ids:
            time.sleep(DELAY)
            try:
                d = json.loads(get(FACADE.format(pid)))
                if isinstance(d, dict) and d.get("source"):
                    cands.append((score(d.get("scriptName") or "", t), pid, d))
            except Exception:
                pass
        if not cands:
            verdicts["fetch_error"] += 1
            out[r["url"]] = {"verdict": "fetch_error", "detail": "no candidate fetched"}
            continue

        cands.sort(key=lambda c: -c[0])
        best_score, best_pid, best = cands[0]
        same = best_pid.lower() == captured_id.lower()

        if best_score < SCORE_FLOOR:
            # "Best of a set where nothing matches" is not evidence of anything.
            verdicts["unresolved"] += 1
            out[r["url"]] = {"verdict": "unresolved", "ids": len(ids), "score": round(best_score, 3),
                             "winner_is_captured": same, "captured": captured_id, "all_ids": ids}
            print(f"[{i}/{len(remaining)}] unresolved ({len(ids)} ids, best score "
                  f"{best_score:.2f} < {SCORE_FLOOR}) {r['slug']}")
        elif same:
            verdicts["first_best"] += 1
            out[r["url"]] = {"verdict": "first_best", "ids": len(ids), "score": round(best_score, 3),
                             "id": best_pid, "captured": captured_id, "all_ids": ids}
            print(f"[{i}/{len(remaining)}] first_best ({len(ids)} ids, score {best_score:.2f}) "
                  f"facade={r['script_name']!r}")
        else:
            verdicts["by_name"] += 1
            out[r["url"]] = {"verdict": "by_name", "ids": len(ids), "score": round(best_score, 3),
                             "was": captured_id, "now": best_pid,
                             "new_name": best.get("scriptName")}
            print(f"[{i}/{len(remaining)}] ⚠ by_name WRONG-PUB {r['script_name']!r} -> "
                  f"{best.get('scriptName')!r} (score {best_score:.2f})")
            if args.apply:
                with open(PINE_DIR / f"{r['slug']}.pine", "w", encoding="utf-8", newline="") as f:
                    f.write(best["source"])
                r.update(pub_id=f"PUB;{best_pid}", script_name=best.get("scriptName"),
                         script_access=best.get("scriptAccess"), version=best.get("version"),
                         source_len=len(best["source"]))

    cleared = verdicts["title_match"] + verdicts["first_sole"] + verdicts["first_best"]
    flagged = verdicts["by_name"] + verdicts["id_changed"] + verdicts["unresolved"] \
        + verdicts["indeterminate"] + verdicts["fetch_error"]
    print(f"\nverdicts: {dict(verdicts)}")
    print(f"CLEARED (capture stands): {cleared}   FLAGGED (needs review or rewrite): {flagged}")
    print(f"residual SUSPECT rate = {flagged}/{len(captured)} = "
          f"{flagged/len(captured)*100:.2f}%  vs 5% threshold -> "
          f"{'PASS' if flagged/len(captured) <= 0.05 else 'FAIL'}")

    if args.apply:
        # SIDECAR, never a truncate of the append-only audit log: the raw jsonl is
        # the only forensic record of the duplicate rows from the concurrent-crawler
        # operator error, and rewriting it from the collapsed dict would destroy them.
        SIDECAR.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"wrote {len(out)} verdicts -> {SIDECAR}  (audit log left intact)")
    else:
        print("dry run — nothing written. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
