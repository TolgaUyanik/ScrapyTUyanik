---
title: "Evidence supporting factor-based seasonalities"
slug: "factor-seasonalities"
date: "2023-08-21"
modified: "2023-08-21"
url: "https://alphaarchitect.com/factor-seasonalities/"
categories: ["Seasonality", "Research Insights", "Factor Investing", "Basilico and Johnsen", "Academic Research Insight", "Momentum Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Evidence supporting factor-based seasonalities

> Factor seasonality reflects its own stock-level equivalent. It is not an independent risk factor.

Factor seasonality always seemed to be an idea that was too close to factor timing to help build factor strategies.  Surprisingly, the authors find a substantial factor seasonality effect across global markets, suggesting that the assumption is unwarranted.  This is the first study I have encountered that tested the proposition that portfolios sorted twice on a specific factor first and high returns second are valuable.  The basic strategy is to buy factors with high average “same calendar month” return and short factors with low “same calendar month” returns.  Ultimately, the authors make the case that factor seasonality reflects its own stock-level equivalent. It is not an independent risk factor.

## Factor seasonalities: International and further evidence

* Aleksander Mercik, Daniel Cupriak, and Adam Zaremba
* Finance Research Letters
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4490643)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category.

## What are the research questions?

1. Is there evidence of cross-sectional seasonality in equity factors in the US and globally?
2. What is the source of the factor seasonality observed?

## What are the Academic Insights?

1. YES. The evidence is presented in Table 3 below. Countries with high seasonality (high average same calendar returns) outperformed their low return counterparts by 30bps monthly, on average.  That value was reduced to 18bps when price seasonality was introduced to the analysis (PSEAS, left side of Table 3) and further reduced to 14bps when the Fama-French 6 risk factors were introduced (PSEAS+FF6, right side of Table 3).  Five of the 39 countries produced negative, insignificant average returns.  The scope of the study is substantial, testing 143 factors across 39 markets and spanning the years 1931 to 2022. The results were robust to various changes in methodology. The building blocks of factor seasonality strategies are a sample of factor portfolios. *All variables were obtained from Jensen et al. (2023) using publicly available code from [Global Factor Data.](https://jkpfactors.com/)* Factors directly related to cross-sectional seasonality were excluded. The factor strategies were implemented as long-short value-weighted portfolios that buy or sell a tercile of stocks in each market, consistent with Jensen et al. (2023).
2. Three explanations were analyzed: stock price seasonality, [cross-sectional variation](https://alphaarchitect.com/2020/01/how-to-turn-cross-sectional-into-time-series-momentum-and-be-home-in-time-for-dinner/) in factor returns, and factor momentum.  Evidence was only found for stock price seasonality.  The authors conclude that the seasonality observed is a function of the seasonality at the individual stock level. The abnormal returns associated with factor seasonality are completely subsumed by stock price seasonality.

## Why does it matter?

The research presented in this piece fills in a gap in the literature on the performance of equity factors.  As opposed to factor timing studies, the authors analyzed the effect of factor seasonality in a cross-sectional examination of excess returns.  The analysis is broad—39 individual markets and 143 individual factors, 40 to 90 years in most cases, plus four aggregates (developed markets, emerging markets, world, and world ex-USA). There were 5903 factors portfolios constructed. The practical application for building factor strategies is demonstrated in the pervasive and positive impact on portfolio returns.

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2023/08/2023-08-14-22_57_54-1-1.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.*

## Abstract

> We study factor return seasonalities in international markets. Using up to 143 characteristics sorted portfolios from 39 countries, we document a pervasive cross-sectional pattern: anomalies with a high average same-calendar month return outperform those with low average returns. The effect persists across individual markets and global samples and cannot be attributed to common risk factors. Neither factor momentum nor cross-sectional variation in unconditional premia explains the phenomenon. Instead, the effect originates from price seasonalities, which transmit to factor portfolios, engendering seasonality in their returns. Consequently—rather than manifesting an independent asset pricing phenomenon—**factor seasonality merely reflects its stock-level equivalent.**
