---
title: "Complexity is a virtue in return prediction"
slug: "complexity-is-a-virtue-in-return-prediction"
date: "2024-06-11"
modified: "2024-06-11"
url: "https://alphaarchitect.com/complexity-is-a-virtue-in-return-prediction/"
categories: ["Empirical Methods", "Research Insights", "Basilico and Johnsen", "Academic Research Insight", "AI and Machine Learning"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Complexity is a virtue in return prediction

> Simple models severely understate return predictability compared to “complex” models in which the number of parameters exceeds the number of observations.

Finance has seen unprecedented growth in the use of artificial intelligence, specifically in machine learning models.  Applications have included portfolio construction, stock analysis and in this case, the prediction of stock market returns.  This paper discusses the benefits of using complex models as found in AI, over simple models such as ordinary least squares for predicting market returns. The authors highlight the limitations of traditional simple models and advocate for the adoption of complex, machine learning-based approaches. Traditionally, market return predictions have relied on simple models with only a few parameters which significantly understate the predictability of stock returns. Complex models, which use more parameters than the number of observations, offer much better levels of predictability for market returns. Good news for the application of AI in quantitative finance.

This is an excellent article. I believe it will provide much impetus in moving finance and investments in the direction of complexity and away from the very restrictive, simple models we are using currently. A word of warning: the article is heavy on the mathematical and theoretical foundations of ML models. The reward for working through the details is an understanding of the statistical linkages between the large or complex and small or simple models. This summary will only provide a review of the high points, at least for now.

## The Virtue of Complexity in Return Prediction

* Bryan Kelly, Semyon Malamud and Kangying Zhou
* Journal of Finance
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4166368)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category.

## What are the research questions?

1. What are the main objectives of the article?
2. Does the “virtue of complexity” associated with highly parameterized, machine learning models apply to the prediction of market returns?
3. Is high complexity or highly parameterized models the same as datamining?

## What are the Academic Insights?

1. The article has three main objectives:
   * First, the authors argue that simple models, which use only a few parameters, significantly understate return predictability compared to complex models with more parameters than observations.
   * Second, they provide theoretical proof that complex models outperform simple models in predicting returns when appropriate shrinkage is applied. Shrinkage is a crucial technique in using complex models for return prediction, ensuring that these models maintain predictive power without overfitting the training data. Shrinkage means that the coefficients are reduced towards zero compared to the OLS parameter estimates, in order to achieve parameter selection.
   * Third, the empirical evidence from the U.S. equity market supported the theoretical findings, demonstrating the benefits of complex models. The focus was on forecasting the aggregate stock market return using a set of 14 predictor variables and evaluating the market timing strategies derived from these forecasts. The empirical analysis targets the monthly excess return of the CRSP value-weighted index. The information set for prediction includes predictor variables from Goyal and Welch (2008), available monthly from 1926 to 2020, (Dividend-Price Ratio, Dividend Yield, Earnings-Price Ratio, Stock Variance, Book-to-Market Ratio, Net Equity Expansion, Treasury Bill Rate, Long-Term Yield, Long-Term Return, Term Spread, Default Yield Spread, Default Return Spread, Inflation, one lag of the market return). Returns and predictors were volatility-standardized using backward-looking standard deviations to preserve the out-of-sample nature of forecasts.
2. YES. A simple definition of a highly parameterized model refers to the situation when the model parameters are larger than necessary to fit the data. In addition to establishing the virtue of complexity, the authors demonstrate that out-of-sample R2 from a prediction model is a poor measure of its economic value. A simulated [market timing model](https://alphaarchitect.com/2021/04/market-timing-using-aggregate-equity-allocation-signals/) earned large economic profits indicated by significant Sharpe ratios and information ratios, even when the R2 was large and negative. See the highlights in Table I for performance measures. Note that the complex (nonlinear) model turns in positive Sharpe and information ratios when compared to the linear model and the market itself. This is strong empirical evidence supporting the theoretical claims about the virtue of complexity in return prediction and market timing strategies. It demonstrates that high-complexity models can achieve substantial economic value regardless of the R2. The results advocate for the inclusion of rich, nonlinear models in empirical finance to leverage the benefits of model complexity. Perhaps researchers should focus more on economic value and less on forecast accuracy.
3. NO. In some cases, data mining *can* involve high parameterization, especially when complex models are used to uncover patterns in data. For instance, using a neural network, also a highly parameterized model, to find patterns in customer behavior can be seen as an intersection of data mining and high parameterization. A quick refresher on the meaning of datamining: the “discovering historical patterns that are driven by random, not real, relationships and assuming they’ll repeat…a huge concern in many fields” (Asness, 2015). In finance, datamining is especially relevant when researchers are attempting to explain or identify patterns in stock returns. It is difficult to ensure that the results are not “one-time wonders” especially if the data has been used inappropriately. These practices are at high-risk to produce significant results out of random phenomena which goes a long way toward explaining why predictions about investment strategies fail on a going forward basis.

## Why does it matter?

The research presented here establishes the “virtue of complexity” found in ML models and finds that it aligns itself very closely with real-world market behavior without the bias imposed by the simple models or the misuse of statistics. The authors do caution against adding variables to a model on an arbitrary basis but encourage adding them if they are likely to be relevant. They also encourage the use of *highly parameterized nonlinear prediction models*. A few takeaways: (1) Simple models are preferable only if they are specified correctly and that’s a tall order, (2) Complex models are preferable under general conditions, and (3) There is a need to move beyond simple models and consider the benefits of complexity, especially in the context of machine learning, to improve return predictions and portfolio performance .

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2024/06/2024-06-07-00_40_24-The-Journal-of-Finance-2023-KELLY-The-Virtue-of-Complexity-in-Return-Predi-2.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.*

## Abstract

> Much of the extant literature predicts market returns with “simple” models that use only a few parameters. Contrary to conventional wisdom, we theoretically prove that simple models severely understate return predictability compared to “complex” models in which the number of parameters exceeds the number of observations. We empirically document the virtue of complexity in U.S. equity market return prediction. Our findings establish the rationale for modeling expected returns through machine learning.
