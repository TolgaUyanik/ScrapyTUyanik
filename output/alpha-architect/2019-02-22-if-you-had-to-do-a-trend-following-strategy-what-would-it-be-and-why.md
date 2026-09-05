---
title: "If you had to do a trend following strategy, what would it be and why?"
slug: "if-you-had-to-do-a-trend-following-strategy-what-would-it-be-and-why"
date: "2019-02-22"
modified: "2021-10-09"
url: "https://alphaarchitect.com/if-you-had-to-do-a-trend-following-strategy-what-would-it-be-and-why/"
categories: ["Research Insights", "Trend Following", "Introduction Course"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# If you had to do a trend following strategy, what would it be and why?

> The topic of this blog post was inspired by Wes, who said the following: Valeriy, you have done more formal academic research on trend-following than […]

The topic of this blog post was inspired by Wes, who said the following:

> Valeriy, you have done more formal academic research on trend-following than anyone I know…Skepticism aside, let’s I forced you to pick a trend-following strategy, what would it be and why?

I decided to take on the question. I wanted to keep my response succinct so I focused on the use of trends in stock markets.

## **To follow the trend or not?**

> Marry, and you will regret it; don’t marry, you will also regret it; marry or don’t marry, you will regret it either way Attributed to Søren Kierkegaard
>
>  Attributed to Søren Kierkegaard

Trend following is not a magical system that makes money without any downside. Trend following does not produce, “Stock-like returns with bond-like risk.” Even though over a very long run the performance of a trend-following strategy seems to be better than that of its buy-and-hold counterpart, there are two caveats:

* First, as Keynes is attributed as saying, “In the long run we are all dead.”
* Second, the long run expected growth rate of a trend-following strategy is lower than that its buy and hold counterpart. Hence, the final wealth of a trend-follower is deemed to be lower than that of a passive investor. Over the intermediate run, the chances that a trend-following strategy outperforms its passive counterpart are 50%, at best.(1)

On the upside, a trend-following strategy has the potential to protect the investor from large drawdowns. Trend-following strategy resembles a [protective put strategy](https://www.fidelity.com/viewpoints/active-investor/protect-your-profits) where the investor buys a put option as insurance against potential losses. When the market prices go up, paying the insurance premium drains the investor returns. In contrast, when the market prices go down, trend-following is able to protect the investor from large losses. The longer and stronger the market downturn, the better the protective ability is likely to be. Yet, one needs to keep in mind that large drawdowns happen very infrequently; examples are as follows: the Wall Street crash of 1929, the 1973-74 stock market crash, the 2000 Dotcom bubble crash, and the 2008 Global Financial crisis. In more detail, the benefits of trend-following are described at the end of Chapter 9 in [Zakamulin (2017)](https://alphaarchitect.com/2017/12/20/book-review-market-timing-with-moving-averages/).(2)

## **What stock index to follow?**

The most robust performance of trend-following strategies is observed when the underlying index is a well diversified index of large stocks. For example, for trend-following it is better to use S&P 500 than the DJIA (Zakamulin 2014 and Zakamulin 2017).(3)

## **To short or not to short?**

When the trend-following indicator generates a Sell signal, there are two alternative strategies. Most commonly, a Sell signal is a signal to sell the stocks and invest the proceeds in cash. That is, a trader goes out of the stock market and places money in the risk-free asset. The payoff to this strategy resembles that of a [protective put strategy](https://www.fidelity.com/viewpoints/active-investor/protect-your-profits).

The other alternative is to shorts stocks when a Sell signal is generated. Specifically, when a Sell signal is generated, a trader needs not just to sell own stocks, but sell stocks borrowed from a broker. The idea in this strategy is not only to protect oneself from losses, but to profit from the stock price decrease. The payoff to this strategy resembles that of a [straddle strategy](https://www.fidelity.com/learning-center/investment-products/options/options-strategy-guide/long-straddle).

In stock markets, selling short the stocks should be
avoided. The performance of trend-following strategies with short selling is
very poor even in back-tests (Zakamulin 2017, Chapters 9 and 10).

## **Daily or monthly trading?**

Trend-following strategies can be implemented on either daily or monthly data. For example, with daily trading one can use 50- and 200-day Moving Average Crossover ([MAC](https://stockcharts.com/school/doku.php?id=chart_school:overview:arthur_hill_on_moving_average_crossovers)). With monthly trading, trend-following can be implemented using 2- and 10-month MAC.

Using daily data produces better performance in back-tests,
but using monthly data produces better performance in forward-tests (Zakamulin
2017, Chapters 9 and 10). Because the results of back-tests are subject to
data-mining bias, the results of forward tests are more reliable. Consequently,
monthly trading seems to be better than daily.

## **Which trend-following rules to use?**

The most popular trend-following rules are the Momentum ([MOM](https://en.wikipedia.org/wiki/Momentum_(technical_analysis))) rule, the MAC rule, and the Moving Average Envelope ([MAE](https://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_envelopes)) rule. The MAC and MAE rules can be implemented using various types of moving averages: Simple Moving Average ([SMA](https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/sma)), Linear Moving Average ([LMA](https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/wma)), and Exponential Moving Average ([EMA](https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/ema)). Trend-following can also be implemented by comparing, for example, the price and the SMA of prices.

There are not very big differences between various types of moving
averages. For example, SMA is the simplest and most known type of a moving
average. In empirical tests it performs as good as the other types of moving
averages. Similarly, there are in principle not very big differences between
various trading rules. Hence, a trend-following strategy can be implemented as
10-month MOM, SMA, or MAE rule. Statistical tests are not able to reject the
hypothesis that all these rules deliver the same performance.

However, a number of empirical and theoretical studies suggest that rules based on moving averages have a small advantage over the MOM rule.(4) A feasible explanation for why the SMA rule marginally outperforms the MOM rule is presented in Zakamulin and Giner (2018). This explanation is grounded on the observation that the stock market dynamics is time-varying and, hence, there is no *N*-month trend-following rule that is always optimal to use at any time. Therefore, a trend-following rule must deliver robust performance in a changing market environment (this idea is entertained in Zakamulin 2015). It looks like the MOM rule is less robust than the rules based on moving averages. In this regard, 10-month (or 12-month) SMA rule should be preferred to 10-month (or 12-month) MOM rule. Current back-tests suggest that the MAC rule based on using 2- and 10-month SMA performs slightly better than the 10-month SMA rule.

The MAE rule is also a rule which shows good performance.
According to Zakamulin (2017), the MAE rule must be preferred to all other
rules with daily trading. This rule can also replace the popular 10-month SMA
rule. For example, a trend-following strategy can be implemented as a 10-month
SMA with 1% envelope.

## **To combine trend-following rules or not?**

Some quants argue that, in order to improve the robustness and enhance the performance of trend following, it is wise to combine several trend-following rules.(5)

One possible realization of this idea is to combine the signals of several trading indicators into one “pooled” indicator. This approach is equivalent to creating a trading indicator with a new weighting scheme. For example, it is easy to show that the trading signal of, say, 3-month SMA rule equals to the sum of trading signals of 1-, 2-, and 3- month MOM rules. That is, *N*-month SMA rule is, as a matter of fact, a combination of *N* MOM rules. This knowledge also explains why the average performance of the SMA rule is marginally more robust than that of the MOM rule.

The other possible realization to combining trend-following rules is, for instance, to invest 50% into the *p*-month SMA strategy and the other 50% into the *q*-month SMA strategy. This combination might be profitable if in the market there are simultaneously trends with durations of *p* and *q* months. To the best of my knowledge, the only example of a published scientific paper where the author reports the superior performance of such a combination is the paper by Glabadanidis (2017) .(6) The explanation for why this combination delivered a superior historical performance is as follows: Over the period from 1960 to 2000 in the US small stock market there were both a strong short-term trend with duration of about 1 month and a usual stock market trend with duration of about 10 month (Zakamulin 2017, Chapter 10). Unfortunately, the short-term trend ceased to exist in the small-cap element of the stock market. I am not aware of the existence of several trends with different durations in the US large stock market. Therefore, in my opinion there is not a strong fundamental argument to combine several trading rules to follow trends in the large stocks.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | [See Jack’s recent piece](https://alphaarchitect.com/2019/02/20/trend-following-a-decade-of-underperformance/), which emphasizes this point! |
| ↑2 | Zakamulin (2017) “Market Timing with Moving Averages: The Anatomy and Performance of Trading Rules”, book published by Palgrave, available [here](https://www.amazon.com/Market-Timing-Moving-Averages-Developments/dp/3319609696/ref=mt_hardcover?_encoding=UTF8&me=) |
| ↑3 | Zakamulin (2014) “The Real-Life Performance of Market Timing with Moving Average and Time-Series Momentum Rules”, article published in [Journal of Asset Management](https://link.springer.com/article/10.1057/jam.2014.25), Volume 15, Issue 4 Zakamulin (2015) “Market Timing with a Robust Moving Average”, working paper, available at the [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2612307). |
| ↑4 | Zakamulin and Giner (2018) “Trend Following with Momentum versus Moving Average: A Tale of Differences”, working paper, available at the [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3293521) |
| ↑5 | e.g., Corey Hoffstein |
| ↑6 | Glabadanidis (2017) “Timing the Market with a Combination of Moving Averages”, journal article published in [International Review of Finance](https://onlinelibrary.wiley.com/doi/abs/10.1111/irfi.12107), Volume 17, Issue 3 |

 function footnote\_expand\_reference\_container\_46417\_179() { jQuery('#footnote\_references\_container\_46417\_179').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_46417\_179').text('−'); } function footnote\_collapse\_reference\_container\_46417\_179() { jQuery('#footnote\_references\_container\_46417\_179').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_46417\_179').text('+'); } function footnote\_expand\_collapse\_reference\_container\_46417\_179() { if (jQuery('#footnote\_references\_container\_46417\_179').is(':hidden')) { footnote\_expand\_reference\_container\_46417\_179(); } else { footnote\_collapse\_reference\_container\_46417\_179(); } } function footnote\_moveToReference\_46417\_179(p\_str\_TargetID) { footnote\_expand\_reference\_container\_46417\_179(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_46417\_179(p\_str\_TargetID) { footnote\_expand\_reference\_container\_46417\_179(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
