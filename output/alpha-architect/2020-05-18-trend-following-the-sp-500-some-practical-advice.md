---
title: "Trend Following the S&P 500? Some Practical Advice"
slug: "trend-following-the-sp-500-some-practical-advice"
date: "2020-05-18"
modified: "2022-05-20"
url: "https://alphaarchitect.com/trend-following-the-sp-500-some-practical-advice/"
categories: ["Research Insights", "Trend Following", "Basilico and Johnsen", "Academic Research Insight"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Trend Following the S&P 500? Some Practical Advice

> BREAKING INTO THE BLACKBOX: Trend Following, Stop Losses, and the Frequency of Trading: the case of the S&P500 Andrew Clare, James Seaton, Peter N. Smith, […]

## BREAKING INTO THE BLACKBOX: Trend Following, Stop Losses, and the Frequency of Trading: the case of the S&P500

* Andrew Clare, James Seaton, Peter N. Smith, and Stephen Thomas
* Working Paper, Cass Business School, London and University of York, UK
* A version of this paper can be found [here](http://ssrn.com/abstract=2126476)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

Now that market volatility is back, tail risk management strategies are gaining some attention. A lot of investors are dipping their toe into the water and exploring trend-following strategies on the S&P 500 — arguably the most popular U.S. stock market index.This paper explores multiple trend following signals (TF) with various degrees of complexity, frequency, and trading (they also check out the use of stop-loss (S-L) rules). The authors perform a comparison of these approaches to traditional valuation metrics. The TF signals are calculated over July 1988-June 2011 for the S&P 500 index (a short window of time, which has some obvious caveats). Please note that the paper we examine here is written in plain language and is not as esoteric as more formal academic literature we typically cover — so one can expect a trade-off between academic rigor and accessibility. If you are looking for a quick intro to trend-following, this is a good place to start (along with [Meb Faber’s excellent piece here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461)).

Here are the strategies examined:

* A simple daily moving average (MA): The buy signal is triggered when the value of the S&P 500 moves above the average and the moving average ranges from 10 to 450 days;
* MA crossovers: The buy signal is triggered when the shorter duration average of the S&P 500’s index value moves above the longer duration average, ranging from 25/50 days through 150/350 days; and
* Breakout rules: The buy signal is triggered when the S&P 500’s index value trades at a high, ranging from 10 to 450 days.

Questions addressed:

1. Do more complex trend following strategies beat simple strategies?
2. Does the frequency of trading matter?
3. Do trend following strategies that trade more frequently result in costly movements into and out of the market?
4. Is there any advantage to using stop-loss rules?
5. Are trend following signals superior to fundamental valuation metrics?

## What are the Academic Insights?

1. NOT SO MUCH. A set of TF signals including moving average, crossover, and breakout rules are compared. The Sharpe ratios are presented in the chart below. There appears to be no advantage to complexity as long as the average length of the signal calculated is greater than 300 days on a daily basis. For shorter periods, 200-250 days or less, the crossover and breakout rules produced superior risk-adjusted returns when compared to a simple MA. However, those methods did not outperform a simple buy-and-hold approach.
  
2. NO. Many trend-following rules are often applied using high-frequency data. However, when daily and monthly risk-adjusted returns from high (daily) and low (monthly) are compared, there appears to be no real advantage to the higher frequency signal with the caveat that the average length of the signal exceeds at least 100 days. Generally, monthly trading appeared to be superior to daily. The application of the rules in the monthly context had higher returns and lower volatility. It appears that the end-of-month trading is sufficient. A clear benefit to practitioners looking to implement DIY trend-following approaches.
  
3. YES. The table clearly shows that longer-term signals produce superior performance relative to shorter-term signals. The increase (excessive?) in trading costs associated with shorter-term signals evidently detracts from performance.
  
4. NO. Consistent with other research (Kaminski and Lo (2008)) stop-loss rules implemented to avoid or limit drawdowns over time or magnitude do not appear to be advantageous.  S-L rules are very popular in the fund management industry and among retail investors. Three S-L strategies are examined: a typical breakout rule, trailing stop-losses, and purchase cost stop-losses. A typical breakout rule is triggered for selling when the MA is broken through on the downside and buying when the break occurs on the upside. The trailing S-L assumed a 200 day MA as the breakout with stopping out triggered by a range of declines from that point, between 3%-15%. The purchase cost rule is triggered to sell the asset when its return falls below 5 standard deviations from the purchase price.  All three methods did not appear to have a positive impact on the trend following rule (MA). However, the purchase cost technique had higher returns and volatility than the breakout and trailing rules.  The simple TF rule itself is the preferred stop-loss technique.
  
5. YES. Traditional valuation metrics are tested and include dividend yields, earnings yields, and relative yields on equities and bonds. Results were obtained using the January 1952 – June 2011 Shiller data to forecast returns from various valuation metrics and then compared to the results for the end-of-month 10-month TF rule. Consistent with other research, the trend following rules reduced volatility by 33%-50% producing much higher Sharpe ratios.

One very important caveat: The results are specific to the S&P 500 and not necessarily robust to other universes.  We’ve [developed some tools](https://alphaarchitect.com/trendfollowing/) if you’d like to review various trend-following signals in real-time.

## Why does it matter?

The authors make a useful contribution to practitioners, fund managers, and clients by exploring a number of practical questions for TF strategies.  Consideration of frequency of trading signals, the usefulness of stop losses, and performance comparison to valuation signals relative to TF are generally lacking in the research published in many academic journals. Instead, most studies concentrate on testing a variety of trading rules across many asset classes. The practical implications of this research are straight-forward: the best stop-loss rule is actually a change in the trend signal itself; daily trading is not a necessary condition for superior performance, and traditional financial metrics are no match for a simple 200-300 day average.

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2020/05/2020-05-07-14_49_10-Document2-Word-800x1051.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

---

## Abstract

> In this paper we compare a variety of technical trading rules in the context of investing in the S&P500 index. These rules are increasingly popular both among retail investors and CTAs and similar investment funds. We find that a range of fairly simple rules, including the popular 200-day moving average trading rule, dominate the long only, passive investment in the index. In particular, using the latter rule we find that popular stop loss rules do not add value and that monthly end of month investment decision rules are superior to those which trade more frequently: this adds to the growing view that trading can damage your wealth. Finally we compare the MA rule with a variety of simple fundamental metrics and find the latter far inferior to the technical rules over the last 60 years of investing.
