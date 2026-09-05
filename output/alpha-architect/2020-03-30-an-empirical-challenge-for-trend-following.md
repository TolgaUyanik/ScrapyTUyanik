---
title: "An Empirical Challenge for Trend-Following"
slug: "an-empirical-challenge-for-trend-following"
date: "2020-03-30"
modified: "2020-03-30"
url: "https://alphaarchitect.com/an-empirical-challenge-for-trend-following/"
categories: ["Research Insights", "Factor Investing", "Trend Following", "Basilico and Johnsen", "Academic Research Insight", "Momentum Investing Research", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# An Empirical Challenge for Trend-Following

> Editor’s Note: For the foreseeable future, we’ll be focusing on research that explores investment strategies that are believed to help investors manage risk and diversify […]

*Editor’s Note: For the foreseeable future, we’ll be focusing on research that explores investment strategies that are believed to help investors manage risk and diversify their portfolios.*

#### Time Series Momentum: Is it There?

* Dashan Huang , Jiangyuan Li , Liyao Wang, Guofu Zhou
* *Journal of Financial Economics,* 2020
* A version of this paper can be found [h](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2960350)[e](https://jfds.pm-research.com/content/1/3/57_id=2960350)[re](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3165284)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Research Questions

There is ample evidence in the literature that stock past returns predict future returns. One of the most comprehensive studies is [Moskowitz et al. (2012)](https://www.aqr.com/Insights/Research/Journal-Article/Time-Series-Momentum), which shows that time-series momentum (TSM) is everywhere (they test it on 55 assets).(1) Later studies confirmed the results on even a broader set of asset classes and time periods ([here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2993026) and [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2618243)). At the same time, other studies question the profitability of TSM ([here](https://www.researchgate.net/publication/303846490_Time_series_momentum_and_volatility_scaling) and [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2610288)). As such, the predictability of past stock returns, momentum, is still an open question. The authors of this paper re-examine the statistical and economic evidence of TSM. The paper is organized in two main sessions: the first one studies the predictability of TSM while the second one addresses the profitability of a strategy based on TSM signals.

## What are the Academic Insights?

The authors use the same dataset as [Moskowitz et al. (2012)](https://www.aqr.com/Insights/Research/Journal-Article/Time-Series-Momentum): futures prices for 24 commodities, nine developed country equity indexes, 13 developed government bonds, and nine currency forwards. The sample time period is different: from January 1985 to December 2015 (Moskowitz et al. was studying the data from 1985 to 2009).

They find the following:

1. By running a time series regression of monthly return for each asset on its past 12-month return, at the 10% significance level, 47 of the 55 assets have a t -statistic of less than 1.65, suggesting that the in-sample evidence of TSM is weak. Due to concerns of data-mining, the authors perform an out of sample test ( January 2000- December 2015) following a methodology introduced by [Campbell and Thompson (2008)](https://dash.harvard.edu/bitstream/handle/1/2622619/Campbell_Predicting.pdf?sequence=2) and calculate the metric ” out-of-sample R squared OS” for each asset. They find that only three assets deliver significant R squared OS at the 10% level, indicating again that the evidence on time series predictability is weak among the assets.
  
2. Following [Moskowitz et al. (2012)](https://www.aqr.com/Insights/Research/Journal-Article/Time-Series-Momentum), the authors also run a pooled regression by stacking all asset returns together. Consistent with [Moskowitz et al. (2012)](https://www.aqr.com/Insights/Research/Journal-Article/Time-Series-Momentum), they find a t -statistic of 4.34 in the regression of predicting the next one-month return using the past 12-month return. At the conventional critical level of 2, one could interpret this t -statistic of 4.34 as strong evidence of predictability.
  
3. However, the authors go a step further and argue that the pooled regression is likely to over-reject the null hypothesis for three reasons:
     
   * First, if assets have different mean returns, the slope estimate from the pooled regression without controlling for fixed effects tends to be biased upward ( [Hjalmarsson, 2010](https://www.federalreserve.gov/Pubs/ifdp/2008/933/ifdp933.pdf) ).
     
   * Second, as a predictor, the past 12-month return is persistent and can generate substantial size distortions ( i.e. [Stambaugh, 1999](http://schwert.ssb.rochester.edu/f533/jfe99_rs.pdf)).
     
   * Third, because volatility varies dramatically across assets, volatility scaling in the pooled regression without controlling for fixed effects further exacerbates the upward bias.
4. Specifically, due to the concerns discussed above, the t -statistic from the pooled regression is questionable. To assess the degree of over-rejection, the authors use two bootstrap methods. The first is a parametric wild bootstrap that simulates samples based on the fitted pooled regression residuals, and the second is a nonparametric pairs bootstrap that resamples the predictor and the dependent variable simultaneously. They find that the 5% critical values of the bootstraps are 12.53 and 4.83, respectively. They conclude that a high t -statistic found by [Moskowitz et al. (2012)](https://www.aqr.com/Insights/Research/Journal-Article/Time-Series-Momentum) is not statistically significant in supporting the existence of TSM. This finding is robust to all alternative cases, such as within each asset class, with different sample periods, and without volatility scaling.
  
5. When looking at the profitability of a strategy that goes long assets with positive past 12-month return and short assets with a negative past 12-month return, they take a different approach compared to [Moskowitz et al. (2012)](https://www.aqr.com/Insights/Research/Journal-Article/Time-Series-Momentum), which utilized volatility scaling. The authors here think that volatility scaling causes complexity in performance attribution. Hence they use simple equal weighting. They examine the performance of the TSM strategy in four different ways:
     
   1. They examine the performance of a similar strategy that does not require predictability. They propose a times series history (TSH) strategy that buys assets if their historical mean returns are positive and sell them otherwise, which is theoretically profitable even if asset returns are independent over time, but some have significantly higher means than others. They find that TSM and TSH perform virtually the same and their differences in average returns, as well as in risk-adjusted ones, are indifferent from zero. They conclude that because the TSH strategy is defined without requiring time-series predictability, it seems questionable to attribute the performance of the TSM strategy to predictability.
     
   2. They report the results of TSH with alternative portfolio weighting schemes, past 12-month return weighting and equal weighting with a zero-investment constraint. The results are similar, and the alpha differential between the TSM and TSH strategies is always indifferent from zero. In short, the profitable performance of the TSM strategy is similar to that of the TSH strategy that requires no predictability, suggesting that the performance of the TSM does not necessarily support predictability at the 12-month frequency across asset classes.
     
   3. Based on the predictive slope of [Lewellen (2015)](http://faculty.tuck.dartmouth.edu/images/uploads/faculty/jonathan-lewellen/ExpectedStockReturns.pdf), they examine the overall predictability of TSM across assets. The slope measures how realized returns are explained by predicted returns. If the past 12-month return perfectly predicts the next one-month return, the slope should have a value of one. They find that for the TSM forecasts the slope has a value close to zero, suggesting that the TSM forecasts have little predictive power.
     
   4. The authors would like to also find under what conditions the TSM is a better trading strategy than the TSH. Based on one thousand simulated samples by using pooled regression with varying assumed degrees of time-series momentum (i.e., the slope varies from 0.1 to 0.4), we find that the TSM and TSH strategies perform similarly when the slope is 0.1 (with real data, the slope of the pooled regression is 0.08, controlling for fixed effects). When the slope is 0.2, the TSM outperforms the TSH, but the difference is statistically insignificant. When the slope is 0.4, the TSM dominates the TSH in the sense that it does better in almost all the simulated samples. Because the two strategies generate similar performance using real data, our simulation indicates that the evidence of TSM is likely weak if it exists. Combined with other results, the TSM is unlikely to be statistically significant for all the assets. In short, a lack of empirical evidence exists to support the hypothesis that the TSM is everywhere.

## Why does it matter?

This study challenges the time-series momentum anomaly and the influential study by [Moskowitz et al. (2012)](https://www.aqr.com/Insights/Research/Journal-Article/Time-Series-Momentum). The authors conclude that the evidence for TSM is weak in both asset-by-asset time series regressions and a pooled regression accounting for size distortions. While the authors do not claim in any way that there is no predictability in the asset classes, they suggest that the predictability, if it exists, is not as simple as a constant 12-month return rule. ([Here is some of our own research](https://alphaarchitdev.wpengine.com/2016/12/22/time-series-momentum-volatility-scaling-and-crisis-alpha/) on the subject.)

Additionally, they suggest some examples of future research following this result such as examining different time horizons for TSM, a possible optimal combination of different time horizons and the possibility that the predictability of the time horizon could be time-varying and different for the various asset classes.

It’s called the continuing academic debate!

## The Most Important Chart from the Paper:

![](https://alphaarchitdev.wpengine.com/wp-content/uploads/2020/03/3.30.20-EB-Article-600x1095.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> Time series momentum (TSM) refers to the predictability of the past 12-month return on the next one-month return and is the focus of several recent influential studies. This pa- per shows that asset-by-asset time series regressions reveal little evidence of TSM, both in- and out-of-sample. While the t -statistic in a pooled regression appears large, it is not statistically reliable as it is less than the critical values of parametric and nonparametric bootstraps. From an investment perspective, the TSM strategy is profitable, but its perfor- mance is virtually the same as that of a similar strategy that is based on historical sample mean and does not require predictability. Overall, the evidence on TSM is weak, particu- larly for the large cross section of assets.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | <https://alphaarchitdev.wpengine.com/2019/06/26/trend-following-the-epitome-of-no-pain-no-gain/> |

 function footnote\_expand\_reference\_container\_55936\_165() { jQuery('#footnote\_references\_container\_55936\_165').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_55936\_165').text('−'); } function footnote\_collapse\_reference\_container\_55936\_165() { jQuery('#footnote\_references\_container\_55936\_165').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_55936\_165').text('+'); } function footnote\_expand\_collapse\_reference\_container\_55936\_165() { if (jQuery('#footnote\_references\_container\_55936\_165').is(':hidden')) { footnote\_expand\_reference\_container\_55936\_165(); } else { footnote\_collapse\_reference\_container\_55936\_165(); } } function footnote\_moveToReference\_55936\_165(p\_str\_TargetID) { footnote\_expand\_reference\_container\_55936\_165(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_55936\_165(p\_str\_TargetID) { footnote\_expand\_reference\_container\_55936\_165(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
