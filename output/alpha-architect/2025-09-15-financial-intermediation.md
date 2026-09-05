---
title: "Why did credit marketplaces ditch peer-to-peer?"
slug: "financial-intermediation"
date: "2025-09-15"
modified: "2025-09-15"
url: "https://alphaarchitect.com/financial-intermediation/"
categories: ["Banking Institutions", "Elisabetta Basilico", "Research Insights", "Other Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Why did credit marketplaces ditch peer-to-peer?

> Most platforms now intermediate—pooling loans into short-dated portfolios and, increasingly, offering bank-like products that absorb liquidity risk. Why did credit marketplaces evolve away from pure peer-to-peer? This paper quantifies the welfare value of those design choices.

Over the past decade, online credit markets promised to “cut out the middleman.” Early platforms let lenders hand-pick loans and hold them to maturity. But a silent shift took place: most platforms now intermediate—pooling loans into short-dated portfolios and, increasingly, offering bank-like products that absorb liquidity risk. Why did credit marketplaces evolve *away* from pure peer-to-peer? This paper quantifies the welfare value of those design choices. Using universe-level data from a major Chinese platform (Renrendai), the authors show that maturity transformation and liquidity design—not just screening and monitoring—explain the rise of intermediation and who benefits from it. The punchline: marketplace intermediation boosts credit provision and lender surplus, but the optimal design flips with investors’ liquidity needs and the platform’s cost of creating liquidity.

## The Value of Financial Intermediation: Evidence from Online Debt Crowdfunding

* Braggion, Manconi, Pavanini, Zhu
* The Journal of Financial Economics , 2025
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3557942)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight/) category

## Key Academic Insights

**From P2P to Marketplace—A Complete Flip**

In 2010, 100% of Renrendai lending was peer-to-peer; by early 2017, >98% was marketplace (portfolio) credit. Portfolios were short-dated (3, 6, 12 months most common), while underlying loans were typically 36 months, creating a **~**22-month maturity mismatch and exposing investors to liquidity risk at rollover.

#### Liquidity Is Usually Fine—Until It Isn’t

When investors chose to liquidate at portfolio maturity, the average resale time on the internal secondary market was about half a day, but the distribution had a thick right tail: around 9.5% of portfolios took more than one day (mean 4.2 days, max 88 days). All investors in a given portfolio share that same realized resale time.

#### Intermediation Is Matching Maturities, Not Just Screening

A structural equilibrium model shows that allowing maturity mismatch expands the product menu and better matches lenders’ horizon preferences. In a counterfactual with only P2P, credit provision falls 73% and lender surplus drops 45%—clear welfare gains from marketplace intermediation, beyond classic screening and monitoring effects.

#### Who Values What? Heterogeneous Lenders

Lenders like yield across the board, but:

* A 10% increase in return raises direct-loan demand by about 12.1% versus roughly 6.5% for portfolio products.
* Sensitivity to liquidity risk (resale time) is much higher for less-active investors; for the most active, the effect is near zero.

Translation: sophisticated, frequent users tolerate liquidity risk; casual investors don’t.

#### Platform Design Choices Are Deliberate

When assembling portfolios, the platform tilts to longer-maturity, lower-rate loans and avoids higher-default categories, consistent with easing adverse selection while controlling realized risk in packaged products. It also prefers primary-market loans (fee economics).

## Practical Applications for Investment Advisors

**1) Look Through the Wrapper: Horizon and Liquidity Firs**t

Short-dated portfolio wrappers over long loans embed rollover and liquidity risk. Evaluate expected resale times and their tails, not just the average.

#### **2) Match Product to Client Type**

* Sophisticated or yield-focused clients may tolerate marketplace liquidity risk.
* Liquidity-sensitive or infrequent investors may prefer bank-like features where the platform bears liquidity risk.

#### 3) Platform Selection Equals Design Selection

Two platforms with the same borrower mix can deliver very different investor outcomes depending on: maturity mismatch policy, liquidity commitment, secondary-market mechanics (price fixed at par versus market-clearing), and portfolio construction constraints (credit screens).This echoes broader discussions in private credit markets, where structure and underwriting strongly affect investor outcomes. For a deeper dive into how different segments of private credit compare, see our post entitled [Private Credit: Upper Versus Lower Middle Market Lending](https://alphaarchitect.com/middle-market-lending/?utm_source=chatgpt.com).

#### 4) Stress the Tails

Average liquidity looks fine, but right-tail delays (days to liquidate) matter at scale and in stress. Build liquidity buffers and set expectations accordingly.

## How to Explain This to Clients

“Think of many online lending products as short-term wrappers on long-term loans. That design helps offer attractive menus and keeps money flowing to borrowers. But if you want your cash back exactly on time, you may have to wait while the platform resells your loans—sometimes days. Some platforms now offer bank-like options that promise quick access to cash; in those, the platform takes on the liquidity risk, not you. So the decision is a trade-off: higher yield with possible delays, or lower yield with faster access.”

## The Most Important Chart from the Paper

**Fig. 1. Direct and marketplace loans at Renrendai, 2010Q4–2017Q1**

The figure plots the outstanding volumes of loans at Renrendai, for each calendar quarter over the period 2010–2017. The dark bars denote direct, or peer-to-peer, loans, and the lighter-shaded bars loans that are part of portfolio products, i.e., marketplace loans.

![](https://alphaarchitect.com/wp-content/uploads/2025/09/The-value-of-financial-intermediation_-Evidence-from-online-debt-crowdfunding-.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

## Abstract

> ### 
>
> Most online marketplaces are peer-to-peer. Credit ones, however, are not and they have resurrected many features of traditional financial intermediaries. To understand why, we use online credit as a laboratory to investigate the value of financial intermediation. We develop a structural model of online debt crowdfunding and estimate it on a novel database. We find that abandoning the peer-to-peer paradigm raises lender surplus, platform profits, and credit provision, but exposes investors to liquidity risk. A counterfactual where the platform resembles a bank by bearing liquidity risk can generate larger lender surplus and credit provision when liquidity is low and lenders are risk averse.
