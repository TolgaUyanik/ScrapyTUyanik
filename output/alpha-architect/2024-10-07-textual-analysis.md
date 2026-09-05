---
title: "Reading the WSJ May Make You a Better Economist"
slug: "textual-analysis"
date: "2024-10-07"
modified: "2024-10-07"
url: "https://alphaarchitect.com/textual-analysis/"
categories: ["Elisabetta Basilico", "Research Insights", "Academic Research Insight", "Other Insights", "Behavioral Finance"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Reading the WSJ May Make You a Better Economist

> How can textual analysis of business news, specifically The Wall Street Journal (WSJ), be used to measure the state of the economy?

The paper proposes an innovative approach to measuring the state of the economy by examining how textual analysis of business news, particularly from *The Wall Street Journal* (WSJ), can be used to accomplish such a goal.

## Business News and Business Cycles

* Leland Bybee, Bryan Kelly, Asaf Manela, Dacheng Xiu
* Journal of Finance, 2024
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3446225)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Research Questions?

The research questions are as follows:

1. How can textual analysis of business news, specifically The Wall Street Journal (WSJ), be used to measure the state of the economy?
2. What is the structure of news coverage related to economic events, and how do these topics evolve over time?
3. Does news attention contain information that is distinct from standard numerical economic indicators in predicting macroeconomic outcomes?
4. Can news-based models reliably detect variations in the equity risk premium, and how do they perform compared to traditional benchmarks in market timing strategies?
5. How can the narratives extracted from news articles be used to better understand the drivers of economic fluctuations and model-based expectations?

## What are the Academic Insights?

By analysing the full text of the The Wall Street Journal (WSJ ), consisting of approximately  
800,000 articles from 1984–2017, the authors find:

1. Textual analysis of business news, specifically *The Wall Street Journal* (WSJ), can be used to measure the state of the economy by identifying and tracking economic themes discussed in news articles. This process involves applying topic modeling, a machine learning technique, to categorize the content of the WSJ into clusters of related words, or “topics,” such as “recession,” “employment,” or “market volatility.” By analyzing the frequency and prominence of these topics over time, researchers can gauge which economic issues are receiving attention and how they evolve in response to real-world events. This textual data provides a comprehensive view of economic conditions, reflecting the concerns of both news producers and consumers.
2. The structure of news coverage related to economic events is organized into distinct, interpretable topics that represent key economic themes. Using a topic modeling technique, the paper identifies clusters of words that frequently co-occur in *The Wall Street Journal* (WSJ) articles. These clusters form specific topics, such as “recession,” “Federal Reserve,” “unemployment,” “stock market,” or “natural disasters.” Each topic encapsulates a particular area of economic activity, enabling researchers to map and categorize how the media discusses the economy. The topics evolve over time based on the economic environment and the occurrence of significant events. The evolution of these topics reflects both cyclical economic patterns and unexpected shocks. Over time, topics related to major economic shifts, such as recessions or [market volatility](https://alphaarchitect.com/2018/05/market-volatility-hang-enjoy-ride/), tend to dominate coverage during periods of uncertainty. This structured coverage helps capture both short-term fluctuations and long-term trends in the economy, providing a rich source of information for understanding how economic narratives develop and change over time.
3. Yes, news attention contains information that is distinct from standard numerical economic indicators in predicting macroeconomic outcomes. The paper demonstrates that textual analysis of *The Wall Street Journal* (WSJ) can capture valuable insights about future economic conditions that are not fully reflected in traditional indicators like stock prices, interest rates, or economic uncertainty measures. For example, the study finds that news coverage of specific topics, such as “recession,” has significant predictive power for future output and employment, even after controlling for common macroeconomic variables in a standard vector autoregression (VAR) model. This suggests that news attention provides additional, independent information about the economy, particularly during periods of heightened uncertainty.
4. Yes, news-based models can reliably detect variations in the equity risk premium, and they often outperform traditional benchmarks in market timing strategies. The paper demonstrates that by using topic modeling to analyze business news from *The Wall Street Journal* (WSJ), researchers can extract signals that forecast time-varying expected stock market returns, also known as the equity risk premium. These news-based models are able to predict changes in market returns by identifying specific topics in news coverage that are closely tied to market sentiment and economic conditions, such as recession risks or financial market developments. The use of “Online Latent Dirichlet Allocation” (LDA) in the study allows for real-time processing of news articles, ensuring that predictions are based only on information available at that time, thereby avoiding look-ahead bias.
5. The narratives extracted from news articles can be utilized to enhance the understanding of the drivers of economic fluctuations and model-based expectations in several ways: mapping economic conditions, linking text to economic dynamics, enhancing forecasting and interpreting model impulse responses. By interpreting the impulse responses of the model in terms of these narratives, researchers can better understand how economic shocks propagate through the economy and how public perception, as shaped by news, impacts economic dynamics.

## Why does this study matter?

This study matters because it enhances our understanding of the complex relationship between news narratives and economic dynamics, providing valuable insights that can improve economic modeling, forecasting, and policy formulation. In an increasingly complex and interconnected global economy, understanding how news media shapes perceptions of economic conditions is crucial. The study highlights the role of media as an information intermediary, influencing consumer behavior, investor decisions, and policy formulation.

## The Most Important Chart from the Paper:

![](https://alphaarchitect.com/wp-content/uploads/2024/09/2024-09-30-11_47_04-ssrn-3446225-2.pdf.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

## Abstract

> We propose an approach to measuring the state of the economy via textual analysis of business news. From the full text of 800,000 Wall Street Journal articles for 1984–2017, we estimate a topic model that summarizes business news into interpretable topical themes and quantifies the proportion of news attention allocated to each theme over time. News attention closely tracks a wide range of economic activities and can forecast aggregate stock market returns. A text-augmented VAR demonstrates the large incremental role of news text in forecasting macroeconomic dynamics. We retrieve the narratives that underlie these improvements in market and business cycle forecasts.
