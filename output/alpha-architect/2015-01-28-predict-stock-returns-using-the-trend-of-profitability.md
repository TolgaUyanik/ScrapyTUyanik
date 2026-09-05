---
title: "Predict Stock Returns Using the TREND of Profitability"
slug: "predict-stock-returns-using-the-trend-of-profitability"
date: "2015-01-28"
modified: "2022-05-30"
url: "https://alphaarchitect.com/predict-stock-returns-using-the-trend-of-profitability/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Predict Stock Returns Using the TREND of Profitability

> The Trend in Firm Profitability and the Cross Section of Stock Returns Akbas, Jiang and Koch A version of the paper can be found here. Want […]

### The Trend in Firm Profitability and the Cross Section of Stock Returns

* Akbas, Jiang and Koch
* A version of the paper can be found [here](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2538867&download=yes).
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category](https://alphaarchitect.com/category/academic-research/).

### **Abstract:**

> This study shows that **the recent trajectory of a firm’s profits predicts future profitability and stock returns**. The predictive information contained in the trend of profitability is incremental beyond that provided by the profit level, and it is not subsumed by other well-known determinants of returns. Our results are consistent with risk-based valuation models which imply that, holding book-to-market and investment fixed, firms with a higher profit trend have higher expected profits, and should thus command higher expected returns. Alternative mispricing explanations that involve investor under or overreaction do not account for all our findings.

### Alpha Highlight:

Recent studies have shown that profitability-based factors have robust power to predict expected stock returns. For example, [Novy-Marx (2013)](http://rnm.simon.rochester.edu/research/OSoV.pdf) highlights the gross profitability premium in “[the other side of value](https://alphaarchitect.com//2011/02/19/the-other-side-of-value/#.VK6bhyvF9HU).” His research shows that gross profitability has roughly the same return-predictive power as the value factor (B/M). [Fama and French (2014)](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2287202) also add a profitability factor (and an investor factor) into their well known 3-factor model, thus expanding their model to a [5-factor model](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html).

The gross profitability factor is interesting, but may still be somewhat incomplete. Consider that when we examine the **“level”** of profitability, this “level” is static, but obviously firm operations are dynamic. What makes this paper worth reading is that it also considers the **“trend”** of profitability, and shows that the “trend” (upward, downward, or divergent) provides incremental predictive information about future profits and stock returns, after accounting for the static “level” of profitability outlined in Novy-Marx (2013).

This paper hypothesizes that firms with higher trends in profitability will outperform those with a lower trend. To test this conjecture, the paper **sorts firms based on profit trend** and compares their performances. It finds that a H-L hedge strategy that is long stocks with the highest trend in profits for the most recent quarter, and is short stocks with the lowest trend, yields an average **1%** monthly return.

Sounds great. But how exactly do we measure the profit trend?

Here’s a step by step review of how the paper thinks about this question:

1. Measure the quarterly *profit level* of a firm as the *average* *gross profit* (Novy-Marx, 2013) over the past 8 quarters (2 years).
2. Estimate the *profit trend* each quarter by regressing the firm’s gross profit on a time trend, quarterly seasonal dummies, and a constant, again using the past eight quarters of data. (See Equation 1 in paper)
3. The **coefficient** of the time trend is the measure of the trend in gross profit for that quarter. A larger coefficient indicates a higher profit trend for that quarter.
4. Sort portfolios each month into deciles based on the profit trend estimated in step 2.

### Key Findings:

The below table shows the results of one-way sort based on the firm’s profit trend over the sample period from 1977 to 2012.

The H-L hedge portfolio that is long high profit trend firms and short low profit trend firms earns an average EW monthly return of 0.83%.

[![2015-01-08 11_48_49-The trend in firm profitability.pdf - Adobe Reader](https://alphaarchitect.com/wp-content/uploads/2015/01/2015-01-08-11_48_49-The-trend-in-firm-profitability.pdf-Adobe-Reader.png)](https://alphaarchitect.com/wp-content/uploads/2015/01/2015-01-08-11_48_49-The-trend-in-firm-profitability.pdf-Adobe-Reader.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

To ensure the predictive power of profit trend is not subsumed by the overall profit level, the paper uses a two-way sorting method that measures profit trend predictive power after *controlling for the profit level*.

The results show that even after controlling for the level of profitability, firms with a high profit trend still outperform low profit trend firms by 0.50% to 0.85% per month.

[![2015-01-08 12_53_04-The trend in firm profitability.pdf - Adobe Reader](https://alphaarchitect.com/wp-content/uploads/2015/01/2015-01-08-12_53_04-The-trend-in-firm-profitability.pdf-Adobe-Reader1.png)](https://alphaarchitect.com/wp-content/uploads/2015/01/2015-01-08-12_53_04-The-trend-in-firm-profitability.pdf-Adobe-Reader1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Table 4 shows the results of a Fama-MacBeth regression analysis: It demonstrates that the predictive power of the profit trend is not in fact subsumed by other variables.

In every specification of models (1)~(4), the coefficient of the profit trend is **significantly positive**. In addition, the coefficient of the profit level (PROFIT) is also positive in all instances, which suggests that profit level and profit trend are both good predictive factors.

[![2015-01-08 11_49_34-The trend in firm profitability.pdf - Adobe Reader](https://alphaarchitect.com/wp-content/uploads/2015/01/2015-01-08-11_49_34-The-trend-in-firm-profitability.pdf-Adobe-Reader.png)](https://alphaarchitect.com/wp-content/uploads/2015/01/2015-01-08-11_49_34-The-trend-in-firm-profitability.pdf-Adobe-Reader.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

A reasonable question: will the high trend premiums encounter reversal or are they robust in the long run?

Figure 2.1 shows that our H-L hedge portfolio continues to earn significant premiums over the 24 post-formation months. After 2 years, the abnormal returns erode somewhat, but are still positive.

Figure 2.2 shows the cumulative return of the H-L hedge portfolio. A $1 initial amount appreciates to about $1.12 over five years.

[![2015-01-08 11_43_23-The trend in firm profitability.pdf - Adobe Reader](https://alphaarchitect.com/wp-content/uploads/2015/01/2015-01-08-11_43_23-The-trend-in-firm-profitability.pdf-Adobe-Reader.png)](https://alphaarchitect.com/wp-content/uploads/2015/01/2015-01-08-11_43_23-The-trend-in-firm-profitability.pdf-Adobe-Reader.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

It would appear that, at the margin, the trend in profits may add some marginal predictive ability beyond static profitability measurements.
