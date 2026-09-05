---
title: "More on the Factor Investing Replication Debate"
slug: "more-on-the-factor-investing-replication-debate"
date: "2021-03-26"
modified: "2022-05-21"
url: "https://alphaarchitect.com/more-on-the-factor-investing-replication-debate/"
categories: ["Volatility (e.g., VIX)", "Research Insights", "Factor Investing", "Basilico and Johnsen", "Academic Research Insight", "Low Volatility Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# More on the Factor Investing Replication Debate

> Open Source Cross-Sectional Asset Pricing Andrew Chen and Tom Zimmermann Working paper A version of this paper can be found here What are the research questions? […]

## Open Source Cross-Sectional Asset Pricing

* Andrew Chen and Tom Zimmermann
* Working paper
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3604626)

## What are the research questions?

There has been a wave of articles (and press) suggesting that academic research suffers from a replication crisis. A “replication crisis” simply means that other researchers are unable to replicate the results from prior research using similar experimental conditions.

Psychology seems to be the field that has received the most scrutiny, but financial economics has also received criticism. We’ve covered the subject fairly extensively, and the research we’ve discussed has been one-sided in the direction of, “most financial research is bogus”. (some example articles are [here](https://alphaarchitect.com/2017/10/13/replicating-anomalies/), [here](https://alphaarchitect.com/2017/03/03/evidence-based-investing-take-alpha-shove/), [here](https://alphaarchitect.com/2016/06/28/backtesting-strategies-based-multiple-signals-beware-overfitting-biases/), and [here.](https://alphaarchitect.com/2017/09/13/what-happens-when-you-data-mine-2-million-fundamental-quant-strategies/)).(1)

But academic finance researchers don’t sit quietly when someone suggests that their efforts are a big waste of time. Larry [recently covered](https://alphaarchitect.com/2021/03/23/is-there-a-replication-crisis-in-finance/) an excellent piece from researchers associated with AQR which suggests that the “replication crisis” in finance really isn’t a crisis at all.

The article discussed below only reinforces the message from the AQR researchers: there isn’t a replication issue in academic finance research.

But the real contribution of this paper’s authors is to provide transparent access to the algorithms and data sources the generated the results in the first place. (similar to [what AQR did](https://github.com/bkelly-lab/GlobalFactor)).

I’ll borrow the words from the authors:

> In our view, an open-source dataset is essential because recent studies cast doubt on the credibility of the entire cross-sectional asset pricing literature

## What are the Academic Insights?

1. There isn’t a “replication crisis” in academic finance.

But don’t take the authors’ word for it: Prove it yourself. And oh by the way, here are the resources for you to conduct your due diligence:

* [Github Code](https://github.com/OpenSourceAP/CrossSection)

## Why does it matter?

This paper, similar to the [AQR paper](https://www.aqr.com/Insights/Perspectives/The-Replication-Crisis-That-Wasnt), serves as a counterbalance to the argument that academic research is a bunch of trash and cannot be relied upon. But more importantly, the authors of this paper provides the resources that will allow independent researchers to transparently investigate the findings from any given research paper.

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2022/04/replication-rates-800x800-1.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> We provide data and code that successfully reproduces nearly all cross-sectional stock return predictors. Our 319 characteristics draw from previous meta-studies, but we differ by comparing our t-stats to the original papers’ results. For the 161 characteristics that were clearly significant in the original papers, 98% of our long-short portfolios find t-stats above 1.96. For the 44 characteristics that had mixed evidence, our reproductions find t-stats of 2 on average. A regression of reproduced t-stats on original long-short t-stats finds a slope of 0.90 and an R^2 of 83%. Mean returns are monotonic in predictive signals at the characteristic level. The remaining 114 characteristics were insignificant in the original papers or are modifications of the originals created by Hou, Xue, and Zhang (2020). These remaining characteristics are almost always significant if the original characteristic was also significant.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | If we had our druthers, we rather bury our heads in the sand and take academic research as gospel because we rely on this research to inform our investment decisions! |

 function footnote\_expand\_reference\_container\_62025\_59() { jQuery('#footnote\_references\_container\_62025\_59').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_62025\_59').text('−'); } function footnote\_collapse\_reference\_container\_62025\_59() { jQuery('#footnote\_references\_container\_62025\_59').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_62025\_59').text('+'); } function footnote\_expand\_collapse\_reference\_container\_62025\_59() { if (jQuery('#footnote\_references\_container\_62025\_59').is(':hidden')) { footnote\_expand\_reference\_container\_62025\_59(); } else { footnote\_collapse\_reference\_container\_62025\_59(); } } function footnote\_moveToReference\_62025\_59(p\_str\_TargetID) { footnote\_expand\_reference\_container\_62025\_59(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_62025\_59(p\_str\_TargetID) { footnote\_expand\_reference\_container\_62025\_59(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
