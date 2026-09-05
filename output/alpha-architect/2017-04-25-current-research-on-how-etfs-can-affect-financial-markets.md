---
title: "How ETFs Might Affect Financial Markets"
slug: "current-research-on-how-etfs-can-affect-financial-markets"
date: "2017-04-25"
modified: "2022-05-11"
url: "https://alphaarchitect.com/current-research-on-how-etfs-can-affect-financial-markets/"
categories: ["Uncategorized"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# How ETFs Might Affect Financial Markets

> We’ve heard a lot of questions recently from clients and readers regarding how ETFs might affect financial markets. The short answer is “nobody knows.” The […]

We’ve heard a lot of questions recently from clients and readers regarding how ETFs might affect financial markets.

The short answer is “nobody knows.” The long answer is researchers are trying to figure it all out.

In this piece we inventory some of the more interesting research articles on the subject and encourage readers to explore these articles in depth.

## How ETFs Might Influence Markets

I’ve already written a bit about how ETFs are impacting asset prices via an article I shared at ETF.com. Here [is a link](http://www.etf.com/sections/etf-strategist-corner/how-etfs-are-impacting-asset-pricing). The piece [discussed some work](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2800590) from Lin William Cong and Doug Xu, which delivered 3 core predictions:

1. **Market Efficiency Increases:** ETFs, or “composite securities,” should improve overall price efficiency, and the impact is bigger for relatively illiquid assets. However, the authors do make the point that firm-specific news might actually get incorporated into prices more slowly. Ironically, as algo-driven ETFs displace “stock-pickers,” stock-pickers might find that their nuanced information collection abilities could become more valuable.
2. **Volatility and Correlations Increases:** ETFs could increase asset volatility and correlations across baskets that have similar systematic factor exposures. On one hand, this is to be expected if systematic factor exposures are being priced more accurately. On the other hand, portfolio diversification assumptions of the past may not hold into the future, if the diversification benefits across composite portfolios increases.
3. **Mixed Liquidity and Price Impact Effects:** The authors find that transaction costs and impact costs might increase for illiquid securities. However, the authors find that overall costs to trade securities driven by systematic factors may decrease when traded via composite securities such as ETFs.

This research is great, but there are other researchers with equally compelling and insightful thoughts on how the ETF vehicle might affect the markets. They also bring more data to the theoretical discussion.

For example, we [conducted an interview](https://alphaarchitect.com/2016/12/13/an-interview-with-a-leading-academic-expert-on-etfs/) with Zahi Ben-David, who co-authored some great work with Prof. Francesco Franzoni (University of Lugano) and Prof. Rabih Moussawi (Villanova University) on ETFs and their influence on the stock market. Their original paper is [posted here](https://ssrn.com/abstract=1967599) and their survey paper is [posted here]( https://ssrn.com/abstract=2865734). A summary of their research findings in the words of Zahi:

> Our main result is that **ownership by ETFs cause prices of the underlying stocks to be noisier**. This is a causal claim, i.e., the ownership by ETFs increases the volatility of the underlying stocks. We know that this volatility is noise since sharp changes in flows at the ETF level causes price changes in underlying stocks, which tend to reverse after a few days.

Zahi has some interesting comments on the potential liquidity benefits and costs of ETFs:

> ETFs appear to be a double-edge sword for the liquidity of the underlying securities. On one hand, **they provide liquidity** because arbitrageurs (during normal market conditions) are quick to close any mispricings between ETFs and the underlying securities. So, a market price move is transmitted quickly to the underlying stocks.

And now the downside:

> On the other hand, ETFs **crowd out liquidity from the securities to the ETF**. This means that investors who use to trade the underlying securities directly in the past, prefer now to trade the ETF – it is cheaper and easier. This means that we lose liquidity at the stock level. One implication of this is that stock returns become less informative about companies’ financial prospects.

These findings corroborate with many of the theoretical predictions highlights in the work by Cong and Xu that I discussed earlier.

Jack did a great job digging into a [really cool paper](https://alphaarchitect.com/2017/04/12/how-are-etfs-affecting-the-stock-market-is-there-a-dark-side-to-etfs/) that expands on one of the predictions from Cong and Xu. Namely, an analysis of ETFs may help “asset prices to better reflect systematic information, but less asset-specific information.” A key feature of this empirical analysis is that their results reflect a correlation between changes in ETF ownership and changes in firms’ trading costs and pricing efficiency, but not causation. So certainly an interesting finding, but we definitely need more theory and thinking to definitely make a claim that ETFs are causing a ruckus in underlying liquidity and pricing efficiency of stocks.

Some more recent theoretical literature is coming down the pipe and further expands upon the ideas above. For example, “[Can ETFs Increase Market Fragility? Effect of Information Linkages in ETF Markets](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2740699),” by Ayan Bhattacharya and Maureen O’Hara, highlight a very interesting kink in the ETF armor when it comes to trading harder to trade securities (illiquid or tough to access for most investors).

Here is the paper’s abstract:

> We show how inter-market information linkages in ETFs can lead to market instability and herding. **When underlying assets are hard-to-trade**, informed trading may take place in the ETF. Underlying market makers, then, **have an incentive to learn from ETF price**. We demonstrate that this learning is imperfect: market makers pick up information unrelated to asset value along with pertinent information. **This leads to propagation of shocks unrelated to fundamentals and causes market instability**. Further, if market makers cannot instantaneously synchronize prices, inter-market learning can lead to herding, where speculators across markets trade identically, unhinged from fundamentals.

In English, typically market prices are established on the underlying assets and the ETF vehicle simply reflects these values. However, this assumes the ETF vehicle is the sideshow and the underlying stocks are the main event. But what happens when the ETF is the main event and the underlying assets become more of the sideshow? Now the supply/demand dynamics of the ETF vehicle, which may or may not be related to the fundamental values of the underlying asses in the ETF basket, can create manufactured noise, and thus more volatility and instability in the underlying assets. These effects are especially important for the harder-to-trade assets where arbitrage is costly and the supply/demand dynamics from the ETF market are more likely to be based on noise.

The authors deploy the model in the context of the GREK ETF from 2014 to 2015, with a particular eye on the Greek debt crisis in the summer of 2015. They find that their model does a decent job describing some of the events that took place. In addition, the authors laundry list their top policy concern and some potential solutions:

* Problem: ETFs can potentially enhance volatility and distort pricing for individual hard-to-trade securities. (The mechanism is similar to “noise trader risk,” which is [described in this article](https://alphaarchitect.com/2015/06/08/behavioral-finance-part-behavior-part-market-frictions/))
  + Solutions: Only allow ETFs to trade in easier-to-trade securities; make the basket sizes smaller; and/or increase the transparency related to the securities in the underlying baskets

Finally, a hot off the press paper from Kevin Pan and Yao Zeng, “[ETF Arbitrage Under Liquidity Mismatch](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2895478),” follows a similar path to the papers above and highlights that there are potential problems when there is a liquidity mismatch between the ETF (liquid) and the underlying (illiquid). This research is focused on corporate bond markets, in particular, where there is an identifiable conflict of interest that market makers (“APs”) face and some data to explore their hypothesis.

First, what is the conflict market makers face when trading illiquid bonds? Well, because bonds are relatively illiquid, market makers end up having to hold some level of inventory in the underlying bonds. If this inventory is relatively small, APs have an incentive to arbitrage mispricings across the ETF price and the ETF NAV. However, if a market maker stacks up a substantial inventory of bonds, they may have an incentive to par down their balance sheet risk, regardless of potential arbitrage opportunities. For example, if I’m a market maker and I’ve created a substantial long position in bonds, I may do some ETF creates to drop my inventory, even if the ETF is trading a discount to the underlyings! So in some cases, a market maker may distort the arbitrage pricing mechanism, not enhance it! One can imagine how this might play out in a fast-moving market where there are increased capital and regulatory constraints (i.e., AP inventory needs to be cut down). In these situations, presumably in a tough market, a market maker may decide to deliver their bonds in for discounted ETF shares, thus making the ETF discount even more extreme. If secondary ETF holders were hoping to sell their ETF positions at roughly fair value, they may be surprised that they are on the same side of the ETF trade as the market makers. Obviously, this could create a problem. At least in theory.

## Are ETFs Weapons of Mass Financial Destruction?

Consumers are overwhelmingly voting with their feet when it comes to ETFs. These vehicles are often cheaper, more tax-efficient, more transparent, and easier to use than traditional vehicles.

*Are ETFs a panacea?* Definitely not.

*Should there be an ETF for every asset class and exposure in the world?* Probably not.

The research described above on hard-to-trade assets and corporate bond ETFs are both interesting case studies that suggest investors and policy makers should dig into the weeds and possibly slow down the innovation in areas of the market where there could be large unforeseen risks. All that said, I’m an optimist and a fan of free-market competition and innovation. With enough time, and in close coordination with regulators, I’m sure there are smart methods to help ETF providers help financial consumers in the more esoteric corners of the investment world.

And what about the broader implications regarding ETFs and their effects on underlying asset volatility and mispricing? The literature above seems to suggest this is inevitable and a cost society should consider relative to the expected benefits the ETF structure can bring to the table. But we should ask an important question: What is the baseline? We already know that there have been noise trader effects in individual stock issues for as long as markets have been around. These noise trades create distortions in underlying securities, increase volatility, and distort market efficiency. If these noise traders stop trading stocks and start trading ETFs, is the net effect on volatility and market efficiency essentially zero? Or will there be a significant marginal increase in problems because of the ETF structure? Hard to say without a ton of data and a lot of brain damage, but my gut instinct suggests that the ETF simply shifts where noise traders transact — from the individual stock to the ETF. I doubt there will be many structural affects on the market as a whole over the long term. But who knows. I guess we’ll have to find out in real-time.

Thanks for reading.

[![](https://alphaarchitect.com/wp-content/uploads/2017/04/etf-waves-1030x642.png)](https://alphaarchitect.com/wp-content/uploads/2017/04/etf-waves.png)
