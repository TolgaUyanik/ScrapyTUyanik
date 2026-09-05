---
title: "Can Artificial Intelligence outsmart seasoned equity analysts?"
slug: "can-artificial-intelligence-outsmart-seasoned-equity-analysts"
date: "2024-10-28"
modified: "2024-10-28"
url: "https://alphaarchitect.com/can-artificial-intelligence-outsmart-seasoned-equity-analysts/"
categories: ["Tommi Johnsen", "Research Insights", "Academic Research Insight", "AI and Machine Learning"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Can Artificial Intelligence outsmart seasoned equity analysts?

> If the task is to identify a firm’s true profitability, can AI outsmart seasoned analysts?

If the task is to identify a firm’s true profitability, can AI outsmart seasoned analysts? Given the increasingly bloated nature of financial reports, decoding the twists and turns associated with events like obscure one-time gains and out-of-nowhere expenses to extract core earnings has become challenging even for accountants. This research will unravel how AI can successfully attack the problem for us and maybe even outsmart the professionals.

## Scaling Core Earnings Measurement with Large Language Models

* Matthew Shaffer and Charles C.Y. Wang
* Working Paper
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4979501)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category.

## What are the research questions?

1. Describe the LLMs and prompting structure used in this research.
2. Do the LLMs estimate Core Earnings accurately from 10K filings?
3. Do estimates of Core Earnings made by LLMs outperform traditional benchmarks such as the GAAP Net Income and Compustat’s OPEPS and OIADP with respect to typical measures of earnings persistence?
4. What about non-recurring adjustments? Are the adjustments made by the LLM to GAAP Net Income, truly nonrecurring?
5. Do the LLMs generate Core Earnings measures that accurately forecast future net income and over the long-term as well?
6. Does the LLM-Generated Core Earnings outperform at the firm-level?

## What are the Academic Insights?

1. The researchers used OpenAI’s GPT-4o (LLM) to estimate core earnings. The specific objective was to evaluate the ability of the LLM in handling very complex financial disclosures contained in 10-K filings. Two prompting strategies: the lazy analyst approach and the sequential prompt approach, were given a single prompt or a sequence of prompts and as well as the definition of core earnings and the full text of the 10K. The ‘lazy analyst’ approached required the LLM to estimate core earnings and provide a rationale. No other guidance was given in order to assess the LLM’s basic performance. To maximize accuracy and effectiveness, the sequential prompt approach was used and instructed to follow 3 prompts: (1) identify unusual expenses/losses, (2) identify unusual income/gains, and (3) aggregate and quantify core earnings. Unlike other more limiting versions, GPT-4o can accommodate the lengthy text contained in 10-K filings.
2. YES. However, it depends on the specific LLM approach used. The structured approach provided better guidance, helping the LLM produce more accurate core earnings estimates. These approaches helped to evaluate the reasoning process of the LLM and how different prompting strategies influenced the quality of the model’s output. In contrast to the baseline prompting approach, the sequential prompting approach did produce a reliable core earnings measure. A high-quality [core earnings](https://alphaarchitect.com/2019/10/core-earnings-new-data-and-evidence/) measure should capture stable, ongoing profitability and exclude volatile, non-recurring components. The latter was superior at avoiding conceptual errors by breaking the forecasting task into small steps. Nonrecurring gains and losses were filtered out and then aggregated in an accurate manner. The baseline approach tended to confuse core earnings with other earnings-type measures such as EBITDA and Cashflow and made incorrect adjustments for recurring expenses such as Interest, Depreciation, and Amortization.
3. YES. Again, the sequential measure generated a core earnings forecast that reflected the stable components of profitability over time. The sequential model produced an autoregressive coefficient, which reflects the level of persistence, of .917 compared to the GAAP Net Income AR coefficient of .849. The higher coefficient suggests that the LLM core earnings measure captured the stable components of profitability over time. However,Compustat’s OPEPS and OIADP had slightly higher persistence values with coefficients of 1.0174 and 1.0178, respectively. The authors conclude the sequential approach still provided a competitive and valid measure of stability, capturing more meaningful elements of core profitability, especially when compared to GAAP Net Income.
4. WEAK. In this case, the objective was to make sure the adjustments to earnings are nonrecurring and do not affect or persist into the future. The results indicate the adjustments did include some recurring elements and did not exclude transitory components completely. Persistence coefficients were estimated for the sequential measure (.0288, not significant) and the ‘lazy analyst’ measure (.0759, significant at 5%), and Compustat’s OIADP (.3125, significant at 1%).
5. YES. The hypothesis that the core earnings measure accurately reflects components of profitability that drive future performance was validated. The LLM-generated core earnings measure provided more accurate predictions of future profitability than the benchmark. The mean absolute prediction error was $1.58 for the sequential measure, $1.77 for the GAAP Net Income benchmark, and $1.56 for Compustat’s OPEPS. The explanatory power (R-square) obtained from regression estimates of next-period net income was 70.86% for the sequential approach exceeded that of the GAAP Net Income benchmark at 60.87%. When the prediction horizon was extended to two years, the sequential measure produced an R² of 83.60%, higher than Compustat’s OPEPS 66.57%. The LLMs were more effective at capturing the components of earnings that persist over a longer term.
6. YES. Firm-level predictive regressions showed that the sequential approach was the most reliable earnings forecast. The statistics were convincing. The sequential model produced an R-square of 28.39%, and produced the highest average coefficient of 0.4564, and the lowest mean squared error.

## Why does it matter?

This research matters because it explores the practical use of LLMs to reduce the time, cost, and expertise needed for predicting core earnings from increasingly complex financial disclosures. The authors argue that the use of LLMs in this context could democratize financial analysis by allowing investors to access more reliable earnings metrics without relying solely on expensive proprietary databases or specialized financial expertise.

## The most important chart in the paper

![](https://alphaarchitect.com/wp-content/uploads/2024/10/2024-10-16-08_57_35-LLMs_Earnings_SSRN_Wes.pdf-and-2-more-pages-Personal-Microsoft​-Edge-1-1200x741.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

## Abstract

> We study the application of large language models (LLMs) to the estimation of core earnings, i.e., a  
> firm’s persistent profitability from its core business activities. This construct is central to investors’  
> assessments of economic performance and valuations. However, quantifying it requires judgment  
> and integration of information scattered throughout financial disclosures contextualized with general industry knowledge. This has become increasingly difficult as financial disclosures have become  
> more “bloated” and accounting standards have increased non-recurring impacts on GAAP net income.  
> LLMs, with their ability to process unstructured text, incorporate general knowledge, and mimic human reasoning, may be well-suited for this kind of task. Using the text of 10-K filings from U.S. public  
> companies between 2000 and 2023, we employ LLMs with two prompting strategies: (i) a baseline  
> “out of the box” approach providing only a definition of core earnings and the full 10-K, and (ii) a  
> structured “sequential” approach, refined through experiments, instructing the model to identify unusual losses, then gains, and then tabulate and aggregate them. We evaluate the models’ analyses by  
> reviewing their stated reasoning process and analyzing their core earnings measures with an array of  
> standard quantitative tests. Under the baseline approach, the LLM conflates core earnings with other  
> financial concepts (e.g., EBITDA). However, the sequential approach yields a valid core earnings measure that outperforms GAAP Net Income and Compustat’s OPEPS and OIADP in predicting average future earnings in most standard tests. Our findings are relevant for practitioners, showing how these  
> models can fail and succeed in complex tasks of this nature. For researchers, we pave a path for using current and future models to generate valid, neutral, scalable measures of core earnings, rather  
> than relying on surrogates provided by company management or standard data providers. Overall,  
> our findings suggest LLMs have enormous potential for lowering the costs associated with processing  
> and analyzing the increasingly bloated financial disclosures of publicly traded companies.
