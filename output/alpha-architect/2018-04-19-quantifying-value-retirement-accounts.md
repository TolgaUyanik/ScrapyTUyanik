---
title: "Quantifying the Value of Retirement Accounts"
slug: "quantifying-value-retirement-accounts"
date: "2018-04-19"
modified: "2018-04-19"
url: "https://alphaarchitect.com/quantifying-value-retirement-accounts/"
categories: ["Guest Posts", "Tactical Asset Allocation Research", "Tax Efficient Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Quantifying the Value of Retirement Accounts

> Many people talk about the tax benefits of retirement accounts. However, few attempt to quantify and estimate the actual benefits. To make matters worse, when […]

Many people talk about the tax benefits of retirement accounts. However, few attempt to quantify and estimate the actual benefits.

To make matters worse, when the topic *is* addressed, many of the discussions rely on flawed logic and do not properly measure the true benefit.

For example, I often hear investors (even investment and tax professionals) summarize the core benefit as being due to “tax deferral.” In my view, however, deferring taxes is not the primary benefit of using retirement accounts. Moreover, deferral can actually work out to the detriment of investors, since overall tax rates can increase and investors can move into higher tax brackets by the time they must pay their taxes.(1)

This article highlights what I believe to be the real golden goose behind retirement accounts. In particular, there is immense value in not having to pay taxes on investment income and rebalancing (i.e., dividends, interest, and capital gains).(2) I attempt to quantify this benefit for a variety of portfolio strategies and tax brackets via historical simulations.(3)

**Spoiler:** While the results are dependent on market performance and each investor’s tax bracket, my calculations indicate the tax benefits of retirement accounts range between 0.7% and 2.7% per year.(4)

## Overview

If one uses Google to search for the phrases “tax benefits of retirement accounts,” or “value of tax deferral,” the results are mixed.(5) Among the varied topics in the search results, you will find much sponsored and marketing content, many irrelevant discussions, and plenty of financial jargon. At best I found some relevant but generic discussions with anecdotal examples. However, this was buried among articles with flawed logic and outright false claims (some from sources I thought reputable).

I cannot rule out the possibility that my Google search skills may just need improvement. However, I knew what I was looking for and still could not find it succinctly presented – let alone anything outlining a sensible general framework for decisions around funding retirement accounts. This was my motivation for writing this article.

My goal here is to provide a simple framework investors, as well as investment (or even tax) professionals, can leverage in order to make sensible decisions around funding retirement accounts. In particular, I quantify and estimate the relative value of dollars used to fund retirement accounts versus those invested without the tax benefits.

It is worth noting that retirement accounts have other advantages and disadvantages. For example, assets within retirement accounts are generally better-protected from creditors than if they were held outside retirement accounts. However, there are also liquidity constraints and early withdrawal penalties. I do not address these or other issues here for several reasons. For example, they are only occasionally relevant and are difficult to quantify.  However, the overriding factor is that I would like to keep my framework as simple as possible by focusing on what I find to be the most valuable benefit (which I refer to as the real golden goose).

This article has four sections and a short conclusion. The first section discusses the deceptive nature of the term *tax deferral* when used in the context of retirement account benefits. The second section highlights what I believe drives the real value of using retirement accounts – the ability to avoid paying taxes on investment income, rebalancing, and growth. I then quantify this benefit via historical simulations in the third section. There are a number of variables that affect the results (tax rates, portfolio strategies, etc.). So I provide results across multiple scenarios. The fourth section discusses the relevance of the results and highlights practical examples where investors and related professionals can leverage these results to make better financial planning decisions.

## Tax Benefits versus Tax Deferral

There is some confusion surrounding the tax benefits of retirement accounts. I suspect some of this is due to them being described as tax *deferral* benefits. I regularly hear investors and tax professionals use this description and you can find many instances of this around the internet and other media. Some highlight the benefit of reducing current income, and hence taxes, when making contributions to a retirement account. Some point out the likelihood of paying *more* taxes down the road when using retirement accounts (since the investments will appreciate and they will pay taxes on more income when it is taken out).

These two views are opposite sides of the same coin. In this context, funding a retirement account can be viewed as a choice between paying fewer taxes now or more taxes later. The link that ties them together is the *time value of money*. For example, one could contribute to their IRA to reduce their current (income) tax bill and then invest those tax savings. In this case, they should have more money to pay the higher tax bill down the road.

If we assume we can invest at the same rate of return within or outside of a retirement account, then the economic decision to fund a retirement account or not hinges on whether one’s income tax rate will be higher or lower when the money is taken out. If they are the same, then the math works out identically and it makes no difference; you will end up with the same amount of money whether you contribute or not (see Figure 1).

**Figure 1: To Fund or Not to Fund a Retirement Account**

![](/wp-content/uploads/2018/04/Fig1.png)

Source: Aaron Brask Capital

If overall tax rates rise or the investor climbs into a higher tax bracket, then it is possible for the deferral to work against them. Of course, tax rates and future tax brackets could work to the benefit of the investor as well. These details should be considered in order to better measure the benefit or detriment of tax *deferral*. Notwithstanding, there is still one appreciable detail I have left out. Above I relied on the assumption that we can invest at the same rate of return inside or outside of retirement accounts. However, that is definitely not the case. The next two sections should make this abundantly clear.

## The Real Golden Goose of Retirement Accounts

In the example scenario highlighted in Figure 1, there are two details (aside from the tax rates) that make a significant difference between the dollar amounts at the end of the period. First, the dollar invested outside the IRA embeds unrealized capital gains at the end of the period. In order to spend that money, the investor will have to pay capital gains taxes.(6) Second, it is unrealistic to assume one could achieve the same returns outside of an IRA versus within. If nothing else, the dividend and interest payments would trigger taxes. Moreover, rebalancing a portfolio could also result in capital gains taxes during the investment period.

This highlights what I believe to be the most important benefit of retirement accounts: the ability to avoid paying taxes on the dividends, interest, and capitals gains while they reside within a retirement account. At current prices, the dividend yield of the overall US stock market is a little over 1.5% and the 10-year treasury yield is just under 3%. If an investor pays 15% tax on dividends and an income tax of 25%, then a typical 60/40 portfolio would currently pay about 44 basis points in tax per year on the investment income.

Of course, yields on stocks and bonds are near historic lows right now. Thus the tax impact on this investment income is much lower now than it has been in the past. Moreover, this does not include any additional taxes incurred from rebalancing the portfolio to maintain the 60/40 weightings, nor liquidating the portfolio in cases where the money is to be spent. The next section describes the historical simulation I built to make these calculations and displays the results across a variety of scenarios (portfolio mixes, tax rates, glide paths, etc).

Pièce De Résistance(7)

### Some Assumptions

I use rolling 20-year periods between 1968 and 2018. So this analysis is based on 30 sample periods – many of which are overlapping. I simulate portfolios with buy and hold, fixed asset allocation, as well as glide path strategies.(8) Rebalancing is implemented annually. I use the S&P 500 benchmark for equity allocations and the performance of 10-year Treasury bond for the fixed income allocations.

I use conservative assumptions regarding the tax consequences of rebalancing and capital gains distributions.(9) I assume optimal tax lot selling when rebalancing (i.e., highest basis holdings sold first). I also assume the benchmarks generate no capital gains distributions (we can thank the [tax efficiency of exchange-traded funds](http://alphaarchitdev.wpengine.com/2014/04/01/why-etfs-are-more-tax-efficient-than-mutual-funds/) for this feature).

Lastly, I assume dividends and interest payments are received at the end of each year. Of course, this does not precisely reflect reality. However, it should not alter the results significantly. The assumption is made for both the taxed and untaxed portfolios (retirement account) and we are primarily interested in the *relative* results.

### The Results

The results I present are based on historical simulations of portfolio performance. My goal is to quantify the tax benefits of the retirement accounts. So I express these benefits as the difference between the *annualized* total returns of the portfolios held within and outside of retirement accounts.(10)

I calculate results for both liquidated and non-liquidated scenarios. The liquidated portfolio scenario is relevant to situations where investors end up spending the money (capital gains will apply to the realized gains for portfolios outside of retirement accounts). The non-liquidated portfolio scenario would be relevant to cases where the investor does not need to access the money. For example, it could remain invested until being inherited or donated to a charity and benefit from a step-up basis – hence avoiding capital gains on the unrealized gains.

I run the simulations across three dimensions: strategy type, risk level, and tax rates. As mentioned above, there are three types of strategies: buy and hold, fixed asset allocation, and glide paths.

For each strategy, I observe four different risk levels by varying the stock and bond allocations (80/20, 60/40, 40/60, and 20/80). Within each of these risk levels, I analyze the impact of both moderate and high tax brackets.(11)

Here are some of the key findings:

* For *liquidated* portfolios, the benefit ranged from 1.1% to 2.7% and averaged 1.7% across all scenarios.
* For *non-liquidated* portfolios, the benefit ranged from 0.7% to 2.7% and averaged 1.5% across all scenarios.
* Strategy trends
  + Buy and hold strategies with no rebalancing benefited the least with an average differential of 1.5% – presumably due to less tax friction from rebalancing.
  + Fixed asset allocation strategies were in the middle with an average differential of 1.6%.
  + Glide path strategies benefited the most with an average differential of 1.8% – presumably due to increased rebalancing (higher equity growth versus falling equity allocations).
* Lower risk (i.e., stock) allocations benefited the most with an average differential of 2.0% for 20/80 portfolios versus 1.2% for 80/20 portfolios. Delving deeper into the tax benefits reveals the income tax on the bond coupons drove this trend.
* The obvious trends across tax rates materialized (i.e., higher tax brackets benefit more). The average differential for the moderate tax bracket was 1.3% versus 1.9% for the high tax bracket.

I suspect there are many investors pursuing a 60/40 fixed asset allocation approach that falls within the moderate tax bracket I used here. In this particular scenario (see Figure 7 below), the tax benefit of retirement accounts averaged 1.3% for liquidated portfolios and 1.1% for non-liquidated portfolios.

There are, of course, many ways to slice and dice these results.

Below are several bar charts that make comparisons across different dimensions. However, I have also provided tables containing all of the results for those interested in other comparisons.

**Figure 2: Average Benefit across Strategies**

![](/wp-content/uploads/2018/04/Fig2.png)

Source: Aaron Brask Capital

**Figure 3: Average Benefit across Risk (stock/bond %)**

![](/wp-content/uploads/2018/04/Fig3.png)

Source: Aaron Brask Capital

**Figure 4: Average Benefit for High vs Low Tax Bracket**

![](/wp-content/uploads/2018/04/Fig4.png)

Source: Aaron Brask Capital

**Figure 5: Average Benefit for Liquidated vs Non-Liq.**

![](/wp-content/uploads/2018/04/Fig5.png)

Source: Aaron Brask Capital

**Figure 6: Buy and Hold Strategies**

![](/wp-content/uploads/2018/04/Fig8.png)

Source: Aaron Brask Capital

**Figure 7: Fixed Asset Allocation Strategies**

![](/wp-content/uploads/2018/04/Fig6.png)

Source: Aaron Brask Capital

**Figure 8: Glide Path Strategies**

![](/wp-content/uploads/2018/04/Fig7.png)

Source: Aaron Brask Capital

## Some Applications

The above analysis provides a means of quantifying the tax benefits of retirement accounts. These results can be considered in various aspects of financial planning, but I believe the most important takeaway is for investors to establish and maximize contributions to retirement accounts such as IRAs, 401Ks, etc. More generally, investors should try to maximize the longevity of these tax benefits where possible since the benefit compounds with time.

For starters, a good rule of thumb is to spend money outside of your non-retirement accounts first so the tax benefits can accrue longer. However, Roth-type accounts should also be considered (whether via contribution or conversion). This could extend the tax advantages by avoiding required minimum distributions. Moreover, leaving IRAs to younger heirs (e.g., children or grandchildren) with longer expected life spans can extend the longevity of these benefits even further. Of course, investors considering such strategies should weigh the impact of what income tax rates will apply.

Another topic related to the tax benefits of retirement accounts is *asset* *location*. In particular, once an asset *allocation* is prescribed, it is sensible to consider which assets should be placed within the retirement accounts versus outside. While this is an important consideration and should be integrated into the financial planning process, it is beyond the scope of this article. Indeed, asset location is a rich topic and depends on a variety of factors (e.g., types of accounts, tax efficiency of assets, expected returns, time horizon, whether funds are likely to be spent during one’s lifetime or not, etc.).

The notion of tax benefits is also relevant to *annuities*. Indeed, financial professionals selling these products often highlight their tax advantages. The results I quantified above can help evaluate the cost/benefit of these tax advantages. It is worth noting the earnings accrued within annuities are taxed as income when the funds are removed. So the deferral benefit will likely be offset by the higher taxation of those earnings as income (relative to capital gains if they were incurred outside a retirement account). In my experience, the fees of annuity products (especially variable annuities) often outweigh their tax benefits. As a result, I believe investors interested in annuities should be specifically interested in the products’ non-tax-related benefits (e.g., asset protection or other riders) in order to justify their costs. However, I generally find it is possible to construct more cost-efficient solutions. I provide a more detailed discussion of these concepts [here](http://www.aaronbraskcapital.com/research/income-generation-101-retirees/).

The last application I mention here relates to *net unrealized appreciation* (NUA) transactions. Without going into the details, employees who own significantly appreciated stock in their company retirement plans have two options; they can take the stock out of their retirement plan and place it in a brokerage account or roll it into an IRA. There are advantages and disadvantages related to both options, but weighing the tax benefits of the IRA is naturally a relevant consideration.

Maximizing the utility of retirement accounts involves many other variables I have not discussed here – potential need for early withdrawals, desire for asset protection, potential changes in laws regarding tax treatment, etc. Moreover, many of these factors should be addressed in a holistic fashion to optimize each investor’s particular situation. I hope that by quantifying some of tax benefits of retirement accounts above, investors and other professionals will be able to leverage these results to improve their financial planning.

# Conclusions

The tax benefits of retirements accounts range between 0.7% and 2.7% per year. However, the results vary across the different dimensions I considered and there are other variables to consider. Suffice to say, benefits on this order of magnitude can translate into tremendous value for investors. Thus it is wise to contribute to and maximize these retirement account benefits where possible.

This conclusion is both unsurprising and already well-known. However, I could not find any studies or research that quantified these benefits. So I hope my results can be helpful to others involved in financial planning where the value of these tax benefits is relevant and can impact decisions around their strategies.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | I don’t mention it here, but there is also the possibility that rules are retroactively changed. For example, investors with large retirement accounts might be told that there are tax penalties for amounts over some amount (e.g., $3mm). |
| ↑2 | Technically, these investment-related taxes are not deferred; they are simply not paid. However, in the case of an IRA the accumulated benefit of not paying these taxes may result in paying higher income taxes if/when the money is eventually taken out of the retirement account. |
| ↑3 | **Disclaimer:** I am not a tax professional. This article is not and should not be construed as tax advice. Investors should seek advice from a CPA or qualified tax professional for any questions or issues related to taxes**.** |
| ↑4 | Wes and his team find something similar, albeit via different assumptions/framework [here](http://alphaarchitdev.wpengine.com/2011/07/09/taxes-are-more-important-than-alpha/). |
| ↑5 | **Note:** Unless otherwise stated, the retirement accounts discussed in this article are assumed to be individual retirement accounts (IRAs). |
| ↑6 | Capital gains taxes on the investment growth may not apply in cases where the investments are passed on to heirs or charities where they would typically benefit from a *step-up* basis. I provide results for both scenarios. |
| ↑7 | **Disclaimer:** This analysis is neither exhaustive nor precise. The following results are essentially the result of a mathematical exercise which relies on several simplifying assumptions. |
| ↑8 | Glide paths systematically reduce equity allocations by 1% per year. |
| ↑9 | To be fair, tax harvesting could potentially mitigate, if not eliminate, many capital gains taxes. However, the resulting portfolio would generally have a lower basis and trigger higher capitals gains when it is ultimately sold. |
| ↑10 | I compare the same portfolios inside and outside retirement accounts. However, an investor could employ an asset location strategy. That is, one could maintain the same overall asset allocation while allocating differently within versus outside retirement accounts. This diminishes the value of my results to some extent since the comparison assumes the same asset allocations in both the retirement and taxable portfolios. However, academic and practitioner white papers (Michael Kitces and Betterment highlight estimates [here](https://www.kitces.com/blog/asset-location-the-new-wealth-management-value-add-for-optimal-portfolio-design/) and [here](https://www.betterment.com/resources/introducing-tax-coordinated-portfolio/)) seem to indicate the average asset location benefit is between 20 and 50 basis points. So the magnitude of my results below are still very relevant. |
| ↑11 | I assumed 15% (20%) dividend and long-term capital gains and 25% (39.6%) income tax rates for the moderate (high) tax bracket. |

 function footnote\_expand\_reference\_container\_36545\_97() { jQuery('#footnote\_references\_container\_36545\_97').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_36545\_97').text('−'); } function footnote\_collapse\_reference\_container\_36545\_97() { jQuery('#footnote\_references\_container\_36545\_97').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_36545\_97').text('+'); } function footnote\_expand\_collapse\_reference\_container\_36545\_97() { if (jQuery('#footnote\_references\_container\_36545\_97').is(':hidden')) { footnote\_expand\_reference\_container\_36545\_97(); } else { footnote\_collapse\_reference\_container\_36545\_97(); } } function footnote\_moveToReference\_36545\_97(p\_str\_TargetID) { footnote\_expand\_reference\_container\_36545\_97(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_36545\_97(p\_str\_TargetID) { footnote\_expand\_reference\_container\_36545\_97(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
