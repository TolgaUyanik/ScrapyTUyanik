---
title: "How to Measure the Liquidity of Cryptocurrency?"
slug: "how-to-measure-the-liquidity-of-cryptocurrency"
date: "2021-03-15"
modified: "2021-03-15"
url: "https://alphaarchitect.com/how-to-measure-the-liquidity-of-cryptocurrency/"
categories: ["Transaction Costs", "Crypto", "Research Insights", "Basilico and Johnsen", "Academic Research Insight"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# How to Measure the Liquidity of Cryptocurrency?

> In this blog we discuss the academic research surrounding the question of cryptocurrency liquidity. How to Measure the Liquidity of Cryptocurrency? Brauneis, Mestel , Riordan […]

In this blog we discuss the academic research surrounding the question of cryptocurrency liquidity.

## How to Measure the Liquidity of Cryptocurrency?

* Brauneis, Mestel , Riordan and Theissen
* *Journal of Banking and Finance,* 2021
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3503507)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Research Questions?

In January 2020, trading in bitcoin exceeded $930 billion and has certainly grown over the past year. Unlike nearly any other asset, bitcoin can be traded 24 hours a day, 7 days a week on trading platforms around the globe. While trading cryptocurrencies has become relatively frequent, the high number of exchanges combined with the lack of regulated data makes determining the liquidity of these markets problematic. The authors attempt to find a transaction-based measure to describe actual liquidity on a cryptocurrency exchange.

## What are the Academic Insights?

By analyzing a novel and comprehensive set of continuous transactions data and order book snapshots comprising the 50 best bids and asks for two major cryptocurrencies (bitcoin and ethereum) on three large exchanges (Bitfinex, Bitstamp, and Coinbase Pro), the authors compare the performance of transactions based liquidity measures to benchmark measures derived from high-frequency order book data (quoted and effective spread, price impact, and the cost of a roundtrip trade) and they find:

1. The measure used should depend on the question being asked, as there is not (yet) a universally best measure. Specifically, they identify three questions: i) the ability to capture the time series variation of liquidity; ii) the ability to capture the level of liquidity; iii) the ability to capture cross exchange differences in liquidity.

2. The proxies that use high, low, and closing prices, the [Corwin and Schultz (2012)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2012.01729.x) and [Abdi and Ranaldo (2017)](https://academic.oup.com/rfs/article/30/12/4437/4047344) estimators, best capture the time-series variation in cryptocurrency liquidity. These measures work for all data frequencies, exchanges (Bitfinex, Bitstamp, Coinbase Pro), benchmark measures (quoted spread, effective spread, price impact, cost of a roundtrip trade) and for both bitcoin and ethereum.

3. The measures that perform best in the cross-sectional analysis are the Amihud (2002) illiquidity ratio and the [Kyle and Obizhaeva (2016)](https://pages.nes.ru/aobizhaeva/Kyle_Obizhaeva_Invariance.pdf) estimator because they do well at all data frequencies and for both currency pairs.

4. An important application of liquidity proxies is to select an execution venue among a number of alternatives. The authors use the low frequency estimators to rank trading venues according to their liquidity and they find that the Amihud (2002) illiquidity ratio and the Kyle and Obizhaeva (2016) estimator best replicate the ’true’ ranking when compared to the ranking generated using high-frequency order book measures.

## Why does cryptocurrency liquidity matter?

This paper augments the literature on low-frequency transactions-based liquidity measures by extending the analysis to cryptocurrencies, an important and emerging asset class.

Findings are useful for researchers, investors, traders, trading venue operators and regulators to understand liquidity levels and dynamics on cryptocurrency exchanges with relatively easy to acquire and process aggregate price and volume data.

## The Most Important Chart from the Paper:

![Data such as number of transactions and order books is important for assessing the liquidity of cryptocurrency.](https://alphaarchitdev.wpengine.com/wp-content/uploads/2021/03/image-26-800x235.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> This paper investigates the efficacy of low-frequency transactions-based liquidity measures to describe actual (high-frequency) liquidity. We show that the Corwin and Schultz (2012) and Abdi and Ranaldo (2017) estimators outperform other measures in describing time-series variations, irrespective of the observation frequency, trading venue, high-frequency liquidity benchmark, and cryptocurrency. Both measures perform well during high and low return, volatility, and volume periods. The Kyle and Obizhaeva (2016) estimator and the Amihud (2002) illiquidity ratio outperform when estimating liquidity levels. These two estimators also reliably identify liquidity differences between trading venues. Overall, the results suggest that there is not yet a universally best measure but there are reasonably *good* low-frequency measures.
