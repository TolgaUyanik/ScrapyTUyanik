---
title: "Payday Anomaly Revisited"
slug: "payday-anomaly-revisited"
date: "2019-01-08"
modified: "2022-05-17"
url: "https://alphaarchitect.com/payday-anomaly-revisited/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Payday Anomaly Revisited

> Unless you are a die-hard buy-and-hold investor, chances are that you need to rebalance your portfolio at some point. The question is when? And how […]

Unless you are a die-hard buy-and-hold investor, chances are that you need to rebalance your portfolio at some point.

The question is when? And how often? And why at a specific time? Some strategies rebalance once a year, some multiple times a day.

What if there were better times to rebalance? Last thing you want is to rebalance on a highly volatile day like August 31, 1998 and deal with a -6.5% drop, right? What if, on the contrary, there were no better or worse day to rebalance, hence accepting the fact that it’s purely random?

In order to address these questions, we will start by reviewing the findings of a very interesting and recent paper called the “[Payday Anomaly](https://poseidon01.ssrn.com/delivery.php?ID=840017005024119074097110101115115069035015009020000075110100084096007028074120013010028032100126054048009107101116093068116080055044090011064096011015117114083073026090054017012009117015070108012006007083113004104096117097120070101098023004000086020104&EXT=pdf)” by Aixin Ma and William Pratt.

Next, we will compare its results to different data sets, from Fama-French to actual index funds.

Finally, we will focus on the days that show stronger returns, including actual end-of-the-month days as well as days 1, 2, and 16.

The main goal here is to present some analysis so that readers can decide whether there might be better days to rebalance.

## Show Me the Data

The “[Payday Anomaly](https://poseidon01.ssrn.com/delivery.php?ID=840017005024119074097110101115115069035015009020000075110100084096007028074120013010028032100126054048009107101116093068116080055044090011064096011015117114083073026090054017012009117015070108012006007083113004104096117097120070101098023004000086020104&EXT=pdf)” paper explores the possible turn-of-the-month anomaly.

Here is an extract from the conclusion:

> *The 16th day systematically outperforms the other calendar days, except two other paydays, the 1st and the 2nd days of the month. This confirms our hypothesis that semi-monthly pay system contributes to detectible abnormal returns not only at the turn of the month, but in the middle of the month as well.*

First, let’s see if we can reproduce the findings by using the same [SPX Yahoo Finance](https://ca.finance.yahoo.com/quote/%5EGSPC/history?period1=-630950400&period2=1540796400&interval=1d&filter=history&frequency=1d), from January 3, 1950 to March 19, 2018, totalling 17,156 days.

Using a similar pivot function, we are able to sort by calendar days, showing average daily returns next to the averages of the paper, followed by a difference column, if any:

[![](https://alphaarchitect.com/wp-content/uploads/2018/11/compday2-600x581.png)](https://alphaarchitect.com/wp-content/uploads/2018/11/compday2.png)

By looking at the last column that represents the difference between our data and the paper’s data, everybody would agree that we were able to reproduce the same averages over the same period. Yes, on average, day 16 outperforms the other calendar days, except the 1st and 2nd day of the month.

Great, we’ve confirmed the core findings from the paper.

## Fama-French Comparison

Now, because we are a curious bunch, let’s see what we get with the Fama-French data, over the same period, i.e., from January 3, 1950 to March 19, 2018. The data is available [here](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip) for free. Once downloaded, the data looks like this:

[![](https://alphaarchitect.com/wp-content/uploads/2018/11/famaraw-600x150.png)](https://alphaarchitect.com/wp-content/uploads/2018/11/famaraw.png)

From there, we extract *Mkt* simply by adding the *RF* column to the *(Mkt-RF)* column. Using the same pivot function with the same columns as the first table, here is what we get:

[![](https://alphaarchitect.com/wp-content/uploads/2018/11/FamaYahoo2-600x404.png)](https://alphaarchitect.com/wp-content/uploads/2018/11/FamaYahoo2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

Avid readers will notice some difference between the two data sets, that again supposedly cover the same period of time, from January 3, 1950 to March 19, 2018. The Fama-French has 17,250 days while Yahoo GSPC has 17,156 days. Yahoo’s data set is short of 94 days. What? Looking a bit closer to the sets, it looks like the shift occurs from May 26, 1952. Why? I have no idea.

Second, we can see differences between daily averages from the two data sets, highlighted in the last column. Why? There could be many reasons.

Remember, we are now comparing Fama-French to Yahoo GSPC (same as SPX Yahoo Finance). On one hand, it includes all CRSP firms incorporated in the US and listed on the NYSE, AMEX, or NASDAQ, while on the other hand, the S&P 500 Universe only.

The difference?

As of today, it’s equivalent to comparing the US total market index (3,630 companies) and the S&P 500 index (506 companies).

Could dividends be a source of discrepancy? Does Yahoo GSPC include dividends? A quick way to find out is to plot returns of Yahoo GSPC, Fama-French as well as actual funds that track both US total market and S&P 500, with and without dividends:

[![](https://alphaarchitect.com/wp-content/uploads/2018/11/compETF-800x367.png)](https://alphaarchitect.com/wp-content/uploads/2018/11/compETF.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

What do we see?

Fama-French and VTSMX are almost a perfect match, since 1992, the year of the fund’s inception. For those not familiar with the [VTSMX](https://investor.vanguard.com/mutual-funds/profile/portfolio/vtsmx) fund, it is the Vanguard fund that tracks the CRSP US Total Market Index. In other words, it supposes to replicates Fama-French method. As for the S&P 500 index, we use [VFINX](https://investor.vanguard.com/mutual-funds/profile/portfolio/vfinx), also from Vanguard. The chart shows both VFINX and VFINX(NoAdj) which respectively corresponds to the S&P500 index with dividends and without dividends (non-adjusted).

The second observation is that while being close to VFINX(NoAdj), the proxy for the non-adjusted S&P 500 index, Yahoo GSPC does not really match it. Why? Again, no idea here. Finally, it’s interesting to notice the effect of small- and mid-caps when comparing VTSMX and VFINX since 1992, but I’m digressing here.

Let’s recap what we have found so far:

* We were able to reproduce the daily averages from the paper by using the same data set from SPX Yahoo Finance. From January 3, 1950 to March 19, 2018, we also saw that the 16th, 1st and the 2nd days of the month outperform the other calendar days.
* Next, we compared the Yahoo Finance data to Fama-French data over the same period. We noticed differences in daily averages as well as in the number of days. These differences did not alter the observation made on the 16th, 1st and 2nd days of the month. They show similar strong daily returns.
* Finally, we observed that SPX Yahoo Finance data is not matching the S&P 500 index, adjusted or not for dividends, at least since 1986, inception year of VFINX.

Now that we have a better idea about the data sets that we are dealing with, let’s take a closer look at these days of the month that show stronger returns than average.

## Actual End-of-the-month Days

The next log chart shows the average daily returns of the actual end-of-the-month days. It could be a 31st, 30th, 29th, 28th, 27th or even a 26th like in February 1954:

[![](https://alphaarchitect.com/wp-content/uploads/2018/11/EOM-600x257.png)](https://alphaarchitect.com/wp-content/uploads/2018/11/EOM.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

Since May 1952, they were 790 end-of-the-month days, far more than day 16, 238 extra days exactly. Why May 1952? As mentioned earlier, Yahoo Finance is missing days prior to that date. That’s the reason why. There is an apparent up-trend from 1952 until 1990, then it starts to flatten for Fama-French and even decline for Yahoo Finance. Overall, there is a significant spread over time between to two data sets that could be explained by the dividend distribution that happens at the end of the month, just an hypothesis, given that, as seen earlier, Yahoo data seems to be unadjusted.

Now, how do we know that we are not dealing with an outlier distribution? A bit like someone who, after having flipped 1,000 times a coin, would get 999 tails? In order to test for pure random walk or actual anomaly, we are going to bootstrap these 790 days. In plain english, it means that we will place the 790 samples (observations) in a big jar, pick one at random, write down the number, put it back in the jar, repeat that 790 times, write down the average and start again 1,000 times. At the end, we should have picked 790,000 samples. We would have essentially sampled 1,000 times the 790 samples, hence the name, resamples. I have done it. I have blisters.

The bootstrap distribution is the distribution of averages from each resample (1,000 total). If the bootstrap distribution appears to be normal, then we are onto something, i.e., there might be an effect. However, if the bootstrap distribution is non-normal, then it’s closer to a random walk.

Here are the bootstrap distributions:

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/bootFF-600x375.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/bootFF.png)

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/bootYahoo-600x376.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/bootYahoo.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/bootRecap.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/bootRecap.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

From both distribution charts and statistics, it would appear that we are dealing with pretty normally distributed resamples. That would mean that, on average, and over this specific period of time, actual end-of-the-month daily returns are stronger than other days of the month, averaging +0.13% per day (Fama-French).

## Day 16

The authors of the Payday Anomaly write that the reason behind these stronger than average returns is the *hypothesis that semi-monthly pay system contributes to detectible abnormal returns not only at the turn of the month, but in the middle of the month as well*.

To find out, let’s plot the 16th day average returns since 1952, for Fama-French and Yahoo. The chart below shows the average daily returns of the 16th day. The first observation is that, on average, both data sets are trending up since 1952. Had an investor started to trade each 16th day of the month since April 1952, he/she would have more than doubled his/her investment, averaging +0.14% per day (Fama-French)

[![](https://alphaarchitect.com/wp-content/uploads/2018/11/chart16-600x271.png)](https://alphaarchitect.com/wp-content/uploads/2018/11/chart16.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

Next, let’s see whether we are dealing with a random walk or not, by applying the same bootstrapping technique. Again, the distributions below represent the distribution of averages from each resample.

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/Day16FF-600x376.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/Day16FF.png)

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/Day16Yahoo-600x374.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/Day16Yahoo.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/day16boot.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/day16boot.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

The two bootstrap distributions corresponding to Fama-French and Yahoo data sets for day 16, appear to be normal, confirming the abnormal average returns of day 16, since 1952.

## Finally, Day 1 and Day 2

As for the previous days, we plot the log returns of day 1 and day 2, using Fama-French and Yahoo data, since 1952. Similarly to day 16, they are both trending up, on average.

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/Day1.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/Day1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/Day2-600x365.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/Day2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

The bootstrap distributions also look relatively normal, confirming the abnormal average returns of day 1 and day 2, since 1952.

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/FFday1-600x378.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/FFday1.png)

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/YahooDay1-600x374.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/YahooDay1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/bootDay1.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/bootDay1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/FFday2-600x374.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/FFday2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/yahooDay2.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/yahooDay2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/bootDay2.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/bootDay2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

## All the same? Not Really. Meet Day 19

Before wrapping up, let’s take a look at the worst average day, day 19, since 1952, using the same data sets:

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/Day19log-600x369.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/Day19log.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

Followed by the bootstrap distributions that look relatively normal:

![](https://alphaarchitect.com/wp-content/uploads/2018/12/Day19FF-600x375.png)

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/Day19Yahoo-600x377.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/Day19Yahoo.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

[![](https://alphaarchitect.com/wp-content/uploads/2018/12/bootDay19.png)](https://alphaarchitect.com/wp-content/uploads/2018/12/bootDay19.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

## Conclusion

First, by replicating and comparing the initial paper to other data sets, we found out that yes, there were days with stronger average returns, specifically day 16, day 1, day 2, and end-of-the-month days. Second, we showed that the initial data set from Yahoo Finance was different from both Fama-French and actual S&P 500 funds such as VFINX, adjusted or not. It did not however alter the original findings. The bootstrap distributions tend to confirm that the original observations were not outliers, hence reinforcing the hypothesis of abnormal returns.

Now the big question is what are the factors responsible for these abnormal returns? The authors of the “Payday Anomaly” offer an answer by concluding that the, “*result confirms our hypothesis that semi-monthly pay system contributes to detectible abnormal returns not only at the turn of the month, but in the middle of the month as well.”*

This is a compelling hypothesis.

For those of us who rebalance their portfolios at the end of the month, how do you feel about these results? Ready to stomach another August 31, 1998?

And finally, who wants to short day 19?
