---
title: "The World’s Longest Trend-Following Backtest"
slug: "the-worlds-longest-trend-following-backtest"
date: "2015-11-09"
modified: "2022-05-25"
url: "https://alphaarchitect.com/the-worlds-longest-trend-following-backtest/"
categories: ["Trend Following", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# The World’s Longest Trend-Following Backtest

> Were in the middle of an academic research project and we ran a simple long-term trend-following model from January 1, 1801 to September 30, 2015. Recently, […]

Were in the middle of an academic research project and we ran a simple long-term trend-following model from January 1, 1801 to September 30, 2015.

Recently, there has been some research on the performance of trend-following rules over long periods [here](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2677212) (and highlighted by CXO [here](http://www.cxoadvisory.com/27792/technical-trading/long-run-moving-average-horse-race-for-timing-the-u-s-stock-market/)).

Our trend-following methodology is further described in our [downside protection piece](https://alphaarchitect.com/2015/08/13/avoiding-the-big-drawdown-with-trend-following-investment-strategies/).

* **Absolute Performance Rule:** **Time Series Momentum Rule (TMOM)**
  + Excess return = total return over past 12 months less return of T-Bills
  + If Excess return >0, go long risky assets. Otherwise, go long alternative assets (T-Bills)
  + Concept made popular by Gary Antonacci
* **Trending Performance Rule:** **Simple Moving Average Rule (MA)**
  + Moving Average (12) = average of 12 month prices
  + If Current Price – Moving Average (12) > 0, go long risky assets. Otherwise, go long alternative assets (T-Bills).
  + Concept made popular by Meb Faber
* **Robust Asset Allocation Rule: Combination of TMOM and MA (ROBUST)**
  + 50% TMOM, 50% MA

Our study includes 6 asset classes and strategies assessed over the sample time period:

* **SPX** = S&P 500 Total Return Index spliced with generic US stock market data in early years
* **LTR**= 10-Year Treasury Total Return Index
* **SP\_MA** = SPX with MA rule applied
* **60,40**=60/40 SPX, LTR
* **SP\_TMOM**= SPX with TMOM rule applied
* **SP\_ROBUST**= SPX with ROBUST rule applied

Results are gross, no fees are included. All returns are total returns and include the reinvestment of distributions (e.g., dividends). Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

## Key Trend-Following Results

First, the laundry list of domestic equity drawdowns over time that exceed 15%. I’ve highlighted the worst performer in **red** across the index, 10-years, and the index with MA:

[![The World's Longest Trend-Following Backtest_1800-2015 drawdown tables](https://alphaarchitect.com/wp-content/uploads/2015/11/The-Worlds-Longest-Trend-Following-Backtest_1800-2015-drawdown-tables.png)](https://alphaarchitect.com/wp-content/uploads/2015/11/The-Worlds-Longest-Trend-Following-Backtest_1800-2015-drawdown-tables.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Takeaways

* MA rule, TMOM rule and ROBUST rule, historically, have reduced drawdowns
* Treasury bonds, historically, act like insurance assets and serve as a “[crisis alpha](https://alphaarchitect.com/2015/08/19/crisis-alpha-surprising-ways-to-hedge-stock-portfolio-risk/)” instrument

### Robustness

Here we look at top SPX drawdowns and the associated results across the different strategies over two sample periods:

#### **Downside Protection: 1800-1926**

[![The World's Longest Trend-Following Backtest_1800-1926](https://alphaarchitect.com/wp-content/uploads/2015/11/The-Worlds-Longest-Trend-Following-Backtest_1800-1926.png)](https://alphaarchitect.com/wp-content/uploads/2015/11/The-Worlds-Longest-Trend-Following-Backtest_1800-1926.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

**Downside Protection: 1927-2015**

[![The World's Longest Trend-Following Backtest_1927-2015](https://alphaarchitect.com/wp-content/uploads/2015/11/The-Worlds-Longest-Trend-Following-Backtest_1927-2015.png)](https://alphaarchitect.com/wp-content/uploads/2015/11/The-Worlds-Longest-Trend-Following-Backtest_1927-2015.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

**Bottom line:** [asset allocation](https://alphaarchitect.com/2014/12/02/the-robust-asset-allocation-raa-solution/) and [tactial market timing](https://alphaarchitect.com/2015/08/13/avoiding-the-big-drawdown-is-downside-protection-helpful-or-heresy/) are interesting subjects if one seeks to minimize tail risks.
