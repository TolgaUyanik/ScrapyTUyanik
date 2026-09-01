# TVSRC-3 — browser-harness fallback

Source: `TODO.md:106`. Severity in spec: MINOR, **conditional — "do not pre-build"**.

## Task text (condensed)

Only build this if a TVSRC-1 slice trigger fires. Triggers, any one:
1. **>2 of 20** slice urls fail with a **non-404** HTTP error (404s are `dead_404`, an expected outcome, not a failure);
2. **0 of 20** match `PUB_RE` (TradingView changed its embed);
3. a Cloudflare / JS interstitial appears.

## Outcome: **NOT TRIGGERED — correctly left unbuilt.**

Measured on the 20-URL validation slice:

| Trigger | Threshold | Measured | Fired? |
|---|---|---|---|
| non-404 HTTP errors | >2 of 20 | **0** (`http_error` count 0; the 5 failures were all 404 → `dead_404`) | no |
| `PUB_RE` misses | 0 of 20 match | **15 of 20 matched** (`no_pub_id` count 0; the other 5 never reached the regex, being 404s) | no |
| Cloudflare / JS interstitial | any | none — 30×200 + 5×404, no challenge pages, no JS wall | no |

Confirmed again at scale mid-run: across 349 unique rows the tallies remain `http_error = 0`, `json_error = 0`, `no_pub_id = 0`. The plain-HTTP path is holding, so the fallback has nothing to fall back from.

## ⚠ A note the spec did not anticipate, worth recording

The robots.txt STOP gate fired on `pine-facade.tradingview.com` (`User-agent: * / Disallow: /`). Before the user overrode it, TVSRC-3 was briefly considered as a route around the block. **It is not one, and this should stay written down:** browser-harness would read *the same disallowed endpoint over a different transport*. That is circumvention, not a fallback. TVSRC-3's triggers are about the plain-HTTP path *breaking*, never about a policy answer being inconvenient. The block was resolved by asking the user, which is what the STOP policy prescribes — not by switching tools.

## Verdict

No implementation, so nothing to review; the gate is recorded as N/A rather than PASS. Leaving TVSRC-3 unchecked in `TODO.md` is the correct end state — the trigger conditions remain live for any future run.

Files touched: none.
