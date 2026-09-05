---
title: "Hot Topic: Does “Gamma” Hedging Actually Affect Stock Prices?"
slug: "hot-topic-does-gamma-hedging-actually-affect-stock-prices"
date: "2021-02-01"
modified: "2021-02-01"
url: "https://alphaarchitect.com/hot-topic-does-gamma-hedging-actually-affect-stock-prices/"
categories: ["Research Insights", "Factor Investing", "Basilico and Johnsen", "Academic Research Insight", "Momentum Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Hot Topic: Does “Gamma” Hedging Actually Affect Stock Prices?

> Hedging Demand and Market Intraday Momentum Guido Baltussen, Zhi Da, Sten Lammers and Martin Martens Journal of Financial Economics, Forthcoming A version of this paper […]

## Hedging Demand and Market Intraday Momentum

* Guido Baltussen, Zhi Da, Sten Lammers and Martin Martens
* *Journal of Financial Economics,* Forthcoming
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3760365)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Research Questions

More and more evidence seems to suggest that [social Media](https://alphaarchitdev.wpengine.com/2018/08/27/fintwit-might-matter-for-momentum-and-mean-reversion-in-stock-prices/) impacts daily momentum and volatility. Some hedge funds that were short GME the past couple of months should have read these blog posts. In a similar vein, there is plenty of twitter chatter on the topic and [anecdotal evidence](https://www.wsj.com/articles/the-invisible-forces-exacerbating-market-swings-11582804802) that during the last week of February 2020 ( when the US market crashed more than 10%), market volatility was exacerbated by market makers with short gamma positions. Gamma measures how much the price of a derivative accelerates when the underlying security price moves. Products with gamma exposure are typically options and leveraged ETFs. When prices of underlying assets move, market makers need to conduct hedging activities. Consequently, they have to buy additional securities when prices are rising and sell when prices are falling in order to ensure their positions are delta-neutral. Trading in the direction of the market price movement will exacerbate market swings and thereby result in increased market intraday momentum.

A quick example to makes things more concrete. Let’s say you are a reddit “WSBer” trying to manipulate the market. The user mentions that fellow members should buy out of the money calls in addition to the underlying stock. Why are they suggesting this? To create a “gamma squeeze’. How would this work? Well, the option market maker who sold this out of the money option WSBer needs to hedge their short position in the option, even though that sold call may be way out of the money. And what’s crazy is that if the price of the stock moves higher, the option dealer who sold the call needs to worry about hedging their short position as an increasing rate, thus driving potential demand that may put even more gas on the fire. That’s the theory, at least.

The authors of this study researched market [intraday momentum](https://alphaarchitdev.wpengine.com/2015/02/12/overnight-momentum-vs-intraday-momentum/), in other words, time-series momentum at the market level at the intraday frequency. They did this with 54 different time series across equities, bonds, and commodities going back to the 1970s covering 45 years of history. They ask the following research questions:

1. Is market intraday momentum everywhere?
2. Is gamma hedging an important driver?

## What are the Academic Insights?

The authors define a trading day as the 24-hour-period from the market close on day t − 1 to the market close on day t. The trading day is divided into five parts: overnight (ON, from close to open); first half-an-hour (F H, the first 30 minutes after the market open); middle-of-the-day (M, from the end of F H to an hour before the market close); second-to-last-half-an-hour (SLH, the second-to-last 30 minute interval); last half-an-hour (LH, the last 30 minutes before the market close). The combination of the first two partitions is labelled as “ONFH” (ONF H = ON +F H). The combination of the first four partitions is labelled as “rest-of-the-day” (ROD = ON + F H + M + SLH). ROD is the focus of the paper.

![](https://alphaarchitect.com/wp-content/uploads/2021/01/2021-01-29-10_05_09-SSRN-id3760365-1.pdf-CCleaner-Browser-edited-800x295.png)

The authors find:

1. YES-The rest-of-day return (rROD) positively and significantly predicts the last half-an-hour return (rLH) across all major asset classes and markets. This effect is robust over time across our sample period of 1974 to 2020, and distinct from cross-sectional intraday return seasonality. A simple market intraday momentum trading strategy produces consistent returns over time, translating into high and attractive (annualized) Sharpe ratios between 0.87 and 1.73 at the asset class level.

2. YES- By studying two datasets (SP500 index options and leveraged ETFs) the authors confirm that hedging demand on a particular index drives the magnitude of its market intraday momentum pattern.

3. While the authors do find evidence that large price jumps during the day predict subsequent returns, consistent with intraday hedging activities, the bulk of the hedge seems to take place towards the end of the day.

## Why does it matter?

This paper contributes to the voluminous literature on return momentum ( see for example Jegadeesh and Titman, 1993 for the cross-section and Moskowitz et al., 2012 for the time series). Instead, this study focuses on market momentum within a trading day. Most interestingly, it brings evidence to a novel economic force: hedging demand coming from options and leveraged ETFs amplify price changes and affect market return dynamics over several days.

## The Most Important Chart from the Paper:

Table 7 shows that indeed intraday momentum is much more pronounced on negative NGE days. On days with positive NGE, however, there is no significant intraday momentum. This provides strong support for our hedging demand hypothesis, i.e., that intraday momentum is partially driven by option hedging demand

![](https://alphaarchitect.com/wp-content/uploads/2021/01/2021-01-29-10_36_17-SSRN-id3760365-1.pdf-CCleaner-Browser-800x283.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> Hedging short gamma exposure requires trading in the direction of price movements, thereby creating price momentum. Using intraday returns on over 60 futures on equities, bonds, commodities, and currencies between 1974 and 2020, we document strong “market intraday momentum” everywhere. The return during the last 30 minutes before the market close is positively predicted by the return during the rest of the day (from the previous market close to the last 30 minutes). The predictive power is economically and statistically highly significant and reverts over the next few days. We provide novel evidence that links market intraday momentum to the gamma hedging demand from market participants such as market makers of options and leveraged ETFs.
