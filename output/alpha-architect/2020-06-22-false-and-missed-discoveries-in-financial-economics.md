---
title: "Can Statistics Actually Determine if Managers Have No Skill?"
slug: "false-and-missed-discoveries-in-financial-economics"
date: "2020-06-22"
modified: "2020-06-22"
url: "https://alphaarchitect.com/false-and-missed-discoveries-in-financial-economics/"
categories: ["Research Insights", "Basilico and Johnsen", "Academic Research Insight", "Active and Passive Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Can Statistics Actually Determine if Managers Have No Skill?

> Campbell Harvey and Yan Liu Journal of Finance, 2020 A version of this paper can be found here Want to read our summaries of academic finance […]

* Campbell Harvey and Yan Liu
* Journal of Finance, 2020
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3073799)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Research Questions?

Whether they are selecting a manager, a factor, or a strategy, investors can make two types of mistakes.

* We thought we were hiring Peter Lynch, not this loser!
  + A Type I error (or false discovery) when selecting a manager who turns out to be unskilled.
* That Warren Buffett guy is washed up, let’s pass.
  + A type II error (missed discovery) when not selecting or missing a manager that the investor thought was unskilled but was not.

The authors of this paper seek to exhibit ways in which type I and type II errors can be measured. Additionally, these types of errors present varying levels of economic importance and cost not fully taken into account by current statistical analysis.

In the context of multiple testing, it is difficult to evaluate the Type II error rate for at least two reasons: large numbers of alternative hypotheses and the multidimensional nature of the data.

In this paper, the authors propose a different approach, to consider the importance of test power. In other words, how well can statistical tests actually identify skill if it genuinely exists. Turns out that the power of common “manager performance” tests is pretty poor. To include the [often-cited paper](http://mba.tuck.dartmouth.edu/bespeneckbo/default/AFA611-Eckbo%20web%20site/AFA611-S8C-FamaFrench-LuckvSkill-JF10.pdf) by Fama and French, “Luck versus Skill in the Cross-Section of Mutual Fund Returns.” The TLDR is that the Fama French tests would never find much evidence for manager skill, even if the reality was that there were lots of managers with investing skills.

The authors propose the following:

1. A simple metric to summarize the information contained in the parameters of interest and to evaluate Type I and Type II error rates. In essence, this metric reduces the dimensionality of the parameters of interest and allows us to evaluate error rates around what we consider a reasonable set of parameter values.
2. An error rates evaluation tool using a bootstrap method, which allows investors to capture cross-sectional dependence nonparametrically. Because this method is quite flexible in terms of how it defines the severity of false positives and false negatives, it is possible to evaluate error rate definitions that are appropriate for a diverse set of finance applications.

## What are the Academic Insights?

The paper proceeds with two practical applications of this framework: to select outperforming strategies (by studying two datasets, the Standard and Poor’s CAPIQ database on a broad set of 484 long-short alpha strategies, and the 18,113 anomalies studied in Yan and Zheng, 2017), and to analyze mutual fund performance (by focusing on the joint test approach used in Fama and French (2010), which treats the mutual fund population as a whole and tests whether the entire mutual fund population has zero alpha (the null hypothesis) versus at least one fund has a positive alpha).

The authors show that when the threshold t-statistic increases, the Type I error rate (the rate of false discoveries among all discoveries) declines while the Type II error rate (the rate of misses among all non discoveries) increases.

With regards to the first application, the authors find that neither 2.0 (the usual cutoff for 5% significance) nor 3.0 (based on Harvey, Liu, and Zhu (2016)) is optimal from the perspective of the investor. The preferred choices lie between 2.0 and 3.0 for the examples considered and depends on both p0 and the data that we study. This bootstrap-based framework generates t-statistic thresholds that are calibrated to the particular decision being considered and the particular data under analysis.

With regards to the second application, Fama and French’s (2010) joint test suggests that very few (if any) funds exhibit skill on a net return basis. The authors confirm that the Fama and French (2010) approach performs well in terms of the Type I error rate for the mutual fund data. However, they find that the Type II error rates(1) are very high. Even when 2% of funds are truly outperforming and are endowed with on average an annualized alpha of 10.66%, there is still an 86.9% chance (at the 5% significance level) of the Fama and French (2010) approach falsely declaring a zero alpha for all funds.

Given the above finding, the authors explore whether there are indeed outperforming funds. Their conclusion is as follows:

> “*There is some evidence for the existence of outperforming funds but consistent with the long literature in mutual fund evaluation, it is only modest evidence of fund outperformance*.”

## Why does it matter?

Current research on multiple testing focuses on controlling the Type I error rate, This study shows that it is also important to consider the Type II error rate. For the selection of investment strategies, a weighted average of the Type I error rate and the Type II error rate is likely more consistent with the investor’s objective function. With the advent of big data and higher computing power, it is important to try and correct data mining as much as possible. This is an attempt made by the authors of the paper.

It’s an intense paper but worth the read!

## The Most Important Chart from the Paper:

![](https://alphaarchitdev.wpengine.com/wp-content/uploads/2020/06/image-19.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> Multiple testing plagues many important questions in finance such as fund and factor selection. We propose a new way to calibrate both Type I and Type II errors. Next, using a double-bootstrap method, we establish a t-statistic hurdle that is associated with a specific false discovery rate (e.g., 5%). We also establish a hurdle that is associated with a certain acceptable ratio of misses to false discoveries (Type II error scaled by Type I error), which effectively allows for differential costs of the two types of mistakes. Evaluating current methods, we find that they lack power to detect outperforming managers.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | i.e., the probability of failing to reject the null hypothesis |

 function footnote\_expand\_reference\_container\_57097\_73() { jQuery('#footnote\_references\_container\_57097\_73').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_57097\_73').text('−'); } function footnote\_collapse\_reference\_container\_57097\_73() { jQuery('#footnote\_references\_container\_57097\_73').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_57097\_73').text('+'); } function footnote\_expand\_collapse\_reference\_container\_57097\_73() { if (jQuery('#footnote\_references\_container\_57097\_73').is(':hidden')) { footnote\_expand\_reference\_container\_57097\_73(); } else { footnote\_collapse\_reference\_container\_57097\_73(); } } function footnote\_moveToReference\_57097\_73(p\_str\_TargetID) { footnote\_expand\_reference\_container\_57097\_73(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_57097\_73(p\_str\_TargetID) { footnote\_expand\_reference\_container\_57097\_73(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
