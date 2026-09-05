---
title: "Digging Deeper into Adaptive Asset Allocation"
slug: "digging-deeper-into-adaptive-asset-allocation"
date: "2016-06-20"
modified: "2022-05-24"
url: "https://alphaarchitect.com/digging-deeper-into-adaptive-asset-allocation/"
categories: ["Interviews", "Book Reviews", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Digging Deeper into Adaptive Asset Allocation

> In some ways, investing is simple. After all, we all want the same things. High returns. Low volatility. Small max drawdowns. Unfortunately, it’s very difficult–if […]

In some ways, investing is simple. After all, we all want the same things. High returns. Low volatility. Small max drawdowns.

Unfortunately, it’s very difficult–if not impossible–to have your cake and eat it too.

There are always tradeoffs among these desires that have to be managed by investors. Want low volatility? Be willing to accept lower returns. Want to maximize returns? You may have some ugly max drawdown events. It’s a like a game of whack-a-mole, where when you hit the mole with the hammer, another one just pops up someplace else. It’s hard to wack all the moles at the same time. Perhaps the best investment strategies try to strike a balance among them.

This is the goal of a new book, “[Adaptive Asset Allocation: Dynamic Global Portfolios to Profit in Good Times – and Bad](https://www.amazon.com/Adaptive-Asset-Allocation-Dynamic-Portfolios/dp/1119220351),” written by Adam Butler, Michael Philbrick, and Rodrigo Gordillo, which is the group who runs the finance blog, [GestaltU](http://gestaltu.com/), and [ReSolve Asset Management](http://www.investresolve.com/). The authors argue that by using sophisticated modern portfolio management techniques, you can engineer an intelligent long-term financial plan that can give you high returns, with low volatility, while managing tail risks.

[![book cover](https://alphaarchitect.com/wp-content/uploads/2016/06/book-cover.png)](https://alphaarchitect.com/wp-content/uploads/2016/06/book-cover.png)

Adam, Michael, and Rodrigo’s new book: Adaptive Asset Allocation

We’re fans of anything that promotes investor education, which means we like the GestaltU blog and we’re fans of the team’s new book. If you’re looking to learn more about cutting edge quantitative finance, no matter whether it relates to principal component analysis, risk parity, or new thoughts on Harry Brown’s Permanent Portfolio, this book is an enjoyable read that provides insights throughout.

We sat down with Adam Butler recently, and asked him some tough questions related to the many concepts behind Adaptive Asset Allocation.

Below is our interview with Adam:

**AA**: You mentioned in the book that you had a backtest that involved timing the Russell 2000 which showed 50% CAGRs and Sharpe Ratio > 4. But when you tried to trade it, it blew up after a few weeks and you lost 25% of your money. We’ve certainly had experiences like that. Humbling, but instructive. How do you guard against the dangers of data mining?

**Adam**: Let’s go back to a simple axiom: there is no universal well of excess returns from which every investor can draw; alpha is a zero-sum game. For one investor to generate returns that are above average, an equal dollar value of investors must endure returns that are below average. So the first step in avoiding data-mining bias is to identify the market ‘losers’ that you are going to take advantage of. That is, which investors are making systematic errors, and why?

As you’ve identified in your own articles, perhaps the most consistent investor mistake is extrapolation – in either direction. Value is predicated on investors observing an extreme negative trend in fundamentals and pricing in a linear continuation of that trend. In fact what happens is that fundamentals tend to revert to the mean over the long-term, so fundamentals are rarely as bad as investors price in, and prices eventually recover to correct this. Momentum is also driven by extrapolation in both directions, which manifests in herding behavior, and over- and under-reaction to changes in fundamentals.

Once you’ve identified the ‘willing losers’ on the other side of your trades, and the biases that lead them to make the same errors over and over, there is one more critical step. You need to identify limits to arbitrage. That is, why have smart investors not already recognized these sources of returns and deployed capital to arbitrage away the opportunity.

Only once you’ve identified a likely source of returns, and identified reasonable [limits to arbitrage](https://alphaarchitect.com/2015/08/17/the-sustainable-active-investing-framework-simple-but-not-easy/), should one begin to test their idea with backtesting. Then backtesting becomes a hypothesis test, with roots in the scientific process. Tests are run on historical data to determine if portfolios exposed to the chosen risk premium perform better (and portfolios negatively exposed perform worse) than a naïve portfolio, such as the market cap weighted portfolio, or the equal weight portfolio. This is typically evaluated using statistical tests.

If a source of excess returns works in one market, it should bolster confidence substantially to observe that it works the same way in other markets and, where possible, across asset classes. If a factor seems to only work in a few markets, and not in others, it is probably just statistical noise and one shouldn’t rely on persistence out of sample.

It’s also important to test a strategy in different time periods. It’s relatively easy with modern technology and data sources to test strategies back to the early 2000s. This is useful for prototyping. But once you’ve identified a factor that makes sense, is pervasive across markets, and robust to different specifications, it is critical to put in the extra effort to test it back through earlier periods. You should observe the same character across sub-periods, though all strategies will wax and wane in terms of the strength of the premium.

It’s critical to choose neutral parameters that are consistent with your hypothesis, but not rely on any particular specification. For example, the value premium can be harvested by sorting on P/B, P/E, P/CF, EV/EBITDA, P/S, etc. Any one of these should work about the same over the long-term, so the research process should not be about identifying which one is the best. Rather, all of these specifications should be expected to work, and a thorough researcher will test them all, and average the results to determine the true power of the underlying factor. The same is true for momentum. Much of the momentum literature focuses on past 12 months returns, with a skip month. But if momentum is a genuine risk premium, it should work well at other lookbacks as well, like 3 months, 6 months, etc. And in fact it does.

There are more advanced tests of significance, for example tests of random portfolios, that I won’t get into here. And of course there are lots of other nuances in strategy development. But the most important by far are the identification of willing losers and limits to arbitrage, along with pervasiveness across markets; persistence across time periods, and; insensitivity to parameter specification. If these criteria are well met, you are on the right track.

**AA**: In your discussion regarding estimating volatility, you tend to focus on recent volatility to provide estimates for the future. Do you ever consider tail risk measures?

**Adam**: We have tested a wide variety of ways to measure risk, including advanced methods involving elementary machine learning, and methods from Extreme Value Theory. We also follow the quantitative finance literature on the topic quite closely, as this is a topic of great interest to most quants. In our own investigations, we have seen little benefit from using tail risk measures, such as downside deviation, VaR, CVaR, CDaR or EVaR in measuring risk for risk budgeting purposes or optimization. The primary challenge is that risk information decays very quickly, so the fact that an asset had a cluster of very large losses nine months ago provides almost no information about how the asset will behave tomorrow, or this week.

The literature we’ve seen concludes that relatively simple measures, such as EWMA, perform just as well as much more complicated methods (like multivariate GARCH), and have the added benefit of parsimony. We have also tested integrating higher moments, like skewness and kurtosis into our risk calculations, but in our analysis they haven’t added much value.

I would mention one other observation that I think many nascent quants may take issue with. We are equally concerned with upside volatility as we are with downside volatility. When assets move into a period of accelerating upward movement, upside daily changes increase accordingly. Yet an expanding range often occurs near the end of a move. As a result, it is prudent to reduce exposure during these periods to keep overall risk exposure constant, as what goes up with large moves usually comes down with the same large magnitude moves.

**AA**: You mention naïve diversification requires a well-specified universe, but since this type of covariance matrix is unstable, this can create problems out of sample. Then you say that you are more confident about parameter estimates with your chosen 10-asset universe. Why are covariance matrices, and volatility and return estimates, more reliable for these assets?

**Adam**: In the book we tried to convey the point that, if as an investor you are not paying attention to correlations (and therefore covariances) *explicitly* by measuring them, then you had better pay attention *implicitly* by taking care in assembling your investment universe. To take an extreme example for illustration, imagine a portfolio of 5 stocks and one government bond. Even if you inverse volatility weight the assets, the stocks will consume the vast majority of portfolio risk. That’s because we haven’t accounted for the fact that most of the movement from the 5 stocks are derived from one source of risk (the market), while the movement from the bond comes from an entirely different source of risk (rates).

The only way to ensure that the true sources of risk are balanced in a portfolio is by accounting for correlations. If two assets are highly correlated, we can say that they are both responding to the same underlying factors (betas, sources of risk). If two assets are lowly correlated then they are responding to different sources of risk. To maximize diversification, we want to ensure the portfolio is well balanced across different sources of risk – not just well balanced across asset classes.

The fact is, if all assets in a portfolio are highly correlated, such as with an all-stock portfolio, then the differences in their covariances are swamped by the error in the estimates. That is, from a statistical standpoint they might as well all be exactly the same asset. On the other hand, if you assemble a nicely diversified universe, where assets respond structurally to different sources of risk – such as the 10 asset universe we specify in the book – then many pairwise correlations will be statistically significantly different from 1, and therefore the covariances offer meaningful information about how to diversify and lower overall portfolio volatility.

**AA**: Risk parity has been criticized because in recent years it has allocated heavily to bonds, which have been on a bull run in a falling rate environment. In a rising rate environment, this approach won’t work as well. How would you respond to this criticism?

**Adam**: Risk parity is about deriving returns from assets that deliver their best performance in very different economic and inflation environments. It is also about ensuring that assets with different ambient risks deliver equal risks to the overall portfolio. That means assets with lower volatility and lower correlation to other assets will earn a higher weighting.

Traditional portfolios, with 60% of their capital in stocks and 40% of their capital in bonds, are over 90% exposed to equity risk, because equities are so much more volatile than bonds. And that means these portfolios are 90% dependent on global growth, benign inflation, and abundant liquidity, because equities only thrive under these conditions. An asset’s long-term return contribution is a function of:

1. the average returns the asset delivers when conditions are favorable vs. the returns the asset ‘gives back’ when conditions are unfavorable, and;
2. the percentage of time that conditions are favorable vs. unfavorable.

Equities deliver pretty good returns when conditions are favorable (about 75% of the time historically), but they also produce catastrophic losses when conditions are unfavorable (about 25% of the time).

However, other asset classes hit home runs during periods where equities do poorly. In periods of accelerating inflation shocks like the 1970s commodities, gold, emerging market stocks, TIPs, and real estate produce massive returns, while developed market equities typically suffer. In periods of deflationary shocks like the Great Depression and the last 20 years in Japan, long-term government bonds crush it.

What many people misunderstand about risk parity is that, by constructing the portfolio so that it is equally exposed to several risk factors (growth, inflation, liquidity, etc.), an investor should also expect to derive the same amount of *return* from each factor. So a risk parity portfolio is no more exposed to bond risk than to stock risk, or any other major risk premium. Rather, the portfolio is perfectly balanced so that an investor is agnostic about what economic environments the future holds. And by maximizing diversification, an investor can thrive in each environment with the least amount of risk. I’d call that a win-win.

From an empirical standpoint firms like AQR and Bridgewater have good asset class data back to 1970, and even the 1950s (see [here](https://www.aqr.com/library/aqr-publications/can-risk-parity-outperform-if-yields-rise) and [here](https://www.bwater.com/Uploads/FileManager/research/Our%20Thoughts%20about%20Risk%20Parity%20and%20All%20Weather.pdf)). Their analysis demonstrates that risk parity portfolios don’t do any better in periods with declining rates than they do in periods with rising rates, in terms of the risk premium that they generate above cash. However, with current cash rates so low, investors everywhere should be counting on lower future nominal returns to all asset classes, not just bonds.

**AA**: I noticed there was limited discussion in the book of stock selection strategies. What are your views on return anomalies and factor investing?

**Adam**: I would say I am a cautious proponent of factor investing at the security level. I am a proponent because I believe that the behavioral errors that manifest in momentum, value, and a few other anomalies are indelible human qualities, and at the end of the day most large pools of capital are still controlled by humans. As such, these phenomena should be observed everywhere, across asset classes, within asset classes, and at the individual security level. And in fact AQR did a pretty good job of demonstrating that [they are observed everywhere](http://pages.stern.nyu.edu/~lpederse/papers/ValMomEverywhere.pdf)!

I am cautious, however, because some anomalies have become quite crowded. In some cases, I think factor ETFs are positioned to deliver negative return premia over the foreseeable future. For example, many low volatility equity strategies hold constituents which trade at an aggregate 25-30% premium to the broader market in terms of valuation. So while these ETFs may still harvest the low volatility premium, they are substantially *short* the value premium.

First generation factor funds were extremely diversified pools like the Russell 1000 Value ETF. The second generation evolved to concentrated factor portfolios and multi-factor portfolios. These strategies may be harder to stick with, because of high volatility and tracking error, which is positive because these qualities become barriers to arbitrage for many institutions.

I think the third generation of factor investing will deliver ‘pure’ factor exposures, which will focus exclusively on specific risk premia, and actively neutralize unintended factor bets. Fourth generation products may offer efficient zero-beta long-short factor portfolios that will provide true orthogonal sources of return. I think that will be genuinely exciting.

**AA**: The book contained a few references to leverage, such as how it can be used for volatility weighting purposes. What do you think about leverage?

**Adam**: Leverage is so misunderstood.

Sharpe and Tobin proposed the concept of the Capital Market Line in the early 1960s. They described how an investor can generate better risk adjusted returns from scaling exposure to a diversified portfolio rather than concentrating risk in assets further out the risk spectrum, like equities. Remember, equity-like assets only thrive in certain environments; in other environments they are highly destructive to wealth. Moreover, equities have substantial embedded leverage of about 2:1, so concentrated equity investors are taking on leverage anyway.

Moreover, in a risk parity context we believe that over the long term broad asset classes should produce excess returns in line with their risk. Assets with high risk should produce high returns, and assets with low risk should produce low returns. However, if you scale exposure to asset classes so that they all have the same risk, they should all produce similar excess returns. Why would anyone concentrate their portfolio in just one source of risk, rather than scaling exposures to a diverse basket of risk premia so that their portfolio is more resilient to a wide variety of economic outcomes?

Once you have a resilient “all weather” type portfolio, it is a simple matter to scale the portfolio to any reasonable risk/return target. The benefit of course is that you’ve now significantly reduced tail risk through diversification, and can achieve materially higher returns for the same level of risk. To be clear, it is possible to utilize leverage to significantly reduce risk for all types of investors, while providing enhanced returns. This may be counterintuitive, but once again we observe an opportunity to garner excess returns from the willing losers who are not inclined to embrace this type of approach.

**AA**: You talk about how expensive equities are today by many measures. And obviously bonds are expensive too. Do you think prices in the current period favor one asset class over the other?

I wouldn’t want to be in a position where I had to choose a strategic long-term portfolio in today’s environment. So many global asset classes are at valuation extremes rarely observed before in recorded history. Of course, we felt valuations were stretched in 2012! That was an important impetus for us to look in a different direction in order to help investors meet long-term investment goals. The manifestation of this quest is our Adaptive Asset Allocation methodology.

As to whether one might favor stocks or bonds at current relative valuations, I couldn’t comment. If I had to choose a long-term strategic asset allocation, I would choose some facsimile of long-term risk parity, such as Bridgewater’s All Weather Fund. We are working on our own version of this portfolio using *structural* definitions of risk, and correlation assumptions based on how different assets *should* react to a variety of economic dynamics.

For example, it is intuitive to compare the risks of assets in terms of their relative *duration*, which is the sensitivity of the asset class to changes in interest rates. Stocks, bonds, real estate, and perhaps even commodities have implied durations as a function of their expected cash-flows. This is not a quantitative measure of risk, but rather a fundamental reality steeped in first principles of financial markets. We can say the same about correlations by examining the structural drivers of prices in different economic environments. Stocks and bonds, for example, react predictably to growth and inflation at equilibrium, and this information translates to simple correlation assumptions. The focus moves away from precision and toward the goal of being ‘generally correct’. Once we have structural risk and correlation assumptions, it is a simple matter to create a robust strategic risk parity solution.

Interestingly, we think this type of solution – which is naturally countercyclical because it rebalances *against* large relative asset class moves – is a great compliment to pro-cyclical risk parity strategies, such as our ReSolve Global Risk Parity offering.

**AA**: You describe how one can use momentum or trend following in an asset allocation context. How did you settle on your specific timing signals? Can you tell us more about how you think it is best applied in markets?

**Adam**: Wow, this is a complex question. The fact is, momentum systems with different tenors (i.e. weighted average lookbacks), universes, number of holdings, holding periods, weighting methods, and rebalancing methods may perform wildly differently in the short and intermediate term. The overarching goal is to be generally correct, and minimize the probability of being specifically wrong. We want to capture the factor with a net, rather than try to nail it with a sniper rifle.

As a rule, we have absolutely zero faith in parameter optimization. The optimal parameter combination in the past has absolutely no bearing on what will work in the future. As a result, we draw randomly across the viable parameter space for every parameter that we use. For example, as the literature is clear that the momentum signal lies somewhere in the range of 20:252 days, we draw random combinations of lookbacks from this range to form momentum estimates.

But how many random lookbacks should we draw? Faber says 5, i.e. 1, 3, 6, 9 and 12 months. Other papers use 2 (3 months + 12 months), others use 3, etc. Who is to know what is optimal? So we choose randomly between 2 and 7 each time we draw. We make 500 draws of random lookback combinations for each method each time we rebalance. We run each sample through the optimizer so that each one generates an optimal portfolio weight. This addresses the known issues with optimization around parameter estimation and error maximization. Note this number of samples (500) was chosen on the basis of computational time. If we had more computer power we would draw more, because even 500 draws is an infinitesimally small fraction of the total sample space.

Once a portfolio is formed, the question becomes how long to hold the portfolio for. Since long-term asset class data is only available at monthly frequency for many assets, most papers on multi-asset momentum use monthly data. As a result, a monthly holding period has become the default for many GTAA strategies. But there is nothing magical about this holding period. In fact, we observe a very large dispersion of results using 21 day holding periods, with rebalancing on different days of the month. To avoid this risk of unlucky rebalance dates, we run many strategies in parallel with holding periods of 1, 5, 10, 15 and 20 days. For the multi-day holding period strategies, we run one strategy for each day. For example, we run five 5-day strategies, one on each day of the week, so that we aren’t just rebalancing on Fridays. In all, this means that each day, our portfolio consists of 20 unique portfolios based on different holding periods.

Note that we also know there are many ways to measure momentum. In all, we use 5 distinct but related measures of relative momentum, and another 5 different but related portfolio optimization methods to construct portfolios. This gives us 41 different combinations of momentum and optimization (a couple of optimizations can’t effectively utilize some forms of momentum). In all, we run 41 types of optimizations \* 20 unique holding periods \* 500 samples = 410,000 sub-portfolios each time we form a portfolio.

Why perform all these convolutions? It has to do with the law of large numbers. If we have a small number of samples, then the mean outcome will be dominated by luck. Bad luck might cause the observed mean to be far below the population mean (or vice versa). It’s only after we have many observations (trades, and probably market regimes as well) that the observed mean can be expected to converge to the population mean.

If we rely only on time to provide a large number of samples so that the true ‘skill’ of the strategy emerges, it would require many decades. By resampling the way we do, we generate many observations *cross-sectionally*, which minimizes the probability of bad luck in any one bet, and maximizes the probability that the observed mean of the approach will converge to the population mean as quickly as possible. After all, clients and prospects will only give you so much time to demonstrate your skill before their patience runs out.

**AA**: Great, Adam. Provocative thinking, as always. Thanks for making time for us.

**Adam**: Absolutely.
