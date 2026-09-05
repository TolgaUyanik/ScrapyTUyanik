---
title: "Financial Media, Price Discovery, and Merger Arbitrage"
slug: "financial-media-price-discovery-and-merger-arbitrage"
date: "2021-08-16"
modified: "2021-08-16"
url: "https://alphaarchitect.com/financial-media-price-discovery-and-merger-arbitrage/"
categories: ["Event Driven Investing", "Research Insights", "Basilico and Johnsen", "Academic Research Insight", "AI and Machine Learning"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Financial Media, Price Discovery, and Merger Arbitrage

> Financial Media, Price Discovery, and Merger Arbitrage Buehlmaier and Zechner Review of Finance, forthcoming A version of this paper can be found here Want to read […]

## Financial Media, Price Discovery, and Merger Arbitrage

* Buehlmaier and Zechner
* *Review of Finance,* forthcoming
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2858999)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Research Questions?

This paper contributes to the literature on understanding the limits of arbitrage and the resulting dynamics of price  
discovery. Specifically, it studies the context of “[merger arbitrage](https://alphaarchitdev.wpengine.com/2016/04/28/facts-fiction-merger-arbitrage/),” which is a well-known investment strategy and unless there are [limits to arbitrage](https://alphaarchitdev.wpengine.com/2014/05/20/introduction-behavioral-finance-part-2-limits-arbitrage/), this market segment should be highly efficient.

The authors ask the following question:

* Do texts in financial media provide information about the probability of merger completion which is not already contained in the target stock price?

## What are the Academic Insights?

The authors analyze the Thomson Reuters SDC Platinum database to identify merger-related information, the Dow Jones Factiva dataset for financial press information, the Center for Research in Security Prices (CRSP) for price data, and Compustat for accounting data. By applying methods of textual analysis and computational linguistics(1) the authors calculate the media implied completion probability in the context of a well-defined corporate event: corporate mergers.

The authors find the following:

1. Strong evidence that stock prices underreact to information in financial media both in event time as well as in calendar time tests. In fact, a one standard deviation increase in the media-implied probability of merger completion results in an increase of 1.2 percentage points in the subsequent twelve-day stock return (2.2 percentage points  
   per month) of the target firm. Additionally, when they vary the holding period after the announcement day from one to twelve days, the return effects of a given increment in media implied merger completion probability increase monotonically, implying that information indeed is slow-moving
  
2. Merger arbitrage becomes significantly more profitable if one uses media information to filter out those announced deals with low completion probability. If one uses media information to eliminate those deals with a media-implied completion probability of less than or equal to 85%, which is equivalent to filtering out approximately 28% of all announced deals, then this increases the annualized risk-adjusted return of the trading strategy(2) by 9.3 percentage points
  
3. Price efficiency relative to media information varies with financial market conditions (proxied by the Merrill Lynch US High Yield Master II OptionAdjusted Spread) : media-based profits are particularly large and significant when it is hard for institutional investors to lever up, as indicated by a large high-yield spread. In this case, annualized risk-adjusted returns increase by 11.3 percentage points when filtering out deals with low ex-ante media-implied completion probability. Differently, such profits decrease significantly or vanish completely when high-yield spreads are small

The authors also conduct the analysis with an alternate measure by substituting the “content” based measure with a “coverage” based measure. They find weaker results for media coverage, consistent with the notion that coverage may be easier to manipulate. They also find weak evidence in favor of a certification role of the media. In fact, when they restrict the construction of the media measures to the top newspapers and top newswires to separately investigate their information content, they find that often these top news sources contribute more novel information to the market, consistent with their certification role to stock market investors

## Why does it matter?

This paper is the first to model the probability of an economic outcome as a direct function of textual media content. In fact, they do not use an indirect dictionary approach, where words are classified according to positive or negative psychological associations(3). Instead, they directly relate each word in a press article to merger completion, which is the central focus of this study. In other words “they let the data speak by estimating meaning directly from the data”.

## The Most Important Chart from the Paper:

![](https://alphaarchitect.com/wp-content/uploads/2021/06/2021-06-03-13_28_32-SSRN-id2858999-1.pdf-600x680.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> Using merger announcements and applying methods from computational linguistics we find strong evidence that stock prices underreact to information in financial media. A one standard deviation increase in the media-implied probability of merger completion increases the subsequent 12-day return of a long-short merger strategy by 1.2 percentage points. Filtering out the 28% of announced deals with the lowest media-implied completion probability increases the annualized alpha from merger arbitrage by 9.3 percentage points. Our results are particularly pronounced when high-yield spreads are large and on days when only few merger deals are announced.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | the naïve Bayes model |
| ↑2 | i.e., the “alpha” of the Fama and French (1993) three-factor model |
| ↑3 | important in finance research because this approach can cause misclassifications |

 function footnote\_expand\_reference\_container\_63479\_103() { jQuery('#footnote\_references\_container\_63479\_103').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_63479\_103').text('−'); } function footnote\_collapse\_reference\_container\_63479\_103() { jQuery('#footnote\_references\_container\_63479\_103').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_63479\_103').text('+'); } function footnote\_expand\_collapse\_reference\_container\_63479\_103() { if (jQuery('#footnote\_references\_container\_63479\_103').is(':hidden')) { footnote\_expand\_reference\_container\_63479\_103(); } else { footnote\_collapse\_reference\_container\_63479\_103(); } } function footnote\_moveToReference\_63479\_103(p\_str\_TargetID) { footnote\_expand\_reference\_container\_63479\_103(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_63479\_103(p\_str\_TargetID) { footnote\_expand\_reference\_container\_63479\_103(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
