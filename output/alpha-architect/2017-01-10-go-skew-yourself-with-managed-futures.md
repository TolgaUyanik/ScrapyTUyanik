---
title: "Go Skew Yourself with Managed Futures"
slug: "go-skew-yourself-with-managed-futures"
date: "2017-01-10"
modified: "2017-01-10"
url: "https://alphaarchitect.com/go-skew-yourself-with-managed-futures/"
categories: ["Research Insights", "Trend Following", "Guest Posts", "Managed Futures Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Go Skew Yourself with Managed Futures

> Skewness is a statistical measure of how returns behave in the tails of a probability distribution. Wikipedia has a more robust definition of skewness with […]

Skewness is a statistical measure of how returns behave in the tails of a probability distribution. Wikipedia has a more robust definition of skewness with some good visuals [here](https://en.wikipedia.org/wiki/Skewness). If an investment (e.g., stocks) has negative skewness this means that the extreme returns are more likely to be negative than positive (it has a tendency to crash).  However, if its return has a positive skewness (e.g., buying a call option on stocks) then its large returns are more likely to be positive than negative.

When putting together a portfolio, all else equal, one should have a preference for positive skewness — avoid large negative losses and enjoy large positive gains.

[![Wes' attempt at humor](https://alphaarchitdev.wpengine.com/wp-content/uploads/2017/01/tailrisk-1030x402.png)](http://alphaarchitdev.wpengine.com/wp-content/uploads/2017/01/tailrisk.png)

Wes’ attempt at humor

But we face a problem as investors: stocks usually make up the lion’s share of risk in a portfolio and stocks have negative skewness.  But stocks aren’t the only negative skewness asset causing problems for portfolio managers looking to build a positive skew portfolio. Arguably, many asset classes exhibit negative skewness (B&H REITs, B&H HY bonds, B&H commodities, L/S equity, merger arb, and so forth). In fact, very few investments have positive skewness. And the investments that do possess this characteristic are expensive (e.g., the premium associated with buying call options).

One potential positive skew asset is trend-following managed futures. Managed futures have historically enjoyed positive skewness.  To understand why Managed Futures have positive skewness, watch this great TED talk by Kathyrn Kaminski, Ph.D. on convergent versus divergent strategies [here](https://www.youtube.com/watch?v=6vcxsJVBqIo).

Even though Managed Futures tend to have positive skewness (see my old piece [here](http://alphaarchitdev.wpengine.com/2016/08/24/managed-futures-understanding-a-misunderstood-diversification-tool/)), is there a way to increase their skewness and produce so-called [crisis alpha](http://alphaarchitdev.wpengine.com/2015/08/19/crisis-alpha-surprising-ways-to-hedge-stock-portfolio-risk/)? Kathryn thinks there might be a way to do so.

### Taming of the Skew

Dr. Kathyrn Kaminski (the same one as the TED talk, above) has been a prolific writer, researcher, and practitioner on the subject of Managed Futures.  She even co-authored a fantastic (and dense) [book](https://www.amazon.com/Trend-Following-Managed-Futures-Trading/dp/1118890973) on the subject.  I think one of Dr. Kaminski’s best works is a very unappreciated research [paper](http://www.valuewalk.com/wp-content/uploads/2016/06/The_Taming_of_the_Skew___Campbell__Company.pdf), co-authored with Brendan Hoffman,  called, “The Taming of the Skew.”

The point of this paper is to study how different Managed Futures risk allocation methods have an impact on the performance profiles of their fund (Sharpe ratio, Skewness, and Crisis Alpha).(1)

### Managed Futures Risk Allocation

Managed Futures funds use futures in making their investments and they managed them (har-har).  The use of futures contracts allows them to control how much volatility their fund exhibits by changing the mix of futures contracts and cash collateral.(2)

 If a managed futures fund wants to exhibit lower volatility, they simply hold more cash as collateral and if they want their fund to exhibit higher volatility, they simply use the cash to purchase more futures contracts.

The ability to explicitly control the volatility of the fund is a potential source of manager skill, return, and risk (as opposed to a stock fund manager who must passively accept whatever level of volatility that stocks exhibit).

“The Taming of the Skew” looks at three different ways that Managed Futures managers can choose to allocate their risk:

* **Constant Risk Target** – Always size futures contracts so that the fund exhibits a specific overall volatility level.  For example, the manager might want their fund to be as close as possible to a 10% annualized standard deviation risk level.  This is the most popular risk allocation method for Managed Futures mutual funds.
* **Signal Strength** – Size futures contracts in proportion to how strong the trend signal is for each future contract.  For example, if crude oil is exhibiting positive short-term, medium-term and long-term time horizons then crude oil would get a large risk allocation.  If lean hogs are exhibiting positive long-term trends but negative short-term trends then it might get a smaller risk allocation.
* **Equity Risk Targeting** – Size futures contracts so that the volatility of the Managed Futures fund matches the level of the VIX.  For example, if VIX were at 10 then the Managed Futures fund would target a 10% annualized volatility.  If the VIX were at 40 then the Managed Futures fund would target a 40% annualized volatility.

### Taming of the Skew Conclusion

Dr. Kaminski and Dr. Hoffman found that Constant Risk Targeting (the most popular risk allocation method for Managed Futures funds) produced the highest Sharpe Ratio (i.e., it looks the best when graphed by itself), but had the smallest positive skew, the smallest crisis alpha, and the highest correlation (although slightly negative) to the S&P 500.  Said another way, Constant Risk Targeting looks good on a stand alone basis but doesn’t do as much as it could/should to diversify a stock portfolio.

Alternatively, Equity Risk Targeting produced the second-best Sharpe Ratio, second highest skewness, largest crisis alpha, and most negative correlation to the S&P 500.  Said another way, Equity Risk Targeting still looks pretty good on a stand alone basis, but does a lot more for portfolio diversification.

### Practical Problem With Taming of the Skew and a Simple Solution

Most of us aren’t portfolio managers at a Managed Futures fund, which means that we don’t have the ability to change the volatility target of the Managed Futures funds that we use on a daily, weekly, monthly or yearly basis.  This means that most investors don’t have the ability to implement the Equity Risk Targeting solution that Drs. Kaminski and Hoffman discussed.

Fret not, as I want to propose a simple solution that arrives at a similar result.  The solution starts with understanding volatility clustering.(3)

The jist of volatility clustering is that when the stock market gets volatile it tends to stay volatile for some period of time.  This means that if we know when stocks are likely to be volatile we can simply take some measures to make the portfolio less aggressive and therefore less volatile.

Trend following on stocks has been a good way to [avoid drawdowns](http://alphaarchitdev.wpengine.com/2015/08/13/avoiding-the-big-drawdown-downside-protection-investment-strategies/), historically, but trend following might also be able to differentiate volatility regimes in stocks and help us better allocate risk to Managed Futures.

Let’s put this idea to the test.

### Hypothesis

When stocks are trending up they will be in a low volatility regime, and when stocks are trending down, they will be in a high volatility regime.

* Trend is positive = volatility is low = want less volatile Managed Futures and more stocks
* Trend is negative = volatility is high = want more volatile Managed Futures and less stocks

### Data Series

I use the MKT-Rf data stream from 7/1926 through 8/2016 for the trend following test (which is available from [AQR](https://www.aqr.com/library) or Ken French’s [website](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)). The returns are total returns and include dividends and distributions.

The trend following signal for stocks is going to be [absolute momentum](http://alphaarchitdev.wpengine.com/2015/03/31/absolute-momentum-and-stock-momentum-strategies-friends-not-enemies/).  Absolute momentum is defined by the sum of the prior 12 month’s return from MKT-Rf.  If the prior 12 months’ return for the MKT-Rf is positive then the trend is positive and vice versa.

I am going to use the returns for the Barclays Top 50 CTA index (BTop50) as a rough proxy for the return of trend-following managed futures funds.  Information on the index can be found [here](http://www.barclayhedge.com/research/indices/btop/).  I am also going to create a BTop50 High Volatility index, which will be the same excess return (BTop50 total return minus the return of cash) but leveraged 50% so that it is 50% more volatile (i.e., 15% annualized volatility level).  
We will define Crisis Alpha as the return of Managed Futures in the same month where the MKT-Rf factor had a loss of 5% or worse.

Total returns for stocks is the sum of the return for the MKT-Rf risk factor plus the return of cash.

### Does Trend Following Split Volatility Regimes?

In the first test, we examine if trend following on stocks is able to differentiate between volatility regimes.  We use absolute momentum on the MKT-Rf risk factor (as described above) and note the differences in the two regimes via the table below:

![volatility-regimes](https://alphaarchitect.com/wp-content/uploads/2016/12/Volatility-Regimes.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

You can tell from comparing the results in the table, above, that the volatility when the trend is positive (15.84%) is materially less than the volatility when the trend is negative (23.52%). For the statistically inclined this gives an F-Test value of 1718 which is very statistically significant.

This tells us that trend following can help differentiate between a low volatility regime (trend is positive) and a high volatility regime (trend is negative).

### Using Stock Trend Signal to Determine Managed Futures Risk Level

For this next test, we are going to attempt to replicate the effects Equity Risk Targeting strategy shown by Dr. Kaminski, but do it in a more simple way:

* If stock trends are positive then own the BTop50 index (index has a 10% volatility)
* If stock trends are negative then own the BTop50 High Volatility index (Synthetic index that is the BTop50 index but at a 50% higher volatility level)

Switching between the same index at different volatility levels is meant to represent selling a lower volatility Managed Futures fund and owning a higher volatility Managed Futures fund. Because indices don’t have different volatility levels, we attempt to replicate the strategy by creating our own high volatility Managed Futures fund.

The performance table for the BTop50 index, Btop50 HV, and the BTop50 Switch index is below:

![btop50-switch](https://alphaarchitect.com/wp-content/uploads/2017/01/BTop50-Switch.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

What we see from the switching strategy is that it provides two very attractive benefits:

1. Improved long-term return and Sharpe ratio
2. Provides almost the same crisis alpha as the higher volatility Managed Futures fund, but at a much lower overall volatility level (12% compared to 15%).

This isn’t the same type of enhancement that Dr. Kaminski shows in her research article, but its a step in the right direction and the improvement in Crisis Alpha (diversification when you actually want diversification) may make the simple strategy just as effective when combined in a portfolio with stocks.

### Combining Trend Following on Stocks with Managed Futures Switching Strategy

Now we are going to combine the two tools we have discussed in this post (trend following on stocks and managed futures volatility switch) and see if the combination can meaningfully improve risk characteristics for portfolios.  I call the combination of the two ideas the “Skew Yourself” portfolio.

To test if the Skew Yourself portfolio actually improves risk characteristics, we are going to examine two other portfolios:

* 80% US stocks (MKT-Rf risk premium plus cash return) and 20% BTop50 index.  The portfolio is rebalanced monthly.
* 80% US stocks (MKT-Rf risk premium plus cash return) and 20% BTop50 high volatility index.  The portfolio is rebalanced monthly.
* Skew Yourself Portfolio:
  + When stock trends are positive this portfolio owns 80% US stocks (MKT-Rf risk premium plus cash return) and 20% BTop50 index.  The portfolio is rebalanced monthly.
  + When stock trends are negative this portfolio owns 70% US stocks (MKT-Rf risk premium plus cash return) and 30% BTop50 high volatility index.  The portfolio is rebalanced monthly.

The results table is below:

![combined-portfolio](https://alphaarchitect.com/wp-content/uploads/2017/01/Combined-Portfolio.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

The first thing that strikes me is that at a portfolio level (stocks combined with Managed Futures) there isn’t much difference between a dedicated 20% allocation to the BTop50 and a dedicated 20% allocation to the BTop50 high volatility (BTop50 at a 50% higher volatility level).  I was very surprised to see this result as I would have expected much better risk statistics from the dedicated allocation to BTop50 high volatility.

The second thing that strikes me is the improvement in the Skew Yourself portfolio, especially given the relatively minor changes (Skew Yourself and Stocks & Btop50 are different only 30% of the time, when absolute momentum is negative, and in the 30% of the time they are different Skew Yourself only owns 10% less stocks and owns a more volatile Managed Futures fund).

Skew Yourself portfolio has:

* increased CAGR
* decreased volatility
* improved Sharpe ratio
* improved maximum drawdown
* improved the sum of all drawdowns
* has improved the skewness over Stocks & BTop50
* has improved the crisis alpha over Stocks & BTop50

Not bad. The two simple uses of trend following in the Skew Yourself portfolio certainly seems to lead to similar results as the more complex solution proposed by Dr. Kaminski.

### Conclusion

Dr. Kaminski and Dr. Hoffman have published some great research about Managed Futures funds that could help improve the performance and risk profiles of a portfolio of US Stocks and Managed Futures.

However, the methods she discusses aren’t practical for most investors.  I propose a simple solution to arrive at a similar results.  The small and infrequent changes that I propose do appear to improve returns and various risk metrics.

The trend of stocks can be useful in many different ways!

References[+]

References

|  |  |
| --- | --- |
| ↑1 | An example of this research is [here](http://alphaarchitdev.wpengine.com/2016/12/22/time-series-momentum-volatility-scaling-and-crisis-alpha/) |
| ↑2 | See [this piece](http://alphaarchitdev.wpengine.com/2016/12/21/commodity-investing-is-complex-and-volatile-but-unique/) for more information on future’s mechanics |
| ↑3 | Meb Faber has a great white paper on volatility clustering [here](http://seattletechnicaladvisors.com/images/Faber.pdf) and Yang has a discussion of the use of vol clustering in the context of stock simulation [here](http://alphaarchitdev.wpengine.com/2014/07/28/a-simulation-study-on-simple-moving-average-rules/). |

 function footnote\_expand\_reference\_container\_25894\_165() { jQuery('#footnote\_references\_container\_25894\_165').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_25894\_165').text('−'); } function footnote\_collapse\_reference\_container\_25894\_165() { jQuery('#footnote\_references\_container\_25894\_165').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_25894\_165').text('+'); } function footnote\_expand\_collapse\_reference\_container\_25894\_165() { if (jQuery('#footnote\_references\_container\_25894\_165').is(':hidden')) { footnote\_expand\_reference\_container\_25894\_165(); } else { footnote\_collapse\_reference\_container\_25894\_165(); } } function footnote\_moveToReference\_25894\_165(p\_str\_TargetID) { footnote\_expand\_reference\_container\_25894\_165(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_25894\_165(p\_str\_TargetID) { footnote\_expand\_reference\_container\_25894\_165(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
