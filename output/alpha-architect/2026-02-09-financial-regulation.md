---
title: "Financial Regulation and AI: A Faustian Bargain?"
slug: "financial-regulation"
date: "2026-02-09"
modified: "2026-02-09"
url: "https://alphaarchitect.com/financial-regulation/"
categories: ["Banking Institutions", "Elisabetta Basilico", "Research Insights", "AI and Machine Learning", "Other Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Financial Regulation and AI: A Faustian Bargain?

> Financial regulation has always faced a trade-off between simplicity and precision. Simple rules are transparent and robust, but often miss where risks actually build up. More sophisticated tools can be more precise, but they are harder to understand, harder to explain, and sometimes change behavior in unexpected ways.

Financial regulation has always faced a trade-off between simplicity and precision. Simple rules are transparent and robust, but often miss where risks actually build up. More sophisticated tools can be more precise, but they are harder to understand, harder to explain, and sometimes change behavior in unexpected ways.

## Financial Regulation and AI: A Faustian Bargain?

* Clayton and Coppola
* Working paper, 2025
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5365224)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight/) category

## Key Academic Insights

**Predictive Power Is Not the Same as Policy Wisdom**  
AI models can forecast where stress, forced selling, or fire sales are likely to occur. But regulation is not just about prediction. It is about intervention. A model may be excellent at forecasting outcomes while being largely silent about how those outcomes change once policy is applied. Using such models mechanically risks acting on correlations that are not policy invariant.

**Regulatory Value Comes from Alignment, Not Accuracy**  
The paper shows that a predictive model can improve welfare even if it provides no causal insight, but only when its predictions line up with areas where the regulator already understands the causal impact of intervention. Precision matters most where policy tools actually work. High overall accuracy is not enough.

**Deep Learning Fits Holdings Data Especially Well**  
The authors develop a graph-based deep learning model designed for financial holdings data, where investors and assets form a network. The model predicts trading patterns and liquidation pressure well out of sample, including during crises such as 2020. This shows that AI can meaningfully improve regulators’ real-time situational awareness

**AI Is a Complement to Structural Knowledge, Not a Substitute**  
The core message is not anti-AI. Predictive models are most useful when paired with economic reasoning and prior knowledge about how policy tools transmit through markets. AI expands what regulators can see, but it does not replace theory, judgment, or institutional design.

## Practical Applications for Investment Advisors

**Expect faster and more targeted policy responses**  
If regulators adopt AI-driven tools, stress episodes may evolve differently than in the past. Interventions may be more targeted, more asset-specific, and faster. Advisors should be prepared for liquidity events that unfold quickly and unevenly across markets.

**Watch for crowding created by perceived protection**  
When markets believe regulators can and will stabilize specific segments, investors may crowd those areas. What looks protected can become fragile precisely because too many portfolios lean on the same assumption. Advisors should treat regulatory backstops as changing risk, not eliminating it.

**Incorporate holdings-based risk, not just price-based risk**  
This paper highlights that fragility often comes from who holds what, not just from leverage or [valuations](https://alphaarchitect.com/us-exceptionalism/). Advisors can translate this insight by monitoring ownership concentration, fund overlap, and flow sensitivity in the assets clients hold.

## How to Explain This to Clients

> “Regulators are starting to use advanced AI tools to spot risks in real time. That can help limit damage during market stress, but it also changes how investors behave. If people expect support, they may take more risk, which can create new vulnerabilities. Our job is not to guess the next intervention, but to build portfolios that are resilient even when policy tools, market behavior, and incentives shift.”

## The Most Important Chart from the Paper

Figure 2 plots the correlation between the trained model’s predictions and the targets for both tasks: the blue bars show the performance on the training sample, while the red bars show the out-of-sample performance on the validation set.

![](https://alphaarchitect.com/wp-content/uploads/2026/01/2026-01-09-12_06_00-Financial-Regulation-and-AI_-A-Faustian-Bargain_.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

## Abstract

> ### 
>
> We examine whether and how granular, real-time predictive models should be integrated into central banks’ macroprudential toolkit. First, we develop a tractable framework that formalizes the tradeoff regulators face when choosing between implementing models that forecast systemic risk accurately but have uncertain causal content and models with the opposite profile. We derive the regulator’s optimal policy in a setting in which private portfolios react endogenously to the regulator’s model choice and policy rule. We show that even purely predictive models can generate welfare gains for a regulator, and that predictive precision and knowledge of causal impacts of policy interventions are complementary. Second, we introduce and train a deep learning architecture tailored to financial holdings data—a graph transformer—and we discuss why it is optimally suited to this problem. The model learns vector embedding representations for both assets and investors by explicitly modeling the relational structure of holdings, and it attains state-of-the-art predictive accuracy in out-of-sample forecasting tasks including trade prediction.
