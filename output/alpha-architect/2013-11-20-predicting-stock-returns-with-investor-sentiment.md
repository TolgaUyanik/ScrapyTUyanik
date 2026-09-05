---
title: "Predicting Stock Returns with Investor Sentiment"
slug: "predicting-stock-returns-with-investor-sentiment"
date: "2013-11-20"
modified: "2022-06-01"
url: "https://alphaarchitect.com/predicting-stock-returns-with-investor-sentiment/"
categories: ["Research Insights", "Behavioral Finance"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Predicting Stock Returns with Investor Sentiment

> Market participants often claim that investor sentiment matters for stock returns. This premise was formally studied by Malcolm Baker and Jeffrey Wurgler in their landmark […]

Market participants often claim that investor sentiment matters for stock returns. This premise was formally studied by Malcolm Baker and Jeffrey Wurgler  in their landmark 2006 paper, “Investor Sentiment and the Cross-Section of Stock Returns.” Baker and Wurgler show evidence that supports the common notion investors have held for many years: sentiment matters.

Baker and Wurgler’s sentiment index has been used by many follow-on researchers looking to analyze how sentiment affects their specific research question. However, there hasn’t been much research associated with trying to build a more precise and accurate investment sentiment index.  
*Until now.*  
Dashan Huang, Fuwei Jiang, Jun Tu, and Guofu Zhou have a new paper (recently [published in the RFS](https://academic.oup.com/rfs/article/28/3/791/1576380/Investor-Sentiment-Aligned-A-Powerful-Predictor-of)) that introduce an econometric technique that enhances the predictability of sentiment. The table below shows how adding their enhanced sentiment indicator can improve the predictability associated with other variables thought to predict returns.

[![betterr2](https://alphaarchitect.com/wp-content/uploads/2013/11/betterr2.png)](https://alphaarchitect.com/wp-content/uploads/2013/11/betterr2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

And here is a nice figure highlighting the ability of the enhanced sentiment index to predict excess market returns:

[![new index is better than old one](https://alphaarchitect.com/wp-content/uploads/2013/11/new-index-is-better-than-old-one.png)](https://alphaarchitect.com/wp-content/uploads/2013/11/new-index-is-better-than-old-one.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

## **Strategy Summary:**

The paper begins by creating an aligned investor sentiment index via the partial least squares (PLS) method.

* Data are available from Baker and Wurgler (2006) and span from 1965 through 2010 (546 months).
* The sentiment index is a linear combination of six individual measures: Closed-end fund discount rate, share turnover, number of IPOs, first-day returns of IPOs, dividend premium and equity share in new issues.

Next, the paper forecasts aggregate stock market returns using this new index, both in-sample and out-of-sample. The authors compare their statistical results (β, R-square, t-stats) with the measures in the existing literature.

The findings are as follows:

* Sentiment index exhibits statistically and economically significant predictability. It is important not only cross-sectionally, but also at aggregate market level.
* The in-sample R-square is more than 5 times greater than that in Baker and Wurgler (2006), and out-of-sample R-square is more than 10 times greater.
* Adding sentiment index in conjunction with economic variables can substantially improve the forecasting performance.
* The sentiment index in this paper is more volatile, so it may better capture the short-term variation with future stock return.
* Table 7 examines how the sentiment index predicts different portfolios.
  + Stocks that are speculative, small, distressed (high book-to-market ratio) or high growth opportunity (low book-to-market), or past losers are more sensitive to investor sentiment.

**Feeling Sentimental Lately?**

---

## Investor Sentiment Aligned: A Powerful Predictor of Stock Returns

* Dashan Huang, Fuwei Jiang, Jun Tu, and Guofu Zhou
* A version of the paper can be found [here.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2311618)
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category!](https://alphaarchitect.com/category/academic-research/)

## **Abstract:**

> The widely used Baker and Wurgler (2006) sentiment index is likely to understate the predictive power of investor sentiment because their index is based on the ﬁrst principal component of six sentiment proxies that may have a common noise component. In this paper, we propose a new sentiment index that is aligned for explaining stock expected returns by eliminating the noise component. We ﬁnd that the aligned sentiment index has much greater power in predicting the aggregate stock market than the Baker and Wurgler (2006) index: it increases the R-squares by more than ﬁve times both in-sample and out-of-sample, and outperforms any of the well recognized macroeconomic variables. Its predictability is both statistically and economically signiﬁcant. Moreover, the new index improves substantially the forecasting power for the cross-section of stock returns formed on industry, size, value, and momentum. Economically, the driving force of the predictive power of investor sentiment appears stemming from market underreaction to cash ﬂow information

## **Data Sources:**

Baker Wurgler data: <http://people.stern.nyu.edu/jwurgler/>

New index data: <http://apps.olin.wustl.edu/faculty/zhou/SentimentIndices_Dec2014.xls>
