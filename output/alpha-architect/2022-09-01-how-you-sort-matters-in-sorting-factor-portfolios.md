---
title: "How You Sort Matters in Sorting Factor Portfolios"
slug: "how-you-sort-matters-in-sorting-factor-portfolios"
date: "2022-09-01"
modified: "2022-09-02"
url: "https://alphaarchitect.com/how-you-sort-matters-in-sorting-factor-portfolios/"
categories: ["Research Insights", "Factor Investing", "Larry Swedroe", "Academic Research Insight"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# How You Sort Matters in Sorting Factor Portfolios

> Non-standard errors capture uncertainty due to differences in research design choices. We establish substantial variation in the design choices made by researchers when constructing asset pricing factors. By purposely data mining over two thousand different versions of each factor, we find that Sharpe ratios exhibit substantial variation within a factor due to different construction choices, which results in sizable non-standard errors and allows for p-hacking. We provide simple suggestions that reduce the average non-standard error by 70%. Our study has important implications for model selection exercises.

In “[Your Complete Guide to Factor-Based Investing](https://www.amazon.com/Your-Complete-Guide-Factor-Based-Investing/dp/0692783652/ref=sr_1_1?crid=F4TCPQVHTRO4&keywords=your+complete+guide+to+factor+based+investing&qid=1656105447&sprefix=your+complet%2Caps%2C106&sr=8-1),” Andrew Berkin and I established criteria that must be met before considering investing in a factor-based strategy. We established the criteria to minimize the risks that any findings were the result of data-mining exercises. Data mining occurs when, instead of beginning with a hypothesis, researchers “torture the data until it confesses.” [Empirical research](https://academic.oup.com/rfs/article/29/1/5/1843824) has found that due to data dredging, many anomalies are likely false discoveries. For example, the authors of the 2020 study “[Replicating Anomalies](https://academic.oup.com/rfs/article-abstract/33/5/2019/5236964)” (read Wes’ Review [here](https://alphaarchitect.com/2017/10/replicating-anomalies/)) examined 452 anomalies and found that about two-thirds of them failed to replicate even if they did not adjust for [multiple testing](https://en.wikipedia.org/wiki/Multiple_comparisons_problem).

The data-mining problem occurs because there is no consensus on construction methods. Thus, the more freedom the researcher has increased the risk of data mining occurring, as they can select construction choices in order to meet statistical and performance-related hurdles. With that in mind, to determine which exhibits in what John Cochrane called a “zoo of the factors” were worthy of investment, Berkin and I used the following criteria. For a factor to be considered, it must meet all the following tests. To start, it must provide explanatory power to portfolio returns and have delivered a premium (higher returns). Additionally, the factor must be:

* Persistent — It holds across long periods of time and different economic regimes.
* Pervasive — It holds across countries, regions, sectors and even asset classes.
* Robust — It holds for various definitions (for example, there is a value premium whether it is measured by price-to-book, earnings, cash flow or sales).
* Investable — It holds up not just on paper but also after considering actual implementation issues, such as trading costs.
* Intuitive — There are logical risk-based or behavioral-based explanations for its premium and why it should continue to exist.

Our analysis of the research led Berkin and me to conclude that out of the [zoo containing hundreds of factors](https://alphaarchitect.com/2017/10/takeaways-from-a-non-phd-who-powered-through-a-144-page-factor-investing-paper/), only five equity factors met all the above criteria: market beta, size, value, momentum, and profitability/quality.

## **Mind Your Sorts**

Amar Soebhag, Bart Van Vliet, and Patrick Verwijmeren contribute to the literature with their June 2022 paper, “[Mind Your Sorts](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4136672&download=yes),” in which they examined 250 versions of each factor they considered in order to determine the extent to which the differential design choices in constructing factors matter. They noted:

> “Ambiguity regarding construction choices creates room for researchers to construct factors in a way that maximizes some statistical criteria, such as maximizing Sharpe ratios and t-statistics.”

They added:

> “A better understanding of the design choices that matter allows researchers to more effectively show the robustness of their findings in future work, while also helping readers in interpreting the presented results.”

Taking transaction costs into account, they considered eight construction choices that researchers face in their research design:

1. 70/30 or 80/20 breakpoints.
2. NYSE or NYSE-AMEX-Nasdaq (NAN) breakpoints.
3. Including or excluding microcaps.
4. Including or excluding financial firms.
5. Industry neutralization or not.
6. Value weighting or equal weighting.
7. Independent or dependent sorts.
8. Sorting on the most recent market capitalization or from June.

They then constructed 11 factors (see Table 3 below) using each possible combination of choices, leading to 256 (2^8) construction combinations. They also considered several factor models, including the Fama-French five-factor (market beta, size, value, profitability, and investment) and six-factor (adding momentum) models, and the [q-factor model](https://www.nber.org/papers/w26538) (market beta, size, investment and return on equity). Their data sample covered the 50-year period 1972-2021. Following is a summary of their findings:

* Sharpe ratios exhibited wide variation within a factor due to different construction choices—resulting in sizable [nonstandard errors](https://albertjmenkveld.com/blog/2021-11-30-non-standard-errors/) (defined as the standard deviation of the generated Sharpe ratios across the possible construction method) across all factors and allowing for [p-hacking](https://embassy.science/wiki/Theme:6b584d4e-2c9d-4e27-b370-5fbdb983ab46). In five out of 11 factors, the nonstandard error was greater than the standard error.

![](https://alphaarchitect.com/wp-content/uploads/2022/08/image-33-800x761.png)

![](https://alphaarchitect.com/wp-content/uploads/2022/08/image-37-800x546.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

* As an example of the wide variation within factors depending on construction choices and on how the HML (high-minus-low, or value) factor was constructed, Sharpe ratios varied between 0.18 and 1.24.
* The average ratio of the nonstandard error to the standard error across factors was 1.20—factor returns are not only a function of their sorting characteristics but also a function of their construction choices.
* Variation in construction choices affects factor exposure of a portfolio, the liquidity of a portfolio, and its risk diversification—portfolio construction methods matter. For example, equal weighting led to portfolios with higher illiquidity than value weighting and higher gross Sharpe ratios.
* Microcaps significantly increased the factor exposure and level of diversification of a factor portfolio while significantly increasing illiquidity.
* Especially high turnover factors such as momentum and PEAD (post-earnings announcement drift), which rebalance monthly, are expensive to trade, leading to a low (or negative) net return. Average transaction costs were higher for equal-weighted factors compared to value-weighted factors, resulting in lower Sharpe ratios (0.04 versus 0.19, respectively) on average.
* Introducing 30th-70th percentile breakpoints as opposed to 20th-80th percentile breakpoints significantly reduced factor exposure and illiquidity while increasing the level of diversification.
* Including firms from the financial industry had no significant impact on either factor exposure or the illiquidity level of a portfolio. Their inclusion mainly affected the breadth of the universe, increasing diversification.

Their findings led Soebhag, Van Vliet and Verwijmeren to conclude:

> “Factor design choices matter. Our results imply that multiple construction methods should be considered to reduce the potential for data mining. We find that particularly important choices are those concerning industry-adjusted characteristics, micro stocks, value-weighting, and NAN breakpoints. For future studies, we recommend considering these four choices in a ‘specification check’ in which the distribution of the results from the combinations of these methodological possibilities are reported in graphical form.”

They added:

> “Factors should not be compared against each other when their construction method differs, but should be compared using the same construction choices. In short, our main recommendation is that researchers mind their sorts.”

## **Investor Takeaway**

It is important that investors minimize the risks of making investment decisions that are based on the results of data-mining exercises. To help investors make more informed decisions, Andrew Berkin and I created the criteria that should be met before committing assets to a factor-based strategy. Soebhag, Van Vliet, and Verwijmeren demonstrated how important it is to perform due diligence that considers those criteria. Forewarned is forearmed.

## Important Disclosures

*For informational and educational purposes only and should not be construed as specific investment, accounting, legal, or tax advice.  Certain information is based on third party data which may become outdated or otherwise superseded without notice.  Third party information is deemed to be reliable, but its accuracy and completeness cannot be guaranteed.  By clicking on any of the links above, you acknowledge that they are solely for your convenience, and do not necessarily imply any affiliations, sponsorships, endorsements or representations whatsoever by us regarding third-party Web sites. We are not responsible for the content, availability or privacy policies of these sites, and shall not be responsible or liable for any information, opinions, advice, products or services available on or through them. The opinions expressed by featured authors are their own and may not accurately reflect those of Buckingham Strategic Wealth® and Buckingham Strategic Partners® , collectively Buckingham Wealth Partners. Neither the Securities and Exchange Commission (SEC) nor any other federal or state agency have approved, confirmed the accuracy, or determined the adequacy of this article. LSR-22-318*
