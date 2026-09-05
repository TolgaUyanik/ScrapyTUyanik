---
title: "Understanding How ETFs Trade in the Secondary Market"
slug: "trading-etfs-in-the-secondary-market"
date: "2014-12-03"
modified: "2022-10-25"
url: "https://alphaarchitect.com/trading-etfs-in-the-secondary-market/"
categories: ["Investor Education", "Key Research", "Uncategorized"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Understanding How ETFs Trade in the Secondary Market

> An ETF’s liquidity has everything to do with the underlying liquidity of the positions the ETF holds. This has a few implications: Pay attention to the liquidity on the holdings of your ETF–this will explain the spreads in the secondary market; Trade ETFs when the underlyings are liquid–avoid trading ETFs at the open or when overall market volume is lackluster; Avoid huge market orders, and stick to limit orders; Moreover, for huge trades, communicate directly with the market maker or your ETF trading desk.

An educated investor can defend against the financial services industry, which is a marketing juggernaut and doesn’t always have your best interest in mind. In this article, we’ll discuss how ETFs trade in the secondary market.

The focus for today is understanding how markets are made in ETFs. As it turns out, market-making for ETFs differs fundamentally from the type of market-making associated with other listed securities.

We had a great interview on [ETF market making](https://alphaarchitect.com/2014/11/insider-insights-on-etf-market-making-very-cool/#.VHXdcovF9MU) with [Chris Hempstead](https://www.linkedin.com/in/chris-hempstead/), a big shot over at KCG, one of the largest ETF market makers in the world.

Chris’ final words:

> Ask questions.  Get comfortable. Ask more questions.  DO NOT let someone tell you that an ETF is illiquid simply because it doesn’t trade a lot.  You are not investing in volume.  You are investing in a product that tracks an index.  If you can efficiently buy and sell the optimal product, other people’s volume is the least of your concerns.  Find a broker that understands how to access the cheapest and most efficient liquidity at the moment in time you need to trade.

Chris really set the stage for this discussion and answered some burning questions many of you probably had in the back of your mind.

A PDF version of this is [available here](https://alphaarchitect.com/wp-content/uploads/2021/08/Understanding_How_ETFs_Trade_in_the_Secondary_Market.pdf).

## How Markets are Made in ETFs

[![Screenshot of bid prices for certain tickers](https://alphaarchitect.com/wp-content/uploads/2014/12/How-ETFs-Trade-in-the-Secondary-Market_1.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/How-ETFs-Trade-in-the-Secondary-Market_1.png)

[![Screenshot of bid prices for certain tickers](https://alphaarchitect.com/wp-content/uploads/2014/12/How-ETFs-Trade-in-the-Secondary-Market_2.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/How-ETFs-Trade-in-the-Secondary-Market_2.png)

[![How ETFs Trade in the Secondary Market_3](https://alphaarchitect.com/wp-content/uploads/2014/12/How-ETFs-Trade-in-the-Secondary-Market_3.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/How-ETFs-Trade-in-the-Secondary-Market_3.png)

An ETF is simply a basket of securities that are publicly traded in the marketplace. Consider an ETF that holds 2 stocks: MSFT and INTC.

Throughout the day, there is an “INAV,” or intra-day net asset value, which tracks the value of an ETF on a 15-second basis. The INAV will be based on the prices associated with MSFT and INTC. Unfortunately, INAVs are not always 100% accurate, and by design, they can be up to 15-seconds delayed. 15-seconds doesn’t sound like a long time, but in the context of intraday markets, 15-seconds can be an eternity.

Because INAV values can have issues, market makers and ETF sponsors maintain a separate, real-time price on their ETFs. On a tick-by-tick basis, market makers track the “true” value of an ETF.

Market makers don’t track the tick-by-tick value of an ETF for their health–they do it so they can make money! Market makers are in the business of making markets, which costs money. Someone has to buy the computers, pay the employees, and pay the rent to keep the lights on at the market-making shop.

One way the market maker makes money is by creating a bid/ask spread around the ETF’s true tick-by-tick value. For example, let’s say the value of the underlying basket of stocks in an ETF is worth $25. A market maker might post a bid at 24.95 and post an ask of 25.05. So if someone wants to sell the ETF, they will get 24.95, not $25. The 5-cent difference goes to the market maker. Similarly, on the buy transaction, an ETF buyer will pay $25.05 for the ETF. The buyer will get an asset worth $25, and the 5-cent premium will go to the market maker for making a market in the ETF.

Here are some example limit books from 11/26 (~9:35am) on PIZ, IWM, and SPY.

PIZ trades in international markets; IWM trades in small-cap stocks; SPY trades in mid/large-cap stocks.

**PIZ**  
The spread is 9 cents or roughly a 4bps spread on either side. Pretty liquid. (Note: the $24.95 is the last trade)

**IWM**  
The IWM has a 1-cent spread on either side or ~1bp. Incredibly liquid.  
  
SPY  
SPY is incredibly liquid, and the spread is 1 cent or 1/2 a cent on either side. This is essentially “free” for all intents and purposes.

## How is the Spread Priced?

Investors often confuse the liquidity of an ETF with the “volume” of shares traded for the ETF. But this is not the right way to think about it.

As Chris highlighted in his interview:

> **DO NOT let someone tell you that an ETF is illiquid simply because it doesn’t trade a lot.** You are not investing in volume.  You are investing in a product that tracks an index.

[![ETF liquidity is driven by underlying liquitidy](https://alphaarchitect.com/wp-content/uploads/2014/12/ETF-liquidity-is-driven-by-underlying-liquitidy.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/ETF-liquidity-is-driven-by-underlying-liquitidy.png)

What is Chris talking about?

Well, if you notice the three limit books from above, they have three different spreads and trade in three different asset classes. You’ll also notice that the PIZ book is less liquid than the IWM book, and the IWM book is less liquid than the SPY book.

Of course, a big part of the “visible” liquidity in these three different limit books is driven by the popularity and interest in these ETFs. And while popularity and interest certainly contribute to liquidity because there is a large and robust secondary market (i.e., ETF holders are trading amongst each other), the fundamental driver of liquidity for most ETFs is the liquidity of the underlying assets that the ETF holds. The reason why the liquidity of the underlying assets is so important to ETF liquidity has to do with how the market makers make a profit, which we’ll get to in a minute. Certainly, the liquidity of the underlying assets helps describe the spreads in PIZ, IWM, and SPY observed above. In general, international stocks (PIZ) are less liquid than Russell 2000 stocks (IWM), and US small-caps (IWM) are less liquid than S&P 500 stocks (SPY). The spreads on these three ETFs seem to match up with the liquidity of the stocks they contain.

This intuition underlying this concept is set forth in the chart below, which has four quadrants. Note how in quadrant 1 (upper left), illiquid underlying assets result in an illiquid ETF, and in quadrant 2 (upper right) liquid underlying assets result in a liquid ETF. There are two important corollaries here for ETF investors. In quadrant 3 (lower left) illiquid underlying assets DO NOT result in a liquid ETF. In quadrant 4 (lower right) liquid underlying assets DO NOT result in an illiquid ETF.(1)

## **Why is liquidity in an ETF driven by the liquidity in the underlying?**

This underlying liquidity matters because it is the liquidity of the underlying assets that determines how market makers create the “spread.” The spread is set such that it is profitable for the market maker. Market makers, specifically authorized participants (APs), can arbitrage differences between the net-asset-value (NAV) of an ETF and the value of the underlying ETF holdings.

At every given point in the day, an AP calculates the cost to buy the basket of securities that form an ETF, and the cost of selling a basket of securities that form an ETF. They compare these two “theoretical” portfolios to the live net asset value of the ETF.

Let’s work through an example so you can understand how these market makers think:

Consider the “TECH” ETF that holds 1 share of MSFT and 1 share of INTC. Let’s say MSFT’s bid/ask is 47.31 by 47.35 and INTC’s bid/ask is 36.49 by 36.51. This means that an investor can buy MSFT at 47.35 and buy INTC at 36.51. This also implies that an investor can sell MSFT at 47.31 and sell INTC at 36.49.

Let’s say the current live net asset value based on mid-point prices on TECH is  83.83. The market maker will identify how much it costs to buy and sell the basket for TECH.

To buy the underlying in TECH, it would cost 83.86 (47.35+36.51), and to sell the underlying in TECH, it would net 83.80 (47.31+36.49).

Given this information, the AP will sit back and think, “How do I make a market in TECH?” Being a profit-minded AP, they might set their market prices as follows:

> **Bid** 83.75; **Ask** 83.91.

#### Secondary Market Purchase

Let’s say someone comes along in the secondary market, sees the posted Ask, and wants to purchase the ETF at $83.91. When this happens, what does the market maker do?

The AP does not own any ETF shares to sell. However, as a market maker, he can effectively create new shares by  “selling short” a TECH share to this secondary market participant for $83.91. The AP is “short,” in the sense that he will, at some point in the future (within 6 days), need to deliver these ETF shares to the buyer. As he sells the ETF “short” in the secondary market, he will simultaneously go into the market and go long the basket for $83.86 as a hedge. The AP wants to be fully hedged: he is long the basket of names and short the ETF (but has to deliver it in the future). He has made the market, is fully hedged, and has made a small spread in the transaction.

#### Secondary Market Sale

Let’s say someone comes along in the secondary market, sees the posted Bid, and wants to sell the ETF at $83.75. So the market maker buys the ETF from this secondary market participant at $83.75, and in order to hedge, he shorts the basket of names (MSFT and INTC) at $83.80.

All sounds great up until this point, but we have all been taught the following:

1. Markets are driven by demand and supply.
2. Markets can remain irrational longer than one can remain solvent.

Recall that, in these examples, the market makers are managing a market-neutral book. Why are market makers content with the arrangement knowing that market-neutral books can get out of wack in the short run? Answer: daily arbitrage opportunity.

Let’s go back to the “Secondary Market Sale” example above. Let’s say that secondary market participants relentlessly hit the market maker’s Bid at $83.75. At each transaction, the market maker has been buying, buying, and buying ETF shares. But the market maker has been hedging all along by shorting the basket of MSFT and INTC. Suddenly, the market maker looks up and has a HUGE position in the ETF (although it is hedged). And here is the beauty of the ETF structure from the market maker’s perspective. They don’t require secondary market volume to unwind the hedged book — the market maker can simply redeem an ETF unit, and simultaneously cover his shorted basket of MSFT and INTC.

Again there are two great features of ETFs from the market maker’s perspective:

1. What makes ETFs unique is the AP’s ability to arbitrage the spread between underlying assets and the ETF NAV at the end of every trading day.
2. The reason the “hedge” transactions are good hedges is that the AP can always create/redeem ETF shares and underlying securities to unwind any positions they have long/short. Once again, this can occur regardless of the ETF’s market volume. This daily arbitrage mechanism takes a lot of the market-making risk off the table, which gets reflected in the underlying spreads for ETFs that trade liquid underlying securities.

## How Does all of this Liquidity Talk Show Up in Practice?

So let’s say the TECH ETF has ZERO shares traded and a limit book that looks like a blank monitor. When trading a common stock, this is a major issue. No liquidity means no love when it comes to buying/selling.

However, when trading an ETF, ZERO shares traded don’t really matter. What matters is how liquid the underlying shares are that make up the ETF. The market makers have computers continually monitoring the underlying TECH ETF basket, and if investors are buying/selling in the market and they can make an arbitrage profit–they will do so!

Consider the TECH ETF. Sure, it has ZERO shares traded, but the underlying assets that TECH holds are extraordinarily liquid (MSFT and INTC). This means that the ETF shares are equally liquid–even if you don’t “see it” as daily trading volume, as you would with ordinary stocks.

If a large investor wants to put in an order to buy $1,000,000 worth at 83.91, they can get filled with little market impact–if they go about the process correctly–and let’s not even consider the “primary” market, let’s stick to secondary trading. This investor would simply need to communicate with the AP community or the ETF sponsor and tell them that a large limit order is hitting the market. This will prevent the APs from being “surprised” by a huge order. If they are “surprised,” they may think an arbitrageur is trying to get the best of them and that perhaps something is wrong with a stock in the basket or with their own internal NAV calculations of which they are not yet aware, and reflexively widen the spread.

But if they are aware of a large order, the APs know full well they can make profits by selling the TECH ETF @ 83.91, while buying and holding the basket/covering their shorts of MSFT and INTC, and thus they will sell as much TECH ETF as any secondary market participant can handle at 83.91, up until their buying pressure in the underlying MSFT and INTC starts having an impact on the actual underlying securities (in other words, it would probably require a lot bigger order than a $1,000,000 order).

In other words, if an ETF is composed of large liquid stocks, even if its secondary market volumes are very low, the market makers should be able to transact large volumes of the ETF without a significant impact on bid/ask spreads. Regardless, if you attempt a very large transaction, it still makes sense to communicate with the ETF sponsor, so they can keep the market makers informed and ensure an orderly fill without spread impact.

## Summary of how ETFs trade

As Chris mentioned, **“DO NOT let someone tell you that an ETF is illiquid simply because it doesn’t trade a lot.”**  
Chris is correct. An ETF’s liquidity has everything to do with the underlying liquidity of the positions the ETF holds. This has a few implications:

* Pay attention to the liquidity on the holdings of your ETF–this will explain the spreads in the secondary market.
* Trade ETFs when the underlyings are liquid–avoid trading ETFs at the open or when the overall market volume is lackluster.
* Avoid huge market orders and stick to limit orders. Moreover, for huge trades, communicate directly with the market maker or your ETF trading desk.

[![Example of opening prices for some ETFs](https://alphaarchitect.com/wp-content/uploads/2014/12/How-ETFs-Trade-in-the-Secondary-Market_4.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/How-ETFs-Trade-in-the-Secondary-Market_4.png)

Also, a special note on trading ETFs at the open. Here is a live example from Friday, November 28th, the day after Thanksgiving, when the markets are not very active.

You’ll notice that this mid/large domestic-focused ETF is illiquid at open because the underlying names are illiquid. However, 3 minutes later, after the underlying has settled, the bid/ask tightens to reflect the underlying holdings’ liquidity.

First, the opening limit book on an ETF @ 9:30am with a fair value estimate is 25.32–huge spreads (23.78 x 26.82):

Next, the same limit book 3 minutes later @ 9:33am with a fair value estimate of 25.308–tighter spreads (25.25 x 25.36):

## [How ETFs Trade in the Secondary Market_5](https://alphaarchitect.com/wp-content/uploads/2014/12/How-ETFs-Trade-in-the-Secondary-Market_5.png)**What’s the lesson here on ETF trading?**

Trade ETFs like you would trade the underlying stocks in an ETF. If the underlying assets are illiquid, expect the ETF to be illiquid; if the underlying assets are liquid, expect the ETF to be liquid.

Better trading and execution will lead to better returns and happier investments. Go forth and compound!

Note: Bloomberg has a really cool feature called implied liquidity, which allows ETF buyers to grasp the true liquidity of an ETF better.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | In some ETFs, there is a possibility that it becomes so popular, and the secondary market becomes so deep, that an ETF can actually be more liquid than the underlying assets the ETF holds. For example, high-yield debt. Nonetheless, there is a tail-risk to this liquidity in the sense that the liquidity is driven by other ETF holders and not a market maker. To the extent ETF holders all demand liquidity at the same time and the liquidity of the ETF reverts to the underlying liquidity, there is a chance investors endure some pain. |

 function footnote\_expand\_reference\_container\_15358\_47() { jQuery('#footnote\_references\_container\_15358\_47').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_15358\_47').text('−'); } function footnote\_collapse\_reference\_container\_15358\_47() { jQuery('#footnote\_references\_container\_15358\_47').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_15358\_47').text('+'); } function footnote\_expand\_collapse\_reference\_container\_15358\_47() { if (jQuery('#footnote\_references\_container\_15358\_47').is(':hidden')) { footnote\_expand\_reference\_container\_15358\_47(); } else { footnote\_collapse\_reference\_container\_15358\_47(); } } function footnote\_moveToReference\_15358\_47(p\_str\_TargetID) { footnote\_expand\_reference\_container\_15358\_47(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_15358\_47(p\_str\_TargetID) { footnote\_expand\_reference\_container\_15358\_47(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
