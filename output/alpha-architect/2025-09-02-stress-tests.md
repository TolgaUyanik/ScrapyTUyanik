---
title: "Designing Risk Scenarios"
slug: "stress-tests"
date: "2025-09-02"
modified: "2025-09-01"
url: "https://alphaarchitect.com/stress-tests/"
categories: ["Banking Institutions", "Elisabetta Basilico", "Research Insights", "Other Insights", "Corporate Governance"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Designing Risk Scenarios

> This paper rethinks how financial regulators should design stress tests. Rather than treating stress testing as a pass/fail assessment, the authors show it should be viewed as an exercise in information gathering.

This paper rethinks how financial regulators should design stress tests. Rather than treating stress testing as a pass/fail assessment, the authors show it should be viewed as an exercise in information gathering. Using a Kalman filter model, they demonstrate how regulators can optimize stress scenarios to learn the most about banks’ exposures to systemic risk. The paper emphasizes the trade-off between signal clarity and [estimation error](https://alphaarchitect.com/reducing-estimation-error-in-mean-variance-optimization/), and shows that better-designed scenarios can help regulators choose between blanket capital rules and more efficient, targeted interventions.

## Designing Stress Scenarios

* Cecilia Parlatore & Thomas Philippon
* The Journal of Finance, 2025
* A version of this paper can be found [here](https://www.nber.org/papers/w29901)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight/) category

## Key Academic Insights

**Stress Testing Is an Information Problem**

The paper reframes stress testing as a learning mechanism. Regulators use stress tests not just to assess resilience, but to learn about banks’ unknown exposures to macroeconomic risk factors. By modeling this process via a Kalman filter, the authors treat the design of scenarios as a problem of optimal information acquisition.

#### Optimal Scenarios Depend on Trade-offs

Regulators face a trade-off: more extreme stress scenarios may yield better signals about risk exposures but also lead to higher estimation noise. The optimal scenario design balances this trade-off based on **intervention costs**, regulatory objectives, and prior beliefs about systemic risks.

#### Systemic Risks Require Targeted Stress

When risks are correlated across institutions, regulators should prioritize scenarios that stress those systemic factors. The more interconnected the exposures, the more informative the stress scenario becomes for making precise interventions that minimize financial system-wide disruptions.

#### Capital vs. Targeted Interventions

Regulators can respond to stress test results by imposing either general capital requirements or targeted interventions (e.g., LTV caps). The paper shows that targeted interventions require more precise information, which means that designing scenarios that sharpen this insight has higher value when targeted actions are feasible.

## Practical Applications for Investment Advisors

**Understand the Purpose Behind Stress Testing**

Stress tests aren’t just about checking if banks can survive hypothetical recessions. They’re about giving regulators better visibility into risk exposures. Knowing this helps advisors better interpret stress test outcomes and anticipate regulatory responses.

#### Tailor Risk Mitigation to Information Quality

When executing portfolio stress tests, advisors might design scenarios that target specific risk factors (e.g., inflation shocks or interest rate jumps) where exposures are less well understood, especially for complex or opaque assets.

#### Expect Scenario Design to Evolve

The paper suggests that scenario designs should change over time as regulators learn more. Advisors can use this logic to rotate or evolve their own internal stress testing to mirror changes in macro conditions and exposure uncertainty. Want to see how regulatory stress frameworks influence real-world market pricing? Check out our earlier post on [The Variance Risk Premium is Pervasive](https://alphaarchitect.com/the-variance-risk-premium-is-pervasive/), which explores how stress testing shapes risk mitigation behavior in banks.

## How to Explain This to Clients

“Stress tests aren’t crystal balls—they’re smart questions regulators ask to better understand where risk lies in the financial system. The more useful the answers, the more tailored and effective the actions regulators can take. It’s a bit like a doctor ordering the right blood test before prescribing medicine.”

## The Most Important Chart from the Paper

**Figure 2: Feasible Set of Residual Variances**  
This figure shows how the posterior uncertainty about banks’ risk exposures changes based on prior correlations among risk factors. The more correlated the exposures, the more information can be extracted from a given scenario, and the more targeted the stress test can become.

![](https://alphaarchitect.com/wp-content/uploads/2025/08/Designing-Risk-Scenarios.pdf-Adobe-Acrobat-Reader-64-bit.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

## Abstract

> ### 
>
> We develop a tractable framework to study the optimal design of stress scenarios. A principal wants to manage the unknown risk exposures of a set of agents. She asks the agents to report their losses under hypothetical scenarios before mandating actions to mitigate the exposures. We show how to apply a Kalman filter to solve the learning problem and we characterize the scenario design as a function of the risk environment, the principal’s preferences, and the available remedial actions. We apply our results to banking stress tests. We show how the principal learns from estimated losses under different scenarios and across different banks. Optimal capital requirements are set to cover losses under an adverse scenario while targeted interventions depend on the covariance between residual exposure uncertainty and physical risks.
