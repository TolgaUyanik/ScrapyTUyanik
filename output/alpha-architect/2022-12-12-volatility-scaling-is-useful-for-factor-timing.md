---
title: "Volatility scaling is useful for factor timing"
slug: "volatility-scaling-is-useful-for-factor-timing"
date: "2022-12-12"
modified: "2022-12-12"
url: "https://alphaarchitect.com/volatility-scaling-is-useful-for-factor-timing/"
categories: ["Volatility (e.g., VIX)", "Research Insights", "Factor Investing", "Basilico and Johnsen", "Academic Research Insight"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Volatility scaling is useful for factor timing

> This paper investigates the effects of volatility scaling on factor portfolio performance and factor timing.

The research summarized here is built upon a documented risk management strategy applied to factor investing (Barroso and Santa-Clara, 2015; Moreira and Muir, 2017). The idea was to overlay a scaled volatility measure designed to change risk exposures and hopefully produce higher Sharpe ratios. That basic research is ‘tweaked’ in this article by analyzing the effect of scaling on portfolios with a *combination* of factors. Four of the Fama-French factors are considered: Mkt-RF, SMB, HML and MOM. The more interesting question addressed was whether scaling volatility is useful in timing factors.

## The impact of volatility scaling on factor portfolio performance and factor timing

* Federico Nucera and Björn Uhl
* Journal of Asset Management
* A version of this paper can be found [here](https://link.springer.com/article/10.1057/s41260-022-00279-9)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category.

## What are the research questions?

1. Does volatility scaling affect the performance of portfolios that combine factors?
2. Does volatility scaling affect the ability to time factors?

## What are the Academic Insights?

1. YES. The results were as most would expect. Using the inverse of the realized volatility to scale the returns of equity factors did improve performance.  The results for the optimized (MV) portfolios are presented below in Table 3.  Two other weighting schemes including risk-parity (RP) and equal-weighting (EW) were examined with similar although slightly lower positive results.  Overall, the scaling of the factors improved the Sharpe ratio, Sortino ratio and the downside risk metric, MDD.  In comparison to the buy and hold benchmark, the EW and MV strategies outperformed for all but the latest period tested, across all metrics.  The RP strategy produced mixed results, outperforming its benchmark for 5 of the 10-year windows considered.
2. YES, SORT OF. This is perhaps the most interesting finding in the article. The subject of timing an investment strategy has been “worked over” both in the academic literature and investment practice.  Most would agree that [timing of factors](https://alphaarchitect.com/2021/09/factor-timing-is-tempting/) is challenging at best.  In this piece, the authors argue that timing factors could be achieved by managing the risk of factor returns via volatility scaling.  If volatility is predictable, then using a timing signal based on its past performance could be valuable.  A significant autocorrelation function (ACF) of factor returns is of course required to make the timing strategy work.  Tests of the ACF of factor returns with a lag of 12 months are tested on an individual basis and the results are significant for MKt-RF, SMB and HML.  As one might expect, there was little evidence of predictability for MOM since the autocorrelation has been captured in the structure of the MOM factor itself.  The timing strategy used was simply constructed by holding only the scaled factor that exhibited the best performance over the previous 12 months, thus rotating over factors over time.  The strategy returned the following statistics: Return 7.5% vs 5.1% BMK; Sharpe ratio .90 vs. .65 BMK; MDD 3.92 vs. 5.7 BMK; and Sortino ratio .05 vs. .03 BMK.

## Why does it matter?

Although the authors conclude that “our results show that volatility scaling improves factor return predictability, but this does not necessarily translate into a profitable factor rotation strategy”, the reported results do have practical relevance. Volatility scaling is a beneficial overlay strategy for at least three equity factors although it may not be constant over time or over short investment horizons.

## The most important chart from the paper

![Comparison of period performance is relevant to the question of volatility scaling.](https://alphaarchitect.com/wp-content/uploads/2022/12/2022-12-05-22_26_43-VolScaling_JAM.pdf-and-1-more-page-Personal-Microsoft​-Edge-1200x545.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract on volatility scaling research

> This paper investigates the effects of volatility scaling on factor portfolio performance and factor timing. We focus on the four equity factors analyzed by Carhart (1997) and find that volatility scaling may lead to higher diversification benefits for a long-horizon investor when equity factors are combined into a portfolio. Depending on the portfolio formation methodology, we also discover a substantial time-variation in portfolio performance. In addition, our results show that volatility scaling improves factor return predictability, but this does not necessarily translate into a profitable factor rotation strategy.
