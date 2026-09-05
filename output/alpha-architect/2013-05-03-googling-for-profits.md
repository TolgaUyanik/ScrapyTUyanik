---
title: "Googling for Profits?"
slug: "googling-for-profits"
date: "2013-05-03"
modified: "2022-06-02"
url: "https://alphaarchitect.com/googling-for-profits/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Googling for Profits?

> Quantifying Trading Behavior in Financial Markets Using Google Trends Tobias Preis, Helen Susannah Moat, and H. Eugene Stanley A version of the paper can be […]

### Quantifying Trading Behavior in Financial Markets Using Google Trends

* Tobias Preis, Helen Susannah Moat, and H. Eugene Stanley
* A version of the paper can be found [here.](http://www.nature.com/srep/2013/130425/srep01684/full/srep01684.html)
* Want a summary of academic papers with alpha? Check out our free [Academic Alpha Database](https://alphaarchitect.com/category/architect-academic-insights/)!

### **Abstract:**

> Crises in financial markets affect humans worldwide. Detailed market data on trading decisions reflect some of the complex human behavior that has led to these crises. We suggest that massive new data sources resulting from human interaction with the Internet may offer a new perspective on the behavior of market participants in periods of large market movements. **By analyzing changes in Google query volumes for search terms related to finance, we find patterns that may be interpreted as ‘‘early warning signs’’ of stock market moves**. Our results illustrate the potential that combining extensive behavioral data sets offers for a better understanding of collective human behavior.

### **Data Sources:**

Google SVI and Dow Jones Returns.

### **Alpha Highlight:**

I simply can’t get my head around the fact that search terms for “color”, “restaurant”, “religion”, “cancer”, and so forth, can have such great outcomes. This smells like a classic case of data-mining on steroids. That said, a very fascinating study and who’s to say it might not work?

![goog](https://alphaarchitect.com/wp-content/uploads/2013/05/goog.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Strategy Summary:**

* Analyze the *Google Trends* data each week (ending Sunday night) for the key search term “debt” by U.S. users.Other search terms such as “stocks, portfolio, inflation, housing, dow jones” yield similar (but lower) returns.
  + If the current week’s “debt” search N is higher than the average over the past 3 weeks (weeks *t-1, t-2, t-3*), sell DJIA at close of first trading day and hold this short position until the close of the first trading day the next week.
  + If the current week’s “debt” search N is lower than the average over the past 3 weeks (weeks *t-1, t-2, t-3*), buy DJIA at close of first trading day and hold this long position until the close of the first trading day the next week.
  + This strategy yields a return of 326% from 1/5/2004 until 2/22/2011, whereas the buy-and-hold return for the DJIA over this period was 16%, and a simple momentum strategy in the paper yields 33%.
* Allowing the seach base to include non-U.S. users decreases the returns.
* Returns are split among the long and short portfolios, so the returns are not entirely driven by the short portfolio.

### **Commentary:**

* Other non-financially related search terms such as “color, religion, cancer” also yield higher returns than the simple buy-and-hold portfolio as well as the simple momentum strategy in the paper.
  + Outperformance of search terms such as these question the impact of the study.
* “Debt” having the highest return during the recent financial crisis makes sense, although this may not have worked as well in the past and in future crises.
  + For example, “Internet stocks” may have worked the best in the lates 1990s and early 2000s.
* Finance research on this subject is more robust:
  + <https://alphaarchitect.com/2012/12/news-and-google-hits-a-path-to-20-alpha/>
  + [In Search of Attention](https://www3.nd.edu/~pgao/papers/Google_JF2011.pdf)

> We propose a new and direct measure of investor attention using search frequency in Google (Search Volume Index (SVI)). In a sample of Russell 3000 stocks from 2004 to 2008, we ﬁnd that SVI (1) is correlated with but different from existing proxies of investor attention; (2) captures investor attention in a more timely fashion and (3) likely measures the attention of retail investors. An increase in SVI predicts higher stock prices in the next 2 weeks and an eventual price reversal within the year. It also contributes to the large ﬁrst-day return and long-run under performance of IPO stocks.
