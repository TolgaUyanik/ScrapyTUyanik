---
title: "Using Utilities to Time the Market"
slug: "using-utilities-to-time-the-market"
date: "2014-08-11"
modified: "2022-05-31"
url: "https://alphaarchitect.com/using-utilities-to-time-the-market/"
categories: ["Research Insights", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Using Utilities to Time the Market

> Strategy Background Beta Rotation strategy (BRS) is discussed by Charles Bilello and Michael Gayed in their new paper, “An International Approach to Beta Rotation: The […]

### Strategy Background

**Beta Rotation strategy (BRS)** is discussed by Charles Bilello and Michael Gayed in their new paper, “[An International Approach to Beta Rotation: The Strategy, Signal, and Power of Utilities](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2417974)” The paper shows significant rolling out performance over a simple buy and hold strategy of the market throughout multiple time periods. They won the 2014 Charles H. Dow Award based on their research. At the core, the strategy is *a simple buy and rotate of utility stocks based on the relative strength of the utility sector:*

> “When a price ratio (or the relative strength) of the Utilities sector to the broad market is positive over the prior 4-week period, position into Utilities for the following week. When a price ratio (or the relative strength) of the Utilities sector to the broad market is negative over the prior 4-week period, position into the broad market for the following week.”  
> “In order to achieve a more tactical strategy that is better able to adapt to intra-month volatility, we converted the monthly time frame into a weekly signal.”

We replicate the strategy and put it through a barrage of robustness tests. The results hold up, but are less impressive than those from the original paper (likely due to methodological changes).

As a thought experiment we looked at a long short strategy that maximally exploits any edge the BRS system might have in timing the market. There is no evidence the L/S system works, which suggests the timing model is not overly impressive. Nonetheless, we have never found ANY timing model that is overly impressive.

Overall impression on the timing system: **definitely worth a look.**

### Simulation Background

Simulated Historical Performance: 1/1/1927 to 12/31/2013.

1. Instead of using weekly signal, we use monthly signal, which is more practical and serves as a robustness test to the original results.
   * Broader stock market index: VW\_CRSP
   * Utility stock market index: Utilities data from [Ken French Data Library](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)
2. We back test both BRS Long strategy and BRS Long + short strategy.
   * **BRS Long Strategy:** When the relative strength of the Utilities sector to the broad market is positive over the prior month, position into Utilities for the following month; otherwise, position into broad market for the following month.
   * **BRS Long + Short strategy:** When the relative strength of the Utilities sector to the broad market is positive over the prior month, position into Utilities and short broad market for the following month; otherwise, position into broad market and short Utilities for the following month.

### BRS Long Strategy

#### **Summary Statistics:**

* The BRS strategy shows some evidence for out performance with higher Sharpe and Sortino ratios.

[![2014-07-02 12_33_05-BRS_strategy - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_33_05-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_33_05-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Invested Growth:**

* Long term out performance
* High correlation with broad market

[![2014-07-02 12_35_52-BRS_strategy - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_35_52-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_35_52-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Drawdown Summary:**

* Still extremely risky and can suffer large drawdowns

[![2014-07-02 12_39_11-BRS_strategy - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_39_11-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed-1030x541.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_39_11-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Rolling CAGRs:**

* Strong long-term relative performance over 5-year cycles
* 70.02% chance of beating the VW\_CRSP over 5-year cycles
* 77.34% chance of beating the utility sector over 5-year cycles

[![2014-07-02 12_46_00-BRS_strategy - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_46_00-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_46_00-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Rolling Drawdowns:**

* Correlated drawdown episodes
* Large drawdowns during market downturns

[![2014-07-02 12_47_00-BRS_strategy - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_47_00-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_47_00-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Rolling Alphas:**

* No evidence for value-add over time

[![2014-07-02 12_49_09-BRS_strategy - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_49_09-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_49_09-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### BRS Long+Short Strategy

#### **Summary Statistics:**

* The BRS Long + Short strategy under performs overall, and is worse than pure buy and hold strategy
* Relatively lower volatility

[![2014-07-02 12_51_06-BRS_strategy - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_51_06-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_51_06-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Invested Growth:**

* Poor long-term performance

[![2014-07-02 12_52_20-BRS_strategy - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_52_20-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed-1030x554.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_52_20-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Drawdown Summary:**

* Less risky than the market because of the hedged nature of the strategy

[![2014-07-02 12_53_59-BRS_strategy - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_53_59-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_53_59-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Rolling CAGRs:**

* Weak long-term relative performance over 5-year cycles
* Only 23.98% chance of beating the VW\_CRSP over 5-year cycles
* Only 26.93% chance of beating utility stocks over 5-year cycles

[![2014-07-02 12_57_25-BRS_strategy - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_57_25-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-12_57_25-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Rolling Drawdowns:**

* Non correlated drawdown episodes
* Less affected by market drawdown events

[![2014-07-02 13_00_12-BRS_strategy - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-13_00_12-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed-1030x558.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-13_00_12-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

#### **Rolling Alphas:**

* No evidence for value-add over time

[![2014-07-02 13_01_51-BRS_strategy - Microsoft PowerPoint (Product Activation Failed)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-13_01_51-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)](https://alphaarchitect.com/wp-content/uploads/2014/07/2014-07-02-13_01_51-BRS_strategy-Microsoft-PowerPoint-Product-Activation-Failed.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.
