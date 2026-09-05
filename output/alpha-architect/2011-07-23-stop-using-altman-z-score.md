---
title: "Stop Using the Altman-Z Score."
slug: "stop-using-altman-z-score"
date: "2011-07-23"
modified: "2022-06-04"
url: "https://alphaarchitect.com/stop-using-altman-z-score/"
categories: ["Research Insights", "Factor Investing"]
tags: ["abnormal returns", "Altman-Z", "Z Score", "Financial Distress"]
best_of: false
source: "alphaarchitect.com"
---

# Stop Using the Altman-Z Score.

> Ed Altman is simply a legend. Everyone in finance is familiar with the Altman Z-Score and many analysts use it religiously–despite the fact there has […]

Ed Altman is simply a legend.

Everyone in finance is familiar with the Altman Z-Score and many analysts use it religiously–despite the fact there has been 50 years worth of research suggesting there are better methods. The Altman Z-Score kinda reminds me of the CAPM: the CAPM has been shown to not be [very effective](http://www.google.com/url?sa=t&source=web&cd=1&ved=0CBUQFjAA&url=http%3A%2F%2Fwww.bengrahaminvesting.ca%2FResearch%2FPapers%2FFrench%2FThe_Cross-Section_of_Expected_Stock_Returns.pdf&ei=4SkrTqL0DIby0gGi773QCg&usg=AFQjCNGNbtAGduKWC0EEQ8WrPqNMNaJbPg&sig2=6XKoJtC01tsBLuHe9sn3Pg), and yet, everyone still uses it?

Nonetheless, Prof. Altman single handily created an empire based on his original 1968 book/research on [predicting corporate bankruptcy](http://pages.stern.nyu.edu/~ealtman/PredCorpBkrptcy.pdf).

Prof. Altman went ahead and outdid himself with his [new ZETA score](http://pages.stern.nyu.edu/~ealtman/ZETA-Analysis.pdf):

The point of this post is to highlight some recent research that concocts a model that predicts better than the Altman-Z AND is relatively straight forward to implement (at least relative to the ZETA score, which is proprietary and involves a lot of leg work to reverse engineer).

Before we begin, here are some recent models showing that Altman-Z is dead:

* [Shumway (2001)](http://www-personal.umich.edu/~shumway/papers.dir/forcbank.pdf)
  + Shows that half of the variables included in Altman-Z are no longer predictive of bankruptcy–ouch.
  + He also identifies a model that trumps the Altman-Z in out of sample tests–double ouch.
* [Chava and Jarrow (2004)](http://www2.wu-wien.ac.at/rof/papers/pdf/Chava-Jarrow_Bankruptcy%20Prediction.pdf)
  + Verify with expanded data that Altman’s model sucks vs. Shumway’s model.
  + Determine that controlling for industry effects can significantly improve bankruptcy prediction models.

## What does this paper add to the party?

The authors devise a model that ends up improving the forecast accuracy by 16% compared to Shumway and Chava and Jarrow’s models (which in turns mean it is *way* better than Altman-Z).  
Here is how they set up their prediction variables:

* profitability measure=weighted average (quarter’s Net income/MTA)(1)
  + MTA=Market value of total assets=book value of liabilities +market cap.
* leverage measure=Total liabilities/MTA
* short-term liquidity=cash & equivalents/MTA
* Recent relative performance=weighted average(log(1+stock’s return)-log(1+S&P 500 return)
* Recent volatility=annualized stock’s standard deviation over the previous 3 months
* Relative size=log(stock market cap / S&P 500 total market value)
* Overvaluation factor=MTA/adjusted book value, where adjusted book value=book value+.1\*(market cap-book value)
* Stock price level=Log(recent stock price), capped at $15, so a firm with a stock price of $20, would be given a value of log(15) instead of log(20).

Here is the “explanation” from the text:

[![](https://alphaarchitect.com/wp-content/uploads/2011/07/debt2.png "debt2")](https://alphaarchitect.com/wp-content/uploads/2011/07/debt2.png)

What the authors meant to say is that their weighted average is simply calculated as follows: .5333\* t+.2666\*t-1+.1333\*t-2+.0666\*t-3. Here is a table comparing the stats on the various measures above for the universe of firms and for firms that have failed:

[![](https://alphaarchitect.com/wp-content/uploads/2011/07/debt.png "debt")](https://alphaarchitect.com/wp-content/uploads/2011/07/debt.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

It certainly seems that the variables are capturing something regarding failed firms!

So how do we go about predicting bankruptcy/failure? Behold the magical distress formula:

[![](https://alphaarchitect.com/wp-content/uploads/2011/07/debt1.png "debt1")](https://alphaarchitect.com/wp-content/uploads/2011/07/debt1.png)  
After running some logistic regressions the authors determine that their model beats the best alternatives out there over a variety of time periods:

[![](https://alphaarchitect.com/wp-content/uploads/2011/07/debt4.png "debt4")](https://alphaarchitect.com/wp-content/uploads/2011/07/debt4.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

[![](https://alphaarchitect.com/wp-content/uploads/2011/07/debt5.png "debt5")](https://alphaarchitect.com/wp-content/uploads/2011/07/debt5.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Here are the results from the logistic regression:  
If you forgot to get a PhD in some quantitative field and you are not sure how to use these regression results, here is a quick background on [logistic regressions](http://www.youtube.com/watch?v=NHOO7iceJrw):

* Calculate the following: 
  + Logit=-8.87-.09\*PRICE+MB\*.07-.005\*RSIZE+1.55\*SIGMA-7.88\*EXRETAVG-2.27\*CASHMTA+1.6\*TLMTA-20.12\*NIMTAAVG
  + P=probability of failure=1/(1+exp-(logit))

Once you have calculated your P’s you are ready to predict which firms are likely to go bankrupt. So how might one use this information? Well, if you could predict which firms are going bankrupt–assuming the market hasn’t already priced in a bankruptcy–you might be able to make some money. Let’s see.

Here are results of sorting portfolios based on “P”  every January and holding stocks for one year.

[![](https://alphaarchitect.com/wp-content/uploads/2011/07/failure.png "failure")](https://alphaarchitect.com/wp-content/uploads/2011/07/failure.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Pretty wild, eh? Stocks with low probabilities of failure do well, but from a statistical standpoint, it is hard to say if there is any alpha. However, check out the high probability of default firms–wow–negative alphas galore!

We’re getting closer to affording our gold-plated Mercedes!

## **Investment Strategy**

Strategy 1:

1. Stop using Altman-Z to predict bankruptcy

Strategy 2:

1. Calculate logits using the estimates from table 2
2. Calculate the probability (P from above) of bankruptcy using the logit figures calculated in 1.
3. Go long low P firms, and WAY short high P firms.
4. Make money.

To juice up strategy 2:

1. Focus on distressed firms in the extreme growth and value categories (see below)

[![](https://alphaarchitect.com/wp-content/uploads/2011/07/1.png "1")](https://alphaarchitect.com/wp-content/uploads/2011/07/1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Commentary:**

I’ve been playing with the ‘financial quality’ variables for one of our in-house ‘value factor’ models recently (every quant shop has to have one, right?). I’ll admit it, we were using Altman-Z as a component of that variable, but after doing some research I’m sh&$canning Altman-Z and going test this model out instead. No disrespect to Prof. Altman, but when the evidence shows something works better, why not use it?

---

## Predicting Financial Distress and the Performance of Distressed Stocks

* John Y. Campbell, Jens Hilscher, and Jan Szilagyi
* A version of the paper can be found [here](https://disq.us/url?url=https%3A%2F%2Fdash.harvard.edu%2Fbitstream%2Fhandle%2F1%2F9887619%2Fjoim_predicting_financial_11.pdf%3Fsequence%3D2%3AHtcZsrANuwhCV141a8VdA-9tzxw&cuid=2945298). ([Here](https://scholar.harvard.edu/files/campbell/files/campbellhilscherszilagyi_jf2008.pdf) is the Journal of Finance version)

## **Abstract**

> In this paper we consider the measurement and pricing of distress risk. We present a model of corporate failure in which accounting and market-based measures forecast the likelihood of future financial distress. Our best model is more accurate than leading alternative measures of corporate failure risk. We then use our measure of financial distress to examine the performance of distressed stocks from 1981 to 2008.We find that distressed stocks have highly variable returns and high market betas and that they tend to underperform safe stocks by more at times of high market volatility and risk aversion. However, investors in distressed stocks have not been rewarded for bearing these risks. Instead, distressed stocks have had very low returns, both relative to the market and after adjusting for their high risk. The underperformance of distressed stocks is present in all size and value quintiles. It is lower for stocks with low analyst coverage and institutional holdings, which suggests that information or arbitrage-related frictions may be partly responsible for the underperformance of distressed stocks.

## **Data Sources**

The study covers the 1963-2008 time period. Data come from Compustat and CRSP. Data on failures come from [Kamakura Risk Information Services](http://www.kamakuraco.com/ProductsServices/KamakuraRiskInformationSvcs.aspx).

References[+]

References

|  |  |
| --- | --- |
| ↑1 | weighted average is represented by some silly a&\* equation meant to create confusion for the layman. |

 function footnote\_expand\_reference\_container\_1748\_120() { jQuery('#footnote\_references\_container\_1748\_120').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_1748\_120').text('−'); } function footnote\_collapse\_reference\_container\_1748\_120() { jQuery('#footnote\_references\_container\_1748\_120').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_1748\_120').text('+'); } function footnote\_expand\_collapse\_reference\_container\_1748\_120() { if (jQuery('#footnote\_references\_container\_1748\_120').is(':hidden')) { footnote\_expand\_reference\_container\_1748\_120(); } else { footnote\_collapse\_reference\_container\_1748\_120(); } } function footnote\_moveToReference\_1748\_120(p\_str\_TargetID) { footnote\_expand\_reference\_container\_1748\_120(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_1748\_120(p\_str\_TargetID) { footnote\_expand\_reference\_container\_1748\_120(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
