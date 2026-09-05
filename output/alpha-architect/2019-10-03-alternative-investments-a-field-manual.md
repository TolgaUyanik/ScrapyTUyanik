---
title: "Alternative Investments – A Field Manual"
slug: "alternative-investments-a-field-manual"
date: "2019-10-03"
modified: "2019-10-03"
url: "https://alphaarchitect.com/alternative-investments-a-field-manual/"
categories: ["Financial Planning", "Factor Investing", "Guest Posts"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Alternative Investments – A Field Manual

> It’s not a perfect world out there and often times alternative funds are mischaracterized, misused, and not put through a rigorous enough portfolio construction process. […]

It’s not a perfect world out there and often times alternative funds are mischaracterized, misused, and not put through a rigorous enough portfolio construction process. It’s my hope that I can forewarn you of the proverbial landmines and better prepare you to invest (or not invest) in the alternative space.(1)(2)

## Identifying a Unique Return Stream

The first step most analysts make with alternative investments is to look at the correlation between the returns of the alternative investment and stocks. The analyst then uses this correlation to determine if the investment is providing the desired diversification to the portfolio or not. This is a good first step, but the process of evaluation shouldn’t stop there.

Let’s use merger arbitrage mutual funds as an example of how only looking only at correlations can lead an investor astray (a background on merger arbitrage is [available here](https://alphaarchitdev.wpengine.com/2018/01/25/a-quantitative-strategy-for-enhancing-merger-arbitrage/), and a [podcast on it is here](https://www.aqr.com/Insights/Podcasts/The-Curious-Investor/Season-Two/Why-Merger-Arb-Works)). I have a table that shows the correlation between four of the largest merger arbitrage funds and their correlation to US stocks:

![](https://alphaarchitect.com/wp-content/uploads/2019/08/image-4.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

A quick glance a the table makes It’s pretty easy to draw a knee-jerk conclusion that merger arbitrage funds (with aggregate 64% correlation with the market) are not a worthwhile alternative investment. However, when we take that analysis one step further you’ll find that the knee-jerk response is likely wrong.(3)

## Help Arrives – Regression Analysis

So the first step of the analysis turned out what at first glance appears to not be a unique return stream. As a means of sorting out just how unique of a return stream this is, the analyst should follow up the correlation study with a regression analysis on the funds using all known factors to determine 1) do they have sensitivity to return sources that we want and 2) do they have a unique return source that might be worth paying for?

Let’s do the regression and discuss what we find:

![](https://alphaarchitect.com/wp-content/uploads/2019/09/image-1-1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

What we see from the analysis, above, is the following:

1. All the funds have various factor loadings, but all of them tend to have a pretty persistent (but small) factor loading to US stock market risk or MKT.
2. Given how volatile the MKT return stream is compared to the others, this is what likely drives the persistently high correlation to US stocks.
3. Surprisingly, the funds tend to have negative factor loadings to other known factors, especially Betting Against Beta or BAB.
4. Most of the funds have a positive and statistically significant alpha.
5. The equal-weight portfolio of all four funds shows the benefits of diversification – all the factor loadings tend to moderate.
6. The equal-weight portfolio of all four funds shows a statistically significant alpha of 1.76%! This is what we were looking for…**despite the high correlation to stocks, these funds (in aggregate) deliver a return stream that is unique and uncorrelated to all other factors in our regression!**

So we found **alpha** when we were looking for a **unique and uncorrelated source of return**, what gives?(4)

## We Have Identified An Alternative Return Source, Now What?

Now that we have identified a unique and uncorrelated return source, we need to “clean” the returns by hedging out all other unwanted risks (factors). This “cleaning” will allow us to use the return source in portfolios in a more efficient way as we can use the return and risk from the “alpha” and just assume a 0% correlation to all other return sources. This makes portfolio construction (the next step) a little easier. If you were able to more complex modeling, this step may be unnecessary.

We can see from the regression of the equal-weight portfolio that the only statistically significant risk is to the MKT at 0.08 beta. However, our regression also shows that the equal-weight portfolio has very close to a statistically significant negative beta to BAB (low beta) and QMJ (quality). It is important to note these risks as they can be very helpful in deciding which tool(s) to use to hedge risks.

For example, let’s consider two liquid and available hedging options 1) a mutual fund that owns a portfolio of bonds and is short an S&P future and 2) a fund that owns low beta stocks and shorts an equal dollar amount of high beta stocks. Option 1 would have an expected beta of approximately -1 (its short stocks) but would have a negative expected risk premium (short MKT which costs about 5.5% per year and long bonds which might earn back 1.5% per year). Option 2 would have an expected risk premium of approximately 0% (long and short equal dollar amount of stocks) but would also have a beta to MKT of about -1 as well as having positive beta to BAB and QMJ. Therefore, Option 2 would appear to be a much better hedge for merger arbitrage funds as it would not only undo the unwanted MKT beta but also the negative BAB and QMJ betas as well!

When we look at the resulting portfolio (22.5% in each of the four merger arbitrage mutual funds and 10% in the fund that is long low beta stocks and short high beta stocks) we see the following performance:

![](https://alphaarchitect.com/wp-content/uploads/2019/09/image-2-2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

We see a return stream that delivers a Sharpe ratio of 1.26 with no correlation to US stocks (or bonds which isn’t shown) and that delivered a 2.34% return per year over the last 7 years. This is fantastic right, we’ll all be like Hans Gruber and retire to a beach drinking Mai Tais while collecting our 2.34% return…unless you happen to be somewhere far off on the right-hand side of the wealth distribution, 2.34% doesn’t quite sound “beach and Mai Tai worthy,” does it?

## Portfolio Construction – The Final Piece

So far, we have identified a unique and uncorrelated return stream and we have “cleaned” the return stream by hedging out as many of the risks an unintended bets that we could in the most capital-efficient way possible. However, there is one final piece – Portfolio Construction.

Why does portfolio construction matter? – let’s look at a couple of examples:

### Portfolio Construction Example 1

Let’s take a naive construction approach and add a 10% allocation to the alternative investment portfolio above and keep a 90% allocation to a balanced index fund of US stocks and bonds:

![](https://alphaarchitect.com/wp-content/uploads/2019/09/image-3.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

What happened? I thought we just sprinkled the magic fairy dust of “alpha” all over this portfolio and the results got worse — What’s going on?

* The return of our benchmark or baseline portfolio was 10.09% over this period of time, so when we decrease the allocation by 10% and allocate elsewhere, the 10% would have to earn a higher return than the rest of the portfolio to improve the return.
* The 10% allocation to the alternative investment portfolio did do its job – volatility was decreased from 7% down to 6.4% and the Sharpe ratio increased from 1.32 to 1.36. This is what one would expect
* Most people get this far and assume that allocating to alternative investments can’t help portfolios (because they don’t improve returns using a simple allocation framework) and that a simple portfolio of stocks and bonds is far superior. If this is all the farther you go into portfolio construction, then I am inclined to agree – you would be better off using only traditional stocks and bonds.

### Portfolio Construction Example 2

In the book “Seven Habits of Highly Effective People”, Steven Covey discusses beginning with the end in mind. Let’s do that with portfolio construction – Let’s try and end up with a portfolio that has a 0.4% excess return over our benchmark. This means that we would have to allocate 20% of our portfolio to the alternative investment portfolio at a 2% “alpha” and still have the remaining 80% of the portfolio have a beta of 60% to MKT and 40% to bonds. How is this possible? Leverage! Corey Hoffstein at Newfound Research has a great blog post [here](https://blog.thinknewfound.com/2017/12/portable-beta-making-returns-youre-already-getting/) and “Jake” from the blog Econompic has a similar post [here](http://econompicdata.blogspot.com/2016/07/the-case-for-hedge-funds.html). I won’t rehash what’s in the blog posts, but leverage works in this example not because we are looking to increase the total risk of the portfolio, but because we are using the leverage to buy a diversifying return source…but leverage is still risky!

So, what does this portfolio look like?

![](https://alphaarchitect.com/wp-content/uploads/2019/09/image-4.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

We see the following:

* Results were a little better than expected with an excess return closer to 1%. This is likely a result of a mild rebalancing bonus from adding an uncorrelated asset to the portfolio.
* Risk level was largely unchanged from the benchmark or starting portfolio…this is because we were trying to target a similar beta to MKT and bond risk.
* Sharpe ratio improved quite a bit – what one should expect from earning a higher return at the same level of risk.
* Max drawdown did decrease which is a good example of some additional diversification from including the uncorrelated returns.

Generally, I would say that in this instance, liquid alternative investments were a good addition to the portfolio and did their job nicely. This just goes to show you the importance of portfolio construction because Portfolio Construction Example 1 & 2 used the same raw materials but got very different results!

## Conclusions

Alternative investments aren’t for everyone. To effectively use them, an investor has to be able to do the following:

* Identify uncorrelated sources of risk and return (hard)
* “Clean” the return sources to isolate the wanted return and hedge out the other unintended bets (harder)
* Have the tools and portfolio construction know-how to build a portfolio that keeps the desired betas to traditional return sources (stocks and bonds) but also incorporates the alternative investments into portfolios (hardest)

Skip any one of the three critical steps and it is likely investors will end up with a portfolio that differs (perhaps dramatically) from what one would expect. This variance from the expectation is often the reason why alternative investments don’t look good in the financial press where the writers use simplistic assumptions on portfolio construction. Before investing in alternative investments, you need to make an honest assessment of your ability to do all three of the steps I’ve laid out. If you can’t (and that’s not a bad thing), picking up your toys and moving to the non-alternative sandbox is the best course of action.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | A little twitter defense disclosure; alternative assets aren’t for everyone! However, if you’re one of those on the fence about alternative investing I want to walk you through the process and empower the alternative investor in you with some knowledge. |
| ↑2 | Another great article that covers the use of alternatives in risk management can be found in a [post](https://alphaarchitdev.wpengine.com/2018/04/05/tail-risk-hedging-alternative-approach-risk-management/) by Aaron Brask. |
| ↑3 | We are aware that merger arbitrage can have a dynamic beta that shifts to being positive at the worst time (i.e., market is blowing up). Merger arbitrage is not a perfect alternative strategy — nothing is — but it serves as a nice example for the point I am making in this piece. |
| ↑4 | Initially, we all think of “alpha” as the Holy Grail of the investment universe **Asset Manager Expertise**!!!!! Well, not so fast. In my mind there are two sources of “alpha” 1) unique manager skill and 2) an intercept from a regression that didn’t contain enough factors to make the intercept 0% or not statistically significant. I am sure that version 1 of “alpha” (unique manager skill) exists but I am not sure I would want it in my portfolio (see my answer [here](https://abnormalreturns.com/2019/07/11/blogger-wisdom-genuine-surprises/)). The “alpha” in the regression, above, is definitely an example of the second kind of alpha – an incorrectly specified regression. In other words, we’ve found returns that are uncorrelated and unique from the market and all the other factors in our regression, NOT ACTUAL ALPHA! (BUT WE DO HAVE STATISTICALLY SIGNIFICANT REGRESSION TO THE MARKET, AND ALMOST SIGNIFICANT TO BAB AND QMJ). This is a little beyond the scope of this blog post, but we can test to see how correlated the “alpha” is for all of the funds. This will show that the “alpha” is highly correlated and likely a common risk factor/return source between all of the funds. Therefore, it should have been an independent variable in the regression. If we then take the alpha from the equal-weighted portfolio and include it in the regression as an independent variable, the “alpha” for these funds would all likely go away or become statistically insignificant. |

 function footnote\_expand\_reference\_container\_49883\_126() { jQuery('#footnote\_references\_container\_49883\_126').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_49883\_126').text('−'); } function footnote\_collapse\_reference\_container\_49883\_126() { jQuery('#footnote\_references\_container\_49883\_126').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_49883\_126').text('+'); } function footnote\_expand\_collapse\_reference\_container\_49883\_126() { if (jQuery('#footnote\_references\_container\_49883\_126').is(':hidden')) { footnote\_expand\_reference\_container\_49883\_126(); } else { footnote\_collapse\_reference\_container\_49883\_126(); } } function footnote\_moveToReference\_49883\_126(p\_str\_TargetID) { footnote\_expand\_reference\_container\_49883\_126(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_49883\_126(p\_str\_TargetID) { footnote\_expand\_reference\_container\_49883\_126(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
