---
title: "Factor Investors Beware: Positive SMB May Not Mean You Own Small-Caps"
slug: "factor-investors-beware-positive-smb-may-not-mean-you-own-small-caps"
date: "2017-11-10"
modified: "2022-04-29"
url: "https://alphaarchitect.com/factor-investors-beware-positive-smb-may-not-mean-you-own-small-caps/"
categories: ["Research Insights", "Factor Investing", "Size Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Factor Investors Beware: Positive SMB May Not Mean You Own Small-Caps

> Regression analysis is used all the time to assess how a portfolio “loads” on certain factors. The most common factor loadings examined are the market, […]

Regression analysis is used all the time to assess how a portfolio “loads” on certain factors. The most common factor loadings examined are the market, size, value, and momentum factors. This can be an informative exercise, and there are nice tools online, such as [portfolio visualizer](https://www.portfoliovisualizer.com/), which allow investors to examine factor loadings on funds. *Note: We have an article (with an excel file), explaining factor regressions found [here](https://alphaarchitect.com/2011/08/01/how-to-use-the-fama-french-model/) if you are interested in getting your hands dirty.*

Sometimes we should take a step back and ask–what does this “small-cap factor” beta mean?(1)

Without getting into the math, a positive Beta means that a fund/portfolio has a positive correlation with a specific factor. Most long-only equity funds have a market beta ~ 1, reflecting the fact they are long the market factor. However, many investors focus their attention on factor regressions and examine a particular fund’s loading on the size, value, and momentum factors. In this context, a positive SMB (size) loading should imply that the fund has a small-cap tilt. The same goes for HML (Value) and UMD/MOM (Momentum).

But what does a positive factor loading really mean?

Intuitively, funds that have positive loadings on various factors should have underlying characteristics that match the factor loadings. E.g., you have a positive SMB factor loading, you should actually own small caps. (see the factors versus characteristics [debate here](https://alphaarchitect.com/2017/10/31/focus-on-portfolio-characteristics-not-factors/)).

For example, IWN has a .82 SMB beta estimate on PortfolioVisualizer.com and VB has a .57 SMB beta estimate. So IWN has more small-cap factor exposure than VB. But what does it actually mean? Is IWN 44% more small-cap (.82/.57 -1) ? Unclear.

A more intuitive approach is to just look at the actual market cap distributions. See below (a chart from our free [visual active share tool](/tools)).

[![](https://alphaarchitect.com/wp-content/uploads/2017/11/small-cap-visual.png)](https://alphaarchitect.com/wp-content/uploads/2017/11/small-cap-visual.png)

The chart above highlights explicitly how these funds are structured with respect to market-cap. No guessing games or weird interpretations via factor analysis.

But I digress. Let’s look at a paper that formally examines the challenges of interpreting small-cap “factor loadings.”

Below, we examine the results from a paper titled, “What Does ![\beta_{SMB}](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-c49a84d9bca1aeb5ca3cc1a0c3e6ad06_l3.png "Rendered by QuickLaTeX.com")>0 Really Mean?” by Hsiu-Lang Chen and Gilbert W. Bassett. A link to the paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2658380).

We dig into their findings below.

## Core Finding: Virtually All Portfolios Will Have Positive SMB

The authors first examine the sample size, or “N,” in the data. The SMB (Small minus Big) portfolio is formally [constructed](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_factors.html) as follows:

> SMB = 1/3 (Small Value + Small Neutral + Small Growth) – 1/3 (Large Value + Large Neutral + Large Growth)

The reason for splitting the universe into Value (i.e., cheap), Neutral, and Growth (i.e., expensive) is an attempt to minimize the Value factor (HML) that may be embedded in the SMB factor, by adding and subtracting Value, Neutral, and Growth portfolios. To split firms into S (Small) and B (Big), Fama and French in their 1993 [paper](https://faculty.fuqua.duke.edu/~charvey/Teaching/IntesaBci_2001/FF_Common_risk.pdf), used the median NYSE market capitalization for size–the 50th percentile of market cap for NYSE firms. However, using the NYSE median is not necessarily the median for all firms in the CRSP database — NYSE stocks are a lot bigger!

The authors highlight how using an NYSE market cap cut affects results over time:

[![](https://alphaarchitect.com/wp-content/uploads/2017/11/a-positive-smb-loading-1.png)](https://alphaarchitect.com/wp-content/uploads/2017/11/a-positive-smb-loading-1.png)

Source: What Does B\_SMB > 0 Really Mean? by Chen and Bassett. Accessed 11/8/17 from https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=2658380

The top image plots the number of firms in the B (Big) portfolio in Blue and the S (Small) portfolio in pink. One notices that in the second half of the sample, after AMEX and NASDAQ stocks have been added to CRSP, there are more Small (S) stocks than Big (B) stocks. However, when examining these firms from a market-capitalization perspective (and not the number of firms), we see that the Small (S) portfolio only makes up around 8% of the total market capitalization of all stocks!

So given that everyone now knows how the portfolios are formed (there are more Small stocks, but they make up a smaller percentage of market cap), the authors next form long-only portfolios, by going long x% in Big (B) and (100 – x)% in Small (S). They then examine the 3-factor (MKT, SMB, HML) loadings of these various portfolios. Table 2 (below) shows three-factor attribution for portfolios based on different combinations of Small (S) and Big (B).

[![What Does ßSMB0 Really Mean](https://alphaarchitect.com/wp-content/uploads/2015/09/What-Does-ßSMB0-Really-Mean.png)](https://alphaarchitect.com/wp-content/uploads/2015/09/What-Does-ßSMB0-Really-Mean.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The portfolio highlighted in red is “**80%BIG, 20%SMALL**“, which consists of 80% BIG (B) and 20% SMALL (S). This portfolio is obviously tilted toward **large-cap stocks**. However, the three-factor attribution still gives a **positive** and significant SMB coefficient (0.13)! In addition, except when S=0%, the SMB coefficients for all the reference portfolios remain **positive.**Even a 90% Big and 10% Small portfolio has a small (but positive) SMB loading.

So while a positive SMB means that the portfolio is tilting toward small-cap stocks, one needs to understand what this loading really means.(2)

(3)

Figure 1 above highlights that ~92% of the market-cap is made up by the Big (B) portfolio. Table 2 highlights the -0.07 loading on the 100% Big portfolio, and the 0.93 loading on the 100% Small portfolio. The estimated cutoff for a portfolio to have a positive SMB loading simply requires the portfolio to have a 7% or higher weight on the Small portfolio, which is close to the 92% of the market-cap weight in Figure 1.(4)

So (on average) any portfolio with a small allocation (above 7%) to smaller stocks, can generate a positive SMB loading!(5)

We like this paper since it calls attention to the *interpretation* of factor attribution and the importance of characteristics-based portfolio analysis.

Factor analysis is insightful, but far from perfect and can be hard to interpret (more discussion on characteristics vs. factors is [here)](https://alphaarchitect.com/2017/10/31/focus-on-portfolio-characteristics-not-factors/).

---

# What Does \beta_{SMB}>0 Really Mean?

* Chen and Bassett
* A version of the paper can be found [here](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2658380).
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category](https://alphaarchitect.com/category/academic-research/).

### Abstract:

> A positive SMB coefficient in a Fama-French regression is often interpreted as signaling a portfolio weighted toward small-cap stocks. We present a portfolio with known very large size, which has a positive SMB coefficient for all periods. We emphasize that this is associated with the co-existence of both “M” ― the market ― and “SMB” ― the mimicking portfolio for size ― in the Fama-French three-factor model. We explain why the model can attribute small size to large-cap stocks and portfolios. The results highlight how coefficients should be interpreted when a self-financing portfolio is used for portfolio attribution.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | Formally, Beta is a regression coefficient, here is a [link](https://en.wikipedia.org/wiki/Simple_linear_regression) explaining simple linear regressions, and [here is a post](https://alphaarchitect.com/2014/12/19/a-quick-lesson-in-volatility-measures/) that teaches you how to calculate beta in excel. |
| ↑2 | Fama and French (1993 and 1996) show that *only the largest* quintile size portfolio has a negative factor loading on SMB. |
| ↑3 | The authors cite the example of a 2011 paper by Elton et al., which states, “When we examine the small-minus-big factor, we see that the average beta is 0.1628, demonstrating a general tendency for funds to hold small stocks. However, over 25% of our funds have a negative beta with the size factor, which indicates that they are overweight large stocks.” |
| ↑4 | Also mathematically shown in the paper |
| ↑5 | There are other ways to have a positive SMB loadings as well |

 function footnote\_expand\_reference\_container\_20910\_64() { jQuery('#footnote\_references\_container\_20910\_64').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_20910\_64').text('−'); } function footnote\_collapse\_reference\_container\_20910\_64() { jQuery('#footnote\_references\_container\_20910\_64').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_20910\_64').text('+'); } function footnote\_expand\_collapse\_reference\_container\_20910\_64() { if (jQuery('#footnote\_references\_container\_20910\_64').is(':hidden')) { footnote\_expand\_reference\_container\_20910\_64(); } else { footnote\_collapse\_reference\_container\_20910\_64(); } } function footnote\_moveToReference\_20910\_64(p\_str\_TargetID) { footnote\_expand\_reference\_container\_20910\_64(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_20910\_64(p\_str\_TargetID) { footnote\_expand\_reference\_container\_20910\_64(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
