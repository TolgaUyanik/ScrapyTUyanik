---
title: "An After-Hours Arbitrage Opportunity: $50k to $760k in 12 years?"
slug: "an-after-hours-arbitrage-opportunity-50k-to-760k-in-12-years"
date: "2014-02-20"
modified: "2022-06-01"
url: "https://alphaarchitect.com/an-after-hours-arbitrage-opportunity-50k-to-760k-in-12-years/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# An After-Hours Arbitrage Opportunity: $50k to $760k in 12 years?

> Slow Price Adjustment to Public News in After-Hours Trading Jiasun Li A version of the paper can be found here. Want a summary of academic papers […]

### Slow Price Adjustment to Public News in After-Hours Trading

* Jiasun Li
* A version of the paper can be found [here.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2379126)
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category!](https://alphaarchitect.com/category/academic-research/)

### **Abstract:**

> During 2002-2012 (2,769 trading days) stock prices adjusted slowly in response to public news in after-hours trading. 5,881 rule-based intra-day trading opportunities each offered an average return of 1.53% within less than 4 hours. After trading costs and controlling for market breadth, price impact, execution latency and multitask incapability, a marginal investor who exploited this slow price adjustment could beat the market by 10% per year without proportional risk. To assess trading costs, I conducted a real trading experiment. Under Regulation National Market System (Reg NMS), I find significant use of intermarket sweep orders (ISO) that exploited this opportunity. The evidence suggests that individual investors’ contrarian behavior slowed down price adjustment. Other market frictions (investor inattention, limited arbitrage capital, short-sale constraints or market illiquidity) could not explain the slow price adjustment. The results highlight the economic significance of after-hours trading (particularly under Reg NMS).

### **Data Sources:**

IBES/TAQ, 2002 to 2012

### **Alpha Highlight:**

Quick trigger after-hours trading can be profitable!

[![Click to Enlarge](https://alphaarchitect.com/wp-content/uploads/2014/02/SSRN-id2379126.png)](https://alphaarchitect.com/wp-content/uploads/2014/02/SSRN-id2379126.png)

[Click to Enlarge] The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Strategy Summary:**

1. Paper documents systematic slow price adjustments in response to public news in after-hours significant trading volume.
   * Data includes all S&P 1500 firms from Jan 2002 to Dec 2012 that announce quarterly earnings report after the market closes at 4 pm.
     + Figure 1 illustrates the slow intraday price adjustment in after-hours trading following earnings announcements.
2. Strategy: Buy-PAS/ sell-NAS according to the announcement between 4pm to 8pm and hold the position until the end of the trading day.
   * Paper define a positive announcement surprise (PAS) to be announcement in which neither revenue nor EPS misses consensus estimates and at least one of them beats the corresponding consensus number. A negative announcement surprise (NAS) is defined conversely.
     + Figure 2 shows that the performance of this strategy is persistent. In the last 9 years no quarter had a negative total return.
     + Immediate response to the announcement generates a return of 1.53% within less than four hours. Even with a reaction delay of a minute, after-cost return is still 0.66%.
3. To further illustrate the economic significance of the slow price adjustment, paper uses a hypothetical investor with initial $50,000 in Jan 2002 who followed the buy-PAS/sell-NAS strategy.
   * Figure 3 shows the $50,000 increased to $759,577 by the end of 2012, while a buy-and-hold benchmark (S&P 500) would have increased to $62,112.
     + This assumes a 1 minute delay from the news and the trade being implemented (for the PAS and NAS).
     + This incorporates realistic transaction costs and market frictions into it, which is $0.005/share upper bound, and takes market breadth and price impact as explicit costs. The hypothetical investor caps each position size by the lower of her prevailing wealth and the volume in the first minute to account for market breadth. In addition, she further caps each position by 5,000 shares to address price impact.
     + If there are multiple PAS/NAS, the stock with the most analysts is bought (sold) for the PAS (NAS) strategy.
     + For days with no PAS or NAS, the money sits in cash.
4. Paper then reports the relative behaviors of ISO (Intermarket sweep orders) and non-ISO trade in after-hours and suggests that non-ISO posters’ contrarian behavior contributes to the slow price adjustment.
   * ISOs facilitate institutional investor’s need for execution immediacy. This represents 53.1% of the volume and represents a proxy for institutional trades.
   * To investigate whether non-ISO trade contrarianly compared to ISO trades, the paper classify each trade into either buy or sell initiated using the Lee-Ready Algorithm, and then define a “momentum trade” as a buy (sell) initiated trade after PAS (NAS) and a “contrarian trade” a sell (buy) initiated trade after PAS (NAS).
     + Table 4 shows that ISOs are more likely to be in momentum trades, and momentums trades are more likely to be exectuted through ISOs. This also shows that non-ISOs are more likely to be contrarian trades, and contrarian trades are more likely to be executed by non-ISOs.
       - Appears that the contrarian trades of individual investors (non-ISOs) leads to a slowdown of the price adjustment.
5. Finally, paper examines possible explanations for the slow price adjustment.
   * Table 5 shows that investor inattention, limited arbitrage capital, short-sale constraints or market illiquidity could not explain the slow price adjustment.

### **Strategy Commentary:**

* Requires daily rebalancing
* Intense trading costs associated with after-hours markets
* Limited scalability

**Nice little prop-trading strat?**
