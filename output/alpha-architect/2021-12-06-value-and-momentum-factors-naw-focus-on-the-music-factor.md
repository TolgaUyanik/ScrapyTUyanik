---
title: "Value and Momentum Factors? Naw, Focus on the Music Factor!"
slug: "value-and-momentum-factors-naw-focus-on-the-music-factor"
date: "2021-12-06"
modified: "2021-12-06"
url: "https://alphaarchitect.com/value-and-momentum-factors-naw-focus-on-the-music-factor/"
categories: ["Relative Sentiment", "Research Insights", "Basilico and Johnsen", "Academic Research Insight", "Behavioral Finance"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Value and Momentum Factors? Naw, Focus on the Music Factor!

> Can market sentiment be derived from the tunes that your fellow countrymen are listening to? According to the research summarized here you’ll find that there is important market information buried in the listening habits of Spotify users.

## Music Sentiment and Stock Market Returns Around the World

* Edmans, Fernandez-Perez, Garel, Indriawan
* *Journal of Financial Economics,* forthcoming
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3776071)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Research Questions?

What if all those sleepless nights hunting for value and momentum [factors](https://alphaarchitdev.wpengine.com/2017/06/06/the-value-momentum-trend-philosophy/) in the CRSP data were for naught? Maybe we should have been hanging out with our friends and taking note of what they were listening to!

The authors of this paper aim to research an endogenous measure that reflects a “national mood”, a proxy for a country’s actual sentiment. The requirements are for it to be available at a high frequency, at a country rather than city level, and globally comparable (which means it needs to be language-free and thus does not require a sentiment dictionary, the accuracy of which may vary across languages).

By borrowing from the psychology literature that individuals reflect their mood in their music choices and that music sentiment is correlated with economic behavior or beliefs that may drive behavior ([North and Hargreaves, 1996](https://psycnet.apa.org/record/1998-01899-002); [Saarikallio and Erkkilä, 2007](https://journals.sagepub.com/doi/10.1177/0305735607068889), [Sabouni, 2018](https://www.researchgate.net/publication/323560860_The_Rhythm_of_Markets)), they ask the following question:

1. Is there a relation between music sentiment and stock market returns?

## What are the Academic Insights?

By collecting data from Spotify on 40 countries from January 1, 2017, to December 31, 2020, the authors are able to identify 58,000 unique songs with over 500 billion streams. On average, they have 8.6 million streams daily per country, with around 43,000 streams per song. In addition to the top-200 songs, Spotify also provides a metric of a song’s musical positivity known as *valence*. This metric is measured by Spotify’s music intelligence division, The Echo Nest(1).

They find:

1. YES, there is a positive and significant association between music sentiment and contemporaneous returns. The authors control for past returns, the world market return, seasonalities, weather conditions, and macroeconomic variables. A one-standard-deviation increase in music sentiment is associated with a higher weekly return of 8.1 basis points (bps), or 4.3% annualized. BUT this effect reverses over the next week: a one-standard-deviation increase in music sentiment predicts a lower next-week return of 7.0 bps or -3.7% annualized. Both results are consistent with sentiment-induced temporary mispricing, and prior theoretical and empirical findings that negative investor sentiment causes prices to temporarily fall but subsequently correct. The authors apply additional robustness checks like daily returns, dollar and local currency returns, they exclude one country at a time to exclude that that they are not driven by a specific country and they exclude the 50 most-streamed songs per country to address the concern that Spotify suggests songs to users. As well as they perform some out of sample testing like studying equity mutual funds and government bond indices.

## Why does it matter?

We’re not quite ready to launch an ETF on market sentiment based on Spotify users yet (if you’d like to do so here’s our guide to [launching your own ETF](https://alphaarchitdev.wpengine.com/2021/11/16/how-to-start-an-etf-resources-and-faq/)!) However, this paper is important because it introduces a novel measure of investor sentiment, which captures the actual sentiment rather than shocks to the sentiment which has been more frequently measured. And who knows unique sources of alpha are out there waiting to be found, maybe with more time UPBT, the Spotify upbeat ETF will be the new value fund. This paper is a good complement to research on [relative sentiment](https://alphaarchitdev.wpengine.com/2021/08/12/relative-sentiment-and-market-returns/).

## The Most Important Chart from the Paper:

![](https://alphaarchitdev.wpengine.com/wp-content/uploads/2022/04/2021-10-18-13_00_50-Microsoft-Word-music-sentiment-and-stock-returns-20210814.docx-1200x604-1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

![](https://alphaarchitdev.wpengine.com/wp-content/uploads/2021/10/2021-10-18-13_00_33-Microsoft-Word-music-sentiment-and-stock-returns-20210814.docx-1200x562.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> *This paper introduces a real-time, continuous measure of national sentiment that is language-free and thus comparable globally: the positivity of songs that individuals choose to listen to. This is a direct measure of mood that does not pre-specify certain mood-affecting events nor assume the extent of their impact on investors. We validate our music-based sentiment measure by correlating it with mood swings induced by seasonal factors, weather conditions, and COVID-related restrictions. We find that music sentiment is positively correlated with same-week equity market returns and negatively correlated with next-week returns, consistent with sentiment-induced temporary mispricing. Results also hold under a daily analysis and are stronger when trading restrictions limit arbitrage. Music sentiment also predicts increases in net mutual fund flows, and absolute sentiment precedes a rise in stock market volatility. It is negatively associated with government bond returns, consistent with a flight to safety.*

References[+]

References

|  |  |
| --- | --- |
| ↑1 | The Echo Nest was initially a research spin-off from the MIT Media Lab and then acquired by Spotify in 2014. The Echo Nest assigned positivity scores to a sample of 5,000 songs and then used machine learning to create an algorithm that is then applied to the rest of the music in the world. “Valence” measures the positivity of the music, not the lyrics. It ranges from 0 to 1; songs with high valence sound more positive (e.g., happy, cheerful, euphoric), whereas songs with low valence sound more negative (e.g., sad, depressed, angry). |

 function footnote\_expand\_reference\_container\_67524\_12() { jQuery('#footnote\_references\_container\_67524\_12').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_67524\_12').text('−'); } function footnote\_collapse\_reference\_container\_67524\_12() { jQuery('#footnote\_references\_container\_67524\_12').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_67524\_12').text('+'); } function footnote\_expand\_collapse\_reference\_container\_67524\_12() { if (jQuery('#footnote\_references\_container\_67524\_12').is(':hidden')) { footnote\_expand\_reference\_container\_67524\_12(); } else { footnote\_collapse\_reference\_container\_67524\_12(); } } function footnote\_moveToReference\_67524\_12(p\_str\_TargetID) { footnote\_expand\_reference\_container\_67524\_12(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_67524\_12(p\_str\_TargetID) { footnote\_expand\_reference\_container\_67524\_12(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
