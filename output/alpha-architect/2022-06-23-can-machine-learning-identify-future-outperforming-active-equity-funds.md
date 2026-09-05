---
title: "Can Machine Learning Identify Future Outperforming Active Equity Funds?"
slug: "can-machine-learning-identify-future-outperforming-active-equity-funds"
date: "2022-06-23"
modified: "2022-06-21"
url: "https://alphaarchitect.com/can-machine-learning-identify-future-outperforming-active-equity-funds/"
categories: ["Research Insights", "Factor Investing", "Larry Swedroe", "Trend Following", "Academic Research Insight", "AI and Machine Learning", "Value Investing Research", "Momentum Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Can Machine Learning Identify Future Outperforming Active Equity Funds?

> We show, using machine learning, that fund characteristics can consistently differentiate high from low-performing mutual funds, as well as identify funds with net-of-fees abnormal returns. Fund momentum and fund flow are the most important predictors of future risk-adjusted fund performance, while characteristics of the stocks that funds hold are not predictive. Returns of predictive long-short portfolios are higher following a period of high sentiment or a good state of the macro-economy. Our estimation with neural networks enables us to uncover novel and substantial interaction effects between sentiment and both fund flow and fund momentum.

Ron Kaniel, Zihan Lin, Markus Pelger, and Stijn Van Nieuwerburgh contribute to the asset pricing literature with their January 2022 study “[Machine-Learning the Skill of Mutual Fund Managers](https://papers.ssrn.com/sol3/Papers.cfm?abstract_id=3977883)” in which they used machine learning in the form of an artificial neural network to examine the universe of actively traded U.S. equity mutual funds between 1980 and 2019 and the stocks they hold in order to determine which, if any, characteristics can help identify future outperformers. They benchmarked performance against the Carhart four-factor model (beta, size, [value](https://alphaarchitect.com/2014/10/the-quantitative-value-investing-philosophy/), and [momentum](https://alphaarchitect.com/2015/12/quantitative-momentum-investing-philosophy/)) as well as an eight-factor model that added investment, profitability, short-term reversal, and long-term reversal. They also examined 46 stock characteristics weighted by the funds’ holdings and 13 fund and fund family characteristics. The fund characteristics included fund return momentum and fund flow. In addition, they included a variable that summarized the overall state of the market proxied either by [investor sentiment](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=464843) or by a comprehensive measure of macroeconomic activity ([Chicago Fed National Activity Index](https://www.chicagofed.org/publications/cfnai/index)). Following is a summary of their findings:

* Machine learning was able to identify fund characteristics that differentiated *relatively* high-performing from *relatively* low-performing mutual funds.
* The model predictions generated a large difference in performance out of sample, with most of the benefit coming from avoiding the underperformers. Buying the 10% of mutual funds with the best predicted performance each month and using the model not only to select but also to weight the funds within the top decile generated a cumulative abnormal return of 72% over the sample period. Buying the 10% of mutual funds with the worst predicted performance each month produced a cumulative abnormal return of ‑119%. The 191% difference in out-of-sample performance based on the model’s predictions was economically large and statistically significant.
* The results were robust to alternative holding period assumptions—the predictability of economically significant relative performance lasted for three years.
* About 10 to 20% of funds generated positive abnormal returns even after fees.
* Most of the benefits accrued from avoiding the worst-performing funds—the effect came mostly from the short leg.
* The best and the worst funds had similar fees.
* Fund momentum and fund flow are the most important predictors of future risk-adjusted fund performance. In addition, these two fund characteristics matter much more when investor sentiment is high—high sentiment periods coincided with more fund return predictability.
* Characteristics of the stocks that funds hold are not predictive—little can be learned about fund abnormal returns from the factor exposure of the stocks they hold.
* The level of fund (and stock) returns is extremely hard to predict.

![](https://alphaarchitect.com/wp-content/uploads/2022/06/image-33-800x452.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

![](https://alphaarchitect.com/wp-content/uploads/2022/06/image-34-800x350.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

Their findings led the authors to conclude:

> “The salience of flow and fund return momentum as the key predictors suggests that some investors can detect skill and (re)allocate their investment towards such skilled managers. This reallocation of investment flows is not as strong as the frictionless model [Berk and Green](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=383061) (2004) predicts. Skill leaves a trail in the form of fund return momentum for investors to exploit in the next period. Put differently, the flows are gradual and small enough that it takes several periods until the fund runs into zero marginal abnormal returns.”

However, they added:

> “The results are potentially also consistent with funds and fund families attracting flows through marketing rather than—or in addition to—through investment skill. … Marketing-induced inflows create buying pressure for stocks that the fund typically invests in. In a world with [downward-sloping demand curves](https://www.nber.org/papers/w21749), this raises prices and lifts fund returns. Through the flow-performance relationship, as well as through persistence in marketing-driven flows, the out-performance creates more inflows in the next period. The demand pressure increases prices further, generating momentum in fund returns. The fact that flows and fund momentum have a much stronger association with fund performance in high-sentiment periods lends further credence to this marketing-driven channel.”

## **Investor Takeaways**

The finding that [momentum](https://alphaarchitect.com/2015/12/quantitative-momentum-investing-philosophy/) in fund returns can help investors in actively managed funds identify relative winners and losers among fund managers should not be a total surprise, as momentum has been found to exist in [virtually all markets](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2993026) (stock, bonds, commodities, and currencies) and even in [factors](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3116974) (more [here](https://alphaarchitect.com/2021/05/the-explanatory-power-of-factor-momentum/)). Even investors using passive/systematic strategies (such as index funds) can utilize this information in how and when they trade. For example, they could consider delaying trading (such as rebalancing or adding new cash flows) to take advantage of the information from fund momentum and fund flows.

Finally, a word of caution on applying the findings of machine learning (see an application to factor investing [here](https://alphaarchitect.com/2022/02/machine-learning-the-recovery-of-missing-firm-characteristics/)). A major benefit of artificial intelligence tools (such as machine learning) is that they have a great capacity to deal with massive amounts of data. But that also creates the risk that findings can be the result of “torturing the data until it confesses”—correlation doesn’t necessarily mean causation. Thus, it is critical that any findings should be supported by either risk- or behavioral-based explanations, and those findings should be persistent across economic regimes, pervasive across asset classes and regions, and survive transaction costs. In this case, the finding regarding momentum’s explanatory power is consistent with the literature (as demonstrated in [Your Complete Guide to Factor-Based Investing](https://www.amazon.com/Your-Complete-Guide-Factor-Based-Investing/dp/0692783652)), and the finding on cash flow’s predictive power is also consistent with the finding on momentum. That consistency provides more confidence that the findings are not the result of data mining.

### Important Disclosures:

*For informational and educational purposes only and should not be construed as specific investment, accounting, legal, or tax advice.  Certain information is based upon third party data which may become outdated or otherwise superseded without notice.  Third party information is deemed to be reliable, however its accuracy and completeness cannot be guaranteed. By clicking on any of the links above, you acknowledge that they are solely for your convenience, and do not necessarily imply any affiliations, sponsorships, endorsements or representations whatsoever by us regarding third-party websites. We are not responsible for the content, availability or privacy policies of these sites, and shall not be responsible or liable for any information, opinions, advice, products or services available on or through them. The opinions expressed by featured authors are their own and may not accurately reflect those of the Buckingham Strategic Wealth® or Buckingham Strategic Partners®, collectively Buckingham Wealth Partners. Neither the Securities and Exchange Commission (SEC) nor any other federal or state agency have approved, determined the accuracy, or confirmed the accuracy of this article. LSR-21-239*
