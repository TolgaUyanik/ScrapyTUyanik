---
title: "Do Decomposed Financial Ratios Predict Stock Returns and Fundamentals Better?"
slug: "do-decomposed-financial-ratios-predict-stock-returns-and-fundamentals-better"
date: "2012-08-07"
modified: "2022-06-10"
url: "https://alphaarchitect.com/do-decomposed-financial-ratios-predict-stock-returns-and-fundamentals-better/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Do Decomposed Financial Ratios Predict Stock Returns and Fundamentals Better?

> Do Decomposed Financial Ratios Predict Stock Returns and Fundamentals Better? Xiaoquan Jiang, Bong Soo Leei A version of the paper can be found here. Abstract: […]

# Do Decomposed Financial Ratios Predict Stock Returns and Fundamentals Better?

* Xiaoquan Jiang, Bong Soo Leei
* A version of the paper can be found [here](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1535585).

### **Abstract:**

> “We investigate the prediction of excess returns and fundamentals by financial ratios, which include dividend-price ratios, earnings-price ratios, and book-to-market ratios, by decomposing financial ratios into a cyclical component and a stochastic trend component. We find both components predict excess returns and fundamentals. Cyclical components predict increases in future stock returns, while stochastic trend components predict declines in future stock returns in long horizons. This helps explain previous findings that financial ratios in the absence of decomposition find weak predictive power in short horizons and some predictive power in long horizons. We also find both components predict fundamentals.”

### **Data Sources:**

This research uses stock prices (P), dividends (D, four-quarter moving sum of dividends), and earnings (E, four-quarter moving sum of earnings) of the Standard and Poor’s (S&P) 500 index from 1926:Q1 to 2008:Q4. The risk-free rates (Rf) are measured as one-month T-bill rates from CRSP. The consumption-wealth ratio (CAY) is from Lettau and Ludvigson (2001). Inflation rates are based on the Consumer Price Index from the Bureau of Labor Statistics.

### **Discussion:**

In this research, the authors examine the predictive power of financial ratios (log dividend-price ratio (DP), log earnings price ratio (EP), and log book-to-market ratio (BP)) in predicting stock returns and fundamentals. All the ratios are measured as the difference between the log of fundamentals and log of prices.

The authors decompose the financial ratios into a cyclical component and a stochastic trend component using the Hodrick and Prescott’s (1997) Kalman filter procedure.

Table1 shows report summary statistics of the three financial ratios (DP, EP, and BP), their cyclical components (CDP, CEP, and CBP), their stochastic trend components (GDP, GEP, and GBP), consumption-wealth ratio CAY, relative T-bill rates (RTB), and log excess returns (R).

[![](https://alphaarchitect.com/wp-content/uploads/2012/08/102.jpg)](https://alphaarchitect.com/wp-content/uploads/2012/08/102.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

We see a downward trend for all three financial ratios. R, CAY, and RTB are stationary, while all financial ratios are highly persistent.

In  long-horizon prediction tests, the authors run regressions using a cyclical component and a stochastic trend component.

[![](https://alphaarchitect.com/wp-content/uploads/2012/08/103.jpg)](https://alphaarchitect.com/wp-content/uploads/2012/08/103.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Each component of financial ratios predicts future excess returns. The cyclical components, which are associated with the expected return with a mean-reverting component around a business-cycle-length, predict future excess returns with a positive coefficient. While the stochastic trend components predict future excess returns with a negative coefficient.  
  
A similar observation is made in multivariate forecast regression using both cyclical and stochastic trend components as predictors in Table 3.

[![](https://alphaarchitect.com/wp-content/uploads/2012/08/104.jpg)](https://alphaarchitect.com/wp-content/uploads/2012/08/104.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Investment Strategy:**

1. Decompose financial ratios into a stochastic trend component and a cyclical component.
2. Predict stock returns by the cyclical component over short horizons and by stochastic trend component over long horizons.
3. Predict dividend growth by the cyclical component of dividend-price ratio, especially over short horizons.
4. Predict accounting returns by the stochastic trend component of book-to-market ratio, in particular, over long horizons.
5. Predict earnings growth by the cyclical component of the earning-price ratio over short horizons and by the stochastic trend component of the earning-price ratio over long horizons.
6. Make money.

### **Commentary:**

Since the two components of financial ratios tend to offset much of each other’s prediction, the decomposed financial ratios based on the Hodrick and Prescott (1997) method help us predict stock returns and fundamentals better than financial ratios alone in both long and short horizons.
