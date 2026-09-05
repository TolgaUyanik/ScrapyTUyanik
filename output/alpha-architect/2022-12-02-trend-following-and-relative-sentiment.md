---
title: "Trend Following and Relative Sentiment: Complementary Factors"
slug: "trend-following-and-relative-sentiment"
date: "2022-12-02"
modified: "2022-11-30"
url: "https://alphaarchitect.com/trend-following-and-relative-sentiment/"
categories: ["Relative Sentiment", "Research Insights", "Larry Swedroe", "Trend Following"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Trend Following and Relative Sentiment: Complementary Factors

> Since it is likely that both the Relative Sentiment and Trend Following strategies will underperform at some points in the future, “a 50-50 combination of TF and RS might reduce the emotional volatility an investor may experience from holding only the underperforming strategy.”

Trend following ([time series momentum](https://alphaarchitect.com/2018/02/time-series-momentum-aka-trend-following-the-historical-evidence/)) is one of the most well-documented and well-known factors in investing, demonstrating persistence, pervasiveness, robustness, and implementability (survives transaction costs). Lesser well-known is relative sentiment—an indicator that measures the positions, flows, and attitudes of institutional investors compared to those of individual investors. The research has found that “relative sentiment demonstrates statistically and economically significant predictive power across different regions, periods, and datasets—even after adjusting for data-snooping.” The hypothesis supporting the findings is that institutions are informed traders, while individuals are “noise traders” who experience mostly unfavorable outcomes.

Raymond Micaletti, author of the October 2022 study “[The Complementarity of Trend Following and Relative Sentiment,](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4235609)” investigated the complementary nature of trend following and relative sentiment for equities. He noted that trend following had produced economically and statistically significant results over the long term and benefits from ensuring investors are fully invested during strong uptrends—the periods during which great fortunes can be made—and it prevents investors from riding assets to zero. But he also noted it does have some weaknesses, the most glaring of which are that it tends to stay in the market too long after the market has peaked (waiting for an exit signal and thereby relinquishing gains) and that it tends to stay out of the market too long after the market has bottomed out. These weaknesses can be seen in the chart below covering the U.S. equity market drawdown and recovery from July 17, 1998, through December 23, 1998. The green panels signify trend following is long equities and the red panel flat equities. Over this period, the 10-month moving average strategy rode the market down 20 percent and exited near the eventual trough. It then proceeded to sit on the sidelines while the market rallied 25 percent through the end of November before eventually reentering the market near the previous peak. During this episode, trend following sold low and bought high.

![](https://alphaarchitect.com/wp-content/uploads/2022/11/us-equity-market-800x812.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

It was this vulnerability that led Micaletti to “seek a complementary factor, one that could sidestep more of the market’s drawdown from the peak and capture more of its rise from the trough while not being too much of a drag when the market is trending strongly.” He hypothesized that relative sentiment could fit this prescription—adjusting allocations to a given asset based on whether institutions are more or less bullish on the asset relative to individuals. His hypothesis was based on these research findings:

* [Equity markets tend to have higher returns and lower volatility when relative sentiment is bullish](https://alphaarchitect.com/2019/02/relative-sentiment-a-unique-market-timing-tool-that-isnt-trend-following/)—when institutions are more bullish than retail investors.
* [Relative sentiment has worked outside the U.S](https://alphaarchitect.com/2022/07/relative-sentiment-and-machine-learning-for-tactical-asset-allocation-out-of-sample-results/).
* [Relative sentiment has worked out of sample](https://alphaarchitect.com/2022/01/implied-secular-regime-change-evidence-from-relative-sentiment/).
* [Relative sentiment appears to provide more predictive power than time series momentum](https://alphaarchitect.com/2022/07/relative-sentiment-and-machine-learning-for-tactical-asset-allocation-out-of-sample-results/).

Micaletti noted that when momentum was positive (trend-following strategies are fully invested) but relative sentiment was bearish, such conditions tended to coincide with market peaks. Thus, in these instances, relative sentiment strategies tended to avoid more of the market’s subsequent drawdown compared to trend-following strategies. Conversely, when momentum was negative (trend-following strategies are out of the market) but the relative sentiment was bullish, equities tended to deliver their best, most-concentrated annualized returns, as rallies out of meaningful market troughs tended to be powerful. The result was that “relative sentiment appears as though it may be able to buffer trend following strategies during their weakest moments—by losing less on the way down and gaining more on the way back up.” The question remained whether relative sentiment would be too much of a drag on trend-following strategies during trend-following’s strongest periods—entrenched uptrends when trend-following strategies are fully invested.

Micaletti’s data sample covered the period November 1994-August 2022. The relative sentiment (RS) indicator was an equally weighted composite of three RS signals as they became available: November 1994 (a composite of five underlying RS signals from the nonequity assets of crude oil, natural gas, British pound, euro and two-year bond), November 1998 (a tactical asset allocation strategy, based on Micaletti’s prior research, adjusted for secular changes in equity-bond correlations) and September 2002 (Sentix-based RS with machine learning). Each indicator represented the desired equity allocation between 0 and 100 percent. The first two indicators had weekly frequencies (driven by the [Commitments of Traders report](https://www.cftc.gov/MarketReports/CommitmentsofTraders/AbouttheCOTReports/index.htm)), while the third had a monthly frequency (driven by [Sentix relative sentiment](http://www.sentix.de/index.php/en/item/sntm.html)). Equity allocations were refreshed on a weekly basis but updated only if they deviated from the current equity allocation by more than 10 percentage points. The portion of the portfolio not invested in equities was invested in an aggregate bond index. For the trend following (TF) strategy, he first examined six different implementations:

1. A 200-day moving average strategy.
2. A 40-week moving average strategy.
3. A 10-month moving average strategy.
4. An 84- and 200-day dual momentum strategy.
5. A 17- and 40-week dual momentum strategy.
6. A 4- and 10-month dual momentum strategy.

Micaletti chose the 10-month moving average strategy as his representative TF strategy because it had a slight performance edge over the other five strategies during the time period tested. To maintain an apples-to-apples comparison with RS, anytime the TF strategy was out of the equity market, it invested in an aggregate bond index. He then examined the cumulative performance of RS, TF and a 50/50 combination of both (TFRS) over the following time-series partitions:

1. The full time period.
2. Peak-to-trough periods.
3. Trough-to-recovery periods.
4. Peak-to-recovery periods (i.e., the combination of periods 2 and 3).
5. Non-drawdown periods.

Following is a summary of his findings:

* The performance of RS and TF was quite similar.
* Although RS had a slight edge in absolute and risk-adjusted performance, a higher compound annual growth rate (CAGR) and Sharpe ratio, and a lower maximum drawdown, the strategies tracked each other closely—their correlation was 0.69.

![performance statistics](https://alphaarchitect.com/wp-content/uploads/2022/11/performance-stats-1-800x223.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

* A 50/50 combination of the strategies produced virtually the same return and Sharpe ratio as RS while having thinner tails (lower excess kurtosis) than either TF or RS, suggesting some complementarity between the two strategies.
* RS held up slightly better than TF during peak-to-trough periods (losing 60 percent versus 66 percent for TF). While TF had a lower average equity exposure than RS during these periods, it initially started out with much higher equity exposure (100 percent), which eventually went to zero as the market proceeded to the trough. The correlation between RS and TF during these times fell to 0.45.

![peak to trough](https://alphaarchitect.com/wp-content/uploads/2022/11/peak-trough-1-800x222.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

Overall trough-to-recovery periods, RS generated 2.3 times the total return of TF from troughs to recoveries (856 percent versus 371 percent). RS gained a 27.9 percent annualized rate compared to 16.2 percent for TF. The 50/50 combination strategy captured approximately 1.5 times the total return of TF (appreciating at a 22.1 percent annualized clip).

![trough to recovery](https://alphaarchitect.com/wp-content/uploads/2022/11/trough-recovery-1-800x209.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

During the market’s round trip from peak-to-trough-to-prior-peak, RS generated approximately 2.6 times the total return of TF (421 percent to 165 percent), appreciating at an annualized rate of 10.6 percent compared to 3.6 percent for TF.

![peak to recovery](https://alphaarchitect.com/wp-content/uploads/2022/11/peak-to-recovery-1-800x218.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

TF performed best when the market was not in peak-to-recovery mode—when the equity market was moving higher without meaningful pullbacks. During these intervals, TF behaved essentially the same as the market, having a 98.6 percent average equity allocation and a CAGR of 24.5 percent (compared to 25 percent for the market). In contrast, RS had a 59.3 percent allocation to equities during these periods and a CAGR of 16.9 percent—highlighting one of the weaknesses of RS, not being fully invested in equities during strong uptrends. While RS outpaced TF by 2.6 times during peak-to-recovery periods, TF closed the gap during non-drawdown periods, outperforming RS by 2.2 times. Note that the combo strategy achieved a respectable middle ground during these non-drawdown periods. It had a 78.9 percent average allocation to equities, a 20.8 percent CAGR and a Sharpe ratio of 1.62, the highest of the three strategies.

![outside peak to recovery](https://alphaarchitect.com/wp-content/uploads/2022/11/outside-peak-to-recovery-1-800x218.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

Micaletti also examined the equity allocations through time of the RS, TF, and TFRS factors and found:

* At peaks, TF had an average equity allocation of 100 percent versus the RS average equity allocation of 49.9 percent—RS started off each drawdown at an advantage relative to TF.
* Four weeks post peak, TF still tended to be fully invested in equities, with an average equity allocation of 88.9 percent (at four weeks past the peak, TF was fully invested in eight of nine cases), while RS saw its average equity allocation decrease to 45.0 percent by this time.
* Closer in time to a trough, TF had largely exited the market. For example, at two weeks before the trough, TF had an average equity allocation of 11.1 percent (it had exited equities in eight out of nine cases), while RS held its allocation roughly steady, at 48.7 percent.
* One week before a trough, the allocations of both RS and TF remained roughly constant from the prior week, 46.7 percent and 11.1 percent, respectively.
* At a trough, RS began to increase its equity allocations—moving from an average of 46.7 percent one week before 57.9 percent at the trough. It then steadily increased its exposure in subsequent weeks, such that by eight weeks past the trough, RS had reached an average equity allocation of 68.3 percent—a larger equity allocation than its average across all periods. In contrast, TF was slow to reallocate to equities. By six weeks past a trough, TF had an average equity allocation of just 25 percent (it had reentered the market in only two of eight cases).
* At eight weeks past a trough, TF’s mobilization was a little better, having reallocated to equities in only four of eight cases. This slowness to reallocate to equities on the part of TF—more so than its slowness to exit after the peak—was the main driver of its underperformance.

His findings led Micaletti to conclude: “From the perspective of a TF investor, about half of the time market conditions are ripe for the strategy, and the other half they can be anguishing—giving back gains from market peaks and missing out on gains after market troughs. The opposite perspective holds for an investor in RS. About half of the time, RS thrives by taking advantage of the volatility surrounding drawdowns to sell high and buy back low, whereas the other half lags by not being fully invested during strong uptrends. Therefore, investors in one or the other might routinely see their emotions fluctuate between euphoria and despair depending on market conditions.” He added that the 50/50 combination strategy had the lowest tracking error to a perfect-foresight strategy. Thus, since both the RS and TF strategies will likely underperform at some points in the future, “a 50-50 combination of TF and RS might reduce the emotional volatility an investor may experience from holding only the underperforming strategy.”

## **Investor Takeaways**

The research demonstrates that both TF and RS strategies have added value over the long term. And while the overall performance of TF and RS across the full time period (November 1994- September 2022) tracked each other closely, TF strongly underperformed during drawdown periods (slow to lower its equity allocation after a peak and especially slow to raise its equity allocation after a trough) and strongly outperformed otherwise. Conversely, RS outperformed during drawdown periods by having a lower equity allocation at the peak and holding that lower allocation steady on the way to the trough. It then raised its equity allocation quickly at the trough and continued to raise it in subsequent weeks. Micaletti showed that, historically, a simple 50/50 combination of TF and RS appeared to provide similar returns to the top-performing RS strategy but did so with thinner tails of the return distribution. It also had the lowest tracking error to a perfect-foresight strategy. Thus, a hybrid portfolio may reduce emotional volatility relative to the ups and downs experienced by TF-only or RS-only investors.

Micaletti’s finding should not be surprising, as ensemble strategies that are not perfectly correlated tend to perform better than any single strategy because they provide diversification benefits. It is why fund families such as Alpha Architect, AQR, Avantis, and Bridgeway use multiple signals for their value and momentum strategies rather than using one single “best” metric.

*Larry Swedroe is head of financial and economic research for Buckingham Wealth Partners and Buckingham Strategic Wealth, a community of more than 140 independent* *registered investment advisors throughout the country.*

*For informational and educational purposes only and should not be construed as specific investment, accounting, legal, or tax advice. Certain information is based upon third party data which may become outdated or otherwise superseded without notice. Third party information is deemed to be reliable, but its accuracy and completeness cannot be guaranteed. By clicking on any of the links above, you acknowledge that they are solely for your convenience, and do not necessarily imply any affiliations, sponsorships, endorsements or representations whatsoever by us regarding third-party websites. We are not responsible for the content, availability or privacy policies of these sites, and shall not be responsible or liable for any information, opinions, advice, products or services available on or through them. The opinions expressed by featured authors are their own and may not accurately reflect those of Buckingham Strategic Wealth® or Buckingham Strategic Partners®, collectively Buckingham Wealth Partners. Neither the Securities and Exchange Commission (SEC) nor any other federal or state agency have approved, determined the accuracy, or confirmed the adequacy of this article. LSR-22-402*
