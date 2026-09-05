---
title: "Pathetic Protection via Protective Puts"
slug: "pathetic-protection"
date: "2019-07-15"
modified: "2019-07-15"
url: "https://alphaarchitect.com/pathetic-protection/"
categories: ["Crisis Alpha", "Factor Investing", "Basilico and Johnsen", "Academic Research Insight", "Managed Futures Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Pathetic Protection via Protective Puts

> Pathetic Protection: the Elusive Benefits of Protective Puts Roni Israelov Journal of Alternative Investments, Winter 2019 A version of this paper can be found here Want to read our […]

## Pathetic Protection: the Elusive Benefits of Protective Puts

* Roni Israelov
* *Journal of Alternative Investments, Winter 2019*
* A version of this paper can be found [here](https://www.aqr.com/Insights/Research/White-Papers/Pathetic-Protection-The-Elusive-Benefits-of-Protective-Puts)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Research Questions?

Investors would like to maximize upside participation while mitigating losses. This preference is at the base of the growth of the liquid insurance market in the form of equity index options.

The author investigates the following research question:

1. Are protective put options an effective tail hedge?

## What are the Academic Insights?

By testing ( via a real world implementable strategy\* and via Monte Carlo simulations\*\*) the hedging properties of put protection strategies and comparing them with the straightforward risk-reducing alternative that statically divests the equity position, the author concludes that portfolios protected with (expensive) put options have worse peak-to-trough drawdown characteristics per unit of expected return than portfolios that have instead simply statically reduced their equity exposure in order to reduce risk. This means investors who reduce their positions will likely achieve better outcomes than those who purchase protection.

Buying an equity put option reduces equity exposure. In that regard, it is similar to divestment. Both actions reduce risk and consequently expected return. Where the two approaches differ is that the put option introduces time-varying equity exposure, which adds risk. Additionally, a put-protected equity position is more volatile than an equity position that is sized to match the beta of the put protected portfolio. The protected position is less negatively skewed than the divested position, but its increased volatility is unhelpful, and unlike the divested position, the protected position is subject to path-dependent outcomes.

\*Cboe S&P500 5% Put Protection Index

\*\* via a super idealized scenario in which crash risk is unpriced ( absense of volatility risk premium) as well as including a volatility risk premium and situations of sudden (one day) equity crashes

## Why does it matter?

The results in this paper challenge the view that put options are the most direct and effective approach to protecting a portfolio against large losses. Differently, buying protection more often than not and on average leads to worse drawdowns than does divesting the equity position to match the average return.

This is particularly true when options are priced with a volatility risk premium.

In the words of the author:

[in this case],”The outcome is precisely the opposite of what is intended.”

## The Most Important Chart from the Paper:

Exhibit 19 plots the percentage of time divesting had better peak-to-trough drawdowns than protecting with put options: 97% over very short horizons and 100% over longer horizons.

![](https://alphaarchitect.com/wp-content/uploads/2019/02/pathetic-protection.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.



---

## Abstract

> Conventional wisdom is that put options are effective drawdown protection tools. Unfortunately, in the typical use case, put options are quite ineffective at reducing drawdowns versus the simple alternative of statically reducing exposure to the underlying asset. This paper investigates drawdown characteristics of protected portfolios via simulation and a study of the CBOE S&P 500 5% Put Protection Index. Unless your option purchases and their maturities are timed just right around equity drawdowns, they may offer little downside protection. In fact, they could make things worse by increasing rather than decreasing drawdowns and volatility per unit of expected return.
