---
title: "A Surprising Way to time Value and Momentum: Updated Analysis"
slug: "can-high-minus-low-hml-time-value-and-momentum"
date: "2014-08-28"
modified: "2022-05-31"
url: "https://alphaarchitect.com/can-high-minus-low-hml-time-value-and-momentum/"
categories: ["Value Investing Research", "Momentum Investing Research", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# A Surprising Way to time Value and Momentum: Updated Analysis

> Exploiting Factor Autocorrelation to Improve Risk Adjusted Returns K Oversby A version of the paper can be found here. Want a summary of academic papers with […]

# Exploiting Factor Autocorrelation to Improve Risk Adjusted Returns

* K Oversby
* A version of the paper can be found[here.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2456543)
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category!](https://alphaarchitect.com/category/academic-research/)

### **Abstract:**

> The Fama-French three factor model is ubiquitous in modern finance. Returns are modeled as a linear combination of a market factor, a size factor and a book-to-market equity ratio (or “value”) factor. The success of this approach, since its introduction in 1992, has resulted in widespread adoption and a large body of related academic literature. The risk factors exhibit serial correlation at a monthly timeframe. This property is strongest in the value factor, perhaps due to its association with global funding liquidity risk. Using thirty years of Fama-French portfolio data, I show that autocorrelation of the value factor may be exploited to efficiently allocate capital into segments of the US stock market. The strategy outperforms the underlying portfolios on an absolute and risk adjusted basis.
>
> Annual returns are 5% greater than the components and Sharpe Ratio is increased by 86%. The results are robust to different time periods and varying composition of underlying portfolios. Finally, I show that implementation costs are much smaller than the excess return and that the strategy is accessible to the individual investor.

### **Alpha Highlight:**

This interesting paper [“Exploiting Factor Autocorrelation to Improve Risk Adjusted Returns”](http://www.naaim.org/wp-content/uploads/2014/04/00L_Kevin_Oversby_Exploiting-Factor-Autocorrelation.pdf) caught our attention. We highlighted this paper a month ago [via a paper summary](https://alphaarchitect.com/?p=13544), but decided to dig a little deeper.

The paper claims that by using [HML](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_factors.html) to switch between small value and small momentum portfolios, the strategy can generate superior returns. We conducted our own backtesting by using data from the [French website](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html).

The first part of our study is the replication of the paper’s strategy; Second part is the robustness test;  Third part is implementation discussion.

### Data

Monthly returns from 01-1984 to 12-2013

1. Value-weighted [6 Portfolios Formed on Size and Book-to-Market (2 x 3)](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)
2. Value-weighted [6 Portfolios Formed on Size and Momentum (2 x 3)](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)
3. Value-weighted [100 Portfolios Formed on Size and Book-to-Market (10 x 10)](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)
4. Value-weighted [25 Portfolios Formed on Size and Momentum (5 x 5)](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)
5. PDP, PRF total return series, 01-2006 to 12-2013,  from Bloomberg

### Strategy

According to the paper:

[![2014-08-05 15_09_22-Exploiting Factor Autocorrelation to Improve Risk Adjusted Returns.pdf - Adobe A](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-08-05-15_09_22-Exploiting-Factor-Autocorrelation-to-Improve-Risk-Adjusted-Returns.pdf-Adobe-A.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-08-05-15_09_22-Exploiting-Factor-Autocorrelation-to-Improve-Risk-Adjusted-Returns.pdf-Adobe-A.png)

We follow the same strategy:

* IF last month’s HML > 0 and Return (value) > 0, then go into value (high b/m, small);
* IF last month’s HML < 0 and Return (MOM) > 0, then go into MOM (high mom, small);
* IF last month’s return < 0 then go into risk-free;
* IF none of above exists, then go into risk-free.

### Replication

VW 2 x 3 size/bm and 2\*3 size/mom. We selected SMALL value and SMALL momentum, using SMALL HML (small size high bm minus small size low bm) as the switching signal. The results from our analysis and the corresponding table from the paper are tabulated below:

[![](https://alphaarchitect.com/wp-content/uploads/2014/07/small-val-mom-6-stat1.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/small-val-mom-6-stat1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Paper results**

[![2014-08-15 12_54_41-Exploiting factor autocorrelation to improve risk adjusted returns.pdf - Adobe R](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-15-12_54_41-Exploiting-factor-autocorrelation-to-improve-risk-adjusted-returns.pdf-Adobe-R.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-15-12_54_41-Exploiting-factor-autocorrelation-to-improve-risk-adjusted-returns.pdf-Adobe-R.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### $1 Dollar Growth

[![small val mom 6](https://alphaarchitect.com/wp-content/uploads/2014/07/small-val-mom-63.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/small-val-mom-63.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### Paper results

[![2014-08-15 12_56_49-Exploiting factor autocorrelation to improve risk adjusted returns.pdf - Adobe R](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-15-12_56_49-Exploiting-factor-autocorrelation-to-improve-risk-adjusted-returns.pdf-Adobe-R.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-15-12_56_49-Exploiting-factor-autocorrelation-to-improve-risk-adjusted-returns.pdf-Adobe-R.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The results are not as good as what is stated in the paper, but still good enough to warrant further study and investigation.

### Robustness test

#### Large caps

We still use VW 2 x 3 size/bm and 2\*3 size/mom. However, we selected BIG value and BIG momentum, using BIG HML (big size high bm minus big size low bm) as the switching signal. The results drop significantly relative to the results for small-caps. However, the portfolio benefits from combing value and momentum exposures are still valid: sortino ratios are much higher and drawdowns are vastly improved.

[![big val mom 6 stat](https://alphaarchitect.com/wp-content/uploads/2014/07/big-val-mom-6-stat1.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/big-val-mom-6-stat1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

$1 Dollar Growth

[![big val mom 6](https://alphaarchitect.com/wp-content/uploads/2014/07/big-val-mom-61.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/big-val-mom-61.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### More Refined Value and Momentum Portfolios

We use two extreme value and momentum portfolios: the value portfolio is the smallest value portfolio from the 10 x 10 size/bm portfolios cuts; the momentum portfolio is the smallest momentum portfolio from 5 x 5 size/mom cuts.

[![small val mom 25 100 stat](https://alphaarchitect.com/wp-content/uploads/2014/07/small-val-mom-25-100-stat1.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/small-val-mom-25-100-stat1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

$1 Dollar Growth

[![small val mom 25 100](https://alphaarchitect.com/wp-content/uploads/2014/07/small-val-mom-25-1001.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/small-val-mom-25-1001.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Small and concentrated portfolios generate stronger results. Wes recently had a nice post on the size effect [“Does the size effect exist? Probably”](https://alphaarchitect.com/2014/07/02/does-the-small-cap-size-effect-exist-probably/) if you’d like to explore further.

### Implementation?

Results for small caps look good. But there are many implementation challenges. If one uses the small momentum 5 x 5 split and small value 10 x 10 split, one can easily end up with liquidity issues due to the size of firms in the portfolios. By using 2 x 3 split, one can limit liquidity issues, but the results aren’t as strong.

*Are there other ways we can implement this strategy?*

ETFs might be a good solution. Below we show the backtest results by using total returns of PDP (value) and PRF (momentum) from 01-2006 to 12-2013. “Portfolio” is the switch strategy between PDP and PRF based on 2 x 3 big HML signal.

[![pdp prf stat](https://alphaarchitect.com/wp-content/uploads/2014/07/pdp-prf-stat2.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/pdp-prf-stat2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

$1 Dollar Growth

[![pdp prf](https://alphaarchitect.com/wp-content/uploads/2014/07/pdp-prf1.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/pdp-prf1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The results are strong. That said, implementing this strategy could be a challenge for the non-professional or non-quant geek investor. Good luck!
