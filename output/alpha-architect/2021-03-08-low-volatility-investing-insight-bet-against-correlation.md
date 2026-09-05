---
title: "Low Volatility Factor Investing: Risk-Based or Behavioral-Based or Both?"
slug: "low-volatility-investing-insight-bet-against-correlation"
date: "2021-03-08"
modified: "2022-05-21"
url: "https://alphaarchitect.com/low-volatility-investing-insight-bet-against-correlation/"
categories: ["Volatility (e.g., VIX)", "Research Insights", "Factor Investing", "Basilico and Johnsen", "Academic Research Insight", "Low Volatility Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Low Volatility Factor Investing: Risk-Based or Behavioral-Based or Both?

> Betting against correlation: Testing theories of the low-risk effect Cliff Asness, Andrea Frazzini, Niels Joachim Gormsen, Lasse Heje Pedersen Journal of Financial Economics A version […]

## Betting against correlation: Testing theories of the low-risk effect

* Cliff Asness, Andrea Frazzini, Niels Joachim Gormsen, Lasse Heje Pedersen
* Journal of Financial Economics
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2913508)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

The [low-risk effect](https://alphaarchitect.com/2017/02/21/swedroe-insights-explaining-the-low-risk-effect/) (aka low volatility) is based on the empirical observation that assets with low risk have high alpha. Specifically in this research, the effect is defined as the risk-adjusted return spread between low-risk and high-risk portfolios and not just low-risk stocks.  Since the low-risk effect confounds traditional asset pricing models, various researchers have developed competing rationales for its existence and suggest the best way to measure it.

Low-risk as a [function of *leverage constraints*](https://alphaarchitect.com/2018/09/13/how-leverage-constraints-effect-mutual-fund-risk-taking/) was proposed by Black (1972) and Frazzini and Pedersen (2011, 2014) and tested the ‘[Betting Against Beta](https://alphaarchitect.com/2019/08/06/betting-against-beta-bab-construction/)’ (BAB) factor as representative of low-risk. Prior studies have produced evidence consistent with the notion that changes in margin requirements affect the slope of the security market line and the returns to BAB.

On the other hand, the *behavioral explanation* of the low-risk effect reflects investors’ preference for [lottery-like returns](https://alphaarchitect.com/2014/06/09/betting-beta-demand-lottery/) as proposed by Barberis and Huang (2008), and Brunnermeier, et al. (2007). In that case, the low-risk effect is driven and should be measured, by idiosyncratic risk. Recall that beta depends on volatility and correlation, while idiosyncratic risk depends only on volatility.

In order to differentiate between the two hypotheses, the authors construct two new factors from BAB that capture one proposition *without* being overtly related to the other:

* ‘Betting Against Correlation’ (BAC) to represent the leverage hypothesis and ‘Betting Against Volatility’ (BAV) to represent the preference for lottery-like, idiosyncratic returns.
* The long leg of BAC consists of stocks with low correlation to the market (therefore low beta) and the short leg consists of those with high correlation while matching the volatility of the stocks that are on the long and short side.
* The long side of BAV is low volatility (low risk) and short high volatility while matching correlation (similar betas) on both sides. Clever.

The key research questions:

1. Is the low-risk effect driven by leverage constraints and best measured using BAC?
2. Or is the low-risk effect a function of behavioral biases and best measured using various measures of idiosyncratic risk?

## What are the Academic Insights?

1. YES. A derivation is provided in the article defining BAB as a linear function of BAC and BAV. BAC should have lower betas and should exhibit positive risk-adjusted returns, but the returns should be lower than the return to BAB. See the results depicted in the graph below. BAC returned a monthly alpha value of 0.6% (t=5.25) with US data and 0.4% (t=3.47) with global data after adjusting for the Fama-French five factors. Since control for volatility is embedded in the spread, these results are differentiated from behavioral factors.
  
2. Unclear. Idiosyncratic measures of risk should have positive alphas consistent with the behavioral explanation of the low-risk effect.  The authors use three measures including IVOL (idiosyncratic risk), LMAX (low maximum return over the previous month), and SMAX (low maximum return scaled by volatility). All three exhibit significant alphas with US data: .25% (t=3.68) for SMAX; .24% (t=2.63) for LMAX; and .21% (t=2.38).  The five-factor Fama-French model was again used for risk adjustment. None were significant with global data, however.

Overall, the results are consistent with the notion that leverage constraints cause the BAB and BAC returns.  In contrast, the results are weaker and inconsistent for behavioral hypotheses (although they cannot be completely ruled out).  Note that the authors conduct numerous robustness checks including margin debt, sentiment, change in the CPI, and amusingly, variables associated with the casino/lottery industry. Various constructions method, the impact of turnover, out-of-sample tests across time, and different asset classes were also investigated.

## Why does it matter?

The main takeaway from my perspective is the dominance of the theory of leverage and the consequent performance exhibited by the BAC factor.  Stocks with low correlation to the market deliver higher risk-adjusted returns that are not explained by other factors associated with the low-risk effect. Moreover, low systematic (beta) risk factors outperform idiosyncratic risk factors out-of-sample in both the US and global markets. This study is well-conceived and conducted. It is difficult to find fault with the methodology, robustness checks, and theory behind this research. ([although there are discussions on this topic](https://alphaarchitect.com/2019/08/06/betting-against-beta-bab-construction/)).

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2021/02/2021-02-24-19_13_18-BettingAgainstCorrelation_Asness_JFE.pdf-and-1-more-page-Personal-Microsoft​.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> We test whether the low-risk effect is driven by (a) leverage constraints and, thus, risk should be measured using beta versus (b) behavioral effects and, thus, risk should be measured by idiosyncratic risk. Beta depends on volatility and correlation, with only volatility related to idiosyncratic risk. We introduce a new betting against correlation (BAC) factor that is particularly suited to differentiate between leverage constraints and behavioral explanations. BAC produces strong performance in the US and internationally, supporting leverage constraint theories. Similarly, we construct the new factor SMAX to isolate lottery demand, which also produces positive returns. Consistent with both leverage and lottery theories contributing to the low-risk effect, we find that BAC is related to margin debt while idiosyncratic risk factors are related to sentiment.
