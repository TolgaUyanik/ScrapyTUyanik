---
title: "Discussion: Managing the Costs of Passively Investing in Active Strategies"
slug: "discussion-managing-the-costs-of-passively-investing-in-active-strategies"
date: "2020-05-14"
modified: "2022-05-20"
url: "https://alphaarchitect.com/discussion-managing-the-costs-of-passively-investing-in-active-strategies/"
categories: ["Research Insights", "Academic Research Insight", "Active and Passive Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Discussion: Managing the Costs of Passively Investing in Active Strategies

> We recently covered a paper by David Blitz that highlighted the potential problems with passively investing in “active” strategies. The research piece is great and […]

[We recently covered a paper](https://alphaarchitect.com/2020/05/04/why-passively-investing-in-active-methods-may-not-work/) by David Blitz that highlighted the potential problems with passively investing in “active” strategies. The research piece is great and surfaces a lot of great concepts. Like a lot of research we publish/summarize this article appears to “shoot Alpha Architect in the foot.” To summarize, the piece was essentially a smack-down on implementing factors via ETFs versus mutual funds.(1) By design, this quick blog post is meant to serve as a counter-weight to the points discussed by Blitz. When it comes to taking a stand on the debate, we are like Switzerland — neutral. We simply see a set of different costs/benefits, but no “correct” answers for every single situation. Mutual fund, active ETF, Index ETF, insurance-wraps, structured-products, Hedge Fund, SMA, etc — all have different costs/benefits and different use cases.

So without further ado, let’s dig into the interesting insights discussed by David Blitz.

## What are the Issues Blitz Raises?

### **Performance accountability is weaker in the passive framework**

There is an inherent limitation to fiduciary responsibility and performance accountability in the passive methodology. The index provider only provides paper portfolios and therefore is not incentivized to outperform the market after fees and costs. The index replicator is only incentivized to produce performance numbers that match the paper portfolio.  The role of fiduciary ultimately defaults to investors who typically take a more charitable view of performance for index replicators than active managers themselves, especially with respect to underperformance and may be in a weak position to evaluate the product.

#### Comments

* Without a doubt, there are Index providers whose sole purpose in life is to match the benchmark with perfection, even if it means engaging in terrible trading practices and/or it guarantees a poor investment result for the client.
* Despite the above comment, ETF sponsors do have flexibility in tracking an index with different tracking error constraints and requirements related to their goal of tracking a given Index. For example, the prospectus may state that the ETF sponsor needs to own at least 80% of the index constituents or have a goal of maintaining less than 5 percentage points in benchmark drift a year. These sorts of rules provide a lot of flexibility for ETF sponsors to track an index, but also be savvy on trading and execution.
* One can also build an index to incorporate sensible concepts, systematically. Worried about bad execution? Fine, build some pre-trade execution program into the index methodology.
* Skin in the game is also a nice solution. How much personal capital does the ETF sponsor invest in their own products? If the operators behind the ETF have skin in the game, they will be more likely to engage in activity that maximizes the expected benefits for the ETF and maybe not be so beholden to “track the index” as if it were a religious law to have 0.0000% tracking error as an index fund.

### **Efficiency of trading is also weaker**

Factor index replicators are constrained by a lack of flexibility in trading that results in higher costs of trading when compared to active managers.  Maintaining active factor exposures requires active trading, although most index providers rebalance quarterly or semiannually.  That practice forces trading in large amounts into a concentrated period of time (usually a few days) on an annual basis. This eliminates the opportunity to engage in opportunistic events that require trading in smaller amounts over longer periods. For example, active managers enjoy a number of advantages including the ability to identify cheap block trading opportunities, the ability to use fund inflows to purchase highly ranked stocks and selling off poorly ranked stocks.  The passive methodology essentially shuts out those types of liquidity events and alpha-generating opportunities. As a result, passive investors are subject to relatively higher trading and market impact costs.

#### Comments

* As long as a process is systematic, it can be built into an Index and implemented as such. There are plenty of Index methodology documents that build in dynamic changes that are unaffiliated with a standard rebalance period.
* Depending on the strategy/factor, it is empirically unclear that active rebalancing is better than scheduled rebalancing — especially if there are seasonality effects and/or the signal/noise ratio is high. Active rebalancing can end up being more expensive from a transaction costs perspective if it encourages more activity and if 1) the trading activity doesn’t actually add value and 2) is systematically turned on when trading costs are the highest (i.e., during a crisis).
* ETF sponsors can implement slippage models as part of their regular-scheduled rebalance process. For example, let’s say you want to own the 50 cheapest stocks in an index. You run your quarterly rebalance and you own 1 stock that is ranked #51. On one hand, you could eat a full transaction costs and sell the #51 stock, but on the other hand, you could avoid the transaction cost and hold the #51 stock. Portfolio managers can use tools that weigh the cost/benefits of “drifting from a model” versus the reality of transaction costs. Portfolio managers — even those managing funds to an Index — actually have a decent amount of flexibility to track an index, but also do their best for the specific fund they are managing, even if it results in some index tracking error.

### **Passive funds have little to no control over capacity**

Furthermore, the culture, mindset and most importantly the business model of passive management is decidedly inconsistent with capacity control. The ability to attract assets, to increase the size of a passive fund are instead considered indicators of success as the fund becomes increasingly able to benefit from economies of scale. In contrast, asset-gathering takes a back seat to generating excess returns as the first priority for active managers.  They also have the ability to close funds to new investors if capacity limits are exceeded and generally expected to do so in order to protect performance.

#### Comments

* True. There are very limited means that an ETF can leverage to limit creation/redemptions. The vehicles are highly transparent with easy access/exit rules, by design.
* While theoretically true, one can probably count on one hand the number of highly successful mutual funds that “limited their capacity” because they cared about their clients. The more likely case is they hired a 100 wholesalers because the profit incentive to raise AUM outweighed the incentive to constrain the capital to maximize the expected performance. To factcheck this situation, simply look at the funds that “constrain capacity” and then review what percentage of their resources are dedicated to distribution. If the fund is actually locked and the firm is 99% research/operations, great, if the fund is “locked” and 50% plus of the resources are dedicated to selling, well, something doesn’t smell right.

### **Opportunities to manipulate prices or arbitrage**

There are at least two issues associated with trading activity associated with the time lag that occurs due to the preannouncement of trades by index providers. Since the reconstitution of the index is announced prior to the actual trade date, there is a window of time available for other investors to act and profit by providing liquidity necessitated by the index provider. For example, hedge funds engage in index arbitrage by taking the opposite side of the index trade while the cost is borne by index investors.  More significantly, the window also provides the index replicator an opportunity to influence prices of the stocks moving in and out of the index. A clear conflict of interest.

#### Comments

* One small clarification on timing options available to ETF sponsors tracking an index. ETF sponsors and Index providers don’t necessarily have to set things up as Blitz describes. The ETF sponsor can actually trade ahead of time to be inline with an index so that when the index is officially announced the fund and the index are in sync. Of course, the ETF sponsor and the index can also use the approach outlined in the critique: index released; ETF trades to the index.
* Determining which approach is the “best” is actually extremely complicated. Trading transparency and regularity can potentially lead to efficient execution. For example, if the market making community as a whole is competing to provide liquidity for a highly transparent Index fund attempting to shift in/out of stocks, there is an argument that their execution costs may be lower than the “active fund” that is highly opaque and secretive with their trading activity. Eventually, these “secret” traders need to confront a market maker, who will add a high-risk premium in their bid/ask when they are trading off against an unknown market participant versus a highly transparent market participant. The empirical question is whether or not the liquidity costs of “avoiding frontrunning” are actually lower than the cost of an approach that says, “Please, front-run me. We think you market makers are competitive dogs and will deliver us really cheap liquidity if we tell you exactly what we are doing. Have fun.” In short, when it comes to rebalancing/execution costs and the different approaches, it’s complicated and to say that there is a “right” answer in today’s complex world of trading and execution is a bold statement.

### **Passive strategies tend to be static**

Index providers (and therefore replicators) resist changes to their methodology regardless of obvious improvements that could and should be made.  To a certain degree, the resistance can be justified if the index is widely known and used by investors for benchmarking or risk control.  Such unintended turnover in the replicated portfolio can be costly and undesirable from the index investor’s point of view.  On the other hand, change is the currency of the active manager.  As market-beating performance is the objective, it is imperative that active managers have the flexibility to improve strategies.

#### Comments

* True. The ability for an index to adapt and change is difficult and compliance-heavy, by design. The whole point of a systematic index is to follow a rule book that everyone understands ahead of time.
* On the flip side, being active gives the porfolio manager an ability to change and adapt with fewer frictional costs. And while this may sound intuitively appealing, the reality is that investing is a high signal/noise process and the empirical realities are well-studied and understood. The idea that a portfolio manager is magically finding gold nuggets on a regular basis is probably unrealistic.

## Summary

There are no clear cut answers on the questions raised by Blitz. This piece is meant to serve as a balance to the comments made so readers can hear both sides of the arguments. The reality is we take no strong stance on either side of the argument — there are simply costs and benefits to every approach and the role of an advisor or asset manager is to navigate complexities as best they can and deliver their best effort to their clients. Hope you enjoyed this short piece and let us know if you have comments and/or insights.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | Why discuss research that goes against the grain? First, our mission is to *empower investors through education*, not *empower investors through propaganda*. Second, we embrace research that highlights the controversy around what we do as a firm — it is impossible to be perfect; we believe the world is simply full of trade-offs and we seek to identify the best set of trade-offs that works for our firm and our clients. |

 function footnote\_expand\_reference\_container\_56786\_113() { jQuery('#footnote\_references\_container\_56786\_113').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_56786\_113').text('−'); } function footnote\_collapse\_reference\_container\_56786\_113() { jQuery('#footnote\_references\_container\_56786\_113').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_56786\_113').text('+'); } function footnote\_expand\_collapse\_reference\_container\_56786\_113() { if (jQuery('#footnote\_references\_container\_56786\_113').is(':hidden')) { footnote\_expand\_reference\_container\_56786\_113(); } else { footnote\_collapse\_reference\_container\_56786\_113(); } } function footnote\_moveToReference\_56786\_113(p\_str\_TargetID) { footnote\_expand\_reference\_container\_56786\_113(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_56786\_113(p\_str\_TargetID) { footnote\_expand\_reference\_container\_56786\_113(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
