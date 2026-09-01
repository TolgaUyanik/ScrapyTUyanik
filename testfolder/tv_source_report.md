# TVSRC-2 — TradingView Pine source coverage report

Worklist: **705** urls · rows logged: **705** · `attempted == 705` (reported separately, not a term in the identity)

## Reason-code tally

| Code | Count | % |
|---|---:|---:|
| `captured` | 360 | 51.1% |
| `dead_404` | 345 | 48.9% |
| `protected` | 0 | 0.0% |
| `no_pub_id` | 0 | 0.0% |
| `http_error` | 0 | 0.0% |
| `json_error` | 0 | 0.0% |

### Acceptance identity
```
captured + dead_404 + protected + no_pub_id + http_error + json_error == 705
360 + 345 + 0 + 0 + 0 + 0 = 705
OK
```

## Name-check gate (validates the n=1 first-PUB hypothesis)

Captured rows compared: **360**

| Band | Count | Meaning |
|---|---:|---|
| `exact` | 292 | normalized names identical |
| `benign` | 32 | containment (author prefix/suffix) or difflib ratio >= 0.8 (version bump) |
| `SUSPECT` | 36 | **wrong-PUB signal** |

SUSPECT rate: **10.00%** vs threshold 5% -> **FAIL**

### Post-remedy resolution (`resolve_suspects.py --apply`)

| Verdict | Count | Capture stands? |
|---|---:|---|
| `title_match` | 2 | yes |
| `first_sole` | 24 | yes |
| `unresolved` | 10 | **needs review** |

Raw SUSPECT **36/360 = 10.00% FAIL** → resolved as **26 cleared / 10 flagged**.

**Residual rate = 10/360 = 2.78% vs 5% → PASS**

⚠ `cleared` means *no evidence of a mis-pick*, established by elimination (sole id) or by the CSV title matching the file's own `title=`/`shorttitle=`. It does **not** mean the script's behaviour was verified — see `needs_eye`.

### SUSPECT rows (raw, pre-remedy)

| slug | facade scriptName | CSV title |
|---|---|---|
| `7H1DGxKV-ORB-Range-Indicator-with-Fibonacci-Targets` | ORB & Full Extended Range Indicator | ORB Range Indicator with Fibonacci Targets |
| `XFStl5Pg` | SMA Highlight + Thick MACD Arrows + MACD Cycle Zones (Peak Precision) | SMA Highlight + MACD Crossover Arrows |
| `bzZIooYd` | Kassa 30 (dezente Linien mit weiter links gesetzten Labels) | Kassa 30 70 90 Eröffnung |
| `itrqFcIl` | Long and Short Strategy with RSI, ROC, MA Selection, Exit Visualization, and Strength Indicator | Long and Short Strategy with Multi Indicators [B1P5] |
| `M7opHh7K-Weekly-Change-Screener-5-Sell-Threshold` | 15-Min Chart, 7-Day High-Low Signal | Weekly % Change Screener (5% Sell Threshold) |
| `iNpKsdYt` | Scout Regiment - MACD | SCTI-MACD |
| `JRqtd0Zr-AO-AC-Zones-Log-Price` | Log‑Scaled AO/AC Zones | AO/AC Zones (Log Price) |
| `8wXrFmYZ-Momentum-Reversal-Strategy` | long short automated trade AKC | Momentum Reversal Strategy |
| `dj78jmEN-Zeefreaks-Predator-Mask-Crypto` | MAs | Zeefreaks Predator Mask Crypto |
| `lyCTgr1L` | Intraday Combo Strategy [Stoch RSI + MACD + Supertrend + BB + ADX] | Intraday Combo Strategy HH |
| `lmCaTAPv` | Scout Regiment - K13 | SCTI-RSK |
| `9yxmTRPA-Multi-Timeframe-SMT` | Standalone SMT (Penta, Corrected) | Multi-Timeframe SMT |
| `WtaFZGLB` | PnL_EMA_TRACK12_PRO_3.7 | PnL_EMA_TRACK12_PRO_3.3_full_adjusted |
| `hZUbIp7I-Big-Candle` | Big Candle Up/Down Alert | Big Candle |
| `u3RhMjMd-Relative-Strength-Line-by-Ankit-Prajapati` | Relative Strength Line (0–100 Scale) | Relative Strength Line by Ankit Prajapati |
| `cBP2lt0d-RSI-Long-Only-with-Confirmed-Crossbacks` | RSI Long & Short Strategy | RSI Long Only with Confirmed Crossbacks |
| `3oS2DPqQ-Sessions-13-Zones-ValentijnJelte` | Sessions 13-Zones (UTC Based) | Sessions 13-Zones ValentijnJelte |
| `0sjcsPgM-Supply-Demand-Zones-Fixed-v3-Cross-YES-Only` | Supply/Demand Zones / Interval Time V2 | Supply/Demand Zones - Fixed v3 (Cross YES Only) |
| `O4apDjnm-Previous-Day-Levels-High-Low-Open-Close` | Previous Day + Premarket Levels (actualiza 16:30 NY) | Previous Day Levels (High, Low, Open, Close) |
| `28E07V1U-Prev-Candle-Quarters-MTF-Price` | Prev Candle Body Quarters V9 | Prev Candle Quarters (MTF) – % + Price |
| `L5AVnfam-Discord-Levels-Label-Toggle` | Discord Levels (Extended) | Discord Levels (Label Toggle) |
| `fUzq426Q-Previous-Candle-High-Low-Clean` | Before Previous Candle High/Low (Line Starting on Candle) | Previous Candle High/Low (Clean) |
| `Y50HrNyB` | EMA排列状态 + MACD零轴信号 [合并版] | 多维度市场分析指标 v2 (区间框选) |
| `rP6UBHNp-SPY-QQQ-VIX-Status-Table` | SPY, QQQ, VIX Table Status | SPY, QQQ, VIX Status Table |
| `57i9oK2t-Twin-Range-Filter-Buy-Sell-Signals` | 1H 20EMA | Twin Range Filter – Buy/Sell Signals |
| `18LGpqXT` | 瀑布线 | Waterfall Line (PBX indicator) |
| `29RV8RAj-PayBack-by-Catboy` | PayBack | PayBack by Catboy |
| `HwniNkOM-Nebula-by-Catboy` | Nebula | Nebula by Catboy |
| `eHu68rVD-Daily-EMA-21-34-50` | Daily EMA 21/34/55 (Matches Built-in) | Daily EMA-21/34/50 |
| `KULW7WSA` | THF Scalp & Trend + FVG + Ichimoku [Custom Colors 2] | THF Crossover and Trend Signals Golden & Death Cross with Volume |
| `n7OXjXv8-ZFT-Classic` | MAs | ZFT Classic |
| `hi9fLmaP-123-Toolkit` | 123 | 123 Toolkit |
| `R3y6mh9a-Improved-Weinstein-Stage-Analysis` | Enhanced Weinstein Stage Analysis - Institutional | Improved Weinstein Stage Analysis |
| `gjQ5aBFB-Volume-Bars-Shubhashish-Dixit` | Daily Volume + MA + Labels - Shubhashish Dixit | Volume Bars - Shubhashish Dixit |
| `j9FH2RoA-nikki-es-2m` | ES Order Flow Bubbles | nikki es 2m |
| `mZI09xFI-nikki-ES-2m` | ES Order Flow Bubbles | nikki ES 2m |


## `needs_eye` — review queue (name-field mismatch OR structurally trivial)

**37** of 360 captures flagged: **33 name-field mismatch** (≈ the SUSPECT band, since no `title=`/`shorttitle=` matched either) + **4 structurally trivial** (<=4 non-comment lines), overlaps counted once.

⚠ Only the structurally-trivial half is genuinely source-level; the name half is still a name check. Do not read this as 37 rows of new payload-level signal.

| slug | body lines | chars | pine title/shorttitle | CSV title |
|---|---:|---:|---|---|
| `hi9fLmaP-123-Toolkit` | 2 | 173 | 123 | 123 Toolkit |
| `QanK2qIs-Previous-Close-Label` | 3 | 378 | Previous Close Label | Previous Close Label |
| `73jeDsYt-First-Trading-Day-of-Week-Holiday-Safe` | 4 | 323 | First Trading Day of Week (Holiday Safe) | First Trading Day of Week (Holiday Safe) |
| `f59acFpu-Alternate-Hourly-Highlight` | 4 | 177 | Alternate Hourly Highlight | Alternate Hourly Highlight |
| `57i9oK2t-Twin-Range-Filter-Buy-Sell-Signals` | 6 | 311 | 1H 20EMA | Twin Range Filter – Buy/Sell Signals |
| `j9FH2RoA-nikki-es-2m` | 10 | 715 | ES Order Flow Bubbles | nikki es 2m |
| `mZI09xFI-nikki-ES-2m` | 10 | 698 | ES Order Flow Bubbles | nikki ES 2m |
| `dj78jmEN-Zeefreaks-Predator-Mask-Crypto` | 11 | 654 | MAs / AOTS | Zeefreaks Predator Mask Crypto |
| `hZUbIp7I-Big-Candle` | 11 | 1143 | Big Candle Up/Down Alert | Big Candle |
| `u3RhMjMd-Relative-Strength-Line-by-Ankit-Prajapati` | 12 | 890 | Relative Strength Line (0–100 Scale) | Relative Strength Line by Ankit Prajapati |
| `gjQ5aBFB-Volume-Bars-Shubhashish-Dixit` | 15 | 1264 | Daily Volume + MA + Labels - Shubhashish Dixit / Vol Bars by Shubh | Volume Bars - Shubhashish Dixit |
| `fUzq426Q-Previous-Candle-High-Low-Clean` | 18 | 1216 | Before Previous Candle High/Low (Line Starting on Candle) | Previous Candle High/Low (Clean) |
| `eHu68rVD-Daily-EMA-21-34-50` | 18 | 1154 | Daily EMA 21/34/55 (Matches Built-in) | Daily EMA-21/34/50 |
| `M7opHh7K-Weekly-Change-Screener-5-Sell-Threshold` | 20 | 1504 | 15-Min Chart, 7-Day High-Low Signal | Weekly % Change Screener (5% Sell Threshold) |
| `JRqtd0Zr-AO-AC-Zones-Log-Price` | 21 | 1184 | Log‑Scaled AO/AC Zones | AO/AC Zones (Log Price) |
| `cBP2lt0d-RSI-Long-Only-with-Confirmed-Crossbacks` | 21 | 1005 | RSI Long & Short Strategy | RSI Long Only with Confirmed Crossbacks |
| `18LGpqXT` | 26 | 1544 | 瀑布线 | Waterfall Line (PBX indicator) |
| `XFStl5Pg` | 41 | 2975 | SMA Highlight + Thick MACD Arrows + MACD Cycle Zones (Peak Precision) | SMA Highlight + MACD Crossover Arrows |
| `29RV8RAj-PayBack-by-Catboy` | 43 | 2341 | PayBack / PayBack v1.0 | PayBack by Catboy |
| `bzZIooYd` | 45 | 3921 | Kassa 30 (dezente Linien mit weiter links gesetzten Labels) | Kassa 30 70 90 Eröffnung |
| `8wXrFmYZ-Momentum-Reversal-Strategy` | 54 | 3997 | long short automated trade AKC | Momentum Reversal Strategy |
| `Y50HrNyB` | 58 | 4385 | EMA排列状态 + MACD零轴信号 [合并版] / 多维度分析 v5 | 多维度市场分析指标 v2 (区间框选) |
| `rP6UBHNp-SPY-QQQ-VIX-Status-Table` | 71 | 4225 | SPY, QQQ, VIX Table Status | SPY, QQQ, VIX Status Table |
| `O4apDjnm-Previous-Day-Levels-High-Low-Open-Close` | 81 | 5874 | Previous Day + Premarket Levels (actualiza 16:30 NY) | Previous Day Levels (High, Low, Open, Close) |
| `3oS2DPqQ-Sessions-13-Zones-ValentijnJelte` | 84 | 5100 | Sessions 13-Zones (UTC Based) | Sessions 13-Zones ValentijnJelte |
| `lyCTgr1L` | 87 | 5670 | Intraday Combo Strategy [Stoch RSI + MACD + Supertrend + BB + ADX] | Intraday Combo Strategy HH |
| `itrqFcIl` | 128 | 11708 | Long and Short Strategy with RSI, ROC, MA Selection, Exit Visualization, and Strength Indicator | Long and Short Strategy with Multi Indicators [B1P5] |
| `28E07V1U-Prev-Candle-Quarters-MTF-Price` | 154 | 7319 | Prev Candle Body Quarters V9 | Prev Candle Quarters (MTF) – % + Price |
| `L5AVnfam-Discord-Levels-Label-Toggle` | 201 | 11351 | Discord Levels (Extended) | Discord Levels (Label Toggle) |
| `KULW7WSA` | 213 | 15788 | THF Scalp & Trend + FVG + Ichimoku [Custom Colors 2] | THF Crossover and Trend Signals Golden & Death Cross with Volume |
| `7H1DGxKV-ORB-Range-Indicator-with-Fibonacci-Targets` | 236 | 13873 | ORB & Full Extended Range Indicator | ORB Range Indicator with Fibonacci Targets |
| `0sjcsPgM-Supply-Demand-Zones-Fixed-v3-Cross-YES-Only` | 268 | 17068 | Supply/Demand Zones / Interval Time V2 | Supply/Demand Zones - Fixed v3 (Cross YES Only) |
| `lmCaTAPv` | 295 | 24900 | Scout Regiment - K13 / Scout Regiment - K13 | SCTI-RSK |
| `R3y6mh9a-Improved-Weinstein-Stage-Analysis` | 313 | 26103 | Enhanced Weinstein Stage Analysis - Institutional / InstStages | Improved Weinstein Stage Analysis |
| `WtaFZGLB` | 510 | 39017 | PnL_EMA_TRACK12_PRO_3.7 | PnL_EMA_TRACK12_PRO_3.3_full_adjusted |
| `HwniNkOM-Nebula-by-Catboy` | 1053 | 70142 | Nebula / Nebula v2.2 | Nebula by Catboy |
| `9yxmTRPA-Multi-Timeframe-SMT` | 1100 | 119911 | Standalone SMT (Penta, Corrected) | Multi-Timeframe SMT |


## `scriptAccess` of captured rows

| Access | Count |
|---|---:|
| `open_no_auth` | 360 |

## Files on disk

`datastore/pine/*.pine`: **360** — matches captured count 360
