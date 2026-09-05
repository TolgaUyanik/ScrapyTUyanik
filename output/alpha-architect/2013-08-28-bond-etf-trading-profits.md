---
title: "Bond ETF Trading Profits?"
slug: "bond-etf-trading-profits"
date: "2013-08-28"
modified: "2022-06-01"
url: "https://alphaarchitect.com/bond-etf-trading-profits/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Bond ETF Trading Profits?

> Predictability in Bond ETF Returns Jon A. Fulkerson, Susan D. Jordan, and Timothy B. Riley A version of the paper can be found here. Want a […]

### Predictability in Bond ETF Returns

* Jon A. Fulkerson, Susan D. Jordan, and Timothy B. Riley
* A version of the paper can be found[here.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2273930)
* Want a summary of academic papers with alpha? Check out our free [Academic Alpha Database](https://alphaarchitect.com/tools/)!

### **Abstract:**

> We study the persistence of bond ETF premiums and discounts. Following a day of high or low premiums or discounts over NAV, ETFs tend to maintain a premium or discount for up to 30 days. Premiums and discounts also predict distinct patterns of returns after daily closing. Overnight returns are negative following a high premium, while ETFs with large discounts are followed by positive overnight returns. The large discount ETFs have substantially higher returns than high premium ETFs over the subsequent thirty days. We find that traditional liquidity measures, along with prior deviations from NAV, are significant in explaining a fund’s premiums/discounts. Finally, we examine a long-short portfolio strategy to exploit the observed deviations from NAV, and find it generates an alpha of .96% per month or about 11.5% per year.

### **Data Sources:**

CRSP mutual fund database Jan 2007 to December 2011.

### **Alpha Highlight:**

Exhibit 10 shows monthly alpha (bond OLS regression) of 0.96%.

[![bondetf](https://alphaarchitect.com/wp-content/uploads/2013/08/bondetf.png)](https://alphaarchitect.com/wp-content/uploads/2013/08/bondetf.png)

### **Strategy Summary:**

1. Each month, compute each Bond ETF’s Premium/NAV ratio.
   1. Computed as (Price – NAV) / NAV.
2. Sort into deciles based on this ratio.
3. Buy the lowest decile of ETFs (lowest Premium/NAV) and short the highest decile ETFs (highest Premium/NAV).
   1. Rebalance each month.
   2. This long/short portfolio has a monthly return of 0.70% (0.94% for long leg and 0.24% for the short leg as shown in Exhibit 9).
   3. Controlling for bond factors (in Exhibit 10), this long short portfolio earns an abnormal return of 0.96% per month.

### **Commentary:**

* Paper points out that arbitrage may not be a profitable strategy.
* Paper shows the persistence of these premiums and discounts (measured up to a month as shown in Exhibit 8).
* Premiums increase if a Bond ETF is illiquid.

**Anyone tried this?**
