---
title: "Fund Selection When Borrowing Is Restricted"
slug: "fund-selection-when-borrowing-is-restricted"
date: "2026-03-02"
modified: "2026-03-01"
url: "https://alphaarchitect.com/fund-selection-when-borrowing-is-restricted/"
categories: ["Transaction Costs", "Empirical Methods", "Elisabetta Basilico", "Research Insights", "Other Insights", "Behavioral Finance", "ETF Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Fund Selection When Borrowing Is Restricted

> Once borrowing is realistically restricted, the Sharpe ratio can stop lining up with what investors actually care about: utility. This paper argues that in this constrained world, the geometric mean is a better compass.

Selecting mutual funds is one of the most important jobs investors face. Yet the tool everyone reaches for, the Sharpe ratio, quietly assumes something most real people do not have: the ability, and willingness, to borrow at the risk free rate to lever the “best” fund up or down to their preferred risk level. Once borrowing is realistically restricted, the Sharpe ratio can stop lining up with what investors actually care about: utility. This paper argues that in this constrained world, the geometric mean is a better compass. And a shrinkage adjusted version, the generalized geometric mean (GGM), can improve real world fund ranking and selection.

## **Mutual Fund Selection When Borrowing Is Restricted: On the Virtues of the Generalized Geometric Mean**

* Moshe Levy
* Financial Analyst Journal, 2025
* A version of this paper can be found [here](https://www.tandfonline.com/doi/full/10.1080/0015198X.2025.2589733?src=)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight/) category

## Key Academic Insights

**The Sharpe ratio is “almost perfect” only in a world with borrowing**  
With unlimited borrowing at the risk free rate, the highest Sharpe fund can be levered to match the risk of any other fund while delivering a higher expected return. That makes Sharpe rankings line up extremely closely with investor welfare. But this alignment relies on leverage being available and used.

**Borrowing restrictions break the Sharpe ratio’s welfare ranking**  
When investors cannot borrow, they cannot lever the top Sharpe fund to reach their desired risk point. In this setting, two funds with similar [Sharpe ratios](https://alphaarchitect.com/does-sharpe-parity-work-better-than-risk-parity/) can offer very different “opportunity sets” once you allow only lending, not borrowing. That is why the Sharpe ratio can rank a fund highly even when it delivers lower certainty equivalent outcomes for many investors.

T**he geometric mean becomes a better practical ranking statistic**  
The paper’s core claim is that when borrowing is restricted, ranking by geometric mean (GM) aligns much more closely with investor welfare than ranking by Sharpe or by common alpha measures. The intuition is that GM naturally rewards higher compounded growth and penalizes volatility in a way that better matches constrained choice.

**The generalized geometric mean fixes the “estimation reality” problem**  
Even if GM is the right target, estimating future GM from past returns is noisy. The proposed solution is a generalized geometric mean (GGM.) Shrink the gross, pre fee, GM toward the cross sectional mean because past performance is an error prone estimate of the future. Then subtract fees without shrinking them, because fees are largely known. This approach, which effectively overweight fees relative to noisy past performance, improves out of sample fund selection.

## Practical Applications for Investment Advisors

**Use the right metric for the constraint your client actually faces**  
Most clients are not borrowing to lever mutual funds. Some cannot. Some will not. Some are effectively constrained by platform rules, risk controls, or common sense. Sharpe is the right ranking rule only when clients can lever at the risk-free rate. When leverage is constrained, Sharpe can misrank funds because you can’t scale the max-Sharpe fund to the desired risk level. A GM or GGM style ranking is designed for the no borrowing reality, so it better matches what the client can truly implement.

**Make fees matter more, because they are the part you can actually know**  
People often overweight recent returns and underweight fees. But returns are noisy and hard to forecast, while fees are one of the few things you can be fairly sure about. GGM builds this into the ranking: it discounts past performance for estimation error, but takes fees at face value. That automatically gives fees more influence in the decision than a naive performance screen. If your client cannot explain why a higher fee is worth it in terms of a repeatable edge, the default assumption should be that the fee is real and the edge is uncertain.

**Improve fund shortlists without pretending you can forecast perfectly**  
You do not need to turn your process into a math contest. The takeaway is a process upgrade. When building a shortlist, prefer measures that are consistent with constrained implementation and robust to estimation error. Practically, that means de emphasizing Sharpe and conventional alpha screens as primary ranking tools in constrained accounts, and leaning more on compounding aware metrics plus fee discipline.

**Client fit beats metric purity**  
The point is not “everyone must buy the top GM fund.” The point is: if you are ranking and selecting among active funds, the criterion should match the client’s constraint set and behavioral reality.

**Use retirement conversations to reset the benchmark**  
Many clients judge success by raw returns. The paper shows raw returns can look fine while risk-adjusted performance deteriorates. Advisors can educate clients to focus on outcomes that matter: meeting spending goals, managing downside risk, controlling taxes and fees, and maintaining a robust allocation.

## How to Explain This to Clients

> “Sharpe ratio works best in a world where you can borrow to boost a good fund and lend to dial it down. Most people do not invest that way. If you cannot borrow, two funds that look ‘equally good’ by Sharpe can actually lead to different outcomes. This research suggests we should pay more attention to compounded growth and to fees. Fees are certain. Performance is noisy. So we use a ranking approach that better matches what you can really do in your account.”

## The Most Important Chart from the Paper

![](https://alphaarchitect.com/wp-content/uploads/2026/01/2026-01-15-13_05_06-Mutual-Fund-Selection-When-Borrowing-Is-Restricted-On-the-Virtues-of-the-Genera.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

## Abstract

> ### 
>
> The Sharpe ratio is almost perfectly aligned with investors’ welfare when borrowing is unrestricted. However, when borrowing is realistically restricted, this alignment breaks down dramatically. We show that the geometric mean (GM) provides a much better alternative for fund ranking in this case. Estimates of the ex-ante GM can be improved by first shrinking the sample gross GM and then subtracting fees. The generalized GM (GGM) captures this idea and provides a good estimate of the future net GM. We argue that mutual fund selection can be substantially improved by employing the GGM rather than the more popular Sharpe ratio or alpha.
