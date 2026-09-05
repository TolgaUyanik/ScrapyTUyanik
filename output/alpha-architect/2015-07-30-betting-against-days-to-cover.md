---
title: "Betting Against Days to Cover"
slug: "betting-against-days-to-cover"
date: "2015-07-30"
modified: "2022-05-27"
url: "https://alphaarchitect.com/betting-against-days-to-cover/"
categories: ["Research Insights", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Betting Against Days to Cover

> Days to Cover and Stock Returns Hong, Li, Ni, et al. A version of the paper can be found here. Want a summary of academic papers […]

### Days to Cover and Stock Returns

* Hong, Li, Ni, et al.
* A version of the paper can be found [here](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2568768).
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category](https://alphaarchitect.com/category/architect-academic-insights/).

### Abstract:

> The short ratio — shares shorted to shares outstanding — is an oft-used measure of arbitrageurs’ opinion about a stock’s over-valuation. We show that days-to-cover (DTC), which divides a stock’s short ratio by its average daily share turnover, is a more theoretically well-motivated measure because trading costs vary across stocks. Since turnover falls with trading costs, DTC is approximately the marginal cost of the shorts. At the arbitrageurs’ optimum it equals the marginal benefit, which is their opinion about over-valuation. DTC is a better predictor of poor stock returns than short ratio. **A long-short strategy using DTC generates a 1.2% monthly return.**

### Betting Against Short Interest?

Literature shows that betting against stocks with high short interest (shares sold short/shares outstanding) generates future stock premiums. That’s probably because high short interest ratios may indicate the presence of information suggesting fundamental values are lower than the market indicates. What’s more, people believe that short sellers are mostly professionals and arbitrageurs who are more informed.

Researchers are showing a growing interest in the short ratio as a signal. [Rapach, Ringgenberg and Zhou (2015)](https://alphaarchitect.com/2015/02/23/can-you-predict-stock-market-returns-with-short-interest/) illustrate that short interest can forecast poor stock returns and cannot be subsumed by other existing market predictors.

In this paper, however, the authors point out the drawbacks of using the short interest ratio to make short decisions.

For example:

* Stock A and Stock B both have high level of short ratios. Let’s say, 10% of the shares outstanding of both stocks had been sold short.
* 5% of Stock A’s shares outstanding change hands daily on average; while only 1% of Stock B’s shares outstanding change hands daily on average.

So, short sellers can close their positions in Stock A (2 days) more quickly than in Stock B (10 days). Shorting Stock B has a higher marginal cost than shorting Stock A, due to liquidity constraints. In other words, if daily trading volumes are limited, then the high demand from sellers cannot be covered quickly, which may lead to more severe downward price pressure.  
  
From this point of view, the paper suggests that **Days to Cover (DTC)**, which measures how many days it would take all short sellers to cover their short positions, can better predict poor performances than **Short Ratio (SR)** does. DTC is calculated as below:  
[![Days to cover fomula](https://alphaarchitect.com/wp-content/uploads/2015/04/Days-to-cover-fomula.png)](https://alphaarchitect.com/wp-content/uploads/2015/04/Days-to-cover-fomula.png)

### Empirical Findings:

This paper constructs the long-short portfolios sorted on DTC and SR. Specifically, in each month, it sorts stocks based on either DTC or SR into 10 deciles. Then it builds a zero investment portfolio that goes long the stocks in the lowest DTC or SR decile and short the stocks in the highest DTC/SR decile. The full test sample is from 1988 to 2012.

* The equal-weighted return of the L/S portfolio based on DTC yields about 1.19% per month, with a significant t-stat of 6.67, and the Sharpe ratio is *1.33*. The value-weighted returns are weaker but are also statistically and economically significant.
* In contrast, the equal-weighted return of the L/S portfolio based on SR only gains about *0.71%* per month, with a t-stat of 2.57, and the Sharpe ratio is *0.51*.

Figure 4 shows that L/S strategy based on DTC outperforms the strategy based on SR.

[![SR and DTC performance](https://alphaarchitect.com/wp-content/uploads/2015/04/SR-and-DTC-performance.png)](https://alphaarchitect.com/wp-content/uploads/2015/04/SR-and-DTC-performance.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Figure 5 reports the trailing 10-year Sharpe ratios. We can see the Sharpe ratio for DTC strategy is much higher than SR strategy over the whole sample period.

[![Sharpe ratios of SR and DTC](https://alphaarchitect.com/wp-content/uploads/2015/04/Sharpe-ratios-of-SR-and-DTC.png)](https://alphaarchitect.com/wp-content/uploads/2015/04/Sharpe-ratios-of-SR-and-DTC.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Figure 6 illustrates the annual equal-weight returns for both strategies. DTC strategy outperforms SR strategy in ***20 out of 25 years***. Additionally, the DTC strategy shows ***lower volatility of returns and lower drawdowns***.

[![DTC and SR annual returns](https://alphaarchitect.com/wp-content/uploads/2015/04/DTC-and-SR-annual-returns.png)](https://alphaarchitect.com/wp-content/uploads/2015/04/DTC-and-SR-annual-returns.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Some thoughts:

An interesting paper with some nice results. Here are some things to consider:

* When micro-caps are eliminated, the difference between the short-ratio and days-to-cover starts to lose significance.
  + Additional analysis into mid/large cap firms would be nice, this is not shown in the paper (eliminating firms below the NYSE 40th percentile).
* It would be nice to show the ***significance*** of the long and short legs of the portfolio (Figure 3 shows the decile returns, but not the significance).
  + Would also want to see the significance once moving out of “all stocks” and into only mid/large cap stocks.
* When trading, the cost of shorting stocks will deteriorate returns.
  + In our example above, where stocks A and B both have a Short-ratio of 10, one should expect (in general) stock B (with a DTC ratio of 10) to have a higher shorting cost than stock A (with a DTC ratio of 2) since stock B is less liquid. By construction, the DTC portfolios will short firm B (with a higher short cost) more often than firm A.
