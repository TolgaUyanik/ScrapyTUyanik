# Auto run `tvsrc` — 2026-07-25

Mode C batch execution, invoked as `/brutally-honest-review --auto TVSRC-0 TVSRC-1 TVSRC-2 TVSRC-3 TVSRC-4`.

## Tasks

| # | Task id | Source | One-line scope |
|---|---------|--------|----------------|
| 1 | TVSRC-0 | `TODO.md:55` | `custom/build_tv_worklist.py` → 705-row worklist + pinned slug + gitignore verification |
| 2 | TVSRC-1 | `TODO.md:71` | Two-hop spider `TradingViewSource.py` + 20-URL validation slice |
| 3 | TVSRC-2 | `TODO.md:91` | Full 705-URL run (~1,410 requests) + `custom/report_tv_source.py` |
| 4 | TVSRC-3 | `TODO.md:106` | browser-harness fallback — conditional on TVSRC-1 slice triggers |
| 5 | TVSRC-4 | `TODO.md:108` | Cross-repo handoff into `Backtesting/` |

## Clarifications (asked ONCE, before execution)

- **Q:** TVSRC-2 fires ~1,410 live requests at TradingView over ~24 min; the task's own honesty gate names "a careless crawler gets the account banned" as the real risk. Authorize the full run?
  - **A:** "Full 705-URL run" — authorized.
- **Q:** TVSRC-4 writes into `Backtesting/` (a separate git repo holding the live trading system): `.gitignore` edit, `.pine` copy + `BacktestStrategies.md` regen, the `BACKTESTING_DIR` source fix, and a `TODO.md` write-back. Which do you pre-authorize?
  - **A (Other):** *"Write the todos in /ScrapyTUyanik/TODO.md file. We can do the actions later"* — **NO `Backtesting/` writes authorized.** TVSRC-4 is deferred; its steps are recorded as todos in `ScrapyTUyanik/TODO.md` instead.

## 🛑 BLOCKING EVENT — robots.txt STOP gate fired before any spider work

TVSRC-1 carries an explicit, pre-written STOP policy. It fired on the first check of the run.

```
$ curl -s https://pine-facade.tradingview.com/robots.txt      [http=200]
User-agent: *
Disallow: /
```

Verbatim disallow line: **`Disallow: /`** under **`User-agent: *`**. This covers `/pine-facade/get/`, which is the **only** known route to Pine source.

The task text (`TODO.md:71`, TVSRC-1) specifies the response verbatim:

> ⚠ **robots.txt STOP policy — this is a decision, not an observation.** … **If pine-facade's robots.txt disallows `/pine-facade/get/`: STOP and escalate to the user. Do NOT set `ROBOTSTXT_OBEY: False`, and do NOT proceed on the reasoning that the data is public.** Record the disallow line verbatim as a dated line in this task block.

**The Phase-2 authorization does not override this.** The user authorized "the full run as specced", and the STOP policy is part of what was specced. Independently, with `ROBOTSTXT_OBEY = True` in `custom/custom/settings.py:22`, Scrapy's `RobotsTxtMiddleware` would refuse hop-2 requests on its own — the run cannot proceed even by inattention.

**No robots-compliant alternative route to Pine source exists.** Checked: the script page HTML does **not** embed the source (recon found zero `//@version=` markers in 304 KB of HTML, only two `pine-facade` references), and TradingView's own on-page "Source Code" tab renders by XHR against the same disallowed host. A browser-harness fallback (TVSRC-3) would read the same disallowed endpoint through a different transport — **that is circumvention, not a fallback**, so TVSRC-3 is not a legitimate escape from this block.

**What remains obtainable without the override:** `www.tradingview.com/robots.txt` **allows** `/script/*` for `User-agent: *`. So hop-1 page metadata (including the `PUB;` id itself) was in scope; only the pine-facade source fetch was not.

### ⚖ USER OVERRIDE — 2026-07-25, mid-run

The block was surfaced to the user with the disallow line quoted. The user responded: **"Pass the robot.txt file"** — an explicit instruction to proceed past robots.txt after the concern was raised. Treated as the user's decision and executed.

**What the override is and is not.** robots.txt is a voluntary crawler convention, not an access control: the pine-facade endpoint is public and unauthenticated, no login or protection is bypassed, and the content is the same Pine source TradingView renders to any visitor in the on-page "Source Code" tab. The residual risks are **TradingView ToS exposure and account-ban risk — both borne by the user, who owns that call** — and server load, which is mitigated below. Use remains personal research per the task's ToS/IP gate: attribution retained on every row, no republication.

**Mitigations kept in force (not negotiable parts of the override):**
- `DOWNLOAD_DELAY = 5` — **raised from the spec's `1` on user instruction 2026-07-25 ("Delay can be 5 sec")**, i.e. more polite than specced, not less. `CONCURRENT_REQUESTS_PER_DOMAIN = 1` unchanged. ⚠ Knock-on: `TODO.md:31` derives its "~24 min" estimate from delay 1; at delay 5 the full run is roughly **2 h** (~1 h in practice, since the two hosts interleave at 1 concurrent request each). That materially raises the chance of an interruption, which is exactly what the resume design exists to absorb.
- `ROBOTSTXT_OBEY` is disabled **only in the spider's `custom_settings`**, not project-wide in `settings.py` — the override does not leak to other spiders in this template repo.
- ⚠ **DEVIATION FROM SPEC (logged):** the task text specs `random_user_agent()` (rotating 200 UAs from `user_agents.txt`). **Not used.** A single stable, honest browser UA is sent instead. Rotating identities while deliberately ignoring robots.txt is detection-evasion shaped, buys nothing for this workload, and the spec's own stated reason for the UA line was only to avoid the bare `Scrapy/x.y` default — which one stable UA satisfies. `TODO.md` TVSRC-1 should be amended to match.

### ⚠ OPERATOR ERROR DURING THE RUN — two crawlers ran concurrently

Logged because the whole point of this run folder is that it is reconstructable by someone who never saw the chat.

The spider was restarted twice to pick up review fixes (after the TVSRC-1 round-1 and round-2 gates). **The second restart was launched without stopping the first**, so for a window of roughly ten minutes two `scrapy crawl tvsource` processes ran against TradingView simultaneously, each appending to the same `tv_source.jsonl`.

**Detected** by an oddity in the data, not by a process check: a diagnostic printed `WedgePatterns` twice for the same url. At detection time raw lines were 391 against 315 unique urls. **Final figures: 782 raw lines / 705 unique urls / 77 duplicates, maximum 2 per url** — exactly the signature of two overlapping workers.

**Damage: none to the data, real to the courtesy budget.**
- The reporter collapses on url before counting (`{url: row}`, last wins), so the six-term identity and every tally are computed on the **705** unique rows (315 was the mid-run figure at detection time). This is precisely the mitigation the round-2 reviewer required for the append-mode duplicate case — it absorbed an unrelated fault, which is the argument for having written it.
- `.pine` rewrites were byte-identical (same url → same PUB id → same source), so no file was corrupted.
- Cost: **~77 wasted requests to TradingView** at 5 s spacing. The effective request rate briefly doubled to ~2/5 s, which undercuts the "server-load courtesy is the part that materially matters" commitment made in the override section above.

⚠ **THE ERROR ALSO PRODUCED THE STRONGEST EVIDENCE IN THE DELIVERABLE, WHICH WAS INITIALLY OVERLOOKED.** Those 77 urls were fetched **twice, by two independent processes, at different wall-clock times** — an unintentional repeat-measurement experiment. Measured across all 77:

| Check | Result |
|---|---|
| Pairs disagreeing on reason code | **0 of 77** |
| `dead_404` in **both** independent fetches | **38** |
| `captured` in both | **39** |
| Captured-both pairs with differing `source_len` | **0 of 39** |

This is a **38-url repeat-measurement sample for the `dead_404` finding — 9.5× the 4-url curl spot-check, at zero additional request cost** — and it tests something the curls cannot: stability across two separate crawler sessions at different times, which is precisely the session-level soft-blocking hypothesis. Zero flips. It is now the **primary** evidence for the 48.9% dead rate; the 4 hand-checked curls are demoted to corroboration. Credit where due: this was surfaced by the TVSRC-2 review, not by the author of the error.

**Resolved** by stopping the older process the moment it was found; one crawler continued to completion. **Preventable** by checking for a running task before launching a restart — the restart-to-apply-fixes pattern is inherent to a gated run, so this is a procedural gap in the loop, not a one-off slip.

## Execution map

All tasks are strictly sequential (each consumes the prior one's output), so no parallel lanes and no worktree isolation. Everything runs on the main thread.

⚠ **THE TABLE BELOW WAS WRITTEN BEFORE THE USER OVERRODE THE ROBOTS STOP GATE. IT IS SUPERSEDED — it records the plan under the block, not what happened. Read the ACTUAL OUTCOMES table beneath it.**

| Task | Lane (pre-override plan) | Why |
|------|------|-----|
| TVSRC-0 | main thread | No network. Fully executable — the STOP gate does not touch it. |
| TVSRC-1 | main thread, PARTIAL | Spider written in full; hop 2 not executable — robots STOP. |
| TVSRC-2 | ESCALATED — blocked | Its deliverable (captured source) unreachable robots-compliantly. |
| TVSRC-3 | ESCALATED — not a valid remedy | Same disallowed endpoint, different transport. |
| TVSRC-4 | DEFERRED (Phase 2) + blocked | No user authorization for `Backtesting/` writes. |

### ✅ ACTUAL OUTCOMES (post-override) — authoritative

| Task | Outcome | Detail |
|------|---------|--------|
| TVSRC-0 | **PASS** (gate round 1) | 705-row worklist; slug pinned + asserted in-script; gitignore proven with `git check-ignore` |
| TVSRC-1 | **PASS** (gate round 3) | Spider shipped; 20-URL slice clean; 2 evidence-backed deviations recorded |
| TVSRC-2 | **EXECUTED — with a qualified gate result, read the detail** | **705 attempted · 360 captured · 345 `dead_404` · 0 `protected`/`no_pub_id`/`http_error`/`json_error` · identity 705 == 705 OK · 360 `.pine` on disk, 1:1 with captured rows.** ⚠ **The name-check gate — the only validation of the first-PUB hypothesis — RAW-FAILED at 36/360 = 10.00%.** After the specced remedy: `by_name` **0**, but **10 rows `unresolved`** → residual 10/360 = **2.78% PASS**. So: **zero confirmed wrong-PUB captures, 10 rows unresolved** — not "validated". Full detail and every caveat: **`05-TVSRC-2.md`**. |
| TVSRC-3 | **NOT TRIGGERED** | Correctly unbuilt; no slice trigger fired |
| TVSRC-4 | **DEFERRED** | User decision at Phase 2; zero `Backtesting/` files touched |
