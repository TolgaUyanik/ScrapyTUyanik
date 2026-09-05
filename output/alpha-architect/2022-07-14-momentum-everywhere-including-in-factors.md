---
title: "Momentum Everywhere, Including in Factors"
slug: "momentum-everywhere-including-in-factors"
date: "2022-07-14"
modified: "2022-07-11"
url: "https://alphaarchitect.com/momentum-everywhere-including-in-factors/"
categories: ["Research Insights", "Factor Investing", "Larry Swedroe", "Trend Following", "Academic Research Insight", "Value Investing Research", "Momentum Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Momentum Everywhere, Including in Factors

> Managed portfolios that exploit positive first-order autocorrelation in monthly excess returns of equity factor portfolios produce large alphas and gains in Sharpe ratios. We document this finding for factor portfolios formed on the broad market, size, value, momentum, investment, prof- itability, and volatility. The value-added induced by factor management via short-term momentum is a robust empirical phenomenon that survives transaction costs and carries over to multi-factor portfolios. The novel strategy established in this work compares favorably to well-known timing strategies that employ e.g. factor volatility or factor valuation. For the majority of factors, our strategies appear successful especially in recessions and times of crisis.

Empirical research, including the 2017 paper “[A Century of Evidence on Trend-Following Investing](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2993026),” has found [momentum](https://alphaarchitect.com/2015/12/quantitative-momentum-investing-philosophy/) to be a persistent and pervasive factor in returns of not only stocks but other asset classes as well, including bonds, commodities, and currencies. Recent empirical research on the momentum factor, including the 2018 studies “[Factor Momentum Everywhere](https://www.aqr.com/Insights/Research/Working-Paper/Factor-Momentum-Everywhere)” ([Summary](https://alphaarchitect.com/2019/06/is-factor-momentum-really-everywhere/)) and “[Is there Momentum in Factor Premia? Evidence from International Equity Markets](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3332927),” and the 2019 studies “ [Factor Momentum and the Momentum Factor](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3014521)” and “[Factor Momentum](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3116974),” has examined whether momentum can be found in factors as well and has found:

* Times-series ([trend](https://alphaarchitect.com/2015/08/avoiding-the-big-drawdown-with-trend-following-investment-strategies/)) factor momentum is a pervasive property of factors—a strategy that buys the recent top-performing factors and sells poor-performing factors to achieve significant investment performance above and beyond traditional stock momentum.
* Factor momentum explains all forms of individual stock momentum—stock momentum strategies indirectly time factors: they profit when the factors remain autocorrelated and crash when these autocorrelations break down.
* Demonstrating pervasiveness, factor momentum is a global phenomenon.
* Factor momentum can be captured by trading almost any set of factors.
* Industry momentum stems from factor momentum.

These findings support the conclusion that momentum among equity factors is a pervasive phenomenon in financial markets.

Volker Flögel, Christian Schlag, and Claudia Zunft contribute to the momentum literature with their study “[Momentum-Managed Equity Factors](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3423287),” published in the [April 2022 issue of the Journal of Banking and Finance](https://www.sciencedirect.com/science/article/abs/pii/S0378426621002107). They began by noting:

> “The premiums associated with asset pricing anomalies like size, book-to-market equity, and momentum are sizable, persist across decades, and exist in various markets. However, the remarkable performance of the associated factor portfolios goes along with sudden crashes and long periods of downturns. Examples are the enormous outperformance of large caps in the 1980’s the 1990’s and the momentum crash in 2009. Against the background that the distribution of excess returns of equity factors is strongly time-varying, it appears worthwhile to perform what is called ‘factor timing’, i.e. to hold more of a factor portfolio when its excess return is expected to be high and, vice versa, to scale the factor exposure down when the expected excess return is low.”

Motivated by empirical research findings, they developed a timing strategy for factor portfolios in equity markets—the higher the last-month excess return of the plain factor relative to past levels, the more the strategy invests in the plain factor and vice versa.

Flögel, Schlag, and Zunft calculated the excess return of the market (MKT) as well as excess returns of factors formed on size (SMB), book-to-market equity ([**HML**](https://alphaarchitect.com/2014/10/the-quantitative-value-investing-philosophy/)), momentum ([**WML**](https://alphaarchitect.com/2015/12/quantitative-momentum-investing-philosophy/)), investment (CMA), operating profitability (RMW) and volatility (SMV). For each of these factors and at each month’s end, they computed a timing signal that contained information on the expected next-month excess return of the given plain factor.

The authors explained:

> “In particular, we calculate the [z-score](https://www.investopedia.com/terms/z/zscore.asp) of the last-month excess return of the plain factor, where standardization is performed with respect to an expanding window of past monthly excess returns of this factor. Then, we compute the associated value of the standard normal cumulative distribution function, so that the resulting timing signal approaches one when the last-month excess return of the plain factor is very high relative to past levels and is close to zero when it is relatively low. Making use of the timing signal, a managed factor then systematically scales the excess returns of the respective plain factor up or down over time.”

Their data sample covered the period July 31, 1963-November 28, 2014. Portfolios were rebalanced monthly. Following is a summary of their key findings:

* Managed portfolios that exploit positive autocorrelation in monthly excess returns of equity factor portfolios produced large alphas and gains in Sharpe ratios—the annualized Sharpe ratios increased from 0.40 to 0.55 for the market factor, from 0.32 to 0.61 for size, from 0.43 to 0.60 for book-to-market equity, from 0.16 to 0.46 for operating profitability and from 0.12 to 0.33 for volatility. The increases were significant at the 1% level in three out of five cases, and at the 5% level in the other two. They did find that the evidence on timing-induced performance improvements for momentum-managed momentum and investment was weak in the U.S., though it was significant in international markets.
* Factor momentum was the only timing variable with predictive power for HML.
* Timing strategies tended to perform well when (holding all other variables fixed) the return on volatile stocks was higher than the one on stable stocks.
* The value-added induced by factor management via short-term momentum is a robust empirical phenomenon that survives transaction costs and carries over to multifactor portfolios—while managing factors based on last month’s momentum increased turnover, the increase in turnover induced by timing did not outweigh the benefits of timing. In addition, turnover could be reduced using a smoothed version of the timing signal, and timing still yielded significant benefits.
* On average, the exposure of managed to plain factors was around or even less than 1, and exposures were not skewed with means similar to medians. The maximum exposure ranged from 1.53 for CMA to 2.03 for MKT—evidence that the performance of managed factors is not due to excessive leverage.
* For the majority of factors, momentum strategies have been successful when utility is highest—in recessions and times of crisis.
* The performance enhancements induced by momentum-based factor management withstood a battery of robustness checks including subperiods, various definitions of factors (such as P/E or P/CF instead of book-to-market), European markets, during recessions, reduced leverage, and out-of-sample tests for the factors with longer histories (beta, size, value, and momentum). In addition, they were not spanned by well-known timing strategies that employ factor volatility, factor valuation, or [sentiment](https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.2006.00885.x).
* There was little evidence in favor of a risk-based explanation for the performance of the timing strategies.

![](https://alphaarchitect.com/wp-content/uploads/2022/07/image-5-1200x1017.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

Flögel, Schlag and Zunft’s findings led them to conclude:

> “We identify a new timing strategy which exploits the predictive power of the excess returns of equity factors over the previous month. The positive mean alphas and increases in Sharpe ratios induced by momentum-based timing are substantial and pervasive across factors, survive transaction costs, exist in multi-factor portfolios, and withstand plenty of robustness checks. Momentum-managed factors are not spanned by timing strategies already known from the literature. We also find that our strategies outperform alternative specifications of time series factor momentum strategies.”

## **Investor Takeaways**

There is strong empirical evidence demonstrating that factor momentum provides information on the cross-section of returns and has generated alpha relative to existing asset pricing models. It is for that reason that firms like [Alpha Architect](https://alphaarchitect.com/) and [AQR Capital Management](https://www.aqr.com/), leaders in factor investing strategies, incorporate factor momentum into some of their strategies. Individual investors can utilize this information without incurring additional costs by incorporating factor momentum into trading decisions. For example, when rebalancing, they can delay purchases of assets with negative factor momentum and delay sales of assets with positive factor momentum.

## Important Disclosures

*For informational and educational purposes only and should not be construed as specific investment, accounting, legal, or tax advice. Certain information is based upon third party data which may become outdated or otherwise superseded without notice.  Third party information is deemed to be reliable, but its accuracy and completeness cannot be guaranteed.  By clicking on any of the links above, you acknowledge that they are solely for your convenience, and do not necessarily imply any affiliations, sponsorships, endorsements or representations whatsoever by us regarding third-party websites. We are not responsible for the content, availability or privacy policies of these sites, and shall not be responsible or liable for any information, opinions, advice, products or services available on or through them. The opinions expressed by featured authors are their own and may not accurately reflect those of Buckingham Strategic Wealth® or Buckingham Strategic Partners®, collectively Buckingham Wealth Partners. Neither the Securities and Exchange Commission (SEC) nor any other federal or state agency have approved, determined the accuracy, or confirmed the adequacy of this article. LSR-22-309*
