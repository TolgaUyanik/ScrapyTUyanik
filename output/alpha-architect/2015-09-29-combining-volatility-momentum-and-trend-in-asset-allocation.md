---
title: "Combining volatility, momentum, and trend in asset allocation"
slug: "combining-volatility-momentum-and-trend-in-asset-allocation"
date: "2015-09-29"
modified: "2022-05-25"
url: "https://alphaarchitect.com/combining-volatility-momentum-and-trend-in-asset-allocation/"
categories: ["Research Insights", "Momentum Investing Research", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Combining volatility, momentum, and trend in asset allocation

> The Effective Combination of Risk-Based Strategies with Momentum and Trend Following Gregory Guilmin A version of the paper can be found here. Want a summary of […]

### The Effective Combination of Risk-Based Strategies with Momentum and Trend Following

* Gregory Guilmin
* A version of the paper can be found [here](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2556747).
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category](https://alphaarchitect.com/category/academic-research/).

### Abstract:

> The Efficient Market Hypothesis (EMH) has been widely called into question in the investment literature, through two main anomalies: timing and low-volatility anomalies. In this paper, we aim to combine the predictive power of timing and low-volatility strategies to deliver better risk-adjusted portfolio performance. We adopt a **two-step approach** for a constant dataset composed of 18 country MSCI stock market indices over the 1975-2014 period. **First, we use different timing strategies: moving averages and momentum.** We select stock market indices based on different moving averages (6, 8, 10, and 12 months), while the momentum strategy ranks the different stock market indices into momentum subsets (low, medium, and high momentum). After the first step using the different timing strategies, **the second step consists in building risk-based portfolios** (MV, ERC, and MD) as well as 1/N benchmark portfolios for each of these timing strategies. Our results highlight the effectiveness, the relevance and the robustness of our approach. First, risk-based portfolios using relevant timing strategy indeed provide better returns, lower volatilities, higher Sharpe ratios, and lower Value-at-Risk (VaR) and Expected Shortfall (ES) than traditional risk-based portfolios. The second contribution of our approach features that risk-based strategies provide better risk-adjusted returns and lower VaR and ES than the 1/N portfolio within a context in which the first step is dedicated to the application of a relevant timing strategy. Finally, among these risk-based portfolios using relevant timing strategies, the MD and MV portfolios usually obtain the best risk-adjusted performance.

### Alpha Highlight:

Risk-based portfolio strategies are popular in the asset management industry. Three common strategies are Minimum Variance (MV), Equal Risk Contribution (ERC) and Maximum Diversification (MD). These strategies do not depend on asset returns’ forecasts and they are based on a single criterion: **risk**.

The interest in estimation procedures relying on a risk measure could be explained by three major factors:

1. Reconsideration of the importance and the relevance of portfolio risk management.
2. Better predictability of security variance and covariance risks by comparison with expected returns.
3. The outperformance of the “low-volatility anomaly.” Details [here](https://alphaarchitect.com/category/architect-academic-insights/low-volatility-investing/).

In addition to the low-volatility anomaly, a large number of authors have talked about the “momentum anomaly.” The momentum effect has been emphasized by Jegadeesh and Titman (1993). Momentum strategies are profitable in most major stock markets worldwide and this outperformance of momentum strategies is consistent over time. Linked to this concept of cross sectional momentum, time-series momentum, such as trend following strategies, have been identified. Several academic papers show that moving average trading rules have predictive power for future returns, and that trend following strategies with moving averages are effective in practice (Among others, see Brock et al., 1992; Clare et al., 2014; Faber, 2007, 2013; Hurst et al., 2010 and ap Gwilym et al., 2010).

### Methodology:

Given this backdrop, in which risk-based strategies and timing strategies have been developed in the literature, the purpose of this paper is to combine the two strategies. This two-step approach consists in applying a timing strategy (either a moving average or a momentum strategy in the first step) followed by risk-based portfolio optimization procedures (second step). We compute risk-based and equally weighted (as a benchmark) portfolios with and without timing strategies in the first step for a constant empirical dataset composed of 18 country MSCI stock market indices. The estimation period ranges from January 1975 to December 2014. To the best of our knowledge, this paper is the first to shed light on the combination of timing and risk-based strategies.

#### ***First Step: Selection of the stock market indices***

The methodology consists of two steps. In the first step, moving averages are used to select stock market indices that perform well (by exhibiting an upward trend) and that are used in the second step of our analysis (i.e., in the risk-based and 1/N portfolio optimization). Stock market indices exhibiting a negative trend are not selected as an input in the portfolio optimization procedure. If the price of the stock market index is above its x − month moving average, then this index is selected for the portfolio optimization procedure. Conversely, if it crosses below its x − month moving average, then the stock market index is not selected for the second step. We use moving averages of varying lengths: 6, 8, 10, and 12 months.  
To add an additional timing strategy, we also select stock market indices in accordance with the concept of momentum, in which a stock market’s performance relative to its peers predicts its future relative performance. As long-term investors, the momentum strategy involves ranking stock market indices based on their past 12-month performance and splitting them into three subsets, depending on the value of their momentum compared with one of their peers. The three subsets are the low, medium and high momentum subsets, respectively.

#### ***Second Step: Portfolio optimization***

After selecting stock market indices following the different timing strategies of the first step, the second stage consists in applying different portfolio optimization procedures to find the optimal weights of the selected stock market indices. Selection (1st step) and weighting (2nd step) are adjusted simultaneously, i.e., on a monthly basis (end of month).

We apply three risk-based portfolio strategies (Minimum Variance, Equal Risk Contribution and Maximum Diversification) as well as the 1/N benchmark portfolio strategy, usually considered a relevant benchmark in the literature. First, the Minimum Variance (MV) portfolio aspires to minimize the global variance of the portfolio. Second, the Equal Risk Contribution (ERC) portfolio is the portfolio in which the risk contribution is the same for all assets in the portfolio. Finally, the Maximum Diversification (MD) portfolio (also called the Most Diversified Portfolio), introduced by Choueifaty (2006), is the portfolio that maximizes diversification. Diversification is computed using the diversification ratio. The diversification ratio is defined as the ratio of its weighted average volatility to its portfolio volatility.

### Main Findings:

The table below summarizes results based on a constant dataset composed of 18 country MSCI stock market indices between 1975 and 2014. We can see that **all portfolios that employ moving averages in the first step perform better than initial risk-based portfolios.** Regarding momentum, **high momentum risk-based strategies offer better annual performance than initial risk-based portfolios.**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Table 1: Portfolio performances with the constant country MSCI Indices sample (1975-2014) | | | | | | |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | **Annualized** | **Annual** | **Annualized** | **Sharpe** | **VaR (1%)** | **ES (1%)** |
|  | **returns (%)** | **returns (%)** | **Volatility (%)** | **Ratio** | **(%)** | **(%)** |
| **Initial Portfolios** |  |  |  |  |  |  |
| 1/N | 8.931 | 10.013 | 16.723 | 0.599 | -13.118 | -18.531 |
| MV | 8.152 | 8.866 | 14.017 | 0.632 | -10.987 | -14.785 |
| ERC | 8.785 | 9.781 | 16.131 | 0.606 | -12.550 | -18.116 |
| MD | 8.624 | 9.655 | 16.275 | 0.593 | -14.254 | -17.890 |
| **With timing strategies** |  |  |  |  |  |  |
| 6 months |  |  |  |  |  |  |
| 1/N | 10.032 | 10.732 | 14.965 | 0.717 | -11.946 | -15.482 |
| MV | 9.987 | 10.472 | 13.439 | 0.779 | -10.238 | -13.884 |
| ERC | 9.605 | 10.256 | 14.387 | 0.713 | -11.592 | -15.107 |
| MD | 10.515 | 11.166 | 14.882 | 0.750 | -11.966 | -15.843 |
| 8 months |  |  |  |  |  |  |
| 1/N | 10.401 | 11.062 | 14.897 | 0.743 | -11.946 | -15.363 |
| MV | 10.626 | 11.056 | 13.419 | 0.824 | -10.212 | -13.961 |
| ERC | 10.107 | 10.694 | 14.218 | 0.752 | -11.592 | -15.000 |
| MD | 11.079 | 11.650 | 14.664 | 0.794 | -11.966 | -15.787 |
| 10 months |  |  |  |  |  |  |
| 1/N | 9.832 | 10.534 | 14.842 | 0.710 | -11.665 | -15.258 |
| MV | 9.299 | 9.853 | 13.499 | 0.730 | -10.871 | -14.453 |
| ERC | 9.486 | 10.119 | 14.170 | 0.714 | -11.311 | -15.026 |
| MD | 10.191 | 10.855 | 14.744 | 0.736 | -11.966 | -16.022 |
| 12 months |  |  |  |  |  |  |
| 1/N | 10.612 | 11.229 | 14.725 | 0.763 | -11.904 | -15.220 |
| MV | 10.523 | 10.957 | 13.358 | 0.820 | -10.602 | -14.488 |
| ERC | 10.494 | 11.020 | 14.021 | 0.786 | -11.621 | -15.066 |
| MD | 11.206 | 11.766 | 14.671 | 0.802 | -12.325 | -16.304 |
| Low momentum |  |  |  |  |  |  |
| 1/N | 5.359 | 7.021 | 18.821 | 0.373 | -14.322 | -19.843 |
| MV | 5.533 | 6.855 | 17.063 | 0.402 | -13.632 | -17.501 |
| ERC | 5.162 | 6.704 | 18.127 | 0.370 | -14.152 | -19.464 |
| MD | 5.773 | 7.233 | 17.884 | 0.404 | -13.852 | -19.023 |
| Medium momentum |  |  |  |  |  |  |
| 1/N | 8.919 | 9.997 | 16.747 | 0.597 | -12.766 | -17.035 |
| MV | 9.245 | 10.101 | 15.602 | 0.647 | -11.012 | -15.796 |
| ERC | 9.069 | 10.087 | 16.456 | 0.613 | -12.456 | -16.953 |
| MD | 9.247 | 10.309 | 16.770 | 0.615 | -14.402 | -18.084 |
| High momentum |  |  |  |  |  |  |
| 1/N | 11.896 | 13.022 | 18.266 | 0.713 | -14.637 | -20.915 |
| MV | 12.583 | 13.446 | 17.231 | 0.780 | -11.539 | -18.729 |
| ERC | 12.16 | 13.178 | 17.834 | 0.739 | -13.770 | -20.125 |
| MD | 12.092 | 13.218 | 18.356 | 0.720 | -13.443 | -20.719 |
| **Market-cap weighted benchmarks** | |  |  |  |  |  |
| MSCI World | 8.016 | 8.839 | 14.782 | 0.598 | -11.073 | -14.564 |
| MSCI World Momentum | 11.432 | 12.130 | 15.817 | 0.767 | -11.517 | -14.965 |

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.*

Trend following and high momentum strategies are effective for 1/N portfolio optimization but also for risk-based portfolios because they produce better annual returns compared with initial risk-based portfolios. With respect to risk measures such as volatility, Value-at-Risk (VaR) and Expected Shortfall (ES), risk-based portfolios that employ moving averages exhibit lower volatility than initial risk-based portfolios as well as lower VaR and ES. This finding is important because it enables investors to reduce the risk to which they are exposed. With higher returns and lower risk, risk-based portfolios that use moving averages have higher Sharpe ratios than initial risk-based portfolios. High momentum risk-based portfolios, by contrast, have higher risk, which is largely compensated for by higher returns. Therefore, such portfolios are characterized by higher Sharpe ratios than initial risk-based portfolios. This paper documents the effectiveness, in terms of risk and return, of the use of these relevant timing strategies combined with risk-based portfolio strategies.

In addition to that, robustness checks were also conducted with different other datasets, different estimation periods as well as different parameters of the variance-covariance matrix.

Note: This is a guest post by [Gregory Guilmin](https://gregoryguilmin.wordpress.com/) who has just obtained his PhD from the University of Louvain and who reached out last year to share his dissertation research.
