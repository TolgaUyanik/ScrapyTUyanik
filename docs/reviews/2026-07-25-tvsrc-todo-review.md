# Brutally Honest Review — TVSRC task block

**Date:** 2026-07-25
**Target:** `ScrapyTUyanik/TODO.md` (task block `TVSRC`, all 5 sub-tasks + recon table)
**Type:** design / spec
**Verdict:** REVISE
**Findings:** 6 CRITICAL · 9 MAJOR · 3 MINOR · 0 NIT
**Reviewer:** independent read-only subagent (fresh context, no authorship attachment)

---

## What survived the audit

Recorded first so the revision does not "fix" things that are already correct:

- **762 rows / 705 unique URLs** — re-counted independently. Correct.
- **"Same dataset" as `Backtesting/datastore/source/StrategyLibrary.csv`** — the URL *sets* are identical, zero symmetric difference. Earned, not spin.
- **Every TVLIB claim** checks out verbatim against `Backtesting/TODO.md:34-46`: TVLIB-0 as the storage decision, TVLIB-1 speccing the scrape, the missing `BacktestStrategies.md` root cause, the 83/762 = 10.9% baseline, the 2026-07-24 scope lock.
- **The `BACKTESTING_DIR` bug is real** — `parse_pinescript.py:21` and `extract_strategy_rules.py:44`, one `dirname` short.
- **`gen_board.py:23-24` genuinely only reads `Backtesting/TODO.md`** — the "no board tags here" claim is correct.

---

## Findings

### CRITICAL

- **`TODO.md:20` — recon table, "URL shape" row** — Claim `` `/script/<8charId>-<slug>/` — all 762 `` is **false**, and it sits under a "DO NOT RE-DERIVE" banner so a fresh session will trust it. Measured: **103 of 705 unique URLs have no slug segment at all** (`.../script/01DBv9uI/`, `.../script/2Bt3ns4g/`) — 14.6% of the corpus with nothing to name a file after.
  - Fix: restate as `` `/script/<8charId>[-<slug>]/` — 705/705 carry an 8-char id; **602 have a trailing slug, 103 do not**. ``

- **`TODO.md:30`, `TODO.md:32` — `slug` is never defined** — It is a column in `tv_urls.csv` and the primary key of the entire Pine filesystem, and the doc never says how it is derived. Both obvious readings break: "text after the 8-char id" is **empty for 103 URLs** and **collides in 12 groups** (`Trent-Finder-V3`, `Midnight-30min-High-Low` ×3, `Pre-Market-High-and-Low`, `PSX-OBV-Divergence-Labels-1D`, …), silently overwriting `.pine` files. The CSV `title` is not filesystem-safe. **Data loss is silent** — JSONL still hits 705 rows while `datastore/pine/` holds fewer files.
  - Fix: pin it in TVSRC-0 — `slug = url.rstrip('/').rsplit('/', 1)[-1]` (whole final segment, id included). Verified on the real data: **705/705 unique, 0 case-insensitive collisions on NTFS, max 70 chars, all ASCII**, chars limited to `[A-Za-z0-9_%-]`. Three URLs carry percent-escapes (`uY9EBtHq-RSI-1H-afi%C8%99at-pe-3M`) — keep them escaped, do **not** `unquote`. Add acceptance: `len(set(slugs)) == 705`.

- **`TODO.md:34` — "the five counts sum to 705" is unsatisfiable** — Two disjoint sets of five exist in the task and neither works. Printed counts are `attempted / captured / protected / dead_404 / failed`, but `attempted` is 705 by definition so those five can never sum to 705. Reason codes are `dead_404 · protected · no_pub_id · http_error · json_error` — those sum to the **failure** set, because `captured` is not among them. Either reading leaves the gate impossible and the session will fudge it.
  - Fix: `captured + dead_404 + protected + no_pub_id + http_error + json_error == 705`, with `attempted == 705` reported separately. Add a priority ladder, because the codes are **not disjoint**: `no_pub_id` (hop-1) > `dead_404` (hop-2 HTTP 404) > `http_error` (any other non-2xx) > `json_error` (2xx, unparseable) > `protected` (parsed, `scriptAccess != open_no_auth`) > `captured`. First match wins.

- **`TODO.md:30` — the `.gitignore` fix does not work** — Git anchors a pattern containing a mid-string slash to the `.gitignore`'s own directory, so a root-level `datastore/pine/` entry will **not** match `custom/datastore/pine/`, which is where files actually land (Scrapy runs from `custom/`). The ToS/IP tripwire the task loudly flags stays wide open. Compounding: `tv_source.jsonl` matches **no** existing rule — `*.jl` does not match `.jsonl`, `*.json` does not match `.jsonl`, and `testfolder/*` is root-anchored so it misses `custom/testfolder/`.
  - Fix: specify exact unanchored lines — `**/datastore/pine/`, `*.pine`, `*.jsonl`. Acceptance: `git status --porcelain` after a run shows zero untracked `.pine` / `.jsonl`.

- **`TODO.md:38` — TVSRC-4 walks the same tripwire at the destination, silently** — `Backtesting/.gitignore` is `*.csv` + `!datastore/source/*.csv` with **no `.pine` rule**; `datastore/source/` is deliberately tracked. Executing TVSRC-4 as written **commits ~700 third-party Pine files into the Backtesting repo** — precisely the outcome TVLIB-0 exists to prevent and that TVSRC-0 spends a paragraph guarding against upstream.
  - Fix: add a gate before the copy step — "add `datastore/source/pine/` to `Backtesting/.gitignore` and verify with `git check-ignore -v datastore/source/pine/x.pine` BEFORE copying a single file." State as a gate, not a note.

- **`TODO.md:13` vs `TODO.md:38` — direct contradiction** — Line 13: "TVLIB-0 (storage decision) is **answered by TVSRC-0 below**." Line 38: "Copy … to **whatever path TVLIB-0 settles on**" — i.e. still open. Both cannot be true. A fresh session running TVSRC-4 has no destination, invents one, then marks TVLIB-0 `[x]` for a decision it just made off-spec.
  - Fix: decide it here. TVSRC-0 answers TVLIB-0 for the Scrapy side; state the Backtesting destination explicitly as `Backtesting/datastore/source/pine/<slug>.pine` and delete "whatever path TVLIB-0 settles on".

### MAJOR

- **`TODO.md:38` — "point `parse_pinescript.py` at it and re-run" understates the only real code change** — `parse_pinescript.py:23,505` reads **one markdown file** (`BacktestStrategies.md`) via a single `open()` and parses Pine blocks out of it. It cannot consume a directory of `.pine` files. This is not a constant edit; it is either a new directory-walk ingest or a regeneration of `BacktestStrategies.md`. Neither is specced → the handoff stalls or gets improvised.
  - Fix: pick one and write it down. Cheapest — add a TVSRC-4 sub-step: `custom/pine_to_md.py` (~15 lines) concatenates `datastore/pine/*.pine` into `Backtesting/BacktestStrategies.md` in the block format the parser already expects (cite the parser's regex), leaving the parser unchanged apart from the `BACKTESTING_DIR` fix.

- **`TODO.md:32` — no encoding specified, on a cp1254 box** — Python's default `open()` codec here is cp1254 (proven this session by a `UnicodeEncodeError: 'charmap' codec … cp1254`). Pine sources routinely carry Turkish/Cyrillic/CJK comments and em-dashes. The run crashes or mojibakes hundreds of URLs in, and resumability then treats corrupt rows as done.
  - Fix: contract line — every `open()` in the spider, `build_tv_worklist.py`, and `report_tv_source.py` passes `encoding='utf-8'` explicitly; `.pine` written `newline=''`/LF; JSONL uses `json.dumps(..., ensure_ascii=False)`. Acceptance: at least one captured `.pine` with a non-ASCII byte round-trips.

- **`TODO.md:30` vs `TODO.md:32` — "one row per attempted URL including failures" is not achievable by the described flow** — Rows are only written in the hop-2 callback. The `no_pub_id` case never reaches hop 2 — and the doc's own "Wrong id trap" row (line 25) guarantees it happens. Same for a hop-1 HTTP error. The run silently loses rows and the sum-to-705 gate fails for a reason nobody will diagnose.
  - Fix: spell out in TVSRC-1 — "if hop-1 yields no `PUB;` match, or returns non-2xx, `yield` a terminal JSONL row immediately (`pub_id=None, source_available=False, error='no_pub_id'|'http_error'`) and do **not** issue hop 2." Add `errback=` on both Requests so DNS/timeout failures produce a row instead of vanishing into Scrapy's log.

- **`TODO.md:32` — resumability rule can never converge** — "skip urls already logged with `error is None`" means every terminal-but-failed row is retried on **every** restart: a `dead_404` is dead forever, a `protected` is protected forever, yet both carry a non-None `error`. On a run the doc says "WILL be interrupted at least once", this re-burns the whole failure set each resume. Worse, the acceptance test only exercises the success path, so the bug **passes the gate**.
  - Fix: "skip urls whose logged `error` is in the TERMINAL set `{None, 'dead_404', 'protected', 'no_pub_id'}`; retry only `{'http_error', 'json_error'}`." Extend acceptance: "kill mid-run, restart, assert request count on resume equals `705 − len(terminal rows)`."

- **`TODO.md:15-28` — the recon table mixes three evidence grades under one "DO NOT RE-DERIVE" banner** — Row 19 (762/705) is a full census and earns its confidence. Row 24 ("first in document order = the target script") is **n=1** — one page, `kGSi6ONc`. Row 28 (404 rate) is **n=6**. Row 20 is flatly wrong. A fresh session cannot tell which rows are safe to build on, and the banner tells them not to check.
  - Fix: add an `Evidence` column — `census n=705` / `n=1 page` / `n=6 sample` / `docs`. Demote row 24 from fact to "**WORKING HYPOTHESIS (n=1)**, validated at scale by the TVSRC-2 name-check gate."

- **`TODO.md:34` + `TODO.md:24` — the 5% mismatch gate names a trigger but no remedy** — It is the *only* validation of an n=1 heuristic, and "TVSRC-1 needs fixing" says fixing **how**? No alternative rule is named, and longest/last are already ruled out at line 24. A session that trips this gate invents a heuristic or quietly lowers the threshold.
  - Fix: name the fallback in TVSRC-2 — "on mismatch, re-resolve by fetching ALL `PUB;` ids on the page and selecting the one whose `scriptName` best matches the CSV `title` (normalized Levenshtein); log `pub_selection='by_name'` on those rows." Define the normalization now (casefold, strip non-alphanumerics, collapse whitespace) so the mismatch number is reproducible.

- **`TODO.md:36` — TVSRC-3's trigger is both mistimed and self-contradictory** — (a) It is framed as preventing a failed run, but is only computable **after** TVSRC-2 has burned all 1,410 requests. (b) The 5% threshold collides with the doc's own line 28 (1 dead 404 in 6 ≈ 17%), and `HTTPERROR_ALLOWED_CODES = [404]` leaves it undefined whether a dead script is `dead_404` or `http_error` — under the wrong reading TVSRC-3 fires on a healthy run.
  - Fix: move the trigger to TVSRC-1's 20-URL slice — "if >2 of 20 fail with a non-404 HTTP error, or 0 of 20 match `PUB;`, stop and go to TVSRC-3" — and restate as "`http_error` (404s excluded — those are `dead_404`) > 5%".

- **`TODO.md:32` — the robots.txt branch is the one genuinely unowned decision in the spec** — "confirm `ROBOTSTXT_OBEY = True` does not block it, and if it does, record that fact" — record it and then **what**? Ship nothing? Set `ROBOTSTXT_OBEY: False` anyway? The operator is handed a policy question with no policy.
  - Fix: one line — "if pine-facade robots.txt disallows `/pine-facade/get/`, **STOP and escalate to the user** — do not disable `ROBOTSTXT_OBEY`. Record the disallow line verbatim in this task block."

- **`TODO.md:30`, `:32`, `:34` — every path is cwd-relative and the cwd is never stated** — `../../TradingViewStrategies.csv` resolves only from `custom/`; run as `python custom/build_tv_worklist.py` from the repo root it resolves to `d:/AwakenAnalytics/PersonalProjects/TradingViewStrategies.csv` and dies. Separately **`testfolder/` is at the repo ROOT, not under `custom/`** — the repo's own `CLAUDE.md:20` writes it as `../testfolder/output.json`. So `testfolder/tv_source.jsonl` from a spider running in `custom/` creates a second, un-gitignored `custom/testfolder/`, and `report_tv_source.py` may read the other one. Two scripts, two directories, same name.
  - Fix: anchor on `__file__`, not cwd — `ROOT = Path(__file__).resolve().parents[1]` in `custom/build_tv_worklist.py`, then `ROOT.parent.parent / 'TradingViewStrategies.csv'`, `ROOT / 'custom' / 'datastore' / 'tv_urls.csv'`, `ROOT / 'testfolder' / 'tv_source.jsonl'`. State the canonical paths once in the storage contract; reuse verbatim in TVSRC-1/-2/-4.

### MINOR

- **`TODO.md:32` — the `PUB;` regex carries two unstated brittleness assumptions** — The class is lowercase-only, so an uppercase hex id yields a false `no_pub_id`; and it assumes `PUB;` appears unescaped in raw HTML, which is not guaranteed inside an embedded JSON blob (`PUB%3B`, `PUB\u003B`). One page was checked.
  - Fix: `r'PUB(?:;|%3B|\\u003[Bb])([0-9a-fA-F]{32})'`, capture group 1. Acceptance addition: on the 20-URL slice report `no_pub_id` count; if >2, re-derive the regex against saved HTML in `HTML_Files/` before the full run.

- **`TODO.md:32` — the spider's `name` attribute is never specified** — Only the `scrapy crawl tvsource` acceptance command implies it, and the repo has three inconsistent casings to copy from (`CustomSpider`, `custompw`, `CustomAPI`). An implementer plausibly names it `TradingViewSource` and the acceptance command fails.
  - Fix: state it — `class TradingViewSourceSpider(scrapy.Spider): name = "tvsource"`.

- **`TODO.md:40` vs `TODO.md:26` — the User-Agent is claimed but never wired** — Line 26 conditions the robots.txt verdict on "the browser UAs in `user_agents.txt`", but no sub-task requires using them. `Custom.py` — the stated fork base — sets no UA, so the fork ships the default `Scrapy/x.y (+https://scrapy.org)` for 1,410 requests. The robots verdict survives (Scrapy is not a named AI crawler, so `User-agent: *` applies), but the doc's own stated real risk is "a careless crawler gets the account banned".
  - Fix: add to TVSRC-1 — `headers={'User-Agent': random_user_agent()}` on every Request via `from custom.utils import random_user_agent`. One import, one kwarg. Then either the line-26 qualifier is true, or drop it.

---

## Summary

The recon that actually is a census holds up — 762 rows / 705 unique URLs re-counted independently, and the URL sets in `TradingViewStrategies.csv` and `Backtesting/datastore/source/StrategyLibrary.csv` have zero symmetric difference, so "same dataset" is earned rather than spin. Every TVLIB cross-claim checks out verbatim, the `BACKTESTING_DIR` bug is real at both cited files, and the `gen_board.py` exemption is correct. That is a rare amount of homework, and it makes the failures worse rather than better, because the doc spends that credibility stamping "DO NOT RE-DERIVE" on things it did not measure. "URL shape … all 762" is flatly false — 103 of 705 URLs have no slug — and the file-naming key `slug` is never defined, has 12 collision groups under the obvious reading, and is the primary key of the whole Pine filesystem. The sum-to-705 gate is unsatisfiable under either set of five it could mean. The gitignore fix the doc calls "required, not cosmetic" is anchored to the wrong directory and misses `.jsonl` entirely, and TVSRC-4 then carries the identical un-gitignored Pine files into a **tracked** `Backtesting/datastore/source/`. Line 13 says TVLIB-0 is answered; line 38 says it is still open. A fresh session gets stuck four separate times before the first HTTP request. The six CRITICALs are one or two lines of text each — fix them and this becomes a genuinely strong spec.
