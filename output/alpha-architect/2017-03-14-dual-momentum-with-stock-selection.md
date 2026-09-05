---
title: "Dual Momentum with Stock Selection"
slug: "dual-momentum-with-stock-selection"
date: "2017-03-14"
modified: "2022-05-11"
url: "https://alphaarchitect.com/dual-momentum-with-stock-selection/"
categories: ["Research Insights", "Trend Following", "Momentum Investing Research", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Dual Momentum with Stock Selection

> Jack did a nice recap on a momentum paper last week that looks at using fundamentals (revenue volatility, low cost of goods, and B/M) to help identify the best price momentum stocks. This paper sounds similar to the paper Jack reviewed, but there is a key difference: the researchers are looking at the momentum of the fundamentals, not the absolute value of the fundamentals. The authors compile a fundamental momentum variable by calculating the moving averages of 7 elements: return on equity return on assets earnings per share accrual-based operating profitability cash-based operating profitability gross profitability net payout ratio

Gary Antonacci may not be happy to learn that his “Dual Momentum” label has been pirated by a team of academics (Huang, Zhang, and Zhou)(1)(2) in a new paper that explores the combination of price and fundamental momentum stock-picking strategies. The authors also investigate the common rebuttal that transaction costs destroy stock momentum strategies. The authors perform a variety of robustness tests and their results are strong and significant. The author’s describe their results best (regarding ***stock-selection*** momentum):

> Dual momentum is not attributable to transaction costs.

Can a stock-picking focused dual momentum approach dethrone the asset-level dual momentum approach outlined by our friend Mr. Antonacci?

[![dual momentum argument](https://alphaarchitect.com/wp-content/uploads/2017/03/dual-momentum-argument.png)](https://alphaarchitect.com/wp-content/uploads/2017/03/dual-momentum-argument.png)

Photo taken during a summit of Mt. Shingle in the Flattops wilderness of Colorado. Many quantitative finance arguments were discussed.

In this post we explore and explain the results from this new paper and encourage readers to read our summary and the underlying paper to make their own decisions.

Let’s dig in…

## Fundamentals Momentum and Price Momentum

Jack did a [nice recap](https://alphaarchitect.com/2017/03/08/firm-specific-information-and-momentum/) on a momentum paper last week that looks at using fundamentals (revenue volatility, low cost of goods, and B/M) to help identify the best price momentum stocks.

This paper sounds similar to the paper Jack reviewed, but there is a key difference: the researchers are looking at the momentum of the fundamentals, not the absolute value of the fundamentals. The authors compile a fundamental momentum variable by calculating the moving averages of 7 elements:

1. return on equity
2. return on assets
3. earnings per share
4. accrual-based operating profitability
5. cash-based operating profitability
6. gross profitability
7. net payout ratio

The 7 measures are combined in a three-step regression process to create a fundamental implied return, or FIR. One can think of their process as a rudimentary machine-learning approach that uses the trend in fundamentals to predict future stock returns. The authors then use their FIR metric to identify long and short portfolios.

Price momentum portfolios are generally formed based on the past 12 month cumulative returns (skipping the most recent month)(3).

## How Do Fundamental Momentum and Price Momentum Perform?

The authors look at the performance of independent sorts on fundamental and price momentum.

[![fundamental momentum and price momentum](https://alphaarchitect.com/wp-content/uploads/2017/03/fundamental-momentum-and-price-momentum-1030x835.png)](https://alphaarchitect.com/wp-content/uploads/2017/03/fundamental-momentum-and-price-momentum.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Note the strong dispersion in returns created by both fundamental and price momentum. This suggests that both effects exists in the data and price momentum is not subsumed by fundamental momentum (argument put forth in a [recent Novy Marx paper](https://alphaarchitect.com/2016/01/21/is-price-momentum-a-brother-from-another-mother/)).

The authors also look at the decay of each momentum factor over time.

[![returns after formation](https://alphaarchitect.com/wp-content/uploads/2017/03/returns-after-formation-1030x641.png)](https://alphaarchitect.com/wp-content/uploads/2017/03/returns-after-formation.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Consistent with their prior data, the price and fundamental momentum portfolios have decidedly different portfolio dynamics. Fundamental momentum, akin to value, is slow-moving, whereas price momentum is shorter-lived and requires turnover to be effective. The authors hypothesize that the combination of fundamental and price momentum can be leveraged to create a dual momentum portfolio that exploits the natural differences in the two types of momentum.

## Dual Momentum with Fundamentals and Price

To create the dual momentum stock-picking strategy, the authors go long the ***top price momentum top FIR portfolio*** and short the ***low price momentum low FIR portfolio*** (the 2 red portfolios circled in the table above).

Some high-level conclusions (all results are associated with the long/short dual momentum portfolio):

* Fundamental momentum and price momentum are complements, not substitutes (great diversification benefits)
* Dual momentum earns a monthly average return of 2.16% versus 0.93% and 0.88% for price and fundamental momentum, respectively

The returns over time for each of the momentum strategies are pictured below in a chart from the paper:

[![momentum horserace](https://alphaarchitect.com/wp-content/uploads/2017/03/momentum-horserace-1030x730.png)](https://alphaarchitect.com/wp-content/uploads/2017/03/momentum-horserace.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Both price and fundamental momentum perform well over time, but dual momentum is especially strong because of the natural diversification benefits of combining price/fundamental momentum over time. The authors also throw the [kitchen sink of asset pricing models](https://alphaarchitect.com/2017/02/03/factor-models-are-more-art-and-less-science/) (CAPM, FF3, Carhart, FF5, and Hou, Xue, and Zhang) at the portfolios and identifies significant alpha across the board.

The dual momentum findings are similar to those found when combining value and momentum portfolios. The chart below shows the relative spreads of value, momentum, and the combo portfolio, relative to the S&P 500 ([See here](https://alphaarchitect.com/2016/03/22/why-investors-should-combine-value-and-momentum/) for details).

![](https://alphaarchitect.com/wp-content/uploads/2016/03/why-to-combine-value-and-momentum-fig-5.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Note that the combo portfolio is highly effective because it pools together 2 effective strategies that have limited correlation (a similar idea as dual momentum — combine fundamental and price momentum — 2 effective strategies that don’t act the same).

### Dual Momentum Robustness Tests

The authors look at the problem from a variety of angles to see if Dual Momentum can withstand the gauntlet. None of the robustness concepts create enough doubt to suggest that the findings associated with dual momentum are questionable.

Here are some ideas that the authors test:

* Are the results due to micro-caps?
* Do transaction costs eat all the profits?
* Are there weird factor exposures involved?
* Does the short side of the L/S portfolios drive all the “alpha”?
* Do permutations on fundamental momentum metrics eliminate the results?
* Do changes in the portfolio sorting technique eliminate the results?

Again, the answer to all of these questions are “No.” There are certainly other things the authors could consider, but they do a pretty good job of throwing a lot of darts at their model. Nobody can ever eliminate the possibility of data-mining and/or overfitting, but the robustness tests help alleviate some of these concerns.

## Conclusions

This paper is extremely interesting and the strategy is pretty compelling. Doing this strategy in real-life would be pretty intense from an operational perspective, but certainly doable for a professional or someone who is handy with technology. That said, we’re unsure if the Dual Momentum strategy outlined is dramatically different and/or better than a portfolio construct that is closely related to one we’ve explored in the past: [the value and momentum combination](https://alphaarchitect.com/2015/03/26/the-best-way-to-combine-value-and-momentum-investing-strategies/). Moreover, we think the relationship between fundamental momentum and our particular flavor of value — Quantitative Value — make the relationship even tighter. Why do we say this? Well, when it comes to capturing the value premium, we suggest a focus on cheap (10% decile EBIT/TEV) and then a suite of “quality” metrics, many of *which capture the concepts described to calculate fundamental momentum*. We think fundamental momentum and the quality metrics buried in the [Quantitative Value system](https://alphaarchitect.com/2014/10/07/the-quantitative-value-investing-philosophy/), capture similar things. On net, when one combines Quantitative Value with a price-based momentum system, or whether one combines “fundamental momentum” with a price-based momentum system, we think the endstate will be similar. The long/short aspect could be simplified to be long-only with a passive benchmark short, and much of the operational complexity and risk associated with running a short book could be sidestepped. This would alter the nature of the strategy, but the simplification might be worth the benefit of simplicity.

In the end, the correct answer isn’t “Antonacci Dual Momentum” or “Stock-picking Dual Momentum,” but probably, “both.” — We allude to this “both” answer in an old post, “[Absolute momentum and stock momentum strategies: friends not enemies.](https://alphaarchitect.com/2015/03/31/absolute-momentum-and-stock-momentum-strategies-friends-not-enemies/)”

We look forward to starting the conversation on this really interesting paper and concept. Perhaps the quant geeks at [Quantopian](https://www.quantopian.com/) and across the blogosphere can do some testing on their own and share the results with the community.

---

# Dual Momentum (Now called “Twin Momentum”)

* Huang, Zhang, and Zhou
* A version of the paper can be found [here .](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2894068)
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap](https://alphaarchitect.com/category/architect-academic-insights/) Category.

### Abstract:

> Using both their levels and their time-series trends of a collection of firms’ major fundamentals, we find for the first time that fundamentals matter: they too can generate strong return momentum. The top 20% high fundamental firms outperform the bottom 20% by 88 bps per month, whose performance is comparable with the popular price momentum but with little correlation and with no 12-month reversal. Combining price momentum and fundamental momentum yield a dual momentum that has an average return more than the sum of both price momentum and fundamental momentum. The dual momentum cannot be spanned by extant risk factor models, nor can it be explained by short-sale impediments and investor sentiment.

h.t., Nico P. for sending this paper our way.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | btw, [Guofu Zhou](http://apps.olin.wustl.edu/faculty/zhou/) is one of my favorite researchers and an absolute BEAST when it comes to research |
| ↑2 | If you’d like more information on Dual Momentum, visit [Gary’s site](http://www.dualmomentum.net/) or [review our analysis](https://alphaarchitect.com/2015/02/13/asset-allocation-horserace-robust-asset-allocation-raa-vs-dual-momentum/). |
| ↑3 | [see here](https://alphaarchitect.com/2014/07/16/momentum-investing-ride-winners-and-cut-losers-period/) if you need a refresher |

 function footnote\_expand\_reference\_container\_27270\_109() { jQuery('#footnote\_references\_container\_27270\_109').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_27270\_109').text('−'); } function footnote\_collapse\_reference\_container\_27270\_109() { jQuery('#footnote\_references\_container\_27270\_109').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_27270\_109').text('+'); } function footnote\_expand\_collapse\_reference\_container\_27270\_109() { if (jQuery('#footnote\_references\_container\_27270\_109').is(':hidden')) { footnote\_expand\_reference\_container\_27270\_109(); } else { footnote\_collapse\_reference\_container\_27270\_109(); } } function footnote\_moveToReference\_27270\_109(p\_str\_TargetID) { footnote\_expand\_reference\_container\_27270\_109(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_27270\_109(p\_str\_TargetID) { footnote\_expand\_reference\_container\_27270\_109(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
