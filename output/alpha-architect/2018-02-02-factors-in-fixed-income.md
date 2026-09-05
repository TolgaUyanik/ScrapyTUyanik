---
title: "Value and Momentum Factors in Fixed Income"
slug: "factors-in-fixed-income"
date: "2018-02-02"
modified: "2018-02-02"
url: "https://alphaarchitect.com/factors-in-fixed-income/"
categories: ["Guest Posts"]
tags: ["alpha", "backtest", "anomaly", "Quant-picker", "Strategy", "Fama French", "CAPM", "Z Score", "Institutional Investor"]
best_of: false
source: "alphaarchitect.com"
---

# Value and Momentum Factors in Fixed Income

> Smart beta (or factor investing) seems to be the product du jour in ETFs. There are so many different factor products available that just about […]

Smart beta (or [factor investing](http://alphaarchitdev.wpengine.com/2017/02/03/factor-models-are-more-art-and-less-science/)) seems to be the product du jour in ETFs.  There are so many different factor products available that just about every fund company seems to offer them…even Vanguard is launching their own suite of factor-based stock funds. Note that nearly all of these products are focused on stocks…not bonds.

*Why the lack of factor love for fixed income instruments?*

Fixed income seems to be the red-headed stepchild of factor investing and academic factor research!  The earliest factor research that explores bonds was done by none other than [Fama and French in 1993](http://rady.ucsd.edu/faculty/directory/valkanov/pub/classes/mfe/docs/fama_french_jfe_1993.pdf). Their core finding was that duration and credit were the core drivers of bond returns. The research on bond factors beyond this original FF 1993 paper, especially relative to the research on equity factors, is almost non-existent as far as I can tell. That said, fixed income factor investing research did receive some of its first love in 2013 with, “[Value and Momentum Everywhere](https://www.aqr.com/library/journal-articles/value-and-momentum-everywhere),” where fixed income factor returns (at least value and momentum) are shown to be attractive.(1)  Justin Sibears at Newfound Research (in one of my favorite articles of 2017) shows that an investor can use factor investing in the municipal bond market in his post, “[Smart Beta with Muni Bond ETFs](https://blog.thinknewfound.com/2017/05/navigating-municipal-bonds-factors/).”  Jordan Brooks and Dr. Moskowitz published “[Yield Curve Premia,”](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2956411) which shows cross section fixed income factors are better predictors of returns than other yield curve based models.  Finally, Corey Hoffstein at Newfound research published a great [post](https://blog.thinknewfound.com/2018/01/timing-bonds-value-momentum-carry/) just this week on using factors to time duration exposure in fixed income.  I am not aware of much additional research beyond a couple of client educational papers published by AQR (the additional [research](https://www.aqr.com/Insights/Research/Alternative-Thinking/Style-Investing-in-Fixed-Income) focuses on CUSIP level bond selection factors which would be difficult for the average investor to exploit on their own).

Perhaps the most surprising revelation to me is that the [recent research](https://www.aqr.com/library/aqr-publications/alternative-thinking-4q-2017-the-illusion-of-active-fixed-income-diversification) which shows that many active managers simply exploit the term and credit risk factors and [Justin Sibers](https://blog.thinknewfound.com/2017/05/navigating-municipal-bonds-factors/) shows that (of the funds they looked at) municipal bond funds don’t exploit factors in fixed income.

I hope to add my thoughts to the fixed income factor research by showing that factor investing exists in credit sector selection and that even a very simple factor strategy can potentially harvest those factors.

## Data

I use Bloomberg Barclays fixed income indices for this analysis (both yield and total returns).  The specific indices used are as follows:

![](https://alphaarchitect.com/wp-content/uploads/2018/01/Credit-Indices.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

To calculate real yields I use inflation expectations over various horizons from the Cleveland Federal Reserve inflation expectation data (available [here](https://www.clevelandfed.org/our-research/indicators-and-data/inflation-expectations.aspx)).  Specifically, I use the 2-year expected inflation for short-term bonds, I use the 7-year inflation expectation for intermediate-term bonds and I use the 15-year inflation expectation for long-term bonds.  I use expected inflation to calculate real yield because inflation expectations have a term structure and therefore a 2-year bond and a 30-year bond could trade at very different nominal yields but have the same real yield.  For example, in January 2009, the nominal yield on the BloombergBarclays Corporate Bond 1-5 Year index was 6.6% but had a real yield (using 2-year expected inflation) of 5.6%.  In the same month, BloombergBarclays Corporate 10+ Year Corporate Bond Index had a nominal yield of 6.96% (greater than the short-term bond index nominal yield) but had a real yield of 5.17% (less than the real yield of the short-term bond index).

Each index has a unique starting date, but data is available for all indices starting in 1995.  Therefore, it takes until 2002 to have enough data to calculate the 5-year Z-scores and the 2-year averages (more below).

## Factor Definition Methodology

With respect to fixed income, real yield is generally accepted as the measure of value.  Because this analysis uses bonds of varying degrees of credit risks, one shouldn’t blindly compare the real yield of different bond sectors as if they have similar credit risk (for a similar discussion on stock valuation I suggest you start reading some of Lawrence Hamtil’s blog [posts](http://www.fortunefinancialadvisors.com/blog/how-differences-in-composition-distort-market-valuation-differences)).

To account for the differences in credit risk, I calculate a yield Z-Score for each index (the current real yield is compared to the 5-year average real yield for the same index and the difference of the two is divided by the standard deviation of the real yield over the 5-year period of time).  In this way, we can compare each bond with how cheap or expensive it is compared to its recent history.  This is largely consistent with other valuation methodologies in research where a 5-year return reversal is used.

As an example of how this is done, in January 2009 the BloombergBarclays Corporate Bond 1-5 Year index had a real yield of 5.6% and its average real yield over the previous 60 months was 2.62%.  Over this same time period, the real yield had an annualized standard deviation of 4.45%.  The Z-Score for January 2009 is then (5.6%-2.62%)/4.45% = 2.42.  This means that the index appears to be 2.42 “standard deviations” cheap compared to its 5-year average.

Momentum is (thankfully) much easier to calculate, where I use the trailing 12-month return for each index.

## Factor Long/Short Portfolios

I attempt to follow academic research convention by creating long/short portfolios of the bond indices where the long portfolio consists of the average of the three bond sectors that rank highest on the desired attribute, the middle two sectors are ignored and the average of the bottom three bond sectors constitute the short portfolio.  In this way, the long/short portfolios are dollar neutral.

For value, the average of the prior two years of Z-scores are used to rank each sector to create the long/short portfolios.  The two years of Z-scores are used so that the value portfolio is tranched so that timing luck and turnover are reduced.  For momentum, the trailing twelve-month return is used to rank portfolios.  This is a very similar methodology that Justin Sibears used in his [post](https://blog.thinknewfound.com/2017/05/navigating-municipal-bonds-factors/).

Below is a graph of the performance of the long/short dollar neutral portfolio for each factor:

![](https://alphaarchitect.com/wp-content/uploads/2018/01/Long-Short-Credit-Factors.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

The summary statistics for the series are shown below:

![](https://alphaarchitect.com/wp-content/uploads/2018/01/Long-Short-Summary.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

One can see from the graph and chart, above, value and momentum factors in fixed income have positive (gross) returns and are also negatively correlated…these are very similar (although less impressive) results to value and momentum in equity markets. Nice to see the robustness of the result we’ve seen [over and over again](http://alphaarchitdev.wpengine.com/2016/03/22/why-investors-should-combine-value-and-momentum/).  One interesting difference is that the long/short return for value is almost twice as large as momentum in the fixed income markets…perhaps it’s just better to be a value investor in fixed income?

## Regression Analysis of Long/Short Factors

The next natural question is as follows: Are these results actually value and momentum in fixed income markets or are these results something new/different?  Thankfully, the fine folks at AQR have published the various return series from their Value and Momentum Everywhere [paper](https://www.aqr.com/library/journal-articles/value-and-momentum-everywhere) and made the return series available for download [here](https://www.aqr.com/library/data-sets/value-and-momentum-everywhere-factors-monthly).

Below, I run a regression analysis of the long/short value factor I’ve created against the AQR fixed income value factor from their website.  The regression results are below:

![](https://alphaarchitect.com/wp-content/uploads/2018/01/Value-Regression.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

This analysis shows that this version of the value factor isn’t the same as AQR’s (the r-squared is only 5%), however, they are clearly related, as this value factor has a 0.31 beta and a 2.9 t-stat.

I do the same analysis for the momentum portfolio with the results below:

![](https://alphaarchitect.com/wp-content/uploads/2018/01/Momentum-Regression.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

The results for the momentum regression are very similar as the regression analysis for value – this version of fixed income momentum isn’t the same as AQR’s with an r-squared of only 1.3%, but it has a 0.19 beta to AQR’s momentum factor with a 1.58 t-stat.

It is not surprising that these long/short fixed income factors are related, but not highly correlated, to the value and momentum results in Value and Momentum Everywhere, as the fixed income markets used in Value and Momentum Everywhere are ten global government bonds as opposed to a swath of bond sectors from a single country.

## Long Only Implementation

Long/short factors are interesting and show that a particular strategy “works,” but is it possible to use fixed income factors for a traditional long-only investor? You bet!  As Sam Lee (in this [blog post](http://svrn.co/blog/2016/6/6/every-active-fund-is-a-long-short-fund-a-simple-framework-for-assessing-the-quality-quantity-and-cost-of-active-management)) and Corey Hoffstein (in this [blog post](https://blog.thinknewfound.com/2017/11/longshort-portfolios-all-the-way-down/)) remind us, every deviation from a benchmark is a combination of the benchmark + a long/short portfolio.  What this means is that we can start with a benchmark and simply add or subtract the long/short factor exposure.

To test this, we build a benchmark that is simply the equal-weighted average of all eight sectors that were used in the analysis.  The long-only factor fixed income portfolio is then the benchmark + the average weight of the value and momentum portfolio.

For example, if both the value portfolio and the momentum portfolio would be short-intermediate term investment grade sector then it would be completely avoided in the long-only portfolio and its weight would be used elsewhere.  If the value and momentum long/short portfolio were giving a mixed signal to a fixed income sector then it would receive a neutral weight (same as the benchmark).  If both the value and momentum long/short portfolio would be long the intermediate term investment grade sector, the long-only factor portfolio would be overweight that particular fixed income sector.

Does this strategy work?

Below, I show the graph of the long-only fixed income factor portfolio vs. the equal-weighted benchmark:

![](https://alphaarchitect.com/wp-content/uploads/2018/01/Long-Only-Graph.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

The following is a brief summary statistics for the two portfolios:

![](https://alphaarchitect.com/wp-content/uploads/2018/01/Long-Only-Summary-Stats.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

As you can see from the summary stats above, even the long-only factor portfolio has an excess return with a similar volatility of the benchmark.  In addition, the long-only factor portfolio generates a (gross) alpha of 2% per year and has a 0.92 beta to the benchmark.

These results are interesting, but Corey Hoffstein (Corey and I corresponding regarding our blog posts as we both were independently writing about factors in bonds) asked a great question – Are these results due to implicitly timing interest rates (i.e., these factors were correctly changing the duration of the bond portfolio) or are they due to cross-sectional factors (i.e., picking bond sectors correctly while not correctly changing the duration of the portfolio)?

To determine the answer to this question, I estimated the duration of the Benchmark portfolio and the

Long Only Factor portfolio and graphed them over time, below:

![](https://alphaarchitect.com/wp-content/uploads/2018/01/Durations-Over-Time.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

It should be clear from the graph above, that the Long Only Factor portfolio was, in fact, making very large interest rate bets.

The next step was to determine if these interest rate bets were the driver of returns or if the Long Only Factor Portfolio was successful in making cross-sectional bond selections.  To determine the answer to this question, I created another portfolio where the bond sectors that were exhibiting positive factor characteristics were not equally weighted, but instead, duration weighted so that the ending portfolio had a duration equal to that of the benchmark each month (I realize this doesn’t eliminate interest rate risk entirely as it still leaves different curve kinks but it should be a good approximation).  This change resulted in the following results:

![](https://alphaarchitect.com/wp-content/uploads/2018/01/Duration-Equalized-Returns.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

Here are the summary stats for the Duration Equalized Factor portfolio:

![](https://alphaarchitect.com/wp-content/uploads/2018/01/Duration-Equalized-Summary-Stats.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

As you can see from the results above, the Duration Equalized performance does decline when interest rate bets are removed but the majority of the (gross) outperformance remains.  This would seem to indicate that the (gross) outperformance appears to be due to cross-sectional factors in fixed income markets (this conclusion would also be supported by the regression analysis which shows meaningful loadings on cross-sectional value and momentum in government bonds).

## Conclusion

Factor investing in equities seems to get all the attention in both academic research and in the creation of investable products.  However, value and momentum in fixed income markets appears to have all the desirable attributes (returns and low/negative correlation to each other) as factors in equities.  Even using very simple factor definitions (please read Corey’s [post](https://blog.thinknewfound.com/2018/01/timing-bonds-value-momentum-carry/) on duration timing with factors to understand how one might construct a more complex factor methodology for fixed income), these results show that it might be possible to harvest fixed income factors for individual investors.

For those interested (and understanding that this is now almost a month out of date), the Long Only Factor portfolio (which is NOT neutralized for duration differences) would have the following allocation as of 12/31/17:

1. 16.67% BloombergBarclays Corporate 1-5 Year
2. 16.67% BloombergBarclays Corporate 10+ Year
3. 16.67% BloombergBarclays High Yield
4. 33.33% BloombergBarclays US High Yield 1-5 Year
5. 16.67% BloombergBarclays Treasury 1-3 Year

## Post Script

Mike Harris (of priceactionlab.com) asked some great questions via twitter and I wanted to share both his questions and answers as a post script for everyone’s benefit (they all have to do with parameter specification and if the results shown in the post were optimized):

* What do the results look like if you include only the Top 1 position by value and momentum, what about Top 2 for each factor or Top 4 for each factor?

![](https://alphaarchitect.com/wp-content/uploads/2018/02/Chop-Analysis.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

I graph the answers, above, for the long/short factor portfolios.  The answers are largely what we expect in that the fewer assets included, the better the returns but the more variable the results.  The results are approximately the same and appear to be robust to the breakpoints decision about how many assets to include in the factor long/short portfolio.

* What do the results look like if you change the Z-Score lag to 1 year, 3 years or 4 years?

![](https://alphaarchitect.com/wp-content/uploads/2018/02/Z-Score-Lags.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

I graph the results of the changes, above.  Again, we can see that the results appear to be robust to the decision of how long of an averaging period to use in building the value long/short portfolio.

Mike’s questions are great and help show that the results in the post are not optimized or data mined and are robust to specification.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | Bai, Bali, and Wen have a new paper as well. [Check it out here](https://www.houseoffinance.se/wp-content/uploads/2016/06/Bai-Jennie_The-Cross-Section-of-Expected-Corporate.pdf). |

 function footnote\_expand\_reference\_container\_35174\_177() { jQuery('#footnote\_references\_container\_35174\_177').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_35174\_177').text('−'); } function footnote\_collapse\_reference\_container\_35174\_177() { jQuery('#footnote\_references\_container\_35174\_177').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_35174\_177').text('+'); } function footnote\_expand\_collapse\_reference\_container\_35174\_177() { if (jQuery('#footnote\_references\_container\_35174\_177').is(':hidden')) { footnote\_expand\_reference\_container\_35174\_177(); } else { footnote\_collapse\_reference\_container\_35174\_177(); } } function footnote\_moveToReference\_35174\_177(p\_str\_TargetID) { footnote\_expand\_reference\_container\_35174\_177(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_35174\_177(p\_str\_TargetID) { footnote\_expand\_reference\_container\_35174\_177(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
