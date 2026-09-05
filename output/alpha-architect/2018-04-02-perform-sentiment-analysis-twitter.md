---
title: "How to Perform Investment Sentiment Analysis on Twitter"
slug: "perform-sentiment-analysis-twitter"
date: "2018-04-02"
modified: "2018-04-02"
url: "https://alphaarchitect.com/perform-sentiment-analysis-twitter/"
categories: ["Basilico and Johnsen", "Academic Research Insight"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# How to Perform Investment Sentiment Analysis on Twitter

> Company Event Popularity for Financial Markets using Twitter and Sentiment Analysis Mariana Daniel, Rui Ferreira Neves, Nuno Horta Expert Systems with Applications, 2017 A version […]

## Company Event Popularity for Financial Markets using Twitter and Sentiment Analysis

* Mariana Daniel, Rui Ferreira Neves, Nuno Horta
* *Expert Systems with Applications*, 2017
* A version of this paper can be found [here](https://dl.acm.org/citation.cfm?id=3030777)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/academic-research-insight/) category.

## What are the research questions?

By studying tweets on thirty companies in the Dow Jones Index, the authors ask the following research question:

1. Is it possible to develop a system for the detection and discovery of the popularity of special events on Twitter that may influence the financial markets?

## What are the Academic Insights?

The system devised by the authors is composed of five steps:

* **Identification of the financial community** by identifying relevant users ( those with more followers than users followed) based on 10 influencers
* **Filtering of the tweets**based on Investopedia financial dictionary
* **Definition of sentiment** by using four text analysis tools ( MySentiment Api, TextBlob, SentiStrenght and Affin)
* **Normalization**by volume
* **Event detection**

The authors study over 12 million tweets from 9,000 users over 710 days ( from September 2013 and September 2015). Of these tweets, only 192,935 (those with content relevant to the financial markets) are analyzed.

The three case studies presented in the paper (Apple, Microsoft and Walmart) are examples of the efficiency of the model in dealing with massive amounts of data and very high levels of noise typical of social networks.

## Why does it matter?

While this is not the typical paper that researches relations between data and market performance, it shows the details of how to approach sentiment analysis on Twitter starting from the definition of a relevant community of users down to the definition of a popular company event.

## The Most Important Chart from the Paper:

![](https://alphaarchitect.com/wp-content/uploads/2018/02/Twitter-Sentiment-ANalysis.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

---

## Abstract

> The growing number of Twitter users makes it a valuable source of information to study what is happening right now. Users often use Twitter to report real-life events. Here we are only interested in following the financial community. This paper focuses on detecting events popularity through sentiment analysis of tweets published by the financial community on the Twitter universe. The detection of events popularity on Twitter makes this a non-trivial task due to noisy content that often are the tweets. This work aims to filter out all the noisy tweets in order to analyze only the tweets that influence the financial market, more specifically the thirty companies that compose the Dow Jones Average. To perform these tasks, in this paper it is proposed a methodology that starts from the financial community of Twitter and then filters the collected tweets, makes the sentiment analysis of the tweets and finally detects the important events in the life of companies.
