---
title: "News and its Impact on Risk and Returns Around the World"
slug: "news-and-its-impact-on-risk-and-returns-around-the-world"
date: "2020-10-12"
modified: "2020-10-12"
url: "https://alphaarchitect.com/news-and-its-impact-on-risk-and-returns-around-the-world/"
categories: ["Research Insights", "AI and Machine Learning", "Macroeconomics Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# News and its Impact on Risk and Returns Around the World

> How news and its context drive risk and returns around the world Charles Calomiris and Harry Mamaysky Journal of Financial Economics, August 2019 A version […]

## How news and its context drive risk and returns around the world

* Charles Calomiris and Harry Mamaysky
* *Journal of Financial Economics, August 2019*
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2944826).
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/academic-research-insight/) category.

## What are the Research Questions?

News is now data. But how is this data associated with changes in stock market returns and risks, and is there predictive power in the news via the words used?

This innovative paper asks and answers nine important questions about the interrelationship of news and stock market outcomes.

1. How should one best measure news using word flow?
2. Which aspects of word flow should be the focus of measurement?
3. How can we capture changes over time of the patterns that link frequency, topics, sentiment, and entropy measures of word flow with market outcomes?
4. Given the potential importance of identifying topical context, how should one identify topics?
5. Does the effect of our word flow measures operate through a risk channel?
6. How should one measure risk?
7. Do empirical patterns that apply to individual company stocks or the aggregate U.S. index also apply to other countries?
8. What source of news should one use?
9. Over what time frame should word flow predict risk and return?

## What are the Academic Insights?

1. According to the authors, there are two major methods: a) atheoretical without an a priori position regarding which particular words should be the focus of the analysis and b) identification of key lists of words or combinations of keywords (based on a priori criteria) to see how their presence matters for market outcomes. This paper utilizes the former one, which does not require researchers to know in advance what aspects of word flow are most relevant and it is less prone to data mining issues.
  
2. The authors suggest focusing at a minimum on sentiment (positive or negative) based on a preidentified dictionary, frequency of appearance of certain words, unusualness (entropy) of word strings, the context in which words appear (topics) – which is important since sentiment matters differently depending on the context.
  
3. The authors use principal component analysis to identify a dividing point. In fact, they present results for the entire sample period (1998-2015) and for two subperiods (April 1998-February 2007, and March 2007-December 2015). They also use a rolling elastic net regression to allow for dynamic changes of coefficients.
  
4. Within the set of atheoretical means of identifying topics, there are two common methods, namely the Louvain (Blondel et al., 2008, where each word belongs to only one topic area ) and latent Dirichlet allocation (LDA, see Blei, Ng, and Jordan, 2003, where words can appear in more than one topic area ). The author focus on the first one, which has the advantage of being faster in computational speed.
  
5. Yes, the authors find that when a word flow measure predicts positive expected returns, it also predicts a reduction in risk. This suggests that the factors captured by news flow are not priced risks.
  
6. To capture risk, in addition to using the standard deviation of returns, the authors also employ the “maximum one-year drawdown.” This measures, at any point in time, the maximum percentage decline that occurs from the current index value during the next year. This measure also is intended to capture the fact that “downside risk” may be treated differently from “upside risk” (the standard deviation of returns treats them as identical).
  
7. No, there is ample evidence in the literature that they do not. For this reason, the authors divide countries into EMs and DMs and perform separate panel analyses of each group of countries. They look at a total of 51 countries from 1998 to 2015.
  
8. In this specific case, and given the global focus of the analysis, the authors looked for an English source and decided to use Thomson Reuters news database.
  
9. Much of the existing finance literature on the effects of sentiment on individual stocks’ returns have focused on high-frequency predictions. However recent studies, including the one we reviewed here, find that it can be useful to aggregate over longer periods of time when analyzing news for individual stocks.

## Why does it matter?

The news and word choice within it are relatively new data sets to be examined for predictive power in markets. It is possible that within the words we use hidden meaning and correlations could be found that without the aid of a computer we would never have noticed. Five interesting findings from this paper are as follows.

1. The plots for EMs and DMs are quite similar for all the topical categories. One noteworthy aspect of the event studies is that news events appear to cause more of a market reaction in the DM sample than in the EM sample. This can reflect either more timely reporting by Reuters in their developed market news bureaus or information leakage (perhaps due to weaker regulatory enforcement) in EM economies.
  
2. The nature of news, and the range of potential news outcomes, differ in EMs and DMs (reflecting important differences in the political and economic environments, which are reflected in returns outcomes).
  
3. The news contained in the text flow measures studied, forecast one-year ahead returns, and drawdowns. One interpretation of this finding is that word flow captures “collective unconscious” aspects of news that are not understood at the time articles appear but that capture influences on the market that have increasing relevance over time.
  
4. Principal components analysis of topic areas suggests a possible change in coefficient values occurs during the onset of the global financial crisis.
  
5. Word flow measures tend to have greater incremental predictive power (measured in terms of the percentage improvement in R-squared) for understanding returns and risks in EMs, although they also have important incremental predictive power for returns and drawdowns in DMs.

## The Most Important Chart from the Paper:

![](https://alphaarchitdev.wpengine.com/wp-content/uploads/2020/10/image-600x544.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> We develop a classification methodology for the context and content of news articles to predict risk and return in stock markets in 51 developed and emerging economies. A parsimonious summary of news, including topic-specific sentiment, frequency, and unusualness (entropy) of word flow, predicts future country-level [returns, volatilities](https://www.sciencedirect.com/topics/economics-econometrics-and-finance/returns-volatility), and drawdowns. Economic and statistical significance is higher and larger for the year ahead than monthly predictions. The effect of news measures on market outcomes differs by country type and over time. News stories about emerging markets contain more incremental information. Out-of-sample testing confirms the economic value of our approach for forecasting country-level market outcomes.
