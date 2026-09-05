---
title: "Tactical Asset Allocation Series: Part 2 (Equal-Weight)"
slug: "tactical-asset-allocation-series-part-2-equal-weight"
date: "2012-11-05"
modified: "2022-06-10"
url: "https://alphaarchitect.com/tactical-asset-allocation-series-part-2-equal-weight/"
categories: ["Research Insights", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Tactical Asset Allocation Series: Part 2 (Equal-Weight)

> This is the second part in our series on tactical asset allocation. Our initial pieces outlined the basics of tactical asset allocation and offered some […]

This is the second part in our [series](https://alphaarchitect.com/category/architect-academic-insights/tactical-asset-allocation/) on tactical asset allocation.  Our initial pieces outlined the basics of tactical asset allocation and offered some foundation knowledge. In the series that follow (including this one), we will highlight all the models we present on our tactical asset allocation module of our software package (this is free–[simple click here to login](https://alpha.turnkeyanalyst.com/users/sign_in)).

The models and basic explanation follow:

### **Core 6:**

* SP500=[S](http://www.google.com/finance?q=NYSEARCA%3ASPY&ei=27VPUNiJD9C30AH-eQ)tandard and Poors 500 Total Return Index
* EAFE=The MSCI EAFE Total Return Index
* EEM=MSCI Emerging Markets Total Return Index
* REIT=FTSE NAREIT All Equity REIT Total Return Index
* GSCI=S&P GSCI Total Return Index
* US\_10Yr=Merril Lynch US Treasury 10-Year Treasury Futures Total Return Index

### **Models:**

* **ew\_index**=equal-weight Core 6.
* **ew\_index\_ma**=equal-weight Core 6 with 12-month moving average trading rule.
* **mom**=equal-weight Core 6 shifted by relative 12-month momentum.
* **mom\_ma**=mom strategy with 12-month moving average trading rule.
* **risk\_parity**=unlevered risk parity for Core 6.
* **risk\_parity\_ma**=unlevered risk parity for Core 6 with 12-month moving average trading rule.
* **risk\_parity\_mom**=unlevered risk parity weights for Core 6, adjusted by relative 12-month momentum.
* **risk\_parity\_mom\_ma**=unlevered risk parity weights for Core 6, adjusted by relative 12-month momentum, with a 12-month moving average trading rule.

More details can be found here:

<http://empiritrage.com/2012/07/13/a-horse-race-between-tactical-asset-allocation-models/>

The first model we’ll cover is the plain vanilla equal-weight index, rebalanced monthly.

### Equal-Weight Tactical Asset Allocation

The equal-weight system is the simplest model one can devise: an investor simply invests 1/n in each asset class, rebalanced monthly.

Academic research on asset allocation clings to the tenants of mean variance optimization and concludes that investors should hold the market portfolio, or the portfolio of all risky assets weighted by their respective value in the market portfolio. But how does the theoretical answer actually stack up against the very simple equal-weight strategy?

DeMiguel, Garlappi, and Uppal has a answer to this question in their [Review of Financial Studies Paper](http://thefinanceworks.net/Workshop/1002/private/3_Asset%20pricing/Articles/DeMiguel%20Garlappi%20Uppal%20on%20naive%20vs%20optimal%20diversification%20RFS%202009.pdf):

> We evaluate the out-of-sample performance of the sample-based mean-variance model, and its extensions designed to reduce estimation error, relative to the naive 1/N portfolio. Of the 14 models we evaluate across seven empirical datasets, none is consistently better than the 1/N rule in terms of Sharpe ratio, certainty-equivalent return, or turnover, which indicates that, out of sample, the gain from optimal diversiﬁcation is more than offset by estimation error. Based on parameters calibrated to the US equity market, our analytical results and simulations show that the estimation window needed for the sample-based mean-variance strategy and its extensions to outperform the 1/N benchmark is around 3000 months for a portfolio with 25 assets and about 6000 months for a portfolio with 50 assets. This suggests that there are still many “miles to go” before the gains promised by optimal portfolio choice can actually be realized out of sample.

So what is the real takeaway from this research? It is hard to do much better than 1/N in a world with so much volatility!

Here are some additional pieces on the subject written by fellow bloggers/researchers:

* <http://www.macroresilience.com/2010/07/08/heuristics-and-robustness-in-asset-allocation/>
* <http://aatheory.blogspot.com/2007/01/1n-solution.html>
* <http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2139878>
* <http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2139878>
* <http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2012278>

Use our tool to generate the latest weights, or simply type 1/5 into a calculator:

[![109](https://alphaarchitect.com/wp-content/uploads/2012/11/109-1024x444.png)](https://alphaarchitect.com/wp-content/uploads/2012/11/109.png)  
Here are the performance stats over time (January 1, 1979 to August 31, 2012):

[![110](https://alphaarchitect.com/wp-content/uploads/2012/11/110.png)](https://alphaarchitect.com/wp-content/uploads/2012/11/110.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The diversification concept is interesting, but did it really help? The simple 60/40 portfolio and the long-bond trade have outperformed!

A few takeaways:

* The equal-weight strategy reduces risk relative to a domestic-equity-only index, but the risk reduction is limited.
* Long bonds have experienced quite a run.
* 60/40 is tough to beat.

In our next series we will look at tactical asset allocation strategies that integrate momentum into the mix. Stay tuned…

### Disclosure:

Performance figures contained herein are hypothetical, unaudited and prepared by Alpha Architect, LLC; hypothetical results are intended for illustrative purposes only.

Past performance is not indicative of future results, which may vary.

There is a risk of substantial loss associated with trading commodities, futures, options and other financial instruments. Before trading, investors should carefully consider their financial position and risk tolerance to determine if the proposed trading style is appropriate. Investors should realize that when trading futures, commodities and/or granting/writing options one could lose the full balance of their account. It is also possible to lose more than the initial deposit when trading futures and/or granting/writing options. All funds committed to such a trading strategy should be purely risk capital.

Hypothetical performance results (e.g., quantitative backtests) have many inherent limitations, some of which, but not all, are described herein. No representation is being made that any fund or account will or is likely to achieve profits or losses similar to those shown herein. In fact, there are frequently sharp differences between hypothetical performance results and the actual results subsequently realized by any particular trading program. One of the limitations of hypothetical performance results is that they are generally prepared with the benefit of hindsight. In addition, hypothetical trading does not involve financial risk, and no hypothetical trading record can completely account for the impact of financial risk in actual trading. For example, the ability to withstand losses or adhere to a particular trading program in spite of trading losses are material points which can adversely affect actual trading results. The hypothetical performance results contained herein represent the application of the quantitative models as currently in effect on the date first written above and there can be no assurance that the models will remain the same in the future or that an application of the current models in the future will produce similar results because the relevant market and economic conditions that prevailed during the hypothetical performance period will not necessarily recur. There are numerous other factors related to the markets in general or to the implementation of any specific trading program which cannot be fully accounted for in the preparation of hypothetical performance results, all of which can adversely affect actual trading results. Hypothetical performance results are presented for illustrative purposes only.

Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

There is no guarantee, express or implied, that long-term return and/or volatility targets will be achieved. Realized returns and/or volatility may come in higher or lower than expected.
