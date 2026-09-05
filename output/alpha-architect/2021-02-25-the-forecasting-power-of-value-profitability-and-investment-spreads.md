---
title: "The Forecasting Power of Value, Profitability, and Investment Spreads"
slug: "the-forecasting-power-of-value-profitability-and-investment-spreads"
date: "2021-02-25"
modified: "2022-05-21"
url: "https://alphaarchitect.com/the-forecasting-power-of-value-profitability-and-investment-spreads/"
categories: ["Research Insights", "Factor Investing", "Larry Swedroe", "Academic Research Insight", "Other Insights", "Value Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# The Forecasting Power of Value, Profitability, and Investment Spreads

> Studies such as the 2019 paper “Value Return Predictability Across Asset Classes and Commonalities in Risk Premia,” have demonstrated that while it is difficult to […]

Studies such as the 2019 paper “[Value Return Predictability Across Asset Classes and Commonalities in Risk Premia](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3054017),” have demonstrated that while it is difficult to time investments based on their value spreads(1) which we’ve covered occasionally [here](https://alphaarchitect.com/2017/12/21/the-returns-to-value-strategies-when-valuation-spreads-are-wide/) and [here](https://alphaarchitect.com/2014/09/12/valuation-spreads-over-time-a-unique-market-timing-signal/), value spreads do contain information on the returns to value strategies in individual equities, industries, commodities, currencies, global government bonds, and global stock indexes.

Yiqing Dai, Tariq Haque, and Ralf Zurbruegg contribute to the literature on factor investing with their study “Factor Return Forecasting Using Cashflow Spreads” which appears in the September 2020 issue of the International Review of Economics & Finance. They sought to improve factor forecasts by augmenting the book-to-market (BM) spread with the difference in operating profitability (the OP spread(2)) and the difference in investment (the INV spread(3)). The sample period is July 1963–June 2017.

Following is a summary of their findings:

* The OP and INV spreads have significant predictive power for the value factor (HML: High book-to-market Minus Low book-to-market), the profitability factor (RMW: Robust Minus Weak profitability), and the investment factor (CMA: Conservative Minus Aggressive investment).
* Controlling for the OP and INV spreads significantly improves the predictive power of the BM spread over HML, RMW, and CMA.
* Because of correlations, the BM, OP, and INV spreads each have much stronger predictive power when all are used simultaneously as predictors compared to when each is used alone to predict factor returns.
* For HML and RMW, the BM and OP spreads have a strong negative correlation (-0.66 and -0.81 respectively), implying that an increase in the BM spread comes with a decrease in the OP spread. Given that the BM spread and the OP spread have opposite effects in factor returns, this negative correlation indicates that using one spread alone to forecast returns could lead to large forecasting errors. For example, an increased BM spread tends to be associated with a decreased OP spread, so that while the increased BM spread implies a higher factor return this is then offset by the decreased OP spread which implies reduced factor returns. For CMA, the BM spread has a moderate negative correlation with the OP spread (-0.398), as well as a moderate positive correlation with the INV spread (0.440). The OP spread and the INV spread are moderately negatively correlated (-0.365). These moderate correlations imply that a joint control for the BM, OP, and INV spreads is needed to improve factor forecasting.
* The OP and INV spreads are not just substitutes for the traditional Fama-French factors.
* Their results hold in multiple robustness tests.

To exploit the predictive power of the BM and cashflow spreads, the authors created a dynamic composite factor that adjusts its exposure to the HML, RMW and CMA factors according to whether the BM and cashflow spreads of these factors are high compared to historical levels. Net of transaction costs, their dynamic composite factor has a Sharpe ratio that is 52% higher than that of a static factor that has constant and equal exposure to the HML, RMW and CMA factors, and has a highly significant monthly alpha of 0.224% (t-stat= 3.96) even after allowing for the five factors from Fama and French and the momentum factor.

Their findings led Dai, Haque, and Zurbruegg to conclude:

> “We show that our profitability and investment spreads have significant predictive power in factor returns. Additionally, we show that controlling for these spreads increases the predictive power of the BM spread. Our results demonstrate that factor returns forecasting needs a joint control for the BM, profitability, and investment spreads, to account for the correlations among these spreads.”

They Added:

> *“Given the strong predictive power of these characteristic spreads, we further develop a dynamic factor that takes into account the current BM, profitability,* and investment spreads for the HML, RMW and CMA factors relative to their historical levels, and which ultimately generates a significantly higher Sharpe ratio than a similar factor that has constant and equal exposure to HML, RMW, *and CMA.”*

## Summary

The empirical findings of Dai, Haque, and Zurbruegg are logical because “ensemble” (multi-metric) strategies tend to work better than single-factor strategies as they benefit from diversification of sources of risk. Importantly, their methodology could be used for factors other than the value factor and that the “value spread”, “profitability spread” and “investment spread” can be computed for any long/short factor by looking at the cash flow characteristics of the stocks comprising the long and short legs of other factors. Of course, using this information to time the market is difficult. For example, while we know that the CAPE 10 provides information on future equity returns (higher values predict lower returns and vice versa), using it as a [timing tool has not proven productive](https://alphaarchitect.com/2017/12/21/the-returns-to-value-strategies-when-valuation-spreads-are-wide/) as cheap (expensive) stocks can get cheaper (more expensive).

References[+]

References

|  |  |
| --- | --- |
| ↑1 | The difference in the BM ratio between the long side of the value and the short side of the value factor portfolio. Imagine when the difference between the value stocks B/M vs the Expensive stocks B/M is extremely high, the return generated from the value factor would also be high. |
| ↑2 | The profitability spread asks to what extent firms in the long leg have higher expected returns than those in the short leg owing to their higher profitability |
| ↑3 | investment spread asks to what extent firms in the long leg invest have lower expected returns than those in the short leg due to more aggressive investment. |

 function footnote\_expand\_reference\_container\_60442\_83() { jQuery('#footnote\_references\_container\_60442\_83').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_60442\_83').text('−'); } function footnote\_collapse\_reference\_container\_60442\_83() { jQuery('#footnote\_references\_container\_60442\_83').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_60442\_83').text('+'); } function footnote\_expand\_collapse\_reference\_container\_60442\_83() { if (jQuery('#footnote\_references\_container\_60442\_83').is(':hidden')) { footnote\_expand\_reference\_container\_60442\_83(); } else { footnote\_collapse\_reference\_container\_60442\_83(); } } function footnote\_moveToReference\_60442\_83(p\_str\_TargetID) { footnote\_expand\_reference\_container\_60442\_83(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_60442\_83(p\_str\_TargetID) { footnote\_expand\_reference\_container\_60442\_83(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
