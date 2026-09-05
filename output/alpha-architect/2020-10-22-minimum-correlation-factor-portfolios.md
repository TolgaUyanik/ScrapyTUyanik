---
title: "Building Factor Portfolios Based with the Lowest Correlations"
slug: "minimum-correlation-factor-portfolios"
date: "2020-10-22"
modified: "2022-05-21"
url: "https://alphaarchitect.com/minimum-correlation-factor-portfolios/"
categories: ["Skewness", "Research Insights", "Factor Investing", "Guest Posts"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Building Factor Portfolios Based with the Lowest Correlations

> INTRODUCTION The two basic rules of asset allocation are: i) identify assets with positive expected payoffs, and ii) ensure that the assets are not too […]

### **INTRODUCTION**

The two basic rules of asset allocation are: i) identify assets with positive expected payoffs, and ii) ensure that the assets are not too highly correlated, so that diversification benefits can be harvested. Although the rules are simple, implementation is often complex.

Equities have a positive expected return over the long-term as stocks represent risk capital in for-profit companies. Bonds pay interest. However, the case is not so clear for some asset classes like commodities or currencies. Neither Gold nor Bitcoin generate cashflows and are mainly driven by market sentiment.

Similarly, when creating a multi-factor portfolio, an investor should select factors that are expected to generate positive excess returns and are not too highly correlated. A classic strategy would be to [combine Value and Momentum](https://alphaarchitect.com/2016/07/07/creating-an-alternative-investment-strategy-with-value-and-momentum/), where research shows that these allow investors to outperform markets while being lowly correlated to each other as cheap stocks are typically not outperforming at the same time that the best-performing stocks tend to trade at expensive valuations.

In this short research note, we will analyze two-factor portfolios created by minimizing factor correlations.

### **METHODOLOGY**

We focus on seven factors namely Value, Size, Momentum, Low Volatility, Quality, Growth, and Dividend Yield in the US stock market. The long-only portfolios are created by selecting the top 30% stocks ranked by the factor definitions, which are in line with industry and academic standards. Only stocks with a minimum market capitalization of $1 billion are included. Portfolios are rebalanced monthly and each transaction incurs costs of 10 basis points.

The single-factor portfolios effectively represent smart beta strategies, which are available to investors via low-cost ETFs. There is little academic support for the Growth factor generating positive excess returns, but it is a widely followed investment style, which warrants its inclusion in this analysis.

### **PAIRING THE VALUE FACTOR**

Some factors are structurally highly correlated as they represent similar bets, e.g. sorting stocks by their dividend yield is one approach to determining if they are valued cheaply or expensive. However, even in this case, the correlation between the Value and Dividend Yield factors fluctuated across time.

We can highlight the changing correlations by using the Value factor as a case study. We calculate the correlation of the Value portfolio to the six other factors using a one-year lookback and always select the factor with the lowest correlation. The analysis highlights that the Size, Momentum, and Growth factors most frequently appeared as exhibiting the lowest correlation with the Value factor, which implies higher correlations to the Low Volatility, Quality, and Dividend Yield factors.

Some of these relationships are expected, e.g. the low correlation between Value and Growth, while others like the higher correlation between Value and Quality may be more of a surprise.

![](https://alphaarchitect.com/wp-content/uploads/2020/03/Factor-with-the-Lowest-Correlation-to-Value-in-the-US-1200x600.png)

Source: FactorResearch.The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

It is interesting to explore how factor correlations varied over the last 30 years. We observe the average minimum factor correlation was approximately 0.8 and almost the same across factors, which is perhaps explained by all factors representing long-only portfolios where most of the performance can be explained by the market beta.

The low and high points in minimum correlations were also comparable across factors. Correlations below 0.4 are relatively low for long-only portfolios and typically only reached when markets are significantly distorted, e.g. during the tech bubble in 2000. The high points of minimum correlations occurred during the global financial crisis from 2008 to 2009, when the correlations of almost all assets spiked and converged towards one.

![](https://alphaarchitect.com/wp-content/uploads/2020/03/Minimum-Two-Factor-Correlations-1990-2018-1200x600.png)

Source: FactorResearch.The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

**### TWO-FACTOR MINIMUM CORRELATION PORTFOLIOS**

We create two-factor portfolios by combining each of the seven factors with the factor exhibiting the lowest correlation. The portfolios are weighted equally between the two factors and rebalanced annually. For example, cheap stocks might be combined with growth stocks for one year, then with small stocks for the following year, and so on.

We observe that all two-factor portfolios outperformed the US stock market in the period from 1990 to 2018, except for the portfolio including Dividend Yield. These results support the case for factor investing, but it should be noted that most of the excess returns were achieved during the tech bubble implosion between 2001 and 2003, where certain factors like Value, Size, and Low Volatility significantly outperformed the stock market.

![](https://alphaarchitect.com/wp-content/uploads/2020/03/Two-Factor-Minimum-Correlation-Combinations-in-the-US-1200x600.png)

Source: FactorResearch.The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

### **ANALYZING MINIMUM CORRELATION PORTFOLIOS**

Intuitively, investors might expect that a multi-factor portfolio comprised of two factors, especially when selected on low correlations, should generate better risk-adjusted returns than a factor on a stand-alone basis.

However, analyzing the risk-adjusted returns between 1990 and 2018 highlights only marginal diversification benefits. The average risk-return ratio of the single-factor and two-factor portfolios were almost identical. Certain factors like Momentum benefited from being paired with a low-correlated factor, while others like Low Volatility did not. It is surprising that the diversification benefits were not stronger.

![](https://alphaarchitect.com/wp-content/uploads/2020/03/Two-Factor-Combinations-versus-Single-Factors-Risk-Return-Ratios-1200x599.png)

Source: FactorResearch.The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

Perhaps the lack of larger diversification benefits can be explained by the choice of only rebalancing annually. Markets change continuously and perhaps more frequent rebalancing might extract more value by adjusting quicker to shifting correlations.

We rerun the analysis with monthly, quarterly, and semi-annual rebalancing, but the risk-return ratios do not change compared to annual rebalancing. Although markets change constantly, correlations were relatively stable over time. On a positive note, annual rebalancing results in low transaction costs and reduced portfolio maintenance.

![](https://alphaarchitect.com/wp-content/uploads/2020/03/Two-Factor-Combinations-with-Different-Rebalancing-Periods-Risk-R-1200x600.png)

Source: FactorResearch.The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

As a further step in analyzing the two-factor portfolios created by minimizing factor correlations, we construct portfolios based on maximum correlations. Somewhat unexpected, both approaches resulted in similar risk-return ratios, which suggests that correlations are perhaps less meaningful when creating two-factor portfolios than commonly assumed.

![](https://alphaarchitect.com/wp-content/uploads/2020/03/Two-Factor-Combinations-Minimum-vs-Maximum-Correlations-Risk-Retu-1200x600.png)

Source: FactorResearch.The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

### **FURTHER THOUGHTS**

The most favorite factor combinations are likely small and cheap as well as cheap and winning stocks. The correlations between these factors were low historically, which is perceived as attractive from a classic portfolio construction perspective.

This analysis highlights that combining two factors by minimizing correlations did not generate significant diversification benefits. Naturally, there is a significant amount of research, including our own, that shows that multi-factor portfolios generate higher risk-adjusted returns than factors on a stand-alone basis. However, most of the research is focused on combining theoretical long-short factors, which feature much lower correlations than long-only factor portfolios. Unfortunately, most investors pursue factor investing via long-only smart beta products. As usual, there is a difference between theory and reality.
