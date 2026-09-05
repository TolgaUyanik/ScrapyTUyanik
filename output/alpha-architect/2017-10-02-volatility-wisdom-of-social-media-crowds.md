---
title: "Academic Research Insight: VOLATILITY WISDOM OF SOCIAL MEDIA CROWDS"
slug: "volatility-wisdom-of-social-media-crowds"
date: "2017-10-02"
modified: "2022-04-29"
url: "https://alphaarchitect.com/volatility-wisdom-of-social-media-crowds/"
categories: ["Research Insights", "Basilico and Johnsen"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Academic Research Insight: VOLATILITY WISDOM OF SOCIAL MEDIA CROWDS

> Title: VOLATILITY WISDOM OF SOCIAL MEDIA CROWDS Authors: Ahmet K. Karagozoglu and Frank J. Fabozzi Publication: Journal of Portfolio Management, Winter 2017 […]

* **Title:**   VOLATILITY WISDOM OF SOCIAL MEDIA CROWDS
* **Authors:**Ahmet K. Karagozoglu and Frank J. Fabozzi
* **Publication:**Journal of Portfolio Management, Winter 2017**[(version here)](http://www.iijournals.com/doi/abs/10.3905/jpm.2017.43.2.136?journalCode=jpm)**

## **What are the research questions?**

Using raw tweets from Twitter and StockTwits (“Trader Mood Data” from PsychSignal) a minute-by-minute social media sentiment signal is constructed for numerous financial instruments and used to evaluate various trading strategies.

1.   Can information gathered from social media tweets be used to construct a realistic volatility signal that can be used to predict future market volatility without relying on complex estimation methodologies?  
2.  Can trading strategies using a signal developed from the volatility of social media sentiment outperform after fees and costs?  What is the investment impact of this type of “sentiment”?

## **What are the Academic Insights?**

1.  YES.  The authors backtest a social anomaly score (SAS) constructed from tweets as a proxy for crowd-based sentiment regarding the stocks included in the S&P 500.  The trading strategy relies on the hypothesis that the larger the crowd, the more accurate will be the volatility measures that are estimated from that crowd.

Two SAS scores are calculated:  SAS-w consists of the weighted sentiment expressed for constituents of the S&P 500 Index and the SAS-spy is based on sentiment on the SPY.  If the SAS-w exceeds the SAS-spy on any day, the strategy is to go long the VIX-linked ETP and short the VIX-linked ETP if the reverse occurs.  In other words,  if the weighted sentiment of the crowd for volatility exceeds that for the market proxy ETF, then market volatility will increase when we rely on the wisdom of the crowd.  If the reverse is true, and crowd-based volatility is less than that of the market ETF, then market volatility will be expected to decrease. A medium and long-term version of the SAS scores are constructed and used to forecast daily and weekly market volatility. The VIX-linked ETPs includes the VIXY-the ProShares VIX short-term futures ETF; the VIXM-the ProShares VIX mid-term futures ETF; the VXX, the iPath S&P500 VIX short-term futures ETN; and the VXZ-the iPath S&P 500 VIX mid-term futures ETN.

2.  YES.  Five different strategies (of aggregation of tweets, such as mean, median) were used to calculate each score using long and medium-term SAS scores from the database produced roughly consistent results in terms of net profitability, risk-adjusted returns and risk measures.  This was especially true for the aggregation method used in Strategy 1.

Focusing on long-term SAS scores, all five aggregation strategies outperformed the buy-and-hold for the VIXY and for the VXX (strategy 1), after fees and costs.  Strategy 1 for the VIXY and VXX exceeded 100% for the period, with Sharpe ratios of 1.45 and 1.39, respectively.  Aggregation strategies 2-5 produced returns in excess of 90% for the VIXY and VXX compared to 40.6% for the buy-and-hold.

The data covered the period September 2012 to April 2016. The authors point out one caveat:  during this period the VIX was declining, possibly affecting their results.  However, they also point out that the trading signals produced not only equal distributions between long and short positions, but both produced positive profits.  There is no reason to believe that the same results would not occur when the VIX is in an upward trend.

Another caveat:  The results may be affected by datamining biases.  There were forty-four simulations, with five aggregation strategies covered, across both long and medium term SAS scores.  Even if the returns were not tested for robustness say on an out-of-sample basis, a reasonable haircut of even 25% would result in attractive returns.

## **Why does it matter?**

This article presents additional evidence on the practicality of obtaining effective measures of investor sentiment from social media.  A superior set of data from social media when compared to other published studies on the topic, is utilized.  While the database is similar to that used in other studies, it is unique in that it offers a much broader range of coverage.  SAS scores were constructed in a simple, easily calculated method (aggregated via averages, medians, for example) and then converted into trading signals.  The trading strategy was intuitively based on the idea that data obtained from larger social crowds would be more accurate in predicting future market volatility.  The trading strategy was implemented successfully with easily accessible and very liquid exchange-traded vehicles linked to the VIX.  Finally, returns were calculated net of fees and commissions.

## **What is the most important chart from the paper?**

![](https://alphaarchitect.com/wp-content/uploads/2017/09/2017-09-23-13_11_01-Microsoft-Edge.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.
