---
title: "Does Portfolio Timing Based on Volatility Signals Outperform Buy and Hold?"
slug: "does-portfolio-timing-based-on-volatility-signals-outperform-buy-and-hold"
date: "2020-10-26"
modified: "2022-05-21"
url: "https://alphaarchitect.com/does-portfolio-timing-based-on-volatility-signals-outperform-buy-and-hold/"
categories: ["Research Insights", "Factor Investing", "Basilico and Johnsen", "Academic Research Insight", "Low Volatility Investing", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Does Portfolio Timing Based on Volatility Signals Outperform Buy and Hold?

> On the Performance of Volatility-Managed Portfolios Scott Cederburg, Michael S. O’Doherty, Feifei Wang, Xuemin (Sterling) Yan Journal of Financial Economics A version of this paper […]

## On the Performance of Volatility-Managed Portfolios

* Scott Cederburg, Michael S. O’Doherty, Feifei Wang, Xuemin (Sterling) Yan
* Journal of Financial Economics
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3357038)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

The popularity of using volatility to inform portfolio strategies has grown as the research tying volatility-managed techniques and improved risk/return portfolio performance has proliferated in the [literature](https://alphaarchitect.com/2019/05/22/volatility-targeting-improves-risk-adjusted-returns/).  The portfolios examined in the empirical literature generally utilize conservative positions in underlying factors (market, momentum, betting-against-beta, financial distress, size, and so on) when volatility has been high recently, and aggressive (leveraged) when volatility has been low. In the aggregate, the research documents that the volatility-managed (VM) effect is pervasive and economically significant. But that isn’t the full story on volatility-based timing…*With an emphasis on real-time implementation*, this study reexamines the performance of VM strategies and extends the analysis to 103 strategies in total.

1. Do volatility-managed portfolios outperform unmanaged portfolios on a risk/return basis?
2. Can real-time investors capture the economic gains implied by the in-sample analysis?
3. Why or why not?

## What are the Academic Insights?

1. YES. Replicating previous research and on an in-sample basis, the benefits of volatility management are confirmed empirically.  Positive and significant alphas are generated on a risk-adjusted basis.  As an example, the largest volatility-managed alpha was 23.39% for the momentum strategy. Other standouts included MKT, RMW (profitability), BAB (betting against beta), and ROE factors. On a risk/return basis, the authors calculated appraisal ratios (alpha/MSE) of sufficient size to support the conclusion that the mean-variance efficient front is expanded.  This research also expanded the universe to 103 new volatility-managed trading strategies across 9 factor categories, including Accruals, Intangibles, Investment, Market, Momentum, Profitability, Trading, Betting Against Beta, and Value.  Positive alphas were earned by 77 (75%) of the expanded set of strategies, of which 23 estimates were significant at 5%. When adjusted for Fama/French factors, 70 strategies earned positive alphas, with 21 significant.
  
2. NO. The authors reported significant degradation of real-time performance for the volatility-managed strategies. The economic impact of adding volatility-managed strategies was assessed using 2 out-of-sample or real-time approaches:  An allocation between a volatility-managed portfolio + original portfolio + risk-free security was compared to the second allocation to the same original portfolio + risk-free security. The results are presented in Table 5 below. With the exception of the MOM, ROE, and BAB factors, the volatility-managed portfolios exhibited significant degradation of real-time performance. Further, when Fama/French risk factors were included the out-of-sample performance for MOM, BAB and ROE also declined.
  
3. STRUCTURAL SHIFTS. So why the failure? The authors attribute the degradation of real-time performance to the instability of the regression parameters (coefficients) estimated for the volatility-managed portfolios.  It is necessary to estimate the scaling parameters from past data via regression, in order to enact volatility management during real-time periods.  Those estimates exhibited structural shifts when moving from past regimes into the future. Inasmuch as they were understood and applied as effective scaling scenarios, they were ultimately poor indicators of future scaling performance.

## Why does it matter?

This research highlights the difficulty investors face when attempting to obtain in-sample outperformance when volatility management necessitates the use of past data to determine scaling parameters.  The dynamics of the relationship between in-sample performance and real-time application are problematic when knowledge of the return-generating process is unstable.The execution of the analysis was rigorous.  Robustness checks on alternative designs included minimum window lengths of past data used to estimate scaling parameters, various rolling training samples, investor risk aversion parameters, and leverage constraints.  None of which changed the results in a favorable direction.

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2020/10/2020-10-15-17_08_30-Microsoft-Edge-2-1200x937.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> Using a comprehensive set of 103 equity strategies, we analyze the value of volatility-managed portfolios for real-time investors. Volatility-managed portfolios do not systematically outperform their corresponding unmanaged portfolios in direct comparisons. Consistent with Moreira and Muir (2017), volatility-managed portfolios tend to exhibit significantly positive alphas in spanning regressions. However, the trading strategies implied by these regressions are not implementable in real time, and reasonable out-of-sample versions generally earn lower certainty equivalent returns and Sharpe ratios than do simple investments in the original, unmanaged portfolios. This poor out-of-sample performance for volatility-managed portfolios stems primarily from structural instability in the underlying spanning regressions.
