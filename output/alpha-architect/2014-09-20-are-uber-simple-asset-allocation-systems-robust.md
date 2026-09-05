---
title: "Tactical Asset Allocation: Are Uber-Simple Systems Robust?"
slug: "are-uber-simple-asset-allocation-systems-robust"
date: "2014-09-20"
modified: "2022-05-31"
url: "https://alphaarchitect.com/are-uber-simple-asset-allocation-systems-robust/"
categories: ["Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Tactical Asset Allocation: Are Uber-Simple Systems Robust?

> Simple and Effective Market Timing with Tactical Asset Allocation Lewis A. Glenn A version of the paper can be found here. Want a summary of […]

### Simple and Effective Market Timing with Tactical Asset Allocation

* Lewis A. Glenn
* A version of the paper can be found [here](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2437049).
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category](https://alphaarchitect.com/category/academic-research/)!

### **Abstract:**

> A simple market timing algorithm is examined that switches from an exchange traded fund representing U. S. equities to one holding treasury long bonds every month on the last day, the **switch being made to whichever ETF has the greatest ratio of current adjusted closing price to adjusted closing price μ months earlier.** The parameter μ is determined so as to maximize total return and minimize the total number of trades, however the results are relatively insensitive to μ over a fairly wide range. The performance of this scheme is compared to that of an Ivy 5 portfolio consisting initially of equal dollar amounts of ETFs in U. S. equities, foreign large blend, 7-10 year treasuries, real estate, and commodities. As with the paired switching approach, each ETF is purchased only once a month, on the last day, in this case only if its adjusted closing price exceeds the 10-month simple moving average (SMA). Otherwise that portion of the portfolio is invested in a cash surrogate.
>
> Comparison is made over the 10-year period ending on 12/31/13. It is shown that **the average annual return of the paired switching algorithm exceeds 30% in this period, which is 3 times greater than that of the Ivy 5.** Moreover, only 45 trades were required for the paired switching approach, whereas the Ivy 5 required 70 in the same period. **The maximum draw down was 14.6% for the Ivy 5 and 18.8% for paired switching.**

### **Alpha Highlight:**

The IVY 5 portfolio, described by [Faber(2007)](http://www.trendfollowing.com/whitepaper/CMT-Simple.pdf) and then further elaborated by [Faber and Richardson (2009)](http://www.theivyportfolio.com/), is a portfolio of 5 asset classes, including the S&P 500 index, the MSCI EAFE index, the US 10-year government bonds, a commercial real estate index, and a commodity index (GSCI). The “simple and effective market timing trading rule” is to buy each index when the monthly price exceeds the 10-month simple moving average (SMA), and to invest in cash (or the risk free asset) when the moving average rule is broken. This strategy is simple and easy, which is why we offer a [low-cost version of the concept](https://alphaarchitect.com/wp-content/uploads/2018/01/RAA_Factsheet_vF.pdf).

In this paper, the author extends the IVY5 with MA concept, and points out that the simple moving average (SMA) method on the IVY 5 portfolio may not work as well as a 2-asset class paired switching method.   The paired switching method concept requires one to invest in a pair of negatively correlated assets and periodically switch the position based on relative performance of the 2 assets in the pair (eg. SPY and TLT)

The results in the paper show that a simple switching system (Simple TAA) between SPY and TLT outperforms the IVY 5 portfolio from 2004/01 to 2013/12. We replicate the backtest presented in the paper and comment accordingly.

### **Key Results:**

1. The Simple TAA strategy works well between 2004/01 and 2013/12.
2. Out of sample results from 1978 to 2003 suggests that the **IVY 5 outperforms the Simple TAA strategy**.
3. Out of sample results from 1927 to 1977 suggests that the **Simple TAA strategy is not robust**. A fixed allocation can achieve similar performance.

### **Our Replication Process:**

##### Same Period in this Paper: 2004/01/02 to 2013/12/31

Here are the acronyms in our report:

* **SPY-TLT\_3\_MOM:** when SP500’s total return over the last 3 months is bigger or equal to TLT’s total return over last 3 months, invest SPY; otherwise, invest in risk-free.
* **IVY5:** Equal-weighted portfolio of SP500, LTR (10-year), GSCI (commodity), REIT (commercial real estate), EAFE (international)
* **IVY5\_MA\_1\_10:** IVY5\_MA is IVY5 with 10-month MA rule trigger: when the last month’s price is bigger than the average of the last 10 month price, risk on; otherwise, risk-off and go to risk-free asset.
* **TLT:** iShares Barclays 20+ Year Treasury Bond.
* **SP500:** S&P500 total return index.
* **EAFE:** MSCI EAFE Total Return Index
* **LTR:** The Merrill Lynch 10-year U.S. Treasury Futures Total Return Index
* **REIT:** FTSE NAREIT All Equity REITS Total Return Index
* **GSCI:** S&P GSCI Total Return CME

### Summary Statistics:

The simple TAA (simple switching method) outperforms during 2004/1 to 2013/12.

[![2014-09-02 10_02_34-Simple and effective TAA_v2.pptx - Microsoft PowerPoint (Product Activation Fail](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_02_34-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_02_34-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Dollar Growth:

Our replication matches the paper’s results. The chart below is from the paper, and the second chart is our replication results.

Chart from the original paper:

[![2014-09-02 10_07_07-Simple and effective TAA_v2.pptx - Microsoft PowerPoint (Product Activation Fail](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_07_07-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_07_07-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Our replication result:

[![2014-09-02 14_07_31-Simple and effective TAA_v2 - Microsoft PowerPoint](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-14_07_31-Simple-and-effective-TAA_v2-Microsoft-PowerPoint.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-14_07_31-Simple-and-effective-TAA_v2-Microsoft-PowerPoint.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Annual Returns:

The simple TAA (simple switching method) works well during the 2008 financial crisis, driven by the performance of the long-bond.

[![2014-09-02 10_08_29-Simple and effective TAA_v2.pptx - Microsoft PowerPoint (Product Activation Fail](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_08_29-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_08_29-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### DrawDown Analysis:

The simple TAA (simple switching method) has smaller drawdowns.

[![2014-09-02 10_11_18-Simple and effective TAA_v2.pptx - Microsoft PowerPoint (Product Activation Fail](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_11_18-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_11_18-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Robustness Analysis:

**Market Cycle:** Strong recent bull market performance from the simple TAA (simple switching method).

[![2014-09-02 10_17_56-Simple and effective TAA_v2.pptx - Microsoft PowerPoint (Product Activation Fail](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_17_56-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_17_56-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

**Rolling CAGRs:**Simple TAA (simple switching method) performance is driven by the past 5 years.

[![2014-09-02 10_19_55-Simple and effective TAA_v2.pptx - Microsoft PowerPoint (Product Activation Fail](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_19_55-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_19_55-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

**Rolling Drawdowns:** Simple TAA (simple switching method) has strong drawdown protection.

[![2014-09-02 10_21_31-Simple and effective TAA_v2.pptx - Microsoft PowerPoint (Product Activation Fail](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_21_31-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_21_31-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Out-of-Sample Summary Statistics:

#### 1978/1/1 to 2003/12/31 and 2004/1/1 to 2013/12/31

The replication results look good, but the 2004 to 2013 time period is short and unique.

*How about some out-of-sample tests?*  
To do our out-of-sample test, we use the 10 years long-term bond (LTR) to replace the iShares Barclays 20+ Year Treasury Bond (TLT) due to data availability.

* **SPY-LTR\_3\_MOM:** when SP500’s total return over last 3 months is bigger or equal to LTR’s total return over last 3 months, risk on; otherwise, invest in risk-free.
* **IVY5:** Equal-weighted portfolio of SP500, LTR, GSCI, REIT, and EAFE.
* **IVY5\_MA\_1\_10:** IVY5\_MA is IVY5 with MA rule trigger: when the last month’s price is bigger than the average of the last 10 month price, risk on; otherwise, risk-off and go to the risk-free asset.
* **LTR:** 10 year long-term bond.
* **SP500:** S&P500 total return index.

##### Summary Statistics (1978/1/1 to 2003/12/31):

Simple TAA underperforms IVY5\_MA out of sample. IVY5\_MA has much higher Sharpe Ratio than other strategies.

[![2014-09-02 14_39_50-Microsoft Excel - TAA_analysistool_v29](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-14_39_50-Microsoft-Excel-TAA_analysistool_v29.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-14_39_50-Microsoft-Excel-TAA_analysistool_v29.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Summary Statistics (2004/1/1 to 2013/12/31):

Simple TAA with 10-year bonds outperforms IVY5\_MA, but the results aren’t as strong as the results with TLT. Owning longer duration treasuries through the 2008 crisis is a key driver of returns.

[![](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-14_35_14-Microsoft-Excel-TAA_analysistool_v29.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-14_35_14-Microsoft-Excel-TAA_analysistool_v29.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Out-of-Sample Summary Statistics:

#### 1927/4/1 to 1977/12/31 and 1978/1/31 to 2013/12/31.

In this out-of-sample test we examine 2 fixed allocation methods.

* **SPY-LTR\_3\_MOM:** when SP500’s total return over last 3 months is bigger or equal to LTR’s total return over last 3 months, risk on; otherwise, risk off.
* **60\_40 SPY-LTR:** 60% in SP500, 40% in LTR.
* **70\_30 SPY-LTR:** 70% in SP500, 30% in LTR.
* **LTR:**10 years long-term bond.
* **SP500:**S&P500 total return index.

##### Summary Statistics (1927/4/1 to 1977/12/31):

Simple TAA (simple switching method) performs similar on a risk-adjusted basis to fixed allocations. There is no evidence for value-add.

[![2014-09-02 10_34_18-Simple and effective TAA_v2.pptx - Microsoft PowerPoint (Product Activation Fail](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_34_18-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_34_18-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Summary Statistics (1978/1/31 to 2013/12/31):

Simple TAA (simple switching method) performs similar on a risk-adjusted basis to fixed allocations. Again, no strong evidence for value-add.

[![2014-09-02 10_40_14-Simple and effective TAA_v2.pptx - Microsoft PowerPoint (Product Activation Fail](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_40_14-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)](https://alphaarchitect.com/wp-content/uploads/2014/09/2014-09-02-10_40_14-Simple-and-effective-TAA_v2.pptx-Microsoft-PowerPoint-Product-Activation-Fail.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Conclusion

The out-performance of the Simple TAA strategy is mainly driven by long duration bonds. In out-of-sample tests, Simple TAA performs similar to fixed 60/40 and 70/30and underperforms the IVY5 with an MA asset allocation trading rule. Simple TAA is an interesting idea, but robustness tests suggests that we should be suspect of the extreme outperformance during the 2004 to 2013 time period analyzed in the paper.
