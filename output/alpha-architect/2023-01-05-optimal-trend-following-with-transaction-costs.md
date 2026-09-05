---
title: "Optimal Trend Following with Transaction Costs"
slug: "optimal-trend-following-with-transaction-costs"
date: "2023-01-05"
modified: "2022-12-30"
url: "https://alphaarchitect.com/optimal-trend-following-with-transaction-costs/"
categories: ["Research Insights", "Trend Following"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Optimal Trend Following with Transaction Costs

> In spite of the widespread popularity of trend-following investing, little is still known about optimal trend-following with transaction costs.

* Valeriy Zakamulin and Javier Giner
* Working paper, University of Agder and University of La Laguna
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4282126)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Motivations?

Despite the widespread popularity of [trend-following investing](https://alphaarchitect.com/2019/06/trend-following-the-epitome-of-no-pain-no-gain/), little is known about optimal trend-following with transaction costs. A few existing studies consider this question using a continuous-time model within the stochastic optimal control theory framework. However, despite being theoretically the most appropriate, this approach makes the problem intractable analytically, and the numerical solutions are extremely complex. Therefore, practical implementation of this model is hardly possible. Considering the aforementioned issues, there is an urgent need to develop a model representing an acceptable compromise between theoretical simplicity and practical relevance.

## What are the Research Questions?

Trading rules based on moving averages of past prices are, without doubt, the prevalent trend-following rules used in practice. There are several types of rules and different kinds of moving averages. Traders are familiar with various trading indicators based on moving averages, and the moving average trading rules are implemented in just about any trading platform. Motivated by these considerations, our first research question is to find the optimal trend-following rule in the presence of transaction costs. Our second research question is to approximate the optimal trend-following rule by an existing trend-following rule.

## What are the Theoretical Findings?

We formulate a discrete-time model where the financial asset returns follow a persistent autoregressive process. Instead of the price-based formulation of trend-following rules, we use an equivalent and more suitable return-based formulation. Our approach aims to determine the return weights of the trading indicator that maximizes the trend-following strategy’s performance in the presence of transaction costs. We show that our theoretical model produces a partly tractable optimization problem that can be solved numerically using standard and efficient optimization methods.

First, assuming that the trading indicator uses a given number of return lags, we determine the return weights of the trading indicator that minimizes trading costs. We show that the optimal return-weighting function has the shape of a semi-circle; see Figure 1 for an illustration.

![](https://alphaarchitect.com/wp-content/uploads/2022/12/maxautoc-1-400x267.png)

*Fig. 1: Return weights of the trading indicator that minimizes transaction costs given that the number of return lags equals 25.*

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.*

Second, before attacking the main problem of finding the optimal trend-following rule in the presence of transaction costs, we need to make a feasible assumption about the shape of the autoregressive coefficients of the real-life return process. The problem is that the empirical autoregressive coefficients are rather small and escape detection, see Zakamulin and Giner (2022a). On theoretical grounds (see Zakamulin and Giner [2022b]), one can assume that the autoregressive coefficients are linearly decreasing with the return lag; see Figure 2 for an illustration. It is worth emphasizing that the assumed autoregressive coefficients are the same as the return weights in the popular Simple Moving Average (SMA) rule. We demonstrate that the SMA rule represents the optimal trading rule without transaction costs.

![](https://alphaarchitect.com/wp-content/uploads/2022/12/sma-400x267.png)

*Fig. 2: Autoregressive coefficients of the return process under the assumption that there are 25 coefficients and they are linearly decreasing with the return lag.*

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.*

Third, under reasonable assumptions about the real-life return process, we solve numerically for the return weights of the optimal trend-following rule in the presence of [transaction costs](https://alphaarchitect.com/2017/11/transaction-costs/). The result is depicted in Panel A of Figure 3. The results of our numerical computations are very intuitive. In the absence of transaction costs, the shape of the return-weighting function of the optimal trading indicator resembles the shape of the autoregressive coefficients. When the trading costs are huge, the trading indicator minimizes the transaction costs, and the return-weighting function takes the shape of a semi-circle. In between these two extremes, when the transaction costs are neither negligibly small nor extremely large, the optimal return-weighting function has a hump shape between a linearly decreasing shape and a semi-circle shape. This shape can be well approximated by the return weights of an SMA crossover rule, see Panel B of Figure 3. Consequently, our model justifies using the crossover rules in practice.

![](https://alphaarchitect.com/wp-content/uploads/2022/12/opt-600x300.png)

Fig. 3: Panel A plots the return weights of the optimal trading indicator when the one-way proportional transaction costs are 0.25%. Panel B plots the return weights of the 7- and 25-period SMA crossover rule.

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.*

## Does the Empirical Evidence Support the Theoretical Results?

Yes, we validate the predictions of our theoretical model and demonstrate the advantage of the optimal trend-following with transaction costs using real-world data. We show that the results of this study are in satisfactory agreement with our theoretical model.

## References:

Zakamulin and Giner (2022a), “Time Series Momentum in the US Stock Market: Empirical Evidence and Theoretical Analysis”, an open-access paper published in the International Review of Financial Analysis, available [here](https://www.sciencedirect.com/science/article/pii/S1057521922001363)

Zakamulin and Giner (2022b), “Optimal Trend Following Rules in Two-State Regime-Switching Models”, working paper available at the [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4217513)

![Valeriy Zakamulin](https://alphaarchitect.com/wp-content/uploads/2022/12/Zakamulin_avatar.jpg)

## About the Author: Valeriy Zakamulin

Valeriy Zakamulin is Professor of Finance at the School of Business and Law, University of Agder, Norway, where he teaches graduate courses in Finance. His first graduate academic degree is a MS in Radio Engineering. After receiving this degree, Valeriy Zakamulin had been working for many years as a research fellow at a computer science department, developing both computer hardware and software. Later on Valeriy Zakamulin received a MS in Economics and Business Administration and a PhD in Finance. He has published more than 30 articles in various refereed academic and practitioner journals and is a frequent speaker at international conferences. He has also served on editorial boards of several economics and finance journals. His current research interests cover behavioral finance, portfolio optimization, time-series analysis of financial data, financial asset return and risk predictability, and technical analysis of financial markets.
