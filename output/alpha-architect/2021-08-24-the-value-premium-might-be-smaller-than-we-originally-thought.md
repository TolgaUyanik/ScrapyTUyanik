---
title: "The Value Premium Might be Smaller Than We Originally Thought"
slug: "the-value-premium-might-be-smaller-than-we-originally-thought"
date: "2021-08-24"
modified: "2022-05-23"
url: "https://alphaarchitect.com/the-value-premium-might-be-smaller-than-we-originally-thought/"
categories: ["Research Insights", "Factor Investing", "Basilico and Johnsen", "Academic Research Insight", "Value Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# The Value Premium Might be Smaller Than We Originally Thought

> Is the Value Premium Smaller Than We Thought? Mathias Hasler SSRN Working Paper A version of this paper can be found here Want to read our […]

## **Is the Value Premium Smaller Than We Thought?**

* Mathias Hasler
* SSRN Working Paper
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3886984)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

Remember HML? It was the original formulation for estimating the “value” premium published by [Fama & French](https://alphaarchitect.com/2011/08/01/how-to-use-the-fama-french-model/) in 1992.  In that seminal article, FF argued based on the results they obtained, that the risk of owning equity is multidimensional.  One of those dimensions of risk they used was financial distress proxied by the BE/ME ratio(1), which itself was originally based on the distress factor utilized by Chan and Chen (1991). At the time, Chan and Chen argued that the market signals its judgment about a stock’s price according to its earnings prospects on a relative basis.  That is, stocks judged to have poor prospects will signal with lower (distressed) stock prices and higher book-to-market ratios when compared to stocks judged to have strong earnings prospects.

A rational and powerful explanation for the higher returns tied to “cheap” stocks.

In the article summarized here, the authors contemplate 6 of the decisions implicit in the construction of the original HML factor:  the timing of market equity; the timing of book equity; negative book equity; financial firms; portfolio sorting breakpoints; the timing of market equity to account for the size effect. All of which sum to an average decision in the original HML formulation that may contain a randomly determined bias.

So, reasonable alternatives are proposed, not all that dissimilar to the portfolio decisions used in the [Quantitative Value](https://alphaarchitect.com/2014/10/07/the-quantitative-value-investing-philosophy/) approach. The authors created 6 alternative decisions and used those new methods to construct new HML portfolios (96 to be specific), and the return performance of all possible HML portfolios are averaged.  Under this design, the alternative HML portfolios can be viewed as alternative proxies for the value factor and the return obtained from the alternatives an unbiased average of the value factor premium suitable for comparison to the FF original value premium.

1. What are the alternative decisions used to construct new HML portfolios?
2. Is there a significant difference in the return to value when calculated using the average of the alternative formulations vs. the original?
3. Is the difference due to risk?
4. Does the average return to the alternative HML portfolios reflect more than one dimension?
5. Were the results the same during out-of-sample periods?

## What are the Academic Insights?

1. Alternative Decisions:
   * **When book value of equity is measured**:  *Original* HML: used the book equity of a firm’s last fiscal year with fiscal year-end before the end of December of year t-1 to sort stocks into value and growth portfolios from July of year t to June of year t+1; *Alternative* HML:  used the book equity of a firm’s last fiscal year six months after its fiscal year-end. Both specifications impose a minimum gap of six months for accounting information to become publicly available in order to address reporting issues.
   * **When market value of equity is measured:** *Original* HML: used market equity at the end of December of year t-1. Specifically, market equity at the end of December of year t-1 is used in the denominator of book-to-market equity to sort stocks into value and growth portfolios from July of year t to June of year t+1. *Alternative* HML: used market equity from the most recent month and skip one month in order to avoid the negative first-order serial correlation in monthly stock returns. (See AQR’s “[HML Devil](https://alphaarchitect.com/2015/03/19/how-rebalancing-frequency-affects-quality-and-value-investing-funds/)” discussion here)
   * **How stocks with negative book value of equity are treated**:  *Original* HML portfolio excluded stocks with negative book equity observations. *Alternative* HML: such stocks are included, as negative book value of equity can occur naturally and legally under US GAAP.
   * **How financial stocks are treated:** *Origina*l HML: included financial firms. *Alternative* HML, financial firms are excluded. The magnitude of leverage for financial firms is not likely to indicate distress as it does for nonfinancials.
   * **What breakpoints are used to sort stocks into value, neutral, and growth portfolios**: *Original* HML: used the 30th and 70th percentiles of book-to-market equity of all stocks trading on the NYSE as breakpoints. *Alternative* HML: used the 20th and 80th percentiles and the 40th and 60th percentiles of book-to-market equity of all stocks trading on the NYSE as breakpoints.
   * **When the timing of market equity is set in order to account for the size effect**:  *Original* HML: used market equity at the end of June of year t.  *Alternative* HML:  used market equity at the end of December of year t-1.
  
2. YES. Replication of the Original FF 1992 study produced a monthly return of 0.35%, while the Alternative HML produced: 0.27% per month.  The difference of 0.09% indicates that the original formulation of the FF HML value premium is upwardly biased.
  
3. NO. A comparison of the  standard deviations of the Original (2.57%) and Alternative ( 2.76%) HML monthly portfolio returns indicates there is little evidence that the extra return to the Original HML portfolio is due to additional risk.
  
4. NO. The authors report that the results of a principal components analysis of the monthly returns of the Alternative HML portfolios suggest there is only one underlying factor or dimension. Ninety-one percent of the variation of the Alternative HML portfolio returns was explained by the first principal component.
  
5. PRETTY MUCH. Similar results were found in tests conducted in the out-of-sample period from January 1992 to December 2019, although the bias was slightly less positive.

## Why does it matter?

The analysis presented in this paper was informative as to the magnitude of variability in factor returns that have not been reported regarding the returns to Value to date ([here is another bear case](https://alphaarchitect.com/2019/06/25/large-cap-price-to-book-investing-what-is-dead-may-never-die/) for b/m value, at least in mega-caps). In this case, the focus was on the decisions made in formulating a factor measurement and implementing the test of the newly formulated factor. In addition to the natural variability observed in factor returns when the formulation is held constant, we find that reasonable alternative formulations of factors introduce uncertainty or dispersion in estimates reported that could be significant. In this case, a difference of 8 bps or 9 bps on a monthly basis amounts to quite a bit over long periods of time.

Of course, we expect differences in results when the components of the empirical design are varied on purpose. Although the authors examine 6 differences in design and do report very consistent results (see Table II below), I would caution the reader to refrain from using this research effort as a justification for data mining the “best” formulation.

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2021/08/2021-08-10-13_55_43-SmallPremium_Value_SSRN_fromWes.pdf-and-1-more-page-Personal-Microsoft​-Edge-1200x1293.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> The construction of the original HML portfolio (Fama and French, 1993) includes six seemingly innocuous decisions that could easily have been replaced with alternatives that are just as reasonable. I propose such alternatives and construct HML portfolios. In sample, the average estimate of the value premium is dramatically smaller than the original estimate of the value premium. The difference is 0.09% per month and statistically significant. Out of sample, however, this difference is statistically indistinguishable from zero. The results suggest that the original value premium estimate is upward biased because of a chance result in the original research decisions.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | book value of equity (BE) and market value of equity (ME) |

 function footnote\_expand\_reference\_container\_64206\_99() { jQuery('#footnote\_references\_container\_64206\_99').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_64206\_99').text('−'); } function footnote\_collapse\_reference\_container\_64206\_99() { jQuery('#footnote\_references\_container\_64206\_99').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_64206\_99').text('+'); } function footnote\_expand\_collapse\_reference\_container\_64206\_99() { if (jQuery('#footnote\_references\_container\_64206\_99').is(':hidden')) { footnote\_expand\_reference\_container\_64206\_99(); } else { footnote\_collapse\_reference\_container\_64206\_99(); } } function footnote\_moveToReference\_64206\_99(p\_str\_TargetID) { footnote\_expand\_reference\_container\_64206\_99(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_64206\_99(p\_str\_TargetID) { footnote\_expand\_reference\_container\_64206\_99(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
