---
title: "A Protocol to Prevent “Quants Gone Wild”"
slug: "protocol-to-prevent-quants-gone-wild"
date: "2018-12-17"
modified: "2022-04-28"
url: "https://alphaarchitect.com/protocol-to-prevent-quants-gone-wild/"
categories: ["Academic Research Insight", "AI and Machine Learning"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# A Protocol to Prevent “Quants Gone Wild”

> A Backtesting Protocol in the Era of Machine Learning Rob Arnott, Campbell Harvey, and Harry Markowitz Working paper A version of this paper can be […]

## A Backtesting Protocol in the Era of Machine Learning

* Rob Arnott, Campbell Harvey, and Harry Markowitz
* *Working paper*
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3275654)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight/) category.

## What are the Research Questions?

Data mining in finance has long been a concern for academic researchers. Campbell Harvey, one of the authors on this paper, is leading the effort to ensure the integrity of empirical finance research. For example, [see here for a post](https://alphaarchitect.com/2017/03/03/evidence-based-investing-take-alpha-shove/) on his address to the AFA.

The concerns associated with data mining aren’t going away. A monster increase in affordable computing power is facilitating the use of machine learning to create predictive algorithms in finance. Machine learning algorithms have built-in defenses against data mining, but they aren’t full proof. Moreover, the data required to do proper cross-validation does not exist in finance (at least in the investing realm…HFT may be a different story).(1)

This paper addresses a basic question related to the use of quantitative methods (to include machine learning) in the context of finance:

1. Can we develop a sensible research protocol to deal with data-mining concerns?

## What are the Academic Insights?

The authors outline a great research protocol. Below we outline the 7 steps of the protocol with our simple key takeaway on each. Readers should dig [into the paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3275654) for more detail on each component to fully appreciate what is being proposed.

1. **Research motivation**
   * Start any research project with an ex-ante hypothesis, driven by economic foundations
   * For a “winning strategy,” ask the following question: Who is on the other side of the trade?…and why?
2. **Multiple testing and statistical methods**
   * How many variables were tried?
   * How many combinations were used?
   * Do you have enough data to justify the value of additional complexity? Probably not.
3. **Data and sample choice**
   * Live with the data you’ve been dealt — don’t cherry pick, transform, “clean”, and windsorize at random…
   * …but also make sure the data is accurate (e.g., market cap doesn’t exceed 10 trillion for 20 percent of the data set)
4. **Cross-validation**
   * There is no real “out of sample” at this point, save live trading data and fresh historical data.
5. **Model dynamics**
   * Beware of structural change. Humans are tricky animals with evolving tastes.
   * Avoid “tweaking” a model based on live results.
6. **Complexity**
   * Keeps things as simple as possible, but no simpler.
   * We don’t have enough data to truly assess the value of complexity.
7. **Research culture**
   * Reward good processes, not good results. (h.t. to Annie Duke for expressing a similar idea in “[Thinking in Bets](https://alphaarchitect.com/2018/02/09/book-review-thinking-in-bets-making-smarter-decisions-when-you-dont-have-all-the-facts/).”).
   * Do you know where the bodies are buried? Probably not –Do your own research!

## Why does it matter?

The authors make a simple, but important point:

> When data are limited, economic foundations become more important.

[Here is a framework](https://alphaarchitect.com/2015/08/17/the-sustainable-active-investing-framework-simple-but-not-easy/) for understanding how markets work.

## The Most Important Chart from the Paper

Here is a “magical” backtest of a strategy that is long all stocks with tickers with an “s” as the third letter and short stocks with tickers that have “u” as the third letter.

* In-sample and out-of-sample validation
* No correlation with known factors
* Low turnover

---

![](https://alphaarchitect.com/wp-content/uploads/2018/12/a-vs-b-backtest-1200x957-1.png)

## Abstract

> Machine learning offers a set of powerful tools that holds considerable promise for investment management. As with most quantitative applications in finance, the danger of misapplying these techniques can lead to disappointment. One crucial limitation involves data availability. Many of machine learning’s early successes originated in the physical and biological sciences, in which truly vast amounts of data are available. Machine learning applications often require far more data than are available in finance, which is of particular concern in longer-horizon investing. Hence, choosing the right applications before applying the tools is important. In addition, capital markets reflect the actions of people, which may be influenced by others’ actions and by the findings of past research. In many ways, the challenges that affect machine learning are merely a continuation of the long-standing issues researchers have always faced in quantitative finance. While investors need to be cautious—indeed, more cautious than in past applications of quantitative methods—these new tools offer many potential applications in finance. In this article, the authors develop a research protocol that pertains both to the application of machine learning techniques and to quantitative finance in general.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | We are highlighting some applications of machine learning to investing this week, so what follows is timely! |

 function footnote\_expand\_reference\_container\_44379\_53() { jQuery('#footnote\_references\_container\_44379\_53').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_44379\_53').text('−'); } function footnote\_collapse\_reference\_container\_44379\_53() { jQuery('#footnote\_references\_container\_44379\_53').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_44379\_53').text('+'); } function footnote\_expand\_collapse\_reference\_container\_44379\_53() { if (jQuery('#footnote\_references\_container\_44379\_53').is(':hidden')) { footnote\_expand\_reference\_container\_44379\_53(); } else { footnote\_collapse\_reference\_container\_44379\_53(); } } function footnote\_moveToReference\_44379\_53(p\_str\_TargetID) { footnote\_expand\_reference\_container\_44379\_53(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_44379\_53(p\_str\_TargetID) { footnote\_expand\_reference\_container\_44379\_53(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
