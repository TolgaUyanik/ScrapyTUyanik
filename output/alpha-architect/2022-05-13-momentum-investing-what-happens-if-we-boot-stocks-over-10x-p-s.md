---
title: "Momentum Investing: What happens if we boot stocks over 10x P/S?"
slug: "momentum-investing-what-happens-if-we-boot-stocks-over-10x-p-s"
date: "2022-05-13"
modified: "2022-12-22"
url: "https://alphaarchitect.com/momentum-investing-what-happens-if-we-boot-stocks-over-10x-p-s/"
categories: ["Research Insights", "Factor Investing", "Momentum Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Momentum Investing: What happens if we boot stocks over 10x P/S?

> This was a simple question posed to me by one of our blog readers–what impact does excluding stocks trading at 10x P/S have on a Momentum portfolio? A good question–especially for those who are “value” investors that are interested in momentum. For most systematic value investors, the prospect of adding stocks trading at over 10x P/S sounds ludicrous. Since I didn’t know the exact impact, I went and ran the tests described below.

Short answer up front–very little.(1)

This was a simple question posed to me by one of our blog readers–what impact does excluding stocks trading at 10x P/S have on a Momentum portfolio?

A good question–especially for those who are “value” investors that are interested in momentum. For most systematic value investors, the prospect of adding stocks trading at over 10x P/S sounds ludicrous–see this [article](https://alphaarchitect.com/2019/05/buying-stocks-trading-above-10x-sales-a-good-idea/) on the performance of stocks trading over 10x P/S.

Since I didn’t know the exact impact, I went and ran the tests described below.

## Data

The universe is the largest 1,500 common stocks in the U.S. Data is from FactSet. The data runs from 1/1/1992 through 12/31/2021. Momentum portfolios are constructed every quarter (12/31, 3/31, 6/30, 9/30) by selecting the top quintile (300 firms) using a 12\_2 Momentum calculation (the prior 12-months’ total return ignoring the last month). Returns are shown to equal-weight (EW) portfolios.

Within this top quintile of momentum stocks, I then bifurcate the sample into the following:

1. Above 10x P/S
2. Below 10x P/S

The image below shows the number of firms in each bucket.

![](https://alphaarchitect.com/wp-content/uploads/2022/05/Mom.10x.Price_.to_.Sales_.1.png)

As we can see, there are two time periods when the momentum portfolio has a decent amount of firms trading above 10x P/S (100 firms or more):

1. Post internet bubble–1/1/2000-12/31/2000
2. Post COVID–7/31/2020-6/30/2021

However, the majority of the time the momentum portfolio is under 50 stocks (out of 300) that trade above 10x P/S. The average number of firms within the momentum sample trading above 10x P/S is 44 firms (44 out of 300 = 14.67%).

So what happens if we include/exclude these firms from the momentum portfolios?

## Results

To test the impact, we examine the returns of 3 momentum portfolios, and compare them to the market:

1. US MOM– ALL FIRMS EW: Top quintile of momentum firms (300). Portfolio is equal-weighted.
2. US MOM–EX-FIRMS > 10X P/S EW: Firms within the top quintile on momentum that are trading ***below*** 10x P/S. Portfolio is equal-weighted.
3. US MOM–FIRMS > 10X P/S EW: Firms within the top quintile on momentum that are trading ***above*** 10x P/S. Portfolio is equal-weighted.
4. SP500 INDEX: S&P 500 Index

All returns shown below are gross of any transaction fees and management fees.

![](https://alphaarchitect.com/wp-content/uploads/2022/05/Mom.10x.Price_.to_.Sales_.2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index. Please see a list of descriptions and a list of disclosures [here.](https://alphaarchitect.com/indexes/disclosures/#disclosures)

The results above highlight a few things:

1. Comparing columns 1 and 2, we get the answer to the main question I was posed. Excluding momentum firms trading at 10x P/S has a marginal impact over the long-run (1/1/1992-12/31/2021). There is only a 6 bps a year difference over the entire time period.
2. Comparing columns 1 and 3, we see that building a momentum portfolio solely on stocks trading above 10x P/S is a bad idea ([not surprising](https://alphaarchitect.com/2019/05/buying-stocks-trading-above-10x-sales-a-good-idea/)). One would lose ~ 3.5% annually compared to the simple momentum portfolio.

So is excluding stocks trading above 10x P/S a horrible idea?

No.

There are time periods when there is a pretty large divergence in returns between the naïve momentum portfolio and the momentum portfolio excluding stocks above 10x P/S.

Below are the annual returns, with a few years highlighted:

![](https://alphaarchitect.com/wp-content/uploads/2022/05/Mom.10x.Price_.to_.Sales_.3.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index. Please see a list of descriptions and a list of disclosures [here.](https://alphaarchitect.com/indexes/disclosures/#disclosures)

The annual returns above show that in the internet bubble and the post-COVID there were some pretty large divergences between the 3 momentum portfolios.

## Summary

Overall, we see that excluding firms trading above 10x P/S has a minimal impact over the entire time sample (6 bps difference from 1992 to 2021). However, if one wanted to build a momentum portfolio and exclude these firms, it didn’t historically hurt performance. However, as many know, momentum requires a lot of turnover (see [here](https://alphaarchitect.com/2015/11/how-portfolio-construction-affects-momentum-funds/)), which can cause tax issues if not done within an IRA or another tax-efficient wrapper (such as within an ETF).

References[+]

References

|  |  |
| --- | --- |
| ↑1 | Of course, results may vary based on how many stocks one puts in the portfolio. |

 function footnote\_expand\_reference\_container\_75194\_44() { jQuery('#footnote\_references\_container\_75194\_44').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_75194\_44').text('−'); } function footnote\_collapse\_reference\_container\_75194\_44() { jQuery('#footnote\_references\_container\_75194\_44').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_75194\_44').text('+'); } function footnote\_expand\_collapse\_reference\_container\_75194\_44() { if (jQuery('#footnote\_references\_container\_75194\_44').is(':hidden')) { footnote\_expand\_reference\_container\_75194\_44(); } else { footnote\_collapse\_reference\_container\_75194\_44(); } } function footnote\_moveToReference\_75194\_44(p\_str\_TargetID) { footnote\_expand\_reference\_container\_75194\_44(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_75194\_44(p\_str\_TargetID) { footnote\_expand\_reference\_container\_75194\_44(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
