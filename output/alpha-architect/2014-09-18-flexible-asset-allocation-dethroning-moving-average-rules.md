---
title: "Flexible Asset Allocation: Dethroning Moving Average Rules?"
slug: "flexible-asset-allocation-dethroning-moving-average-rules"
date: "2014-09-18"
modified: "2022-05-31"
url: "https://alphaarchitect.com/flexible-asset-allocation-dethroning-moving-average-rules/"
categories: ["Research Insights", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Flexible Asset Allocation: Dethroning Moving Average Rules?

> Strategy Summary The flexible asset allocation strategy was first proposed by Keller and Putten (2012), in their paper “Generalized Momentum and Flexible Asset Allocation (FAA): An […]

### **Strategy Summary**

The [flexible asset allocation strategy](https://alphaarchitect.com//2013/01/03/flexible-asset-allocation/#.U_DYDfldVMU) was first proposed by Keller and Putten (2012), in their paper “[Generalized Momentum and Flexible Asset Allocation (FAA): An Heuristic Approach](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2193735)“. The flexible asset allocation strategy, hereafter, FAA, incorporates momentum, volatility and correlation into risk regime determination and adjusts weights among 7 different assets. In this post, we will do some back tests on the FAA Strategy. FAA ranks assets based on three factors: **momentum, volatility and correlation**. The best strategy discussed in paper is as follows: 100% weight on 4-month relative momentum, 50% weight on 4-month volatility, and 50% weight on the 4-month correlation. Invest in the top 3 out of 7 assets. Our replication results are similar to the paper’s results. We also conducted an out-of-sample robustness test for the time period of August 1997 to January 2005 and a full sample test from September 1997 to July 2014:

* FAA has significantly higher risk-adjusted return than the EW of 7 assets.
* FAA decreases maximum drawdown dramatically.
* When adjusting look-back periods, the system is robust.

FAA can directly add value when identifying down side risk regimes and decrease maximum drawdown.

We compare moving average rules to FAA and find that FAA historically adds significant value.

However, the added complication does **make us wary of data-fitting** and the time **period is very short.**

### **Data Description**

The following 7 asset classes are used in the back-test:

* Vanguard Total Stock Market Index Fund — VTSMX
* Fidelity Diversified International Fund — FDIVX
* Vanguard Emerging Markets Stock Index Fund — VEIEX
* Vanguard Short-Term Treasury Fund — VFISX
* Vanguard Total Bond Market Index Fund — VBMFX
* Oppenheimer Commodity Strategy Total Return Fund — QRAAX
* Vanguard REIT Index Fund — VGSIX

Daily and monthly total returns are used. Simulation results are from January 31, 2005 through July 31, 2014. No transaction costs are included in any of our analysis. All results are gross of any transaction fees, management fees, or any other fees that might be associated with executing the models in real-time.

### **Strategies Background**

The paper discusses 4 different strategies:

1. **R** –> Relative momentum. Rank assets based on relative 4 month momentum, select top 3 assets.
2. **RA** –>  Relative momentum and absolute momentum. Rank assets based on relative momentum; if absolute momentum > 1, invest; if not, go to risk-free.
3. **RAV** –>  Relative & absolute momentum and volatility. Rank on relative momentum; rank on volatility. 100% weight on relmom + 50% weight on Vol. and rank; if absolute momentum > 1, invest; if not, go to risk-free.
4. **RAVC** –>  Relative & absolute momentum, volatility, and correlation. Rank on relmom; rank on volatility; rank on average correlation. 100% MA + 50% vol. + 50% correl. and rank. If absolute momentum > 1, invest; if not, go to risk-free.

We also include the following legend:

1. **EW\_BM** –>Equal-weight benchmark; monthly-rebalanced.

Our results show that the best strategy is RAVC with 4-month look back period in each factor. We will be focusing on discussing RAVC in the rest of the report. Out-of-sample robustness check explores the effects of adjusting the look-back length. For example, RAVC433 stands for 4-month look-back for momentum, 3-month look-back for volatility, and a 3-month look-back for correlation. Here is a chart describing the FAA strategy:

[![2014-08-12 12_20_34-FAA_v03.pptx - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-12-12_20_34-FAA_v03.pptx-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-12-12_20_34-FAA_v03.pptx-Microsoft-PowerPoint-Product-Activation-Failed.png)

\*If tied with more than 3 assets, EW all of them. If less than 3 assets, invest the rest into risk-free.

### **Paper Replication**

#### **1/1/2005 to 7/31/2014**

In the paper, the data period is from 1/1/2005 to 12/31/2012. Our method is exactly the same as in the paper, but our data period expands to most recent time for the study, which is July 31, 2014. Our replicated results are very close and consistent to those claimed in the paper. The first graph below is our replication result of the four strategies and the Benchmark (BM), and the second graph is the result from paper. We can see the trend is almost the same.

[![2014-08-18 11_10_05-Microsoft Excel (Product Activation Failed) - FAA_ yang_v04.xlsx](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-08-18-11_10_05-Microsoft-Excel-Product-Activation-Failed-FAA_-yang_v04.xlsx.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-08-18-11_10_05-Microsoft-Excel-Product-Activation-Failed-FAA_-yang_v04.xlsx.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

[![2014-08-12 11_14_40-FAA_v03.pdf - Adobe Reader](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-12-11_14_40-FAA_v03.pdf-Adobe-Reader.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-12-11_14_40-FAA_v03.pdf-Adobe-Reader.png) We also made detailed comparisons between our results and the paper results. Note that the paper data period ends at 12/2012, while our period is expanded to 7/2014.

[![2014-08-12 12_02_18-Presentation1 - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-12-12_02_18-Presentation1-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-12-12_02_18-Presentation1-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Summary Statistics**

Adding [Gary Antonacci’s](http://optimalmomentum.blogspot.com/2013/10/momentumthe-only-practical-anomaly.html) absolute momentum can significantly decrease downside risks. RAVC has a very high risk-adjusted return, lowest Standard deviation, lowest Downside risks, and highest Sharpe Ratio.

[![2014-08-12 12_03_02-Presentation1 - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-12-12_03_02-Presentation1-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-12-12_03_02-Presentation1-Microsoft-PowerPoint-Product-Activation-Failed.png)

RAVC444 stands for 4-month look-back for momentum, 4-month look-back for volatility, and a 4-month look-back for correlation. The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

**Annual Returns**  
RAVC has strong relative performance.

[![2014-08-12 12_07_26-Presentation1 - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-12-12_07_26-Presentation1-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-12-12_07_26-Presentation1-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Out-of-sample Backtest**

#### **8/1/1997 to 1/31/2005**

We include January because the authors conduct their study in a similar way (overlapping one month with the other sample). Results are not quantitatively different if we exclude the month of January. In this out-of-sample backtest, RAVC is still relatively strong on Standard Deviation, Sortino Ratio and Sharpe Ratio.

[![2014-08-12 13_13_02-Presentation1 - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-12-13_13_02-Presentation1-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/2014-08-12-13_13_02-Presentation1-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

**Robustness Results**  
We vary the look-back period to assess robustness.

[![3](https://alphaarchitect.com/wp-content/uploads/2014/08/3.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/3.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Full Sample Backtest**

#### **9/1/1997 to 7/31/2014**

We use September and not an August start so we can test a 5-month look-back in some specifications.

#### **Summary Statistics**

RAVC and RA both perform good, and a simple absolute momentum factor can significantly decrease the drawdown.

[![4](https://alphaarchitect.com/wp-content/uploads/2014/08/4.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/4.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

**Robustness Results**  
Given different combinations of the look-back periods, RAVC’s performances are strong. One significant change is that under 3-month look-back periods, the drawdown increases.

[![5](https://alphaarchitect.com/wp-content/uploads/2014/08/5.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/5.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Most of the CAGR is generated from momentum. Taking volatility and correlation into account decreases the downside risk.

[![6](https://alphaarchitect.com/wp-content/uploads/2014/08/6.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/6.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

**Annual Returns**  
RAVC has never had a down year, historically.

[![8](https://alphaarchitect.com/wp-content/uploads/2014/08/8.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/8.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

**Invested Growth**  
RAVC has relatively better invested growth.

[![9](https://alphaarchitect.com/wp-content/uploads/2014/08/9.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/9.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

**Market Cycle Performance**  
PAVC performs the best in all bear markets.

[![10](https://alphaarchitect.com/wp-content/uploads/2014/08/10.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/10.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Rolling CAGR Analysis**

RAVC performs the best overall. RAV and RA are similar.

[![11](https://alphaarchitect.com/wp-content/uploads/2014/08/11.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/11.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Drawdown Analysis**

RAVC provides the best downside protection.

[![12](https://alphaarchitect.com/wp-content/uploads/2014/08/12.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/12.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Short-Term Event Stress Tests**

RAVC performs well during stress events.

[![13](https://alphaarchitect.com/wp-content/uploads/2014/08/13.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/13.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Moving Average Rule Comparison**

#### **4/1/1998 to 7/31/2014**

We use a simple moving average trading rule that compares the current price relative to the average of the past 12 months. If the current price is greater than the 12-month average, the strategy invests in the asset class; otherwise the allocation for the strategy is put into treasury bills.

* RAVC outperforms all other strategies.
* MA is highly correlated with RAVC.

[![14](https://alphaarchitect.com/wp-content/uploads/2014/08/14.png)](https://alphaarchitect.com/wp-content/uploads/2014/08/14.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.
