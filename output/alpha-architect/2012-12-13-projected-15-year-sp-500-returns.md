---
title: "Projected 15-year S&P 500 Returns"
slug: "projected-15-year-sp-500-returns"
date: "2012-12-13"
modified: "2022-06-02"
url: "https://alphaarchitect.com/projected-15-year-sp-500-returns/"
categories: ["Research Insights", "Macroeconomics Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Projected 15-year S&P 500 Returns

> Prediction stock market returns–a fascinating concept. A true magical talent. Of course, we’ve put some of our brainpower (a limited resource!) on the subject […]

Prediction stock market returns–a fascinating concept. A true magical talent.

Of course, we’ve put some of our brainpower (a limited resource!) on the subject and come up with a few observations on the subject:

* <https://alphaarchitect.com/2012/11/predicted-10-year-returns-from-the-shiller-pe/>
* <https://alphaarchitect.com/2011/11/long-term-market-return-projections/>
* <https://alphaarchitect.com/2011/10/the-shiller-pe-ratio/>

The original gangster of predicting future market returns is Jeremy Grantham.

Here is a recent piece he has on GDP growth:

* <http://www.gmo.com/websitecontent/JG_LetterALL_11-12.pdf>

Grantham proposes some serious sluggishness–looking at GDP growth in the 1-2% category

[![](https://alphaarchitect.com/wp-content/uploads/2012/12/JG_OntheRoadtoZeroGrowth_11-12.png "JG_OntheRoadtoZeroGrowth_11-12")](https://alphaarchitect.com/wp-content/uploads/2012/12/JG_OntheRoadtoZeroGrowth_11-12.png)

### Why is understanding GDP growth important?

First, you gotta read Buffett’s classic piece from 1999:  
<http://money.cnn.com/magazines/fortune/fortune_archive/1999/11/22/269071/>

Buffett highlights the inextricable tie between GDP growth and corporate profits. GDP growth is the limiting factor (interest rates and margins are the other factors).

Let’s step back a moment…

Review the following equation from [John Hussman](http://hussmanfunds.com/wmc/wmc050222.htm):

> **LT Total Return = (1+g)(future PE / current PE)^(1/T) – 1** **+ dividend yield(current PE / future PE + 1) / 2**

What are the true unknowns in this equation?

* g, peak to peak earnings growth
* future PE, what you’ll cash out at in the future

g represents the growth of earnings for all firms in the economy (or for our purposes, the S&P 500).

Fundamentally, what drives g?

Revenue growth and corporate profit margins.

Here are some scenarios to think about:

* high sales and margin decompression==>Good
* high sales and margin compression==>Ambiguous outcome
* low sales and margin decompression==>Ambiguous outcome
* low sales and margin compression==>Bad

Back to GDP growth and why it is important. Pushing aside nuance, revenue growth for firms in the economy can’t exceed “revenue growth” of the economy. Assuming profit margins stay the same, earnings growth will roughly increase with nominal GDP. If nominal GDP grows at 6% for the next 50 years, nominal earnings can be expected to grow ~6% over time, assuming profit margins stay at roughly the same level.

### Why is understanding Margin dynamics important?

Thanks to competition, margins are highly mean-reverting. When profits are getting real juicy, capital flies to the rescue to push returns down; when profits are in the outhouse, capital fleas in the other direction and returns slowly creep higher.

Margins matter because they determine earnings growth in the future. A raging GDP growth rate–high top line growth for firms–can be completely offset by a major compression in profit margins. Similarly, a tragic GDP growth (as proposed by Gangsta Grantham) may not be a major issue if margins move higher.

### Modeling it all out

In times of confusion, a model is needed.

We build a simulation model that assumes the following:

* profit margins mean revert: <http://www.puc-rio.br/marco.ind/sim_stoc_proc.html>
* P/E ratios mean revert: <http://www.puc-rio.br/marco.ind/sim_stoc_proc.html>
* GDP growth follows a random drift model: [http://homepages.strath.ac.uk/~hbs96127/mlecture11.ppt](http://www.puc-rio.br/marco.ind/sim_stoc_proc.html)

We also start off with the following parameters:

* profit margins are currently @ 13.68%, with LT average of 10.85%
* GDP growth hits Grantham’s 1.4% bogey, plus 3% inflation
* Current P/E of 15, with LT average of 16.5
* Current Div Yield of 2.21%

In summary, you’ve got slow projected top-line (bad), margin compression (bad), but you’re buying the market relatively cheap (good).

And here is what pops out of the model factory:

First, an example of what the models are doing:

[![](https://alphaarchitect.com/wp-content/uploads/2012/12/Microsoft-Excel-Macro-Model_v03.png "Microsoft Excel - Macro Model_v03")](https://alphaarchitect.com/wp-content/uploads/2012/12/Microsoft-Excel-Macro-Model_v03.png)  
This is one run of the 15 year simulation. You’ll notice 3 things:

1. Profit margins mean revert to the historical average
2. GDP grows, but not in a straight line
3. Earnings grow, but the growth trajectory depends on the mix of GDP growth and margin dynamics.

And here is what you get when you run the model simulation 1000 times:

[![](https://alphaarchitect.com/wp-content/uploads/2012/12/Microsoft-Excel-Macro-Model_v05.png "Microsoft Excel - Macro Model_v05")](https://alphaarchitect.com/wp-content/uploads/2012/12/Microsoft-Excel-Macro-Model_v05.png)  
A range or 2-8% nominal S&P 500 CAGRs over the next 15 years.

Here is a figure that simply uses the Hussman model framework using different future P/E assumptions and an assumed growth rate of 5 (%2 growth, 3% inflation):

[![](https://alphaarchitect.com/wp-content/uploads/2012/12/Microsoft-Excel-Macro-Model_v04.png "Microsoft Excel - Macro Model_v04")](https://alphaarchitect.com/wp-content/uploads/2012/12/Microsoft-Excel-Macro-Model_v04.png)  
At the mean historical P/E we’re looking at ~8% nominal; at the min historical p/e ~3%; at the max historical p/e ~12%. These projections are noticeably higher than what we find in the simulation study–primarily due to an inability for the simple model to incorporate margin mean-reversion.

### Summing it all up

Over the next 15 years you could probably see 2% to 8% CAGRs, and will most likely see something in the range of 5-6% nominal. Rip out some inflation and you’ll notice these aren’t returns to write home about. Of course, relative to the alternatives, a 2-3% real return might be the best think going.
