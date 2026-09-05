---
title: "Market timing with Value and Momentum"
slug: "market-timing-with-value-and-momentum"
date: "2015-07-22"
modified: "2022-05-27"
url: "https://alphaarchitect.com/market-timing-with-value-and-momentum/"
categories: ["Uncategorized"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Market timing with Value and Momentum

> Yesterday we wrote a post showing a potential way to time the market using valuation-based signals. In the past we have also examined how to use […]

Yesterday we wrote a [post](https://alphaarchitect.com/2015/07/21/eureka-a-valuation-based-asset-allocation-strategy-that-might-work/) showing a potential way to time the market using valuation-based signals. In the [past](https://alphaarchitect.com/2014/12/02/our-robust-asset-allocation-raa-solution/) we have also examined how to use momentum-based signals (moving average rules and time-series momentum) to time the market.

A natural question is what happens when we combine the valuation-based signals with the momentum-based signals?

Here at Alpha Architect, we are big believers in [Value](https://alphaarchitect.com/2014/10/07/our-quantitative-value-philosophy/) and [Momentum](https://alphaarchitect.com/category/architect-academic-insights/momentum-investing/). We have written about how to combine Value and Momentum in the security selection process [here](https://alphaarchitect.com/2015/03/26/the-best-way-to-combine-value-and-momentum-investing-strategies/) and [here](https://alphaarchitect.com/2015/05/07/combining-value-investing-momentum-investing-part-2/).

In this post, we examine what happens when we combine valuation-based (value) signals with momentum-based (MA rule) signals.

Here is the setup, from yesterday’s [post](https://alphaarchitect.com/2015/07/21/eureka-a-valuation-based-asset-allocation-strategy-that-might-work/):

### Strategy Background:

We use 1/CAPE as the valuation metric, or the “earnings yield,” as a baseline indicator; however, we adjust the yield value for the realized year-over-year (yoy) inflation rate, by subtracting the year-over-year inflation rate from the rate of 1/CAPE.

To summarize, the metric looks as follows if the CAPE ratio is 20 and realized inflation (Inf) is 3%:

**Real Yield Spread Metric** = (1/20)-3% = 2%  
Some details:

* [Bureau of Labor Statistics (BLS)](http://www.bls.gov/schedule/news_release/cpi.htm) publishes the CPI on a monthly basis since 1913; however, the data is one-month lagged (possibly longer). For example, the CPI for January won’t be released until February. So when we subtract the year-over-year inflation rate from the rate of 1/CAPE, we do 1-month lag to avoid look-ahead bias.
* We use the S&P 500 Total Return index as a buy-and-hold benchmark.

So the two signals we will use are the following:

### Valuation-based signal:

* **80th Percentile Valuation based asset allocation:** own S&P500 when valuation < 80th percentile, otherwise hold risk-free
  + In other word, if last month’s CAPE valuation is in the 80 percentile or higher (data starting 1/1924), buy U.S. Treasury bills (Rf); otherwise stay in the market.

### Momentum-based signal:

* Long-term moving average rule on the S&P 500 (own the S&P 500 if above 12-month MA, risk-free if below the 12-month MA).

Results are gross of any fees.  All returns are total returns and include the reinvestment of distributions (e.g., dividends). Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Our back test period is from 1/1/1934 to 12/31/2014.

### Baseline Results:

Here we show the results to 4 portfolios:

1. Valuation-based market timing: Own S&P500 when valuation < 80th percentile, otherwise hold risk-free.
2. Momentum-based market timing: Own the S&P 500 if above 12-month MA, risk-free if below the 12-month MA.
3. Risk-free: Total return to owning U.S. Treasury Bills.
4. SP500: Total return to the S&P500.

[![CAPE_1](https://alphaarchitect.com/wp-content/uploads/2015/07/CAPE_1.png)](https://alphaarchitect.com/wp-content/uploads/2015/07/CAPE_1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

As previously noted, both Valuation and Momentum-based timing models increase Sharpe and Sortino ratios, while decreasing drawdowns.

Now let’s combine them.

### Combining Value and Momentum Timing models:

Here we show the results to 4 portfolios:

1. (50/50) Abs 80%, MA : Each month, allocate 50% of capital to the valuation-based timing model, and 50% or capital to the momentum-based allocation model.
2. (and) Abs 80%, MA: Each month, examine the valuation and momentum-based signals. If ***both*** say “yes” to being in the market, invest in the S&P 500; if either or both say “no” to being in the market, invest in risk-free.
3. (or) Abs 80%, MA: Each month, examine the valuation and momentum-based signals. If ***either***say “yes” to being in the market, invest in the S&P 500; if ***both*** say “no” to being in the market, invest in risk-free.
4. SP500: Total return to the S&P500.

[![CAPE_2](https://alphaarchitect.com/wp-content/uploads/2015/07/CAPE_2.png)](https://alphaarchitect.com/wp-content/uploads/2015/07/CAPE_2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Takeaways:

* Combining the Value and Momentum-based signals makes sense, when using the “50/50 model” and the “(or) model.” Both of these have higher Sharpe and Sortino ratios compared to standalone value and momentum-based models.
* The “(and) model” does not work very well — you are out of the market too often.

### Conclusion:

Of course, transaction costs and taxes (not shown in the results above) need to be considered. However, it appears that combing value and momentum in market timing is promising, and something we will examine more carefully in the future.
