---
title: "Can smart rebalancing improve factor portfolios?"
slug: "can-smart-rebalancing-improve-factor-portfolios"
date: "2024-09-03"
modified: "2024-09-03"
url: "https://alphaarchitect.com/can-smart-rebalancing-improve-factor-portfolios/"
categories: ["Transaction Costs", "Tommi Johnsen", "Research Insights", "Factor Investing", "Academic Research Insight", "Value Investing Research", "Momentum Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Can smart rebalancing improve factor portfolios?

> This paper provides new evidence on the efficacy of prioritizing transactions so as to focus portfolio turnover on the trades that offer the strongest signals and hence the highest potential performance impact.

This paper aims to test an effective rebalancing method that prioritizes trades with  
the strongest signals to capture more of the factor premium while reducing turnover and  
trading costs. The authors coin the term “smart rebalancing” to capture the essence of their ideas. The empirical tests include widely used factor strategies, including long-short factors and long-only factor-based strategies. All were analyzed using the smart rebalancing approach. The title of this piece is dead-on and the principles described here are suitable for any number of investment strategies.(1)

## Smart Rebalancing

* Rob Arnott, Feifei Li, and Juhani Linnainmaa
* Financial Analysts Journal
* A version of this paper can be found [here](https://rpc.cfainstitute.org/en/research/financial-analysts-journal/2024/smart-rebalancing)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category.

## What are the research questions?

1. Can trading costs and other market frictions be managed to improve the live performance of common factor strategies?
2. The authors develop and test several methods to reduce turnover including priority  
   best, proportional, and priority-worst rebalancing. Which work to reduce turnover costs  
   without sacrificing returns?
3. Do rebalancing approaches based on non-calendar events improve the performance of high-turnover strategies, such as momentum?

## What are the Academic Insights?

1. YES. The study shows that careful and considerate portfolio trading, particularly through the priority-best rebalancing method, can significantly mitigate trading costs and other market frictions. This method involves prioritizing trades based on the strength of their signals, focusing on the most impactful transactions.
2. YES. Smart rebalancing effectively reduces [turnover](https://alphaarchitect.com/2024/05/how-volatility-and-turnover-affect-return-reversals/) and trading costs while maintaining or even enhancing portfolio performance. By prioritizing trades that have the strongest signals, investors can capture more of the factor premium. The priority best rebalancing (prioritizes trades with the strongest signals) was first in performance, followed by the proportional (distributes trades evenly, which can lead to unnecessary trades and higher costs) and then the priority-worst methods (prioritizes the least useful trades which maximizes “noise”). The priority-best retained more of the factor premium, achieved higher net returns, and captured more alpha per unit of turnover than the other two. Truly smart rebalancing on a non-calendar basis.
3. YES. For high-turnover strategies like momentum, non-calendar-based rebalancing (where the portfolio is monitored continuously, and rebalancing is triggered when the deviation from the target portfolio exceeds a preset threshold) seems to be more effective. It allows for more flexible and timely adjustments, reducing unnecessary trades and associated costs.

## Why does it matter?

Smarter rebalanced factor portfolios earned higher Sharpe ratios and CAPM alphas than the market portfolio. However, the extent to which an investor can capture this performance depends on the turnover and trading costs associated with these strategies. For example, strategies with slower-changing signals, such as value and profitability, can retain more alpha than high-turnover strategies like momentum. Take a close look at Table 3 where the essential results are presented. The results are central to the authors’ argument that smart rebalancing methods, especially those that manage turnover and trading costs, significantly improve the performance of most factor strategies. For example, using the priority-best method produces positive and significant CAPM-type alphas when turnover is controlled (see Panel B). The table allows for a direct comparison of how different turnover limits (e.g., 10%, 20%, 50%, 100%) affect the CAPM alpha, providing insights into the trade-offs between turnover and performance. Net-of-turnover CAPM alphas are also presented in Panel F of Table 3. The comparison of Panels B and F illustrates the importance of considering trading costs for practitioners, regardless of the factor considered. Panels D and H provide insight into the baseline average trading costs and turnover. If some thought is given to trading details beyond priority best, proportional, and priority-worst rebalancing, perhaps other turnover reduction techniques are just waiting to be discovered.

## The most important chart in the paper

![](https://alphaarchitect.com/wp-content/uploads/2024/08/2024-08-27-21_16_14-Smart-Rebalancing_FAJ.pdf-and-2-more-pages-Personal-Microsoft​-Edge-1-800x827.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

## Abstract

> The sometimes vast gap between live results and paper portfolio performance is caused in part by  
> trading costs, discontinuous trading, and missed trades or other frictions, along with asset management fees. Smart beta and factor strategies are not exempt from this sort of “implementation  
> shortfall.” This paper provides new evidence on the efficacy of prioritizing transactions so as to  
> focus portfolio turnover on the trades that offer the strongest signals and hence the highest  
> potential performance impact. Rebalancing filters of this sort can capture much of the factor premia  
> for a long-only paper portfolio while cutting turnover and trading costs relative to a fully rebalanced  
> portfolio.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | [see here](https://alphaarchitect.com/2017/11/transaction-costs/) for Jack’s piece on factor investing and trading costs. |

 function footnote\_expand\_reference\_container\_92214\_108() { jQuery('#footnote\_references\_container\_92214\_108').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_92214\_108').text('−'); } function footnote\_collapse\_reference\_container\_92214\_108() { jQuery('#footnote\_references\_container\_92214\_108').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_92214\_108').text('+'); } function footnote\_expand\_collapse\_reference\_container\_92214\_108() { if (jQuery('#footnote\_references\_container\_92214\_108').is(':hidden')) { footnote\_expand\_reference\_container\_92214\_108(); } else { footnote\_collapse\_reference\_container\_92214\_108(); } } function footnote\_moveToReference\_92214\_108(p\_str\_TargetID) { footnote\_expand\_reference\_container\_92214\_108(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_92214\_108(p\_str\_TargetID) { footnote\_expand\_reference\_container\_92214\_108(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
