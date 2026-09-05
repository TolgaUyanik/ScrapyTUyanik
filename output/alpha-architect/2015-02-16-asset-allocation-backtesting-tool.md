---
title: "Our Asset Allocation Backtest Tool (a how to guide)"
slug: "asset-allocation-backtesting-tool"
date: "2015-02-16"
modified: "2022-05-04"
url: "https://alphaarchitect.com/asset-allocation-backtesting-tool/"
categories: ["Tool How-To-Guides"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Our Asset Allocation Backtest Tool (a how to guide)

> Our Asset Allocation Backtesting Tool is Live! You can build and backest your own asset allocation portfolio using our “Allocation Architect” tool. How to Access […]

### Our Asset Allocation Backtesting Tool is Live!

You can build and backest your own asset allocation portfolio using our “Allocation Architect” tool.

### How to Access the Tool?

**Step 1:** Click “Our tools” tab from our [main website page](https://alphaarchitect.com/).

![Alpha Architect Tools](https://alphaarchitect.com/wp-content/uploads/2015/02/Alpha-Architect-Tools-1030x621.png)

Click to enlarge.

**Step 2:** If you already have a username and password, please [sign in](http://tools.alphaarchitect.com/login). If you are new to our tool, just take 30 second to [sign up](http://tools.alphaarchitect.com/signup) and use it for free!

![Alpha Architect Tools Sign in](https://alphaarchitect.com/wp-content/uploads/2015/02/Alpha-Architect-Tools-Sign-in-1030x676.png)

Click to enlarge.

**Step 3:** Click on the [“Allocation Architect” Tool](http://tools.alphaarchitect.com/tools/ma)

![Alpha Architect Tools Asset Allocation](https://alphaarchitect.com/wp-content/uploads/2015/02/Alpha-Architect-Tools-Asset-Allocation-1030x716.png)

Click to enlarge.

### How to Use the “Allocation Architect” Tool?

This tool will help you build a custom allocation portfolio by allowing the user to select different asset class weights, different time horizons, and toggle risk-management.

**Step 1**: Portfolio Inputs: select the time period you want to back test, and select the lookback for the risk-management rules ([Simple Moving Average “SMA” rules](http://en.wikipedia.org/wiki/Moving_average) and [Time Series Momentum “TSMOM”](https://alphaarchitect.com//2015/01/06/quantitative-momentum-research-intermediate-term-momentum/#.VOEBaPnF-k8)). For example, if the user inputs “12” for the SMA and TSMOM rules, when risk-management is selected, the system will apply a 12-month SMA and a 12-month TSMOM rule to each asset class. If the asset class signal for SMA and TSMOM is positive, the asset will be 100% invested; if the signals are mixed, the asset will be 50% invested; and if the signals are both negative, the asset will be 0% invested (proceeds will go into treasury bills). SMA and TSMOM rules are explained [here.](https://alphaarchitect.com//2014/12/02/our-robust-asset-allocation-raa-solution/)

***1. Time Series Momentum Rule (MOM)***

* Excess return = total return over past x months less return of T-bill
  + If Excess return >0, go long risky assets. Otherwise, go alternative assets (T-bills or Zero).
  + Popularized by [Gary Antonacci](http://www.dualmomentum.net/) and rigorously examined by [Moskowitz et al.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2089463)

***2. Simple Moving Average Rule (SMA)***

* Moving Average (N) = average N month prices
  + If Current Price – Moving Average (N) > 0, go long risky assets. Otherwise, go alternative assets (T-bills or Zero).

**Step 2:** Input custom allocation weights for the different assets:  Input numbers directly or toggle the “up” and “down” buttons to adjust weights. We provide 5 core asset classes:

* *Domestic Equity*
* *International Equity*
* *Real Estate*
* *Commodities*
* *10-year Treasury Bonds*

We also include value and momentum equity exposures for domestic and international markets as well as the treasury bill return.  
The total weights must equal 100%.  
*\*Tips: If you want to learn more about each asset, just point your mouse over them. You can get access to the data resources by clicking them.*

**Step 3:** Click “Calculate” button to see the performance results.

![Alpha Architect Tools Asset Allocation_main chart](https://alphaarchitect.com/wp-content/uploads/2015/02/Alpha-Architect-Tools-Asset-Allocation_main-chart.png)

Click to enlarge.

### Understanding the Performance results

**Step 1**: When you hit the “Calculate” button the server will calculate your results (be patient, this could take 5 to 15 seconds).

* Show “risk managed” results by clicking the slider button.
* Your custom portfolio (with/without risk-managed) will be compared to the performance of the balanced version of the [“Robust Asset Allocation Model](https://alphaarchitect.com//2014/12/02/our-robust-asset-allocation-raa-solution/).” The moderate and aggressive versions are also available by checking the boxes.
  + **RAA\_BAL** = 40% Equity; 40% Real; 20% Bonds. Equity split between value and momentum. Risk-Managed.
  + **RAA\_MOD** = 60% Equity; 20% Real; 20% Bonds. Equity split between value and momentum. Risk-Managed.
  + **RAA\_AGG**= 80% Equity; 10% Real; 10% Bonds. Equity split between value and momentum. Risk-Managed.

![Alpha Architect Tools Asset Allocation risk management](https://alphaarchitect.com/wp-content/uploads/2015/02/Alpha-Architect-Tools-Asset-Allocation-risk-management.png)

Click to enlarge.

**Step 2:** The summary tab shows the summary statistics for each portfolio.

* **CAGR:** Compound annual growth rate
* **Standard Deviation:** Sample standard deviation
* **Downside Deviation:** Sample standard deviation, but only monthly observations below 41.67bps (5%/12) are included in the calculation
* **Sharpe Ratio (annualized):** Average monthly return minus treasury bills divided by standard deviation
* **Sortino** **Ratio (annualized):** Average monthly return minus treasury bills divided by downside deviation
* **Worst Drawdown:** Worst peak to trough performance (measured based on monthly returns)

![Alpha Architect Tools Asset Allocation summary](https://alphaarchitect.com/wp-content/uploads/2015/02/Alpha-Architect-Tools-Asset-Allocation-summary.png)

Click to Enlarge.

**Step 3:** The Rolling CAGR shows the rolling compound annual growth rates over X years. We provide results for 1-, 3-, 5-, and 10-year rolling horizons when the data is available.

![Alpha Architect Tools Asset Allocation Rolling CAGR](https://alphaarchitect.com/wp-content/uploads/2015/02/Alpha-Architect-Tools-Asset-Allocation-Rolling-CAGR.png)

Click to Enlarge.

**Step 4**: The Drawdown tab shows the summary statistics for each portfolio.

* The Max Drawdown measure is calculated as the peak-to-trough decline since inception, using monthly returns.
* The Worst-Case Holding Period returns calculate all possible holding period returns for a given holding period length and reports the worst possible holding period return. For example, the worst 6-month holding period return is identified by calculating all possible 6-month holding period returns since inception. For a 12-month track record, there would be 7 possible 6-month holding period returns (e.g., month 1 to month 6, month 2 to month 7, and so forth). We then report the 6-month holding period return that has the worst performance as the worst 6-month holding period return. It is possible that the worst possible 3-month holding period return may be worse than the worst possible 6-month holding period return, because the holding period requirement is different. For example, there might be a -10% 3-month holding period return from month 1 to month 3, and a month 1 to month 6 holding period return of -5%, which happens to be the worst 6-month holding period return. In this scenario the worst case 3-month holding period return will be larger than the worst case 6-month holding period return.

![Alpha Architect Tools Asset Allocation drawdown](https://alphaarchitect.com/wp-content/uploads/2015/02/Alpha-Architect-Tools-Asset-Allocation-drawdown.png)

Click to enlarge.

**Step 5:** The returns tab shows the annual returns for each portfolio.

![Alpha Architect Tools Asset Allocation Returns](https://alphaarchitect.com/wp-content/uploads/2015/02/Alpha-Architect-Tools-Asset-Allocation-Returns.png)

Click to enlarge.

Access the Allocation Architect Tools [here.](http://tools.alphaarchitect.com/tools/ma)
