---
title: "Introduction to Behavioral Finance – Part 2: Limits of Arbitrage"
slug: "introduction-behavioral-finance-part-2-limits-arbitrage"
date: "2014-05-20"
modified: "2026-05-21"
url: "https://alphaarchitect.com/introduction-behavioral-finance-part-2-limits-arbitrage/"
categories: ["Best of Active Management", "Behavioral Finance"]
tags: []
best_of: true
source: "alphaarchitect.com"
best_of_section: "Active Management & Behavioral Finance"
---

# Introduction to Behavioral Finance – Part 2: Limits of Arbitrage

> In the first part of our series, “Introduction to Behavioral Finance – Part 1: Behavioral Bias,” we explored several market anomalies, and the first required condition for the real-life implementability of many quantitative strategies: the existence of human behavioral biases. In this Part 2 of our series, we consider a related question following from our Keynes example: given that certain behavioral biases can affect investors, how can it be that their effects persist in markets so we can take advantage of them? This would seem to contravene the notion of efficient markets, and leads to the second required condition for implementing a tradable strategy: limits to arbitrage.

In the first part of our series, “[Introduction to Behavioral Finance – Part 1: Behavioral Bias](https://alphaarchitect.com//2014/05/19/introduction-behavioral-finance-part-1-behavioral-bias/),” we explored several market anomalies, and the first required condition for the real-life implementability of many quantitative strategies: the existence of human behavioral biases. In Part 2 of our series, we consider a related question: given that certain behavioral biases can affect investors, how can it be that their effects persist in markets so we can take advantage of them? This would seem to contravene the notion of efficient markets, and leads to the second required condition for implementing a tradable strategy: **limits of arbitrage**.

John Maynard Keynes was a shrewd observer of financial markets, and a successful investor in his own right. His investing success, however, was uneven, and at one point he was reportedly wiped out while speculating on leveraged currencies. This perhaps led him to make the famous statement ([debated!](https://quoteinvestigator.com/2011/08/09/remain-solvent/)):

> Markets can remain irrational a lot longer than you and I can remain solvent.

Clearly, there were limits to Keynes’s ability to realize arbitrage profits, and these limits generally form the basis of Part 2 of our Introduction to Behavioral Finance series.

## The Efficient Market Hypothesis

The Efficient Market Hypothesis (the “EMH”), pioneered by Eugene Fama, states that there are varying forms of market efficiency. Of particular interest is semi-strong market efficiency, which claims that markets prices reflect all publicly available information about securities. When mispricings occur in markets, they should be immediately eliminated by arbitrageurs, who exploit these opportunities for a profit. Therefore, in the EMH view, prices should always reflect fundamental value.

In Part 1, we discussed the Value and Momentum anomalies, and how they were related to certain behavioral biases. But, as discussed, in light of the EMH, these should be quickly arbitraged away. Yet they are not. Why not?

The reason these anomalies can exist is that, as Keynes discovered, there are limits to the arbitrage process, which can be constrained in various ways. These limits, when they can be identified, can provide us an opportunity to trade against our pernicious behavioral biases.

## Limits of arbitrage

Let’s quickly review the concept of arbitrage. The textbook definition of “arbitrage” involves a costless investment that generates riskless profits, by taking advantage of mispricings across different instruments representing the same security. Arbitrage is critical to the maintenance of efficient markets, since it is through the arbitrage process that fundamental values are kept aligned with market prices. In practice, arbitrage entails costs as well as the assumption of risk, and for these reasons, there are limits to the effectiveness of arbitrage in eliminating certain security mispricings. There is ample evidence for such limits to arbitrage.

Many of these limits are explored in a ground-breaking 1997 paper called, appropriately, “The Limits of Arbitrage,” (which can be found here: http://ms.mcmaster.ca/~grasselli/ShleiferVishny97.pdf) by Shleifer and Vishny. Below we consider a few limits to arbitrage, and finally, some that may apply to our situation as value investors in the stock market.

**Fundamental Risk**. Arbitrageurs may identify a mispricing of a security that does not have a close substitute that enables riskless arbitrage. If a piece of bad news affects the substitute security involved in hedging, the arbitrageur may be subject to unanticipated losses.

A good example here is a pairs trading strategy, which employs two nearly identical securities in the arbitrage process. Say Coke and Pepsi traditionally trade at a similar valuation, a P/E of 10, yet for some reason, Coke has become very expensive at 20X earnings, while Pepsi remains at a 10X multiple. The arbitrageur would go long Pepsi and short Coke. When the multiples converge to historical equality, at some point in the future, the arbitrageur would realize gains. But what if Pepsi declined to a 5X multiple and Coke increased to a 30X multiple for the next 5 years? The arbitrageur is exposed to the fundamental risks of each security.

**Noise Trader Risk**. Noise traders limit arbitrage. Once a position is taken, noise traders may drive prices farther from fundamental value, and the arbitrageur may be forced to invest additional capital, which may not be available, forcing an early liquidation of the position.

Complicating Noise Trader Risk is the structure of many arbitrage markets. Shleifer and Vishny point out that “millions of little traders” don’t have access to the same information that professional, specialized arbitrageurs do. These professional arbitrageurs, who thus do the bulk of the market’s arbitrage work, will go out and raise capital from third parties to ply their trade. If an arbitrage spread widens, however, these third parties may disrupt the arbitrage process by pulling their capital, just when it is most needed to keep an arbitrage trade on.

A good example is the 2011 bankruptcy of MF Global. MF Global was fundamentally pursuing an arbitrage trade. The firm bought discounted European bonds (that were guaranteed by the European Stability Facility), and then used them as collateral for new loans, which they used to buy yet more bonds. So the bonds were guaranteed, and MF Global only had to repay the loans when the bonds matured at par – in an amount greater than what was owed. It was the perfect arbitrage trade! The ultimate outcome, however, clearly demonstrates the limits to arbitrage: noisy traders pushed bond spreads wider, and MF Global got hit with a margin call that bankrupted the firm.

**Implementation Costs**. Short selling is often used in the arbitrage process, although it can be expensive due to the “short rebate,” representing the costs to borrow the stock to be sold short. In some cases, such borrowing costs may exceed potential profits. If short rebate fees are 10% or 20%, then arbitrage profits must exceed these costs to achieve profitability. That’s a tall order.

**Performance Requirements/Agency Costs**. Another short-circuit to the arbitrage process relates to limits imposed by variations in performance, and how they affect money manager incentives. Consider the pressures produced by “tracking error,” or the tendency of returns to deviate from a benchmark.

Say you have a job investing the pensions of 100,000 firemen. You have a choice of investment strategies. You can invest in:

* **Strategy A:** A strategy that you know (by some magical means) will beat the market by 1% per year over 25 years. You also know that you will never underperform the index by more than 1% in a given year; or
* **Strategy B:**An arbitrage strategy that you know (again by some magical means) will outperform the market, on average, by 5% per year over the next 25 years. The catch is that you also know that you will have a 5-year period where you underperform by 5% per year.

Which strategy do you choose? If you are a professional money manager, the choice is obvious: you choose A.

*Why choose A?* It a bad strategy relative to B.

It all boils down to tracking error and the incentives of the investment manager. Fund managers are not the owners of the capital, which creates a principal agent problem. These managers sometimes make decisions that ensure they maintain a job, but not necessarily maximize risk-adjusted returns for their investors. For these managers, tracking error is everything. The tracking error on strategy B is just too painful. Those firemen are going to start screaming bloody murder during years 3 and 4 of your underperformance, and you won’t be around long enough to see the rebound when it occurs after year 5. But if you follow strategy A, you can lock in a nice job for a long time.

Now it may be that, over long time frames, this arbitrage opportunity is a mile wide – you could drive a proverbial truck through it. But it is this agency problem – the fact that the owners of the capital can, in lean times, begin to doubt the abilities of the arbitrageur and pull their capital – that precludes the arbitrageurs from taking advantage of the opportunity.

It may be for this reason that an anomaly like value investing has continued to work, year after year, and decade after decade, ever since Ben Graham began talking about it almost 100 years ago. People simply cannot stay with it for the long haul, since periodic underperformance drives investors away from the strategy, which means that managers will avoid it, due to career risk. Hence, this could be a factor in why the anomaly can persist over time.

## Putting it all together

We know that behavioral biases can drive stock market anomalies, such as Value and Momentum. And we also know that, due to limits to arbitrage, such anomalies can persist over time, which creates an opportunity for the investor. If an investor can identify situations where these two conditions hold, we may have an opportunity to exploit the bias, by investing in mispriced securities.

Now what is required is a systematic approach to taking advantage of situations that arise we can do so. As it turns out, there are many such approaches, and we invite our readers to follow us as we examine some of these critically on this blog.
