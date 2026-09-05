---
title: "Novel explanations for risk-based option momentum"
slug: "option-risk"
date: "2023-04-25"
modified: "2023-04-24"
url: "https://alphaarchitect.com/option-risk/"
categories: ["Options", "Research Insights", "Guest Posts", "Momentum Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Novel explanations for risk-based option momentum

> In this paper, we propose a cross-sectional option momentum strategy that is based on the risk component of delta-hedged option returns. We find strong evidence of risk continuation in option returns.

In this article we discuss a new risk-based options momentum strategy, and explore the possible reasons for its success.

## A New Option Momentum: Compensation for Risk

* Heiner Beckmeyer, Ilias Filippou, Guofu Zhou
* March 29, 2023
* A recent version of the paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4404190).
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight/) category.

## What Is The Research Question?

Stock momentum trading is popular in practice and extensively investigated in academic studies. The paper finds a new option momentum, extending a recent study by Heston et al. (2022), who show that options also display momentum. Our risk-based [option momentum](https://alphaarchitect.com/2022/11/option-momentum/) is substantially stronger, has a risk explanation, and is also an extension of the stock risk momentum patterns uncovered by Li, Yuan, and Zhou (2023) to the options market. Our paper explores various explanations for the new strategy’s success.

## What Are The Academic Insights?

1. The authors propose a cross-sectional option momentum strategy based on the risk component of delta-hedged option returns, i.e., that portion that is explained by a common risk factor model. They find strong evidence of risk continuation in option returns. Specifically, options with high-risk components significantly outperform those options with lower-risk components. The authors apply the popular instrumental principal component analysis (IPCA) of Kelly, Pruitt, and Su (2019) to identify option risk factors and adjust individual option returns for risks with four latent factors.
2. Sorting options into quintiles based on the past risk component of their returns generates large return spreads in the next month: sorting on the average risk component over the last three months generates a high-minus-low portfolio with a Sharpe ratio of 4.95. Standard momentum using single equity option contracts achieves a Sharpe ratio of 3.39 for the same sorting exercise. The *RiskMom* strategy works for many formation and investment periods and essentially subsumes the performance of standard option momentum in nonparametric tests.
3. The authors perform a battery of tests to ensure the options’ liquidity does not drive the results. The results are robust to estimating the IPCA factor model on a rolling out-of-sample basis. They show that RiskMom is not prone to crashes (see Daniel, and Moskowitz, 2016) and is not followed by a long-term reversal, ruling out a story of overreaction. Furthermore, accounting for the trend component in risk factors and option betas is essential to fully discover RiskMom’s potential, showcasing that simpler factor momentum strategies are inadequate in the options market. Finally, information from the underlying and the option contract is important for the strategy’s success.
4. The authors discuss several possible explanations for the success of the *RiskMom* strategy. Of course, given that *RiskMom* is based on return continuation in the *risk* component of delta-hedged option returns, it is “born” with a risk-based explanation. They furthermore show that *RiskMom* is unexplained by how well the IPCA model can explain individual option returns and that it is partly explained by sticky forecast errors about the future volatility of the underlying. Information from the underlying and option contracts is essential for the strategy’s success. Finally, the authors show that *RiskMom* survives the consideration of realistic to high levels of transaction costs that an investor faces in the options market.

## Why Does This Matter?

The study helps us understand why trend-following works in the options market.

## The Most Important Chart From The Paper

![](https://alphaarchitect.com/wp-content/uploads/2023/04/Table-2-1-1200x712.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.*

## Abstract

> In this paper, we propose a cross-sectional option momentum strategy that is based on the risk component of delta-hedged option returns. We find strong evidence of risk continuation in option returns. Specifically, options with a high risk component significantly outperform those with a low risk component. The risk-based option momentum strategy is highly profitable for different formation and holding periods, and it is more profitable than the recently discovered option momentum strategy of Heston et al. (2022). We show that risk-based option momentum is unrelated to their return-based option momentum and fully subsumes its performance. The strategy is not subject to crash risk, it is not followed by long-term reversals, and survives the consideration of realistic levels of transaction costs. With this, our paper is the first to show that risk in the forward-looking and particularly informative options market is not only time-varying but also highly persistent over time and is well compensated by the corresponding option returns. Finally, we investigate possible explanations for the strategy’s success. Our results are robust to alterations of the empirical setup.
