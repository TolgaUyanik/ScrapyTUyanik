---
title: "No Skill? Well, Active Share Won’t Save You!"
slug: "no-skill-well-active-share-wont-save-you"
date: "2019-08-05"
modified: "2022-05-19"
url: "https://alphaarchitect.com/no-skill-well-active-share-wont-save-you/"
categories: ["Research Insights", "Basilico and Johnsen", "Academic Research Insight", "Active and Passive Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# No Skill? Well, Active Share Won’t Save You!

> Is High Active Share Always Good? Giuliano De Rossi and Gurvinder Brar The Journal of Asset Management A version of this paper can be found here […]

## Is High Active Share Always Good?

* Giuliano De Rossi and Gurvinder Brar
* The Journal of Asset Management
* A version of this paper can be found [here](https://link.springer.com/article/10.1057/s41260-018-0096-5)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

This paper is the first to examine the impact of including an active share target into the mean-variance optimization process of constructing portfolios. They use the Ceria and Stubbs (2006) approach to robust portfolio optimization as methodology. Monte Carlo simulations are run on DJIA stocks with expectations set by the historical return and covariance matrix. The process is complex and I would encourage the interested reader to examine the details in the paper. The authors do an excellent job explaining the process.

1. Will adopting active share targets or limits in an optimization strategy necessarily lead to better performance?
2. What are the implications for limiting active share at various levels of management skill? Is there a minimum level of skill necessary to benefit from targeting active share?

## What are the Academic Insights?

1. NO. The results presented in Table 1, show the distribution of the objective function values out of sample, for 3 strategies: true parameters (no uncertainty, not a feasible portfolio), mean-variance optimization utilizing the sample mean, and constrained mean-variance optimization utilizing a limit on active share. The lower the value of the function, the higher the utility for the investor. The lowest objective function occurs for the infeasible portfolio as expected. *The next “best” result occurs with the targeted active share optimization.* Although the mean return (understood as “alpha” in this application) is lower, so is the level of tracking error, an attractive tradeoff.
2. YES. The authors argue that in realistic conditions, it is possible to specify a minimum level below which a limit on active share would improve performance. The Monte Carlo approach used in this analysis is suggestive of a methodology that could be used to identify a specific cutoff. That is, the issue of the necessary level of IC is necessary to identify cases when constraining active share is beneficial. For example, when varying levels of skill (ICs of .5, .9, 1.5) are introduced to the optimization, the limit on active share again leads to the best outcome if the IC is .9 or lower. At the highest level of skill, IC =1.5, there is an unacceptable deterioration in the level of mean return relative to the reduction in tracking error when active share is targeted. In that case, the unconstrained mean-variance optimization is best.  Interesting.

## Why does it matter?

Although, the Cremers and Petajisto 2009 paper titled: “How active is your fund manager? A new measure that predicts performance”, established a predictive relationship between active share and return performance, it did not establish that increasing active share will necessarily improve portfolio performance.(1) Contrary to expectations, this article establishes that targeting or limiting active share will improve portfolio construction. Although intuitively obvious, a manager will not outperform without taking on active share, but no amount of active share will compensate for lack of skill.

The authors recommend setting active share targets in the context of the portfolio manager’s skill. Any effort to boost and/or market high active share in order to enhance the reputation of the fund is ill-advised.

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2019/07/2019-07-23-21_07_30-Microsoft-Edge-1-1200x422.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> More and more asset managers are committing to an explicit active share target, which takes the form of a lower bound (e.g. at least 75%) or a range of values (e.g. between 75 and 85%). The active share target is used either in conjunction with, or as a substitute for a tracking error limit. We analyse the implications of active share targets on the portfolio construction process using a simple optimisation framework. Our results suggest, counter to conventional wisdom, that in certain situations the portfolio construction process beneﬁts from imposing a limit on active share rather than from boosting active share. In particular, if the signal used in a strategy is weak, then a constraint on active share can help mitigate the effects of model uncertainty.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | [discussed here](https://alphaarchitect.com/2016/09/13/the-expensive-lesson-of-closet-indexing-avoid-low-active-share-and-high-expenses/). |

 function footnote\_expand\_reference\_container\_36448\_182() { jQuery('#footnote\_references\_container\_36448\_182').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_36448\_182').text('−'); } function footnote\_collapse\_reference\_container\_36448\_182() { jQuery('#footnote\_references\_container\_36448\_182').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_36448\_182').text('+'); } function footnote\_expand\_collapse\_reference\_container\_36448\_182() { if (jQuery('#footnote\_references\_container\_36448\_182').is(':hidden')) { footnote\_expand\_reference\_container\_36448\_182(); } else { footnote\_collapse\_reference\_container\_36448\_182(); } } function footnote\_moveToReference\_36448\_182(p\_str\_TargetID) { footnote\_expand\_reference\_container\_36448\_182(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_36448\_182(p\_str\_TargetID) { footnote\_expand\_reference\_container\_36448\_182(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
