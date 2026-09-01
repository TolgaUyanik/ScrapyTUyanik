"""
report_tv_source.py — TVSRC-2. Coverage report over the tvsource scrape.

Reads : ../testfolder/tv_source.jsonl, ../datastore/tv_urls.csv
Writes: ../testfolder/tv_source_report.md

Enforces the TVSRC-2 acceptance identity:
    captured + dead_404 + protected + no_pub_id + http_error + json_error == 705
`attempted` is reported SEPARATELY and is not a term in the sum (it is 705 by
definition, so including it makes the identity unsatisfiable).

NAME-CHECK GATE — the only validation of the n=1 first-PUB hypothesis.
Compares pine-facade scriptName against the CSV title. Normalization: casefold ->
strip non-alphanumerics -> collapse whitespace.

⚠ MEASURED 2026-07-25 on the 20-url slice: a bare equality check reports 20%
mismatch (3/15), but ALL THREE were benign — the CSV title carries an author
name the facade name omits ("Sadi's Pocket Pivot..." vs "Pocket Pivot..."),
or the script was version-bumped since the scrape ("GLOBEX BOX v1.0" vs "v1.5").
None was a wrong-PUB capture. Equality therefore measures title drift, NOT
"did we grab the wrong script", which is what the gate exists to detect.

So the gate classifies into three bands and only the last one counts against 5%:
  exact      — normalized strings equal
  benign     — one name CONTAINS the other AND the two are within a 0.6 length
               ratio (author prefix/suffix), or difflib ratio >= 0.80 (version
               bumps, punctuation drift)
  SUSPECT    — everything else. This is the wrong-PUB signal.

⚠ THE LENGTH GUARD ON CONTAINMENT IS LOAD-BEARING, NOT TIDINESS. Bare `a in b`
whitelists the exact failure this gate exists to catch: classify("ta", "Volume
Delta + RSI Confluence Signals") is a containment match, and "ta" is a real
imported library on that very page (TODO.md's n=1 multi-PUB evidence row). A
short facade name — `ta`, `MA`, `ZigZag` — has high substring odds against any
long title, and short names are precisely what a wrong-PUB library capture
looks like. Without the guard the gate scores such a capture as benign title
drift.

⚠ CORRECTION (2026-07-25, TVSRC-2 review). An earlier version of this docstring
called the `MAs` vs `Zeefreaks Predator Mask Crypto` row "a genuine library
capture". **That was false and is retracted.** The file on disk opens
`indicator(title="MAs", shorttitle="AOTS", overlay=true)` — an indicator, not a
`library()`. Its sibling `n7OXjXv8-ZFT-Classic.pine` is
`indicator(title="MAs", shorttitle="ZFT Classic")`, whose shorttitle is exactly
the CSV title. Both captures are CORRECT. The real lesson is different and more
useful: **facade `scriptName` is the Pine `title=`, while the CSV carries the
TradingView PUBLICATION name, and authors routinely set them differently.** So
this row is a field mismatch, not a mis-pick — see `resolve_suspects.py`, which
now settles exactly this case locally without spending a request.

⚠ SECOND CORRECTION, same review: an intermediate version of this note said
"no library capture was observed at n=360". **Also false.** 12 captures declare
`library()` — and all 12 classify `exact` (facade name == CSV title), including
one whose name is literally `ta`, a legitimately published library at
`/script/RA2vGpkA-ta/` with CSV title `ta`. So `ta` is not even a synthetic
example; it is a real, correctly-captured row in this corpus.

The accurate statement is: **no WRONG-PUB library capture was observed at
n=360** — every `library()` file present is the script its page publishes. The
length guard is therefore PRECAUTIONARY, not empirically forced: it costs
nothing and still SUSPECTs the constructed
`("ta", "Volume Delta + RSI Confluence Signals")` pairing, but it has not yet
caught a real defect and this docstring will not claim otherwise.

CONTAIN_RATIO is 0.50, not 0.60, and the margin is the reason. Lowest observed
GENUINE containment pair: `TheDevashishratio-Momentum [DRM] — Indicator` vs
`TheDevashishratio-Momentum`, len ratio 0.641 — and its difflib ratio is 0.781,
under the 0.80 rescue band, so it survives on the containment band alone. At
0.60 that leaves 0.04 of headroom and a slightly longer title (`... Pro`, ~0.58)
becomes a false SUSPECT. The nearest TRUE positive is `MAs` at 0.10, six times
further down, so the safe window is roughly 0.15–0.63 and 0.50 sits in the
middle of it instead of on the edge.
Threshold: SUSPECT / captured > 5% => first-PUB hypothesis is wrong at scale;
re-resolve those rows by name per TVSRC-2 and rerun.
"""
import csv
import json
import re
import sys
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # -> ScrapyTUyanik/

JSONL    = ROOT / "testfolder" / "tv_source.jsonl"
WORKLIST = ROOT / "datastore" / "tv_urls.csv"
PINE_DIR = ROOT / "datastore" / "pine"
REPORT   = ROOT / "testfolder" / "tv_source_report.md"

CODES = ["captured", "dead_404", "protected", "no_pub_id", "http_error", "json_error"]
TITLE_RE = re.compile(r"""^\s*(?:indicator|strategy|library)\s*\(\s*(?:title\s*=\s*)?["']([^"']+)""", re.M)
SHORT_RE = re.compile(r"""shorttitle\s*=\s*["']([^"']+)""")
VERDICTS = ROOT / "testfolder" / "tv_source_verdicts.json"
SUSPECT_THRESHOLD = 0.05
BENIGN_RATIO = 0.80
# Without this, "ta" matches any long title. 0.50, not 0.60: the lowest observed
# GENUINE containment pair sits at 0.641 (TheDevashishratio-Momentum), and the
# nearest true positive at 0.10 — so 0.50 is the middle of the safe window.
CONTAIN_RATIO = 0.50


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", "", (s or "").casefold())).strip()


def classify(facade_name: str, csv_title: str) -> str:
    a, b = norm(facade_name), norm(csv_title)
    if not a or not b:
        return "SUSPECT"
    if a == b:
        return "exact"
    if (a in b or b in a) and min(len(a), len(b)) / max(len(a), len(b)) >= CONTAIN_RATIO:
        return "benign"
    if SequenceMatcher(None, a, b).ratio() >= BENIGN_RATIO:
        return "benign"
    return "SUSPECT"


def normalize_source_paths() -> int:
    """One-off: rewrite Windows separators in `source_path` to posix, in place.

    Rows written before the `.as_posix()` fix carry `datastore\\pine\\x.pine`.
    They are TERMINAL (error=null) so the spider's resume will never rewrite
    them and the artifact cannot self-heal — TVSRC-4 hands this file to another
    repo, so the separators are normalized here instead. Idempotent.
    """
    lines = [l for l in open(JSONL, encoding="utf-8") if l.strip()]
    out, fixed = [], 0
    for l in lines:
        r = json.loads(l)
        sp = r.get("source_path")
        if sp and "\\" in sp:
            r["source_path"] = sp.replace("\\", "/")
            fixed += 1
        out.append(json.dumps(r, ensure_ascii=False))
    if fixed:
        JSONL.write_text("\n".join(out) + "\n", encoding="utf-8")
    return fixed


def load_rows() -> list[dict]:
    """Raw jsonl -> one row per url, last write wins.

    ⚠ ALWAYS go through this. The file legitimately contains duplicate urls (a
    retried http_error/json_error appends a second row) and did in fact contain
    77 of them from an operator error where two crawlers overlapped. Counting
    raw lines inflates `attempted` past 705 and breaks the six-term identity for
    a reason the report cannot explain.
    """
    raw = [json.loads(l) for l in open(JSONL, encoding="utf-8") if l.strip()]
    return list({r["url"]: r for r in raw}.values())


def main() -> int:
    rows = load_rows()

    # The identity is checked against WHICHEVER worklist was scraped. Hardcoding
    # tv_urls.csv here would report a false MISMATCH the moment the spider is run
    # with -a worklist=... (the union index is 2,960 rows, not 705).
    wl = WORKLIST
    for i, a in enumerate(sys.argv):
        if a == "--worklist" and i + 1 < len(sys.argv):
            wl = ROOT / "datastore" / sys.argv[i + 1]
    wl_rows = list(csv.DictReader(open(wl, encoding="utf-8", newline="")))
    titles = {r["slug"]: r["title"] for r in wl_rows}
    total = len(wl_rows)

    # ⚠ SCOPE THE REPORT TO THIS WORKLIST. The jsonl is a single append-only log
    # shared by every run, so after a second worklist is scraped it holds rows from
    # both. Without this filter: (a) the six-term identity compares N worklists'
    # rows against ONE worklist's total and reports a false MISMATCH, and (b) every
    # row from the OTHER worklist has no entry in `titles`, so the name check scores
    # it against "" and auto-flags it SUSPECT. Measured before the fix: 26.01%
    # SUSPECT, of which 348 were purely this artifact — the true figure was 12.2%.
    wl_urls = {r["url"] for r in wl_rows}
    scoped = [r for r in rows if r["url"] in wl_urls]
    skipped = len(rows) - len(scoped)
    rows = scoped
    print(f"worklist: {wl.name} ({total} rows)"
          + (f" | {skipped} jsonl row(s) from other worklists excluded" if skipped else ""))

    # Only normalize once the crawl is COMPLETE. This function truncate-rewrites the
    # jsonl; run mid-crawl it silently drops any row the spider appended between the
    # read and the write (the spider's handle is O_APPEND so nothing corrupts, but a
    # lost capture row leaves its .pine orphaned -> the report then prints an
    # unexplainable on_disk/captured mismatch). This script IS the natural mid-crawl
    # progress check, so the guard is not theoretical.
    if len(rows) >= total or "--normalize" in sys.argv:
        fixed = normalize_source_paths()
        if fixed:
            print(f"normalized {fixed} windows-separator source_path value(s)")
            rows = load_rows()          # re-read MUST re-collapse — see load_rows()
    elif any("\\" in (r.get("source_path") or "") for r in rows):
        print(f"NOTE: {sum(1 for r in rows if chr(92) in (r.get('source_path') or ''))} "
              f"row(s) carry windows separators; normalization deferred until the crawl "
              f"completes ({len(rows)}/{total}). Force with --normalize.")

    counts = Counter(r["error"] or "captured" for r in rows)
    tally = {c: counts.get(c, 0) for c in CODES}
    unknown = {k: v for k, v in counts.items() if k not in CODES}
    identity = sum(tally.values())

    captured = [r for r in rows if r.get("source_available")]
    bands = Counter(classify(r.get("script_name"), titles.get(r["slug"], "")) for r in captured)
    suspects = [r for r in captured
                if classify(r.get("script_name"), titles.get(r["slug"], "")) == "SUSPECT"]
    rate = len(suspects) / len(captured) if captured else 0.0
    gate = "PASS" if rate <= SUSPECT_THRESHOLD else "FAIL"

    # Scoped to THIS worklist's slugs — PINE_DIR accumulates across every run, so a
    # bare glob would compare one worklist's captured count against the whole corpus.
    on_disk = sum(1 for s in titles if (PINE_DIR / f"{s}.pine").exists())

    L = ["# TVSRC-2 — TradingView Pine source coverage report", "",
         f"Worklist: **{total}** urls · rows logged: **{len(rows)}** · "
         f"`attempted == {len(rows)}` (reported separately, not a term in the identity)", "",
         "## Reason-code tally", "",
         "| Code | Count | % |", "|---|---:|---:|"]
    for c in CODES:
        L.append(f"| `{c}` | {tally[c]} | {tally[c]/total*100:.1f}% |")
    L += ["", "### Acceptance identity", "```",
          " + ".join(CODES) + f" == {total}",
          " + ".join(str(tally[c]) for c in CODES) + f" = {identity}",
          f"{'OK' if identity == total else 'MISMATCH'}"
          f"{'' if identity == total else f' -- {total - identity} url(s) unaccounted for'}",
          "```"]
    if unknown:
        L.append(f"\n⚠ Unknown reason codes present (not in the ladder): `{unknown}`")

    L += ["", "## Name-check gate (validates the n=1 first-PUB hypothesis)", "",
          f"Captured rows compared: **{len(captured)}**", "",
          "| Band | Count | Meaning |", "|---|---:|---|",
          f"| `exact` | {bands.get('exact',0)} | normalized names identical |",
          f"| `benign` | {bands.get('benign',0)} | containment (author prefix/suffix) "
          f"or difflib ratio >= {BENIGN_RATIO} (version bump) |",
          f"| `SUSPECT` | {bands.get('SUSPECT',0)} | **wrong-PUB signal** |", "",
          f"SUSPECT rate: **{rate*100:.2f}%** vs threshold {SUSPECT_THRESHOLD*100:.0f}% "
          f"-> **{gate}**", ""]
    # POST-REMEDY STATE. Without this the durable record says only "FAIL" while the
    # thing that cleared it lives in console output nobody kept.
    resid_gate = None
    v, missing = None, None
    if VERDICTS.exists():
        v = json.loads(VERDICTS.read_text(encoding="utf-8"))
        # A sidecar written against an older/smaller suspect set would silently
        # yield a too-low residual and a passing exit code. Refuse to use a stale one.
        missing = {r["url"] for r in suspects} - v.keys()

    if v is not None and missing:
        # ⚠ SKIP the residual ENTIRELY. An earlier version set `v = {}` and fell
        # through, which computed flagged=0 -> residual 0.00% -> PASS -> exit 0 —
        # i.e. it manufactured the exact silent pass this guard exists to prevent,
        # and did it more confidently than having no guard at all. `resid_gate`
        # must stay None so `effective` falls back to the raw gate.
        L += [f"⚠ **STALE SIDECAR — covers {len(v)} verdicts but "
              f"{len(missing)} of {len(suspects)} current SUSPECT rows are absent.** "
              f"**No residual is computed and the raw gate stands (FAIL).** Re-run "
              f"`resolve_suspects.py --apply`.", ""]
    elif v:
        vc = Counter(x["verdict"] for x in v.values())
        CLEARS = ("title_match", "first_sole", "first_best")
        cleared = sum(vc[k] for k in CLEARS)
        flagged = sum(n for k, n in vc.items() if k not in CLEARS)
        resid = flagged / len(captured) if captured else 0.0
        resid_gate = "PASS" if resid <= SUSPECT_THRESHOLD else "FAIL"
        L += ["### Post-remedy resolution (`resolve_suspects.py --apply`)", "",
              "| Verdict | Count | Capture stands? |", "|---|---:|---|"]
        for k in ("title_match", "first_sole", "first_best", "by_name", "id_changed",
                  "unresolved", "indeterminate", "fetch_error"):
            if vc.get(k):
                L.append(f"| `{k}` | {vc[k]} | {'yes' if k in CLEARS else '**needs review**'} |")
        L += ["", f"Raw SUSPECT **{len(suspects)}/{len(captured)} = {rate*100:.2f}% FAIL** → "
              f"resolved as **{cleared} cleared / {flagged} flagged**.", "",
              f"**Residual rate = {flagged}/{len(captured)} = {resid*100:.2f}% "
              f"vs 5% → {resid_gate}**", "",
              "⚠ `cleared` means *no evidence of a mis-pick*, established by elimination "
              "(sole id) or by the CSV title matching the file's own `title=`/`shorttitle=`. "
              "It does **not** mean the script's behaviour was verified — see `needs_eye`.", ""]
    else:
        L += ["⚠ **No remedy has been run.** The gate above is FAILING and nothing has "
              "cleared it. Run `python resolve_suspects.py --apply`, then re-run this "
              "report — a failing gate with no recorded resolution is not a completed task.", ""]

    if suspects:
        L += ["### SUSPECT rows (raw, pre-remedy)", "",
              "| slug | facade scriptName | CSV title |", "|---|---|---|"]
        for r in suspects[:50]:
            L.append(f"| `{r['slug']}` | {r.get('script_name')} | {titles.get(r['slug'])} |")
        L.append("")

    # SOURCE-LEVEL sanity, because every other check in this report compares NAMES
    # and a name check can never see that a "Twin Range Filter" is a one-line EMA.
    # Flags a capture when the file is structurally trivial (<=4 non-comment lines)
    # or when its own Pine title=/shorttitle= matches NEITHER the CSV title nor the
    # facade name. Cheap, local, and the only signal here that reads the payload.
    eye = []
    for r in captured:
        p = ROOT / (r.get("source_path") or "")
        if not p.exists():
            continue
        txt = p.read_text(encoding="utf-8")
        body = [l for l in txt.splitlines() if l.strip() and not l.strip().startswith("//")]
        names = TITLE_RE.findall(txt)[:1] + SHORT_RE.findall(txt)[:1]
        csv_t = titles.get(r["slug"], "")
        name_ok = any(classify(n, csv_t) in ("exact", "benign") for n in names) or \
            classify(r.get("script_name"), csv_t) in ("exact", "benign")
        if len(body) <= 4 or not name_ok:
            eye.append((r["slug"], len(body), r["source_len"], names[:2], csv_t))
    trivial = sum(1 for e in eye if e[1] <= 4)
    L += ["", "## `needs_eye` — review queue (name-field mismatch OR structurally trivial)", "",
          f"**{len(eye)}** of {len(captured)} captures flagged: **{len(eye)-trivial} name-field "
          f"mismatch** (≈ the SUSPECT band, since no `title=`/`shorttitle=` matched either) "
          f"+ **{trivial} structurally trivial** (<=4 non-comment lines), overlaps counted once.",
          "", "⚠ Only the structurally-trivial half is genuinely source-level; the name half is "
          "still a name check. Do not read this as 37 rows of new payload-level signal.", ""]
    if eye:
        L += ["| slug | body lines | chars | pine title/shorttitle | CSV title |", "|---|---:|---:|---|---|"]
        for slug, nb, ln, nm, ct in sorted(eye, key=lambda e: e[1])[:40]:
            L.append(f"| `{slug}` | {nb} | {ln} | {' / '.join(nm)} | {ct} |")
        L.append("")

    # DEVIATION 2 (see spider docstring): source is kept whenever it arrives,
    # regardless of the scriptAccess label, so the labels are tallied HERE to keep
    # a non-open_no_auth capture visible instead of silently discarded upstream.
    access = Counter(r.get("script_access") or "(none)" for r in captured)
    L += ["", "## `scriptAccess` of captured rows", "",
          "| Access | Count |", "|---|---:|"]
    for k, v in access.most_common():
        flag = "" if k == "open_no_auth" else "  ⚠ non-default"
        L.append(f"| `{k}`{flag} | {v} |")
    L += ["", "## Files on disk", "",
          f"`datastore/pine/*.pine`: **{on_disk}** — "
          f"{'matches' if on_disk == tally['captured'] else '**MISMATCH vs**'} "
          f"captured count {tally['captured']}", ""]

    REPORT.write_text("\n".join(L), encoding="utf-8")

    print(f"attempted={len(rows)} " + " ".join(f"{c}={tally[c]}" for c in CODES))
    print(f"identity: {identity} == {total} -> {'OK' if identity == total else 'MISMATCH'}")
    print(f"name gate: SUSPECT {len(suspects)}/{len(captured)} = {rate*100:.2f}% -> {gate} (raw)")
    if resid_gate:
        print(f"post-remedy residual -> {resid_gate}")
    print(f"needs_eye: {len(eye)} capture(s) flagged for source-level review")
    print(f"pine files on disk: {on_disk} (captured={tally['captured']})")
    print(f"report -> {REPORT}")
    # The raw gate may legitimately FAIL while the remedy clears it; exit on the
    # residual when one exists, so CI-style use reflects the resolved state.
    effective = resid_gate or gate
    return 0 if (identity == total and effective == "PASS" and on_disk == tally["captured"]) else 1


if __name__ == "__main__":
    sys.exit(main())
