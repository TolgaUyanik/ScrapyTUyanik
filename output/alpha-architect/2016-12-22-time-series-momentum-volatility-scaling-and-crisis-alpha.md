---
title: "Time Series Momentum, Volatility Scaling, and Crisis Alpha"
slug: "time-series-momentum-volatility-scaling-and-crisis-alpha"
date: "2016-12-22"
modified: "2022-05-10"
url: "https://alphaarchitect.com/time-series-momentum-volatility-scaling-and-crisis-alpha/"
categories: ["Managed Futures Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Time Series Momentum, Volatility Scaling, and Crisis Alpha

> If you couldn’t tell from our recent monster commodity futures post, we’ve been thinking a lot about futures recently. The futures research area is relatively “fresh,” and […]

If you couldn’t tell from our recent [monster commodity futures](https://alphaarchitect.com/2016/12/21/commodity-investing-is-complex-and-volatile-but-unique/) post, we’ve been thinking a lot about futures recently. The futures research area is relatively “fresh,” and a lot more exciting than hacking through equity stock selection research where we already understand the basic answer — [buy cheap/quality](https://alphaarchitect.com/2014/10/07/the-quantitative-value-investing-philosophy/), [buy strength](https://alphaarchitect.com/2015/12/01/quantitative-momentum-investing-philosophy/), and [embrace relative performance pain](https://alphaarchitect.com/2015/08/17/the-sustainable-active-investing-framework-simple-but-not-easy/).

As part of our research education series on futures, we recently reviewed an engrossing paper, “[Time Series Momentum and Volatility Scaling](https://alphaarchitect.com/2016/08/31/time-series-momentum-and-volatility-scaling/),” by Abby Y. Kim, Yiuman Tse, John K. Wald (KTW), which revisits the findings regarding another futures paper, “[Time Series Momentum](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2089463),” by Tobias J.Moskowitz, Yao Hua Ooi, Lasse Heje Pedersen (MOP).

We recap the core findings from KTW and MOP below:

## Time Series Momentum Key Insights (by MOP)

The key elements from MOP are as follows:

1. 58 future contracts cover the 1965-2009 period (24 commodities, 12 cross-rate currency pairs, 9 developed equity indexes and 13 developed government bonds).
2. Strategy is based on time-series momentum, i.e, were past returns positive or negative? Positive = long; negative = short
3. Positions are volatility weighted so that high-volatility assets will not dominate returns. This is similar to an equally weighted risk parity portfolio, in which the weights refer to risk. In MOP, target vol is around 40% versus average vol of 19%, effectively 2x leverage.
4. A volatility-scaled TSMOM strategy (12 month lookback, 1 month hold) generates 1.09% excess returns monthly (w/t-stat of 5.4), after controlling for Asness et al. value/momentum “everywhere” factors for global stock returns, bond returns, currencies and commodities.
5. TSMOM loads on Asness et al.’s cross-sectional momentum, but their everywhere factor does not explain it.

## Time Series Momentum and Volatility Scaling Key Insights (by KTW)

The KTW paper revisits the analysis from MOP. Using 55 futures contracts cover the 1985-2009 period, the authors confirm the results from MOP. However, KTW identify the following results that appear to conflict with MOP:

1. Using an unscaled, equal-weighted method, the alpha of a TSMOM portfolio drops to 0.39% per month, v.s. vol-scaled, TSMOM’s 1.08% monthly alpha.
2. Without vol scaling, the portfolio alpha is similar to a buy-and-hold futures portfolio. Using the unscaled method, the alpha of a buy-and-hold strategy is 0.34% per month. Moreover, when buy-and-hold is scaled using the MOP method, it generates a 0.73% estimate of monthly alpha.
3. KTW argue that the strong TSMOM returns identified by MOP were due to leveraging a strategy that happened to have a positive alpha estimate for a buy-and-hold “passive” strategy during this sample period.
4. When one examines “unlevered” TSMOM (i.e., with no volatility scaling) it does not significantly outperform buy-and-hold.
5. **Bottomline:** the outperformance of TSMOM is largely driven by vol-scaling, or leverage, not by abnormal returns associated with TSMOM.

## Reconciling the Disagreement

We think MOP and KTW have inspired an intriguing debate. To get closer to understanding the “truth,” we conducted our own research into the question. Our sample covers the 1998-7/2016 period, and includes 38 future contracts for commodities, fixed income, and equities (22 commodities contracts, 7 developed bond contracts, 9 equity index contracts). We excluded currency contracts and a few other contacts because our ability to trade contracts is limited to what is available at Interactive Brokers.

The contracts are as follows:

![2016-10-27-13_45_07-aa-lt-mf-v01-pptx-microsoft-powerpoint](https://alphaarchitect.com/wp-content/uploads/2016/10/2016-10-27-13_45_07-AA-LT-MF-V01.pptx-Microsoft-PowerPoint.png)

### Strategies Tested

1. MF1: volatility weighted, **non-scaled** (annualized volatility of 4.55%), **Buy&Hold**, monthly rebalance
2. MF2: volatility weighted, **non-scaled** (annualized volatility of 4.45%), 12-month **TSMOM**, monthly rebalance
3. MF3: volatility weighted, **scaled** (with target an annualized 12% volatility at the portfolio level), **Buy&Hold**, monthly rebalance
4. MF4: volatility weighted, **scaled** (with target an annualized 12% volatility at the portfolio level), 12-month **TSMOM**, monthly rebalance

The returns from futures are all excess returns and do not include interest received on a fully collateralized futures position.

### Benchmarks

1. SPY – SP500 total return index
2. LTR – U.S. Treasury 10-Year bond total return index
3. 60\_40 – 60% in SPY, 40% in LTR

All returns are total returns and include the reinvestment of distributions (e.g., dividends). Data is from Bloomberg and publicly available sources.

### Results of Our Analysis

The chart below shows the summary results from our analysis, covering the period 1998– 7/2016:

![2016-10-27-11_39_30-microsoft-excel-final-xlsx](https://alphaarchitect.com/wp-content/uploads/2016/10/2016-10-27-11_39_30-Microsoft-Excel-final.xlsx.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Based on our analysis, we can see that there is huge difference between non-vol-scaled (MF1 and MF2) and the vol-scaled (MF3 and MF4). Because vol-scaling is essentially leveraging the positions, when you scale up the vol, you scale up the returns!

Note how the MF1 CAGR of 4.21% and the MF2 CAGR of 4.56% are significantly enhanced by vol-scaling, going to an 11.00% CAGR for MF3 and a 12.25% CAGR for MF4. By contrast, when you de-leverage the position, you get a lower CAGR. Leverage is a powerful thing when applied to a strategy that generates “alpha.”

Here are the annual returns for each strategy:

![2016-10-27-11_42_05-microsoft-excel-final-xlsx](https://alphaarchitect.com/wp-content/uploads/2016/10/2016-10-27-11_42_05-Microsoft-Excel-final.xlsx.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

In each row, we use conditional color formatting to highlight difference of annual returns between different strategies. Red means relatively good and green means relatively bad. MF without TSMOM (MF1, MF3) can provide some degree of tail risk protection in a handful of events such as in 2000, 2001 and 2002. MF with TSMOM can protect investors better in big risk events like 2008, when SPY was down 36%, but MF2 was up 15% and MF4 was up 43%. However, since MF is an alternative asset, in some of the years, these strategies underperforms the market by extreme margins. For example, in 2009, SPY is up 26%, while MF4 is down 10.70%. 

## Is Time Series Momentum a Busted Strategy?

CAGR, standard deviations, and Sharpe ratios are only half of the story when it comes to time series momentum strategies, because correlations and portfolio diversification elements are also valuable. In our view, time series based futures strategies represent an “alternative” asset class, with generally lower correlations to other asset classes.

In order to assess  TSMOM’s relative value as a diversifier, we present below a correlation matrix that compares strategies and benchmarks:

![2016-10-27-11_45_00-microsoft-excel-final-xlsx](https://alphaarchitect.com/wp-content/uploads/2016/10/2016-10-27-11_45_00-Microsoft-Excel-final.xlsx.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

TSMOM (MF2 and MF4) exhibits a -27.56% correlation with SPY. From a portfolio construction standpoint, this is a valuable characteristic. Compare this correlation estimate with the Buy&Hold version of the strategy (MF1 and MF3), which has a *positiv*e 56.48% correlation with SPY (as an aside, if you are curious as to why levered/unlevered correlations of the same strategy would be identical, Cliff Asness has an interesting [post](https://www.aqr.com/cliffs-perspective/hedging-on-hedge-funds-postscript-on-correlations-beta-and-alpha) that discusses a variation of this issue).

From a diversification perspective, TSMOM would seem to add significant value to a portfolio, regardless of vol-scaling.

Finally, here we highlight some large drawdown events for SPY and the associated MF strategy returns over these same periods:

![2016-10-27-12_17_14-microsoft-excel-final-xlsx](https://alphaarchitect.com/wp-content/uploads/2016/10/2016-10-27-12_17_14-Microsoft-Excel-final.xlsx.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

TSMOM (MF2, MF4) generates strong downside protection in the face of big market blow-ups, whereas Buy&Hold futures have generally correlated drawdowns with the SPY, albeit, less dramatic.

Below are monthly return distributions of vol-scaled Buy&Hold (MF3), vol-scaled TSMOM (MF4), and bonds (LTR) compared with negative return months for SPY:

![2016-10-27-12_25_36-microsoft-excel-mf-tsmom-data-xlsx](https://alphaarchitect.com/wp-content/uploads/2016/10/2016-10-27-12_25_36-Microsoft-Excel-MF-TSMOM-DATA.xlsx.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The blue line, MF3 (scaled, Buy&Hold), consistent with its positive correlation with SPY, tends to decline with SPY, although it does not show declines of the same magnitude as SPY.

By contrast, the red line, MF4 (scaled, TSMOM), consistent with its negative correlation with SPY, tends to *increase* when SPY *decreases*. And not only that, the slope for MF4 is actually *steeper* than for bonds (green line)! Wow.

MF4 returns are concentrated in the area where a true alternative asset should be and shows a convexity property that is highly desirable from a portfolio construction standpoint.

## Time Series Momentum Smiles At You

The MOP paper alludes to the convexity effect documented above.

Below is a graph from the MOP paper that documents the quarterly returns for a 12-month TSMOM strategy plotted against the S&P 500:

[![2016-11-04-13_58_34-yangcommodities-pdf-adobe-acrobat-pro](https://alphaarchitect.com/wp-content/uploads/2016/11/2016-11-04-13_58_34-yangcommodities.pdf-Adobe-Acrobat-Pro.png)](https://alphaarchitect.com/wp-content/uploads/2016/11/2016-11-04-13_58_34-yangcommodities.pdf-Adobe-Acrobat-Pro.png)  
From the paper:

> The returns to TSMOM are largest during the biggest up and down market movements…TSMOM, therefore, has payoffs similar to an option straddle on the market…[the] TSMOM strategy generates this payoff structure because it tends to go long when the market has a major upswing and short when the market crashes…Historically, TSMOM does well during “crashes” because crises often happen when the economy goes from normal to bad (making TSMOM go short), and then from bad to worse (leading to TSMOM profits), with the recent financial crisis of 2008 being a prime example.

## Summary

We don’t disagree with KTW that the TSMOM “alpha” found by MOP is related the strategy’s leverage-like use of volatility scaling. Without volatility scaling, returns and/or “alpha estimates” to a TSMOM strategy are not that different from a buy-and-hold strategy. So we commend their research and for making us think harder and longer about the results published in Moskowitz, Ooi, and Pedersen (2012).

However, the real value of the TSMOM strategy is not evident when examining standard summary statistics. Rather, the value of TSMOM strategies is highlighted when one considers the genuinely unique diversification qualities these strategies bring to the table relative to B&H strategies — especially when examining how TSMOM strategies act during SPY “tail” events. When we conduct the full analysis of TSMOM versus B&H futures strategies, we once again identify why TSMOM strategies are unique relative to B&H futures strategies.

---

## Time Series Momentum and Volatility Scaling

* Kim, Tse and Wald
* A version of the paper can be found [here](http://fulltext.study/preview/pdf/960841.pdf).
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap](https://alphaarchitect.com/category/architect-academic-insights/academic-research/#gs.UqZWJJ0) Category.

### Abstract

> Moskowitz, Ooi, and Pedersen(2012) show that time series momentum delivers a large and significant alpha for a diversified portfolio of international futures contracts.We find that their results are largely driven by volatility-scaling returns (or the so-called risk parity approach to asset allocation) rather than by time series momentum. Without scaling by volatility, time series momentum and a buy-and-hold strategy offer similar cumulative returns, and their alphas are not significantly different. This similarity holds for most sectors and for a combined portfolio of futures contracts. Cross-sectional momentum also offers a higher (similar) alpha than unscaled (scaled) time series momentum.
