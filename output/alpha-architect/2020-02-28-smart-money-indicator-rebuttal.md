---
title: "Smart Money Indicator Rebuttal"
slug: "smart-money-indicator-rebuttal"
date: "2020-02-28"
modified: "2022-05-20"
url: "https://alphaarchitect.com/smart-money-indicator-rebuttal/"
categories: ["Relative Sentiment", "Research Insights", "Trend Following", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Smart Money Indicator Rebuttal

> In February 2019, Wes asked that I share my research on what I call the “Smart Money Indicator.” I did a guest post on the […]

In February 2019, Wes asked that I share my research on what I call the “Smart Money Indicator.” I did a guest [post](https://alphaarchitect.com/2019/02/08/relative-sentiment-a-unique-market-timing-tool-that-isnt-trend-following/) on the subject that summarized the results of a [paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3164081) introducing my research on the topic. The indicator measures the *relative* sentiment in equities between institutional investors and individual investors. The metric is formed using the information on how each class of investors is positioned in the futures and options markets.

In particular, the SMI comprises data not only on how investors are positioned in equities, but also on how they are positioned in long-duration bonds and along the yield curve (it turns out this so-called “cross-hedging pressure(1)” is an important ingredient in the SMI’s construction).  The resulting composite indicator quantifies whether institutions are leaning bullish or bearish in equities relative to individuals. (And the reason we are interested in how institutions are positioned relative to individuals in the first place is that institutions tend to outperform individuals over intermediate time horizons(2)(3)(4).)

As discussed in the original paper and the Alpha Architect blog post, the SMI has exhibited some unique and interesting characteristics with respect to market timing, momentum timing, factor timing, cross-sectional equity index selection, and tactical asset allocation (and in subsequent but not yet published research, value timing as well).

For details on those characteristics, we refer you to those original sources as well as to a more recent [paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3475258)(5) on survey-based relative sentiment that corroborates many of the findings of the SMI paper.

We are revisiting the SMI concept because on Friday, February 21st, 2020 CXO Advisory (CXOA) published an article entitled [‘Verification Tests of the Smart Money Indicator [SMI]’](https://www.cxoadvisory.com/sentiment-indicators/verification-tests-of-the-smart-money-indicator/) in response to a request from one of their subscribers to verify the indicator’s historical performance.

First, we would like to thank CXOA for their coverage of the indicator. We respect and appreciate the role they play in independently verifying proposed systematic strategies. And while, in general, the article in question was positively disposed towards the SMI, CXOA’s verification process, unfortunately, **used the wrong dataset** to compute the indicator. Consequently, the output on which they based their review was not a faithful representation of the SMI as described in the original paper. As a result, CXOA’s subsequent conclusions are somewhat misguided.

## **COT DATA**

The data used to compute the SMI comes from the Commitments of Traders (COT) report, released by the Commodities Futures Trading Commission (CFTC) every Friday at 3:30 p.m. Eastern Time. The report is a snapshot of traders’ positions in the futures and (futures) options markets as of every Tuesday. The CFTC releases two types of reports, a *legacy* report and a *disaggregated* report.

The legacy report classifies traders as one of three different categories: Commercial, Non-Commercial, or Non-reportable. Commercial traders are defined as those that use the derivatives markets to hedge business risk. Non-Commercial traders are defined as those that use the derivatives markets for speculative purposes. While Non-Reportable traders are those that have position sizes below the reporting threshold.

For purposes of computing the SMI, we are interested in the positions of the Commercial traders (institutions) and the Non-Reportable traders (individuals). When institutions use the derivatives markets to hedge their equity and bond portfolios, their aggregate positioning across equities, long-duration bonds, and along the yield curve provides a window into how they view the state of corporate and economic fundamentals. The legacy report gives us a clean separation between firms that hedge and firms that speculate.

In contrast, the disaggregated COT report breaks down large
traders (i.e., Commercials and Non-Commercials) into four separate categories:
Dealers, Asset Managers, Leveraged Funds, and Other Reportable Traders.
Unfortunately, this report **does not** provide a clean separation between
hedgers and speculative traders.

We know this because there is no obvious formula to map the positions presented in the disaggregated report to the positions provided in the legacy report—i.e., there is at least some conflation between hedgers and speculative traders in the disaggregated report.

In addition to this conflation, the disaggregated report has
a much shorter history with which to test its validity (it goes back only to
2006), whereas the (weekly) legacy report goes back to 1992.

Further, the disaggregated report is potentially subject to a subtle lookahead bias. When the CFTC first started releasing the disaggregated report in September 2009, it created Pro-forma disaggregated reports back to 2006. When it did this, because it does not maintain historical records of its classifications of large traders, the CFTC used its 2009 classifications and applied those back through time. Thus, if any trading firms had migrated between classifications from 2006 to 2009, some early reports will have been distorted.

When attempting to verify the SMI, CXOA used the disaggregated COT report rather than the legacy report and then used only the Asset Manager positions to represent institutions. If one compares the Asset Manager positions (in the S&P 500 Stock Index, the U.S. Treasury Bond, and the 10-Year Treasury Note) in the disaggregated report to the Commercial positions in the legacy report, one sees that the Asset Manager positions represent only a fraction of the total Commercial positions.

![](https://alphaarchitect.com/wp-content/uploads/2020/02/image-19-800x779.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

The Asset Manager bond positions (US and TY) seem to range
between 40% and 60% of the total Commercial positions, while the Asset Manager
S&P 500 positions have steadily been declining the past 15 years. Given the
discrepancies between the Asset Manager and Commercial positions illustrated in
the chart above, it’s not surprising there are meaningful discrepancies in SMI performance
between those respective COT reports.

To quantify these discrepancies in performance, we consider
a strategy that goes long the U.S. equity market when the SMI is positive and
is in cash otherwise. We begin the computations for this strategy from the
start date of the disaggregated COT report, June 13, 2006. We run this strategy
across all of the SMI parameter combinations used in the original paper (i.e.,
z-score lookbacks of 39, 52, 65, 78, 91, and 104 weeks, and extremum lookbacks
from 1 to 13) and present the annualized returns, Sharpe ratios, and maximum
drawdowns for both the legacy and disaggregated COT reports, along with the
differences between them. We do not lag the SMI data for this illustration (i.e.,
we use a 0-week SMI lag).

(Note: the strategies across the parameter grid have different start dates due to different combinations of lookbacks—a SMI strategy with a z-score lookback of 39 and an extremum lookback of 1 will start much earlier in time than a strategy with a z-score lookback of 104 and an extremum lookback of 13. On top of those lookbacks, we also use a 52-week burn-in period to compute the median of the SMI composite z-score against which the SMI composite z-score is compared to determine whether the SMI is positive or negative. The earliest strategy begins on February 29, 2008, and the latest begins on August 21, 2009.)

![](https://alphaarchitect.com/wp-content/uploads/2020/02/image-20-1200x446.png)

![](https://alphaarchitect.com/wp-content/uploads/2020/02/image-21-1200x440.png)

![](https://alphaarchitect.com/wp-content/uploads/2020/02/image-22-1200x451.png)

With respect to annualized returns, Table 1 indicates that
of the 78 different parameter combinations, the legacy-report SMI (LSMI)
outperforms the disaggregated-report SMI (DSMI) in 72 of them. The average
difference in annualized returns across the entire grid is 248 basis points.

For the set of parameters CXOA used in its verification attempt (M = 13, N = 52), the difference in annualized returns between the LSMI and DSMI is 434 basis points (12.45% vs. 8.11%). Below is a chart illustrating the cumulative discrepancy between the LSMI and DSMI for this parameter case over the time period in question:

![](https://alphaarchitect.com/wp-content/uploads/2020/02/image-18-800x680.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

As is evident from Figure 2, the legacy-report SMI has a much larger separation in cumulative returns between its positive and negative states (the black and purple lines) than the corresponding disaggregated-report SMI. **CXOA’s analysis was predicated on the returns of the green line, whereas the actual SMI for this parameter case corresponds to the black line**.

With respect to the Sharpe ratio, the LSMI outperforms in 75
of the 78 parameter cases with an average difference across the grid of 0.22. Similarly,
for maximum drawdowns, the LSMI has the same or lower maximum drawdown in 76 of
the 78 cases. The worst drawdown across the grid for the LSMI was -18.2%,
whereas the worst drawdown for the DSMI was -34.7%.

These results also hold when looking at 1- and 2-week lags of the SMI. The results for all cases are summarized in the table below:

![](https://alphaarchitect.com/wp-content/uploads/2020/02/image-23-800x474.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

As one can see, the performance of the legacy-report SMI relative to the disaggregated-report SMI is fairly consistent across each of the SMI lags, with the legacy-report SMI strongly outperforming across the parameter grid.

## **CXOA’s MISCONCEPTIONS ABOUT THE SMI**

Beyond the use of an incorrect dataset, there were also two statements made in the CXOA article that we feel should be addressed (even though they were premised on incorrect outputs). The first commented on the lack of a linear relationship between the magnitude of the SMI and forward equity returns. And the second suggested that the superior performance of the 1-week lag SMI (which they observed in their verification process using only one set of parameters) might be the result of data snooping.

> **Statement 1:** “While the average [forward equity] return for [SMI] decile 1 is lowest, there is no systematic progression across deciles. Decile 8 is highest, but decile 7 is second lowest, decile 9 is below average and decile 10 is only fourth highest. Return variability also does not vary systematically across deciles. Lack of progression undermines confidence in the explanation of why SMI should be a good indicator.”

To be fair, the results they were basing this comment on were
faulty. Nonetheless, depending on the parameters that one uses to compute the
legacy-report SMI and the time period that one covers, one might still see
somewhat similar variability across deciles.

For example, if one uses a z-score lookback of 52 weeks, an extremum lookback of 7 weeks, with a 1-week SMI lag, deciles 6 through 10 have the five highest average returns, while deciles 1 through 5 have the five lowest—as one would like to see—although there is no linear progression across deciles.

![](https://alphaarchitect.com/wp-content/uploads/2020/02/image-24-600x663.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

However, if we were to use a z-score lookback of 104 weeks and an extremum lookback of 13 weeks, with no SMI lag,  we see that deciles 8 and 10 have the highest average returns (which again is encouraging), but deciles 1 through 3 have the next three highest returns, even though the SMI is the most negative in those deciles. What is going on in this case?

![](https://alphaarchitect.com/wp-content/uploads/2020/02/image-25-600x661.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

The results in Figure 4 stem from the fact that a) the indicator
in question (with lookbacks of 104 and 13 weeks) is very slow-moving and no
longer reasonably responsive to changes in investor positioning, and b) because
of its slow-moving nature the indicator was often left flatfooted during
periods when the market abruptly reversed course, such as after the 2016
election and after the December 2018 selloff.

For this reason, we would not advocate using such long lookback horizons (as they are well outside the ‘sweet spot’ of the SMI parameter grid). Moreover, we tend to view the SMI as a binary indicator, similar to time-series momentum—i.e., it’s either positive or it’s negative. One does not see a linear progression in average forward equity returns based on the deciles of momentum. Indeed, when momentum is at its most positive or its most negative, it’s often ripe for a reversal, as we can see from the figure below:

![](https://alphaarchitect.com/wp-content/uploads/2020/02/image-26-600x681.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

Thus, the statement ‘Lack of [linear] progression [across deciles] undermines confidence in the explanation of why SMI should be a good indicator,’ seems unwarranted, especially when a) such a criterion is not particularly relevant for a binary indicator like time-series momentum or the SMI, and b) only one parameter combination was investigated.

> **Statement 2:** “The sharpness of improvements for a 1-week lag, in the absence of a behavioral explanation for its superiority, raises concern that this lag is just very lucky.”

Context: CXOA tested three different SMIs corresponding to
three different lags of the (disaggregated) COT data—a 0-week lag, a 1-week
lag, and a 2-week lag. For the particular set of lookback parameters CXOA used,
the 1-week-lag SMI substantially outperformed the other two lags in a strategy
that switched between SPY and TLT depending on whether the SMI was positive or
negative.

In the same vein, CXOA later commented, “Variability in weekly relative performance is large,
suggesting considerable susceptibility to scenario/data snooping bias and aggravating concern that
a 1-week lag in signal execution is lucky.”

(Again, we do acknowledge that these statements were
premised on faulty outputs stemming from faulty inputs. However….)

In the original paper, we took extensive measures to
demonstrate the robustness of the SMI and to account for data snooping across
all of our tests—whether they involved market timing, momentum timing, factor
timing or our tactical asset allocation strategy. The results did show that, in
terms of statistical significance, a 1-week-lag SMI slightly outperformed a 0-week-lag
SMI over 20-plus years of history—but only at the margins. The results were
virtually indistinguishable between the two cases.

However, the reason we used a 1-week lag for our primary
results had nothing to do with cherry-picking the best performing indicator.
Rather it was entirely due to practicality.

As aforementioned, the COT report is released every Friday
at 3:30 p.m., only 30 minutes before the close of trading. It was not released
in a machine-readable format until the mid-2000s.

Thus, for much of the time period covered by our analysis,
one would not have been able to trade on the COT information immediately (and
would have had to wait at least until Monday).

As Friday-to-Friday returns are much more commonly used than
Monday-to-Monday returns, we simply lagged the SMI by one week to account
conservatively for the time it would have taken to access and process the data.

That being said, if a 1-week-lag SMI were to outperform in a
meaningful sense, there might be behavioral reasons to explain such a
phenomenon.

For instance, while there is much prior research that shows institutions outperform individuals over intermediate time horizons, there is also some research that shows institutions underperform individuals over short time horizons(6).

One explanation for the latter might be that institutions control significant amounts of capital and thus need to scale into and out of positions. That is, they gradually buy into falling markets and gradually sell into rising markets, and in the short-run those markets could keep moving against them. A 1-week-lag SMI might unwittingly capture some of those short-term dynamics given that institutions are unlikely to time the precise highs or lows of market movements. Thus, waiting one week (or even just a few days) might conceivably offer better entry or exit opportunities than acting immediately.

Moreover, because CXOA tested a strategy that was long
equities when the SMI was bullish and long TLT when the SMI was bearish, they
introduced a second moving part into the equation. It might be the case that the
equity leg of such a strategy performs better with no lag, but the TLT leg
performs better with a 1-week lag—as equity and bond dynamics are markedly
different.

We tested this idea using the legacy COT data and discovered
that for some parameter cases the 0-lag SMI strategy that switched between equities
and cash outperformed the corresponding 1-lag SMI strategy, but the 0-lag SMI
strategy that switched between equities and TLT *underperformed* the corresponding
1-lag SMI strategy—indicating that the introduction of the TLT leg had
repercussions for overall performance.

This dynamic is illustrated in the chart below, where we see that the red line (Equity-TLT strategy, 1-week SMI lag) outperforms the green line (Equity-TLT strategy, 0-week SMI lag), but the black line (Equity-Cash strategy, 0-week SMI lag) outperforms the purple line (Equity-Cash strategy, 1-week SMI lag):

![](https://alphaarchitect.com/wp-content/uploads/2022/04/imagedsd-27-1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

Yet another possible explanation for a 1-week lag outperforming a 0-week lag is that if one looks at only one parameter combination—as CXOA did—anything could happen. Below we reproduce the annualized return table for the 0-week lag SMI (presented above) and include the same table for the 1-week lag SMI, and then show their differences.

![](https://alphaarchitect.com/wp-content/uploads/2020/02/image-28-1200x434.png)

From Table 5, we see that the 0-week lag SMI has a higher
annualized return in 49 of the 78 parameter cases. That is, it *tends* to
outperform, but not always. Thus, for no other reason than sheer noise, a
1-week-lag SMI could conceivably outperform a 0-week-lag SMI depending on one’s
choice of parameters.

For example, if one were to use parameters on the ‘faster’
side of the SMI’s ‘sweet spot,’ waiting a week to execute would probably be
beneficial. Whereas if one were to use parameters on the ‘slower’ side of the
sweet spot, immediate execution would probably be better.

Indeed, if we look at the distribution of outperformance of the 0-week lag relative to the 1-week lag in Table 5c, we see that the 0-week lag outperforms less in the first three columns of the table than it does in the last three columns, and it outperforms less in the first six rows than it does in the last six. That is, in the upper left quadrant (i.e., the faster side of the parameter-grid sweet spot), the 1-week lag does relatively better; in the lower right (i.e., the slower side of the sweet spot), the 0-week lag does relatively better.

In reality, when using the legacy COT data, there does not
appear to be any meaningful, systematic superiority of a 1-week lag relative to
a 0-week lag that would need explanation.

Nor was our use of a one-week lag anything other than an acknowledgment that for a substantial portion of its history, the COT data would not have been available for immediate trading. No attempt was made to cherry-pick the best performing indicator.

But(!) for any given parameter combination, there could be a myriad of reasons—that having nothing to do with data snooping—as to why a 1-week lag outperforms a 0-week lag. Thus, CXOA’s raising the specter of data snooping—while looking at only one parameter combination and without considering other possibilities—seems unjustified.

## **Conclusion**

While CXOA should certainly be lauded for the work they are doing in independently verifying systematic indicators to help guide and protect investors, in the case of their verification attempt of the SMI, they appear to have fallen short in creating a faithful representation of the indicator. We would like to thank Alpha Architect for providing us this platform to help clarify the record.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | de Roon, Frans A., Theo E. Nijman, and Chris Veld, 2000, Hedging pressure effects in futures markets, The Journal of Finance 55, 1437–1456. |
| ↑2 | Schmeling, Maik, 2007, Institutional and individual sentiment: Smart money and noise trader risk?, International Journal of Forecasting 23, 127–145. |
| ↑3 | Grinblatt, Mark, and Matti Keloharju, 2000, The investment behavior and performance of various investor types: a study of finland’s unique data set, Journal of Financial Economics 55, 43–67. |
| ↑4 | Gibson, Scott, Assem Safieddine, and Ramana Sonti, 2004, Smart investments by smart money: Evidence from seasoned equity offerings, Journal of Financial Economics 72, 581–604.[ref]Gibson, Scott, and Assem Safieddine, 2003, Does smart money move markets?, The Journal of Portfolio Management 29, 66–77. |
| ↑5 | Micaletti, Raymond, Relative Sentiment and Machine Learning for Tactical Asset Allocation (October 25, 2019). Available at SSRN: <https://ssrn.com/abstract=3475258> |
| ↑6 | Campbell, John Y. and Vuolteenaho, Tuomo and Ramadorai, Tarun, Caught on Tape: Predicting Institutional Ownership with Order Flow (October 2004). Harvard Institute of Economic Research Discussion Paper No. 2046; EFA 2004 Maastricht Meetings Paper No. 4242. Available at SSRN: <https://ssrn.com/abstract=519882> or [http://dx.doi.org/10.2139/ssrn.519882](https://dx.doi.org/10.2139/ssrn.519882) |

 function footnote\_expand\_reference\_container\_55346\_196() { jQuery('#footnote\_references\_container\_55346\_196').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_55346\_196').text('−'); } function footnote\_collapse\_reference\_container\_55346\_196() { jQuery('#footnote\_references\_container\_55346\_196').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_55346\_196').text('+'); } function footnote\_expand\_collapse\_reference\_container\_55346\_196() { if (jQuery('#footnote\_references\_container\_55346\_196').is(':hidden')) { footnote\_expand\_reference\_container\_55346\_196(); } else { footnote\_collapse\_reference\_container\_55346\_196(); } } function footnote\_moveToReference\_55346\_196(p\_str\_TargetID) { footnote\_expand\_reference\_container\_55346\_196(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_55346\_196(p\_str\_TargetID) { footnote\_expand\_reference\_container\_55346\_196(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
