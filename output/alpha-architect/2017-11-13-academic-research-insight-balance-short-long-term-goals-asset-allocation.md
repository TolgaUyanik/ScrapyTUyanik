---
title: "Academic Research Insight: How to Balance Short and Long term Goals in Asset Allocation"
slug: "academic-research-insight-balance-short-long-term-goals-asset-allocation"
date: "2017-11-13"
modified: "2017-11-13"
url: "https://alphaarchitect.com/academic-research-insight-balance-short-long-term-goals-asset-allocation/"
categories: ["Basilico and Johnsen", "Academic Research Insight"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Academic Research Insight: How to Balance Short and Long term Goals in Asset Allocation

> Strategic Asset Allocation-Combining Science and Judgment to Balance Short Term and Long Term Goals Peng Wang and Jon Spinney A version of this paper can […]

## Strategic Asset Allocation-Combining Science and Judgment to Balance Short Term and Long Term Goals

* Peng Wang and Jon Spinney
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2746001&rec=1&srcabs=2743374&alg=1&pos=5)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/academic-research-insight/) category.

## What are the research questions?

Investors following a purely quantitative approach to asset allocation are often left with unintuitive portfolios with high turnover. On the other hand, those who pursue ad-hoc approaches face uncertainty about the portfolio’s risk level and the suitability of the allocation to reach specific goals.  
The authors propose a solution to the following question:

1. Can practitioners capture both short (spending requirements and goals) and long-term (capital accumulation to preserve purchasing power) market dynamics by balancing quantitative processes and sound judgment in the resulting portfolios?

## What are the Academic Insights?

By studying portfolios of equity, bonds, and public real estate (including an assumption of decorrelated alpha) from 1995 to 2015,

1. YES – The authors propose a multi-period simulation process to balance short and long-term risks and goals faced by investors. Short-term risk is defined as the annual portfolio drawdown and estimated via a bootstrapping simulation technique. The long-term risk is measured as the probability of the portfolio’s real value declining as a prespecified threshold after a certain time frame. To estimate it, they use a Monte-Carlo simulation approach. As expected, greater allocations to risky assets result in a lower long-term risk but greater downside risk in the short term.

According to the authors, determining the best policy portfolio is an exercise in informed judgment. It is the one that balances the trade-offs between the two risks.

The tool that they propose replaces risk and returns on the XY axis with short term and long term risk probabilities and turns the efficient frontier into a probabilistic frontier of short-term versus long-term risks. The most conservative portfolio (10-80-10) lies in the most top right part of the curve with the lowest short-term risk but with a 70% chance of losing real value over a 10-year investment horizon given certain spending rule, expected returns and inflation assumptions(1). At the opposite end of the spectrum is the portfolio with the highest allocations to risky assets (90/0/10). This portfolio has a 40% probability of losing real value over a 10-year period but has in any given year, a 1% chance of experiencing the drawdown of 35% or more.  
A more typical policy portfolio (60/30/10) presents a better trade-off with minimal impact to long-term risk, but substantial improvement in the short term drawdowns.

## Why does it matter?

Protecting against short-term drawdowns can be quite costly in the long term. As well as, significant short-term drawdowns can be unsustainable for investors due to their spending rule requirements. Additionally, the interactions between investment and spending policy can have implications for both short term and long-term success. Finally, being able to find uncorrelated sources of pure alpha can significantly reduce the long-term risk with little impact to the short term one.

## The Most Important Chart from the Paper:

![](https://alphaarchitect.com/wp-content/uploads/2017/11/Asset-Allocation.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

---

### Abstract

> The authors build on traditional mean-variance optimization with a quantitative framework for combining the best of science and judgment in selecting an asset allocation for long horizon investors such as endowments. The novelty of their approach lies in its ability to balance the desire for long-term returns with the need to manage short-term risk and funding constraints, important goals but often in conflict. In order to reap the benefits of long-term risk premia, investors must be able to withstand occasional short-run painful drawdowns. The authors show how their unified approach can be used to examine how different combinations of asset classes, spending rates, and even alpha impact the policy portfolio over various planning horizons. The framework merges the science of portfolio optimization with a structure that informs sound judgment in determining an organization’s strategic asset allocation and spending policies.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | 5% initial spending rate increasing annually with inflation |

 function footnote\_expand\_reference\_container\_33448\_62() { jQuery('#footnote\_references\_container\_33448\_62').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_33448\_62').text('−'); } function footnote\_collapse\_reference\_container\_33448\_62() { jQuery('#footnote\_references\_container\_33448\_62').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_33448\_62').text('+'); } function footnote\_expand\_collapse\_reference\_container\_33448\_62() { if (jQuery('#footnote\_references\_container\_33448\_62').is(':hidden')) { footnote\_expand\_reference\_container\_33448\_62(); } else { footnote\_collapse\_reference\_container\_33448\_62(); } } function footnote\_moveToReference\_33448\_62(p\_str\_TargetID) { footnote\_expand\_reference\_container\_33448\_62(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_33448\_62(p\_str\_TargetID) { footnote\_expand\_reference\_container\_33448\_62(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
