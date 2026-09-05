---
title: "Using Div Yield to Predict Returns: A lesson in Predictive Regressions"
slug: "using-div-yield-to-predict-returns-a-lesson-in-predictive-regressions"
date: "2014-07-11"
modified: "2022-05-03"
url: "https://alphaarchitect.com/using-div-yield-to-predict-returns-a-lesson-in-predictive-regressions/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Using Div Yield to Predict Returns: A lesson in Predictive Regressions

> Filip Lacerda and Pedro Santa-Clara have an interesting paper that investigates the use of dividend growth to predict future returns. Here is the abstract: The […]

Filip Lacerda and Pedro Santa-Clara have an [interesting paper](http://docentes.fe.unl.pt/~psc/ForecastingDividendGrowthToBetterPredictReturns.pdf) that investigates the use of dividend growth to predict future returns.  
Here is the abstract:

> The dividend-price ratio changes over time due to variation in expected returns and in forecasts of dividend growth. We adjust the dividend-price ratio to isolate the fluctuations that are due to variation in expected returns from those that are due to changing forecasts of dividend growth. This adjusted dividend-price ratio is statistically significant in predictive regressions and yields an in-sample R2 of 16.27% and an out-of-sample R2 of 12.35%, which compare with 7.88% and -2.94% for the unadjusted multiple. Structural estimation of our model obtains even higher measures of fit. Our results are robust across subsamples.

One of my students–Heng Qiao–took on a difficult project and replicated the results from the paper.

Here is Heng’s summary of his work:

> Out-of-sample R2, which is the ratio between the sum squared error of a “smart” model with that of a simple model (historical average forecasting), helps researchers identify if a model actually improves prediction.  This paper develops two new variables dpt and xt , which are the unadjusted dividend-price ratio and the adjusted dividend price ratio, respectively. In the paper, dpt and xt were created through a simple auto-regression, a first-order Taylor Expansion, and a simplification of infinite series. My work was aimed at replicating the paper’s results, and it turns out that there are slight differences between my result and that in the paper. Dealing with the monthly data, my work generated a R2 of 0.53% and R2OOS of 0.8% for dpt,  and a R2 of 0.49% and R2OOS of 0.78% for xt. When moved to the annual data, the results are more statistically significant, with R2 of 2.27% and R2OOS of 9.1% for dpt, and R2 of 20.31% and R2OOS of 20.31% for xt.

Below is a copy of the spreadsheet for your learning pleasure.  
——————–  
[predregression.xlsx](https://alphaarchitect.com/wp-content/uploads/2014/06/predregression.xlsx)  
——————-  
Here is a picture showing the forecast error using the simple dp\_t model in the paper (9.1% R2OOS):  
[![simple](https://alphaarchitect.com/wp-content/uploads/2014/06/simple.jpg)](https://alphaarchitect.com/wp-content/uploads/2014/06/simple.jpg)  
Here is a picture showing the forecast error using the more complex x\_t model in the paper (20.31% R2OOS):  
[![complex](https://alphaarchitect.com/wp-content/uploads/2014/06/complex.jpg)](https://alphaarchitect.com/wp-content/uploads/2014/06/complex.jpg)  
Based on the numbers, the fancy dividend prediction model does enhance the forecasting ability. Visually, as represented in the 2 charts above, there really isn’t much improvement in forecast errors over a simple average return prediction model…

**Predicting the stock market is probably the biggest sucker bet out there…**
