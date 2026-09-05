---
title: "An Easy Way to Simplify and Improve the Shiller CAPE Ratio as a Prediction Tool"
slug: "a-cheap-and-easy-way-to-use-the-cape-ratio-to-predict-market-returns"
date: "2020-11-16"
modified: "2022-05-21"
url: "https://alphaarchitect.com/a-cheap-and-easy-way-to-use-the-cape-ratio-to-predict-market-returns/"
categories: ["Research Insights", "Basilico and Johnsen", "Academic Research Insight", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# An Easy Way to Simplify and Improve the Shiller CAPE Ratio as a Prediction Tool

> Ultra-Simple Shiller’s CAPE: How One Year’s Data Can Predict Equity Market Returns Better Than Ten Thomas K. Philips and Adam Kobor Journal of Portfolio Management […]

## Ultra-Simple Shiller’s CAPE: How One Year’s Data Can Predict Equity Market Returns Better Than Ten

* Thomas K. Philips and Adam Kobor
* Journal of Portfolio Management
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3443289) ([slides here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3443289))
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

Shiller’s (1998) original CAPE ratio (the cyclically adjusted price of an [equity index/10 year average of real earnings](https://alphaarchitect.com/2011/10/06/the-shiller-pe-ratio/)) used to predict long term equity returns, like every online recipe, has been improved over the years by various reviewers.  A number of substitutes for real earnings have been proposed and analyzed including national income + product account earnings; revenue + cash flow; and past earnings weighted by revenues.  Using a 10-year average in any or all of these alternative formulations has the effect of reducing noise and estimates earnings over a full business cycle. The author of this article produces superior results to previous attempts using only one year’s quarterly earnings and revenues. A vastly simpler approach.

1. How do they do it?

## What are the Academic Insights?

1. There are essentially 3 components in the simplified CAPE model. A major attraction of this article is the detailed description of the methodology used to construct and test the model.

* The authors document that a **nonlinear filter** used on quarterly earnings each year is effective at reducing noise and unwanted characteristics of the earnings series.  It is apparent from the data that the worst quarter of each year contributes to the skewness and kurtosis of the earnings series. The worst quarter is substantially different than the other 3 in that its volatility, skewness, and kurtosis are significantly higher. Therefore, the authors discard the worst quarter in each year, add the 3 quarters together and multiply by 4/3 to standardize to the level of earnings. This transformation produces an estimate of earnings over 3 quarters (E3) contains approximately one-half of the volatility of E or CAE (cyclically adjusted earnings) alone. Additional attributes of E3 include reduced bias and variance forecasts.  The authors report adding a quadratic term (E/P)2 produces a larger R2.
* Seasonality or other time variations in corporate profitability and margins are addressed using a second, separate model based on the sale-to-price (S/P) ratio.  The authors hypothesize margins will mean-revert given competitive pressures. Perhaps a low S/P ratio could provide information about a decline in future earnings growth or a high level of profitability not contained in earnings. Adding a quadratic term (S/P)2 to (S/P) more completely approximates the observed nonlinear nature between equity index (SP500, in this case) returns and valuation ratios.
* The final piece of the simplified CAPE is the weighting scheme applied to the above 2 components E3/P, (E3/P)2, and S/P, (S/P)2 to create a composite model and forecast. Weights of the components are calculated as the inverse proportion of their forecast error variances.  The approach of combining two univariate models in this manner is preferable as they are consistent with economic justification as separate variables, at least in the author’s opinion.
* Summary stats are presented in Exhibit 15 below. Note that the composite or simplified CAPE produces the most attractive performance profile, especially when compared to the original Shiller formulation.

## Why does it matter?

The contribution of this research lies in the transformation of the original formulation of the CAPE ratio that is not only more effective at reducing noise, but actually produces more accurate out-of-sample forecasts of the long-run returns of the equity index. (here is another example of [how to use CAPE](https://alphaarchitect.com/2015/07/21/eureka-a-valuation-based-asset-allocation-strategy-that-might-work/))

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2020/11/2020-11-06-19_10_17-Microsoft-Edge-1200x391.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> Professor Robert Shiller’s cyclically adjusted price/earnings ratio (CAPE) has proven to be a powerful descriptor, as well as a useful predictor, of long-term equity returns in the United States and many global markets. CAPE uses a 10-year average of real earnings to simultaneously filter noise in earnings and to estimate corporate profitability over a business cycle. In this article, the authors simplify the CAPE methodology by separating the filtering of noise from the detection of cyclicality in earnings. They filter noise by discarding the worst quarter’s earnings in each year, allowing them to use one year’s earnings instead of 10, and proxy temporal variation in profit margins using the sales-to-price ratio. In addition, they account for an empirical nonlinearity in the relationship between valuation ratios and equity market returns. They combine the output of two models, one based on earnings and the other on sales, to create a robust forecast of 10-year forward returns. In out-of-sample tests, their technique increases the correlation between out-of-sample-forecasts and realizations from 0.69 to 0.87, reduces the standard deviation of the forecast error for the 10-year returns of the S&P 500 relative to CAPE by 40%, and linearizes the relationship between forecast and realized returns.
