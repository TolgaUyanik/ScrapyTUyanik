"""
build_tv_worklist.py — TVSRC-0. Build the deduped URL worklist for the tvsource spider.

Reads : SRC_CSV  = ROOT.parent / "TradingViewStrategies.csv"   (762 rows, 57 dupe urls)
Writes: WORKLIST = ROOT / "datastore" / "tv_urls.csv"          (705 rows: url, title, slug)
        ...where ROOT = ScrapyTUyanik/. Paths are stated as resolved anchors on
        purpose: the cwd-relative form ("../../TradingViewStrategies.csv") is the
        trap this script exists to avoid — it silently resolves one level too high
        when run from the repo root instead of custom/.

SLUG DEFINITION (pinned by TVSRC-0 — do not change without re-verifying):
    slug = url.rstrip('/').rsplit('/', 1)[-1]     # whole final path segment, 8-char id INCLUDED
Verified on the real 705: unique, case-insensitively unique (NTFS-safe), all ASCII,
max 70 chars, chars limited to [A-Za-z0-9_%-]. Percent-escapes are KEPT escaped
(3 urls carry them, e.g. uY9EBtHq-RSI-1H-afi%C8%99at-pe-3M); unquoting would
reintroduce non-ASCII filenames.

Rejected alternatives, do not re-derive:
  - "text after the 8-char id" -> EMPTY for 103 of 705 urls, and collides across
    12 groups (Trent-Finder-V3, Midnight-30min-High-Low x3, ...). Collisions
    overwrite .pine files SILENTLY while the jsonl row count still reads 705.
  - CSV `title` -> not filesystem-safe.

All paths anchor on __file__, never cwd. All I/O is explicitly utf-8 (this box
defaults to cp1254).
"""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # -> ScrapyTUyanik/

SRC_CSV  = ROOT.parent / "TradingViewStrategies.csv"
WORKLIST = ROOT / "datastore" / "tv_urls.csv"

EXPECTED_ROWS = 705


def slug_for(url: str) -> str:
    return url.rstrip("/").rsplit("/", 1)[-1]


def build() -> list[dict]:
    # utf-8-sig, not utf-8: this CSV is hand-maintained in a spreadsheet (Notes,
    # Tasks, Task_Description columns) and `title` is column 1. One "Save as CSV
    # UTF-8" from Excel prepends a BOM -> the fieldname becomes '﻿title',
    # every title reads back empty, the dedupe still yields 705, and TVSRC-2's
    # name-check gate then compares 705 scriptNames against 705 empty strings.
    # No-op when there is no BOM (there is none today).
    with open(SRC_CSV, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    seen, out = set(), []
    for r in rows:
        url = (r.get("url") or "").strip()
        if not url or url in seen:
            continue
        seen.add(url)
        out.append({"url": url, "title": (r.get("title") or "").strip(), "slug": slug_for(url)})

    print(f"source rows: {len(rows)}  ->  unique urls: {len(out)}")
    return out


def main() -> int:
    work = build()

    slugs = [w["slug"] for w in work]

    # Acceptance gates live in the script, not in the operator's eyeballs — and the
    # two the spec pinned are unconditional raises, not asserts: `python -O` elides
    # every assert, which would let this silently overwrite a known-good worklist.
    if len(work) != EXPECTED_ROWS:
        raise SystemExit(f"FAIL: expected {EXPECTED_ROWS} unique urls, got {len(work)}")
    if len(set(slugs)) != len(work):
        raise SystemExit(f"FAIL: slug collision — {len(work) - len(set(slugs))} duplicate(s)")

    assert len({s.lower() for s in slugs}) == len(work), "slug collision (case-insensitive / NTFS)"
    assert all(s.isascii() and s for s in slugs), "non-ascii or empty slug"
    # title feeds TVSRC-2's name-check gate; empty means a BOM or a renamed column.
    assert all(w["title"] for w in work), "empty title — BOM or renamed column?"

    WORKLIST.parent.mkdir(parents=True, exist_ok=True)
    with open(WORKLIST, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["url", "title", "slug"])
        w.writeheader()
        w.writerows(work)

    print(f"slugs unique: {len(set(slugs))}  ci-unique: {len({s.lower() for s in slugs})}  "
          f"maxlen: {max(len(s) for s in slugs)}")
    print(f"wrote {len(work)} rows -> {WORKLIST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
