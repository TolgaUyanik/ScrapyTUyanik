---
title: "Order Flow Correlation May Imply Momentum Factor Crowding"
slug: "order-flow-correlation-may-imply-momentum-factor-crowding"
date: "2020-06-15"
modified: "2021-08-27"
url: "https://alphaarchitect.com/order-flow-correlation-may-imply-momentum-factor-crowding/"
categories: ["Research Insights", "Factor Investing", "Basilico and Johnsen", "Academic Research Insight"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Order Flow Correlation May Imply Momentum Factor Crowding

> Zooming In on Equity Factor Crowding Valerio Volpati, Michael Benzaquen, Zoltán Eisler, Iacopo Mastromatteo, Bence Tóth, and Jean-Philippe Bouchaud Working Paper, SSRN A version of […]

## Zooming In on Equity Factor Crowding

* Valerio Volpati, Michael Benzaquen, Zoltán Eisler, Iacopo Mastromatteo, Bence Tóth, and Jean-Philippe Bouchaud
* Working Paper, SSRN
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3518404)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

This study is one of several studies reviewed [here](https://alphaarchitect.com/2020/01/27/the-predictability-of-crowding-on-factor-strategy-performance/) and [here](https://alphaarchitect.com/2019/10/14/crowded-trades-asset-centrality-and-predicting-equity-bubbles/), attempting to measure factor crowding. This article specifically examines the presence of factor crowding by estimating the correlation between market order flow with the magnitude of the factor signal to trade. They hypothesize that factor crowding can be identified via the correlations associated with supply-demand imbalances where investors trade in the same direction, and with rebalancing order flow. Two measures of order flow are used: anonymous (proprietary) microstructure data for the Russell 3000  and institutional order flow from a proprietary database. Results are limited to the 3 Fama-French factors including HML, SMB and Momentum studied. No other formulations of value, size, and momentum were tested.

## What are the Academic Insights?

In general the authors find significant and mostly consistent results for all 3 factors, with Momentum exhibiting the strongest relationship. See Figure 3 below for Momentum results. Note that *“the grey stripe denotes the significance band for correlations obtained by reshuﬄing the time series (in blocks of 6 months in order to preserve the autocorrelation structure) and calculating the standard deviation of the obtained correlations over 200 reshuﬄed samples.”* Given that rebalance costs of FF factor portfolios are relatively high, the authors impose a slowing down of the trade signal across various period of time. None of the variations in time to trade affected the overall conclusions.
For Momentum trades:

1. There is a significant, negative correlation between trade imbalance and order flow (signal to  buy or sell). See top panel in Figure 3. There is a positive and significant correlation between book imbalance and order flow.  The difference in the signs of the correlation are possibly explained by the use of passive orders in factor trading  in the market-wide nature of the data set used in this test.
2. The metaorder imbalance and volume imbalance also exhibit significant and  positive correlations with the Momentum signal to trade.  See Figure 3, middle panel. The authors hypothesize that the imbalance variable in this data set is *not* sensitive to type of trading (passive vs. active) as is the data set used in #1.  Possibly true.
3. The correlations reported in Figure 3, bottom panel are for the daily close returns and the Momentum signal computed for the Russell 3000 universe.   While significant, the magnitude of the average correlation is low, approximately 0.2%.  It is used to estimate market impact cost of Momentum trades.  The authors report that although the overall correlation is low, it did increase over an examination of subperiods tested between 1999 and 2018. Thus supporting an increase in the magnitude of crowding over time.

For HML and SMB, the same methodology was followed.

1. The results for FF Value and Size are similar to Momentum for market-wide imbalance data. However, significance levels for Size were lower. Not a surprising result given the holding periods for the Size and Value factor are much longer and require smaller amounts of rebalancing activity.
2. For the metadata imbalances, the correlations were only marginally significant.

As to robustness, the author conducted a number of tests to verify the correlations reported.  They find the correlations are indeed stable across stocks and with respect to liquidity and tick size, and the long only or short only components. An implied assumption is that institutional investors are most likely to invest in the three FF factors.

## Why does it matter?

The authors are able to make a strong case for the measurement of crowding in the momentum factor, however, the results for HML and SMB were encouraging, but not as convincing. Nonetheless, the need for identifying conditions of crowding in factor strategies remains and is motivated by at least 3 complications for investors pursuing such systematic strategies:

1. An increase in cash flowing into a factor, potentially reducing excess returns to the strategy;
2. An increase in transactions costs and market impact costs as trade flows follow the strategy,  potentially decreasing excess returns; and
3. An increase in systemic risk as the number of new vendors offering the strategy overlap with existing portfolios; most likely taking the form of liquidation/loss events that cascade across all vendors and investors.

“Crowded trades” is often repeated as an explanation for the large drawdowns for some factor strategies.  Since these strategies have seen substantial inflows over the recent decades, it seems the documentation of crowding is a precondition to link investor inflows to the “death” of these types of systematic strategies.

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2020/06/2020-06-09-15_55_05-Microsoft-Edge-800x1433.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

---

## Abstract

> Crowding is most likely an important factor in the deterioration of strategy performance, the increase of trading costs and the development of systemic risk. We study the imprints of crowding on both anonymous market data and a large database of metaorders from institutional investors in the U.S. equity market. We propose direct metrics of crowding that capture the presence of investors contemporaneously trading the same stock in the same direction by looking at fluctuations of the imbalances of trades executed on the market. We identify significant signs of crowding in well known equity signals, such as Fama-French factors and especially Momentum. We show that the rebalancing of a Momentum portfolio can explain between 1–2% of order flow, and that this percentage has been significantly increasing in recent years.
