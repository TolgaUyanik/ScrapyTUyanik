# Run summary — `tvsrc`, 2026-07-25

Mode C batch execution: `/brutally-honest-review --auto TVSRC-0 TVSRC-1 TVSRC-2 TVSRC-3 TVSRC-4`

| Task | Status | Rounds | Files touched | Follow-ups |
|------|--------|--------|---------------|------------|
| TVSRC-0 | **PASS** | 1 | `custom/build_tv_worklist.py`, `datastore/tv_urls.csv`, `.gitignore` | none |
| TVSRC-1 | **PASS** | 3 (REVISE, REVISE, PASS) | `custom/custom/spiders/TradingViewSource.py`, `custom/report_tv_source.py`, `TODO.md` | 2 recorded deviations |
| TVSRC-2 | **⚠ ESCALATED — round cap** | 3 (REVISE ×3) | `custom/report_tv_source.py`, `custom/resolve_suspects.py`, `testfolder/*`, `datastore/pine/*` (360), `TODO.md`, `00-`/`04-manifest` | **all round-3 fixes applied but not gate-verified** |
| TVSRC-3 | **NOT TRIGGERED** | n/a | none | triggers remain live for future runs |
| TVSRC-4 | **DEFERRED** (user, Phase 2) | n/a | `TODO.md` (4-step checklist) | 4 sub-steps, zero `Backtesting/` writes |

Task-file write-back: **done per house convention** — `TVSRC-0`/`-1` marked `[x]`, `TVSRC-2` marked `[~]` (partially done → escalated) with a dated OUTCOME block carrying the full counts and every caveat, `TVSRC-3`/`-4` left `[ ]` with pointers.

---

## The deliverable

**360 Pine source files, 3.0 M chars / 4 MB, in `datastore/pine/<slug>.pine`** (gitignored), with a 705-row audit log at `testfolder/tv_source.jsonl`.

| Code | Count | % |
|---|---:|---:|
| `captured` | **360** | 51.1% |
| `dead_404` | **345** | 48.9% |
| `protected` / `no_pub_id` / `http_error` / `json_error` | **0** | — |

`360 + 345 + 0 + 0 + 0 + 0 == 705` ✅ · `attempted == 705` · **360 `.pine` on disk, 1:1 with captured rows, zero orphans**.

Corpus: indicator 319 / strategy 29 / library 12 · Pine v6 197, v5 153, untagged 10 · 231 files contain non-ASCII and round-trip clean · `scriptAccess` `open_no_auth` on all 360.

## What the gates actually caught

Eleven review rounds across three gated tasks. The findings that changed the work:

1. **hop-1 404s at 44%** (7× the recon guess) were being written off as TERMINAL with no evidence. Forced a hand spot-check, then a far better one (below).
2. **The name gate's `benign` band whitelisted short names** — `classify("ta", "Volume Delta + RSI Confluence Signals")` returned benign, the exact wrong-PUB case the gate exists to catch. Length guard added.
3. **The remedy that cleared a failing gate existed only in console output.** `pub_selection` was `'first'` on all 360 rows; nothing was persisted. Now a sidecar, with the ids each verdict was decided on.
4. **The elimination logic was weaker than advertised** — zero-ids folded in with one-id, and the page's id was never compared to the captured id.
5. **`first_best` had no score floor.** With one added, **10 rows previously reported as confirmed renames became honestly `unresolved`** — the single most consequential fix in the run.
6. **A staleness guard was inverted**, yielding `residual 0.00% → PASS → exit 0` on a stale sidecar: worse than no guard. Now proven in both directions (stale → exit 1, good → exit 0).

## The headline claim, stated precisely

**Zero confirmed wrong-PUB captures, with 10 rows unresolved.** Raw name gate 36/360 = 10.00% **FAIL** → remedy (`title_match` 2, `first_sole` 24, `unresolved` 10, `by_name` **0**) → **residual 10/360 = 2.78% PASS**.

⚠ **Not** "the first-PUB hypothesis is validated with zero counterexamples" — an earlier draft said that and it was wrong twice over. The hypothesis is **supported at n=360, not proven**: 10 rows could not be settled by name evidence, and every clearance carries a temporal caveat (the pick was made at crawl time; the check re-fetched hours later, and no crawl-time HTML was retained).

## Best evidence in the run came from a mistake

Two crawlers ran concurrently for ~10 minutes — my error, ~77 wasted requests. It also fetched 77 urls **twice, from independent processes, at different times**:

| Check | Result |
|---|---|
| Pairs disagreeing on reason code | **0 of 77** |
| `dead_404` in both fetches | **38** |
| Captured-both pairs differing in `source_len` | **0 of 39** |

That is a 38-url repeat measurement of the `dead_404` finding — **9.5× the 4-url curl check, at zero extra cost**, and it tests session-level soft-blocking, which curls cannot. It was surfaced by the TVSRC-2 reviewer, not by me.

## Outstanding — needs a human

1. **TVSRC-2 escalated at the round cap.** Every round-3 finding is fixed and each fix verified by direct execution, but **no gate re-reviewed those fixes**. A fourth round would settle it.
2. **10 `unresolved` rows** — multi-id pages where no candidate name clears 0.80 against the CSV title. All carry `winner_is_captured: true`. Review queue, not confirmed defects.
3. **37 `needs_eye` flags** — 34 name-field mismatches (≈ the SUSPECT band) + 4 structurally trivial files. Only the trivial half is genuinely source-level.
4. **TVSRC-4 deferred** — 4 steps written up in `TODO.md`, gated on your authorization for `Backtesting/` writes.
5. **Persist hop-1 HTML for flagged rows** in any future run, so the multi-PUB discriminator is replayable offline instead of re-fetching hours later.
6. **TVSRC-1's `> 200 chars` acceptance is retired** — 2 captures fall under it and both are complete valid scripts. Replace with "starts with `//` and parses a declaration".

## Process lesson

The same defect recurred **three times**: a claim corrected in the artifact a reviewer pointed at, left standing in another. Round 1 (`MAs` called a "library capture"), round 2 (`TODO.md` fixed, `04-TVSRC-4.md` missed), round 3 (the retraction itself false — 12 `library()` files exist). **The fix is to grep every artifact for the claim, not to edit the cited line.** The final pass was done that way; `grep -ri renam` now returns only retractions, denials, and unrelated uses.

## Standing caveat

The robots.txt STOP gate on `pine-facade.tradingview.com` (`User-agent: * / Disallow: /`) fired and was **overridden by explicit user instruction** ("Pass the robot.txt file"). ToS and account-ban risk sit with the user, who took that call knowingly. Rate limiting was kept in force throughout (`DOWNLOAD_DELAY = 5`, 1 concurrent request per domain — except during the operator error above). `ROBOTSTXT_OBEY` is disabled **only** in the spider's `custom_settings`; `settings.py:22` remains `True`. Full detail in `00-manifest.md`.
