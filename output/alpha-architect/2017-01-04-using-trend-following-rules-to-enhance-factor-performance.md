---
title: "Using Trend-Following Rules to Enhance Factor Performance"
slug: "using-trend-following-rules-to-enhance-factor-performance"
date: "2017-01-04"
modified: "2022-05-10"
url: "https://alphaarchitect.com/using-trend-following-rules-to-enhance-factor-performance/"
categories: ["Research Insights", "Factor Investing", "Trend Following", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Using Trend-Following Rules to Enhance Factor Performance

> After reviewing the 2016 performance of trend-following (-18.15%), its unclear why anyone would mention the word “trend following” in a public forum. But we’ll give it […]

After reviewing the [2016 performance of trend-following](http://www.wisdomtrading.com/trend-following-december-2016/) (-18.15%), its unclear why anyone would mention the word “trend following” in a public forum. But we’ll give it a whirl anyway…

The comedian Victor Borge once famously observed, “Santa Claus has the right idea – visit people only once a year.”

In studying investment markets, many have taken a similar approach, preferring a once-a-year perspective, which has become a standard convention in academic research.

For example, in market anomaly research, academics often use data that employs an annual rebalance. This is true for many well-known anomalies based on fundamentals such as book-to-market based strategies. Researchers prefer annual data, since quarterly data can be subject to revision, whereas annual information (i.e., 10-k) tends to be a more stable and reliable. While the use of annual data is more robust from a data integrity standpoint, this approach also implies empirical observations will be based on “low frequency” information, since stock characteristics are measured only once every 12 months.

But in the real world, portfolio managers are not like Santa, who gets focused on his job only once a year. Practitioners often rebalance more frequently, since this can be more effective. For instance, Jack posted [here](https://alphaarchitect.com/2015/03/19/how-rebalancing-frequency-affects-quality-and-value-investing-funds/#gs._xJWlL0) about how more frequent rebalancing can enhance value portfolios, even after accounting for costs. Also, [Asness and Frazzini have a paper](https://www.aqr.com/library/journal-articles/the-devil-in-hmls-details) on how more frequent updating of B/M enhances the performance of the B/M anomaly.(1)  
In “[Anomalies Enhanced: The Value of Higher Frequency Information](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2624650),” by Han, Huang and Zhou, the authors explore whether they can improve anomaly results by making use of higher frequency information.

What type of information?

Specifically, they wanted to see if they could use *monthly price performance data* to inform a more frequent, monthly rebalance, in which they would go long “good” stocks, and short “bad” stocks within the long/short legs of various anomalies.

The authors apply **a simple trend performance rule** to make use of high frequency (monthly) performance information. The strategy is quite straightforward, and is referred to as **Moving Average Convergence/Divergence (MACD)**, as originally proposed by [Gerald Appel](https://en.wikipedia.org/wiki/MACD) in the late 1970s. Since it’s based only on prices it’s easy for average investors to apply.

Every month, the authors evaluate each stock in the anomalous portfolios:

* If the 50-day MA price is above than the 200-day MA price, keep it in the long leg of an anomaly as a “good” stock; otherwise, sell it;
* If the 50-day MA price is lower than the 200-day MA price, keep it in the short leg of an anomaly as a “bad” stock; otherwise, drop it.

Then they apply this simple trend-following methodology to the below eight anomalies. The sample period is from July 1965 to Dec 2013.

* Book-to-market ratio anomaly (BM) — Fama and French (1996, 2008)
* Operating profit anomaly (OP) — Fama and French (2015)
* Gross profitability anomaly (GP) — Novy-Marx (2013)
* Asset growth anomaly (AG) — Cooper, Gulen, and Schill (2008)
* Investment growth anomaly (IK) — Xing (2008)
* Net stock issue anomaly (NS) — Ritter (1991)
* Accrual anomaly (AC) — Sloan (1996)
* Net operating assets anomaly (NOA) — Hirshleifer, Hou, Teoh, and Zhang (2004)

The eight anomalous portfolios are constructed based on their accounting variables for the fiscal year ending in calendar year t-1. Next, the authors create equal weight decile portfolios, and spread portfolios between the high and low deciles. Anomaly portfolios are rebalanced annually, and stocks < $5 are deleted to eliminate microstructure issues.

The authors apply the above MA filter on each anomaly each month to keep only “good” stocks in the long leg of the anomaly, and only “bad” stocks in the short leg. In short, they keep stocks whose trends continue, but drop stocks whose trends reverse. Next they form equal-weight portfolios using the remaining stocks left in the deciles, and calculate spread portfolios.

This approach is differentiated from a strictly cross-sectional approach, in that it uses the *time series properties of individual stocks* as an overlay on a simple cross-sectional approach. The idea is that higher frequency information — in the form of short-term momentum signals — can add value to a static anomaly portfolio with an annual rebalance.

### Performance Improvement by MA Filter

The results show that the performance of all the eight annual anomalies is greatly enhanced by the above simple MA approach. (Here is the visual depiction of the results in Table I in the paper)

![Performance Improvement by MA Filter_Avg Ret](https://alphaarchitect.com/wp-content/uploads/2016/01/Performance-Improvement-by-MA-Filter_Avg-Ret.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

![Performance Improvement by MA Filter_Sharpe](https://alphaarchitect.com/wp-content/uploads/2016/01/Performance-Improvement-by-MA-Filter_Sharpe.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Digging into the Results

Seem like a home run! As a result of using the MA filter, all the anomalies show statistically significant (at the 1% level) increases in returns for the spread portfolios, with incremental spread returns ranging from 0.57% to 0.94%.

*What’s not to like about this strategy?*Let’s dig a little deeper.

First, the authors want to know what this MA filter does when applied to *all* stocks, which will be the benchmark. They find the spread of the MA rule yields 0.50%. Now, compared with that benchmark, the incremental spread of 0.57% to 0.94% doesn’t look quite as impressive.

Second, the performance gains from using this “crossover MA” rule come mostly from the short side. When the authors examine the improvement in Fama-French 3-factor alpha using the MA filter, they find the alphas on the short side to be significantly negative and large, whereas on the long side, the alphas are small and insignificant. In addition, performance improvements in the short leg are much larger than those in the long leg. The MA rule seems to succeed because it drops stocks  on the short side whose trends are reversing, suggesting an imminent rebound.

We are left with an MA strategy that mostly enhances the short side of the anomalies, whose spread performances are themselves dominated by the short leg to begin with. From a practitioner perspective, this implies a number of potential issues, since there are numerous impediments to using short sales to benefit from overpricing.

### Information Uncertainty

While we may have some questions about the practical implementability of this strategy in the real world, the results are interesting from a theoretical perspective.

We’ve examined [the world’s longest trend-following backtest](https://alphaarchitect.com/2015/11/09/the-worlds-longest-trend-following-backtest/) and demonstrated that simple moving averages appear to be a robust risk-management signal over the past 200 years. Why might this particular flavor of trend following work so well in this context? The authors go on to conduct some additional tests that shed light on how and why this MA strategy seems to work.

The authors hypothesize it has to with “information uncertainty.” The authors measure this using three proxies: Idiosyncratic volatility (we have posted [here](https://alphaarchitect.com/2014/12/19/a-quick-lesson-in-volatility-measures/#gs.9NvJI3w) on this previously), firm age and number of analysts.

The authors propose the following:

> “[Han, Yang and Zhou (2013)](https://www.kevinsheppard.com/images/c/c5/Han_Yang_Zhou.pdf) shows that the profitability of a simple moving average rule is critically dependent on **information uncertainty** of stocks. Stocks with high information uncertainty generate profits from the MA timing strategy.”

To confirm their hypothesis, the authors use three proxies to measure information uncertainty and compare the performance of firms with different levels of information uncertainty:

1. **Idiosyncratic volatility**: The higher the idiosyncratic volatility, the higher the information uncertainty
2. **Firm age**: The younger the firm, the higher the information uncertainty.
3. **Number of analysts following**: Firms covered by fewer analyst tend to have more information uncertainty.

The results show that firms with higher information uncertainty (higher idiosyncratic volatility, younger age, covered by fewer analyst)  **benefit the most** from the simple MA rule. The authors suggest that this may be because the annual characteristics used to form the anomaly portfolios are *a less reliable signal* for these firms, than for firms with lower information uncertainty.

But there could be more bad news: It may be that firms with higher information uncertainty are also more costly and difficult to short.

Note:For a related post on how to simply incorporate trend-following into a strategy to enhance the benefits of investing in factor-based anomalies, check out our post on [creating an alternative investment strategy with value and momentum.](https://alphaarchitect.com/2016/07/07/creating-an-alternative-investment-strategy-with-value-and-momentum/) One can arguably achieve a same end-state with this approach, but save a lot of brain damage.

---

### Anomalies Enhanced: The Value of Higher Frequency Information

* Han, Huang and Zhou
* A version of the paper can be found [here](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2624650).
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category](https://alphaarchitect.com/category/academic-research/).

### Abstract:

> Many anomalies are based on low frequency attributes, such as annual characteristics, that ignore higher frequency information. In this paper, we provide a simple strategy to incorporate the higher frequency information. We find that there is significant economic value-added. For eight major anomalies, we find that the enhanced anomalies can double the average returns while having similar or lower risks. The results are robust to a number of controls.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | David Foulke got me a shirt related to this paper. The shirt can be summed up in one word: awesome. [hml-devilhttps://alphaarchitect.com/wp-content/uploads/2016/12/hml-devil.png 737w" sizes="(max-width: 500px) 100vw, 500px" />](https://alphaarchitect.com/wp-content/uploads/2016/12/hml-devil.png) |

 function footnote\_expand\_reference\_container\_22013\_171() { jQuery('#footnote\_references\_container\_22013\_171').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_22013\_171').text('−'); } function footnote\_collapse\_reference\_container\_22013\_171() { jQuery('#footnote\_references\_container\_22013\_171').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_22013\_171').text('+'); } function footnote\_expand\_collapse\_reference\_container\_22013\_171() { if (jQuery('#footnote\_references\_container\_22013\_171').is(':hidden')) { footnote\_expand\_reference\_container\_22013\_171(); } else { footnote\_collapse\_reference\_container\_22013\_171(); } } function footnote\_moveToReference\_22013\_171(p\_str\_TargetID) { footnote\_expand\_reference\_container\_22013\_171(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_22013\_171(p\_str\_TargetID) { footnote\_expand\_reference\_container\_22013\_171(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
