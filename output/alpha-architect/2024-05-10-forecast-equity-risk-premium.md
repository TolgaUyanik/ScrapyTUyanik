---
title: "Using Machine Learning Programs to Forecast the Equity Risk Premium"
slug: "forecast-equity-risk-premium"
date: "2024-05-10"
modified: "2024-05-10"
url: "https://alphaarchitect.com/forecast-equity-risk-premium/"
categories: ["Research Insights", "Factor Investing", "Larry Swedroe", "Guest Posts", "AI and Machine Learning", "Other Insights", "Macroeconomics Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Using Machine Learning Programs to Forecast the Equity Risk Premium

> To date, the best metric we have for forecasting future equity returns and the ERP is current valuations. An interesting question is whether more complicated methods using newly developed machine learning models can provide superior forecasts.

The ability to predict stock returns and the equity risk premium (ERP) is of great interest to academics, financial practitioners, and investors, as future estimated returns have implications for asset allocations. To date, the best metric we have for forecasting future equity returns and the ERP is current valuations (whether using current P/E ratios or some cyclically-adjusted average such as Robert Shiller’s popular [P/E 10](https://www.multpl.com/shiller-pe) ratio).

[Vanguard](https://fairwaywealth.com/wp-content/uploads/Vanguard-Research-11-30-2014.pdf)’s research confirmed the findings of previous studies that valuation metrics (such as P/Es) have had an inverse, or mean-reverting, relationship with future stock market returns – although it has only been meaningful at long horizons, explaining about 40% of the time variation in net-of-inflation (real) returns. Their results were similar to whether trailing earnings were smoothed or cyclically adjusted. Forty percent is a high figure for an asset as volatile as equities.

An interesting question is whether more complicated methods using newly developed machine learning models can provide superior forecasts. While current valuations assume a linear relationship, the benefit of machine learning approaches is that they can capture complex relationships between the target variable and predictors without imposing prior model assumptions. They can also deal with a large number of potential predictors, with an emphasis on dimension reduction techniques.

Xingfu Xu and Wei-Han Liu contribute to the literature with their 2023 study “[Forecasting the Equity Premium: Can Machine Learning Beat the Historical Average?](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4781195).” They selected seven machine learning methods used by Shihao Gu, Bryan Kelly, and Dacheng Xiu in their 2019 study “[Empirical Asset Pricing via Machine Learning](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3159577)”: [partial least squares](https://en.wikipedia.org/wiki/Partial_least_squares_regression) (PLS), [principal components regression](https://en.wikipedia.org/wiki/Principal_component_regression) (PCR), [least absolute shrinkage and selection operator](https://en.wikipedia.org/wiki/Lasso_(statistics)) (LASSO), [elastic net](https://en.wikipedia.org/wiki/Elastic_net_regularization) (ENet), [gradient boosted regression trees](https://en.wikipedia.org/wiki/Gradient_boosting#Gradient_tree_boosting) (GBRT), [random forest](https://en.wikipedia.org/wiki/Random_forest) (RF), and [neural networks with three layers](https://www.sciencedirect.com/topics/engineering/three-layered-neural-network) (NN3), as well as four others—[support vector regression](https://towardsdatascience.com/an-introduction-to-support-vector-regression-svr-a3ebc1672c2), [k-nearest neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm), [adaptive boosted trees](https://www.mygreatlearning.com/blog/adaboost-algorithm/), and [extreme gradient boosted trees](https://towardsdatascience.com/xgboost-extreme-gradient-boosting-how-to-improve-on-regular-gradient-boosting-5c6acf66c70a))—and their combination method. They chose these last four because existing studies demonstrate their strong predictive power in other financial predictions.

For prediction performance comparison, they provided both in-sample and out-of-sample analyses of the employed machine learning methods with that of the historical average benchmark. They followed common machine learning practice, splitting the data into training, validation, and testing sets. The training and validation sets were fixed at 85% and 15% of the in-sample data, respectively. Their data covered the period December 1926-December 2020. Using 12 macroeconomic variables (including dividend yields, volatility, earnings/price, book-to-market, net new issuance, the rates on Treasury bills and long-term Treasury bonds, the default spreads between corporate bonds of high versus lower quality and between corporates and Treasurys, and inflation) and 12 technical predictors (based on trend-following strategies such as moving averages and momentum), they found:

Most machine learning methods, especially two tree-based models (random forest and extreme gradient boosted trees), can achieve a very high in-sample fit (an R-squared of more than 80% in monthly samples).

![](https://alphaarchitect.com/wp-content/uploads/2024/05/Table-1-600x501.png)

However, when it comes to the out-of-sample forecasts of different evaluation periods, the competing forecasting models generally failed to outperform the historical average benchmark.

![](https://alphaarchitect.com/wp-content/uploads/2024/05/Table-3-600x487.png)

Notes: This table reports the out-of-sample prediction results for machine learning methods employed in the study of Gu, Kelly, and Xiu (2020). ‘HA’ denotes the historical average benchmark. The statistics in parentheses corresponding to out-of-sample R-squares and success ratio are their respective test statistics based on Clark and West (2007) and Pesaran and Timmermann (1992). ‘-’ means that the statistics are not available. \*\*\*, \*\*, and \* denote significance at 1%, 5%, and 10% levels, respectively. [The success ratio measures directional correctness.]

* The results were robust to the choice of window estimation schemes, data frequencies, and alternative macroeconomic datasets.
* The historical mean was confirmed as the best forecast in terms of out-of-sample R-squared.
* The historical average had higher success ratios than the models.

Xu and Liu attributed

> “the underperformance of machine learning in equity premium prediction to the insufficiently large datasets, the low sign-to-noise ratio, and the evolving markets. We notice that [machine learning methods](https://alphaarchitect.com/2018/12/machine-learning-classification-methods-and-factor-investing/) fail to improve forecast accuracy, especially in out-of-sample situations. … The changing characteristics of markets modify the relation between predictors and the equity premium and exhibit significant noise along the evolution process. A robust predictable pattern in equity premium predictions usually fails to survive for a long while.”

They explained:

> “Although our monthly datasets for the equity prediction problem cover a long period of more than 90 years, our datasets are still small in scale from the perspective of machine learning requirements. Essentially, machine learning is designed for large-scale and highly complex multi-dimensional datasets, but our dataset comparatively fails to meet those requirements for equity premium predictions.”

The finding that the more sophisticated models were not able to outperform the simple historical benchmark is consistent with the findings of Amit Goyal and Ivo Welsh, authors of the study “[A Comprehensive Look at the Empirical Performance of Equity Premium Prediction.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=517667)”

Their findings led Xu and Liu to conclude:

> “Essentially, machine learning methods can be handicapped by their in-sample overfitting. This study advises us not to be over-optimistic about the usage of machine learning in forecasting the equity premium. The excellent in-sample performance of machine learning can backfire in the context of real-world out-of-sample return predictions due to overfitting.” They ended with this hopeful note: “We expect there is ample room to improve existing machine learning algorithms to enhance their out-of-sample forecasting ability.”

## **Investor Takeaway**

Xu and Liu demonstrated that more sophisticated models do not necessarily produce superior results. In fact, they are prone to “[overfitting](https://en.wikipedia.org/wiki/Overfitting)” the data. While advanced machine learning models could not outperform the historical return benchmark, we know that valuations matter to future returns. Thus, investors are best served by not using the historical mean return when estimating future returns. Instead, they should use current valuation metrics such as the CAPE 10. With that said, investors must be sure to treat any estimate in a probabilistic (not deterministic) manner. The following table from the 2017 paper “[The Many Colours of CAPE](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3258404),” by Robert Shiller and Farouk Jivraj, shows that while the CAPE 10 provided valuable information as to future returns, there was still a wide dispersion of potential outcomes.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Q1 1926 – Q2 2017** | | | | | |
| **Starting CAPE Ratio** | | | **Real 10-year S&P 500 Annualized Returns (%)** | | |
| **Average** | **Low** | **High** | **Average** | **Worst** | **Best** |
| 8.6 | 5.6 | 9.6 | 9.8 | 4.2 | 17.2 |
| 10.3 | 9.6 | 11.0 | 10.6 | 3.8 | 16.9 |
| 11.5 | 11.0 | 12.1 | 10.0 | 2.6 | 14.7 |
| 13.0 | 12.1 | 13.9 | 8.7 | 0.7 | 14.1 |
| 15.0 | 13.9 | 16.1 | 7.8 | -1.6 | 15.0 |
| 17.0 | 16.1 | 17.8 | 5.4 | -3.8 | 14.6 |
| 18.7 | 17.8 | 19.9 | 5.0 | -4.0 | 13.5 |
| 21.0 | 19.9 | 22.0 | 2.7 | -3.3 | 8.6 |
| 24.1 | 22.0 | 26.4 | 2.5 | -4.0 | 7.3 |
| 33.2 | 26.4 | 44.2 | 0.9 | -6.1 | 5.8 |

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*

The takeaway is that investment plans should address the potential for those other possible outcomes to occur. Do you have a “Plan B”? If not, let this serve as a wake-up call.

*Larry Swedroe is the author or co-author of 18 books on investing, including his latest Enrich Your Future.*

*The opinions expressed here may not reflect those of Buckingham Wealth Partners. For informational and educational purposes only and should not be construed as specific investment accounting, legal, or tax advice. Certain information is based on third party data and may become outdated or otherwise superseded without notice.  Indices are not available for direct investment. Their performance does not reflect the expenses associated with the management of an actual portfolio nor do indices represent results of actual trading. Information from sources deemed reliable, but its accuracy cannot be guaranteed. Performance is historical and does not guarantee future results. All investments involve risk, including loss of principal. Neither the Securities and Exchange Commission (SEC) nor any other federal or state agency have approved, determined the accuracy, or confirmed the adequacy of this article. LSR-24-649*
