---
title: "Equity Term Structure and Option Returns"
slug: "equity-term-structure-and-option-returns"
date: "2014-01-27"
modified: "2022-06-01"
url: "https://alphaarchitect.com/equity-term-structure-and-option-returns/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Equity Term Structure and Option Returns

> Equity Volatility Term Structures and the Cross-Section of Option Return Aurelio Vasquez A version of the paper can be found here. Want a summary of academic […]

### Equity Volatility Term Structures and the Cross-Section of Option Return

* Aurelio Vasquez
* A version of the paper can be found [here.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1944298)
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category!](https://alphaarchitect.com/category/academic-research/)

### **Abstract:**

> The slope of the implied volatility term structure is positively related with future option returns. We rank firms based on the slope of the volatility term structure and analyze the returns for five different option trading strategies. **Option portfolios with high slopes of the volatility term structure outperform option portfolios with low slopes by an economically and statistically significant amount.** The results are robust to different empirical setups and are not explained by well-known market, size, book-to-market, or momentum factors. Additional higher-order option-related factors, volatility risk premiums, jump risk, and existing option anomalies cannot explain the large option returns.

### **Data Sources:**

1996-2007, OptionMetrics Ivy Database

### **Alpha Highlight:**

Volatility term structure slope has a strong relation with different option strategy returns:

[![Equity_Volatility_Term_Structures](https://alphaarchitect.com/wp-content/uploads/2014/01/Equity_Volatility_Term_Structures.png)](https://alphaarchitect.com/wp-content/uploads/2014/01/Equity_Volatility_Term_Structures.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Strategy Summary:**

**1. Paper finds a strong positive relationship between the slope of the volatility term structure and future option returns for all five trading strategies.**

* Use data for all US equity options and their underlying prices from Jan 4, 1996 to June 30, 2007 (OptionMetrics Ivy database).
  + On average there are 386 stocks per month.
* The slope of the volatility term structure is the difference between implied volatilities (IV) of long-dated and short-dated ATM options.
  + The short-term volatility is the average of the one-month ATM put and call implied volatilities.
  + The long-term volatility is the average of the longest-dated (and same strike as short term) ATM put and call implied volatilities.
* Each month, stocks are ranked based on the slope of the volatility term structure and then subsequent one month option returns are measured.
  + Five option strategies include: Naked call, Naked put, Straddle, Delta-hedged call, and Delta-hedged put.
  + Each option strategy above is tested, by going long the highest decile of IV, and short the lowest decile of IV.
    - Buying straddles from the top decile for IV, and going short straddles from the bottom decile for IV earns an average monthly return of 19.6% before transaction costs (naked-call L/S earns 24.1%; see Table 2 for returns for other option strategies).
    - After transaction costs (bid-ask spread), straddle L/S strategy yields significant 5.5% monthly return (naked call L/S earns insignificant 4.8% monthly return). This return becomes insignificant if bid-ask spread is higher than what is quoted (1.25 times quoted spread).

**2. Paper confirms the predictive power of the slope of the volatility term structure.**

* It uses Fama-MacBeth regressions and double sorts to eliminate possible explanations.
  + The outperformance of portfolios with high slope of the volatility term structure cannot be explained by size, book-to-market, momentum factors, volatility risk premium, jump risk, investor misreaction to volatility changes, option anomalies or firm characteristics.

### **Strategy Commentary:**

* Bid-ask spread decreases the returns from 19.6% to 5.5% for the straddle L/S.
  + There may be a way to increase returns by focusing on those options with lower bid-ask spreads.
* Interesting paper documenting how the term structure of IV impacts option returns.

**Follow Vol Slope when you’re option trading!**
