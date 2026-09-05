---
title: "Forecasting US Equity Market Returns with Machine Learning"
slug: "forecasting-us-equity-market-returns-using-machine-learning"
date: "2020-01-07"
modified: "2022-05-20"
url: "https://alphaarchitect.com/forecasting-us-equity-market-returns-using-machine-learning/"
categories: ["Research Insights", "AI and Machine Learning", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Forecasting US Equity Market Returns with Machine Learning

> Shiller’s CAPE ratio is a popular and useful metric for measuring whether stock prices are overvalued or undervalued relative to earnings. Recently, Vanguard analysts Haifeng […]

Shiller’s CAPE ratio is a popular and useful metric for measuring whether stock prices are overvalued or undervalued relative to earnings. Recently, Vanguard analysts Haifeng Wang, Harshdeep Singh Ahluwalia, Roger A. Aliaga-Díaz, and Joseph H. Davis have written a very interesting paper on forecasting equity returns using Shiller’s CAPE and machine learning: [“The Best of Both Worlds: Forecasting US Equity Market Returns using a Hybrid Machine Learning – Time Series Approach](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3497170)“.

First, what is the Shiller CAPE ratio?(1)

To calculate it we need the following:

* Take 10 years of trailing earnings
* Compute real earnings by adjusting the earnings for inflation to the current CPI price level
* Divide the current market cap of the stock (or index) by average annual real earnings

If we do a simple regression of Shiller’s CAPE ratio against future 10-year returns, we observe a very strong relationship.

![](https://alphaarchitect.com/wp-content/uploads/2019/12/Shiller-regression-nominal-800x494.png)

Source: [Improving U.S. stock return forecasts: A “fair-value” CAPE approach](https://www.valuewalk.com/wp-content/uploads/2017/07/SSRN-id2983860.pdf)

Here we see a historical chart of actual 10-year annualized stock returns vs. those predicted by Shiller’s CAPE. Using the Shiller regression, the current CAPE of about 30 suggests near-zero real return over the next 10 years.

![](https://alphaarchitect.com/wp-content/uploads/2019/12/Shiller-actual-v-forecast-800x486.png)

Source: [Improving U.S. stock return forecasts: A “fair-value” CAPE approach](https://www.valuewalk.com/wp-content/uploads/2017/07/SSRN-id2983860.pdf)

These charts are from the noteworthy 2018 paper “[Improving U.S. stock return forecasts: A “fair-value” CAPE approach](https://www.valuewalk.com/wp-content/uploads/2017/07/SSRN-id2983860.pdf)” by Vanguard analysts Joseph H. Davis, Roger Aliaga-Díaz, Harshdeep Ahluwalia, and Ravi Tolani, previously discussed on Alpha Architect [here](https://alphaarchitect.com/2018/08/03/a-qa-discussion-with-vanguard-researchers-on-the-fair-value-cape-ratio/). The first three authors also co-authored the 2019 machine learning paper.

As the authors discussed, the CAPE ratio has produced a worsening forecasting record in recent years. Since 1985, forecasts based on the Shiller CAPE regression have generated an RMSE of about 7.8%. That’s a large error in an annual return forecast, and forecasts have been consistently too low, as the CAPE has remained persistently high relative to its long-term average.

One criticism of CAPE is that reductions in real interest rates, if persistent, justify a higher P/E. Another is that changes in accounting standards and payouts v. buybacks require adjusting the CAPE model for consistency over time. Jeremy Siegel created [a reformulated CAPE which uses NIPA earnings instead of reported earnings](https://www.tandfonline.com/doi/abs/10.2469/faj.v72.n3.1).

Which brings us to the recent paper. First, the authors used a machine-learning approach to the original Shiller regression. Instead of the simple univariate regression, they added additional variables, tuned several machine learning models, and ensembled them.

The model form is as follows:

![R_{t+120} = f(CAPE_t, Y_t, CPI_t, SPVOL_t, BondVol_t, SVAR_t, TBL_t, DFY_t, DFR_t)](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-b4c74de2fa0727130d8887d77e104bdd_l3.png "Rendered by QuickLaTeX.com")

where

* CAPE is the cyclically adjusted price/earnings (P/E) ratio
* Y is Real 10-year bond yields, or nominal Treasury yield less an estimated 10-year expected inflation rate
* CPI is Year-over-year CPI inflation rate
* SPVol is the Realized S&P500 price volatility, over trailing 12 months
* BondVol is the Realized volatility of changes in our real bond yield series, over trailing 12 months
* SVAR is the stock variance computed as sum of squared daily returns on S&P 500
* TBL is the treasure bill rates
* DFY is the default yield spread computed as the difference between BAA- and AAArated corporate bond yields
* DFR is the default return spread, computed as the difference between the return on longterm corporate bonds and returns on the long-term government bonds

The CAPE response is modeled using these 8 predictors and 4 machine learning regression algorithms: Random Forest, Gradient Boost, Support Vector Machine and Gated Recurrent Unit (a form of [recurrent neural network](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)). Hyperparameters are chosen using time-based cross-validation, starting with the 1926-1959 period and walking forward one month at a time, and choosing the best-performing hyperparameters in the cross-validation set.

Individual ML algorithms displayed small to no advantage vs. the linear regression. An ensemble equal-weighting all the ML models obtained a noteworthy improvement in RMSE vs. a linear regression (4.7% RMSE vs 6.6%). GBM performed best. Boosting algorithms, such as XGBoost and LightGBM, are currently considered state-of-the-art for plain-vanilla tabular forecasting, as opposed to deep learning. While ensembling several algorithms increases the complexity of the forecasting process, it results in more accurate and robust predictions; Kaggle contests are generally won by ensembles, not single-algorithm forecasts.

![](https://alphaarchitect.com/wp-content/uploads/2019/12/Ensemble1-1-800x532.png)

Source: [The Best of Both Worlds: Forecasting US Equity Market Returns using a Hybrid Machine Learning – Time Series Approach](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3497170)

In a second machine learning experiment, the authors applied a 2-step forecasting process pioneered in the Vanguard 2018 paper, enhanced with machine learning.

In the 2018 Vanguard paper, a linear vector autoregression (VAR) was used. In the first step, the fair-value CAPE was estimated using a VAR model of five variables. Each month, each variable is modeled as a linear function of the values of these five variables for the 12 preceding months:

* CAPE real earnings yield, or 1/CAPE
* Real 10-year bond yields, or nominal Treasury yield less an estimated 10-year expected inflation rate
* Year-over-year CPI inflation rate
* Realized S&P 500 price volatility, over trailing 12 months
* Realized volatility of changes in a real bond yield series, over trailing 12 months.

The model can then be used to forecast a value the CAPE is expected to revert to over 10 years under VAR dynamics, such that the long-run CAPE is consistent with long-run relationships between the variables, and also recent levels of those variables.

In the second step, the authors back out the nominal (or real) equity market return implied by the CAPE forecast.

In the 2018 paper, the analysts found a notable improvement in the forecast using a linear VAR version of this methodology.

![](https://alphaarchitect.com/wp-content/uploads/2019/12/Shiller-VAR-800x491.png)

Source: [Improving U.S. stock return forecasts: A “fair-value” CAPE approach](https://www.valuewalk.com/wp-content/uploads/2017/07/SSRN-id2983860.pdf)

In the latest 2019 paper, the same 2-step process is used, but machine learning models are used instead of linear VAR.

Again, each machine learning model is tuned using walk-forward cross-validation to optimize the bias-variance tradeoff for best performance, and the models are ensembled.

![](https://alphaarchitect.com/wp-content/uploads/2019/12/Ensemble2-800x494.png)

Source: [The Best of Both Worlds: Forecasting US Equity Market Returns using a Hybrid Machine Learning – Time Series Approach](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3497170)

A better forecast (2.6% RMSE) was obtained vs. the linear VAR (3.8% RMSE), which in turn was significantly superior to a linear Shiller regression (6.6% RMSE).

By any measure, the current CAPE of over 30 is elevated and points to sub-par future returns, but the more complex models point to moderate returns as opposed to near-zero real returns.

## Conclusion

This paper is a great example of applying machine learning to improve forecasting. Machine learning tends to need a lot of data, but even on monthly data, we see a potentially useful result.

Machine learning is a highly empirical paradigm with no priors on the functional form. Instead of assuming a linear relationship, we can allow the algorithm to find a highly nonlinear model.

In any scientific endeavor, there is a tension between theory and experiment. If you don’t check a theory against real-world data, it’s unlikely to be very good. But if all you do is predict according to past data, without deep theoretical understanding, then as soon as you encounter a future unlike the past, your model is likely to fail.

Machine learning leans toward the latter approach, in that it does not have a strong prior on the functional form of the model relationships. Machine learning models can be sensitive to small departures from past experience. Sometimes the result is a brittle model, for instance, vulnerability to [adversarial attacks](https://openai.com/blog/adversarial-example-research/). In this context of financial modeling, if we get data we haven’t seen in the past, e.g. negative rates, it’s hard to say what the forecast dynamics are going to be using machine learning to forecast the CAPE. Additionally, the complexity of machine learning models can make them hard to interpret.

I like to say that machine learning is statistics for street-fighting. With simple linear models, sometimes you don’t get great results, but you know why: your model doesn’t capture everything, and your data doesn’t perfectly fit the assumptions of normality, etc. With machine learning, sometimes you get better results, but you’re not always sure why: it can be hard to understand exactly what the model is doing.

If you have good data, machine learning forecasting usually just works better in practice. And this paper is a great example of using machine learning models to improve outcomes on a finance problem with important practical implications.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | [Here is a post.](https://alphaarchitect.com/2011/10/06/the-shiller-pe-ratio/) |

 function footnote\_expand\_reference\_container\_53764\_45() { jQuery('#footnote\_references\_container\_53764\_45').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_53764\_45').text('−'); } function footnote\_collapse\_reference\_container\_53764\_45() { jQuery('#footnote\_references\_container\_53764\_45').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_53764\_45').text('+'); } function footnote\_expand\_collapse\_reference\_container\_53764\_45() { if (jQuery('#footnote\_references\_container\_53764\_45').is(':hidden')) { footnote\_expand\_reference\_container\_53764\_45(); } else { footnote\_collapse\_reference\_container\_53764\_45(); } } function footnote\_moveToReference\_53764\_45(p\_str\_TargetID) { footnote\_expand\_reference\_container\_53764\_45(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_53764\_45(p\_str\_TargetID) { footnote\_expand\_reference\_container\_53764\_45(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
