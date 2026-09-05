---
title: "Follow the Leader in the Stock Market–it works!"
slug: "follow-the-leader-in-the-stock-market-it-works"
date: "2013-09-10"
modified: "2022-06-01"
url: "https://alphaarchitect.com/follow-the-leader-in-the-stock-market-it-works/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Follow the Leader in the Stock Market–it works!

> Cross-Firm Information Flows and the Predictability of Stock Returns Anna Scherbina and Bernd Schlusche A version of the paper can be found here. Want a summary […]

### Cross-Firm Information Flows and the Predictability of Stock Returns

* Anna Scherbina and Bernd Schlusche
* A version of the paper can be found [here.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2263033)
* Want a summary of academic papers with alpha? Check out our free [Academic Alpha Database](https://alphaarchitect.com/tools/)!

### **Abstract:**

> Stocks at the center of important news developments may emerge as temporary return leaders for other stocks also affected by the news. We identify leader stocks based on their ability to Granger-cause returns of other stocks and show that thus-identified leaders can reliably predict returns of their followers out-of-sample. Leaders’ predictive ability is robust to firm- and industry-level controls and works at the level of individual stocks rather than industries. Many leaders cannot be easily detected using ex-ante firm characteristics: They are often small, belong to a different industry than their followers, and exhibit only a short-lived leadership. Consistent with our conjecture, the number of followers that a firm has is increasing in the intensity of news coverage that it receives.

### **Data Sources:**

CRSP/COMPUSTAT, TR News Analytics.

### **Alpha Highlight:**

Table 5 suggests 4-factor alpha of 0.74% per month, while Table 7 suggests weekly alpha of 0.31% per week.

[![sign](https://alphaarchitect.com/wp-content/uploads/2013/08/sign.png)](https://alphaarchitect.com/wp-content/uploads/2013/08/sign.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Strategy Summary:**

1. Paper identifies “leader” and “follower” stocks using a Granger-causality test.
2. Follower stocks are all U.S. common stocks with stock prices above $5.00.
3. To identify the follower stocks, run a cross-sectional regression as described in detail on page 9.
   * Regress stock i’s monthly return on stock i’s lagged return, the market lagged return, and the lag return of all other stocks (stock j, then stock k, etc.)
   * If the beta from the lag return of another stock (stock j for example) has a T-stat of greater than 2.00 (also 2.57 for robustness), then stock j would be considered a leader of stock i.
   * This regression is done using monthly returns with lags of 12 or 36 months, as well as weekly returns using lags of 52 weeks.
   * After identifying all leader stocks, compute a “leader signal” using only leaders within the same industry (signal still works if you drop the industry requirement).  This signal is computed by taking the average (equal-weight) of the beta from the regression for each leader times the lagged return for each leader.  Returns are robust to value-weighting (market capitalization).
     + See the appendix for a simple example.
4. Go long the top decile of the “leader signal” and short the lowest decile of the “leader signal.”
   * Using 36-month lags for the regression, the monthly 4-factor alpha is 0.74% per month!
   * Using weekly data (52 week lags), the weekly 4-factor alpha is 0.31% per week!
   * However, this alpha disappears for investments over $100,000 in each the long and short leg (Table 10).
5. This return can be improved upon by splitting the leader signal quintiles based on the follower return the previous week.
   * Going long the top quintile leader signal with the lowest quintile follower returns, and shorting firms from the bottom quintile leader signal with the highest quintile follower returns, earns a weekly alpha of 0.93%!
   * However, this alpha disappears for investments over $250,000 in each the long and short leg (Table 10).

### **Commentary:**

* Weighting the beta’s by their ability to predict returns may enhance performance, as opposed to simple equal weighting or value weighting.
* Would be nice to see the average size and number of firms in the long and short portfolios.
* Interesting result that even small firms can be considered “leaders.”

**Follow the leader anyone?**
