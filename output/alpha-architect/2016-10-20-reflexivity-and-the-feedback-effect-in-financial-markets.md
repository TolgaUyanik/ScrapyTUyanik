---
title: "Reflexivity and the Feedback Effect in Financial Markets"
slug: "reflexivity-and-the-feedback-effect-in-financial-markets"
date: "2016-10-20"
modified: "2022-05-10"
url: "https://alphaarchitect.com/reflexivity-and-the-feedback-effect-in-financial-markets/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Reflexivity and the Feedback Effect in Financial Markets

> Eugene Fama’s Efficient Market Hypothesis argues that because stock prices follow a “random walk,” future price behavior cannot be predicted. In his seminal paper, “Random Walks […]

Eugene Fama’s Efficient Market Hypothesis argues that because stock prices follow a “random walk,” future price behavior cannot be predicted. In his seminal paper, “[Random Walks in Stock Market Prices](http://www.cfapubs.org/doi/pdf/10.2469/faj.v51.n1.1861),” he explains the relationship between prices and fundamentals:

> If the random-walk theory is valid and if security exchanges are “efficient” markets, then stock prices at any point in time will represent good estimates of intrinsic or fundamental values.

In this view, fundamentals may evolve and change, and prices will change to reflect them. Cause and effect are unidirectional: changes in fundamentals affect prices, but prices do not affect fundamentals. But some feel that cause and effect may be bidirectional, and that prices can sometimes alter fundamentals. (note: We argue that reflexivity might explain the so-called “momentum effect,” which we discuss in detail in [Quantitative Momentum](https://alphaarchitect.com/2016/10/05/quantitative-momentum-a-guide-to-momentum-based-stock-selection/) (reader’s digest [version here](https://alphaarchitect.com/2015/12/01/quantitative-momentum-investing-philosophy/))).

### Reflexivity

Back in 1987, George Soros published “[The Alchemy of Finance](https://www.amazon.com/Alchemy-Finance-George-Soros/dp/0471445495),” in which he described his “theory of reflexivity.” Soros’s concept of reflexivity involves a few interrelated ideas:

1. Human judgment is flawed, and humans are fallible. We understand the world only imperfectly.
2. As flawed humans, we can improperly perceive stock fundamentals. Thus, prices can be wrong since they are based on our faulty perceptions of fundamental value. In this view, prices can be subjective, rather than always being purely objective, as they are under Eugene Fama’s Efficient Market Hypothesis.
3. Changes in prices can influence the fundamentals of stocks. Stated another way, the way we perceive fundamentals and how this affects price can cause fundamentals themselves to change.

Reflexivity thus describes an iterative process: Prices set by irrational market participants affect the fundamentals, which affect prices, etc., in a “reflexive” feedback loop.

### How can prices affect fundamentals?

As Soros has put it:

> Usually some error in the act of valuation is involved. The most common error is a failure to recognize that a so-called fundamental value is not really independent of the act of valuation. That was the case in the conglomerate boom, where per-share earnings growth could be manufactured by acquisitions, and also in the international lending boom where the lending activities of the banks helped im­prove the debt ratios that banks used to guide them in their lending activity.

Soros refers to how during the conglomerate boom during the 1960s, companies used their high stock prices to make accretive acquisitions that increased EPS, leading the market to assign them a higher P/E, which boosted their buyout currency and enhanced their ability to make more acquisitions.

Prices can also affect fundamentals in other ways. For instance, a high stock price might enable a company to attract the best talent, and thereby drive growth. A high stock price might enable a secondary offering to raise growth capital, which would accelerate the business. In these cases, perceptions, which are reflected in stock prices, become a self-fulfilling prophecy, as they alter the fundamentals in a self-perpetuating feedback loop. A reflexive feedback loop can also be self-correcting: A low stock price might induce a company to repurchase shares, enhancing EPS, and sending prices rebounding higher.

### Modelling another type of reflexivity

In a new paper, “[Feedback Effects, Asymmetric Trading, and the Limits to Arbitrage](http://finance.wharton.upenn.edu/~itayg/Files/limitstoarbitrage-published.pdf),” by Edmans, Goldstein and Jiang, the authors describe a “feedback effect” that has similarities to reflexivity. They propose a model for how stock prices can influence corporate decision-making that affects fundamentals, which in turn, impacts prices.

The paper provides a great example that illustrates the concept.

In September, 2001, Hewlett Packard announced it intended to purchase Compaq Corporation. The market HATED the idea, and sent the stock plummeting 19% on the day of the announcement. One reason for the big price move was that HP’s board was unanimous in its support for the deal. Although this was a terrible value-destroying deal, it looked very likely that it was going to get done.

The implications of the huge drop in price were not lost on one board member, Walter Hewlett. Hewlett was the son of HP’s founder, and was chairman of the Hewlett Foundation — HP’s second largest shareholder. After the stock price drop, Hewlett announced he opposed the deal. HP’s share price rallied 17% on the news, because Walter Hewlett posed a credible threat to the deal. In this case, the market signaled that the firm’s purchase of Compaq was a negative NPV project, and the information signal was strong enough to get a key decision-maker at HP to change his mind.

If you were a short seller who sold short HP on the Compaq announcement, you would have expected the deal to go through. You would also have been surprised by *the reaction to your selling*: An HP board member threatened to cancel the deal. In the presence of the “feedback effect” from changing prices, Walter Hewlett did something unexpected.

A savvy investor would need to anticipate these second order effects of their own actions. If you were a short seller in this situation, you might be hesitant to sell very aggressively if you were concerned that your selling could cause Hewlett or others to change their decision.

These effects can hold not only in cases of acquisition, but also in a new product launch, or a change in strategy. In any of these cases, decision-makers at the firm can use price signals to make a smarter decision. If you are a manager and you make an announcement that sends your share price plummeting, well then maybe that wasn’t such a hot idea after all, right?

### The model

In order to formalize these ideas, the authors create a simple model that explores equilibrium outcomes when traders trade on good and bad news, with and without feedback.

The model has 3 dates, time = 0, 1, or 2, and a firm manager seeks to maximize firm value and needs to decide whether to a) maintain the investment, b) increase it, or c) reduce it

* **At time=0**, the speculator knows the “state of nature” of the firm (i.e., whether the news is good or bad for firm value), and the profitability of going long/short the firm. The speculator anticipates how firm managers will react to the trading that occurs.
* **At time=1**, trading occurs, with the price anticipating the manager’s investment decision.
* **At time=2**, the firm manager makes the decision (i.e., a, b, or c from above), which may be affected by trading in time 1.

The model builds on the intuition of the “feedback effect,” in which asymmetric trading, which reduces trading on negative information, creates a limit to arbitrage that is generated by the arbitrage process.

From the paper:

> …our model identifies the settings in which the feedback effect, and thus asymmetric trading, is most likely to exist in practice. The asymmetry would be stronger if the value created by correct investment decisions is large, or financial market trading is more informative. It should be weaker if investment is irreversible (e.g., due to a termination fee or firm commitment for an M&A deal), or the manger’s investment decisions are motivated by private benefits rather than firm value maximization.

### Asymmetry between positive and negative information

While the “feedback effect” can *mitigate selling pressure* when there is *negative news*, the authors argue that *when the news is positive*, it *increases the incentive to buy*.

Why?

The manager’s decision table in the paper’s model can be viewed in Table 1 from the paper. It highlights the decision the manager must make at time 2, given a High (H) or Low (L) state. Here a “-1” represents decreasing investment, “0” represents maintaining the current level, and “+1” represents increasing investment. In the “High” state of the model, the manager has an incentive to ***increase*** investment — the assumption is the benefit (x) is larger than the cost (c). Alternatively, in the “Low” state of the model, the manager has an incentive to ***decrease***investment.

[![reflexivity-and-the-feedback-effect](https://alphaarchitect.com/wp-content/uploads/2016/10/reflexivity-and-the-feedback-effect.png)](https://alphaarchitect.com/wp-content/uploads/2016/10/reflexivity-and-the-feedback-effect.png)  
Again, if decision-makers at the firm can use price movements to make smarter decisions, then if the news is good and the price goes up, they are not going to change their minds, because the price is confirming they already made the right decision — in fact they may even have incentives to increase investment! The speculator’s profits are not at risk when he buys on positive information. On the short side, however, the speculator could have a negative profit if an extreme price signal drove managers to change their minds (ie a “-1” in the table above).

### Limits to Arbitrage

This narrative suggests that traders may not seek to fully exploit mispricing they observe that is associated with *bad*news: The feedback effect can pose risks to a position, if the price moves very dramatically in response to it.

Readers of our blog will recognize this as a classic “Limit to Arbitrage” (here is an [overview](https://alphaarchitect.com/2014/05/20/introduction-behavioral-finance-part-2-limits-arbitrage/#gs.LRX5vEA) of the concept, for those curious). [Shleifer and Vishny (1997)](http://ms.mcmaster.ca/~grasselli/ShleiferVishny97.pdf) observed that the risk that an arbitrage position may move against traders in the short run can deter them from pursuing it. Other academics have studied variations on the idea. For instance, [Pontiff (1996)](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=7802), discussed how price impact can create limits to arbitrage. [Lamont and Thaler (2003)](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=384240) highlight how short sale constraints limit arbitrage activities.

These papers emphasize market frictions, but the feedback effect relates to a different type of limit to arbitrage: Real investment and the allocation of real resources.

---

### Feedback Effects, Asymmetric Trading, and the Limits to Arbitrage

Edmans, Goldstein and Jiang

A version of the paper can be found [here](http://finance.wharton.upenn.edu/~itayg/Files/limitstoarbitrage-published.pdf).

Want a summary of academic papers with alpha? Check out our [Academic Research Recap](https://alphaarchitect.com/category/architect-academic-insights/academic-research/#gs.m4HqX7w) Category.

### Abstract:

> We analyze strategic speculators’ incentives to trade on information in a model where firm value is endogenous to trading, due to feedback from the financial market to corporate decisions. Trading reveals private information to managers and improves their real decisions, enhancing fundamental value. This feedback effect has an asymmetric effect on trading behavior: it increases (reduces) the profitability of buying (selling) on good (bad) news. This gives rise to an endogenous limit to arbitrage, whereby investors may refrain from trading on negative information. Thus, bad news is incorporated more slowly into prices than good news, potentially leading to over investment.
