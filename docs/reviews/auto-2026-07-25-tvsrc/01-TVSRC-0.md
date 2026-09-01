# TVSRC-0 — Build the URL worklist + freeze the storage contract

Source: `TODO.md:55`. Severity in spec: MINOR, but gates everything.

## Task text (condensed from source; full text in TODO.md)

Write `custom/build_tv_worklist.py`: read the source CSV → dedupe on `url` (762 → 705, keep first) → carry `title` for the TVSRC-2 name check → emit `datastore/tv_urls.csv` (`url, title, slug`). Pin `slug = url.rstrip('/').rsplit('/', 1)[-1]` (whole final segment, id included). Anchor paths on `__file__`, never cwd. Explicit `encoding='utf-8'`. Add unanchored gitignore rules for `.pine` / `.jsonl`.

Acceptance: 705 rows; `len(set(slugs)) == 705` asserted **in the script**; `git check-ignore -v` matches; `git status --porcelain` shows zero untracked `.pine`/`.jsonl`.

## Execution log

- Wrote `custom/build_tv_worklist.py` (~80 lines incl. the pinned-slug rationale).
- First run: `source rows: 762 -> unique urls: 705`, `slugs unique: 705  ci-unique: 705  maxlen: 70`. Exit 0.
- gitignore rules (`**/datastore/pine/`, `*.pine`, `*.jsonl`) had already been appended and **proven** in the prior session — `git check-ignore -v` matches `datastore/pine/x.pine`, `testfolder/tv_source.jsonl`, and `custom/datastore/pine/y.pine` (the case an anchored rule would miss).

## Review round 1

```
VERDICT: PASS
FINDINGS:
  - severity: MINOR
    location: build_tv_worklist.py:60-63
    problem:  The spec's acceptance gate ("asserted in the script itself, not by eye") is built
              out of four bare `assert` statements. I verified they are elided: running the module
              under `python -O`, `AssertionError` is gone from `main.__code__.co_names` — all four
              gates evaporate and the script then overwrites a known-good worklist with whatever it
              built, silently. `PYTHONOPTIMIZE` is unset on this box today, so this is a loaded gun
              on the shelf, not a fired one — but an acceptance gate a single interpreter flag can
              disarm is a weaker gate than the spec asked for.
    fix:      Convert the two count gates to unconditional raises, e.g.
              `if len(work) != EXPECTED_ROWS: raise SystemExit(f"expected {EXPECTED_ROWS}, got {len(work)}")`
              and the same shape for `len(set(slugs)) != len(work)`. Keep the ascii/ci checks as
              asserts if you want; the row-count and uniqueness gates are the ones the spec pinned.

  - severity: MINOR
    location: build_tv_worklist.py:40
    problem:  `encoding="utf-8"` (not `utf-8-sig`) on a CSV that is visibly hand-maintained in a
              spreadsheet — it carries `Notes`, an unnamed blank column, `Tasks`, `Task_Description`
              — and whose FIRST column is `title`. One "Save as CSV UTF-8" from Excel prepends a BOM,
              the first fieldname becomes `'﻿title'`, `r.get("title")` returns None, and every
              row emits `title=""`. `url` is column 9, so the dedupe still yields 705, and all four
              assertions still pass. The worklist looks perfect and TVSRC-2's name-check gate — the
              ONLY validation of the n=1 first-PUB hypothesis, per the spec's own words — then
              compares 705 pine-facade `scriptName`s against 705 empty strings. Nothing in the script
              asserts a non-empty title, even though the spec states title is carried precisely for
              that gate. (Confirmed the file has no BOM today: first bytes are `b'titl'`.)
    fix:      Read with `encoding="utf-8-sig"` (a no-op when there is no BOM), and add
              `assert all(w["title"] for w in work), "empty title — BOM or renamed column?"`
              next to the existing gates so the failure is loud instead of downstream.

  - severity: NIT
    location: build_tv_worklist.py:4-5
    problem:  The docstring documents the inputs as `../../TradingViewStrategies.csv` and
              `../datastore/tv_urls.csv` — the exact cwd-relative notation the spec's CANONICAL PATHS
              block calls out by name as the live trap ("`../../TradingViewStrategies.csv` silently
              resolves to the wrong place when run from the repo root"). The code is right; the
              documentation teaches the wrong mental model to the next reader, four lines above the
              sentence claiming paths never touch cwd.
    fix:      State the resolved anchors instead: `SRC_CSV  = ROOT.parent / TradingViewStrategies.csv`
              and `WORKLIST = ROOT / datastore / tv_urls.csv`, with ROOT = ScrapyTUyanik/.
SUMMARY: I went in expecting the path off-by-one the spec was revised to fix, and it is not there —
`parents[1]` resolves to `ScrapyTUyanik\` and `ROOT.parent / "TradingViewStrategies.csv"` lands on the
real 1.4 MB file, both confirmed by importing the module and printing the resolved paths. The rest
holds under measurement rather than assertion: source is 762 rows with zero empty, zero
whitespace-padded, and zero malformed urls, so the 762 -> 705 arithmetic is pure dedupe with nothing
hiding behind a filter (57 dupes across 50 groups, and no dupe group has a divergent title, so
keep-first is not even load-bearing); the emitted worklist is exactly 705 data rows, 705 unique slugs,
705 case-insensitively unique, all ASCII, max length 70, all `[A-Za-z0-9_%-]`, the 3 percent-escapes
kept escaped, no Windows reserved device names, no trailing dot or space; `newline=""` is on both the
read and the write, so the multi-line `description` fields parse and the output round-trips; and
re-deriving the output in memory produces bytes byte-identical to what is on disk, so the script is
idempotent. Both gitignore gates pass `git check-ignore -v`, including the `custom/datastore/pine/`
case an anchored rule would have missed, and `git status --porcelain` shows zero untracked `.pine` or
`.jsonl`. The assertions run before the write, so a failure leaves the previous worklist intact rather
than a truncated one — that ordering was not an accident and it is the one design decision here worth
keeping. No slop: no argparse, no config, no abstraction, ~50 lines of which half is the pinned slug
rationale. What is left is a gate made of `assert` and a first-column BOM that would silently gut the
downstream name-check; neither is wrong today, both are one line to make permanently right. Fix those
two and stop touching this file.
```

### Fixes applied (all three, despite PASS)

- **MINOR (assert elision)** → the two spec-pinned gates converted to `raise SystemExit`; ci-unique / ascii kept as asserts. Verified: `python -O build_tv_worklist.py` still gates.
- **MINOR (BOM)** → read switched to `encoding="utf-8-sig"` with the failure mode written into a comment, plus a new `assert all(w["title"] for w in work)`.
- **NIT (docstring)** → docstring now states resolved anchors and names the cwd-relative form as the trap it is.

## Outcome

**PASS (round 1).** Re-ran after fixes: 705 rows, gates hold under both `python` and `python -O`.

Files touched: `custom/build_tv_worklist.py` (new), `datastore/tv_urls.csv` (generated), `.gitignore` (3 lines, prior session).
