# TVSRC-4 — Hand the output to `Backtesting` TVLIB-2

Source: `TODO.md:108`. Severity in spec: MAJOR.

## Outcome: **DEFERRED — not started. Nothing in `Backtesting/` was touched.**

This is a user decision recorded at Phase 2, not a failure and not an escalation-on-cap.

## The Phase-2 exchange

TVSRC-4 writes into `Backtesting/` — a **separate git repo holding the live trading system**. Mode C puts cross-repo mutation outside auto scope without explicit pre-authorization, so it was raised in the one permitted question round, itemized into the four distinct writes:

1. Edit `Backtesting/.gitignore`
2. Copy `.pine` + regenerate `BacktestStrategies.md`
3. Fix the `BACKTESTING_DIR` bug in two live source files
4. Write back to `Backtesting/TODO.md`

**User answer (Other):** *"Write the todos in /ScrapyTUyanik/TODO.md file. We can do the actions later"*

No option was selected. Read conservatively — the smaller blast radius, per Mode C's tiebreak — that is **no authorization for any of the four**, plus an instruction to record the work as todos locally.

## What was done instead

The four steps were written into `ScrapyTUyanik/TODO.md` as a nested checklist under TVSRC-4 (`TVSRC-4a` … `TVSRC-4d`), each carrying its file:line references, its gate, and its acceptance criterion, so the deferred work is executable later without re-deriving anything.

**Verified untouched:** `Backtesting/.gitignore`, `Backtesting/BacktestStrategies.md`, `Backtesting/scripts/utils/parse_pinescript.py`, `Backtesting/scripts/utils/extract_strategy_rules.py`, `Backtesting/TODO.md`.

## One finding worth carrying forward

TVSRC-4c's warning — *"`<title>` MUST be the CSV `title`, NOT pine-facade's `scriptName`"* — was written as a precaution when the spec was drafted. **This run turned it into a live hazard.**

The name-check gate found **36 rows where facade `scriptName` differs from the CSV title**. ⚠ **That is NOT "renamed", and an earlier version of this paragraph said it was — retracted.** The gate established `by_name` **0** and **zero confirmed renames**; 26 of the 36 were shown *not* to be renames (2 matched the file's own `shorttitle`, 24 were single-id pages), and the other **10 are `unresolved` — nothing was established about them either way**. The two worked examples this paragraph previously offered are both refuted by our own artifacts: `iNpKsdYt.pine` opens `indicator(title="Scout Regiment - MACD", shorttitle="SCTI-MACD")`, so the CSV title *is* that file's own `shorttitle` — a publication-name-vs-`title=` field mismatch, verdict `title_match`; and `7H1DGxKV` (`ORB…`) is one of the 10 `unresolved`.

**The operative fact for TVSRC-4c is unchanged and does not depend on renames:** the two name fields genuinely differ on real rows, so using `scriptName` in the markdown headers would silently match **zero** rows in `StrategyLibrary_rules.csv` and report a clean 0 with no error. The note is strengthened in TODO.md accordingly.

⚠ This retraction is the **third** occurrence of the same defect in this run — a claim corrected in one artifact and left standing in another. See `05-TVSRC-2.md` for the full pattern; it is the single biggest process lesson here.

## Verdict

No implementation, so no review gate. **DEFERRED (needs user)**, not ESCALATED — the batch was not blocked by a review cap; the user chose to hold this step.

Files touched: `ScrapyTUyanik/TODO.md` (deferred checklist added). Zero files in `Backtesting/`.
