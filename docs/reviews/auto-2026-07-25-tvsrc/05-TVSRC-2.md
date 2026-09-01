# TVSRC-2 — Full 705-URL run + coverage report

Source: `TODO.md:107`. Severity in spec: MAJOR. **Two review rounds — REVISE, then fixes.**

## Task text (condensed; full text in TODO.md)

Run to completion over all 705 worklist urls, then `custom/report_tv_source.py` writes the coverage report. Every row without source carries a reason code, applied under a priority ladder. Acceptance: the six-term identity sums to 705; `attempted` reported separately; the name-check gate stated with an explicit pass/fail against 5%, and on failure the by-name re-resolution run **and its new rate** reported; ≥10 captured `.pine` spot-checked by eye.

## Execution log

- Full crawl: `elapsed_time_seconds: 2866` (~48 min), `finish_reason: finished`, 470×200 + 232×404 on the final pass.
- Restarted twice mid-run to pick up TVSRC-1 gate fixes; resume skipped terminal rows correctly.
- ⚠ **Operator error**: two crawlers overlapped ~10 min → 77 duplicate rows. Logged in `00-manifest.md`. No data damage; the collapse absorbed it.
- ⚠ **Reporter bug, mine, found and fixed post-crawl**: the round-3 normalization fix re-read the JSONL without re-collapsing duplicates, inflating `attempted` to 782 and `captured` to 399 and breaking the identity. Consolidated into a single `load_rows()`; it is now the only counting path.

## Final results

| Code | Count | % |
|---|---:|---:|
| `captured` | **360** | 51.1% |
| `dead_404` | **345** | 48.9% |
| `protected` | 0 | — |
| `no_pub_id` | 0 | — |
| `http_error` | 0 | — |
| `json_error` | 0 | — |

```
captured + dead_404 + protected + no_pub_id + http_error + json_error == 705
360      + 345      + 0         + 0          + 0           + 0          = 705   OK
attempted == 705   (reported separately, not a term in the identity)
```

**360 `.pine` on disk, 1:1 with captured rows** — zero orphans, zero missing files, every `source_len` matches the byte length on disk, every `source_path` posix, every captured row carries `pub_id` and `script_name`.

Corpus: 3.0 M chars / 4 MB · `indicator` 319, `strategy` 29, `library` 12 · Pine v6 197, v5 153, untagged 10 · 231 files contain non-ASCII and round-trip clean · `scriptAccess` `open_no_auth` on all 360.

## Review round 1 — REVISE (3 CRITICAL, 5 MAJOR, 2 MINOR)

The review verified every count independently and could not break the arithmetic. It broke the **analysis**. Findings, condensed but not softened:

```
CRITICAL — the headline claim "26 first_sole, 10 first_best, 0 by_name, all 36 are renames"
  has ZERO artifact backing. `pub_selection` is the literal string 'first' on all 360 captured
  rows. A dry run writes nothing. There is no 05-TVSRC-2.md. tv_source_report.md terminates at
  "FAIL" and never mentions the remedy. "The entire conclusion that clears the failing gate
  exists only as vanished console output."

CRITICAL — report_tv_source.py's docstring calls facade `MAs` vs CSV `Zeefreaks Predator Mask
  Crypto` "a genuine library capture". It is not: the file opens
  `indicator(title="MAs", shorttitle="AOTS")`. The sibling `n7OXjXv8-ZFT-Classic.pine` is
  `indicator(title="MAs", shorttitle="ZFT Classic")` — shorttitle matching the CSV title exactly.
  "Three artifacts, three different stories."

CRITICAL — "one PUB id ⇒ mis-pick impossible" does not hold as implemented. (a) `len(ids) <= 1`
  folds ZERO ids in with one, so a degenerate response is recorded as proof of a rename.
  (b) The code never compares `ids[0]` against the captured `pub_id`. (c) The pick was made at
  crawl time; the count is made hours later, and no crawl-time HTML was retained.

MAJOR — `first_best` has no minimum-score floor and never prints the score. "First still scored
  highest among a candidate set where every candidate scores badly is not evidence the first is
  correct; it is evidence that none match."

MAJOR — "≥10 captured .pine spot-checked by eye" was not done. It is the only acceptance
  criterion that inspects SOURCE rather than names, and the remedy structurally cannot substitute
  for it — resolve_suspects.py compares strings and never opens a .pine.

MAJOR — the durable record says FAIL while the summary says validated, and the durable record is
  what TVSRC-4 and the next engineer will read.

MAJOR — 00-manifest.md's Execution map still states TVSRC-2 is "ESCALATED — blocked" and hop 2
  "not executed". A 705-url run with 360 captures then happened. Also 76 vs 77 duplicates.

MAJOR — 345 write-offs rest on 4 hand-checked urls: a 1.2% sample. "The decisive evidence is
  already sitting unused in your own data": the operator error double-fetched 77 urls from two
  independent processes at different times.

MINOR — `--apply` truncate-rewrites the append-only audit log, destroying the only forensic
  record of the operator error.
MINOR — TVSRC-0/-1/-2 all still `- [ ]`.
```

### Fixes applied — round 1

| Finding | Fix |
|---|---|
| C1 remedy unpersisted | Resolver rewritten + run with `--apply`; verdicts land in `testfolder/tv_source_verdicts.json`; report reads them; this file written |
| C2 false library claim | **Retracted in the docstring.** Replaced with the real lesson (below) |
| C3 elimination logic | `indeterminate` (0 ids) / `id_changed` (sole id ≠ captured) / `first_sole` (sole id == captured) now distinct verdicts; temporal caveat stated in the docstring |
| M4 no score floor | Floor at `BENIGN_RATIO` (0.80) → `unresolved`; score printed on every branch |
| M5 no eye-check | 10-file spot-check done (below) + a `needs_eye` structural flag added to the report |
| M6 FAIL vs validated | Report now prints the post-remedy verdict table, the residual rate, and its own PASS/FAIL; exit code follows the residual |
| M7 stale manifest | Pre-override table marked superseded; authoritative outcomes table added; 76 → 77 |
| M8 4-curl sample | Replaced by the 38-url repeat-measurement as primary evidence |
| m9 audit-log truncation | `--apply` writes a **sidecar**; the 782-line append-only log is left intact |
| m10 checkboxes | Marked in TODO.md |

### What C2 actually taught (more useful than the retracted claim)

**pine-facade's `scriptName` is the Pine `title=` argument. The CSV `title` is the TradingView *publication* name. Authors routinely set them differently.** `ZFT Classic` is literally its own file's `shorttitle`. So a name mismatch is not prima facie evidence of a mis-pick, and the raw SUSPECT rate measures publication-vs-title drift at least as much as capture error. The resolver now settles exactly this case **locally, with no request** (`title_match`), and it cleared 2 rows on the first pass.

⚠ **A first attempt at this retraction was ALSO wrong** and is itself corrected here: it read "no library capture was observed at n=360". **12 captures declare `library()`** — they are in this document's own corpus line above. All 12 classify `exact` (facade name == CSV title), including one named literally `ta`, a legitimately published library at `/script/RA2vGpkA-ta/` whose CSV title is `ta`. So `ta` is not a synthetic example either; it is a real, correctly-captured row.

The accurate claim is: **no WRONG-PUB library capture was observed at n=360** — every `library()` file present is the script its page publishes. The `CONTAIN_RATIO` length guard is therefore **precautionary, not empirically forced**: it costs nothing and still SUSPECTs the constructed `("ta", "Volume Delta + RSI Confluence Signals")` pairing, but it has not caught a real defect and no docstring claims it has.

## Name-check gate — raw, and after the remedy

Raw: `exact` 292 / `benign` 32 / **`SUSPECT` 36 = 10.00% → FAIL** vs 5%.

Remedy (`resolve_suspects.py --apply`, verdicts persisted):

| Verdict | n | Capture stands? | Basis |
|---|---:|---|---|
| `first_sole` | 24 | yes | page carries exactly ONE id **and it is the id we captured** → **no alternative existed at re-fetch time; no evidence of a mis-pick** |
| `title_match` | 2 | yes | CSV title matches the file's own `title=`/`shorttitle=` |
| `unresolved` | **10** | **unknown — flagged** | 2–4 ids present, best score 0.38–0.78, all under the 0.80 floor |
| `by_name` | 0 | — | no case where a different id scored higher |
| `id_changed` / `indeterminate` / `fetch_error` | 0 | — | — |

**Residual = 10/360 = 2.78% vs 5% → PASS.**

⚠ **TEMPORAL CAVEAT — applies to all 24 `first_sole` clearances, and it is why the basis column says "no evidence of a mis-pick" rather than "mis-pick impossible".** The pick was made against the crawl-time page; the resolver re-fetched **hours later**, and no crawl-time HTML was retained (`HTML_Files/` is empty). **"One id NOW" is not proof of "one id THEN"** — the recon's own n=1 evidence row shows pages that carry 2–3 ids. A future run must persist hop-1 HTML for any row the gate flags so this discriminator is replayable offline. Every verdict now persists the ids it was decided on (`id`, `captured`, `all_ids`), so the 24 clearances are at least re-derivable from the sidecar against the jsonl's `pub_id` with zero requests.

⚠ **The 10 `unresolved` rows all carry `winner_is_captured: true`** — i.e. even where several ids were present, the id we captured *was* the highest scorer; it simply failed to clear the 0.80 floor against the CSV title. That is weaker than a clearance and is correctly counted against the residual, but it is stronger than "no information".

⚠ **Recorded deviation from the spec:** TVSRC-2 says to log `pub_selection='by_name'`/`'first'` on the rows themselves. Verdicts are written to a **sidecar** (`testfolder/tv_source_verdicts.json`) instead, because writing into the jsonl means truncate-rewriting an append-only audit log whose duplicate rows are the only forensic record of the concurrent-crawler operator error. **`pub_selection` in the jsonl remains `'first'` on all 360 captured rows and is NOT the verdict field.**

⚠ **State this precisely, because the earlier version overstated it.** The correct claim is **"zero confirmed wrong-PUB captures, with 10 rows unresolved"** — *not* "the hypothesis is validated with zero counterexamples". The 10 `unresolved` rows are pages with multiple PUB ids where no candidate's name matches the CSV title well; they could be renames or mis-picks and the name evidence cannot separate them. Under the buggy first resolver these same 10 were reported as confirmed renames — the score floor is what turned a false clearance into an honest flag.

## Source-level spot-check (acceptance criterion, 10 files, seed=11)

All 10 sampled captures' Pine `title=` matches their CSV title **byte-for-byte**. Nothing truncated — a truncated column would hide divergence exactly where it would appear.

| slug | CSV title | pine `title=` == CSV title? | chars |
|---|---|---|---:|
| `K0ZLvoh6-London-Session-Market-Structure` | London Session & Market Structure | **YES** | 9827 |
| `QELKUdmG` | 焱鑫趋势追踪v2 | **YES** | 2479 |
| `5azMGL1V-RSI-Shift-Zone-ChartPrime` | RSI Shift Zone [ChartPrime] | **YES** | 4732 |
| `MpdaalO1-S-R-Zones-MTF-TechnoBlooms` | S&R Zones MTF (TechnoBlooms) | **YES** | 8987 |
| `8lfE3qMN-Zone-Shift-ChartPrime` | Zone Shift [ChartPrime] | **YES** | 3069 |
| `Tl4qmvt6-RSI-Overbought-Oversold-MTF` | RSI Overbought/Oversold MTF | **YES** | 3869 |
| `mSJEzF3l` | 20-Day SMA BIAS% | **YES** | 1071 |
| `Rvu0OCiX-EMA-Crossover-Visual-Setup-RS-Cl%C3%A1sico-Confirmado` | EMA Crossover Visual Setup (RS Clásico Confirmado) | **YES** | 1075 |
| `BDHiirPu-PulseLinesLib` | PulseLinesLib | **YES** | 2481 |
| `pNz3hmGc-AI-Breakout-Bands-Zeiierman` | AI Breakout Bands (Zeiierman) | **YES** | 6086 |

Regenerate with: `python - <<'PY'` reading `tv_source.jsonl` + `tv_urls.csv`, `random.seed(11)`, comparing `re.search(r'^\s*(?:indicator|strategy|library)\s*\(\s*(?:title\s*=\s*)?["\']([^"\']+)', txt, re.M)` against the CSV title.

Corpus-wide structural scan: only **4** captures have ≤4 non-comment lines, and 3 of those are legitimately simple scripts whose names match (`Alternate Hourly Highlight`, `First Trading Day of Week`, `Previous Close Label`). The fourth, `123 Toolkit` → `indicator("123")` / `plot(close)`, is a stub the author genuinely published.

⚠ **TVSRC-1's `> 200 chars` acceptance is wrong, not the data.** Two captures fall under it (173 and 177 chars) and both are complete valid scripts. The criterion assumed no trivial scripts exist on TradingView; they do. **This is a goalpost being corrected on evidence, and it is recorded here rather than quietly dropped** — the check should be "starts with `//` and parses a declaration", not a length.

The report now also emits a **`needs_eye`** section — 37 captures flagged as structurally trivial or having no name field matching the CSV title. That is a review queue, not a defect count.

## The 48.9% `dead_404` finding

345 of 705 urls return HTTP 404 at hop 1 (**zero** dead rows carry a `pub_id`, confirming all are hop-1).

**Primary evidence — 38-url repeat measurement, zero new requests.** The concurrent-crawler operator error fetched 77 urls **twice, from two independent processes, at different wall-clock times**:

| Check | Result |
|---|---|
| Pairs disagreeing on reason code | **0 of 77** |
| `dead_404` in both independent fetches | **38** |
| `captured` in both | **39** |
| Captured-both pairs with differing `source_len` | **0 of 39** |

This tests session-level soft-blocking, which a single curl batch cannot. Zero flips.

**Corroborating — 4 urls hand-checked individually:** 404 with *and* without full `Accept`/`Accept-Language` (not a header fingerprint) · 404 on the id-only `/script/<id>/` form with an **empty** `redirect_url` (not a stale slug) · a known-good control returned 200 in the same batch · 404s interleave with captures throughout emit order rather than forming a tail (not a block onset).

**Corroborating — distribution:** dead rate is near-uniform across id-only urls (55.3%) and slug urls (47.8%); median CSV position is similar for dead (377) and captured (337). No positional or url-form artifact.

⚠ **Honest limit:** none of this proves *why* the scripts are gone, only that the 404 is stable, intrinsic to the url, and not induced by our client. The `dead_404` label means "TradingView returns 404 for this url, reproducibly", which is what the reason code claims.

## Review round 2 — REVISE (6 MAJOR, 2 MINOR, 1 NIT)

```
MAJOR — resolve_suspects.py docstring says "VERDICTS (written to `pub_selection`)". Nothing is
  ever written to pub_selection; the collapsed JSONL still carries Counter({'first': 360}). The
  file points the next reader at the exact field round 1 caught as evidence-free.
MAJOR — every first_sole record is {"verdict":"first_sole","ids":1} — the id itself is not
  persisted. 24 of the 26 clearances, i.e. the entire difference between 10.00% FAIL and 2.78%
  PASS, rest on an assertion not checkable from any artifact without re-fetching 24 pages.
MAJOR — 05-TVSRC-2.md and the script state first_sole ⇒ "mis-pick impossible" as an absolute,
  contradicting the same script's temporal caveat 15 lines below. "Four artifacts, two different
  strengths of the one claim carrying the PASS."
MAJOR — TODO.md TVSRC-4c still reads "the name-check gate found a meaningful number of scripts
  RENAMED since the CSV snapshot". by_name is 0. "The round-1 CRITICAL claim surviving as the
  stated justification for a future task's design."
MAJOR — 00-manifest.md's "authoritative" outcomes table omits that the name-check gate raw-FAILED
  at 10.00%, that the PASS is a post-remedy residual, and that 10 rows are unresolved.
MAJOR — "No library capture was observed at n=360" is false. 12 captures declare library(),
  including RA2vGpkA-ta whose facade name and CSV title are both `ta`. "The paragraph written to
  discharge round-1 CRITICAL #2 replaced a false claim with a differently false one."
MINOR — needs_eye heading claims source-level signal; 34 of 37 rows are a name check.
MINOR — residual/exit computed from the sidecar with no coverage check against the suspect set.
NIT   — spot-check table truncates the `pine title=` column exactly where divergence would appear.
```

### Fixes applied — round 2

All nine applied. Verdicts now persist `id`/`captured`/`all_ids`; resolver re-run (**identical counts: 24/10/2**, ids independently reconcilable against the jsonl's `pub_id`); "mis-pick impossible" softened everywhere and the temporal caveat placed under the verdict table; TVSRC-4c rewritten; manifest table extended with the raw-FAIL→residual chain; the library claim corrected **again** (see above); `needs_eye` retitled and split; staleness check added; spot-check table de-truncated.

## Review round 3 (ROUND CAP) — REVISE (1 CRITICAL, 1 MAJOR, 1 MINOR, 1 NIT)

```
CRITICAL — 04-TVSRC-4.md:30 still reads "The name-check gate established that a meaningful share
  of scripts have been renamed by their authors since the CSV snapshot", with two examples both
  refuted by this repo's own artifacts: iNpKsdYt.pine opens
  indicator(title="Scout Regiment - MACD", shorttitle="SCTI-MACD") — the CSV title IS the file's
  own shorttitle, verdict title_match; and 7H1DGxKV is one of the 10 unresolved rows.
  "Round 1 died on cross-artifact disagreement; round 2 died on cross-artifact disagreement; the
  fix for round 2's disagreement created a new one. You fixed the sentence you were pointed at
  instead of the claim."
MAJOR — the staleness guard is INVERTED. On a stale sidecar it sets v = {}, so flagged = 0,
  residual = 0/360 = 0.00%, resid_gate = "PASS", exit 0. "It does NOT fall back to the raw gate as
  claimed... the guard produces exactly [the failure its own comment says it refuses], with a
  0.00% residual, which is worse than the unguarded behaviour." `if not v: CLEARS = ()` is dead code.
MINOR — 05-TVSRC-2.md's Outcome line says "round-2 gate pending" and round 2's findings appear
  nowhere in the run folder.
NIT   — TODO.md's OUTCOME block does not note that pub_selection was never written.
```

### Fixes applied — round 3

- **CRITICAL** → `04-TVSRC-4.md` rewritten; both refuted examples replaced with the honest framing; a cross-artifact grep for `renam` now returns only retractions, denials, and unrelated uses (BOM column, slug, redirect).
- **MAJOR** → guard rewritten to skip the residual entirely on a stale sidecar, leaving `resid_gate = None` so `effective` falls back to the raw gate. Dead `CLEARS = ()` deleted. **Proven both directions:** stale sidecar → no residual printed, `STALE SIDECAR` in the report, **exit 1**; good sidecar → residual printed, **exit 0**.
- **MINOR / NIT** → this section and the round-2 section added; `pub_selection` deviation clause added to TODO.md's OUTCOME block.

## Outcome

⚠ **ESCALATED — TVSRC-2 hit the Mode C three-REVISE round cap.** Rounds 1, 2 and 3 all returned REVISE. Every round-3 finding has been fixed and each fix verified by direct execution, **but no gate has re-reviewed those fixes** — per the cap rule the task escalates to the user rather than looping into a fourth round.

**State at escalation:** identity 705 == 705 OK · 360 `.pine` 1:1 with captured rows · residual gate PASS at 2.78% with 10 rows honestly flagged rather than falsely cleared · staleness guard proven in both directions · no surviving cross-artifact contradiction found by grep.

**The process lesson, stated plainly because it recurred three times:** a claim was corrected in the artifact the reviewer pointed at and left standing in another. Round 1 (`MAs` = "library capture"), round 2 (`TODO.md` fixed, `04-TVSRC-4.md` missed), round 3 (retraction #2 itself false). **The fix is to grep every artifact for the claim, not to edit the cited line** — which is now how the final pass was done.

Files touched: `custom/report_tv_source.py`, `custom/resolve_suspects.py`, `testfolder/tv_source.jsonl` (normalized), `testfolder/tv_source_verdicts.json` (new), `testfolder/tv_source_report.md`, `datastore/pine/*.pine` (360), `00-manifest.md`.
