---
title: "Shedding light on Payment for Order Flow: Insights from Emmet Peppers"
slug: "shedding-light-on-payment-for-order-flow-insights-from-emmet-peppers"
date: "2015-03-16"
modified: "2022-05-04"
url: "https://alphaarchitect.com/shedding-light-on-payment-for-order-flow-insights-from-emmet-peppers/"
categories: ["Interviews"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Shedding light on Payment for Order Flow: Insights from Emmet Peppers

> High frequent traders are armed with powerful weapons: mobs of PhD quants, super-computers, and sophisticated algorithms. HFT has provided wonderful liquidity benefits to the marketplace. Yet, […]

High frequent traders are armed with powerful weapons: mobs of PhD quants, super-computers, and sophisticated algorithms. HFT has provided wonderful liquidity benefits to the marketplace. Yet, as Michael Lewis’ book “Flash Boys” highlights, not all HFT is positive–some HFT participants “front run” traditional investors. The message from Lewis’ book is that traditional investors (both retail and institutional) are often left in the dust.

The details of [how HFT traders front run retail investors](https://alphaarchitect.com//2014/05/28/legal-case-hft-illegal/#.VQbknPzF9MU) has never been explained in great detail. We decided that it was time for a little education into the dark world of “[payment for order flow](http://www.sec.gov/answers/payordf.htm).”

We could have dived in on this project, but decided to recruit a professional: Emmet Peppers at [Interactive Brokers](https://www.interactivebrokers.com/ind/en/main.php).\* Emmet started out in 2002 sorting bins of returned mail as a temp worker at a major global investment bank and worked his way up to mid-level trade support manager for the bank’s trading floor.  In 2006 he made a lateral move to Interactive Brokers before moving into an institutional sales role. Emmet has been at IB for the past 5 years, selling IB’s Clearing, Execution, and Prime Brokerage services and technology to Hedge Funds, Advisors, Introducing Brokers, Prop Groups, and High Net Worth Investors/Traders.  Interactive Brokers is the largest brokerage firm in the United States as measured by Daily Average Revenue Trades (DARTs) and trades on over 100 market centers and 24 countries worldwide.

![Emmet](https://alphaarchitect.com/wp-content/uploads/2015/02/Emmet.jpg)

> Margin rates and commissions are not the only ways brokers make money from your brokerage/investment account.
>
> — Emmet Peppers.

### Interview:

#### ***What should brokerage clients know about brokerage costs?***

**Emmet:** Margin rates and commissions are not the only ways brokers make money from your brokerage/investment account.

#### ***How else do they make money then?***

**Emmet:** If you have not read “Flash Boys” yet by Michael Lewis then I will try to summarize: not only is it the commissions costs, but in many cases there is an additional much larger transaction cost, especially for bigger orders, embedded in your trade execution with your broker. Your order may get sold by your broker to an ‘internalizer’ or High Frequency Trading firm, who then makes even more money off your order [via the exchanges, ECNs, and/or dark pools] than they are paying your broker. Let’s just say these HFT firms who buy customer order flow from brokers are very profitable and run by very wealthy people.

#### ***Wait a second, I can imagine how a big market order can be manipulated, but what if I put my orders in as plain vanilla limit orders? Then if the market goes past my limit price I get filled and don’t have to worry about this ‘added cost’, isn’t that right?***

**Emmet:** You said it! If the market ‘goes past’ your limit price, your order should get filled anyway, so no big problem. But sometimes the market will touch your limit price and then go the other direction. This may be less frequent, but when it happens it can carry a huge ‘opportunity cost’ or it might cause you to be impatient and move your limit price to be more aggressive.

For example at the end of 2013, Facebook was a very hot stock and trading in the mid 50s going into 2014. Let’s say you decided you wanted to own FB if the stock price dropped a bit. On Jan 2nd you put in a buy limit order with your broker for 1000 shares and decided on a limit price of 51.85. This is a strategy you often employ: to buy stocks as they drop instead of chasing them on their way up. If FB would ‘correct’ by just a few points from its price on Jan 2nd 2014 [FB traded in a range between 54.19-55.22 that day] then you would get filled. As your limit order waits patiently, a few weeks later on Jan 27th, FB opens at 54.73 but actually traded as low as 51.85 during the course of the day before going back up and closing the day at 53.55.

Brokers who sell their customer order flow are unlikely to get any fill from the buyers of order flow until the stock actually trades below the limit price of the order they bought. This can be for many reasons that can bring up a whole other conversation, one obvious reason is because the buyers of order flow use the limit price as a free ‘option’ to try and gain pennies or to profit in brief arbitrage opportunities. In the above example, if you are with a broker who sells your order flow or internalizes it through some **proprietary dark pool**, then you may have **unnecessarily missed out** on buying up to 1000 shares of FB on what is now the 52 week low for FB stock as I write this.

#### ***Wow! That is one expensive ‘opportunity cost’, but doesn’t the type of example you outline seem like a very rare occurrence where everything has to line up just right?***

**Emmet:** Yes, the example I’ve given is an extreme example to get the point across. Even if this type of extreme example is only a 1 in 1000 occurrence, then it is still a relatively expensive cost averaged across 999 other trades. What if FB ends up going to 200 or 500 in one day? You could have owned it at 51.85, but because your broker sells its customer order flow your limit order was never filled.

What is actually a much more common occurrence is when someone puts in a limit order and then monitors the market as the price trades down towards their limit price. The stock price temporarily touches their limit price but then they see the market come right back up. *This innocent investor loses patience after a couple seconds and ends up moving their limit price higher to chase the stock for a slightly higher price.* They still get filled but perhaps at a higher price than if their broker was not selling their limit orders to HFTs. While this can still happen if your broker is not selling order flow, it would be much more common with a broker who does sell their customer order flow.

#### ***Are you saying Interactive Brokers doesn’t do this?***

**Emmet:**That is correct. We are the only broker to my knowledge that does not try to profit off of its customer order flow in any other way than commission. For example, the exchange/ECN “IEX” is touted in the “Flash Boys” book as the possible savior to this ‘**payment for order flow**’ cancer in our markets. While we believe our SMART routing algorithm does a better job than IEX, if any of our clients want to route all of their orders to IEX directly instead of through our SMART routing then we will do that for them at no extra cost. I do not know of any other broker out there that would let its clients route all of their orders to IEX at no extra cost.

#### ***This is fascinating, have there been any actual studies or statistics that help show this added ‘payment for order flow’ cost?***

**Emmet:**As a matter of fact our Chairman, Thomas Peterffy, put out [a letter to the SEC](https://institutions.interactivebrokers.com/download/execution_stats_comment_letter.pdf) in August that highlights a stat we now publish monthly. It is a single number showing what our all-in transaction cost truly is. For IB it is about ~1 basis point per transaction. If other brokers published this same stat then investors and traders could compare the true transaction cost between different brokers. The problem is that a lot of brokers and ‘third parties’ funded by brokers publish their own execution stats which are derived in deceiving ways. For example, I once saw an execution quality stat being marketed by one of the major online brokers we all know. The stat looked impressive at first glance but when reading the fine print I learned that their stat only represented the average price improvement of orders that were price improved. There were also orders that weren’t price improved, and more than likely dis-improved, that were excluded entirely from the execution quality stat the broker was publishing. It would be like a football team saying “I win by an average of 10 points per game” but not including any of their losses in that stat. A football team like that could still be 2-14 for the season!

#### ***Yes, I’ve come across those types of statistics before which is why I don’t trust any stats on execution quality anymore.***

**Emmet:**I agree. Brokerage is a business with a lot of ‘smoke and mirrors’ that have evolved over time, especially with trade execution. The sophisticated institutional traders know this, which is why you don’t see any billion dollar hedge funds sending their large orders to online brokers for a flat $5.95 ticket charge. Instead they execute their orders through institutional brokers and typically pay pennies or fractions of pennies per share. What some of these institutional traders are realizing now, per Flash Boys, is that their institutional brokers are also profiting off of their orders in other ways than just commission.

#### ***Sounds a bit hopeless, doesn’t it?***

**Emmet:**In the end I would like to think **transparency will win** somehow. *Perhaps one day some third party could publish a study exposing these execution quality costs between brokers.* They could start with the same size account at IB and a few of the larger online brokers and execute the same strategy simultaneously over the course of a year, even using just limit orders to keep it simple. As the year went on, the third party could publish their findings on the difference in return for running the same exact investment/trading strategy at each of the brokers. I think many people who are fed up with deception in the financial industry would be curious to see how big a difference the performance would be with each broker as the year went on.

### You might be onto something there Mr. Peppers…

————————————–  
Emmet is more than happy to speak further with anyone who is interested in this stuff. His email is: **epeppers@interactivebrokers.com**. Feel free to contact him!

\*Our firm is currently a client of Interactive Brokers. We have received no direct or indirect compensation for posting this material.
