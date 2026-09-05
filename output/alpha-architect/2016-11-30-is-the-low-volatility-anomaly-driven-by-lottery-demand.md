---
title: "Is the Low Volatility Anomaly driven by Lottery Demand?"
slug: "is-the-low-volatility-anomaly-driven-by-lottery-demand"
date: "2016-11-30"
modified: "2022-05-11"
url: "https://alphaarchitect.com/is-the-low-volatility-anomaly-driven-by-lottery-demand/"
categories: ["Research Insights", "Low Volatility Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Is the Low Volatility Anomaly driven by Lottery Demand?

> A few years ago I wrote a summary on a working paper titled “A Lottery Demand-Based Explanation of the Beta Anomaly.” The paper is still […]

A few years ago I wrote a [summary](https://alphaarchitect.com/2014/06/09/betting-beta-demand-lottery/#gs.IsgFyVk) on a working paper titled “A Lottery Demand-Based Explanation of the Beta Anomaly.” The paper is still a working paper, and has been updated (unfortunately they took out a neat picture from the original paper!). Here is a [link](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2408146&download=yes) to the new version of the paper, and the updated abstract is listed below.

> The low (high) abnormal returns of stocks with high (low) beta — the beta anomaly — is one of the most persistent anomalies in empirical asset pricing research. This paper demonstrates that investors’ demand for lottery-like stocks is an important driver of the beta anomaly. When beta-sorted portfolios are constructed to be neutral to lottery demand, the beta anomaly is no longer detected. Regression analyses indicate a positive and significant relation between beta and expected stock returns after controlling for lottery demand. The abnormal returns associated with the beta anomaly are explained by a lottery demand factor. The beta anomaly exists only when the price impact of lottery demand falls disproportionately on high-beta stocks and is concentrated in stocks with low levels of institutional ownership.

### An Introduction to Low Volatility Anomalies

The paper examines the [low beta anomaly](https://alphaarchitect.com/2016/11/16/an-evidence-based-low-volatility-investing-discussion/) (an example of what is broadly deemed the “low volatility” anomaly), whereby low beta (volatility) stocks outperform high beta (volatility) stocks. According to asset-pricing theory, securities with higher risk should produce higher returns (two ways to measure risk are beta or volatility). Since low beta (volatility) stocks outperform high beta (volatility), this is labeled an anomaly. This paper attempts to give a plausible explanation for “why” such an anomaly should exist. Another plausible explanation, shown [here](http://pages.stern.nyu.edu/~lpederse/papers/BettingAgainstBeta.pdf), is that low beta stocks outperform due to leverage constrain/aversion. This paper highlights the fact that investor’s demand for lottery-type stocks can explain the low beta anomaly (using the [MAX](https://alphaarchitect.com/2011/02/07/hot-off-the-jfe-press-maxing-out-your-returns/#gs.01htLbY) measure — simply the largest single-day return over the past year).

The paper is interesting, and I recommend those interested in low beta or low volatility type strategies go and read the current version of the working paper. Table 3 of the paper highlights what happens if one splits the universe (in the paper, all stocks above $5 share price) on two measures, beta and lottery-demand (MAX).

However, we decided to dig into the numbers and see what happens if we simply split a mid/large cap universe on two dimensions: beta and lottery-demand.

### Universe and Experimental Design

We examine all U.S. stocks above the NYSE 40th percentile for market capitalization from 1/1/1963 – 12/31/2015 with the necessary data. This leads to a universe of mid/large cap stocks. The summary statistics on the universe are shown below (no fees or transaction costs are included):

[![low-beta-and-lottery-demand-1](https://alphaarchitect.com/wp-content/uploads/2016/11/low-beta-and-lottery-demand-1.png)](https://alphaarchitect.com/wp-content/uploads/2016/11/low-beta-and-lottery-demand-1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The correlations on the VW Universe and the SP500 are 0.9921, while the correlation on the EW Universe and the Sp500 EW is 0.9718 — confirming that we are looking at similar universes.

Next, we sequentially split the universe of stocks on two dimensions:

1. First, we take the universe and create 5 quintiles based on each firm’s beta measure. Beta is measured by regressing stock daily returns against the VW market over the past year. The quintiles based on Beta are formed every month (ie this is a monthly rebalanced strategy).
2. Second, within each beta quintile, we create 5 quintiles based on the firm’s MAX measure, which proxies for lottery-demand. The MAX measure is simply the stock’s largest daily return over the past month.

As a result, we get 25 portfolios, formed monthly. The returns (CAGRs) to the portfolios are shown below from 1/1/1963 – 12/31/2015. No transaction costs or management fees are applied.

#### Value-Weight CAGRs (VW) across Volatility and Lottery Demand

[![low-beta-and-lottery-demand-2](https://alphaarchitect.com/wp-content/uploads/2016/11/low-beta-and-lottery-demand-2.png)](https://alphaarchitect.com/wp-content/uploads/2016/11/low-beta-and-lottery-demand-2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### Equal-Weight CAGRs (EW) across Volatility and Lottery Demand

[![low-beta-and-lottery-demand-3](https://alphaarchitect.com/wp-content/uploads/2016/11/low-beta-and-lottery-demand-3.png)](https://alphaarchitect.com/wp-content/uploads/2016/11/low-beta-and-lottery-demand-3.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### A Few Takeaways for Low Beta and Low Volatility Strategies

1. For every Beta quintile, in general, the highest MAX quintile (lottery-demand) has the worst returns. Part of this may be driven by short-term [mean reversion](https://alphaarchitect.com/2015/01/14/quantitative-momentum-research-short-term-return-reversal/#gs.bGsQt0c), and part may be due to investor demand for lottery stocks (driving up the prices, and lowering future expected returns).
2. A blanket statement that low beta stock outperforms high beta stocks may be too broad. While, on average, low beta stocks outperform, it is clear that a subset of high beta stocks perform just as well (or even better) than a subset of low beta stocks (especially when reviewing equal-weight portfolios, which are less prone to size effects).

While many investors/advisors have been attracted to low volatility strategies, we think it is important to understand the dynamics of these portfolios. The paper investigated — and our internal analysis — highlights an important fact that lottery-demand likely drives a lot of the results associated with low volatility strategies. Investors and advisors using low volatility strategies (or even building them from scratch) may want to take into consideration the results above and in the original paper.  
Good luck.

---

### A Lottery Demand-Based Explanation of the Beta Anomaly

Bali, Brown, Murray, and Tang

A version of the paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2408146&download=yes).

Want a summary of academic papers with alpha? Check out our [Academic Research Recap](https://alphaarchitect.com/category/architect-academic-insights/academic-research/#gs.m4HqX7w) Category.

### Abstract:

> The low (high) abnormal returns of stocks with high (low) beta — the beta anomaly — is one of the most persistent anomalies in empirical asset pricing research. This paper demonstrates that investors’ demand for lottery-like stocks is an important driver of the beta anomaly. When beta-sorted portfolios are constructed to be neutral to lottery demand, the beta anomaly is no longer detected. Regression analyses indicate a positive and significant relation between beta and expected stock returns after controlling for lottery demand. The abnormal returns associated with the beta anomaly are explained by a lottery demand factor. The beta anomaly exists only when the price impact of lottery demand falls disproportionately on high-beta stocks and is concentrated in stocks with low levels of institutional ownership.
