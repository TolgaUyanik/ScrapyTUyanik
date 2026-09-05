---
title: "Machine Learning: The Recovery of Missing Firm Characteristics"
slug: "machine-learning-the-recovery-of-missing-firm-characteristics"
date: "2022-02-10"
modified: "2022-05-23"
url: "https://alphaarchitect.com/machine-learning-the-recovery-of-missing-firm-characteristics/"
categories: ["Research Insights", "Guest Posts", "Academic Research Insight", "AI and Machine Learning"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Machine Learning: The Recovery of Missing Firm Characteristics

> Firm characteristics are often missing, which forces both researchers and practitioners to come up with workarounds when handling missing data. Previous approaches resorted to either dropping observations with missing entries or simply imputing the cross-sectional mean of a given characteristic. As both procedures accompany serious drawbacks (see below), there is a need for more advanced methods. The authors set up an attention-based machine learning model, motivated by recent advances in natural language to find some answers

## **Recovering Missing Firm Characteristics with Attention-based Machine Learning**

* Heiner Beckmeyer and Timo Wiedemann, University of Muenster (Germany)
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4003455)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category.

## What are the research questions?

Firm characteristics are often missing, which forces both researchers and practitioners to come up with workarounds when handling missing data. Previous approaches resorted to either dropping observations with missing entries or simply imputing the cross-sectional mean of a given characteristic. As both procedures accompany serious drawbacks (see below), there is a need for more advanced methods. The authors set up an attention-based machine learning model, motivated by recent advances in natural language to find answers to the following questions:

1. How do firm characteristics relate to the cross-section of other – observed – characteristics and their historical evolution?
2. How well does the proposed machine learning approach fare against competing approaches?
3. How important is it to explicitly model nonlinear and interaction effects? How important is it to incorporate the temporal dynamics of the characteristics?
4. On which information does the model rely when uncovering the latent structure governing firm characteristics?

## What are the Academic Insights?

The authors show that:

1. The proposed model is highly accurate in extracting the latent structure underlying the evolution of observable firm characteristics. Their approach comfortably outperforms competing methods by a large scale. When using the model to reconstruct available firm characteristics in a controlled environment, the authors show an expected error of around 4 percentiles from the true value which is more than 2-times more accurate than the next-best method.
  
2. Incorporating information about the temporal evolution of the characteristics is essential to boost the model’s ability to reconstruct characteristics. While some characteristics exhibit a high degree of autocorrelation, others predominantly depend on cross-characteristic information. Incorporating both types of information is therefore decisive. The authors highlight that the model is flexible enough to simultaneously uncover a wide range of processes governing the evolution of characteristics in a simulation study.
  
3. Model sanity checks showing the distribution of the reconstructed (i.e., previously missing) characteristics attest internal validity, with results well in line with expectations. Information is more often missing for smaller firms, and those that would be considered of low quality.
  
4. Revisiting the literature on risk factors in financial research shows that many risk premia are likely much smaller than previously thought. Adding to the recent debate on replicability in financial research, the authors highlight, in turn, that most risk premia remain significant. The completed dataset poses an additional out-of-sample hurdle for existing and new risk premia to pass.
  
5. Recovered percentiles of firm characteristics have been made publicly available for future research [here](https://sites.google.com/view/beckmeyer/data-code).

  

## Why Does it Matter?

There is a tendency to simply drop observations with missing data points from the sample and base analyses on the reduced sample. Alternatively, missing characteristics are often imputed by the cross-sectional average. Both procedures, however, may seriously bias statistical inference if firm characteristics are not missing at random. For financial applications, as just one example, it is straightforward to see that this missing-at-random assumption likely does not hold empirically: smaller firms are generally required to provide less complete information. It is therefore of major importance to complete existing data sets of firm characteristics by accurately predicting missing entries in an informed fashion. Consequently, the method proposed in this paper may not only change the statistical significance of previous findings but can also be used to understand how far these findings carry over to a completed dataset, which ultimately leads to more-informed investment decisions.

## The Most Important Chart from the Paper

The most important table of the paper shows the superior performance of the author’s model to competing approaches. At the same time, it highlights that the model can accommodate characteristics of various sources, showing consistently high performance for accounting- and market-based characteristics, as well as hybrid characteristics, which draw information from both sources. Table 1 is shown below. Note the generally poor performance of the commonly used mean imputation method.

![](https://alphaarchitect.com/wp-content/uploads/2022/01/image-15.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

## **Abstract**

> *Firm characteristics are often missing. We set up an attention-based machine learning model borrowing ideas from state-of-the-art research in natural language processing to understand how characteristics relate to the cross-section of other – observed – firm characteristics and their historical evolution. Our model reconstructs firm characteristics with high accuracy and comfortably outperforms competing approaches. Revisiting the vast literature on risk factors in financial research reveals that disregarding the influence of missing observations likely overestimates the magnitude of factor premia. We also provide the filled distribution and raw values for all characteristics for future research.*
