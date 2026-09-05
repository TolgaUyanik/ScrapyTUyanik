---
title: "Improving Commodity Strategies with Momentum and Term Structure"
slug: "improving-commodity-strategies-with-momentum-and-term-structure"
date: "2013-02-05"
modified: "2022-06-10"
url: "https://alphaarchitect.com/improving-commodity-strategies-with-momentum-and-term-structure/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Improving Commodity Strategies with Momentum and Term Structure

> Tactical allocation in commodity futures markets: Combining momentum and term structure signals Ana-Maria Fuertes, Joelle Miffre, and Georgios Rallis A version of the paper can […]

### Tactical allocation in commodity futures markets: Combining momentum and term structure signals

* Ana-Maria Fuertes, Joelle Miffre, and Georgios Rallis
* A version of the paper can be found [here](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1127213).
* Want a summary of academic papers with alpha? Check out our free [Academic Alpha Database](https://alphaarchitect.com/tools/)!

### **Abstract:**

> This paper examines the combined role of momentum and term structure signals for the design of profitable trading strategies in commodity futures markets. With significant annualized alphas of 10.14% and 12.66% respectively, the momentum and term structure strategies appear profitable when implemented individually. With an abnormal return of 21.02%, a novel double-sort strategy that exploits both momentum and term structure signals clearly outperforms the single-sort strategies. This double-sort strategy can additionally be utilized as a portfolio diversification tool. Interestingly, the abnormal performance of the double-sort portfolios cannot be explained by a lack of liquidity or data mining and is robust to transaction costs and to different specifications of the risk-return trade-off.

### **Data Sources:**

Data stream and Bloomberg from 1979 to 2007.

### **Alpha Highlight:**

[![Fuertes, Miffre and Rallis, 2010 - Google Chrome_2013-02-01_08-48-23](https://alphaarchitect.com/wp-content/uploads/2013/02/Fuertes-Miffre-and-Rallis-2010-Google-Chrome_2013-02-01_08-48-23-1024x476.png)](https://alphaarchitect.com/wp-content/uploads/2013/02/Fuertes-Miffre-and-Rallis-2010-Google-Chrome_2013-02-01_08-48-23.png)

[Click to enlarge] The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Strategy Summary:**

1. First compute all commodity futures’ roll returns (using nearest-to-maturity and second-nearest-to-maturity contracts)
2. Next compute all commodity futures’ momentum.  The paper uses past 1-month, 3-month, or 12-month returns to compute momentum.
3. Sort roll returns into 3 groups, with highest 1/3 roll returns being “high”, and lowest 1/3 roll returns being “low.”
4. Then sort the commodities in the “high” group into “winners” and “losers” based on past momentum.  Do the same for the “low” group.
5. Go long the “high-winners” and short the “low-losers.”  All portfolios are EW and are rebalanced every month
6. Table 6 shows that this strategy yields around 18-23% alpha per year.

### **Commentary:**

* Paper finds that rebalancing at the end of the month or on the 15th of the month does not significantly affect returns.
* Paper also sorts on momentum first, then term structure and finds similar results, which are also in Table 6.
* After accounting for trading costs in the paper, the returns are still between 18% and 22% (Table 6).
* Table 7 also highlights that this strategy is negatively correlated with the SP500, and has a small positive correlation to bond returns.
