---
title: "The Hidden Risks of Leveraged Single-Stock ETFs"
slug: "leveraged-single-stock-etfs"
date: "2026-01-02"
modified: "2026-01-02"
url: "https://alphaarchitect.com/leveraged-single-stock-etfs/"
categories: ["Transaction Costs", "Research Insights", "Larry Swedroe", "Other Insights", "ETF Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# The Hidden Risks of Leveraged Single-Stock ETFs

> Leveraged ETFs function precisely as designed—they deliver leveraged exposure to daily returns, not long-term performance. Problems emerge when investors misuse these instruments for purposes they weren’t built for, particularly buy-and-hold investing or long-term wealth accumulation.

Levered ETFs may appeal to those who wish to hedge other positions, those with strong directional views, or those with so-called “lottery preferences.” – Hendrik Bessembinder

**The Explosive Growth of a Risky Product**

Leveraged single-stock Exchange-Traded Funds (LSS-ETFs) have captured investors’ attention with a seductive promise: amplified exposure to popular stocks without the complexity of margin trading. The first levered single stock ETFs (LSS-ETFs) were introduced in July 2022. By late 2024 the market capitalization of LSS-ETFs had grown to more than $17 billion. And there has been a surge in LSS-ETFs rollouts during the first half of 2025, with a total of more than 100 such ETFs trading as of mid-2025. These products typically offer 2x or 3x daily leverage (or inverse exposure) to stocks like Tesla, Apple, or NVIDIA. Direxion, a leader in offering these products uses this advertisement on their website. But do they deliver what investors expect?

My July 16, 2025 Substack column examined the research on the [hidden costs](https://protect.checkpoint.com/v2/r01/___https:/larryswedroe.substack.com/p/the-hidden-risks-of-leveraged-and___.YXAzOnNhcmFncmlsbG86YzpnOjQwODUxNGU2YmU0NjhiMDJmOGRjMDBlZGUxNmNmYmZkOjc6OWMyZDoxZDM3NGY2OTQ0YTE2YzMxZWY2YTg3N2UzMGUwYWJiZTA0MDk4MzVhYjY3NzI2MWE5MThhYzQxY2M5MjQzODNlOnA6VDpO) of leveraged and inverse ETFS, demonstrating that these were products that were designed to be sold to investors, but investors should never buy them. Thanks to Hendrik Bessembinder, author of the August 2025 study, “[Leveraged Single-Stock ETFs](https://protect.checkpoint.com/v2/r01/___https:/papers.ssrn.com/sol3/papers.cfm?abstract_id=5369417___.YXAzOnNhcmFncmlsbG86YzpnOjQwODUxNGU2YmU0NjhiMDJmOGRjMDBlZGUxNmNmYmZkOjc6OTM4NzoyYWIxMTYzMTA2ODYwMTFiNGFlYzMzMjZjN2ExMDViY2E0MTkwMWY5ODhlYjY0NTlmZGZjZDAyYmZiZTkzMTE5OnA6VDpO),” we can also examine the hidden risks and costs of a related product, leveraged single stock ETFs.

Bessembinder compared levered single-stock ETF returns to the benchmark defined by target leverage times the stock return. His data sample of LSS-ETFs covered the period from fund inception through June 31, 2025. As evidence of their popularity, the sample grew from six funds with a combined market capitalization of just $6.4 million on the first date to 33 funds with a combined capitalization of $17.4 billion at the end June 2025.

The following is a summary of his findings:

* For the full sample of 19,456 fund/days, the average fund return was 0.05% compared to an average underlying stock return of 0.16%. For funds with positive leverage the average daily return was 0.22%. Funds with β = 2 leverage had a mean daily return of 0.27%, those with β =1.5 leverage had a mean daily return of 0.22%, but those with β =1.75 leverage had a mean daily return of -0.05%.
* Monthly returns to the LSS-ETFs in the sample underperformed the simple benchmark by an average of 0.88% per month, with 0.45% underperformance attributable to the effects of daily rebalancing and 0.43% attributable to frictions.
* Friction costs were larger for positive leverage (average of 0.53% per month) than for inverse leverage funds (average of 0.26% per month), while rebalancing costs were larger for negative (average of 0.73%) than for positive leverage (average of 0.27%) funds.
* Average friction costs are greater for funds that offer larger absolute exposures. For example, the average friction cost for funds with 𝛽 = 2 is 0.030% per day, compared to 0.019% per day for funds with 𝛽 = 1.5. The average friction cost for funds with 𝛽= -2 is 0.029% per day, compared to 0.010% per day for funds with 𝛽 = -1. Larger friction costs for funds with greater absolute leverage likely reflect the costs implicit in entering larger swap contracts.

![](https://alphaarchitect.com/wp-content/uploads/2025/12/Panel-A.png)

*The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

**The Daily Rebalancing Problem**

As discussed above, friction costs are a significant problem for LSS-ETFs.  Another issue results from the daily rebalancing mechanism. Leveraged ETFs reset their leverage ratio every day, creating a compounding effect that deviates significantly from simple leverage math over longer periods. This daily reset requirement means:

* **Volatility Decay**: When there is negative serial correlation of returns, higher volatility implies that rebalancing trades involve buying high and selling low, which erodes levered ETF returns. This was an important new finding: there is volatility decay only when there is negative serial correlation of returns.
* **Path Dependency**: The sequence of daily returns matters more than the overall return of the underlying stock.
* **Compounding Mismatch**: Monthly and longer-term returns diverge substantially from leveraged [benchmarks](https://protect.checkpoint.com/v2/r01/___https:/alphaarchitect.com/has-benchmarking-made-us-bad-investors/___.YXAzOnNhcmFncmlsbG86YzpnOjQwODUxNGU2YmU0NjhiMDJmOGRjMDBlZGUxNmNmYmZkOjc6OWRjZTpjZjEyMWFmN2Q1YTI4ZmU3ZDI3NGQ3OGJlMDI5MTNhOGZmNjUwMTlhNGJhMjU2OWJhMTNjOGU5ZTRlNTFhNjU0OnA6VDpO).

Bessembinder also exploited the fact that historical daily returns are available for thousands of common stocks over five decades to study the returns that LSS-ETFs would hypothetically have delivered if they had been available to investors in the past—allowing for a much larger sample. He considered hypothetical frictionless returns measured over horizons, including daily, weekly, monthly, six-month, and annual, for hypothetical ETFs with leverage multipliers, beta (β), equal to 3, 2, 1 (unlevered, for comparison) -1, and -2.

He found:

* Mean returns to hypothetical single-stock ETFs with positive leverage would have exceeded unlevered stock returns at all horizons considered, while mean returns to inverse or negative leverage ETFs would have been negative at all horizons.
* Frictionless monthly returns to hypothetical single-stock ETFs underperform the simple benchmark by an average of 0.28% with 3x leverage and by 0.49% with -2x leverage, attributable to the effects of daily rebalancing trades.
* Reflecting the strong skewness in levered fund returns, especially at longer horizons, more than half of hypothetical levered fund returns are less than the unlevered return to the value-weighted U.S. stock market, for all return measurement horizons and leverage multipliers considered.

Importantly, Bessembinder demonstrated that while the following has not yet occurred for any leveraged ETF launched since 2022, a levered ETF can imply a target daily return less than -100%. “For example, (ignoring the relatively minor effects of daily interest) a leverage ratio of three implies that the target ETF return is less than -100% if the stock return is less than -33 1/3%.” However, he showed that it would have occurred with Apple’s stock, for any leverage of 2 or greater, on September 29, 2000 when it fell 51.9%.

 Bessembinder noted:

> “Of course, a target return less than -100% does not imply a return less than -100% to an actual investor who enjoys limited liability. In the absence of a contractual provision or legal ruling that creates a claim on investors’ assets other than those used to purchase the levered ETF, investor returns cannot be less than -100%. The limited liability notion for levered ETFs may rely in part on “acceleration clauses” that allow the sponsor to “call in” the product if it suffers large losses. To avoid a target return less than -100% would require underlying stock and/or swap positions be unwound quickly, even potentially in the presence of trading halts or circuit breakers. To my knowledge the ability to place a floor such that target returns do not fall below -100% has not yet been tested by a case where the specified leverage times the underlying asset daily return for any ETF was less than -100%.”

**Key Investor Takeaways**

The critical insight is that, if you *ignore* the high friction costs Bessembinder identified, leveraged ETFs function precisely as designed—they deliver leveraged exposure to daily returns, not long-term performance. Problems emerge when investors misuse these instruments for purposes they weren’t built for, particularly buy-and-hold investing or long-term wealth accumulation. Consider how [Direxion](https://protect.checkpoint.com/v2/r01/___https:/www.direxion.com/single-stock-etfs___.YXAzOnNhcmFncmlsbG86YzpnOjQwODUxNGU2YmU0NjhiMDJmOGRjMDBlZGUxNmNmYmZkOjc6OTRjZDo2NDZmZjEzZjM1MTNmOTM3NjhjY2VlOTFlYTYxNjgzNjFiNTA2ZjM3Mjk2ODg3NjhkMmY4MTg4NWE0Y2U3MGQwOnA6VDpO), a leading provider of leveraged ETFs, describes their target market: “Now risk-hungry traders can get daily 2X bull or -1X bear exposure to heavily traded individual large cap stocks.” Notice the deliberate language—”risk-hungry traders” seeking “daily” exposure, not long-term investors building wealth. This framing should serve as a clear signal about the intended use (speculating, not investing) and audience for these complex financial instruments.

**Conclusion**

The analysis of US-based leveraged single-stock ETFs reveals a complex landscape where marketing promises don’t always align with real-world performance. While these products successfully achieve their daily objectives, their long-term performance can deviate significantly from investor expectations due to mathematical realities that result from daily rebalancing effects: compounding, volatility decay, and frictions (implementation costs).

The key insights from this research are clear: these products are not suitable for buy-and-hold strategies nor for investors who don’t fully understand their mechanics. The research serves as a crucial reminder that in investing complexity can come with hidden costs and unexpected risks.

The financial industry’s continued innovation in ETF products provides investors with more tools than ever before, but as this research demonstrates, understanding the true costs and behaviors of these tools is essential for making informed investment decisions.

*Larry Swedroe is the author or co-author of 18 books on investing, including his latest*[*Enrich Your Future*](https://protect.checkpoint.com/v2/r01/___https:/www.amazon.com/Enrich-Your-Future-Successful-Investing/dp/1394245440/___.YXAzOnNhcmFncmlsbG86YzpnOjQwODUxNGU2YmU0NjhiMDJmOGRjMDBlZGUxNmNmYmZkOjc6YzEzNDoyOGUwYTY5ZmVkNmY2YWMwYzliMjg0ZDQxZGQxNzJiZWU1NjIxZWUyNjJjYWZiZTQ0MzkwODUyOTgzZWZmZTY3OnA6VDpO)*. He is also a consultant to RIAs as an educator on investment strategies.*
