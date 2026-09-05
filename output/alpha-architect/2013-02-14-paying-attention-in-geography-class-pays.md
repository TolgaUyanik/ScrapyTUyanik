---
title: "Paying Attention in Geography Class…Pays!"
slug: "paying-attention-in-geography-class-pays"
date: "2013-02-14"
modified: "2022-06-02"
url: "https://alphaarchitect.com/paying-attention-in-geography-class-pays/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Paying Attention in Geography Class…Pays!

> Geographic Momentum Quoc H. Nguyen A version of the paper can be found here. Want a summary of academic papers with alpha? Check out our free Academic […]

### Geographic Momentum

* Quoc H. Nguyen
* A version of the paper can be found [here](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1921537).
* Want a summary of academic papers with alpha? Check out our free [Academic Alpha Database](https://alphaarchitect.com/tools/)!

### **Abstract:**

> Do investors pay attention to foreign market conditions when they evaluate multinational corporations? Using geographic segment disclosures by US multinational companies, I find that stock prices do not promptly incorporate information regarding changes in foreign market conditions. This, in turn, generates return predictability in the cross-section of firms with foreign operations. A simple trading strategy that exploits geographic information yields risk-adjusted return of 135 basis points per month, or 16.2% per year. The predictability cannot be explained by firm’s own momentum, industry momentum, post-earnings-announcement drift, being a conglomerate, or exposure to emerging market risk. Consistent with the investor inattention hypothesis, I further document that smaller firms, as well as firms with less analyst coverage, lower institutional holdings, or more complex foreign sales compositions exhibit stronger return predictability. This paper is the first to document the predictable link between foreign country-level indices returns and US firm-level stock returns, and adds to the growing literature concerning the role of investor inattention and firm complexity in price formation.

### **Data Sources:**

Datastream, CRSP, and COMPUSTAT from 1999 to 2010.

### **Alpha Highlight:**

[![Geographic Momentum](https://alphaarchitect.com/wp-content/uploads/2013/02/Geographic-Momentum.png)](https://alphaarchitect.com/wp-content/uploads/2013/02/Geographic-Momentum.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Strategy Summary:**

1. Compute each firm’s geographic return each month based on its sales.
   1. For example, if a firm has 50% sales in US, 30% in Canada, and 20% in India, its geographic return would be:
   2. GeoRet = 0.5\*(US\_Stock\_Return) + 0.3\*(Canada\_Stock\_Return) + 0.2\*(India\_Stock\_Return)
2. At the beginning of each month t, sort stocks in ascending order into 5 quintile portfolios based on lagged geographic returns.
3. *Buy firms in the top 20% of geographic return and short firms in the bottom 20% of geographic return.*
4. *Hold for one month and repeat above steps.*
5. *Make money.*

### **Commentary:**

* Quoc, currently a PhD student about to graduate, presented this paper in the [Drexel Finance Seminar Series](http://www.lebow.drexel.edu/) a few weeks ago–so this is relatively “Hot off the Press.”
* Anomaly holds after controlling for various firms’ characteristics and standard risk factors.
* Investors have limited time and cognition resources to process information from multiple foreign markets and hence delay incorporating those information into stock prices.
* Data intensive to incorporate geographic sales information.
* Results may be driven by micro-cap stocks, as the median firm in the sample has a market capitalization of $360 million.
