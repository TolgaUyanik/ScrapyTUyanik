---
title: "Using Trading Volume to Optimize Portfolio Construction and Implementation"
slug: "trading-volume"
date: "2024-11-01"
modified: "2024-10-28"
url: "https://alphaarchitect.com/trading-volume/"
categories: ["Transaction Costs", "Research Insights", "Larry Swedroe", "Other Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Using Trading Volume to Optimize Portfolio Construction and Implementation

> The authors of the research discussed developed a machine learning model that can accurately predict trading volume for individual stocks. They then demonstrated how this model can be used to construct a portfolio that outperforms a traditional market-cap weighted portfolio.

While portfolio optimization typically focuses on risk and return prediction, implementation costs critically matter. Unfortunately, predicting trading costs is challenging because the largest component for a large investor is price impact, which depends on the size of the trade, the amount traded by other traders in that security, and the identity of the trader, thus, impeding a generic solution. To address the problem, Rusian Goyenko, Bryan Kelly, Tobias Moskowitz, Yinan Su, and Chao Zhang, authors of the August 2024 study “[Trading Volume Alpha](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4802345),” hypothesized that trading volume is a valuable source of information for estimating trading costs. Assuming a fixed trade size, trading costs should be declining in trading volume. To test the hypothesis, they developed a machine learning model that can accurately predict trading volume for individual stocks. They then demonstrated how this model can be used to construct a portfolio that outperforms a traditional market-cap weighted portfolio.

They began by noting that [prior research](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2294498) (Frazzini, Israel, and Moskowitz,2018) has shown that trade size divided by daily trading volume– termed the market participation rate in a stock– is the key driver of price impact costs and that price impact is an increasing function of participation rate. Holding trade size constant, the less trading volume in the stock, the greater the trader’s price impact will be. Thus, all else equal, a higher predicted volume allows the trader to trade larger amounts because price impact per dollar traded will be lower. Conversely, a lower predicted volume causes the trader to trade less aggressively, scaling back trading (perhaps even to zero) because the price impact per dollar will be higher. Thus, their strategy was to forecast trading volume for each security as a proxy for expected trading costs, and then use this forecast to optimize portfolios net of those costs and quantify its benefits. Their analysis assumed that the trade size was fixed. Note that in practice, intuitively, a fund might attempt to trade when the cost to trade was cheap and less when more expensive.

The authors then presented their machine learning model for predicting trading volume. Their model is based on a [recurrent neural network](https://en.wikipedia.org/wiki/Recurrent_neural_network). To predict volume they used technical signals, such as lagged returns and lagged trading volume, as well as firm characteristics that the literature finds capture return anomalies. They then added indicators for various market-wide or firm-level events associated with volume fluctuation, including upcoming and past earnings releases and analyzed both linear and non-linear prediction methods using various neural networks designed to maximize out-of-sample predictability. Finally, they altered the objective/loss function of the neural network to consider the portfolio problem’s economic objective when predicting volume.

The authors then demonstrated how their model can be used to construct a portfolio.

> “To quantify the economic magnitude of volume prediction, we incorporate volume prediction into a portfolio theory problem. We model a portfolio framework that seeks to maximize the net-of-cost performance of the portfolio using a mean-variance utility function, where the cost of transacting scales linearly with participation rate (motivated by theory and empirical work from the literature). The optimization trades off the cost of trading versus the (opportunity) cost of not trading– minimizing trading costs versus minimizing tracking error to the before-cost optimal portfolio– where trading costs and tracking error are endogenously negatively related. In the model, we take the first and second moments of security returns as given and focus solely on the tradeoff between trading costs and tracking error to the pre-cost optimal portfolio.”

Again, note that in practice, when a stock is expensive to trade another option would be to trade something else instead. For example, if stock A gets too expensive to trade, a fund could  consider a similar stock B which is cheaper to trade. That may be better than not trading because there are often a number of stocks with similar characteristics, and thus similar expected returns, and every so often a fund needs to trade (for example, due to cash flows).

Their sample period was 2018 to 2022, or 1,258 days. The cross-section covered around 4,700 stocks, with an average of 3,500 stocks per day, or 4,400,000 observations in total. Following is a summary of some of their key findings:

Their model was able to accurately predict trading volume for a wide range of stocks.

* Price impact costs (assuming trade size was fixed) were linear in participation rate, but non-linear in trading volume—very low trading volume implied exponentially high impact costs, while very high volume implied negligible costs. Machine learning techniques can significantly improve the ability to forecast volume, due in part to the non-linear nature of volume and its relation to trading costs—big data improved the precision of volume forecasts significantly.
* Larger firms have higher prediction accuracy than smaller firms—small firms are not only less liquid on average; their liquidity is also less predictable and more volatile.
* Holding trade size fixed, as volume tends to zero, price impact costs for liquidity demanders approach infinity (note the opposite is true for liquidity providers, which is why it is important to trade patiently), whereas when volume becomes large, impact costs are bounded by zero.
* Predicted changes in volume have much more economic impact when volume is low versus high, creating asymmetric costs of volume forecast errors. However, [tracking error](https://alphaarchitect.com/2024/03/tracking-error/), or the opportunity cost of not trading, is independent of volume. The combination of these two effects implies the optimization will penalize overestimating volume more than underestimating volume. Trading too much when you overestimate volume is more costly than trading too little when you underestimate it. At lower volume, the cost of trading with respect to volume is very steep, and at high volume the cost-volume relationship is flat.
* Trading costs increase with AUM and the relative penalty for tracking error decreases with AUM—the optimal tradeoff between trading costs and tracking error will vary with the size of the portfolio as will the economic impact of volume prediction. For small AUM, tracking error considerations dominate trading cost considerations—the economic benefit to predicting volume may be relatively less valuable. For large AUM, trading cost considerations dominate.
* Factors with a higher turnover (e.g., momentum, short-term reversals) benefit more from portfolio optimization that accounts for expected trading costs based on volume forecasts (see charts).

![](https://alphaarchitect.com/wp-content/uploads/2024/10/Figure_7-800x448.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

* Trading volume alpha was substantial. The marginal improvement on a portfolio from trading volume alpha is as large as finding return alpha. For example, for a $1 billion fund, the after-cost improvement in portfolio performance due solely to trading volume prediction beyond using lagged volume measures, can be as much as double in terms of expected returns or Sharpe ratio after trading costs. Among popular asset pricing factors, the improvement in after-cost returns ranges from 20 bps to 100 bps above using a moving average of lagged volume to predict future volume.

Their findings led the authors to conclude:

> “Volume is highly predictable, especially when using machine learning techniques, large data signals, and exploiting the virtueof complexity in prediction. We find that volume prediction can be as valuable as return prediction in achieving optimal mean-variance portfolios net of trading costs. We find that incorporating an economic objective function directly into machine learning is even more effective for obtaining useful predictions. This feature may be general to many finance applications of machine learning, where incorporating the economic objective directly may dominate a two-step process that first satisfies some statistical objective and then incorporates that statistical object into an economic framework. For volume prediction, the asymmetric cost of overestimating versus underestimating volume is captured (ignored) by an economic (statistical) objective, and delivers sizeable economic impact.” They added: “Refining the prediction methods and deepening the prediction models could add substantially to these improvements, generating even larger trading volume alpha.”

**Summary**

The paper Trading Volume Alpha makes a significant contribution to the literature on trading volume. The authors provide a clear and concise overview of the existing literature. They also presented a novel machine learning model for predicting trading volume. Their findings have the potential to revolutionize the way funds are constructed and strategies implemented. In the conclusion, the authors stated:

> “A more exhaustive search for prediction variables and models that forecast volume more accurately could translate into even larger economic benefits than we show here. Some promising candidates for additional features and methods are lead-lag volume relations across stocks, more seasonal indicators, other market microstructure variables, and more complex nn and rnn models.”

The paper is a must-read for anyone interested in trading volume or machine learning.

Larry Swedroe is the author or co-author of 18 books on investing, including his latest [Enrich Your Future](https://www.amazon.com/Enrich-Your-Future-Successful-Investing/dp/1394245440/ref=sr_1_1?crid=1F1KPWSHNWWZL&dib=eyJ2IjoiMSJ9.R1VwlsG9zUQwWdwscc3NP2weOd68TWy06Pkb7dbZIGAvQh495OyVuwNZUlbqWCFfokLCcTBBe79gcueuy8LrguAAWTJyW9idmKxIIFSxmJU.H837ZP8B-QF65l2KSwZaxbAvrvEqpmZjG4KKjWI1YZk&dib_tag=se&keywords=enrich+your+future+larry+swedroe&qid=1729091327&sprefix=enrich+your+future%2Caps%2C356&sr=8-1).
