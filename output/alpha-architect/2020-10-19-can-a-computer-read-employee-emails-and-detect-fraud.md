---
title: "Can A Computer Read Employee Emails and Detect Fraud?"
slug: "can-a-computer-read-employee-emails-and-detect-fraud"
date: "2020-10-19"
modified: "2020-10-19"
url: "https://alphaarchitect.com/can-a-computer-read-employee-emails-and-detect-fraud/"
categories: ["Research Insights", "Basilico and Johnsen", "Academic Research Insight", "Investment Advisor Education", "AI and Machine Learning"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Can A Computer Read Employee Emails and Detect Fraud?

> Zero-Revelation RegTech: Detecting Risk through Linguistic Analysis of Corporate Emails and News S.R. Das, S. Kim, B. Kothari Journal of Financial Data Science, Spring 2019 […]

## Zero-Revelation RegTech: Detecting Risk through Linguistic Analysis of Corporate Emails and News

* S.R. Das, S. Kim, B. Kothari
* *Journal of Financial Data Science,* Spring 2019
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2960350)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Research Questions

Last week I took you on a tour of utilizing the data hidden in the [language of the news](https://alphaarchitdev.wpengine.com/2020/10/12/news-and-its-impact-on-risk-and-returns-around-the-world/). In this post, we’re taking the analysis of language to corporate emails. Clearly, unlike the data in news, corporate emails are non-public information. Therefore the data is being utilized to develop regulatory technology (RegTech), not hunting for alpha generation. This paper applies natural language programming (NLP), a popular data science technique used in finance, to develop an early-warning system for detecting corporate fraud and/or failure. Specifically, the authors attempt at answering the following research questions:

* Does the sentiment conveyed by employee communications (i.e. emails) contain value-relevant information?
* Is this information conveyed in a timely manner (i.e., does email sentiment lead subsequent stock returns)?
* Do other structural characteristics of internal employee emails (e.g., email length, email volume, or email-network characteristics) also contain value-relevant information?
* Which tends to contain more value-relevant information, the actual verbal content, or structural characteristics of employee emails?

## What are the Academic Insights?

By analyzing a unique dataset made up of 113,000 emails from 144 Enron employees and 1,300 that appeared on PR *Newswire*  from January 2000 to December 2001, the authors find:

1. YES, the authors observe trending patterns in the sentiment contained in emails. Specifically, they observe the positive sentiment from both emails and news articles decline into the year of 2001 as Enron problems started to manifest.
2. YES, the net sentiment of email content is a meaningful predictor of subsequent stock returns. Specifically, a one standard deviation decrease in the net sentiment gleaned from emails is associated with a 4.5% decline in stock returns (coefficient estimate = 2.347, t-statistic = 3.27).
3. YES, the authors find that when the length of emails is added as an independent variable to the regression, it takes over in explaining the relation with future stock returns. In fact, for every 20-character decline in email length, there is a 1.17% in future stock returns. Additionally, the authors find that structural characteristics such as the length of emails contain the most value-relevant information.

## Why does it matter?

The importance of RegTech has grown rapidly since the financial crisis; more than $160 billion has been paid in fines by various financial institutions. Also, about 10%-15% of the staff in financial institutions is dedicated to compliance ( [Arnold, 2016](https://www.ft.com/content/fd80ac50-7383-11e6-bf48-b372cdb1043a)) and a RegTech solution could create a reduction of costs. This paper develops a RegTech expert system solution to parse corporate email content to detect shifts in critical characteristics in a timely, efficient, and noninvasive manner. Clearly it’s hard to make large sweeping conclusions from one data set on a company that the researchers knew had failed. That however shouldn’t stop us from taking a deeper look into the utilization of textual RegTech analysis of corporate management emails as a means to detect risk in a timelier fashion. It may also be used by regulators in their audit process because they can requisition such analyses from firms without intrusively reading emails. In the words of the authors:

> “*Early detection and prevention is better than a cure”*

## The Most Important Chart from the Paper:

![](https://alphaarchitect.com/wp-content/uploads/2020/02/2020-02-10-20_31_29-NLP-on-corporate-emails.pdf-Adobe-Acrobat-Reader-DC-1-600x192.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> *In this paper, we demonstrate how an applied linguistics platform may be used to parse corporate email content and news to assess factors predicting escalating risk or the gradual shifting of other critical characteristics within the firm before they are eventually manifested in observable data and financial outcomes. We find that email content and news articles meaningfully predict increased risk and potential malaise. We also find that other structural characteristics, such as the average email length, are strong predictors of risk and subsequent performance. We present implementations of three spatial analyses of internal corporate communication, i.e., email networks, vocabulary trends, and topic analysis. Overall, we propose a RegTech solution by which to systematically and effectively detect escalating risk or potential malaise without the need to manually read individual employee emails.*
