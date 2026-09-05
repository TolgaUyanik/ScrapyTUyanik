---
title: "A Modification to the Flexible Asset Allocation Model"
slug: "a-modification-of-flexible-asset-allocation"
date: "2014-12-04"
modified: "2020-03-23"
url: "https://alphaarchitect.com/a-modification-of-flexible-asset-allocation/"
categories: ["Research Insights", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# A Modification to the Flexible Asset Allocation Model

> This topic is about Flexible Asset Allocation, a concept I first got wind of thanks to this blog.(1) Thanks to input from David Varadi of […]

This topic is about Flexible Asset Allocation, a concept I first got [wind of thanks to this blog.](http://stagingaa.wpengine.com/blog/2013/10/07/flexible-asset-allocation-assessment/#.VHzOLfldWnE)(1)
Thanks to input from [David Varadi of CSS Analytics](https://cssanalytics.wordpress.com/2014/10/27/flexible-asset-allocation-with-conditional-correlations/), I have also extended this algorithm by injecting a better correlation ranking system, available in my IKTrading package on my [Github.](https://github.com/IlyaKipnis)
Finally, thanks to input from the paper’s authors, I updated the algorithm to allocate weights before dropping assets with a negative momentum. The results show marginal improvement, which was covered in a [recent blog post of mine.](http://quantstrattrader.wordpress.com/2014/11/25/an-update-on-flexible-asset-allocation/)
However, one other phenomenon pointed out to me by one of my readers, Mr. Helmuth Vollmeier, a multi-decade industry veteran, is that in a significant number of instances, the FAA algorithm will have a tie in rankings, with one of the top three rankings (as per the paper) belonging to the risk-free, cash security, in this case, VFISX. From the perspective of a standalone asset, VFISX has a very strong risk to reward ratio, with the following statistics, from the beginning of 1998 to Oct. 30, 2014:
**Annualized Return:** 3.94%
**Annualized Sharpe Ratio (Rf=0%):** 1.70%
Furthermore, here is its equity curve and drawdown profile:

![](https://alphaarchitect.com/wp-content/uploads/2020/03/IBNdq7I.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Overall, the performance is solid from a risk/reward ratio profile, but the returns are relatively low, as we would expect for a risk-free asset. Therefore, in the event of a tie, one interpretation is that by investing in the risk-free asset, one effectively “keeps money off the table.” Is this the correct interpretation? Well, here are the results using the original seven assets from the paper, tested from the start of 1998 to October 30, 2014.

![](https://alphaarchitect.com/wp-content/uploads/2020/03/DklfNct.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Here is an invested growth chart, along with drawdowns:

![](https://alphaarchitect.com/wp-content/uploads/2020/03/RfECf8Q.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

In short, the results seem rather intuitive. By removing a high reward to risk instrument in the event of ties, we increase our overall returns, but pay for it with a slightly worse downside risk. At the end of the day, the tradeoff appears to be a case of splitting hairs (at least when not accounting for commissions and slippage), as the profiles basically overlap when applying the stepwise correlation rank algorithm, which produces a superior result than using a one-pass correlation matrix ranking.
I will release a corresponding blog post on my own blog as an appendix containing the functions and code used to generate the results, for those actually interested in the formal R programming.
Thanks for reading.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | Ilya Kipnis is the author of [QuantStrat TradeR](http://www.quantstrattrader.wordpress.com/). We like the work he does on his blog and his willingness to share his source code on various algorithms with the public. We asked Ilya if he’d be interested in sharing some of his recent insights… |

 function footnote\_expand\_reference\_container\_55767\_45() { jQuery('#footnote\_references\_container\_55767\_45').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_55767\_45').text('−'); } function footnote\_collapse\_reference\_container\_55767\_45() { jQuery('#footnote\_references\_container\_55767\_45').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_55767\_45').text('+'); } function footnote\_expand\_collapse\_reference\_container\_55767\_45() { if (jQuery('#footnote\_references\_container\_55767\_45').is(':hidden')) { footnote\_expand\_reference\_container\_55767\_45(); } else { footnote\_collapse\_reference\_container\_55767\_45(); } } function footnote\_moveToReference\_55767\_45(p\_str\_TargetID) { footnote\_expand\_reference\_container\_55767\_45(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_55767\_45(p\_str\_TargetID) { footnote\_expand\_reference\_container\_55767\_45(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
