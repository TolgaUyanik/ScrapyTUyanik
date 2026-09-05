---
title: "Magic Formula and MA Rules: A Bad Combo!"
slug: "magic-formula-and-ma-rules-a-bad-combo"
date: "2011-11-27"
modified: "2022-06-03"
url: "https://alphaarchitect.com/magic-formula-and-ma-rules-a-bad-combo/"
categories: ["Research Insights", "Trend Following", "Value Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Magic Formula and MA Rules: A Bad Combo!

> Recently, I’ve been investigating various risk management systems. A lot of the work we’ve done is beyond the scope of the blog and/or is related […]

Recently, I’ve been investigating various risk management systems. A lot of the work we’ve done is beyond the scope of the blog and/or is related to things we do with our investment management business. Nonetheless, one of the most intuitive and seemingly robust risk management rules is the use of simple moving averages. The great thing about MA rules is that anyone can understand them (see <http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1926376> or [http://apps.olin.wustl.edu/MEGConference/Files/pdf/2010/49.pdf]( http://apps.olin.wustl.edu/MEGConference/Files/pdf/2010/49.pdf )  for some basics)

I’ve talked about the application of simple moving average models in recent posts:  
<https://alphaarchitect.com/2011/11/investigating-equity-and-bond-allocation-models/>

<https://alphaarchitect.com/2011/11/risk-managed-momentum/>

After exploring the MA rules in great detail, I asked a natural question:

> Okay, so this stuff seems to work on the S&P 500 and a variety of other broad asset classes (at least in-sample). What about applying this system to “alpha generation” models like the Magic Formula or the other systems like deep value and momentum?

Here are some of the highlights from a research piece we internally published:

* Moving average (MA) trading rules have worked historically: the investor can capture a large portion of positive return months and eliminate large drawdowns. The MA (2,10) trading rule has been the most effective MA rule when applied to the S&P 500 index.

* Applying MA rules to  a simple quantitative value strategy actually destroys performance. For example, a portfolio of highly liquid Magic Formula stocks (average daily value traded must be greater than $1.5mm) moves from a CAGR of 12.11% to 7.66% over the 1970 to 2010 period, while volatility goes from 19.47% to 15.01%–not a great risk/reward tradeoff.

* Value strategies can be attractive, but they are very difficult to risk manage. If one believes there are no free lunches in the real-world (or very few), this result will not be surprising: value investing can be very rewarding…if you have an iron stomach!

* We all remember the college wisdom: beer before liquor, never been sicker; liquor before beer, in the clear. Unfortunately, technicals with the S&P, invest with glee, technicals with cheap, makes you weep.

## **Strategy Outline:**

* MA (2,10) looks at the 2 month (~50 day) and the 10 month simple moving averages (~200 day). The rule is triggered if the 2 month goes below the 10 month SMA. If the rule is triggered, invest in the risk free rate, otherwise, the index. Note, the rule is triggered via the moving average calculation based on the magic formula strategy time series.

Magic Formula (MF) Calculations

* Calculate earnings before interest and taxes (EBIT) to total enterprise value (TEV) and rank universe
* Calculate EBIT to net property plant and equipment (NPPE) plus net working capital and rank universe
* Average rankings and rank universe
* Only look at stocks with > $1.5mm average daily volume traded (adjusted by CPI)
* 1970-2010 period
* Total returns and gross of fees.

## **Results Wavetops:**

Unfortunately, the MA rules kill the goose that lays the golden eggs (in this case, the magic formula).

[![40](https://alphaarchitect.com/wp-content/uploads/2011/11/40.png)](https://alphaarchitect.com/wp-content/uploads/2011/11/40.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Rolling alphas go from “pretty weak” for the standard magic formula (bottom chart), to “reliably negative” after applying the MA rule (top chart).

[![41](https://alphaarchitect.com/wp-content/uploads/2011/11/41.png)](https://alphaarchitect.com/wp-content/uploads/2011/11/41.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

We end with the rolling 1-year CAGR analysis and find that there isn’t a single 10-year period where the magic formula–with an MA rule–outperformed the standard buy-and-hold magic formula. Ugly.

[![42](https://alphaarchitect.com/wp-content/uploads/2011/11/42.png)](https://alphaarchitect.com/wp-content/uploads/2011/11/42.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

These results are not promising for trend-following value investing strategies. However, in this analysis we calculated the moving average rule based on the value investing program. We’ve done additional follow-on analysis and there does seem to be evidence that applying a moving average rule — calculated off the broad index — is potentially effective in managing the tail risk of value investing strategies.
