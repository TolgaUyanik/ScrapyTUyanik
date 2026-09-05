---
title: "Is Sector-neutrality in Factor Investing a Mistake?"
slug: "factor-investing-and-sector-neutrality"
date: "2022-04-07"
modified: "2022-06-13"
url: "https://alphaarchitect.com/factor-investing-and-sector-neutrality/"
categories: ["Research Insights", "Factor Investing", "Larry Swedroe", "Academic Research Insight"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Is Sector-neutrality in Factor Investing a Mistake?

> Long-only factor performance is more likely to degrade from sector neutralizing—keeping the sector component produced better long-only factors in 78 percent of the trials. The largest negative from sector neutralizing occurred for the value-weighted long-only factors that trade large stocks, arguably the most investable portfolio.

Firm characteristics such as [size](https://alphaarchitect.com/2020/12/18/is-size-a-useful-factor-or-not/), [book-to-market ratio](https://alphaarchitect.com/2014/10/07/the-quantitative-value-investing-philosophy/), [profitability](https://alphaarchitect.com/2020/12/03/profitability-and-future-stock-returns/), and [momentum](https://alphaarchitect.com/2015/12/01/quantitative-momentum-investing-philosophy/) have been found to be correlated with expected returns. The predictive power of these characteristics may stem from their industry component, their firm-specific component, or both. For example, while the study “[Do Industries Explain Momentum](https://onlinelibrary.wiley.com/doi/abs/10.1111/0022-1082.00146),” found that momentum in stocks stems from the industry component, the study “[The Other Side of Value: The Gross Profitability Premium](https://www.cfainstitute.org/en/research/cfa-digest/2013/05/the-other-side-of-value-the-gross-profitability-premium-digest-summary),” found that the firm-specific component of characteristics contains most of the information, suggesting that an investor benefits from forming portfolios that neutralize sector exposures.

Sina Ehsani, Campbell Harvey, and Feifei Li contribute to the factor-based investing literature with their November 2021 study, “[Is Sector-neutrality in Factor Investing a Mistake](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3959116)?,” in which they examined whether the *within* (firm-specific) component of stock characteristics contains more information about the cross-section of expected returns than the *across* (sector) component. For example, a technology firm may have a high book-to-market ratio (BM) relative to other tech firms, but a low BM relative to non-tech firms. Although the firm would be considered a value company compared to other tech firms, a long-short sort on BM will short this firm because firms in the tech sector generally have a lower BM.

To answer their question, they used empirical bootstraps of historical data of factors, constructed using various portfolio construction techniques. Their measure of performance was the Sharpe ratio(1). Their data sample spanned the period 1963 to 2020. Following is a summary of their findings:

* The within (firm-specific) component of stock characteristics contains more information about the cross-section of expected returns than the across (sector) component. Size, value, and investment factors showed the largest gains.
* The long-short investor likely gains from sector neutralizing—keeping the sector component produced better long-short factors in only 20 percent of the trials.
* The within component of BM was strong in identifying the underperforming stocks of each sector that should go in the short leg, but did not predict the outperforming stocks of the long leg.
* ***Long-only factor performance is more likely to degrade from sector neutralizing***—keeping the sector component produced better long-only factors in 78 percent of the trials. The largest negative from sector neutralizing occurred for the value-weighted long-only factors that trade large stocks, arguably the most investable portfolio.

![](https://alphaarchitect.com/wp-content/uploads/2022/04/image-800x651.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

Their findings led Ehsani, Harvey and Li to conclude:

> “Across BM is better at predicting the outperforming sectors and the within BM is better at predicting the underperforming stocks within each sector. In retrospect, the maximum Sharpe-ratio strategy of the long–short value factor would be to form the long leg using sector BMs and to form the short leg using stock-specific BMs.”

In the investment world, different fund families take different approaches. For example, AQR uses sector neutrality in its long-short funds and also uses it in its long-only funds. Dimensional, which only has long-only funds, does not use a sector neutrality approach. Instead, it uses bands that constrain sector allocation from drifting too far from the eligible universe. And neither Bridgeway’s long-only funds nor Alpha Architect’s long-only funds use sector neutrality.

## **Investor Takeaway**

Investors who pursue factor investing face numerous choices—choices that don’t end once the set of factors they wish to invest in has been chosen. One of the choices is whether the factors should be sector neutralized. Ehsani, Harvey, and Li provided information that can help you make an informed decision.

I would add that sector neutrality does reduce the risk of the behavioral problem of tracking variance (or error) regret. Thus, even though the research shows superior historical results for long-only portfolios that don’t consider sector neutrality, investors prone to that behavioral error might be willing to accept that trade-off. The tracking variance risk is why some funds might choose sector neutrality, as they recognize that most retail investors, and even most institutional investors, don’t have the required discipline to ignore negative short-term tracking variance.

Finally, the Ehsani, Harvey, and Li paper only examined a single factor at a time. However, what should matter most to investors is how that factor interacts with other factors both in the strategy/fund and in the overall portfolio itself. Looking at each factor separately (as the paper does) gets you the “best” answer for just that factor. But what really matters is the impact on the total portfolio. That is the essence of the “[Larry Portfolio](https://www.crispydoc.com/2020/07/27/understanding-the-larry-portfolio/)” (as described in “[Reducing the Risk of Black Swans](https://www.amazon.com/Reducing-Risk-Black-Swans-Volatility/dp/069206074X/ref=sr_1_1?keywords=reducing+the+risk+of+black+swans&qid=1637356442&qsid=131-2058641-6105015&sr=8-1&sres=069206074X%2C0615992978%2CB018EX1UY4&srpt=ABIS_BOOK)”) in which you can take a lot of factor risk to potentially get higher returns, and balance that with high-quality fixed income exposure to dampen the risk of the full portfolio.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | assuming that investors care only about mean and variance, though some investors may care more about raw returns |

 function footnote\_expand\_reference\_container\_72247\_57() { jQuery('#footnote\_references\_container\_72247\_57').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_72247\_57').text('−'); } function footnote\_collapse\_reference\_container\_72247\_57() { jQuery('#footnote\_references\_container\_72247\_57').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_72247\_57').text('+'); } function footnote\_expand\_collapse\_reference\_container\_72247\_57() { if (jQuery('#footnote\_references\_container\_72247\_57').is(':hidden')) { footnote\_expand\_reference\_container\_72247\_57(); } else { footnote\_collapse\_reference\_container\_72247\_57(); } } function footnote\_moveToReference\_72247\_57(p\_str\_TargetID) { footnote\_expand\_reference\_container\_72247\_57(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_72247\_57(p\_str\_TargetID) { footnote\_expand\_reference\_container\_72247\_57(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
