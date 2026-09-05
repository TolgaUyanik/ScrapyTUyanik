---
title: "Dissecting Goldman’s 99 percentile Market-Timing Signal"
slug: "dissecting-goldmans-99-percentile-market-timing-signal"
date: "2015-02-26"
modified: "2022-05-30"
url: "https://alphaarchitect.com/dissecting-goldmans-99-percentile-market-timing-signal/"
categories: ["Research Insights", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Dissecting Goldman’s 99 percentile Market-Timing Signal

> Investors have been worrying, at least for the last several years, that the market is overvalued. By some measures this is undoubtedly true. Just yesterday we highlighted that […]

Investors have been worrying, at least for the last several years, that the market is overvalued. By some measures this is undoubtedly true. Just yesterday we [highlighted](https://alphaarchitect.com//2015/02/25/market-valuations-based-on-cape-a-deeper-dive/#.VO82IvnF-lU) that the Shiller CAPE is in the 94th percentile as of 1/31/2015.

And as valuations have gone higher, the alarm bells in the press have gotten louder.

* Warren Buffett is [“Dumping [US shares] at an alarming rate.”](http://www.moneynews.com/MKTNews/billionaires-dump-economist-stocks/2012/08/29/id/450265/)
* Nobel-Winner, and famed market commentator, Robert Shiller, says “[I may get out of US stocks](http://finance.yahoo.com/news/may-us-stocks-nobel-winner-140135375.html;_ylt=AwrBJR5RoOxU2lQAYgOTmYlQ)“
* And, of course, Goldman Sachs is now telling everyone, [“](http://www.zerohedge.com/news/2015-02-21/smart-money-selling-not-buying-goldman-warns-valuations-99th-percentile)*[The Smart Money Is Selling, Not Buying.”](http://www.zerohedge.com/news/2015-02-21/smart-money-selling-not-buying-goldman-warns-valuations-99th-percentile)*

Digging into the Goldman Sachs call is illuminating. Here is what Goldman’s chief strategist David Kostin says on current market valuations:

> Stocks with attractive valuation are rare in the current environment of stretched share prices. The aggregate S&P 500 trades at 17.3x forward EPS and 10.2x EV/EBITDA. The only time during the past 40 years that the index traded at a higher multiple was during the 1997-2000 Tech Bubble. The median stock sports a P/E and EV/EBITDA of 18.0x and 11.0x, respectively. **These valuations rank in the 99th percentile of both P/E and EV/EBITDA multiples since 1976.**

The implicit assumption underlying Kostin’s “story” is that knowing that the market is in the 99th percentile somehow improves our ability to time the market.

A great story–but is there any evidence to support this claim?

### Does Goldman’s 99% Valuation-Timing Rule Work?

We’ve analysed tactical asset allocation using valuation measures in the [past](https://alphaarchitect.com//2014/06/12/can-market-valuations-be-effective-market-timing-signals/#.VOydGfnF-VN).  
The evidence isn’t promising: Trend-following timing rules have been much more effective than valuation-based timing rules.

Nonetheless, the Goldman Sachs article inspired us to dig into the valuation-timing hypothesis.  
To create our “valuation-timing” indicator, every month we identify the 99 percentile valuations using rolling 5-, 10-, and 20-year look-back periods. Our trading rule is simple: if the current market valuation is greater or equal to the 99 percentile measure, we invest in the risk-free rate (short-term treasury bills), otherwise, we stay invested.

We compare the valuation-timing indicator to a monthly-assessed simple moving-average (MA) trading rule, and a buy-and-hold strategy. The buy-and-hold strategy is straightforward, and the MA indicator is simple: if the current market price is lower than the 12 month moving average, we invest in the risk-free rate (short-term treasury bills), otherwise, we stay invested.

Our conclusion is counterintuitive, but not entirely surprising: **Goldman’s “Valuation-Timing” concept doesn’t have legs.**

#### Strategy Details:

For the MA signals, we use a monthly-assessed 12-month MA rule on the S&P 500 total return index.

* If the price for last month is above the past 12 months average, stay in the market; otherwise, invest in the risk-free asset.

For the valuation signal, we use [CAPE](https://alphaarchitect.com//2011/10/06/the-shiller-pe-ratio/#.VOytHfnF9HU), Shiller’s Cyclically Adjusted PE ratio. Results are similar for P/E and enterprise multiples, but for public replication purposes we use the CAPE data (we sometimes make mistakes and want others to let us know!). CAPE raw data can be accessed from [Shiller’s database](http://www.econ.yale.edu/~shiller/data.htm).

* If last month’s CAPE valuation is in the 99 percentile or higher, buy U.S. Treasury bills (Rf), otherwise stay in the market. For robustness purposes, we use three different rolling look-back periods to determine the 99 percentile valuation at a given point in time: 5-, 10- and 20- years.

Our backtest period is from 1/1/1947 to 1/31/2015 (we start in 1947 because we need to burn 20 years of data for the 20-year look-back metric). Results are gross, no fees are included, and only index returns are included. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. All returns are total returns and include the reinvestment of distributions (e.g., dividends). Strategies are all monthly-rebalanced, meaning Goldman’s valuation litmus test is applied every month.

##### **Strategy Legend:**

* **SP500** = S&P 500 Total Return Index
* **LTR** = The Merrill Lynch 10-year U.S. Treasury Futures Total Return Index
* **Rolling 5 year 99perc CAPE**= Timing signal uses the 99th percentile valuation metric using rolling 5 year look-back periods.
* **Rolling 10 year 99perc CAPE** = Timing signal uses the 99th percentile valuation metric using rolling 10 year look-back periods.
* **Rolling 20 year 99perc CAPE**= Timing signal uses the 99th percentile valuation metric using rolling 20 year look-back periods.
* **(1,12) MA**= If last month’s price is above the past 12 month average, invest in the S&P 500; otherwise, buy U.S. Treasury Bills (RF).

#### Statistics Summary:

##### Full Sample: 1/1/1947 – 1/31/2015

* (1,12) MA outperforms Rolling 10 year Valuation Timing.
* Buy-and-hold is similar to Valuation-Timing.

[![1](https://alphaarchitect.com/wp-content/uploads/2015/03/11.png)](https://alphaarchitect.com/wp-content/uploads/2015/03/11.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

##### First Half: 1/1/1947 – 12/31/1981

* (1,12) MA outperforms Rolling 10 year Valuation Timing.
* Buy-and-hold is similar to Valuation-Timing.

[![2](https://alphaarchitect.com/wp-content/uploads/2015/03/2.png)](https://alphaarchitect.com/wp-content/uploads/2015/03/2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### Second Half: 1/1/1982 – 1/31/2015

* (1,12) MA outperforms Rolling 10 year Valuation Timing.
* Buy-and-hold is similar to Valuation-Timing.

[![3](https://alphaarchitect.com/wp-content/uploads/2015/03/3.png)](https://alphaarchitect.com/wp-content/uploads/2015/03/3.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### Robustness Tests with Different Look-Back Periods

##### Full Sample: 1/1/1947 – 1/31/2015

* (1,12) MA outperforms Rolling 5-, 10-, and 20-year Valuation Timing.
* Buy-and-hold is similar to Valuation-Timing.

[![5](https://alphaarchitect.com/wp-content/uploads/2015/03/5.png)](https://alphaarchitect.com/wp-content/uploads/2015/03/5.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

##### First Half: 1/1/1947 – 12/31/1981

* (1,12) MA outperforms Rolling 5-, 10-, and 20-year Valuation Timing.
* Buy-and-hold is similar to Valuation-Timing.

[![6](https://alphaarchitect.com/wp-content/uploads/2015/03/6.png)](https://alphaarchitect.com/wp-content/uploads/2015/03/6.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

##### Second Half: 1/1/1982 – 1/31/2015

* (1,12) MA outperforms Rolling 5-, 10-, and 20-year Valuation Timing.
* Buy-and-hold is similar to Valuation-Timing.

[![7](https://alphaarchitect.com/wp-content/uploads/2015/03/7.png)](https://alphaarchitect.com/wp-content/uploads/2015/03/7.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### Robustness Tests with 75 percentile Buy-In Trigger

One issue with a 99th percentile trigger is the possibility that you get out when valuations are at 99th percentile, but when the market drops a bit and hits 98th percentile you get right back in. This might “whipsaw” and create poor outcomes.  
To test this conjecture we do another test where we apply the 99th percentile rule, but **we don’t get back in to the market until it has dropped to at least the 75th percentile.**

##### FULL SAMPLE: 1/1/1947 – 1/31/2015

* (1,12) MA outperforms Rolling Valuation Timing with a 75th percentile buy-in rule.
* Buy-and-hold is similar to Valuation-Timing.

[![9](https://alphaarchitect.com/wp-content/uploads/2015/02/92.png)](https://alphaarchitect.com/wp-content/uploads/2015/02/92.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

##### FIRST HALF: 1/1/1947 – 12/31/1981

* (1,12) MA outperforms Rolling Valuation Timing with a 75th percentile buy-in rule.
* Buy-and-hold is similar to Valuation-Timing.

[![10](https://alphaarchitect.com/wp-content/uploads/2015/02/102.png)](https://alphaarchitect.com/wp-content/uploads/2015/02/102.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

##### SECOND HALF: 1/1/1982 – 1/31/2015

* (1,12) MA outperforms Rolling Valuation Timing with a 75th percentile buy-in rule.
* Buy-and-hold is similar to Valuation-Timing.

[![11](https://alphaarchitect.com/wp-content/uploads/2015/02/112.png)](https://alphaarchitect.com/wp-content/uploads/2015/02/112.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Conclusion

There is no evidence to support the use of “valuation-timing,” which performs similarly to buy-and-hold strategies (after costs it would we much worse). There is nothing magical about the 99th percentile. Trend-following, at least historically, seems to more effective.

Perhaps there are more convoluted, complex, and data-optimized ways in which we can leverage overall market valuations to help us time markets. We haven’t found any, but that doesn’t mean they don’t exist.

Please share.
