---
title: "How Trend Following Strategies Shape Return Distributions"
slug: "how-trend-following-strategies-shape-return-distributions"
date: "2020-06-29"
modified: "2022-05-20"
url: "https://alphaarchitect.com/how-trend-following-strategies-shape-return-distributions/"
categories: ["Crisis Alpha", "Research Insights", "Trend Following", "Basilico and Johnsen", "Academic Research Insight"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# How Trend Following Strategies Shape Return Distributions

> Some Observations on Trend Following: A Binomial Perspective David M. Modest Working Paper, QLS Partners LP A version of this paper can be found here Want […]

## Some Observations on Trend Following: A Binomial Perspective

* David M. Modest
* Working Paper, QLS Partners LP
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3397783)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

Crisis Alpha is on everyone’s mind right now, maybe due to a bit of recency bias, but regardless of the reason thinking of and preparing for “tail-risk” is best done before it’s needed. [Trend following](https://alphaarchitect.com/2015/08/13/avoiding-the-big-drawdown-with-trend-following-investment-strategies/) is one such strategy that is rooted in academic research and is an enticing way to manage large drawdown risk, though not without the occasional trip on the [“Pain Train.”](https://alphaarchitect.com/2019/06/26/trend-following-the-epitome-of-no-pain-no-gain/) The author, David Modest, uses a stationary binomial framework, resembling a “coin-flip”, within an efficient market context to simplify markets and explore the features of a simple trend-following (TF) strategy. The methodology of the binomial framework is that a long/short signal is generated from a coin-flip: if heads, the strategy goes long, if the following flip comes up heads again, the strategy makes money.  If the flip is tails, the strategy goes short and if the next flip is again tails, the strategy makes money.  Profits are governed by a random walk with a constant variance. Two scenarios are examined including (1) heads and tails are equally likely; and (2) heads more likely than tails. In the four-period binomial framework used in this experiment, as table 1 below exhibits, there are sixteen-possible price/profit paths to analyze.

Five observations regarding the behavior of a trend following strategy derived from the coin-flip experiment are discussed.

## What are the Academic Insights?

**Observation #1:**  Trend following and the long-only investment strategy have the same expected profits (returns)  and variance of profits (returns).  They differ in that TF dramatically changes the shape of the distribution of returns and the timing of returns. See Table 1 below.

**Observation #2:** In spite of the lack of predictability in prices, but building on observation #1, TF is able to generate alpha during crisis periods when the long only strategy suffers the most.

**Observation #3:**  Option strategies have a similar impact on the shape of the distribution of returns in terms of timing when profits occur, despite the fact that the mean and variance of the distribution are not affected.(1) Using the binomial framework again, but comparing a long call option strategy to the long-only strategy results in the same expected profit and variance, but a different distribution of outcomes. The long call produces a profit 31.25% of the time (with a loss of the call premium 68.75% of the time).  More importantly, it exhibits a strong positive skew and produces crisis alpha of $35.625. The long-only strategy produces a loss only 31.25% of the time with a skew of zero at the same point in time.

**Observation #4:**  The ability to generate crisis alpha is dependent on the shortness of the period of time used to calculate the trend signal.  A shorter period leads to a faster response to a change in market conditions, although accompanied by higher turnover and trading costs.

![](https://alphaarchitect.com/wp-content/uploads/2020/06/image-22-1200x631.png)

**Observation #5:**  TF will generate profits (losses) under the condition that markets exhibit a consistently positive (negative) trend, even if markets are efficient, and given there is a sufficient period of time for the trend to play itself out. While the range of outcomes for the long only and fast TF are the same, the TF exhibits a higher variance relative to the long only strategy and the timing of when profits or losses occur is again different.

## Why does it matter?

The key takeaway: The methodology used in this article, while vastly simplified, clearly demonstrates that trend following affects the timing of the occurrence of profits and losses when compared to a long-only strategy. As a result of that impact on the pattern of cash flows, it appears that TF strategies are likely to generate crisis alpha in both a world modelled on trend-following as well as the scenario in which trend wasn’t present. A bit of a surprise. The research also indicates that finding and dialing in the appropriate sensitivity of a TF methodology is a critical piece of the puzzle.

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2020/06/image-23-1200x785.png)

> “Consider a futures investment environment that resembles “coin-tossing” with a fair coin.11 There is a fifty percent probability of a head and fifty percent probability of a tail. Upon flipping heads, the investor who is long the futures contract earns a $10 profit, and upon flipping tails the long investor loses $10.  Now consider a (fast) trend-following strategy where the trend follower starts long the market. If heads are tossed, the trend follower stays long, but if tails is tossed the trend follower goes short. This is a fast trend following strategy in that next period’s position only depends on the outcome of this period’s coin toss. As depicted in Table 1, there are sixteen possible outcomes of this four-period investment. The outcomes have been colored coded where green indicates a profitable investment for the fast trend follower and red represents unprofitable investments. The maximum profit for both the long-only and fast trend investors is $40 and the maximum loss is -$40. The maximum loss for the long-only investor occurs when four tails are thrown in a row (path #16) and the maximum loss for the trend investor occurs when the path has maximum mean reversion (relative to the starting point; path #10). The expected profit from both strategies are zero and the variance of profits is 400. The unconditional distributions of profits are identical for the two strategies: 6.25%  of the time the strategies deliver $40 of profit, 25% of the time the strategies earns $20 profit, 37.5% of the time $0 profit, 25% of the time −$20 profit, and 6.25% the strategies both earn −$40.18 However, the dynamic nature of the trend-following strategy changes when the profits and losses occur. It generates $20 of profit during the market crisis (i.e., the states where the cumulative profit from the long-only strategy is −$40). Hence, in this crisis state, the trend-following strategy generates $60 of crisis alpha! “

---

## Abstract

> In this paper, I use a simple binomial framework to show (by counter example) that the existence of positive profits from a trend-following strategy (on a single asset), on its own, provides no prima facie evidence on the efficiency or inefficiency of markets. In addition, I explore the most important feature of time series momentum investment strategies: the return shaping impact of trend following through its dynamic positioning. In a stylized efficient market setting (with no transaction costs), I show that the dynamic nature of trend following shapes when profits and losses occur compared to a buy-and-hold strategy. There is, however, a conservation of “mass” in that gains and losses are shuffled across periods such that the unconditional distribution of profits is unaffected. In this sense, trend following, by construction, generates crisis alpha — for crises where large losses occur over extended periods of time. I also show that fast and slow trend following strategies will shape returns in different ways. Due to its ability to shape when profit and losses occur, trend following can provide significant portfolio diversification and hedging potential for those investors with strategic risk-on exposures.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | see a [recent blog post](https://blog.thinknewfound.com/2020/06/option-based-trend-following/) by Nathan Faber here. |

 function footnote\_expand\_reference\_container\_57532\_67() { jQuery('#footnote\_references\_container\_57532\_67').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_57532\_67').text('−'); } function footnote\_collapse\_reference\_container\_57532\_67() { jQuery('#footnote\_references\_container\_57532\_67').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_57532\_67').text('+'); } function footnote\_expand\_collapse\_reference\_container\_57532\_67() { if (jQuery('#footnote\_references\_container\_57532\_67').is(':hidden')) { footnote\_expand\_reference\_container\_57532\_67(); } else { footnote\_collapse\_reference\_container\_57532\_67(); } } function footnote\_moveToReference\_57532\_67(p\_str\_TargetID) { footnote\_expand\_reference\_container\_57532\_67(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_57532\_67(p\_str\_TargetID) { footnote\_expand\_reference\_container\_57532\_67(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
