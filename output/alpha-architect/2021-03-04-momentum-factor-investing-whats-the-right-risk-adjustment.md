---
title: "Momentum Factor Investing: What’s the Right Risk-Adjustment?"
slug: "momentum-factor-investing-whats-the-right-risk-adjustment"
date: "2021-03-04"
modified: "2022-05-21"
url: "https://alphaarchitect.com/momentum-factor-investing-whats-the-right-risk-adjustment/"
categories: ["Research Insights", "Factor Investing", "Momentum Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Momentum Factor Investing: What’s the Right Risk-Adjustment?

> Momentum? What Momentum? Erik Theissen and Can Yilanci A version of this paper can be found here Want to read our summaries of academic finance papers? […]

## Momentum? What Momentum?

* Erik Theissen and Can Yilanci
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3710496)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

The [momentum factor](https://alphaarchitect.com/2015/12/01/quantitative-momentum-investing-philosophy/) represents one of our core investment beliefs: buy winners. So when research presents itself that may contradict our beliefs it provides the opportunity to dig deeper and think harder about the factors we hold so dearly. Erik Theissen and Can Yilanci begin their paper by warming us up to the idea that momentum does outperform, and when measured on a portfolio level risk-adjusted basis, they agree momentum ***has delivered robust excess returns.***

But then they deliver the bad news. The “risk-adjusted” returns researchers use to assess the performance of momentum strategies might be flawed. And after adjusting for risk, momentum ***does not deliver*** significant excess returns. Erik and Can present the argument that the high turnover of momentum portfolios introduce a revolving door of alternative factors in a process they describe below:

> Portfolio-level risk adjustment assumes constant factor exposures of the strategy under investigation. However, it is well known that the factor exposures of momentum portfolios vary over time in a systematic way. (1). Momentum portfolios are characterized by huge turnover as stocks leave and other stocks enter the portfolio every month. Which stocks enter the long and short leg of the momentum portfolio depends on previous factor realizations. Consider the market factor as an example. When the excess return on the market is positive, high beta stocks perform well and low beta stocks perform poorly. Consequently, after a period of positive market excess returns the momentum portfolio will have high beta stocks in its long leg and low-beta stocks in its short leg, resulting in a high beta of the long-short portfolio. After a period of negative market excess returns the reverse will be true, resulting in a negative market beta of the long-short portfolio. Portfolio-level risk adjustment essentially estimates an average market beta of the momentum portfolio, and the average beta may well be (and in fact is) close to zero. Stock-level risk adjustment, on the other hand, captures the time-variation in the market exposure of the strategy. A similar argument can be made for the other factors of the FF5 model.

Because momentum portfolios have dynamic factor exposures, the authors suggest that the appropriate risk estimation technique for a momentum portfolio should be done at the stock level. And this leads to their core research question:

* Does the momentum factor still outperform on a risk-adjusted basis?

  

## What are the Academic Insights?

The research team utilized evidence from multiple samples and global markets (20 developed markets) to conclude the following:

* No. After adjusting for the dynamic factor exposure of momentum portfolios, there are no longer risk-adjusted excess returns.

  

## Why Does it Matter?

The debates surrounding the momentum factor are well-documented. “EMHers” simply cannot accept the empirical fact that the momentum factor has worked so well, historically.(2) Purely risk-based arguments, [which we’ve explored in this blog](https://alphaarchitect.com/2018/03/27/risk-based-explanations-momentum-premium/), simply can’t explain ALL of the excess returns realized by momentum strategies. This leads researchers to explore alternative behavioral explanations. For example, momentum may represent market [mispricing driven by a combination of behavioral bias and costly arbitrage](https://alphaarchitect.com/2018/09/18/momentum-investing-like-value-investing-is-simple-but-not-easy/).

This paper may help these two camps come together. The results suggest that momentum can actually be explained by factor models, but one needs to account for the dynamic nature of factor models. Of course, the ability of momentum strategies to successfully ‘time’ various factors needs to be discussed — is the system loading up on extra risk or exploiting mispricing? Also, what about long-only implementations versus the long/short factor implementation discussed in the paper? Long-only results still look strong.

And so the debates continue…

## The most Important Chart from the Paper

![](https://alphaarchitect.com/wp-content/uploads/2022/04/image-30-600x584-1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> Risk-adjusted momentum returns are usually estimated by sorting stocks into a regularly rebalanced long-short portfolio based on their prior return and then running a full-sample regression of the portfolio returns on a set of factors (portfolio-level risk adjustment). This approach implicitly assumes constant factor exposure of the momentum portfolio. However, momentum portfolios are characterized by high turnover and time-varying factor exposure. We propose to estimate the risk exposure at the stock-level. The risk-adjusted return of the momentum portfolio in month t then is the actual return minus the weighted average of the expected returns of the component stocks (stock-level risk adjustment). Based on evidence from the universe of CRSP stocks, from momentum returns conditional on market states, from volatility-scaled momentum strategies (Barroso and Santa-Clara 2015), from sub-periods and size-based sub-samples, and from an international sample covering 20 developed countries, we conclude that the momentum effect may be much weaker than previously thought.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | (Grundy and Martin 2001; Wang and Wu 2011; Daniel and Moskowitz 2016; Kelly et al. 2020) |
| ↑2 | Those who believe markets are efficient and reflect all available public information (semi-strong hypothesis) |

 function footnote\_expand\_reference\_container\_59781\_77() { jQuery('#footnote\_references\_container\_59781\_77').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_59781\_77').text('−'); } function footnote\_collapse\_reference\_container\_59781\_77() { jQuery('#footnote\_references\_container\_59781\_77').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_59781\_77').text('+'); } function footnote\_expand\_collapse\_reference\_container\_59781\_77() { if (jQuery('#footnote\_references\_container\_59781\_77').is(':hidden')) { footnote\_expand\_reference\_container\_59781\_77(); } else { footnote\_collapse\_reference\_container\_59781\_77(); } } function footnote\_moveToReference\_59781\_77(p\_str\_TargetID) { footnote\_expand\_reference\_container\_59781\_77(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_59781\_77(p\_str\_TargetID) { footnote\_expand\_reference\_container\_59781\_77(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
