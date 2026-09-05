---
title: "Do Trading Costs Destroy Factor Investing?"
slug: "trading-costs-destroy-factor-investing"
date: "2017-05-10"
modified: "2017-05-10"
url: "https://alphaarchitect.com/trading-costs-destroy-factor-investing/"
categories: ["Research Insights", "Factor Investing", "Basilico and Johnsen"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Do Trading Costs Destroy Factor Investing?

> There are a number of recent studies that propose a more rigorous criteria for evaluating the practical significance of factors published in academic research journals. […]

There are a number of recent studies that propose a more rigorous criteria for evaluating the practical significance of factors published in academic research journals.

First, [Harvey, Liu, and Zhu (2015)](http://alphaarchitdev.wpengine.com/2015/04/21/are-value-investing-and-momentum-investing-robust-anomalies/) argue that a t-stat of 3 should be replacing the old 2 as a rule for statistical significance. In 2017, Campbell Harvey [was quoted](http://www.economist.com/news/finance-and-economics/21644202-most-trading-strategies-are-not-tested-rigorously-enough-false-hope) claiming the following:

> Half the financial products (promising outperformance) that companies are selling to clients are false.

Also, [McLean and Pontiff (2014)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2156623), [Chordia, Subrahmanyam and Tong (2014)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2029057), and [Hou, Xue, and Zhang (2017)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2961979) document a post publication reduction in average strategy performance (across numerous anomalies), but surprisingly none of these papers really include an in-depth transaction cost analysis in their performance calculations.

Finally, the Fama-French (and Carhart) factors (*beta, value, size, momentum*), which are the foundation for many *smart beta* strategies, were not designed with t-costs in mind and could potentially overstate what an investor can realize when investing in these strategies. ([Here is a post](http://alphaarchitdev.wpengine.com/2017/02/03/factor-models-are-more-art-and-less-science/) with an introduction to factors.)  
Despite all the aforementioned attempts to question the validity of factor investing strategies, transaction costs are not really addressed in detail.

The academic article that really sparked the debate on the importance of considering transaction costs for factor investment strategies was published by Frazzini, Israel, and Moskowitz (2014) ([Here is a discussion](http://alphaarchitdev.wpengine.com/2016/08/17/surprise-the-size-value-and-momentum-anomalies-survive-after-trading-costs/) of this study). The study sparked debate because it suggested that transaction costs were not that big a deal when one actually looks at live data (which was in contrast to prior academic research).

But the academics were not satisfied with this answer and a more recent study conducted by Robert Novy-Marx and Mihahil Velikov, and [published in the *Review of Financial Studies*](https://academic.oup.com/rfs/article-abstract/29/1/104/1844518/A-Taxonomy-of-Anomalies-and-Their-Trading-Costs?redirectedFrom=PDF) at the beginning of 2016, takes the issue to the next level by evaluating a larger set of well-known anomalies. The article, “[A Taxonomy of Anomalies and Their Trading Costs](http://rnm.simon.rochester.edu/research/ToAatTC.pdf),” examines the after-transaction cost performance for  23 different factor investing strategies over longer horizons and across various market capitalization classes, an improvement over other studies.

Interestingly, the authors calculate transaction costs using the effective bid-ask spread measure proposed by Hasbrouck (2009) ([working paper version here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=388360)). Considering that the bid/ask spread does not account for the price impact of large trades, it should be interpreted as the cost faced by a small liquidity demander. The authors also examine the relationship between low turnover and higher capacity across various factors.

A summary of the main questions and insights include the following:

* ***What are the costs of trading the most important anomalies?***

Figure 3 in the article shows a nice historical perspective of transaction costs for the three main factor investing strategies: *size (SMB), value (HML)* and *momentum (UMD).*  The figure shows the following: *size* and *value* have low transaction costs (the average over the period from 1963 to 2013 was 5.7 bps and 5.5 bps per month) while *momentum* incurs higher transaction cost at an average 48.4 bps per month. We  also observe a downward trend in historical costs, which spike during periods of market turbulence (note: these are long/short factors, not long-only portfolios).

[![](https://alphaarchitdev.wpengine.com/wp-content/uploads/2017/05/fig-3-tc-paper.png)](http://alphaarchitdev.wpengine.com/wp-content/uploads/2017/05/fig-3-tc-paper.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Table 3 in the article shows a deeper dive into the profitability of 23 factor investing strategies. Good news: The authors reach a similar conclusion as Frazzini et al. (2014): *size, value* and *momentum* still have positive returns after transaction costs.  Additionally, by adding *profitability* to the *value* and *momentum* combo, the excess return doubles (from 0.51 to 0.99) and the t-stat improves significantly (from 2.67 to 5.18).

Transaction costs typically reduce value-weighted long/short strategies by 1% of the monthly one-sided turnover.  For instance, a strategy that turns over 20% per month, the spread will be at least 20 bps lower per month. Many of the strategies based on the anomalies studied (at least those with turnover <50%) remain profitable, but in all cases transaction costs significantly reduce their profitability and statistical significance.

* ***What is the capacity that each of these strategies has to attract new capital before it becomes unprofitable to marginal trading?***

Another important topic under debate between academic and practitioner is the (limited) capacity of factor strategies. The authors try to tackle this question in section 5 of the article. Their conclusion is that low turnover strategies tend to have higher capacities. They calculate 170 B capacity for *size,*$50 B. for *value*and $5 B. for momentum. The authors estimates generally agree with Frazzini et al. (2014) on *size* and *value,* but they come up with a MUCH lower estimate for *momentum*(which aligns with Korajczyk and Sadka (2004). Not great news for momentum investors looking to scale their investment!

[![](https://alphaarchitdev.wpengine.com/wp-content/uploads/2017/05/capacity.png)](http://alphaarchitdev.wpengine.com/wp-content/uploads/2017/05/capacity.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

* ***Are there effective transaction cost mitigation techniques?***

The authors find that a buy/hold spread that makes the criterion for entering into a position more stringent that the criteria for maintaining a position is the most effective cost mitigation technique for most of the anomalies studied. They also examine alternative transaction cost mitigation techniques, but they generally find that low-turnover strategies have large capacity, while high turnover strategies (such as momentum) still have limited capacity.

## Conclusion

It seems that everywhere you look there is a promotion related to factor investing and/or smart beta. The incentives to develop strategies with strong backtests are strong, both in academia and in industry. This natural conflict of interest should raise concern for investors who are trying to ascertain the validity of a particular study or investment approach. One must always consider the possibility of [data-snooping](http://alphaarchitdev.wpengine.com/2017/03/03/evidence-based-investing-take-alpha-shove/), [overfitting](http://alphaarchitdev.wpengine.com/2016/06/28/backtesting-strategies-based-multiple-signals-beware-overfitting-biases/#gs.BJhcxZU), and transaction costs — do they make the strong results null and void?

This paper is also important because the results are a great contrast to the research presented in the Frazzini et al. paper. ([detailed review here](http://alphaarchitdev.wpengine.com/2016/08/17/surprise-the-size-value-and-momentum-anomalies-survive-after-trading-costs/)).

**Bottomline:** investors need to be diligent and think critically when presented hypothetical ([live results](http://alphaarchitdev.wpengine.com/2016/02/20/chasing-returns-and-avoiding-spaghetti-against-the-wall-fund-companies/) are arguably more dangerous) results.

---

# **A Taxonomy of Anomalies and Their Trading Costs**

* Robert Novy-Marx
* Mihahil Velikov
* [paper](http://rnm.simon.rochester.edu/research/ToAatTC.pdf)

# **Abstract**

> We study the after-trading-cost performance of anomalies, and effectiveness of transaction cost mitigation techniques. Introducing a buy/hold spread, with more stringent requirements for establishing positions than for maintaining them, is the most effective cost mitigation technique. Most anomalies with turnover less than 50% per month generate significant net spreads when designed to mitigate transaction costs; few with higher turnover do. The extent to which new capital reduces strategy profitability is inversely related to turnover, and strategies based on size, value, and profitability have the greatest capacities to support new capital. Transaction costs always reduce strategy profitability.
