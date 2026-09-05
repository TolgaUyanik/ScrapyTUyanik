---
title: "Factor Investing: The Fama French 5-Factor Model on Chinese A-Shares"
slug: "factor-investing-fama-french-5-factor-model-chinese-shares"
date: "2017-03-31"
modified: "2022-05-11"
url: "https://alphaarchitect.com/factor-investing-fama-french-5-factor-model-chinese-shares/"
categories: ["Research Insights", "Factor Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Factor Investing: The Fama French 5-Factor Model on Chinese A-Shares

> Each year I teach my “seminar in investments” course at Drexel, which consists of the Masters in Finance students and a handful of geeky MBA […]

Each year I teach my “seminar in investments” course at Drexel, which consists of the Masters in Finance students and a handful of geeky MBA students.

[![](https://alphaarchitect.com/wp-content/uploads/2017/03/drexel-schedule-wes-gray-1030x402.png)](https://alphaarchitect.com/wp-content/uploads/2017/03/drexel-schedule-wes-gray.png)  
The first few weeks of the course involve an introduction to various investment frameworks and how to navigate the source academic literature.

The rest of the course is *dedicated to research*. ***Yeah, baby!***  
I divide the class into research groups of 5-6 people and they are required to conduct several research projects over the 10 week course.

This year there were a handful of great research projects conducted. A lot of the research projects are associated with factor investing and most of the groups highlighted things we already understood: momentum works, value works, trend-following works, etc.

However, one group went the extra mile and did an extensive investigation of the Fama and French 5-factor model using out of sample data from the Chinese A-share market. (To learn more about factor models, you can [read our long-form piece](https://alphaarchitect.com/2017/02/03/factor-models-are-more-art-and-less-science/) on the subject).

The data in their study included all A-shares from 1995 to 2014 and excluded financial firms, negative book-to-market ratio firms, firms with less than 5 years of return data, and any firm missing the necessary information to calculate the required metrics to calculate the variables: size, book-to-market, beta, profitability, and asset growth. Some caveats are that the data time period is short and the Chinese A-shares market is extremely volatile — arguably hard to identify much signal from all the noise.

## The 5-Factor Model in the Chinese Market

The students started with a highlight of what was discovered in [Fama and French (2015)](http://www8.gsb.columbia.edu/programs/sites/programs/files/finance/Finance%20Seminar/spring%202014/ken%20french.pdf):

* Profitability and investment help explain the cross-section of US stock returns.
* HML becomes redundant when profitability and investment factors are included in their 5-factor model.

Fama and French (2015) is a pretty extensive study with a handful of robustness tests. However, other authors have identified that the Fama and French 5-factor model may not be as robust as originally contemplated. For example, [here is a discussion](https://alphaarchitect.com/2015/06/10/using-profitability-factor-perhaps-think-twice/) by Hou, Xue, and Zhang and Asness also has a discussion in his piece [here](https://www.aqr.com/cliffs-perspective/our-model-goes-to-six-and-saves-value-from-redundancy-along-the-way).(1)

My students were able to take another angle on the debate by looking at out of sample data from Chinese A-shares.

Here is what my students found:

* The original 3-factor Fama French model works well in the Chinese A-share market.
* HML matters. A lot.
* *Profitability and investment (RMW & CMA) becomes redundant* when the value factor (HML) is included in the asset pricing model. (opposite of the results in the US market)

Long story short, based on the evidence from the Chinese A-share market, the Fama and French 3-factor model (beta, size, and value) still gets the job done and the 5-factor model lacks robustness.

Here is the final slide from my student’s presentation:  
[![](https://alphaarchitect.com/wp-content/uploads/2017/03/chinese-a-share-5-factor-model-1030x542.png)](https://alphaarchitect.com/wp-content/uploads/2017/03/chinese-a-share-5-factor-model.png)

References[+]

References

|  |  |
| --- | --- |
| ↑1 | In our own internal work we’ve identified that gross profitability isn’t that compelling in international markets. |

 function footnote\_expand\_reference\_container\_27554\_99() { jQuery('#footnote\_references\_container\_27554\_99').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_27554\_99').text('−'); } function footnote\_collapse\_reference\_container\_27554\_99() { jQuery('#footnote\_references\_container\_27554\_99').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_27554\_99').text('+'); } function footnote\_expand\_collapse\_reference\_container\_27554\_99() { if (jQuery('#footnote\_references\_container\_27554\_99').is(':hidden')) { footnote\_expand\_reference\_container\_27554\_99(); } else { footnote\_collapse\_reference\_container\_27554\_99(); } } function footnote\_moveToReference\_27554\_99(p\_str\_TargetID) { footnote\_expand\_reference\_container\_27554\_99(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_27554\_99(p\_str\_TargetID) { footnote\_expand\_reference\_container\_27554\_99(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
