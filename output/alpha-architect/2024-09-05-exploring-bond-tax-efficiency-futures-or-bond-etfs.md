---
title: "Exploring Bond Tax Efficiency: Futures or Bond ETFs?"
slug: "exploring-bond-tax-efficiency-futures-or-bond-etfs"
date: "2024-09-05"
modified: "2024-09-03"
url: "https://alphaarchitect.com/exploring-bond-tax-efficiency-futures-or-bond-etfs/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Exploring Bond Tax Efficiency: Futures or Bond ETFs?

> Bond futures are often assumed to be more tax-efficient than bond ETFs. My analysis indicates that this assumption is frequently incorrect. Although investors might view the 60/40 tax treatment of futures as advantageous, a futures strategy faces several challenges compared to a bond ETF, including frequent taxable events, potential tax drag from cash collateral, and additional state taxation. My analysis suggests that, between July 2002 and July 2024, the bond ETF wins under a variety of realistic assumptions. However, bond futures may be compelling for high-tax investors, especially if they can find a tax-efficient cash solution. There is no universally “tax-efficient” instrument between bond futures and bond ETFs; rather, tax efficiency is defined by the investor’s particular circumstances.

# Executive Summary

* Bond futures are often assumed to be more tax-efficient than bond ETFs. My analysis indicates that this assumption is frequently incorrect.
* Although investors might view the 60/40 tax treatment of futures as advantageous, a futures strategy faces several challenges compared to a bond ETF, including frequent taxable events, potential tax drag from cash collateral, and additional state taxation.
* My analysis suggests that, between July 2002 and July 2024, the bond ETF wins under a variety of realistic assumptions. However, bond futures may be compelling for high-tax investors, especially if they can find a tax-efficient cash solution.
* There is no universally “tax-efficient” instrument between bond futures and bond ETFs; rather, tax efficiency is defined by the investor’s particular circumstances.

# Introduction

When are Treasury bond futures advantageous to a bond ETF? Investors might assume that bond futures are advantageous for a given underlying bond exposure due to their Section 1256 tax treatment, which applies a 60% long-term and 40% short-term capital gains tax rate to marked-to-market gains. Since income is typically taxed at a higher rate than long-term capital gains, investors who expect high bond coupons may favor bond futures. However, the taxation on bond futures includes state and local taxes, from which Treasury income is exempt. Additionally, bond ETFs allow for the deferral of capital gains, a benefit that is not available with the mark-to-market treatment of bond futures. Ultimately, whether the bond futures have a tax advantage is an empirical question.

This analysis shows that the answer is complex. Tax efficiency depends not only on the realized split between the underlying bonds’ price and interest returns but also on the after-tax return on cash-like instruments and investor-specific tax situations. **When interest income is the predominant component of total returns and the cash collateral can be invested in a tax-efficient manner, investors in a high tax bracket may be better off using bond futures. However, investors in high-tax states who plan to defer capital gains for significant periods may be better off in a bond ETF.**

Although some prior research has explored this question, significant practical gaps remain. First, the literature is sparse, and there is value in updating the returns to a more recent history. Second, the taxes paid on the cash-like instruments matter, but have been previously ignored. Third, I have not seen a piece that integrates the consideration of state taxes – from which the Treasury bond ETF is exempt – for the bond futures. Finally, I quantify the benefit of potential capital gains deferral on the bond ETF compared to the mark-to-market treatment on the futures.

## Bond and Bond Futures Overview

I assume the target bond exposure is the 7-10 year Treasury, which is gained through the IEF bond ETF.

Bond futures return is the excess return on bonds (i.e. the total return on bonds net of the T-bill rate). (See this [post by Corey Hoffstein](https://www.linkedin.com/posts/coreyhoffstein_one-question-i-receive-all-the-time-is-activity-7188170313287839745-3kTZ?utm_source=share&utm_medium=member_desktop) for a good intuitive explanation of this). For simplicity, I assume that the excess returns of the ETF and the bond futures are identical. [Previous research](https://alphaarchitect.com/2015/04/tax-efficient-investing-how-should-we-invest-in-treasury-bonds/) on this blog has indicated that this is a reasonable assumption. It is worth noting that coupon return is embedded in the futures return and that futures provide an excess return. To calculate the total return, the return of the cash component (e.g. T-bills) must be included.

In short, the comparable exposures are:

* $1M of Treasury bonds or bond ETFs
* 8 contracts of bond futures, offering exposure of ~$125,000 each, plus $950k held in interest-earning cash instruments, such as T-bills. The remaining $50k of cash is assumed to be a 5% margin requirement that does not earn interest.

While bond futures allow for leverage, I abstract from that here. I also simplify by assuming the expense ratio on the bond ETFs and our hypothetical bond futures strategy are the same. I abstract from the fact that bond futures do not trade fractionally. In practice, there could be some rounding in the futures exposures due to the large increments in which they trade.

## Overview of Tax Treatment: Bond ETF and Bond Futures

There are two components of return in the bond ETF: price return and income return. Price return is taxed as capital gains upon the sale of the ETF. In contrast, the interest income generated by the underlying bonds is typically paid out monthly to investors and is taxable at ordinary income tax rates in the year it was earned. While both components of return are federally taxable, interest income stemming from Treasury bonds (including exposure gained via the ETF) is generally exempt from state taxes. Bonds are volatile instruments, so the overall return – and portion of return coming from capital gains – is unknowable, although historically, income returns have been larger than price returns.

Bond futures are subject to Section 1256 taxation, meaning they are marked-to-market at 60% long-term and 40% short-term capital gains tax rates. Moreover, the bond futures position typically requires cash collateral, which may itself earn interest. Of note, the Section 1256 gains are subject to both federal and state taxes.

It is not immediately clear which instrument is more tax-efficient. The table below summarizes the high-level considerations that were just discussed. Moreover, I abstract from the other considerations that may drive investors to the bond futures instrument, such as its ability to be used to gain embedded portfolio leverage.

|  |  |  |
| --- | --- | --- |
|  | **Treasury ETFs** | **Treasury Futures** |
| What are the instrument’s returns? | Total bond returns, with coupon income distributed and treated as ordinary income | Excess-of-cash bond returns, inclusive of price and coupon return. (Return on cash collateral is included as a separate line item in this analysis). |
| Tax treatment: Capital gains | Subject to federal, state, and local taxes | Subject to federal, state, and local taxes |
| Tax treatment: Interest income | Subject to federal taxes | Subject to federal, state, and local taxes |
| When are taxes owed? | Upon sale of position (and potential for step-up in basis) | Marked-to-market each year |
| Tax optionality | Yes – ETF disposition timing is up to the investor | No – mark-to-market each year |
| Carryback losses | None | Section 1256 contracts allow for a carryback of losses across the previous 3 years. Conditions apply, see the [IRS guidelines](https://www.irs.gov/pub/irs-access/f6781_accessible.pdf) |
| Other considerations | Expense ratios should be considered | Expense ratios should be considered; May be used to gain leverage in the broader portfolio |

Now, let’s turn to the data.

# One-Year Investment Example

Consider an investment made for the calendar year 2017. IEF was purchased on the last trading day of 2016 and held until the last trading day of 2017. (For simplicity, I consider this eligible for long-term capital gains). This piece asserts that marginal income and capital gains rates are a central factor in after-tax returns, so I begin with a typical investor’s approximate marginal rates and run sensitivity analysis assuming higher marginal rates. For the typical investor, I assume a capital gains rate of 15.0% and marginal income tax rate of 22.0%, which maps to a married filing jointly couple with taxable income between $89,451 and $190,750 as of the 2023 tax year. I assume that the return on the bond futures is identical to the return on the bond ETF, including identical expense ratios. The table below shows the breakdown of the return.

|  |  |
| --- | --- |
|  | **Calendar year 2017** |
| Price return | 0.72% |
| Income return | 1.84% |
| **Total return** | **2.56%** |
| Risk-free return | 0.93% |
| **Excess return** | **1.63%** |

I then evaluate the net return assuming a $1M initial cash investment, with positions liquidated and taxes paid at the end of the period. The bond ETF’s taxes are fairly straightforward: a 15.0% capital gains tax rate is applied to the $7,200 of price returns ($1,080 of tax) and a 22.0% income tax rate is applied to the $18,400 of income return ($4,048 of tax), resulting in $5,128 of taxes on $25,600 of gains. The end wealth is $1,020,472.

The bond futures case is more complex. I assume the exposure of bond futures is identical ($1M) to that of the bond ETF, i.e. there is no embedded leverage. The bond futures exposure receives the *excess* return that is assumed to be equal to the bond ETF’s return net of the T-bill return. This excess return of $16,300 is taxed at 60% long-term ($9,780) and 40% short-term ($6,520) per the Section 1256 tax treatment. Additionally, the bond futures strategy is assumed to use 5% of its value as margin, with the remaining 95% of its initial investment invested in T-bills. The T-bill return is $8,835 and is also taxed at income tax rates. On net, the strategy pays $4,845 of taxes on $25,135 of gains, resulting in an end wealth of $1,020,290.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Bond ETF |  | Bond futures |
| Initial investment | $1,000,000 | Initial investment | $1,000,000 |
| Price return | $7,200 | LT excess return | $9,780 |
| Income return | $18,400 | ST excess return | $6,520 |
|  |  | T-bill return | $8,835 |
| **Total gains** | **$25,600** | **Total gains** | **$25,135** |
| Capital gains taxes owed | $1,080 | Capital gains taxes owed | $1,467 |
| Income taxes owed | $4,048 | Income taxes owed | $3,378 |
| **Total taxes** | **$5,128** | **Total taxes** | **$4,845** |
| Effective tax rate on investment | 20.0% | Effective tax rate on investment | 19.3% |
| Net return | $20,472 | Net return | $20,290 |
| **End wealth** | **$1,020,472** | **End wealth** | **$1,020,290** |

The results are nearly identical. The bond futures strategy yields $182 less wealth, just two basis points of the portfolio value, but still a loss for the supposedly “tax efficient” instrument.   This is driven by lower total gains of the bond futures – $465 lower than the bond ETF – resulting from the non-interest-bearing margin. While the bond futures has more advantageous taxation in terms of its split between long-term and short-term capital gains, it is not quite enough to overcome the loss in return due to the non-interest-bearing margin.

There are at least key three assumptions in the above analysis that can affect the trade-off. First, the bond ETF could be bequeathed and subject to a step-up in cost basis, while the futures’ mark-to-market treatment forces taxes to be paid. Second, state taxes would disproportionately affect the bond futures: its entire gain would be subject to state tax, whereas the Treasury ETF interest income is exempt. Finally, the tradeoff could look different for an investor in a higher tax bracket.

For the same example, let’s examine how varying these assumptions affects the differences in end wealth, shown in the below table. For the higher tax rates, I assume a 23.8% capital gains and 40.8% marginal income tax rates, which currently maps to the highest federal brackets.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Tax rate: Long-term capital gains | Tax rate: Ordinary income | Bond ETF | Bond futures | Bond futures wins by … |
| Original scenario | 15.0% | 22.0% | $1,020,472 | $1,020,290 | -$182 |
| Original scenario + step-up in ETF | 15.0% | 22.0% | $1,021,552 | $1,020,290 | -$1,262 |
| Original scenario + 5% state tax | 15.0% | 22.0% | $1,020,112 | $1,019,033 | -$1,079 |
| Higher tax rates | 23.8% | 40.8% | $1,016,379 | $1,016,543 | +$163 |
| Higher tax rates  + step-up in ETF | 23.8% | 40.8% | $1,018,093 | $1,016,543 | -$1,550 |
| Higher tax rates + 5% state tax | 23.8% | 40.8% | $1,016,019 | $1,015,286 | -$733 |

The first row shows our initial exercise, with the bond futures losing in end wealth by $182. As expected, the bond futures is more attractive at higher federal tax rates, winning by $163. However, with either a step-up in the cost basis of the ETF or a 5% state tax, the bond futures strategy becomes disadvantageous. The scenarios above show that the choice between bond futures and ETFs depends on the investor’s tax situation and bequest motives.

It’s worth noting that all of these magnitudes are quite small relative to the initial investment (ranging up to ~16 basis points). The benefit’s size will vary with market returns, and this example has relatively low overall returns (2.56%). With higher returns, and over a long horizon with deferral and compounding considerations, these effects will be larger.

The comparison above does not consider one of the bond ETF’s core benefits, namely tax deferral. Investors can choose when to realize gains, and have no such option when using futures contracts. The net result is that the futures’ favorable tax treatment needs to compensate for regular taxable events, which under the assumptions above, it does not.

I examine the full sample in the next section, integrating these tax deferral considerations.

# Multi-year Analysis

I now use historical data to show how the bond ETF would have performed relative to a bond futures exposure between July 30, 2002 and July 30, 2024. I assume an investor starts with $1,000,000 of cash at the beginning of our sample. The investor pays federal income taxes on the ETF’s distributed interest income. I assume there is no spending during the period so that the investor enjoys either a step-up in basis (pre-liquidation wealth) or tax deferral (post-liquidation wealth) on the bond ETF’s price appreciation. I assume that the bond futures has identical excess returns to the bond ETF and holds 95% of the initial investment in T-bills, with the other 5% dedicated to non-interest-bearing cash margin. The bond futures is marked-to-market and pays taxes at the end of each year out of the portfolio. For the bond futures, I treat capital losses similarly to capital gains: capital losses are used to offset gains with like-character, and those tax savings are immediately reinvested in the portfolio. Note that this treatment is in the spirit of the carryback provision, but is a more generous estimate of the potential tax benefit of the bond futures: the carryback could result in deferred tax savings (here, it’s assumed to occur in the same year), as well as reduced savings if short-term losses offset long-term gains (here, it’s assumed to be same-character).

I consider three hypothetical investors with the taxes shown in the below table. NIIT is included when appropriate. In practice, state taxes are highly varied. The 5% example included roughly reflects the consideration for a Massachusetts taxpayer. For simplicity, I assume that these tax rates are static over this period. While tax rates and brackets have changed over time, I do not believe this should change the directional result. Moreover, investors making investment decisions today typically use today’s rates as a best estimate for future rates, unless policymakers issue guidance that strongly suggests otherwise.

|  |  |  |  |
| --- | --- | --- | --- |
|  | Lower tax investor | Higher tax investor | Higher tax investor with state taxes |
| Capital gains tax rate | 15.0% | 23.8% | 23.8% |
| Marginal income tax rate | 22.0% | 40.8% | 40.8% |
| State tax (on both capital gains and income) | 0% | 0% | 5% |

![](https://alphaarchitect.com/wp-content/uploads/2024/08/tlh-bonds.png)

The results from the full sample analysis are summarized in the bar chart above. Over our sample period, the bond futures does not win under any circumstance. The bond ETF would have resulted in higher end wealth over the historical period, with our example producing differences of up to $80,000 (~5% of the portfolio’s end value). The difference is especially stark for investors with a bequest motive.

The bond futures strategy mentioned here faces at least two significant disadvantages. First, the bond ETF grows tax-deferred, while the bond futures pays taxes each year. This is a feature of the Section 1256 contract and comes with the territory of using futures. Second, the cash collateral on the bond futures creates a drag since it produces taxable interest income each year. The next section investigates whether addressing the T-bill drag can make the futures more attractive for the taxable investor.

## Layering on a Tax-Efficient Cash-Equivalent Exposure

The previous analysis assumed that the cash collateral on the bond futures strategy was invested in T-bills. While T-bills are often touted as tax-efficient given their exemption from state and local taxes, they also create some tax drag from their interest income, which results in income taxes owed each year. Is there a better way?

Assume instead that the investor could use a tax-efficient cash management strategy (“TECMS” hereafter) that replicates the T-bill exposure but solves the tax drag: i.e. it is taxed as capital gains and enables tax deferral like an ETF. (For instance, this could be a box spread designed to mimic T-bill returns, but packaged inside an ETF). I assume that the TECMS has a 20 basis point expense ratio but otherwise has identical returns to the T-bill. I assume that the TECMS is held throughout the historical period and either has a step-up in basis (pre-liquidation) or is liquidated at the end of the period (post-liquidation).

![](https://alphaarchitect.com/wp-content/uploads/2024/08/tlh-bonds-2.png)

![](https://alphaarchitect.com/wp-content/uploads/2024/08/tlh-bonds-3.png)

The results are shown in the above charts. The use of the TECMS makes the bond futures appealing for the investor with a bequest motive. For higher tax investors with no state considerations, the benefit is highest, at $110k – a meaningful difference relative to the ~$700k in portfolio growth over the period. TECMS allows the investor with the bequest motive to enjoy a step-up in cost basis at the end of the period, turning tax deferral into tax savings, which is reflected in the magnitude of the benefit.

For an investor aiming to liquidate and spend his portfolio, the results are mixed. Bond futures wins for a higher tax investor without state tax considerations. For this investor, the ability to pay capital gains taxes on some portion of the bond exposure’s excess returns, in addition to the cash-like component, proves beneficial. However, investors with lower taxes are better off in the bond ETF: the cost of the managed futures exposure (from the opportunity cost of the margin and the assumed TECMS expense) outweighs the benefits that it provides. Finally, investors subject to a 5% state tax have nearly identical end wealth from each strategy: the bond futures exposure has lower net returns since all of its gains are subject to state tax, while the bond ETF’s income distributions are exempt from state tax.

# Discussion

When are bond futures more tax-efficient than their ETF counterparts? This analysis has demonstrated that the answer is not straightforward. Implementation matters substantially: what the bond futures investor does with his cash can meaningfully change the results. The intent of the portfolio also matters: the results depend on whether the portfolio is intended for consumption or bequest.

|  |  |  |  |
| --- | --- | --- | --- |
| Using T-Bills | | | |
|  | Low-tax investor | High-tax investor | |
| Low-tax state | High-tax state |
| Bequest | ETF | ETF | ETF |
| Consumption | ETF | ETF | ETF |
| Using Tax-Efficient Cash Management Strategy (TECMS) | | | |
|  | Low-tax investor | High-tax investor | |
| Low-tax state | High-tax state |
| Bequest | Bond futures | Bond futures | Bond futures |
| Consumption | ETF | Bond futures | Tied |

The table above summarizes the directional results from this analysis. When using TECMS, higher-tax investors with no (or low) state taxes may find the bond futures to be advantageous. The bond ETF might win in other circumstances: when using T-bills in the futures strategy, or when considering lower-tax investors in the TECMS version of the futures strategy.

Other considerations may drive the ultimate decision between bond futures and bond ETFs. For instance, bond futures allow an investor to use embedded leverage at competitive borrowing rates, which may be attractive. Moreover, for an investor holding a multi-asset class portfolio, the bond ETF may be forced to realize capital gains during rebalancing, which would diminish the attractiveness of potential capital gains deferral.

All said, there is no universally “tax-efficient” choice between bond futures and bond ETFs; rather, tax efficiency is defined by the investor’s particular circumstances and the strategy’s implementation details.
