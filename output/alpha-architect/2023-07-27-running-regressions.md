---
title: "Regression is a tool that can turn you into a fool"
slug: "running-regressions"
date: "2023-07-27"
modified: "2023-07-27"
url: "https://alphaarchitect.com/running-regressions/"
categories: ["Empirical Methods", "Research Insights", "Factor Investing", "Value Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Regression is a tool that can turn you into a fool

> Running regressions on past returns is a great tool for academic researchers who understand this approach’s nuance, assumptions, pitfalls, and limitations. However, when factor regressions become part of a sales effort and/or are put in the hands of investors/advisors/DIYers, “the tool can quickly turn you into a fool.”

Running regressions on past returns is a great tool for academic researchers who understand this approach’s nuance, assumptions, pitfalls, and limitations. However, when factor regressions become part of a sales effort and/or are put in the hands of investors/advisors/DIYers, “the tool can quickly turn you into a fool.”

![](https://alphaarchitect.com/wp-content/uploads/2023/07/alpha.png)

Don’t get me wrong, running regressions on return series is useful for investors and academic researchers. Still, it is far from a panacea and is only one tool in the investor’s toolkit for understanding and conducting due diligence on a potential investment.

Jack has a [great post](https://alphaarchitect.com/2018/06/factor-regressions-problems-and-how-to-fix-them/) digging into the weeds of factor regressions and highlighting some of the tool’s limitations. And if you want a deep dive into how to run factor regressions, we have an old post that explains how to calculate Fama-French 3-factor alpha.(1) We also have a piece about the fragility of ‘factor’ models and their ability to cause brain damage and confusion. See, “[Factor Investing is more art than science.](https://alphaarchitect.com/2017/02/factor-models-are-more-art-and-less-science/)“

To highlight why one should be skeptical of regression analysis and ascribe too much value to the results, we produce a simple analysis of the QQQ ETF. The QQQ index underlies the ETF and is about as far from being based on a factor-based strategy tied to, “financial science produced by noble prize winners,” as you can get. My lay understanding is Nasdaq created the index to showcase the listings on their exchange and attract issuers to join their exchange. There is no research behind the process, and the official criteria on the Index make this transparent:(2)

* Being listed exclusively on Nasdaq in either the Global Select or Global Market tiers.
* Being publicly offered on an established American market for at least three months.
* Having average daily volume of 200,000 shares.
* Being current in regards to quarterly and annual reports.
* Not being in bankruptcy proceedings.
* …or getting out of RIC tax compliance and [changing randomly](https://www.cnbc.com/2023/07/11/nasdaq-100-to-undergo-rejiggering-because-a-few-tech-stocks-are-now-too-big.html)

Because QQQ is essentially a basket of stocks listed on the Nasdaq with no factor or “alpha” intention, it makes for an interesting example to highlight the limitations of analysis paralysis via regression.

## QQQ has a ton of alpha, according to regression analysis

Here is a summary of the alpha estimates from portfoliovisualizer.com, using various models over the full-time period of QQQ (April 1999 to June 2023).

* [5 Factor Fama French: 5.09% alpha, 3.2 t-stat.](https://www.portfoliovisualizer.com/factor-analysis?s=y&regressionType=1&regressionMethod=1&symbols=QQQ&factorDataSet=-1&marketArea=0&factorModel=0&useHMLDevFactor=false&includeQualityFactor=false&includeLowBetaFactor=false&fixedIncomeFactorModel=0&ffmkt=true&__checkbox_ffmkt=__checkbox_true&__checkbox_ffsmb=__checkbox_true&ffsmb5=true&__checkbox_ffsmb5=__checkbox_true&ffhml=true&__checkbox_ffhml=__checkbox_true&__checkbox_ffmom=__checkbox_true&ffrmw=true&__checkbox_ffrmw=__checkbox_true&ffcma=true&__checkbox_ffcma=__checkbox_true&__checkbox_ffstrev=__checkbox_true&__checkbox_ffltrev=__checkbox_true&__checkbox_aqrmkt=__checkbox_true&__checkbox_aqrsmb=__checkbox_true&__checkbox_aqrhml=__checkbox_true&__checkbox_aqrhmldev=__checkbox_true&__checkbox_aqrmom=__checkbox_true&__checkbox_aqrqmj=__checkbox_true&__checkbox_aqrbab=__checkbox_true&__checkbox_aamkt=__checkbox_true&__checkbox_aasmb=__checkbox_true&__checkbox_aahml=__checkbox_true&__checkbox_aamom=__checkbox_true&__checkbox_aaqmj=__checkbox_true&__checkbox_qmkt=__checkbox_true&__checkbox_qme=__checkbox_true&__checkbox_qia=__checkbox_true&__checkbox_qroe=__checkbox_true&__checkbox_qeg=__checkbox_true&__checkbox_trm=__checkbox_true&__checkbox_cdt=__checkbox_true&timePeriod=2&rollPeriod=60&marketAssetType=1&robustRegression=true)
* [AQR 6 factor model: 6.10% alpha 3.972 t-stat.](https://www.portfoliovisualizer.com/factor-analysis?s=y&regressionType=1&regressionMethod=1&symbols=QQQ&factorDataSet=-1&marketArea=0&factorModel=0&useHMLDevFactor=false&includeQualityFactor=false&includeLowBetaFactor=false&fixedIncomeFactorModel=0&__checkbox_ffmkt=__checkbox_true&__checkbox_ffsmb=__checkbox_true&__checkbox_ffsmb5=__checkbox_true&__checkbox_ffhml=__checkbox_true&__checkbox_ffmom=__checkbox_true&__checkbox_ffrmw=__checkbox_true&__checkbox_ffcma=__checkbox_true&__checkbox_ffstrev=__checkbox_true&__checkbox_ffltrev=__checkbox_true&aqrmkt=true&__checkbox_aqrmkt=__checkbox_true&aqrsmb=true&__checkbox_aqrsmb=__checkbox_true&__checkbox_aqrhml=__checkbox_true&aqrhmldev=true&__checkbox_aqrhmldev=__checkbox_true&aqrmom=true&__checkbox_aqrmom=__checkbox_true&aqrqmj=true&__checkbox_aqrqmj=__checkbox_true&aqrbab=true&__checkbox_aqrbab=__checkbox_true&__checkbox_aamkt=__checkbox_true&__checkbox_aasmb=__checkbox_true&__checkbox_aahml=__checkbox_true&__checkbox_aamom=__checkbox_true&__checkbox_aaqmj=__checkbox_true&__checkbox_qmkt=__checkbox_true&__checkbox_qme=__checkbox_true&__checkbox_qia=__checkbox_true&__checkbox_qroe=__checkbox_true&__checkbox_qeg=__checkbox_true&__checkbox_trm=__checkbox_true&__checkbox_cdt=__checkbox_true&timePeriod=2&rollPeriod=60&marketAssetType=1&robustRegression=true)
* [AA 5 factor model: 6.05% alpha 3.918 t-stat.](https://www.portfoliovisualizer.com/factor-analysis?s=y&regressionType=1&regressionMethod=1&symbols=QQQ&factorDataSet=-1&marketArea=0&factorModel=0&useHMLDevFactor=false&includeQualityFactor=false&includeLowBetaFactor=false&fixedIncomeFactorModel=0&__checkbox_ffmkt=__checkbox_true&__checkbox_ffsmb=__checkbox_true&__checkbox_ffsmb5=__checkbox_true&__checkbox_ffhml=__checkbox_true&__checkbox_ffmom=__checkbox_true&__checkbox_ffrmw=__checkbox_true&__checkbox_ffcma=__checkbox_true&__checkbox_ffstrev=__checkbox_true&__checkbox_ffltrev=__checkbox_true&__checkbox_aqrmkt=__checkbox_true&__checkbox_aqrsmb=__checkbox_true&__checkbox_aqrhml=__checkbox_true&__checkbox_aqrhmldev=__checkbox_true&__checkbox_aqrmom=__checkbox_true&__checkbox_aqrqmj=__checkbox_true&__checkbox_aqrbab=__checkbox_true&aamkt=true&__checkbox_aamkt=__checkbox_true&aasmb=true&__checkbox_aasmb=__checkbox_true&aahml=true&__checkbox_aahml=__checkbox_true&aamom=true&__checkbox_aamom=__checkbox_true&aaqmj=true&__checkbox_aaqmj=__checkbox_true&__checkbox_qmkt=__checkbox_true&__checkbox_qme=__checkbox_true&__checkbox_qia=__checkbox_true&__checkbox_qroe=__checkbox_true&__checkbox_qeg=__checkbox_true&__checkbox_trm=__checkbox_true&__checkbox_cdt=__checkbox_true&timePeriod=2&rollPeriod=60&marketAssetType=1&robustRegression=true)
* [5 factor q-factor model: 3.89% alpha 1.843 t-stat.](https://www.portfoliovisualizer.com/factor-analysis?s=y&regressionType=1&regressionMethod=1&symbols=QQQ&factorDataSet=-1&marketArea=0&factorModel=0&useHMLDevFactor=false&includeQualityFactor=false&includeLowBetaFactor=false&fixedIncomeFactorModel=0&__checkbox_ffmkt=__checkbox_true&__checkbox_ffsmb=__checkbox_true&__checkbox_ffsmb5=__checkbox_true&__checkbox_ffhml=__checkbox_true&__checkbox_ffmom=__checkbox_true&__checkbox_ffrmw=__checkbox_true&__checkbox_ffcma=__checkbox_true&__checkbox_ffstrev=__checkbox_true&__checkbox_ffltrev=__checkbox_true&__checkbox_aqrmkt=__checkbox_true&__checkbox_aqrsmb=__checkbox_true&__checkbox_aqrhml=__checkbox_true&__checkbox_aqrhmldev=__checkbox_true&__checkbox_aqrmom=__checkbox_true&__checkbox_aqrqmj=__checkbox_true&__checkbox_aqrbab=__checkbox_true&__checkbox_aamkt=__checkbox_true&__checkbox_aasmb=__checkbox_true&__checkbox_aahml=__checkbox_true&__checkbox_aamom=__checkbox_true&__checkbox_aaqmj=__checkbox_true&qmkt=true&__checkbox_qmkt=__checkbox_true&qme=true&__checkbox_qme=__checkbox_true&qia=true&__checkbox_qia=__checkbox_true&qroe=true&__checkbox_qroe=__checkbox_true&qeg=true&__checkbox_qeg=__checkbox_true&__checkbox_trm=__checkbox_true&__checkbox_cdt=__checkbox_true&timePeriod=2&rollPeriod=60&marketAssetType=1&robustRegression=true)

These long-term regression statistics are eye-popping. And if I had no insight into the underlying process or concept, and simply had to go on regression, if I saw alpha results/t-stats like this over a 20yr+ stretch, I might fall out of my chair. To summarize, if QQQ were relabeled the, “RenTech Platinum Growth Fund,” which is based on proprietary Nobel-Prize-winning quant research, it would likely be heralded as the greatest quant fund that ever existed.

Here are the current characteristics of the QQQ ETF vs. SPY:

![](https://alphaarchitect.com/wp-content/uploads/2023/07/available-strategies-11.png)

Summary: QQQ is SPY on steroids — a mega-cap, insanely expensive, high-quality index

Is QQQ an alpha-generating hedge fund in plain sight?

Is this the alpha you are after? Is this the alpha that will predict the future? Probably not. This analysis highlights that regression is not a panacea for identifying the underlying merits of a process.

Rant. Over.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | This post is older than the publication of the 5-factor Fama French model and the wonderful quant tool — portfoliovisualizer.com — even existed. |
| ↑2 | as per Wikipedia |

 function footnote\_expand\_reference\_container\_87119\_56() { jQuery('#footnote\_references\_container\_87119\_56').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_87119\_56').text('−'); } function footnote\_collapse\_reference\_container\_87119\_56() { jQuery('#footnote\_references\_container\_87119\_56').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_87119\_56').text('+'); } function footnote\_expand\_collapse\_reference\_container\_87119\_56() { if (jQuery('#footnote\_references\_container\_87119\_56').is(':hidden')) { footnote\_expand\_reference\_container\_87119\_56(); } else { footnote\_collapse\_reference\_container\_87119\_56(); } } function footnote\_moveToReference\_87119\_56(p\_str\_TargetID) { footnote\_expand\_reference\_container\_87119\_56(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_87119\_56(p\_str\_TargetID) { footnote\_expand\_reference\_container\_87119\_56(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
