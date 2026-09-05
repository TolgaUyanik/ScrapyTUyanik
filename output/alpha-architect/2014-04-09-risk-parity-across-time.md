---
title: "Risk Parity Across Time? A Simulation Education…"
slug: "risk-parity-across-time"
date: "2014-04-09"
modified: "2022-06-01"
url: "https://alphaarchitect.com/risk-parity-across-time/"
categories: ["Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Risk Parity Across Time? A Simulation Education…

> Inter-Temporal Risk Parity: A Constant Volatility Framework for Equities and Other Asset Classes R Perchet, R Carvalho T Heckel and P Moulin A version of […]

### Inter-Temporal Risk Parity: A Constant Volatility Framework for Equities and Other Asset Classes

* R Perchet, R Carvalho T Heckel and P Moulin
* A version of the paper can be found[here.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2384583)
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category!](https://alphaarchitect.com/category/academic-research/)

### **Abstract:**

> Inter-temporal risk parity is a strategy which rebalances between a risky asset and cash in order to target a constant level of risk over time. When applied to equities and compared to a buy and hold strategy it is known to improve the Sharpe ratio and reduce drawdowns. We used Monte Carlo simulations based on a number of time series parametric models from the GARCH family in order to analyze the relative importance of a number of effects in explaining those benefits. We found that volatility clustering with constant returns and the fat tails are the two effects with the largest explanatory power. The results are even stronger if there is a negative relationship between return and volatility. On the other hand, if the Sharpe ratio remains constant over time, the only benefit would arise from an inter-temporal risk diversification effect which is small and has a negligible contribution. Using historical data, we also simulated what would have been the performance of the strategy when applied to equities, corporate bonds, government bonds and commodities. We found that the benefits of the strategy are more important for equities and high yield corporate bonds, which show the strongest volatility clustering and fat tails. For government bonds and investment grade bonds, which show little volatility clustering, the benefits of the strategy have been less important.

### **Alpha Highlight:**

We decided to replicate some of the core results in this paper to get confirmation of the findings. Our work generally jives with what the authors found…

The first test in the paper looks at the performance of risk-parity versus buy-and-hold when returns follow a basic model:

[![sim](https://alphaarchitect.com/wp-content/uploads/2014/04/sim.jpg)](https://alphaarchitect.com/wp-content/uploads/2014/04/sim.jpg)

Now, before you freak out at the site of math, all that is happening here is a simulation of fake returns so the authors can conduct an experiment. Below I highlight how one can conduct this simulation via excel.

[![sims](https://alphaarchitect.com/wp-content/uploads/2014/04/sims-1024x371.jpg)](https://alphaarchitect.com/wp-content/uploads/2014/04/sims.jpg)

Here is an example simulation run:

[![Microsoft Excel - inter temporal_v02_sortino](https://alphaarchitect.com/wp-content/uploads/2014/04/Microsoft-Excel-inter-temporal_v02_sortino.jpg)](https://alphaarchitect.com/wp-content/uploads/2014/04/Microsoft-Excel-inter-temporal_v02_sortino.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Below are the results from the paper after running 500 simulations, where each simulation generates 2600 “fake” daily returns on the S&P 500

[![SSRN-id2384583](https://alphaarchitect.com/wp-content/uploads/2014/04/SSRN-id2384583-1024x407.jpg)](https://alphaarchitect.com/wp-content/uploads/2014/04/SSRN-id2384583.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

And here are some results when you simulate prices that have “GARCHY” volatility. Notice how the current vol depends on past returns and past vol? That is an empirically observed feature of stock return data.  
**[![gar](https://alphaarchitect.com/wp-content/uploads/2014/04/gar.jpg)](https://alphaarchitect.com/wp-content/uploads/2014/04/gar.jpg)**  
Here is how you’d perform this simulation in excel:

[![garchvol](https://alphaarchitect.com/wp-content/uploads/2014/04/garchvol-1024x463.jpg)](https://alphaarchitect.com/wp-content/uploads/2014/04/garchvol.jpg)  
Here are the results:

[![ca](https://alphaarchitect.com/wp-content/uploads/2014/04/ca-1024x416.jpg)](https://alphaarchitect.com/wp-content/uploads/2014/04/ca.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The paper goes on and on with various simulations and compares the results between buy and hold and risk parity.

A very interesting read and a great thought experiment–highly recommend readers attempt to build out their own simulations and replicate figures 1 and 2 from the paper.

We took the analysis one step further and did a ‘bootstrap’ analysis where we sampled from the distribution of daily returns from live data. Unfortunately, the results aren’t favorable for risk parity.

[![sortinoetf](https://alphaarchitect.com/wp-content/uploads/2014/04/sortinoetf.jpg)](https://alphaarchitect.com/wp-content/uploads/2014/04/sortinoetf.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.
