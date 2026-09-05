---
title: "Trend-Following: A Deep Dive Into A Unique Risk Premium"
slug: "trend-following-a-unique-risk-premium-explained"
date: "2017-10-18"
modified: "2022-05-12"
url: "https://alphaarchitect.com/trend-following-a-unique-risk-premium-explained/"
categories: ["Research Insights", "Factor Investing", "Trend Following"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Trend-Following: A Deep Dive Into A Unique Risk Premium

> Trend-following strategies have historically been laughed at via the modern academic finance research community. Having first-hand knowledge of that community, we can verify that academic […]

Trend-following strategies have historically been laughed at via the modern academic finance research community. Having first-hand knowledge of that community, we can verify that academic researchers are humans like the rest of us (we checked, academics aren’t robots), and they suffer from group think and confirmation bias. Anything related to momentum and/or trend-following was written off as pseudoscience. We get it. The market is apparently *always efficient* and there is no way one can use past prices to predict future performance.

Roger that. Thanks for the brainwashing.

But investing should be [evidence-based and not faith-based](https://alphaarchitect.com/2016/07/27/evidence-based-investing-requires-less-religion-and-more-reason/). “Evidence-based” is open to interpretation of the so-called evidence, however, the high-level principle of evidence-based investing should revolve around an impossible goal: identifying “truth.” In our quest to find the truth, we opened our minds, hung out with people who had ideas that were 100% against our prior beliefs, and came around to appreciate the potential costs/benefits of trend-following.

Long story short, if you are skeptical of trend-following because there is an academic authority who tells you it is crazy, well, been there done that. We used to be in that camp. But we invite you to at least consider the idea. View trend-following as a risk premium that is probably priced in equilibrium. A “factor,” if you will.

To get the core concept we recommend you start by reading our [piece on the subject.](https://alphaarchitect.com/2015/08/13/avoiding-the-big-drawdown-with-trend-following-investment-strategies/)  
If you are interested in moving beyond the basics I recommend Valeriy Zakamulin’s in-depth [Trend-Following series.](https://alphaarchitect.com/category/education/trend-following-course/)

And if you really want to geek out, you should check out this extremely thorough paper, “[Understanding the Momentum Risk Premium: An In-Depth Journey Through Trend-Following Strategies.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3042173)”

## An In-Depth Journey into the Theory of Trend-Following?

Many investors may not want to read through dense pages of theory associated with trend-following (and cross-sectional momentum), but then again, your an Alpha Architect blog subscriber, so you’ve already got the “geek box” thoroughly checked…maybe you do want to dig in!  
The paper is broken into 4 sections:

* Trend-following theory/models
* Trend-following empirical properties
* Downside protection and the hedging properties of trend-following strategies
* Summary of results

The paper is pretty intense with tons of math (giving me PTSD associated with former financial mathematics classes) so I’ll highlight a few interesting insights and charts from what I feel are interesting insights and takeaways.

I think a paragraph in the conclusion says it all:

> …the traditional diversification approach based on correlations must be supplemented by a payoff approach. However, most risk premia have a concave payoff. The momentum risk premium thus plays a central role as it exhibits a convex payoff, and we know that **mixing concave and convex strategies is key for managing skewness risk in bad times**.

[![](https://alphaarchitect.com/wp-content/uploads/2017/10/trend-smile-1030x747.png)](https://alphaarchitect.com/wp-content/uploads/2017/10/trend-smile.png)  
In short, plugging trend-following strategies into your mean-variance frontier optimizer ain’t gonna work. One needs to think outside the box and consider the tails. How does my portfolio work in extreme scenarios? Are my assets short volatility or long volatility? Most mean-variance-optimized portfolios pool a bunch of “uncorrelated” stuff in a bucket without realizing they are heavily short volatility. To the extent the world muddles along — A-okay — to the extent things get nutty…You’re dead. Trend-following strategies present an opportunity to be long volatility and provide unique portfolio diversification.(1)

And while the class of “trend-following” is interesting, like everything else in life, there is no free lunch. The primary risk associated with trend-following strategies are whipsaws, or trend reversals. In other words, you blow out on a downtrend (or go short) and the asset immediately goes screaming higher, leaving you in the dust. Moreover, trend-following strategies drag on buy and hold most of the time…and this can go on for years. Painful. Costly. Risky.

But hey, what’s the primary lesson of the marketplace? You guessed it: **no pain, no gain.**

---

# Understanding the Momentum Risk Premium: An In-Depth Journey Through Trend-Following Strategies

* Jusselin, Lezmi, Malongo, Masselin, Roncalli, and Dao
* A version of the paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3042173).
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap](https://alphaarchitect.com/category/architect-academic-insights/) Category.

### Abstract:

> Momentum risk premium is one of the most important alternative risk premia. Since it is considered a market anomaly, it is not always well understood. Many publications on this topic are therefore based on backtesting and empirical results. However, some academic studies have developed a theoretical framework that allows us to understand the behavior of such strategies. In this paper, we extend the model of Bruder and Gaussel (2011) to the multivariate case. We can find the main properties found in academic literature, and obtain new theoretical findings on the momentum risk premium. In particular, we revisit the payoff of trend-following strategies, and analyze the impact of the asset universe on the risk/return profile. We also compare empirical stylized facts with the theoretical results obtained from our model. Finally, we study the hedging properties of trend-following strategies.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | Also important to note, cross-sectional “momentum” strategies — long-only or long-short — are typically short-volatility, i.e, they’ll blow up when the world blows up. So this form of “momentum” will help diversify your short-volatility book, but they won’t give you the long-volatility mojo like trend-following. Bottom line: know what you are buying and understand that “momentum” can mean different things to different people. |

 function footnote\_expand\_reference\_container\_32901\_89() { jQuery('#footnote\_references\_container\_32901\_89').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_32901\_89').text('−'); } function footnote\_collapse\_reference\_container\_32901\_89() { jQuery('#footnote\_references\_container\_32901\_89').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_32901\_89').text('+'); } function footnote\_expand\_collapse\_reference\_container\_32901\_89() { if (jQuery('#footnote\_references\_container\_32901\_89').is(':hidden')) { footnote\_expand\_reference\_container\_32901\_89(); } else { footnote\_collapse\_reference\_container\_32901\_89(); } } function footnote\_moveToReference\_32901\_89(p\_str\_TargetID) { footnote\_expand\_reference\_container\_32901\_89(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_32901\_89(p\_str\_TargetID) { footnote\_expand\_reference\_container\_32901\_89(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
