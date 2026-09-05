---
title: "Hot off the JFE Press: Maxing Out…your returns?"
slug: "hot-off-the-jfe-press-maxing-out-your-returns"
date: "2011-02-07"
modified: "2022-06-04"
url: "https://alphaarchitect.com/hot-off-the-jfe-press-maxing-out-your-returns/"
categories: ["Research Insights", "Behavioral Finance"]
tags: ["Lotteries", "Cross-Section"]
best_of: false
source: "alphaarchitect.com"
---

# Hot off the JFE Press: Maxing Out…your returns?

> Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns Turan G. Bali, Nusret Cakici, and Robert F. Whitelaw The Journal of Financial Economics, […]

### Maxing Out: Stocks as Lotteries and the Cross-Section of Expected Returns

* Turan G. Bali, Nusret Cakici, and Robert F. Whitelaw
* The Journal of Financial Economics, Vol. 99 February 2011
* A version of the paper can be found [here](http://pages.stern.nyu.edu/~rwhitela/papers/max%20jfe11.pdf).

### Abstract:

> Motivated by existing evidence of a preference among investors for assets with lottery-like payoffs and that many investors are poorly diversified, we investigate the significance of extreme positive returns in the cross-sectional pricing of NYSE, AMEX, and NASDAQ stocks over the sample period July 1962-December 2005. Portfolio-level analyses and the firm-level cross-sectional regressions indicate a negative and significant relation between the maximum daily return over the past one month (MAX) and expected stock returns. Average raw and risk-adjusted return differences between stocks in the lowest and highest MAX deciles exceed 1% per month. These results are robust to controls for size, book-to-market, momentum, short-term reversals, liquidity, and skewness. Of particular interest, including MAX reverses the puzzling negative relation between returns and idiosyncratic volatility recently documented in Ang et al (2006).

### Data Sources:

This study looks at the July 1926  through December 2005 period.  Stock return data come from the Center for Research in Securities Prices (CRSP), fundamental data come from Compustat.

If you want to backtest this strategy yourself, it it probably going to involve a pay-for-play data service, however, you can get the data for backtesting the recent past and for live implementation at any number of providers–[Financial Visualizations](http://finviz.com/?a=26319369) is probably your best bet, but [finance.yahoo.com](http://finance.yahoo.com) or [finance.google.com](http://finance.google.com) may work as well. In the end, all you need is historical daily prices to make this strategy happen.

### Discussion:

Everyone loves a gamble. And it’s not just pensioners who love to smoke cigarettes in front of a slot machine–no sir. Heck, even I’ve personally lost a fair amount of money gambling in Vegas and Atlantic City–and I knew it was a sucker’s bet before I even started!

So what gives?

Well, one would need to study the psychology research to get a good grasp on why humans enjoy gambles. As of yet, we don’t cover a lot of the behavioral finance research papers on the blog, but there are plenty of good ones out there for you to peruse. The key summary from all of this research is that individuals love to gamble and love lottery-like assets in particular–assets that have long-shot odds, but out-of-this-world payoffs. Another key finding is that people over pay for lottery-like bets, i.e., costs outweigh expected *monetary* benefits (there is certainly some utility associated with the actual act of gambling and dreaming you win the lottery.)

Applying the “lottery love” findings from academic behavioral finance research, we can hypothesize with respect to the stock market. The basic hypothesis is as follows:

H1: If people overpay for lottery-like gambles, we should see that lottery-like stocks will underperform on a risk-adjusted basis.

This paper tests “lottery” hypothesis using a novel approach to identify “lottery-like stocks.” The authors look at the performance of stocks that have had extreme market movements in the recent past and see how they do in the future. The underlying assumption is that investors identify stocks with extreme returns in the past as “lottery stocks” and bid these assets past fundamental value. The specific measure the authors look at to proxy for “lottery-like” is the maximum daily return during the previous month.

So how does this work?

Pretend it is January 31, 2011 and our universe is 2 stocks (XYZ and ABC). We want to form a long/short portfolio on February 1st that takes advantage of the “lottery love” effect. We identify that stock XYZ has a max daily return of 50% in the past month and stock ABC has a max of 1%. Therefore, our portfolio on February 1st will be short XYZ (a lottery stock) and long ABC (a non-lottery stock)–it’s that simple.

Here is a table of results highlighting the average returns and alphas associated with a monthly rebalanced portfolios sorted on Max daily return in the previous month.

[![](https://alphaarchitect.com/wp-content/uploads/2011/02/Untitled1.png "Untitled")](https://alphaarchitect.com/untitled-3/)

“The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.”

Not too shabby! A long/short portfolio generates a raw return of 1.03/month or roughly 12% a year (FYI: the 10-1 results in the table are L/S returns to a strategy that is long lottery, short non-lottery). Moreover, the 4-factor alpha (adjusts for market, size, value, and momentum risk) is 1.18/month or 14.4% a year.

The authors also consider just about every perturbation of their measure that one can imagine. We aren’t going to discuss them here, but if you want the details you can read the paper or send us piles of money to consult on your behalf (or a small amount if you are cheap like us).

### Investment Strategy:

1. Identify proxy for “lottery stocks”
2. Short lottery stocks
3. Long non-lottery stocks or perhaps use another alpha system for your long book
4. Make money.

### Commentary:

This paper was published in a top academic journal, so rest assured–the authors were required to consider almost all alternative explanations for the apparent “alpha” left on the table for this trading strategy. One can imagine a whole slew of reasons why this strategy has good returns–liquidity risk, short-sale constraints (insane rebate, no borrow, etc.), unknown risk factors, and so forth.

The authors find that the strategy may be difficult to implement because of short sale constraints and/or transactions costs. Most importantly, whoever runs the short book against “lottery stocks” must have brass balls and/or run the strategy as a portfolio, because a lot of these “lottery stocks” actually act like lotteries after the formation month–so you are definitely playing with fire here on a stock by stock basis. Nonetheless, a well thought out portfolio construction and risk management policy would certainly make this strategy more digestible to your average quantitative long/short fund. And if you aren’t a quant fund? Well, identify if your stock is a lottery-stock and think twice about owning it in your portfolio–it will save you money, on average.
