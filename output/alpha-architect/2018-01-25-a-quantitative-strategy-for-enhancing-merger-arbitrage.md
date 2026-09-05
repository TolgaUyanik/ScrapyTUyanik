---
title: "A Quantitative Strategy for Enhancing Merger Arbitrage"
slug: "a-quantitative-strategy-for-enhancing-merger-arbitrage"
date: "2018-01-25"
modified: "2022-05-13"
url: "https://alphaarchitect.com/a-quantitative-strategy-for-enhancing-merger-arbitrage/"
categories: ["Research Insights", "Guest Posts"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# A Quantitative Strategy for Enhancing Merger Arbitrage

> Merger arbitrage, sometimes known as “risk arbitrage,” is an investing strategy in which the investor bets on announced M&A deals. After a merger is announced, […]

Merger arbitrage, sometimes known as “risk arbitrage,” is an investing strategy in which the investor bets on announced M&A deals. After a merger is announced, shares of the target tend to trade below the offered price (due to deal uncertainty), representing the arbitrage spread; if the deal is successful, the price moves up and the investor earns the spread.

Merger arbitrage situations are generally of two types:

* All-Cash Offer: the investor simply buys the target stock, and holds until the deal is complete.
* All-Stock offer: the investor purchases shares in the target, and shorts an amount of the acquirer’s stock at the ratio at which the target’s stock will be exchanged for the acquirer’s stock if the deal goes through.

Merger arbitrage funds tend to grind along offering bond-like single-digit returns, and in theory, should provide a premium that is uncorrelated with the market and thus offer diversification benefits.

## **So Why isn’t Everyone doing Merger Arbitrage?**

As Charlie Munger says, “invert, always invert,” so let’s start with why merger arbitrage may NOT be such a great strategy.

The main risk in any merger arbitrage trade is that the deal fails to close. When that happens the target’s stock may fall to the level where it traded before the announcement, and if the buyout premium was substantial, this can result in a loss for the merger arbitrage investor (so much for “arbitrage”).

Thus, in general, the merger arbitrage trade is one in which you *can make a little, but can lose a lot*. It’s like picking up nickels in front of the proverbial steamroller. One of the best academic papers on this subject comes from Mark Mitchell and Todd Pulvino in their paper, “[Characteristics of Risk and Return in Risk Arbitrage.](https://faculty.chicagobooth.edu/john.cochrane/teaching/35150_advanced_investments/mitchell%20pulvino%20characteristics%20of%20risk%20and%20return%20JF.pdf)” Here is an [old post](https://alphaarchitect.com/2016/04/28/facts-fiction-merger-arbitrage/) on the subject that summarizes their research along with the core graphic from the paper that highlights the dynamic beta of merger arbitrage:  
![](https://alphaarchitect.com/wp-content/uploads/2016/04/2016-04-28-14_09_08-mitchell-pulvino-characteristics-of-risk-and-return-JF-Copy.pdf-Adobe-Acroba.png)  
**Evaluating Merger Arbitrage Deals**

So how do you avoid you steam roller? There are so many things that can go wrong in any merger arbitrage deal that could flatten the investor. Maybe the target can’t meet the terms of the merger or obtain shareholder approval. Maybe the deal runs into regulatory issues, or there is a competing bid. If you’re not a merger arb specialist, how do you know which deals to invest in?

What we need is a quantitative signal that can help us identify the bad deals that won’t go on to close, so we don’t invest in them.

## **Academics to the Rescue**

In “[Merger Options and Risk Arbitrage](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr761.pdf?la=en),” by Peter Van Tassel, the author investigates a novel, and very clever, approach to identifying the risk of deal failure, using joint information contained in target stock and options markets to assess the probability of deal success.

## **Cash Deal – Offer Effects on Target Stock**

To see how this works, consider an all-cash deal. At the announcement, the stock price consists of a weighted average of 1) the cash offer, and 2) the present value of dividends. The announcement has shifted the weight from all dividends to part cash. Since cash has zero volatility, the target’s stock price at-the-money volatility is therefore reduced. Simultaneously, if the deal fails the stock will fall to the level near where it was prior to the offer, a potential out-of-the-money or “fat-tail” event that increases the stock price’s skewness and kurtosis. A similar dynamic is at work in stock deals, when the acquirer’s stock is less volatile than the target stock.

## **The Volatility Smile**

Target options contain information about these higher moments in the stock price: lower implied volatility at-the-money and higher implied volatility out-of-the-money give rise to a volatility smile:

[![](https://alphaarchitect.com/wp-content/uploads/2017/06/volatility-smile.png)](https://alphaarchitect.com/wp-content/uploads/2017/06/volatility-smile.png)  
In short, deals with a high probability of success tend to exhibit the volatility smile, due to the higher weighting on the cash component of the stock price.

Furthermore, the more pronounced the volatility smile, the more likely the deals are to be ex-post successful. For example, at-the-money implied volatility decreases over 60% in successful deals but only 25% in failed deals.(1)

## **Can You Pick the Merger Arb Deal That Closed?**

Now that we know something about the volatility smile, take a look at the two graphs below, which show pre- and post-announcement implied volatilities for two separate merger arb transactions.

Can you guess which deal closed?

[![](https://alphaarchitect.com/wp-content/uploads/2017/06/vol-smile-example.png)](https://alphaarchitect.com/wp-content/uploads/2017/06/vol-smile-example.png)  
If you noticed the pronounced volatility smile (the red “V”) post-announcement for the deal on the left, you are on your way to becoming a hot-shot merger arb specialist!

So let’s take this strategy out for a spin, and analyze portfolio returns.

## **The Sample**

The sample included 3,836 deals (2,856 cash deals, and 980 stock deals) over a period running from 1996 through 2012. Targets were US public companies in which acquirers sought a majority stake, with payouts in cash or a fixed amount of acquirer shares. The subset of deals with options data included 1,094 deals, consisting of 744 cash deals and 350 stock deals.

## **Portfolio Returns**

In Table 3 below, “Arb” strategies invest in all deals – cash, stock, and hybrid deals – while “Cash” strategies invest exclusively in cash deals. “Equal” refers to equal-weight portfolios (i.e., simply equal weight all the deals in the sample), while “HP” refers to the high probability merger arb strategy outlined above. The four columns on the left, “Hedge Fund Indexes,” provide a baseline for comparison.

[![](https://alphaarchitect.com/wp-content/uploads/2017/09/mergerarb-1.png)](https://alphaarchitect.com/wp-content/uploads/2017/09/mergerarb-1.png)  
What do you notice? The “Arb HP” strategy obtains a Sharpe ratio of 0.5364 that is over 50% higher than the Sharpe of 0.3276 for an “Arb Equal,” equal weighted portfolio of all the deals in the sample. Not that this nearly *doubles* the CAPM alpha t-statistic, from 4.4368 to 8.4600. Wow. Also, based on the strong Sharpe ratio, the Arb HP strategy seems to handily outperform all the Hedge Fund Indexes. And look at the max drawdown for Arb HP! It’s a mere 2.78%! It seems like the strategy has eliminated almost all of the failed deals from the sample. That’s pretty impressive. Would it be reasonable to use some leverage with this strategy? Could be.

## **Summary**

There’s a lot more interesting analysis in this paper, so curious investors should dive in, but in short, the paper demonstrates how a parsimonious quant model can enhance merger arb returns by accurately forecasting deal outcomes. Who needs a human being to weigh in on merger arb portfolio formation?! Seems like in the aggregate they subtract value from the model. Certainly, if human merger arb specialists are not currently using option prices to inform their decision about whether to invest in certain merger arb deals, perhaps they should consider it.

---

### Merger Options and Risk Arbitrage

* Peter Van Tassel
* A version of the paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2718868).
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap](https://alphaarchitect.com/category/architect-academic-insights/academic-research/#gs.l2xpspQ) Category.

### Abstract:

> Option prices embed predictive content for the outcomes of pending mergers and acquisitions. This is particularly important in merger arbitrage, where deal failure is a key risk. In this paper, I propose a dynamic asset pricing model that exploits the joint information in target stock and option prices to forecast deal outcomes. By analyzing how deal announcements affect the level and higher moments of target stock prices, the model yields better forecasts than existing methods. In addition, the model accurately predicts that merger arbitrage exhibits low volatility and a large Sharpe ratio when deals are likely to succeed.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | Here’s an example of a pronounced volatility smile…har har… |

 function footnote\_expand\_reference\_container\_29167\_185() { jQuery('#footnote\_references\_container\_29167\_185').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_29167\_185').text('−'); } function footnote\_collapse\_reference\_container\_29167\_185() { jQuery('#footnote\_references\_container\_29167\_185').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_29167\_185').text('+'); } function footnote\_expand\_collapse\_reference\_container\_29167\_185() { if (jQuery('#footnote\_references\_container\_29167\_185').is(':hidden')) { footnote\_expand\_reference\_container\_29167\_185(); } else { footnote\_collapse\_reference\_container\_29167\_185(); } } function footnote\_moveToReference\_29167\_185(p\_str\_TargetID) { footnote\_expand\_reference\_container\_29167\_185(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_29167\_185(p\_str\_TargetID) { footnote\_expand\_reference\_container\_29167\_185(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
