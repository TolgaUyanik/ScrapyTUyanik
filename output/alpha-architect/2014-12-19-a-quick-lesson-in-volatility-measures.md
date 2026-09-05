---
title: "How to Calculate Volatility in Excel"
slug: "a-quick-lesson-in-volatility-measures"
date: "2014-12-19"
modified: "2022-06-13"
url: "https://alphaarchitect.com/a-quick-lesson-in-volatility-measures/"
categories: ["Introduction Course", "Investor Education", "Low Volatility Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# How to Calculate Volatility in Excel

> Wild-swinging oil prices have caused some chaos, or “volatility,” in the financial markets recently. We’ve also heard a lot in the financial media regarding the […]

Wild-swinging [oil prices](http://thereformedbroker.com/2014/12/12/oil-is-not-the-first-commodity-to-crash-in-the-post-crisis-period/) have caused some chaos, or “volatility,” in the financial markets recently. We’ve also heard a lot in the financial media regarding the strong performance of [“low volatility” funds](http://falkenblog.blogspot.com/2014/12/history-of-low-volatility-investing.html).

**But what exactly is “volatility” and how do we measure it?**  
We’ve posted some thoughts on the low volatility anomaly (e.g. [Avoid High Beta Stocks. Period.](https://alphaarchitect.com//2014/10/09/avoid-high-beta-stocks-period/#.VF0YGfnF9HU))

But the use of volatility is somewhat ambiguous.

In the studies we’ve conducted we’ve referenced  “beta” and Idiosyncratic volatility (“ivol”).

We thought it might make sense to take a quick break and describe how these concepts are calculated. We first describe 3 ways in which we can describe “volatility” and then we provide a spreadsheet so you can see these calculations in action.

**Standard Deviation:**  
When we talk about a security’s volatility, we first think of the “standard deviation” of stock returns, which measures the degree of fluctuations in relation to its mean return over a period of time. This measure is calculated independently of the market and only requires data on the stock.

**BETA:**  
While Standard Deviation measures the disparity of a security’s return over a period of time, “BETA”, another widely used metric, measures the co-movement of this security with the market. BETA can be calculated by regressing daily stock returns on a market benchmark (such as value weighted CRSP) over a period of time.

**Idiosyncratic volatility (IVOL):**  
Business school professors tell us that there are 2 types of risk: systematic risk and unsystematic risk. Systematic risk can be estimated by Beta. The idiosyncratic risk is the portion of risk that unexplained by BETA. We calculate Idiosyncratic volatility (IVOL) as the standard deviation of the residuals from a regression that uses Beta to estimate the relationship between a given asset and the market.  
  
**Calculation Example:**

1. We use Amazon (Ticker: AMZN) stock as a single stock example, and use the value weighted CRSP index as the market benchmark. If forming a portfolio on 1/31/13, we would use *daily* returns from 1/31/12-1/31/13 to calculate beta and IVOL. (We use daily data to improve frequency and accuracy.)
   * Data resource: [Fama French Library](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html), [Yahoo Finance](http://finance.yahoo.com/q/hp?s=AMZN+Historical+Prices).
2. BETA calculation follows the basic methodology in [Betting Against Beta](http://www.econ.yale.edu/~af227/pdf/Betting%20Against%20Beta%20-%20Frazzini%20and%20Pedersen.pdf).
3. IVOL calculation follows the basic methodology in [IVOL and the Cross-Section of Expected Returns.](http://www.bnet.fordham.edu/cakici/cakici_jfqa_forthcoming.pdf)

#### If you are interested, please click below to download the excel sheet.

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/Microsoft-Excel-Beta-and-IVOL-Example-Sheet.xlsx_2014-11-24_17-41-21-1030x529.png)](https://alphaarchitect.com/wp-content/uploads/2014/11/Beta-and-IVOL-Example-Sheet1.xlsx)

———————————–

[Beta-and-IVOL-Example-Sheet](https://alphaarchitect.com/wp-content/uploads/2014/11/Beta-and-IVOL-Example-Sheet1.xlsx)

———————————–
