---
title: "Follow the Trend AND the Sell-Side!"
slug: "follow-the-trend-and-the-sell-side"
date: "2013-03-26"
modified: "2022-06-02"
url: "https://alphaarchitect.com/follow-the-trend-and-the-sell-side/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Follow the Trend AND the Sell-Side!

> Large Price Changes and Subsequent Returns Suresh Govindaraj, Joshua Livnet, Pavel G. Savor, and Chen Zhao A version of the paper can be found here. Want […]

### Large Price Changes and Subsequent Returns

* Suresh Govindaraj, Joshua Livnet, Pavel G. Savor, and Chen Zhao
* A version of the paper can be found [here.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2200605)
* Want a summary of academic papers with alpha? Check out our free [Academic Alpha Database](https://alphaarchitect.com/tools/)!

### **Abstract:**

> We investigate whether large stock price changes are associated with short-term reversals or momentum, conditional on the issuance of analyst price target or earnings forecast revisions immediately following these price changes. Our study provides evidence that when analyst revisions occur immediately after large price shocks, stock prices exhibit momentum, suggesting the initial price change was based on new information. In contrast, when price changes are not followed by immediate analyst revisions, we document short-term reversals, indicating that the initial price shocks were probably caused by liquidity or noise traders. A trading strategy that is based on the direction of the price change and the existence of immediate analyst revisions in the same direction earns significant abnormal monthly calendar-time returns

### **Data Sources:**

IBES, CRSP, and COMPUSTAT from 1982-2011.

### **Alpha Highlight:**

[![table8](https://alphaarchitect.com/wp-content/uploads/2013/03/table8.png)](https://alphaarchitect.com/wp-content/uploads/2013/03/table8.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Strategy Summary:**

* Identify firms with a stock price move 5% or greater or -5% or less.
  + Eliminate firms under $100 million in market capitalization.
* Check to see if analysts revise their earnings estimate or price target within 5 days after this price move.
* At the end of each month form the following portfolio:
  + Long firms that had a large price increase and an analyst earnings estimate (or price target) increase in the previous month.
  + Short firms that had a large price decrease and an analyst earnings estimate (or price target) decrease in the previous month.
    - If there are multiple analysts following a firm, and the majority increase the price target, this is classified as a price target increase.
  + To increase the returns even more, only keep the firms from the long portfolio with high trading volume on the price change day (above 110% of average 45 days before) and only keep the firms from the short portfolio that had low trading volume on the price change day.
    - This long/short portfolio earns 1.31% abnormal returns per month compared to a portfolio of similar firms matched on size, value and momentum.
  + Equal-weight the firms and rebalance monthly.

### **Commentary:**

* Would be interesting to see what the 3 and 4 factor alpha for this portfolio would be.
* What would the returns look like if the portfolio was value-weighted?
* Although paper eliminates firms under $100 million, results may be driven by some small-cap stocks.
