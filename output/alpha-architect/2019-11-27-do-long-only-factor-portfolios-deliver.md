---
title: "Forbidden Knowledge: Long-Only Academic Factors are Also Cool"
slug: "do-long-only-factor-portfolios-deliver"
date: "2019-11-27"
modified: "2022-05-20"
url: "https://alphaarchitect.com/do-long-only-factor-portfolios-deliver/"
categories: ["Research Insights", "Factor Investing", "Value Investing Research", "Momentum Investing Research", "Low Volatility Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Forbidden Knowledge: Long-Only Academic Factors are Also Cool

> When Equity Factors Drop Their Shorts David Blitz, Guido Baltussen, and Pim van Vliet Working Paper A version of this paper can be found here Want […]

## When Equity Factors Drop Their Shorts

* David Blitz, Guido Baltussen, and Pim van Vliet
* *Working Paper*
* A version of this paper can be [found here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3493305)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Research Questions?

The standard academic approach to factor analysis is through the lens of long-short portfolios (which often confuses practitioners!). For example, a researcher may take the universe of the largest 1,000 stocks and sort them on “value”, as measured via book-to-market. The “value factor” portfolio may go long the top third cheapest stocks (“value leg”) and go short the bottom third most expensive stocks (“glamour leg”).(1)

Long/short academic factor portfolios are convenient because they capture the “spread” between two extremes associated with a given characteristic (e.g., book/market, past 12-month returns, gross profits / total assets, etc.). Researchers can study the spread and gain important insights on how markets work. In addition, long/short factors are usually uncorrelated to the market and play well in the statistics sandbox. This feature makes regression analysis easy and avoids multicollinearity problems (i.e., running a regression with highly correlated dependent variables will make interpreting factor coefficients impossible).

Of course, the problem with academic long/short factors is that practitioners often don’t care about multicollinearity or the short side of a factor portfolio — they care about building long-only portfolios that solve investor needs/demands.(2)

What does this mean in practice? For the vast majority of investors, long-only factor portfolios are the most realistic path to capture the benefits of factors. And to the extent an investor has more advanced knowledge, one could seek to isolate the benefits of factors, by simply being long a specific factor portfolio and then shorting a broad market index (to minimize market, or “beta” risk). This “long the factor, short the market” approach can simplify the operational footprint of a strategy and tell us potentially useful information about long-only factors and their use in real-world portfolios. (We use this approach in our [Global Value Momentum Trend Index](https://alphaarchitect.com/valuemomentumtrend/), for example). But a natural question is whether or not long-only factors actually generate any expected portfolio benefits. One hypothesis is that all the factor mojo is isolated in the short leg and that the long-leg is worthless. This paper is an initial investigation into this question.

Up until this point, not a lot of formal research has been done on isolating the specific benefits of the long-leg and short-leg of factor portfolios. The crew at Robeco address this hole in the literature in their new research piece, “When equity factors drop their shorts.” The research ditches the traditional academic conventions and investigates factor performance by going long the factor / short the market, or going long the market / short the factor.

The key questions addressed are as follows:

1. What is the performance of “long the factor and short the market” portfolios?
2. What is the performance of “long the market and short the factor” portfolios?
3. How are low-risk and value premiums affected?

## What are the Academic Insights?

1. The long leg of factors drives outperformance and have a near-zero correlation across the factors (i.e., good).
2. The short leg of factors have low performance and are correlated across the factors (i.e., bad).
3. In contrast to recent research from Novy-Marx and Fama and French, the long leg of the low-risk and value premiums are NOT explained by the profitability and investment factors. The low-risk and value premiums are actually unique. In contrast, the short-leg of the low-risk and value premiums (i.e, the high risk and expensive stocks) can be explained by the profitability and investment factors.

## Why Does it Matter?

The paper’s key findings are surprising and warrant a deeper dive (one can be sure AQR researchers will have a rebuttal in short order!):

> In sum, short legs offer no value add once controlling for the long legs, as the factor exposure of short legs is fully subsumed by the long legs

Taken at face value, the author’s findings are interesting and require a rethink of the traditional arguments for how and why factors exist in the first place. As many readers know, there are two finance religions: the efficient markets religion (“EMH”) and the behavioral finance religion. EMHers have a ton of explaining to do, given the results in this paper: For example, why would the long-only factors have zero correlation while the short factors have a positive correlation? Aren’t the long-only factors, which have all the positive returns, supposed to be the risky portfolios that contain all the systematic non-diversifiable risk? And aren’t the short portfolios, which have much lower returns, supposed to serve as your human-capital hedge? (see “[Why growth stocks are awesome](https://alphaarchitect.com/2011/08/11/why-growth-stocks-are-awesome/)“).

EMH is coming out of this with a black eye, but the behavioral finance crew isn’t exactly “winning.” [Behavioral finance](https://alphaarchitect.com/2014/05/13/behavioral-finance-and-investing-are-you-trying-too-hard/), as understood in academic research, suggests that prices do not reflect fundamentals because 1) investors are constrained and make poor decisions and 2) exploiting these opportunities is costly (i.e. “limits of arbitrage”). Unfortunately, behavioral finance would suggest that the short leg of factors should have higher “alpha” because the limits of arbitrage are arguably more intense (i.e., shorting is expensive and very difficult). This paper seems to say the opposite — d’oh!

Where does that leave us? Well, apparently we still don’t understand exactly how and why markets work. Maybe none of this is too surprising, as we have [already outlined in the past](https://alphaarchitect.com/2017/02/03/factor-models-are-more-art-and-less-science/) that factor investing is probably more art and less science.

## The Most Important Chart from the Paper

![](https://alphaarchitect.com/wp-content/uploads/2019/11/2019-11-25-09_35_20-When-equity-factors-drop-their-shorts_Oct2019-2.pdf-1200x815.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

---

## Abstract

> This paper makes a breakdown of common equity factor strategies into their long and short legs, and finds that (i) most added value tends to come from the long legs, (ii) the long legs of factors offer more diversification than the short legs, and (iii) the performance of the shorts is generally subsumed by the longs. These results hold across large and small caps, are robust over time, carry over to international equity markets, and cannot be attributed to differences in tail risk. Moreover, we do not even account for the substantially higher implementation costs involved with the shorts compared to the longs. We also challenge recent claims that the value and low-risk factors are subsumed by the new Fama-French factors, as we find that this result is entirely driven by the short legs of these factors and breaks down for the longs. Altogether, our findings show that decomposing factors into their long and short dimensions is crucial for understanding factor premiums and building efficient factor portfolios.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | This isn’t exactly how it always works, but close enough. [See here](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_factors.html) for more details on the Fama French factor portfolios or read the data section of the paper under discussion. |
| ↑2 | There are obvious exceptions. AQR, for example, specializes in delivering long/short portfolios that reflect the construct of academic factor portfolios. The approach is considered to be “alpha efficient” because the user can capture “edge” on both the long and the short side of the portfolio. |

 function footnote\_expand\_reference\_container\_53332\_72() { jQuery('#footnote\_references\_container\_53332\_72').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_53332\_72').text('−'); } function footnote\_collapse\_reference\_container\_53332\_72() { jQuery('#footnote\_references\_container\_53332\_72').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_53332\_72').text('+'); } function footnote\_expand\_collapse\_reference\_container\_53332\_72() { if (jQuery('#footnote\_references\_container\_53332\_72').is(':hidden')) { footnote\_expand\_reference\_container\_53332\_72(); } else { footnote\_collapse\_reference\_container\_53332\_72(); } } function footnote\_moveToReference\_53332\_72(p\_str\_TargetID) { footnote\_expand\_reference\_container\_53332\_72(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_53332\_72(p\_str\_TargetID) { footnote\_expand\_reference\_container\_53332\_72(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
