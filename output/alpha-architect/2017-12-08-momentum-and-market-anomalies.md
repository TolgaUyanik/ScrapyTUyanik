---
title: "Momentum and Market Anomalies"
slug: "momentum-and-market-anomalies"
date: "2017-12-08"
modified: "2022-05-13"
url: "https://alphaarchitect.com/momentum-and-market-anomalies/"
categories: ["Research Insights", "Momentum Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Momentum and Market Anomalies

> Momentum is the tendency for assets that have performed well (poorly) in the recent past to continue to perform well (poorly) in the future, at […]

Momentum is the tendency for assets that have performed well (poorly) in the recent past to continue to perform well (poorly) in the future, at least for a short period of time. Initial research on momentum was published by Narasimhan Jegadeesh and Sheridan Titman, authors of the 1993 study, “[Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency](https://www.jstor.org/stable/2328882?seq=1#page_scan_tab_contents).”

The type of momentum studied by Jegadeesh and Titman is called cross-sectional momentum (applied [example and explanation here](https://alphaarchitect.com/2015/12/01/quantitative-momentum-investing-philosophy/)). It is the type of momentum used in asset pricing models. Cross-sectional momentum measures relative performance, comparing the return of an asset relative to the returns of other assets within the same asset class. Thus, in a given asset class, a cross-sectional momentum strategy might buy the 30 percent of assets with the best relative performance and short sell the 30 percent of assets with the worst relative performance. Even if all the assets had risen in value, a cross-sectional momentum strategy would still short the assets with the lowest returns.

The other type of momentum is called time-series momentum ([covered recently here](https://alphaarchitect.com/2017/08/10/diversification-benefits-time-series-momentum/)). Time-series momentum is also referred to as [trend-following](https://alphaarchitect.com/2015/08/13/avoiding-the-big-drawdown-with-trend-following-investment-strategies/) because it measures the trend of an asset with respect to its own performance. Thus, unlike cross-sectional momentum, time-series momentum is defined by absolute performance. It buys assets that have been rising in value and short sells assets that have been falling in value. In contrast to cross-sectional momentum, if all assets rise in value, then none of them would be shorted.

The research on both types of momentum has shown that their premia have been persistent across long periods of time, pervasive across geography and asset classes (stocks, bonds, commodities, and currencies), robust to various definitions (formation periods) and implementable (as it survives transaction costs).

## Can Momentum Be Used to Time Anomalies? (i.e., “Factor Timing”)

Doron Avramov, Si Cheng, Amnon Schreiber and Koby Shemer contribute to the literature on cross-sectional momentum with their study “[Scaling Up Market Anomalies](http://www.iijournals.com/doi/abs/10.3905/joi.2017.26.3.089),” which appears in the Fall 2017 issue of the Journal of Investing. (Working paper version [available here](http://pluto.huji.ac.il/~davramov/MOM_ANOMALIES.pdf).) Given that the traditional momentum strategy exploits the persistence in stock prices, they examined whether the same persistence exists in 15 well-documented anomalies: failure probability, O-Score, net stock issuance, composite equity issuance, total accruals, net operating assets, momentum, gross profitability, asset growth, return on assets, abnormal capital investment, standardized unexpected earnings, analyst dispersion, idiosyncratic volatility and book-to-market ratio. The three-factor alpha estimates for the 15 strategies are highlighted in the table below:

[![](https://alphaarchitect.com/wp-content/uploads/2017/11/anomaly-portfolios.png)](https://alphaarchitect.com/wp-content/uploads/2017/11/anomaly-portfolios.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The stocks in each anomaly are sorted into deciles, based on their cross-sectional momentum. Based on the returns of the prior month, the strategy the authors examined goes long the stocks in the top decile for each anomaly (the best performers) and short the stocks in the bottom decile (the worst performers), creating 30 portfolios. They then compared the returns of this strategy to a naïve (1/N) strategy that invests equally in all 15 anomalies. As tests of robustness, they also examined portfolios based on the top (bottom) three and four deciles. Their data sample covers U.S. stocks over the period from 1976 through 2013. They also split the sample into pre-, and a post-2000 period, to see if returns diminish over time.

The following is a summary of their findings:

* The momentum strategy considerably outperforms the naive benchmark of equal-weighted investments in each anomaly.
* Thirteen of the 15 long-short strategies produce significantly positive Fama-French three-factor risk-adjusted returns over the entire sample period. Only one produced a negative alpha (-0.04 percent per month), and it was not statistically significant. The average Fama-French three-factor adjusted return for the combined strategy is a highly significant 0.80 percent per month (t-stat of 10.5).
* The strategy conditioned on past one-month return yields a monthly alpha ranging between 1.27 percent and 1.47 percent, indicating a significant 59 percent to 84 percent increase compared with the naive strategy.

The table below highlights the results:

[![](https://alphaarchitect.com/wp-content/uploads/2017/11/momentum-factor-anomaly.png)](https://alphaarchitect.com/wp-content/uploads/2017/11/momentum-factor-anomaly.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

* The proposed momentum-trading strategy remains profitable during the post-2000 period, generating a monthly alpha ranging between 0.77 percent and 0.91 percent.
* There is a strong cross-sectional variation in the Value at Risk (the maximum potential loss in the value of the portfolio over one month with a 5 percent probability) of the 15 strategies ranging from 3.7 percent to 13 percent, suggesting that betting on a single anomaly-based trading strategy could result in significant loss with non-trivial probability. However, due to low correlation of returns of the anomalies, the combined strategy considerably mitigates the Value at Risk to just 2.83.
* Among the 15 anomaly-based trading strategies, 10 (12) strategies produce a significant risk-adjusted return in the long leg (short leg). The results indicate that the short leg of the combined strategy yields a significant risk-adjusted return of -0.50 percent per month, with the long position also generating a significant monthly risk-adjusted return of 0.30 percent per month. This finding is consistent with prior research that has found that the short positions are more profitable than the long positions, likely due to short-sale constraints.
* Nine of the 15 anomalies produce significantly positive Fama-French three-factor adjusted returns in the post-2000 period, compared with 13 profitable anomalies prior to 2000. However, the combined strategy remains highly profitable, generating a significant monthly alpha of 0.81 percent in the pre-2000 period and 0.62 percent in the post-2000 period.
* As momentum has been shown to perform best in periods of high investor sentiment, the authors also examined the momentum in anomalies conditional on high-versus-low investor sentiment and found that the monthly risk-adjusted return ranges between 1.42 percent and 1.73 percent in high-sentiment periods, compared with 1.09 percent to 1.18 percent in periods when investor sentiment is low.

## **Conclusion**

Avramov, Cheng, Schreiber, and Shemer noted:

> The combined strategy displays significantly positive risk-adjusted return also in the post-2000 period even when almost half of the individual anomaly payoffs are insignificant. Moreover, it is evident that the combined strategy mitigates the noise and risk in the individual strategies, and considerably limits the downside risk measured by Value at Risk in both sub-periods.

Their results provide evidence of the pervasiveness and persistence of the cross-sectional momentum premium.
