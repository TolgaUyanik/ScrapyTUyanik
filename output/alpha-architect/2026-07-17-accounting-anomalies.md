---
title: "Two Accounting Anomalies: One May Be Risk, the Other Is Mispricing"
slug: "accounting-anomalies"
date: "2026-07-17"
modified: "2026-07-06"
url: "https://alphaarchitect.com/accounting-anomalies/"
categories: ["Asset Growth", "Accruals", "Research Insights", "Factor Investing", "Larry Swedroe", "Other Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Two Accounting Anomalies: One May Be Risk, the Other Is Mispricing

> Accounting anomalies are dynamic, and the ultimate interpretation depends on sample period, market structure, and the pricing model used.

Two of the longest-running puzzles in accounting and asset pricing research are the accrual anomaly and the post-earnings-announcement drift, or PEAD. Both describe return patterns that standard one-period asset pricing models struggle to explain, and both have generated a huge literature. The recurring question has been the same: is the market mispricing the information, or is it rationally pricing risk that one-period models may miss?

Stephen Penman and Julie Lei Zhu, authors of the June 2026 paper “Explaining Two Prominent Accounting Pricing [Anomalies](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6963000): The Accrual Anomaly and the Post-Earnings-Announcement Drift,” revisit both anomalies and reach two different conclusions. Their sample runs from April 1982 through March 2022.

**Why the benchmark matters**

Most prior research has evaluated these return patterns using one-period models such as CAPM or the Fama–French factor models. Penman and Zhu argue that those benchmarks can be misleading for investors who operate across multiple periods. Under Merton’s intertemporal asset pricing framework, investors care not only about current returns but also about protecting future wealth and preserving future investment opportunities.

That matters because accounting information is inherently forward-looking. Accruals, by design, link current earnings to future earnings and thus speak to risk in future cash flows, dividends, and consumption. In the authors’ framework, the market may price those multiperiod risks in ways that one-period models do not capture [Penman & Zhu (2026)](https://protect.checkpoint.com/v2/r01/___https:/papers.ssrn.com/sol3/papers.cfm?abstract_id=6963000___.YXAzOnNhcmFncmlsbG86Yzpnb29nbGVfbWFpbF9hdHRhY2htZW50OmUwZjJmZThlZDQ2MjYyOWQ4YmFmNDQwYWU5MzA2YTQxOjc6ZGIwZDo5MjJlYWZhOWQ3ODA1MDM4N2ZjZWM5N2RiMmU5ZjQyNGY4YTVjZTkxZjM0YmNhNzRlYzg5NGEwOTZhNTkyMmJhOnA6VDpO).

**The two-factor model**

The paper implements a two-factor model: the market portfolio plus a fundamental hedge factor constructed from accounting information. The hedge factor is an annually rebalanced long–short portfolio that is long firms with the highest implied risk to future earnings and short firms with the lowest. The short side behaves like insurance in bad markets; the long side provides the reverse exposure, performing relatively better in up markets but offering less protection during downturns.

The authors test whether returns on portfolios sorted by earnings-to-price, accruals, momentum, PEAD (standardized unexpected earnings), revenue surprises, and analyst forecast revisions can be explained by exposure to these two factors. If the model is appropriate, portfolios should show market betas near 1.0, systematic variation in hedge exposure, and little or no alpha.

**What the paper found on accruals**

The accrual results are the cleanest. Across multiple data sources, sample windows, and accrual definitions, accrual-sorted portfolios behave in a manner consistent with rational pricing rather than clear mispricing. Market betas are close to 1.0, hedge-factor exposure varies systematically across deciles, and alphas are generally near zero once exposures are accounted for.

Put plainly, the return spread associated with accruals is largely explained by differences in exposure to the hedge factor rather than unexplained [abnormal returns](https://alphaarchitect.com/fascinating-research-alert-earning-calls-cliches-and-negative-abnormal-returns/) in this model. The authors therefore argue that accruals appear consistent with a priced risk characteristic when assessed within their intertemporal framework.

**Why high accruals can still have lower returns**

This point often causes confusion. High accruals imply more uncertainty about future earnings before those earnings are realized, but greater uncertainty alone does not mechanically imply higher expected stock returns. In a multiperiod framework, what matters is the nature of the risk: whether it provides exposure investors want to hold or whether it offers hedge-like protection that investors value. In the authors’ interpretation, accruals help reveal how a stock loads on the hedge factor; high-accrual portfolios may provide more of the hedge-like exposure that multiperiod investors value, which in this framework can be associated with lower expected returns..

Table 2 shows that the low-accrual decile earned a higher raw excess return than the high-accrual decile over the sample period. However, once returns are adjusted for exposure to the market and hedge factor, alphas are essentially zero. The authors’ central point is that the return difference is explained by risk exposures rather than leftover abnormal performance in their sample and model.

![](https://alphaarchitect.com/wp-content/uploads/2026/07/Table-2-1200x1266.webp)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

**What the paper found on PEAD**

The story for PEAD is different. Post-earnings-announcement drift—the tendency for prices to continue moving in the direction of an earnings surprise after the announcement—is the classic underreaction pattern. Using portfolios formed on standardized unexpected earnings (SUE), the paper finds significant alphas that the two-factor model cannot fully explain. High-SUE portfolios earn positive alpha, low-SUE portfolios earn negative alpha, and hedge-factor exposures do not align with the pattern a pure risk-based story would predict. In this model, PEAD therefore looks more like mispricing than compensation for risk.

Penman and Zhu also document that PEAD has diminished over time, consistent with the hypothesis that once a behavioral-based return pattern becomes widely known, arbitrage reduces its profitability. Still, PEAD did not completely disappear in their sample, suggesting that limits to arbitrage and market frictions can allow some residual drift to persist. This pattern is consistent with adaptive-efficiency ideas such as Andrew Lo’s [Adaptive Markets Hypothesis](https://protect.checkpoint.com/v2/r01/___https:/en.wikipedia.org/wiki/Adaptive_market_hypothesis___.YXAzOnNhcmFncmlsbG86Yzpnb29nbGVfbWFpbF9hdHRhY2htZW50OmUwZjJmZThlZDQ2MjYyOWQ4YmFmNDQwYWU5MzA2YTQxOjc6MTgwMDphMDMwZGQwYjlkODlhMTE3N2RjOTRhOTIxNmExNGU1NzNhY2E5YjRhZjI0NTdmOGUzYjhkMjE4ODFkYjdhOTdjOnA6VDpO).

**Broader evidence**

The paper extends the analysis to momentum, revenue surprises, and analyst-forecast revisions. Momentum produces non-zero alpha in this framework, which is consistent with a mispricing interpretation; similarly, drifts following revenue surprises and forecast revisions behave like PEAD and are not fully explained by the hedge factor. The result is a useful split: accounting-related return patterns are not homogeneous—some (accruals) are consistent with priced risk in this model, while others (PEAD, momentum, certain forecast- and revenue-related drifts) are better characterized as mispricing.

**Implications for market efficiency**

The implications are nuanced. The paper suggests markets can price some accounting information as risk while underreacting to other signals in ways that produce persistent return drift. In other words, efficiency appears to be signal-specific. For investors, the takeaway is that a historically profitable strategy is not necessarily a clean, risk-free arbitrage: some premiums can reflect compensation for priced multiperiod risk, while others reflect behavioral mispricing that arbitrageurs may erode over time.

**Conflicting evidence**

A complication for interpreting PEAD (and, to a lesser extent, accruals) is that other studies document sizeable changes in the anomalies over time. For example, Charles Martineau’s study “[Rest in Peace Post-Earnings Announcement Drift”](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3111607) finds that, in modern markets, prices often fully reflect earnings surprises on the announcement date, leading to the disappearance of PEAD for many large stocks by 2006, and later for even microcaps. That finding is consistent with the idea that arbitrage can eliminate behavioral anomalies, and it highlights how anomaly strength can weaken or vanish as markets, trading technology, and information dissemination change.

Other recent work finds that the accrual anomaly can persist in some settings but disappear in others. For example, one [paper](https://protect.checkpoint.com/v2/r01/___https:/papers.ssrn.com/sol3/papers.cfm?abstract_id=4803248___.YXAzOnNhcmFncmlsbG86Yzpnb29nbGVfbWFpbF9hdHRhY2htZW50OmUwZjJmZThlZDQ2MjYyOWQ4YmFmNDQwYWU5MzA2YTQxOjc6MTViMDo3MzNlOTNhZTFhNGJlYTVmZDhlN2U4ZjhjZjAyMTU2ZjRhNGVmZThlOTU0NTk2MzNjMGFlOGU4ZmFiOTg0NmNmOnA6VDpO) reports that the anomaly “lives on” in neglected firms and where investors are less familiar with the accrual calculation, while [another](https://protect.checkpoint.com/v2/r01/___https:/dl.acm.org/doi/abs/10.1287/mnsc.1110.1320___.YXAzOnNhcmFncmlsbG86Yzpnb29nbGVfbWFpbF9hdHRhY2htZW50OmUwZjJmZThlZDQ2MjYyOWQ4YmFmNDQwYWU5MzA2YTQxOjc6NWU5ZjoyZGYzMGQ2YTQ1ODVmNTBkMzdlNTJiYjU0YmM2ODM4MjE4ZTEzZjliZmIzMDUyNzkwNzIyNjM1OThmMTNhMDQzOnA6VDpO) finds that the anomaly has decayed in U.S. markets as hedge-fund capital increased. A separate Canadian [study](https://protect.checkpoint.com/v2/r01/___https:/papers.ssrn.com/sol3/papers.cfm?abstract_id=4560364___.YXAzOnNhcmFncmlsbG86Yzpnb29nbGVfbWFpbF9hdHRhY2htZW50OmUwZjJmZThlZDQ2MjYyOWQ4YmFmNDQwYWU5MzA2YTQxOjc6OTIyMDpkYWEzMjhjZmQ1MGE1MWFhZDc0NGVkM2M2ZDAyMjY4ZTRlNDljMTkzYmMyMDZkNGUxM2RlYmY3NWRlMThlZmMwOnA6VDpO) also reports strong abnormal returns for larger TSX firms, but mixed findings once smaller firms are included. These mixed findings suggest that the final verdict on whether accruals represent a durable priced risk premium rather than time-varying mispricing remains unsettled.

**Conflicting evidence**

A complication for interpreting PEAD (and, to a lesser extent, accruals) is that other studies document sizeable changes in the anomalies over time. For example, Charles Martineau’s study “[Rest in Peace Post-Earnings Announcement Drift”](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3111607) finds that, in modern markets, prices often fully reflect earnings surprises on the announcement date, leading to the disappearance of PEAD for many large stocks by 2006, and later for even microcaps. That finding is consistent with the idea that arbitrage can eliminate behavioral anomalies, and it highlights how anomaly strength can weaken or vanish as markets, trading technology, and information dissemination change.

Other recent work finds that the accrual anomaly can persist in some settings but disappear in others. For example, one [paper](https://protect.checkpoint.com/v2/r01/___https:/papers.ssrn.com/sol3/papers.cfm?abstract_id=4803248___.YXAzOnNhcmFncmlsbG86Yzpnb29nbGVfbWFpbF9hdHRhY2htZW50OmUwZjJmZThlZDQ2MjYyOWQ4YmFmNDQwYWU5MzA2YTQxOjc6MTViMDo3MzNlOTNhZTFhNGJlYTVmZDhlN2U4ZjhjZjAyMTU2ZjRhNGVmZThlOTU0NTk2MzNjMGFlOGU4ZmFiOTg0NmNmOnA6VDpO) reports that the anomaly “lives on” in neglected firms and where investors are less familiar with the accrual calculation, while [another](https://protect.checkpoint.com/v2/r01/___https:/dl.acm.org/doi/abs/10.1287/mnsc.1110.1320___.YXAzOnNhcmFncmlsbG86Yzpnb29nbGVfbWFpbF9hdHRhY2htZW50OmUwZjJmZThlZDQ2MjYyOWQ4YmFmNDQwYWU5MzA2YTQxOjc6NWU5ZjoyZGYzMGQ2YTQ1ODVmNTBkMzdlNTJiYjU0YmM2ODM4MjE4ZTEzZjliZmIzMDUyNzkwNzIyNjM1OThmMTNhMDQzOnA6VDpO) finds that the anomaly has decayed in U.S. markets as hedge-fund capital increased. A separate Canadian [study](https://protect.checkpoint.com/v2/r01/___https:/papers.ssrn.com/sol3/papers.cfm?abstract_id=4560364___.YXAzOnNhcmFncmlsbG86Yzpnb29nbGVfbWFpbF9hdHRhY2htZW50OmUwZjJmZThlZDQ2MjYyOWQ4YmFmNDQwYWU5MzA2YTQxOjc6OTIyMDpkYWEzMjhjZmQ1MGE1MWFhZDc0NGVkM2M2ZDAyMjY4ZTRlNDljMTkzYmMyMDZkNGUxM2RlYmY3NWRlMThlZmMwOnA6VDpO) also reports strong abnormal returns for larger TSX firms, but mixed findings once smaller firms are included. These mixed findings suggest that the final verdict on whether accruals represent a durable priced risk premium rather than time-varying mispricing remains unsettled.

**Key takeaways**

* The accrual anomaly looks less anomalous using the Penman–Zhu intertemporal asset-pricing framework, but later evidence suggests the effect has weakened or disappeared in some settings, so the result is not definitive.
* PEAD still looks more like mispricing in the Penman–Zhu framework because the model leaves significant alpha, although PEAD’s magnitude has diminished over time.
* Momentum, revenue-surprise drift, and analyst-forecast drift behave more like PEAD than accruals in this analysis.
* The benchmark matters: a one-period model can sometimes make priced multiperiod risk appear as mispricing.

**Conclusion**

Penman and Zhu argue that two famous accounting-based return patterns do not have the same economic source. In their model, accruals are consistent with priced multiperiod risk once investor horizons and hedging demands are considered, while PEAD still leaves residual alpha and therefore looks more like mispricing within that framework. At the same time, the broader literature – including evidence that PEAD has largely disappeared in many segments of the market and mixed evidence on accrual persistence – suggests these anomalies are dynamic, and that the ultimate interpretation depends on sample period, market structure, and the pricing model used.

*Larry Swedroe is the author or co-author of 18 books on investing, including his latest*[*Enrich Your Future*](https://protect.checkpoint.com/v2/r01/___https:/www.amazon.com/Enrich-Your-Future-Successful-Investing/dp/1394245440/___.YXAzOnNhcmFncmlsbG86Yzpnb29nbGVfbWFpbF9hdHRhY2htZW50OmUwZjJmZThlZDQ2MjYyOWQ4YmFmNDQwYWU5MzA2YTQxOjc6NGZjNDphYWFhM2JkNTFkMjZmN2RlYjhkZDRmMzY0Y2I0YTgyOTE1MWEzYmYzNjU2NTQwYzA2MDJiYjZlYmE2OTdlMDFkOnA6VDpO)*. He is also a consultant to RIAs as an educator on investment strategies. For informational and educational purposes only and should not be construed as specific investment, accounting, legal, or tax advice.*
