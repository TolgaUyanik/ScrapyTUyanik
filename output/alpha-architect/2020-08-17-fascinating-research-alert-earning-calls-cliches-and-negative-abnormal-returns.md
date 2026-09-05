---
title: "Fascinating Research Alert: Earning Calls, Clichès, and Negative Abnormal Returns"
slug: "fascinating-research-alert-earning-calls-cliches-and-negative-abnormal-returns"
date: "2020-08-17"
modified: "2020-08-17"
url: "https://alphaarchitect.com/fascinating-research-alert-earning-calls-cliches-and-negative-abnormal-returns/"
categories: ["Research Insights", "Basilico and Johnsen", "Academic Research Insight", "AI and Machine Learning"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Fascinating Research Alert: Earning Calls, Clichès, and Negative Abnormal Returns

> When More or Less is Less: Managers’ Clichès J. Klevak, J. Livnat, and K. Suslava Journal of Financial Data Science, Summer 2019 A version of […]

## When More or Less is Less: Managers’ Clichès

* J. Klevak, J. Livnat, and K. Suslava
* *Journal of Financial Data Science,* Summer 2019
* A version of this paper can be found [here](https://jfds.pm-research.com/content/1/3/57.short)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Research Questions

With enough practice, humans can start to get a feel for the tone of a quarterly meeting or start to recognize the unique characteristics of the management. Most of us would be limited to just a handful of managers we could really comprehend on this deep of a level. However, with the assistance of AI, researchers are beginning to delve deeper into the specific words and phrases used by managers in conference calls. This article documents the most frequently used clichés in earnings conference calls and constructs a dictionary of these expressions. Examples (provided in the Appendix of the paper) are “quite frankly” (used by the Pulte Homes CFO as he was delivering disappointing news); “vast majority” (used by the CEO of ITT Educational Services instead of providing a specific number); more or less ( an imprecise way of expressing things) etc.

The main research questions asked are as follows:

1. Is there a correlation between the tone of the conference calls and managers’clichès ?
2. Is there a correlation between the number of clichès and earning per share growth?
3. Is there a correlation between the number of clichès and prior months stock returns?
4. Do investors penalize companies which use a higher number of clichès?

## What are the Academic Insights?

By analyzing a dataset of earnings conference calls for US companies from the Thomson Reuters Street Events database from 2002 to 2016, the authors find that:

1. YES, the tone of the conference call is negatively correlated with the number of clichés
2. YES, earnings per share growth is negatively correlated with the number of clichés
3. YES, prior three months stock returns are negatively correlated with the number of clichés
4. YES, the number of clichés is negatively and significantly associated with three-day abnormal returns indicating that the use of clichés tends to signal further negative news to investors. This holds true even after including control variables like the overall tone of the conference calls, the length of the conference calls and earnings surprises. The caveat is that this effect on future stock returns is immediate (three days) and does not last for longer periods.

## Why does it matter?

This is an interesting example of how AI can be utilized to decipher information that is difficult — or impossible — for humans to sift through the haystack to find the needles. In examining an area of NLP in which machines or algorithms analyze a sample of unstructured data: the use of clichés in the text of conference calls, the researchers found a source of information not previously known. Now investors can listen to conference calls with an ear towards Managers utilization of clichés and assume that with more frequent use, the odds of poor financial results are to follow have increased.

## Abstract

> *In their communications with the public, company managers disclose internal information, sometimes unwittingly. Prior studies have documented that the tone change in earnings conference calls can help predict future excess returns. Similarly, managers who use euphemisms on earnings calls to describe negative performance (think “headwinds”) essentially convey negative information to investors, and their stock is negatively affected. This study investigates another mechanism to identify management’s hedging (or obfuscation): the use of clichés. In this article, the authors identify the most frequently used clichés in earnings calls and examine whether investors react negatively to them. They find that managers use more clichés when performance is bad, and investors correctly react negatively to clichés, even after controlling for negative earnings news and the general tone of th earnings conference call. They also find that a hedge portfolio consisting of long positions in companies that used no clichés and short position in companies that used at least four clichés earned an average of 2% per month and had a statistically significant intercept of 40 bps monthly after controlling for the five-factor Fama–French model.*
