---
title: "The Other Side of Value"
slug: "the-other-side-of-value"
date: "2011-02-19"
modified: "2022-06-04"
url: "https://alphaarchitect.com/the-other-side-of-value/"
categories: ["Research Insights", "Value Investing Research"]
tags: ["abnormal returns", "Value", "book-to-market", "gross profitability"]
best_of: false
source: "alphaarchitect.com"
---

# The Other Side of Value

> The Other Side of Value Robert Novy-Marx A version of the paper can be found here. (sorry, I couldn’t find a free link to the source paper). […]

### The Other Side of Value

* Robert Novy-Marx
* A version of the paper can be found [here](http://www.nber.org/papers/w15940.pdf). (sorry, I couldn’t find a free link to the source paper).
* Live implementation data can be found at [Empirical Finance Data*™*](https://alphaarchitect.com/)

### **Abstract:**

> Profitability, as measured by gross profits-to-assets, has roughly the same power as book-to-market predicting the cross-section of average returns. Profitable firms generate significantly higher average returns than unprofitable firms, despite having, on average, lower book-to-markets and higher market capitalizations. Controlling for profitability also dramatically increases the performance of value strategies. These results are difficult to reconcile with popular explanations of the value premium, as profitable firms are less prone to distress, have longer cashflow durations, and have lower levels of operating leverage, than unprofitable firms. Controlling for gross profitability explains most earnings related anomalies, as well as a wide range of seemingly unrelated profitable trading strategies.

### **Data Sources:**

This paper examines a long time series of accounting and return measures, all of which can be obtained from Compustat and CRSP (it is never explicitly stated, but I assume he got return data from CRSP).  The period analyzed is from July 1963 to December 2009.

### **Discussion:**

First off, let us commend the author for actually citing (on a few occasions) the great [Ben Graham](http://en.wikipedia.org/wiki/Benjamin_Graham). Rarely do you see academics quoting one of the great ‘quantitative’ value investors of our time. Often, it seems the concept of buying portfolios of stocks with certain characteristics was invented in the post-Harry Markowitz period. And yet, Graham was promoting the idea back in the 20’s and 30’s! I digress…

Several simple accounting measures found to help predict stock returns have come to light in the past thirty years, most notably the book-value-to-market-value ratio (B/M) documented by Fama and French (1992, 1993) . In academica, the B/M ratio is known as the “value” factor. B/M measures how many assets you get per unit of price. The other dimension of value is “quality,” or how much value do the underlying assets actually generate. An asset purchased for $100 that produces terds is probably *overvalued* at 1 penny, whereas an asset purchased for $100 that produces golden nuggets is probably *undervalued* at 100x book. The main point is that not all assets are created equal and looking at book values doesn’t always tell you the entire value story.

The author identifies a “quality” measure that dominates many other factors in predicting the cross-section of returns (to include some analysts’ favorites–earnings and free cash flow). The specific factor used is defined as:

Profitability Factor=Revenues(t)-Cost of Goods Sold(t)/Total Assets (t)

The author uses the profitability factor to identify “productive assets,” because using other proxies for quality are sub-par. For example, earnings calculated from net income are noisy.  Earnings can be managed and/or manipulated, such that they may not be representative of the  economic position of a company.  On the other hand, gross profitability, which is calculated as revenues minus cost of goods sold, does a much better job of describing how well the company is performing.  As the author of this paper explains it, “gross profits is the cleanest accounting measure of true economic profitability.”

So Novy-Marx finds that higher profitability tends to predict higher expected returns, but how do the returns look to a trading strategy that longs high profitability and short low profitability?

For each month, the author sorts all firms in to one of five quintiles based on the level of their gross profit divided by total assets, where gross profit equals revenue minus costs of goods sold.  On a raw, non-risk-adjusted basis, the stocks in the highest profitability quintile earn a monthly return 0.33% higher than the stocks in the lowest profitability quintile.  This equates to about 4.03% per year. On a risk-adjusted basis, the L/S strategy garners around 0.55% a month or 6.6%. Novy-Marx also sorts the universe of stocks in to quintiles based on book-to-market ratio in the same way.  Consistent with prior literature, he finds that monthly return to high book-to-market stocks is 0.42% higher than the return to low book-to-market stocks.

![](https://alphaarchitect.com/wp-content/uploads/2011/02/Untitled3.png "Untitled")

“The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.”

So a L/S of high profitability minus low profitability works and a L/S of high B/M and low B/M works. How can we use this knowledge to make better trading strategies?

The author actually posts the numbers for a strategy that captures the ‘alpha’ from both of these trading strategies. Specifically, he looks at the returns of a trading strategy that takes a 50/50 mix of profitability and B/M, longs the highest quintile names, and shorts the lowest quintile names. The combined “profitability and value” strategy produces a return of 0.75% a month (roughly 9% a year), and a realized Sharpe ratio of .9–pretty nice considering the market SR is .32 over the same time period (1963-2009).

Sounds good thus far, but can anyone with more than $5 in assets actually implement this thing?

To address the concerns about liquidity and size constraints, the author looks at a profitability factor and B/M strategy that only trades in the largest stocks (top 500, ex financials). Specifically, at the end of each June, he buys the top 150 stocks with the highest average of profitability and B/M, and shorts the bottom 150 stocks with the lowest average profitability and B/M. Table 7 has all the results:

![](https://alphaarchitect.com/wp-content/uploads/2011/02/Untitled4.png "Untitled")

“The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.”

Looks like the raw returns on the strat that trades L/S on the combo strat earns 0.64% a month–alpha of 0.39% a month. Pretty good for a low turnover (.33 a year), low refinement (150 long, 150 short, out of a universe of 500), high liquidity strategy (huge companies).

### **Investment Strategy:**

1. Each year, separately rank stocks on the basis of their book-to-market ratio and gross profitability.
2. Average the two ranks to produce a combined rank.
3. Take equally-weighted long positions in the top stocks with the highest combined rank and short positions in the stocks with the lowest combined rank.
4. Rebalance every year (you probably want to implement a tax harvesting aspect to the rebalance to maximize tax efficiency–a bit of a headache, but doable).
5. Make money.

### **Commentary:**

This paper sheds light on the opportunities investors and researchers are missing by simplistically defining value stocks merely by their book-to-market ratio.  By expanding the concept of value to other, equally important, accounting measures, a simple trading strategy can be devised.

There are lots of other interesting tidbits in the paper that sophisticated readers may find interesting. [Empirical Finance, LLC](http://www.empiricalfinancellc.com/) has also done internal work on the strategy and found some fascinating results. Nonetheless, one can add a lot of “secret sauce” to the gross profit and B/M strategy, but the reality is you can capture a good portion of the alpha using the “out-of-the-box” trading strat Novy-Marx highlights in Table 7.

Good luck.
