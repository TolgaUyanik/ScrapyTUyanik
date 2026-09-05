---
title: "Bias Algorithms? How Ironic!"
slug: "bias-algorithms-how-ironic"
date: "2014-02-12"
modified: "2022-06-01"
url: "https://alphaarchitect.com/bias-algorithms-how-ironic/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Bias Algorithms? How Ironic!

> Human bias in algorithmic trading John Broussard, Andrei Nikiforov A version of the paper can be found here. Want a summary of academic papers with alpha? […]

### Human bias in algorithmic trading

* John Broussard, Andrei Nikiforov
* A version of the paper can be found [here.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2375739)
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category!](https://alphaarchitect.com/category/academic-research/)

### **Abstract:**

> This paper documents a stark periodicity in intraday volume and in the number of trades. We find activity in both variables spikes by about 20% at regular intervals of 5 or 10 minutes throughout the trading day. **We argue that this activity is the result of algorithmic trading influenced by human traders/programmers’ behavioral bias to transact on round time marks.** An alternative explanation, that algorithms choose to concentrate their trades in time to take advantage of lower costs or to protect themselves from better informed traders, is not supported.

### **Data Sources:**

Nanex, 2003 to 2006.

### **Alpha Highlight:**

Trading takes place at specific time intervals. Why didn’t the programmer tell the algo to trade at random times?

[![fi1](https://alphaarchitect.com/wp-content/uploads/2014/01/fi1.png)](https://alphaarchitect.com/wp-content/uploads/2014/01/fi1.png)  
Trading volume spikes every 5 or 10 minutes and returns to normal volumes 30 seconds later.

[![fi2](https://alphaarchitect.com/wp-content/uploads/2014/01/fi2.png)](https://alphaarchitect.com/wp-content/uploads/2014/01/fi2.png)

### **Strategy Summary:**

1. Paper finds that trading activity explodes on round time marks, such as every half hour.
   * Trading data (from Nanex) are quoted from 30 liquid U.S. stocks and 3 ETFs from April 17, 2003 to Oct 18, 2006, or a total of 882 trading days.
     + Figure 1 shows aggregate volume exhibits U-shaped pattern with sharp spikes in every 5 to 10 minutes.
     + Figure 2 shows percent changes in volume for each 30-second and spikes occur at highly regular intervals (30 minutes apart).
2. Paper then tests two competing hypotheses to explain this increased activity.
   1. Hypothesis 1: Round Numbers Hypothesis
      * Theory is that humans have a tendency towards round numbers when faced with decisions.
      * **Test:** Paper regresses the volume and trade variables on various non-overlapping time dummies to examine whether clustering is progressively more intense as the markers on the time line becomes more and more round.
      * Time dummies correspond to round hour marks (10:00 AM), half-hour marks (10:30 AM), fifteen minutes marks (9:45 AM and 10:15 AM), ten minutes marks (9:40 AM and 10:10 AM), and 5 minutes marks (9:55 AM and 10:05 AM).
        + Table 2 shows average volume increases on the corresponding time marks, indicating that humans tend to prefer round numbers.
   2. Hypothesis 2: Rational Concentration Hypothesis
      * Theory is that liquidity traders tend to cluster trading to protect themselves from better informed rivals (insiders) and take advantage of increased liquidity and reduced transaction costs.
      * **Test:** Paper calculates 5 measures of transaction costs and 1 measure of price impact (see p11) and then, regresses each liquidity variable on various time dummies to check whether there is a significant improving in liquidity on the round time marks.
        + Table 3 shows that five measures of liquidity do not change in any significant way during the spikes (fails to support hypothesis 2).
   * Results: Inclined to attribute the clustering to the human preference for round numbers rather than to a rational optimizing activity of traders and their algorithms.

### **Strategy Commentary:**

* Documents the behavioral bias the people prefer to use round numbers when faced with a task in an uncertain environment.
  + Good summary of the literature with examples of humans’ bias towards round numbers (in financial economics, psychology, and marketing).
* This paper makes sense!  When was the last time you scheduled a meeting at a time not ending in a 0 or 5?
  + Recommend meeting at 9:37 and see what reaction you get.

**Wonder how many “algo hunters” are taking advantage of this already?**
