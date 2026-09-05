---
title: "Creating Better Factor Portfolio via AI"
slug: "creating-better-factor-portfolio-via-ai"
date: "2024-06-24"
modified: "2024-09-12"
url: "https://alphaarchitect.com/creating-better-factor-portfolio-via-ai/"
categories: ["Transaction Costs", "Empirical Methods", "Research Insights", "Factor Investing", "Basilico and Johnsen", "Academic Research Insight", "AI and Machine Learning"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Creating Better Factor Portfolio via AI

> Trading costs, discontinuous trading, missed trades, and other frictions, along with asset management fees can cause a shortfall between live and paper portfolios. The focus of this paper is to test an effective rebalancing method that prioritizes trades with the strongest signals to capture more of the factor premia while reducing turnover and trading costs.

Although the title is a bit daunting this is a working paper with quite a bit of promise, especially with respect to the application of AI methods and models and a unique idea for constructing Value portfolios. In the place of traditional book-to-market ratios, price-to-earnings and EBIT-to-EV, the authors propose constructing portfolios based on predicted future fundamentals rather than current values. A new fundamental approach.

## Uncertainty-Aware Lookahead Factor Models for Quantitative Investing

* Lakshay Chauhan, John Alberg, Zachary C. Lipton
* White Paper
* A version of this paper can be found [here](http://proceedings.mlr.press/v119/chauhan20a/chauhan20a.pdf)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category.

## What are the research questions?

1. What are the new AI methodologies used to construct portfolios with exposures to *predicted* value characteristics?
2. Can deep learning models be used to forecast future financial fundamentals?
3. What role does uncertainty play in quantitative investing, and how can it be incorporated into models?

## What are the Academic Insights?

1. Short explanations of the AI techniques and models used successfully to implement predicted value exposures:
   * Deep Neural Networks(DNNs) are used to forecast fundamentals from past values. Two types of DNNs used include *Multi-Layer Perceptrons* (MLPs) to model complex relationships between inputs and outputs and are akin to regression tasks. *Long Short-Term Memory Networks* (LSTMs) which are capable of processing and predicting time series data.
   * Ensemble Learningis used to improve the accuracy of the forecasts made from DNNs which helps reduce overfitting and associated biases.
   * Uncertainty Quantification approached essentially produce a mean and variance for each forecast, therefore incorporating uncertainty into each prediction.
2. YES. Deep learning models, particularly LSTMs and MLPs, can effectively forecast future financial fundamentals. These models are trained on historical financial data to predict future earnings, which are then used to construct more accurate factor models. Referring to Figure 7 below, note the cumulative returns of different portfolio strategies over the out-of-sample period (from 2000 to 2019). The purpose of this figure is to compare the performance of various quantitative investing models and how incorporating uncertainty-aware strategies improves returns over time. Results of the specific forecasting models:
   * The LFM UQ-LSTM line represents the uncertainty-aware LSTM model, which uses a recurrent neural network (LSTM) to predict future EBIT while incorporating uncertainty estimates. This model adjusts for risk by scaling the predicted EBIT based on the model’s uncertainty estimates.  It consistently outperforms the other model**s** throughout the entire out-of-sample period. Its cumulative returns are higher, showcasing its ability to manage risk and capitalize on more accurate predictions.
   * The LFM UQ-MLP line represents an uncertainty-aware model that uses a Multi-Layer Perceptron (MLP) to forecast EBIT. The predictions are adjusted for uncertainty by scaling down predictions that have higher variance (more uncertainty). It  performs better than simpler models like LFM Auto Reg and LFM Linear but falls short compared to LFM UQ-LSTM.
   * The QFM (standard factor model) line represents a standard factor model that uses current EBIT (earnings before interest and taxes) rather than predicted future fundamentals. This serves as the baseline comparison model.  It underperforms significantly compared to the LFMs, especially the uncertainty-aware models. This highlights the advantage of using predicted future fundamentals over current fundamentals.
   * The widening gap between the lines suggests that the gains from using uncertainty-aware models compound as time progresses, leading to substantially higher cumulative returns in the long run.
3. Neural heteroscedastic regression and Monte Carlo dropout are methods that are used to estimate the uncertainty in predictions. The uncertainty estimates are then used to scale the predicted values, adjusting for risk. The performance of uncertainty-aware models against standard factor models are evaluated by using the Sharpe ration and Compound Annualized Return (CAR) and Sharpe ratio. The uncertainty-aware models, which adjust predictions based on estimated uncertainty, show higher returns and lower volatility and higher Sharpe ratios than the standard models.

## Why does it matter?

F**orward-looking models** that leverage advanced machine learning techniques for better forecasting canmanage risk more effectively by quantifying uncertainty therefore enhancing the performance of investment strategies. These approaches offer the potential for higher returns and more robust risk management, positioning them well for success in a competitive investment landscape.

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2024/06/2024-06-18-17_50_06-AI_Quant_Wes_John.pdf-and-1-more-page-Personal-Microsoft​-Edge-1200x543.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

## Abstract

> On a periodic basis, publicly traded companies report fundamentals, financial data including revenue, earnings, debt, among others. Quantitative finance research has identified several factors and functions of the reported data that historically correlate with stock market performance. In this paper, we first show through simulation that if we could select stocks via factors calculated on future fundamentals (via oracle), that our portfolios would far outperform standard factor models. Motivated by this insight, we train deep nets to forecast future fundamentals from a trailing 5-year history. We propose lookahead factor models which plug these predicted future fundamentals into traditional factors. Finally, we incorporate uncertainty estimates from both neural heteroscedastic regression and a dropout-based heuristic, improving performance by adjusting our portfolios to avert risk. In retrospective analysis, we leverage an industry-grade portfolio simulator (backtester) to show simultaneous improvement in annualized return and Sharpe ratio. Specifically, the simulated annualized return for the uncertainty-aware model is 17.7% (vs 14.0% for a standard factor model) and the Sharpe ratio is 0.84 (vs 0.52).
