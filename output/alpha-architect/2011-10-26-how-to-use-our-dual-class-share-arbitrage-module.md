---
title: "How to Use Our Dual Class Share Arbitrage Module"
slug: "how-to-use-our-dual-class-share-arbitrage-module"
date: "2011-10-26"
modified: "2022-06-03"
url: "https://alphaarchitect.com/how-to-use-our-dual-class-share-arbitrage-module/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# How to Use Our Dual Class Share Arbitrage Module

> Recent market volatility is generating an anxiety in the investing public that is almost palpable, and many are searching for ways to generate returns while […]

Recent market volatility is generating an anxiety in the investing public that is almost palpable, and many are searching for ways to generate returns while managing down their exposure to equity markets.  There are many ways to manage market risk in a portfolio; typically these involve going short some stocks, which dampens the effects of market volatility on a long-only portfolio.  Another strategy involves simultaneously buying and selling different classes of an individual company’s stock, which hedges out changes in the overall market.  Let’s take a moment to describe why these classes might exist, and then we will look at how we can execute this strategy.

Let’s say you have founded a successful company that trades publicly.  One day you decide you need to raise equity, but you are concerned that a secondary offering will reduce the degree of control you have over the company you worked so hard to build.  How can you raise the equity and maintain control?

Faced with this dilemma, founders historically have sometimes opted to divide the equity of the company into two classes of stock, known as Class A and Class B.  The two classes of stock might have equal rights to the cash flows of the company, but have different voting rights.  Perhaps you as the founder will designate the stock you own as Class B stock, with full voting rights, while issuing Class A stock, with reduced or no voting rights.

Welcome to the world of dual class stock, where dozens of such dual class combinations trade on the stock market every day.  What’s interesting to us about these situations is that since the share classes trade independently, the difference, or spread, between their prices can vary dramatically over time, giving rise to arbitrage opportunities.

The spread is dependent on multiple factors in addition to voting rights differences, including liquidity, bid/ask spreads, short sale constraints and others.  Rather than get into the details of how to assess what the given spread should be, you can just look to the trading history.  For example, if a spread is wide versus its trading history, you might put on a trade on in anticipation of the spread compressing to historical levels.

Sounds good, right?  So now all you need is a tool to allow you to identify these kinds of opportunities.  Well you’re in luck!  Here at Turnkey Analyst, we recently launched a dual class share arbitrage module that can assist you in identifying and analyzing these situations.  Let me walk you through a specific opportunity we spotted recently.

First, we launch the dual class module, and then sort the output by magnitude of the spread:

![](https://alphaarchitect.com/wp-content/uploads/2011/10/bottom-dual-class.png "bottom dual class")

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

![](https://alphaarchitect.com/wp-content/uploads/2011/10/top-dual-class.png "top dual class")  
Looking over our output for our top five names, above, we can see that the spreads, or the percentage difference between the two classes in each case, range from a high of 49.7% for Crawford & Company, down to 25.6% for K V Pharmaceutical Co.  Although a large spread, per se, does not necessarily mean there is an opportunity, it can help identify good candidates to analyze more closely.  So that’s what we’ll do next.

Clicking down through these names, we can look graphically at what happened to spreads recently, in each case.  When I clicked on the first name on our list, Crawford & Company, I saw the output below:

![](https://alphaarchitect.com/wp-content/uploads/2011/10/crawford-spread.png "crawford spread")

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

This graph shows us how the two classes of Crawford & Company stock performed relative to each other over the past six months.  While we don’t know where the two classes stood in relation to each other at the beginning of the period, we can see that, versus that starting point at least, there have been times when the Class A stock has outperformed, such as June and September, and other times when the Class B stock was ahead, such as July and October.  This suggests that the spread has been non-constant over the period.  Let’s take a step back and look at what the actual spreads have been over the past year.

![](https://alphaarchitect.com/wp-content/uploads/2011/10/crawford-1yr-spread.png "crawford 1yr spread")

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Above is a graph of the spread between the two classes of Crawford & Company stock for the past trading year.  You can see that the spread started at about 30%, dipped into the low 20% range, and then bounced roughly between the 30% range and the 50% range in the intervening period.  So it’s fair to say that, at least for the past year’s worth of data, the spread appears to be at the high end of its observed trading range, while 30% might be the lower bound on its trading range.  Looks like it could be an arbitrage opportunity.  If we set up our trade properly, and the spread compresses from its roughly 50% range back to, say, 30%, as it has done several times over the past year, we can expect to make some money.  Let’s look a little more closely at this situation.

![](https://alphaarchitect.com/wp-content/uploads/2011/10/crawford-detail.png "crawford detail")  
Clicking on “More Details” for Crawford & Company, we see the output above, which provides a little more information about our opportunity.  It seems that the Class A and Class B shares of Crawford & Company are identical, except that the Class A shares have no voting rights.  So it is reasonable to expect the Class B shares should trade at a higher price, reflecting the incremental value of their associated voting rights.  Is 50% a reasonable premium for the voting rights?  It’s hard to say conclusively, but we do know that there are no other dual class share spreads that currently trade this high.

Furthermore, this particular spread looks rich compared to where it has traded over the past year.  Let’s assume for illustrative purposes that we believe this spread is high and will come down.  How do we set up our arbitrage trade to take advantage of it?

As I write this, CRD-B trades at $6.32, while CRD-A trades at $4.17 (the spread has increased slightly today versus our output), and what we want to do is short the Class B stock, and go long the Class A stock in equal dollar amounts.

![](https://alphaarchitect.com/wp-content/uploads/2011/10/crawford-trade.png "crawford trade")  
The above hypothetical trade shows that to keep our hedge dollar neutral we short 0.66 shares of CRD-B for every share we go long CRD-A.  In this trade we short 79 shares of CRD-B, and go long 120 shares of CRD-A.  Now we wait for the spread to narrow.

If the broader marketplace moves significantly up or down, it may or may not impact the spread.  Theoretically, you don’t particularly care which way the market moves, except to the extent that it might act as a catalyst for narrowing the spread.  This gives you peace of mind as an investor, since here you have a trade whose payoff is largely independent of which way the market moves.

But these are the capital markets.  Anything can happen from here.  The spread could double.  Yet even if that happens, chances are good that if you are patient it will at some point drop below the ~50% range and you won’t suffer permanent capital impairment.  Conversely, you might see the spread narrow from 50% to 30% within two or three months – as has happened three times already in the last calendar year.  If that happened, you could see a nice return on this investment in fairly short order: in very simplistic terms, the roughly $1,000 at risk in this trade could generate perhaps $100 of profits.  In a world with ultra-low bond yields, and high market volatility, I’ll take it.

This is just one way to play the dual class share arbitrage game.  Let’s a take brief look at Heico Corporation, the second company on our Dual Class Module output, as sorted by size of spread. The graph below depicts the 5-year history of the spread between the Class A and Class B shares.

[![](https://alphaarchitect.com/wp-content/uploads/2011/10/heico-spread1.png "heico spread")](https://alphaarchitect.com/?attachment_id=4788 "heico spread")

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

As Joel Greenblatt would say, “Gee that’s interesting.”  Note that the spread is at a 5-year high. Seems like this could be another candidate for further review.

Another possibility might look like the following: say the voting share class usually trades at a higher price than the non-voting, but for some reason that situation is reversed for a given name.  You can make a bet that the traditional price relationship between the classes will be restored.  Sound compelling?  You may be able to find such an opportunity today.

But wait, there’s more!

The Turnkey PhD has written a blog post, <https://alphaarchitect.com/2011/03/dual-class-shares-a-first-class-strategy/>, which discusses a paper that researches a mechanical trading strategy for dual class shares.  Read it, create your own trading rules, and go make some money.

Sometimes these trades have challenges or just plain don’t work when you get into the guts of execution.  The bid/ask spread eats up the profits.  Shares are unavailable to borrow, or your short positions gets called in by the broker.  Applying a meaningful amount of capital compresses the spread rapidly – likewise getting out of the trade widens the spread.

Nevertheless, there are plenty of situations when these trades can make sense.  That’s where you come in.  All it takes is some analysis, some common sense, and the right tool, which we think we have provided you here.  So take a pass through Turnkey Analyst’s Dual Class Module, and review some of the opportunities it is suggesting.  You may like what you find, and even if you don’t, keep your eye on the list since every day new possibilities present themselves.
