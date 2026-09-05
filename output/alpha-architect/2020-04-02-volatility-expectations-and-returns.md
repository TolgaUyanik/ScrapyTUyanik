---
title: "Volatility Expectations and Returns"
slug: "volatility-expectations-and-returns"
date: "2020-04-02"
modified: "2022-05-20"
url: "https://alphaarchitect.com/volatility-expectations-and-returns/"
categories: ["Volatility (e.g., VIX)", "Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Volatility Expectations and Returns

> A large body of research, including the 2017 study “Tail Risk Mitigation with Managed Volatility Strategies” by Anna Dreyer and Stefan Hubrich, demonstrates that while […]

A large body of research, including the 2017 study “[Tail Risk Mitigation with Managed Volatility Strategies](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3074529)” by Anna Dreyer and Stefan Hubrich, demonstrates that while past returns do not predict future returns, past volatility largely predicts future near-term volatility, i.e., volatility is persistent (it clusters). High (low) volatility over the recent past *tends to* be followed by high (low) volatility in the near future. Evidence that past volatility predicts future volatility has been found not only in stocks but also in bonds, commodities and currencies. (For a detailed look at volatility scaling, check out these articles: [Volatility Targeting](https://alphaarchitect.com/2019/05/22/volatility-targeting-improves-risk-adjusted-returns/) and  [Volatility](https://alphaarchitect.com/2016/12/22/time-series-momentum-volatility-scaling-and-crisis-alpha/) Scaling.)

Such evidence has led to the development of strategies that manage volatility (target a constant level of volatility rather than a constant nominal exposure) by leveraging a portfolio at times of low volatility and scaling down at times of high volatility.

Campbell Harvey, Edward Hoyle, Russell Korgaonkar, Sandy Rattray, Matthew Sargaison and Otto Van Hemert contributed to the literature on managing volatility with their 2018 study “[The Impact of Volatility Targeting](https://jpm.iijournals.com/content/45/1/14).” They examined the impact of volatility targeting on 60 assets, with daily data beginning as early as 1926. Their data sample ends in 2017. Among their key findings was that scaling reduces volatility. It also reduces excess kurtosis (fatter tails than in normal distributions): scaling cuts both tails, right (good tail) and left (bad tail). And for portfolios of risk assets Sharpe ratios (SRs), measures of risk-adjusted return, are higher with volatility scaling.

Harvey, Hoyle, Korgaonkar, Rattray, Sargaison, and Van Hemert also found that risk assets exhibit a negative relationship between returns and volatility. Thus, volatility scaling effectively introduces some momentum into strategies. Since volatility often increases in periods of negative returns, targeting volatility causes positions to be reduced, which is in the same direction as what one would expect from a time-series momentum (trend following) strategy.

This finding, that time-series momentum improves risk-adjusted returns, is consistent with that of prior research, including the June 2017 study “[A Century of Evidence on Trend-Following Investing](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2993026)” by Brian Hurst, Yao Hua Ooi and Lasse Pedersen.

![](https://alphaarchitect.com/wp-content/uploads/2020/02/image-8-600x643.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

Lars Lochstoer and Tyler Muir contribute to the literature on volatility with the October 2019 study “Volatility Expectations and Returns.” Their database covered U.S. stocks, realized variance, the VIX (implied volatility index), and investor surveys over the period 1990 through 2018.

Following is a summary of their findings:

* Current volatility relative to its average over the period of a few months negatively forecasts future stock returns over the next month, despite positively forecasting next month’s volatility. This is explained by investors having slow-moving beliefs about stock market volatility.
* When volatility increases, the equity and variance risk premiums fall or stay flat at short horizons, despite the higher future risk. However, these premiums appear to rise at longer horizons after future volatility has subsided, though they do so at horizons for which they only weakly forecast future volatility.
* Strategies that time volatility have generated alpha.
* Measures of the variance risk premium display strikingly similar patterns. For example, increases in volatility appear to negatively predict the premium on VIX futures at short horizons. Claims that provide insurance against future volatility, which are unconditionally expensive, appear “too cheap” after volatility rises. Similar to the pattern in stock returns, increases in volatility positively forecast the variance risk premium at longer horizons.
* The variance risk premium forecasts stock returns more strongly than either realized variance or risk-neutral variance. The variance risk premium strongly forecasts stock returns suggesting equity risk premiums are high when the variance risk premium is high.
* Changes in volatility are negatively correlated with contemporaneous returns. Slow-moving expectations about volatility lead investors to initially underreact to volatility news followed by a delayed overreaction. This results in a weak, or even negative, risk-return tradeoff at shorter horizons, but a stronger tradeoff at longer horizons (beyond where one can strongly forecast volatility).

The authors concluded:

> Agents pay relatively too much attention to past volatility, they temporarily underreact to increases in volatility and then subsequently overreact. When agents see volatility increase they still react partially, driving prices down so that volatility is associated with negative returns contemporaneously. However, the initial underreaction means prices can continue to fall in the next period making ex-ante “risk premiums” appear flat, or even negative, and the subsequent overreaction keeps prices depressed for longer before eventually bouncing back, making it appear as though risk premiums are high well after the shock to volatility has largely subsided. Market expectations of volatility (the VIX) mirror this, meaning the variance risk premium can initially fall before slowly rising at longer horizons.

These findings led them to conclude: “It is cheap to insure against future volatility when volatility increases.” Their results held at the firm level, providing a test of robustness.

## Conclusions

Before drawing any conclusions we need to examine two of their findings. The first is that they found that high realized volatility today predicts high realized volatility tomorrow. The r-squared was 51 percent (Table 1, column 7 of their paper). As noted above, this is well-documented in the literature, and the intuition is that volatility clusters. However, their conclusion that “claims that provide insurance against future volatility, which are unconditionally expensive, appear ‘too cheap’ after volatility rises,” (the premium is -0.7 percent per month during such periods) is actually weak. Table 1, column 5 shows an r-squared of just 0.8 percent, essentially zero.

What can we conclude from their findings? First, they provide further evidence of behavioral anomalies that result from investors under- and overreacting to new information. The high-squared of the variance (0.51) shows that investors tend to behave in this manner. This finding also provides further support for scaling momentum and volatility. However, the low r-squared for the realized premium indicates that trying to time the premium might not be a good trading strategy.
