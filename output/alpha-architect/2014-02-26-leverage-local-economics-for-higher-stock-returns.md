---
title: "Leverage local economics for higher stock returns"
slug: "leverage-local-economics-for-higher-stock-returns"
date: "2014-02-26"
modified: "2022-06-01"
url: "https://alphaarchitect.com/leverage-local-economics-for-higher-stock-returns/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Leverage local economics for higher stock returns

> Geographic Diffusion of Information and Stock Returns Jawad M. Addoum, Alok Kumar, Kelvin Law A version of the paper can be found here. Want a summary […]

### Geographic Diffusion of Information and Stock Returns

* Jawad M. Addoum, Alok Kumar, Kelvin Law
* A version of the paper can be found [here.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2343335)
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category!](https://alphaarchitect.com/category/academic-research/)

### **Abstract:**

> This study shows that value-relevant information about firms is geographically distributed across U.S. states and the market is slow in aggregating this information. The earnings and cash flow of firms can be predicted using the past performance of firms in economically relevant geographical regions, but sell-side equity analysts and institutional investors do not fully incorporate this information in their earnings forecasts and trades, respectively. Consequently, firms exhibit stronger post-earnings-announcement drift and stronger momentum in returns when geographic information is more dispersed and difficult to aggregate. A Long−Short trading strategy that exploits the slow diffusion of geographic information earns an annual, **abnormal risk-adjusted return of about 9%.**

### **Data Sources:**

EDGAR, BLS, CRSP/COMPUSTAT 1995 to 2010.

### **Alpha Highlight:**

[![geo](https://alphaarchitect.com/wp-content/uploads/2014/02/geo.png)](https://alphaarchitect.com/wp-content/uploads/2014/02/geo.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

~7-8%  alpha a year tracking delays in information? Not bad!

### **Strategy Summary:**

1. Paper first identifies economically-connected (EC) firms using the following methodology.
   * Count the number of times states are referenced in the 10-K filings. When a firm lists a state in the 10-K, all firms in this state are considered to be economically connected (EC).
     + Speficically count the number of state references in these four sections of the 10-K: “Item 1: Business”, “Item 2: Properties”, “Item 6: Consolidated Financial Data”, and “Item 7: Management’s Discussion and Analysis.”
   * EC Earnings (Cash-flow) is the citation-share weighted Earnings (Cash-flow) of firms located in EQ states, excluding the firms in the HQ state.
2. Using a Fama-MacBeth regression, find that past-quarter EC Earnings (Cash-flow) has predictive ability for a firm’s next-quarter Earnings (Cash-flow).
   * This has incremental predictive ability over past-quarter HQ Earnings (Cash-flow), which is the Earnings (Cash-flow) of firms in the same state as the firm’s HQ.
   * This predictive ability works at an annual-data frequency, using industry-adjusted earnings and cash-flow, in simple and conglomerate firms, and when excluding firms with strong economic links.
   * Find that analysts do not incorporate the EC information into their earnings forecast.
3. Construct a trading strategy:
   * A Long-short trading strategy where you long (short) firms with high (low) expected earnings surprise.
     + Forecast EPS using Fama-MacBeth regressions, and subtract analyst forecats to create expected earnings surprise variable (Pages 33-34).
     + This generates a monthly alpha of 0.75% or an annual premium of 9%.

### **Strategy Commentary:**

* Slow diffusion (a delay) of geographically dispersed information generates predictable patterns in stock returns.
* Portfolio construction for trading strategy is complicated to construct.
  + A much simpler trading strategy may outperform this trading strategy.

**Ready to build a textual analysis tool to identify the importance of a state to a firm?**
