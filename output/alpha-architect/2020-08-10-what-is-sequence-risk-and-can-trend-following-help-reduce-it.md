---
title: "What is Sequence Risk and Can Trend Following Help Reduce It?"
slug: "what-is-sequence-risk-and-can-trend-following-help-reduce-it"
date: "2020-08-10"
modified: "2022-05-21"
url: "https://alphaarchitect.com/what-is-sequence-risk-and-can-trend-following-help-reduce-it/"
categories: ["Research Insights", "Trend Following", "Basilico and Johnsen", "Academic Research Insight"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# What is Sequence Risk and Can Trend Following Help Reduce It?

> Reducing Sequence Risk Using Trend Following and the CAPE Ratio Andrew Clare, James Seaton, Peter N. Smith, and Stephen Thomas Financial Analysts Journal A version […]

## Reducing Sequence Risk Using Trend Following and the CAPE Ratio

* Andrew Clare, James Seaton, Peter N. Smith, and Stephen Thomas
* Financial Analysts Journal
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2764933)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

What exactly is “sequence risk?” We’ll get more into the weeds of it, but for now, consider it the risk of loss when you can least afford it. Think of a client leaving their retirement party with their shiny new set of steak knives and then learning via the news that their enormous position in their employer’s stock has just dropped 50%. The authors of this paper look deeply into sequence risk and consider [trend following](https://alphaarchitect.com/2019/06/26/trend-following-the-epitome-of-no-pain-no-gain/) and the utilization of CAPE to help alleviate this risk. (See [Corey’s piece](https://blog.thinknewfound.com/2018/07/the-new-glide-path/) for another great perspective on this topic).

1. What is sequence risk and why is it important?
2. Can trend following (TF) signals reduce sequence risk, or otherwise protect a fixed and targeted withdrawal rate for retirement funds?
3. Can an equity valuation measures like the CAPE ratio help in securing higher withdrawals?

## What are the Academic Insights?

1. SEQUENCE RISK is the chance that the worst investment returns occur in the worst order possible. However, most performance measures fail to incorporate the order of returns in the assessment of an investment strategy. It is in the retirement literature that we find the notion of “order” incorporated into the assessment of performance.  In that context, the discussion on performance turns on the impact of regular additions and withdrawals from an accumulated “savings” during periods of accumulation or decumulation. For example, the perfect withdrawal rates (PWR) is given by Return Sets shown in Table 1. Although the performance measures are equivalent across each Return Set, the sequence of returns varies. The highest PWR is associated with the order of returns found in Return Set 1 and the lowest PWR is associated with the order of returns in Set 2 (the worst sequence!).
  
2. YES. A monthly TF filter (10-month MA) replaced a buy & hold (BH) equity strategy utilizing the SP500 as the investment vehicle.  The series of TF returns were calculated from a switching rule: when the SP500 return was above it’s 10-month MA, the strategy earned the next month’s return on the SP500.  If below the 10-month MA, the strategy switches to cash and instead earns the cash rate. A Monte Carlo analysis was conducted using the actual return time series drawn from the TF filter.  The results obtained had the effect of reducing sequence risk:  (1) the distribution of returns from the filter shifted to the right when compared to the BH; (2) ninety percent of the time the PWRs from the filter rule were greater than the BH; (3) at lower probability levels, the PWRs from the filter were twice those from the BH; (4) the average return was 8.84% vs 6.82% for the BH; (5)  volatility was 9.86% vs. 14.29% for the BH; (6) max drawdown was 34.88% vs. 76.8% for the BH; (6) transactions costs were 66% of the BH, a reduction due to the much lower fees associated with holding cash.
  
3. MAYBE. Although some valuation ratios have shown long-run predictability for equities, their performance as an enhancement to the filter rule tested in this article was mixed. When actual returns are high in the initial investing years, it appears that knowledge of the CAPE ratio at the beginning of the year could add value in the retirement years.  However, when returns in the initial years were very poor, the use of the filter rule alone produced superior PWRs. The damage, although mitigated with the CAPE ratio, could not be repaired.

## Why does it matter?

Sequence risk is an exposure most investors fail to appreciate fully. The traditional solutions to managing sequence risk vary from building multi-asset portfolios to purchasing life-time annuities and now include the use of trend following rules within asset classes. Given that returns are not predictable, the results presented in this article provide support (and hope!) for investors who have been *unlucky* in choosing their targeted retirement date. The authors argue that trend following can be a powerful tool for managing *targeted* outcomes for retirement purposes and find that even simple trend following rules reduced the impact of a sequence of negative returns occurring at inconvenient times. While the implications of this article are decidedly positive for investors, retirees, planners and asset allocators, they would be enhanced if there were a generally accepted measure of sequence risk.

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2020/07/image-80-1200x784.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

---

## Abstract

> The risk of experiencing bad investment outcomes at the wrong time, or sequence risk, is a poorly understood but crucial aspect of the risk investors face—particularly those in the decumulation phase of their savings journey, typically over the period of retirement financed by a defined contribution pension scheme. Using US equity return data for 1872–2014, we show how this risk can be significantly reduced by applying trend-following investment strategies. We also show that knowing a valuation ratio, such as the cyclically adjusted price-to-earnings (CAPE) ratio, at the beginning of a decumulation period is useful for enhancing sustainable investment income.
