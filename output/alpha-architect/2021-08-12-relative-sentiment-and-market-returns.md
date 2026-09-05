---
title: "Relative Sentiment and Market Returns"
slug: "relative-sentiment-and-market-returns"
date: "2021-08-12"
modified: "2022-06-13"
url: "https://alphaarchitect.com/relative-sentiment-and-market-returns/"
categories: ["Relative Sentiment", "Research Insights", "Guest Posts", "Academic Research Insight", "Other Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Relative Sentiment and Market Returns

> Market Returns and A Tale of Two Types of Attentions Da, Hua, Hung, and Peng A version of this paper can be found here Want […]

## **Market Returns and A Tale of Two Types of Attentions**

* Da, Hua, Hung, and Peng
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3551662)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight/) category

## **What are the Research Questions?**

This paper studies the relationship between aggregate investor attention and subsequent market returns over the following week. The authors create two different investor attention indicators—one for aggregate retail attention (ARA) and one for aggregate institutional attention (AIA).

ARA is found by taking the market-weighted average of stock-level retail attention, which itself is found by taking the Google Trends Search Volume Index and dividing by its 6-month median. ARA data runs from 2004 until 2018.

AIA is found by taking the market-weighted average of stock-level institutional attention, which itself is given by the Daily Maximum Readership of a stock on Bloomberg (if the DMR is >= 3, the stock-level institutional attention is scored a 1, otherwise a 0).  AIA data runs from 2010 until 2018.

Their universe is all stocks on the NYSE, AMEX, Nasdaq, and NYSE Arca exchanges over the time period 2004 – 2018.

The paper seeks answers to three main questions:

1. Does aggregate investor attention (of either type) predict subsequent market returns?
2. Does aggregate investor attention predict subsequent market returns around macroeconomic news releases (e.g., FMOC, non-farm payrolls, PPI)?
3. Can aggregate investor attention explain the earnings-announcement-cluster (EAC)(1) return premium?

## **What are the Academic Insights?**

This paper has an unequivocal set of findings, consistent with previous literature and with their own internal list of hypotheses.

1. With respect to question one above, the authors find that ARA negatively forecasts one-week ahead market returns in a statistically and economically significant way. A one standard deviation increase in ARA leads to a 22-basis-point (bp) decrease (relative to baseline) of the following week’s market return.  
     
   They further find that the effect is amplified during periods of low liquidity in the market—i.e., during periods when the VIX is high or bid-ask spreads are wide or when stock lending fees are more expensive. In fact, when market liquidity is high, the statistical and economic significance of the effect goes away.  
     
   Consistent with the finding that ARA has more of an effect when market liquidity is low, they also find that at the stock level, retail attention is more predictive for illiquid stocks.  
     
   Turning their attention to AIA, they find that while high AIA is positively related to the following week’s market return, it does not quite reach the level of statistical significance (*t*-stat of 1.5). They also find that there is no difference in predictability for AIA between states of low or high market liquidity.  
     
   Interestingly, they find that when ARA and AIA are combined in one regression (instead of separate regressions), both have statistically significant coefficients.
2. In regards to question two, they find that AIA increases significantly (in a statistical sense) in the days leading up to major news releases and that this AIA is positively and significantly related to the following week’s return. In contrast, ARA has no predictive power around major news releases (and, similarly, AIA has no predictive power when there are no major news releases).  
     
   According to the authors, these findings “support the hypothesis that institutional investors anticipate the arrival of information, and their increased attention and information acquisition coincide with a greater reduction of uncertainty and a realization of a market risk premium. The divergent return predictability patterns between AIA and ARA across news and no-news days further highlight the differences in the way institutional and retail investors react to news and affect aggregate returns.”  
     
   Consistent with AIA coinciding with a greater reduction of uncertainty and a realization of a market risk premium, they find that at the stock level, institutional attention is much more predictive for stocks with higher betas, i.e., ones with greater sensitivity to systematic risk.
3. Lastly, with respect to question three, they find that the earnings-cluster-announcement (EAC) return premium is only observed on days when ARA is high. When ARA is low, the premium does not exist. The pattern they observe is that when ARA is high, the return premium is 36 bps on the day of the announcements (which take place after the close), but the return the next day is muted. In contrast, when ARA is low, there is no abnormal return premium on the day of the announcements, but the next day’s return is higher by 21 bps on average.

> “The result suggests that such premium is driven by retail investors, whose attention to the upcoming announcements triggers excessive buying across a broad range of stocks and generates positive aggregate price pressure in the hours preceding the announcements. The reversal of this price pressure on the next day offsets the accrual of risk premiums associated with the announcements and contributes to a muted return post announcement.”

The findings described above were in-sample findings. Conducting walk-forward analysis, they find that the results hold up well out of sample. Moreover, the results remain valid when various robustness checks are added such as additional control variables and different measures of ARA and AIA.

In summing up their results, the authors state:

> “The findings are consistent with a mechanism in which aggregate retail attention triggers a transitory market-wide price pressure that quickly reverts, whereas aggregate institutional attention is positively associated with the systematic accrual of risk premiums [but primarily only around major macroeconomic releases, e.g., FOMC, non-farm payrolls, PPI]. The rise of aggregate retail attention preceding clustered earnings announcements also provides insights into the preannouncement market return premium puzzle.”

## **Why Does it Matter?**

In addition to lending original and significant insight to the earnings-announcement-cluster phenomenon, this paper adds to the already-voluminous literature on the divergent outcomes experienced by institutional and individual investors. But it does so by using a different data set over a different time period and universe. Consequently, it further confirms the robustness of the institutional vs. retail dichotomy.

Indirectly, the paper further validates the notion that *relative sentiment*—i.e., the comparison of how different classes of investors (usually institutional vs. retail) are positioned relative to one another or how they feel about the market with respect to one another—is a market anomaly along the lines of Value, Momentum, Quality, and other widely accepted factors. (Relative sentiment was previously written about [here](https://alphaarchitect.com/2019/02/08/relative-sentiment-a-unique-market-timing-tool-that-isnt-trend-following/), [here](https://alphaarchitect.com/2020/02/28/smart-money-indicator-rebuttal/), and a newer paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3475258).)

It was telling that though AIA on a standalone basis was not statistically significant in predicting next week’s market return (except around major news releases), when combined with ARA in the same regression, both indicators were significant. Moreover, the authors provide a reason as to why institutions might systematically have better outcomes:

> “Our finding that aggregate institutional attention precedes aggregate retail attention suggests that the better resources and stronger incentives of institutional investors to attend to information translate into their systematic advantage over retail investors.”

In light of the recent rise to prominence of Reddit’s WallStreetBets community (and, in general, the surge in retail trading brought about by the pandemic), it would be interesting to see whether this analysis would have held up over the past year and a half (the time period in the paper ends in 2018).

## **Most Important Chart from the Paper**

![](https://alphaarchitect.com/wp-content/uploads/2021/07/image-2-600x706.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

**Abstract**

> Daily aggregate retail attention to stocks (ARA) strongly and negatively predicts the one-week-ahead market returns, whereas aggregate institutional attention (AIA) positively predicts market returns around scheduled major news announcements. The patterns are consistent with aggregate retail buying that generates a transitory market-wide price pressure that quickly reverts and increased institutional attention preceding the systematic accrual of a risk premium. Cross-sectional tests conditioned on illiquidity and market beta further confirm these channels. Results are robust out- of-sample and the effect of ARA is causal. The aggregate attention patterns also shed light on the puzzling pre-announcement premium observed on days of clustered earnings announcements.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | The EAC return premium is when the market ramps up on days there is a cluster of high-profile earnings announcements after the close. |

 function footnote\_expand\_reference\_container\_64196\_105() { jQuery('#footnote\_references\_container\_64196\_105').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_64196\_105').text('−'); } function footnote\_collapse\_reference\_container\_64196\_105() { jQuery('#footnote\_references\_container\_64196\_105').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_64196\_105').text('+'); } function footnote\_expand\_collapse\_reference\_container\_64196\_105() { if (jQuery('#footnote\_references\_container\_64196\_105').is(':hidden')) { footnote\_expand\_reference\_container\_64196\_105(); } else { footnote\_collapse\_reference\_container\_64196\_105(); } } function footnote\_moveToReference\_64196\_105(p\_str\_TargetID) { footnote\_expand\_reference\_container\_64196\_105(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_64196\_105(p\_str\_TargetID) { footnote\_expand\_reference\_container\_64196\_105(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
