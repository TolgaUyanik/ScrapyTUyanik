---
title: "Asset Allocation vs. Factor Allocation—Can We Build a Unified Method?"
slug: "asset-allocation-vs-factor-allocation-can-we-build-a-unified-method"
date: "2019-12-30"
modified: "2022-05-20"
url: "https://alphaarchitect.com/asset-allocation-vs-factor-allocation-can-we-build-a-unified-method/"
categories: ["Research Insights", "Factor Investing", "Basilico and Johnsen", "Academic Research Insight", "Value Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Asset Allocation vs. Factor Allocation—Can We Build a Unified Method?

> Asset Allocation vs. Factor Allocation—Can We Build a Unified Method? Jennifer Bender, Jerry Le Sun, and Ric Thomas Journal of Portfolio Management A version of […]

## Asset Allocation vs. Factor Allocation—Can We Build a Unified Method?

* Jennifer Bender, Jerry Le Sun, and Ric Thomas
* Journal of Portfolio Management
* A version of this paper can be found [her](https://jpm.pm-research.com/content/45/2/9)[e](https://www.aqr.com/Insights/Research/Working-Paper/Responsible-Investing-The-ESG-Efficient-Frontier)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

We’ve taken a lot of time reviewing multi-factor allocation techniques within the equity portion of a portfolio [here](https://alphaarchitect.com/2018/10/22/constructing-long-only-multifactor-strategies-portfolio-blending-vs-signal-blending/) and [here](https://alphaarchitect.com/2018/10/11/how-a-multi-factor-portfolio-is-constructed-matters/). But thus far we have only written on the concept of utilizing a multi-factor investment technique in contrast with traditional asset allocation [here](https://alphaarchitect.com/2018/02/23/are-factors-better-and-more-diversifying-than-asset-classes-for-the-most-part-we-dont-think-so/). In this post, we are again going to engage the idea of using factors as a supplement to more traditional asset allocation methods.

> “*There is increasing interest in the idea of allocating across factors instead of across traditional asset classes. Allocating across factors has the intuitive appeal of allocating across building blocks that are in theory purer sources of return.*”
>  Jennifer Bender, Jerry Le Sun, and Ric Thomas, Asset Allocation vs. Factor Allocation—*Can We Build a Unified Method?* 2018

1. Can a factor-based allocation approach be successfully combined with traditional asset class allocation?
2. How can it be implemented?
3. Are the results empirically reasonable?

## What are the Academic Insights?

  
1. YES. This article is essentially a “proof-of-concept” piece designed to illustrate that the blending of factor-based allocation with traditional asset class allocation will produce valid empirical results. Although the development of robust factor forecasts remains challenging, the combination of expectations about future factor performance and views on asset classes has benefits.  For decades, investors have relied on the diversification benefits of asset allocation.  However, during periods when asset class correlations have risen, those benefits disappear.  The idea here is to identify common risk factors, rather than asset classes, to build optimally diversified portfolios.
  
2. SEVEN STEPS. *Step1*: Choose a limited but robust set of factors (both long and short term) that explain the cross-section of asset class returns. Be aware that there is a lack of consensus as to the potential candidates for that set. The authors use economic growth, inflation, real rates, momentum and volatility based on published research; *Step2*: For each asset class, estimate the factor exposures from *Step1* for use in *Step3*: Construct “factor-mimicking” portfolios where exposures are matched to weights.  The weighting is done to capture the risk and return characteristics of factors; the mimicking portfolios become the building blocks as opposed to asset classes; *Step4:* Create forecasts for factor returns either estimating times series forecasts,  economic forecasts of factor returns or via historical averages; *Step5:* Calculate the optimal risk-return tradeoffs for factors using the mimicking portfolios in an optimization framework, targeting return or expected risk (min risk, targeted factor exposure, max risk-adjusted returns and so on); portfolios that express discretionary views can be included with the mimicking portfolios; *Step6:* Extract expected returns for each asset class from the asset weights in the mimicking portfolios to use in *Step7:* to construct the final portfolio.
  
3. YES. Three strategies are tested over a short period of time, for illustrative purposes. SAA Quant = long-term factor exposures, tight factor exposures; TAA Quant = short-term factor exposures, relaxed factor exposures; TAA Disc = adds any discretionary view to TAA Quant. Risk to return performance measures are presented in Exhibit 13 below. Note that the Sharpe ratios are very similar ranging from .82 to .94, across the 3 strategies. The information ratios come in very reasonably at .52 and .75. Turnover for the SAA strategy is low at 23% per annum, and 229% to 240% for the TAA strategies.

## Why does it matter?

In this article, the current literature on factor-based asset allocation methods are extended to the multi-asset allocation case and integrated with traditional asset class allocation.  Discretionary input on asset class returns and the use of a long-term and or short-term framework for factor performance are intuitively attractive and easily included in the allocation decision permitting strategic, tactical or other discretionary views.

  

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2019/12/2019-12-26-13_39_21-Microsoft-Edge-1200x835.png)

Source: Jennifer Bender, Jerry Le Sun, and Ric Thomas, Asset Allocation vs. Factor Allocation—*Can We Build a Unified Method?*, 2018
The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

---

## Abstract

> There is increasing interest in the idea of allocating across factors instead of across traditional asset classes. Allocating across factors has the intuitive appeal of allocating across building blocks that are in theory purer sources of return. In practice, factor-based allocation is not easy: Factors are unobservable and must be specified. However, the authors believe there is merit in integrating insights from factors with traditional asset allocation. Information and views about factors and asset classes can be a powerful combination. In this article, the authors present a framework for combining the two paradigms in an innovative way, resulting in optimal allocations that blend insights from both paradigms. Specifically, their approach derives asset class return prediction from factor-based asset allocation, which allows construction of portfolios for various investment objectives from a unified framework.
