---
title: "Portfolio Rebalancing Research: Momentum and Tolerance Bands"
slug: "destabilizing-rebalancing"
date: "2017-05-31"
modified: "2017-05-31"
url: "https://alphaarchitect.com/destabilizing-rebalancing/"
categories: ["Uncategorized"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Portfolio Rebalancing Research: Momentum and Tolerance Bands

> If you are looking for research on stock selection, you’re in luck — the research is everywhere and has arguably been overdone. Get started with Moon […]

If you are looking for research on stock selection, you’re in luck — the research is everywhere and [has arguably been overdone](http://alphaarchitdev.wpengine.com/2017/03/03/evidence-based-investing-take-alpha-shove/). Get started with [Moon Cycles & Stock Market Returns](http://journals.sagepub.com/doi/abs/10.1177/0972652712473405) and [The Congressional Calendar & Stock Market Returns](https://www.unf.edu/~rlamb/Docs/FinServRev.pdf) to get a sense of how esoteric the research has gotten. Hundreds of these papers [have been covered](http://alphaarchitdev.wpengine.com/category/architect-academic-insights/) on the Alpha Architect blog and you could spend a lifetime trying to read all the research on the topic.

But one topic, that is arguably just as important as security selection,  has received very little attention: *rebalancing portfolios.*

In a [prior post,](http://alphaarchitdev.wpengine.com/2017/03/23/do-you-rebalance-your-portfolio-you-are-a-market-timer/) I highlighted an interesting new paper by Brian Baker, Mike Dieschbourg, Damian McIntyre and Arun Muralidhar (BDMM) published on the topic.  In addition to the BDMM paper, there have been some key research pieces published on the topic:

(1)

* [Vanguard](https://www.vanguard.com/pdf/icrpr.pdf) – This paper shows that calendar based rebalancing strategies don’t improve performance and that tolerance band rebalancing strategies tend to add minimum value.
* [TD Ameritrade published in Journal of Financial Planning](http://www.tdainstitutional.com/pdf/Opportunistic_Rebalancing_JFP2007_Daryanani.pdf) – This paper showed that rebalancing returns can be improved with 1) wider tolerance bands (20%) 2) Evaluating portfolios for rebalancing bi-weekly 3) Only rebalancing the asset(s) that is (are) out of balance and 4) Increasing the number of uncorrelated asset classes.
* [Michael Kitces](https://www.kitces.com/blog/best-opportunistic-rebalancing-frequency-time-horizons-vs-tolerance-band-thresholds/) – This post largely reinforces the TD Ameritrade Research and conclusions.

However, after reading these white papers and the BDMM paper there are some practical issues with these papers:

1. The TD Ameritrade paper and the BDMM paper use high frequency data (daily) and a short history (typically back to the mid 1990s).  The conclusion that tolerance bands are effective may be simply due to the the time period selected and may not be reflective of their superiority.
2. The Vanguard paper uses a much longer data history and monthly data frequency, but only uses tolerance bands of up to 10%, which are more narrow than the tolerance band range that was shown to be best in the TD Ameritrade paper (20% tolerance bands).

The rest of this post explores the prior research and I look at new ideas that might improve portfolio rebalancing techniques.

## How to Improve Portfolio Rebalancing Results

In addition to using/testing the conclusions of prior research, I wanted to see if I could improve upon the rebalancing results.  If you recall from my prior post, any decision to rebalance is an **ACTIVE, MARKET TIMING** decision…there, I said it. We are all market timers whether we’d like to admit it or not. Some of us will now choose to put our heads in the sand and pretend they didn’t read the last sentence, but for the rest of us looking to embrace the intellectual challenges markets throw our way — it’s time to get our hands dirty!

If we are going to improve on current rebalancing results, we will have to look to research that has shown some ability to provide positive market timing results.  In my mind, the most robust of these strategies are associated with trend following. Here are some pieces on the topic which highlight the depth of evidence on the subject:

* Wes’ [post](http://alphaarchitdev.wpengine.com/2015/08/13/avoiding-the-big-drawdown-downside-protection-investment-strategies/#gs.qANaZT8) on using trend following to avoid drawdowns.
* Meb Faber’s famous tactical allocation [paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461).
* Gary Antonacci’s [paper](http://www.optimalmomentum.com/RiskPremiaHarvesting.pdf) on dual momentum
* AQR on a [Century of Evidence on Trend Following](https://www.aqr.com/library/aqr-publications/a-century-of-evidence-on-trend-following-investing)

The list could go on, but the papers and posts, above, should provide a good starting place.

### Data Used

To test various rebalancing strategies, I use Ibbotson Associates monthly data from 1/1927 through 4/2017.  Specifically, I use Ibbotson Associates US Large-Cap Total Return series for US Stocks, Ibbotson Associates Intermediate-Term Government Bond Total Return series for bonds, and Ibbotson Associates 30 Day T-Bill Total Return series for cash.

For simplicity, I will only analyze a portfolio comprised of two assets, stocks and bonds.  To also keep the analysis simple, I will only look at one target asset allocation, 50% stocks and 50% bonds.

The benchmark portfolio will be a 50% stock and 50% bond portfolio rebalanced monthly.  This benchmark is chosen because it has the least variance in stock allocation over time, which should highlight any return improvement (or decrease) due to rebalancing decisions.

In addition, I ignore all transaction and tax costs.

### Testing the 20% Portfolio Rebalancing Tolerance Band

One of the first strategies that I wanted to test was the 20% tolerance band rebalancing approach but using a longer data history (1/1927 through 4/2017).  This tolerance band approach was shown to be optimal based on the TD study.

The specific rebalancing rules I tested were as follows:

1. Set the initial allocation to 50% stocks and 50% bonds on 1/1927.
2. As long as the stock allocation stayed between 40% and 60% at month end, no rebalancing trades were placed.
3. If at the end of any month the tolerance range was breached (either at an allocation of 60.01% and above or at an allocation of 39.99% and below), the portfolio was rebalanced back to the 50% stock and 50% bond target allocation.

The results of this strategy versus the benchmark monthly rebalanced portfolio are shown below:

![](https://alphaarchitect.com/wp-content/uploads/2017/05/20-Tolerance-Band-Results.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

What these results show are that 20% tolerance bands (when applied to a monthly frequency of reviewing potential rebalancing trades) does appear to improve the portfolio Compounded Average Growth Rate (CAGR) by about 0.24% per year as well as improve the Sharpe Ratio and a slightly reduce the maximum drawdown. However, the standard deviation of the portfolio and the sum of all drawdowns is increased.  This is expected as the portfolio allocation is allowed to drift more due to the tolerance bands. Of course, the most striking feature of the analysis is the # of trades: 1,084 versus 23. Clearly, the tolerance band approach is more efficient by minimizing the number of necessary trades.

### Momentum Informed Tolerance Band

The next rebalancing strategy I tested is one of my own design, which I call Momentum Informed Tolerance Band (“20% Tol, Mom” in the following tables).  The idea behind this rebalancing strategy is to use absolute momentum in stocks to help inform (i.e., market time) what half of the tolerance band the stock allocation should be in.

The specific rules are as follows:

1. If stocks have positive absolute momentum (stock returns are greater than cash returns over the prior 12 months), the stock allocation should be between 50% and 60% of the portfolio.  If it isn’t, the portfolio is rebalanced to either 50% (if under 50%) or 60% (if over 60%).  If the stock allocation is between 50% and 60% no rebalancing trades are placed.
2. If stocks have negative absolute momentum, the stock allocation should be between 40% and 50% of the portfolio.  If it isn’t, the portfolio is rebalanced to either 40% (if under 40%) or 50% (if over 50%).  If the stock allocation is between 40% and 50% no rebalancing trades are placed.

The results of this strategy (as well as previous ones) are shown in the table, below:

![](https://alphaarchitect.com/wp-content/uploads/2017/05/20-Tol-Mom.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The result of this rebalancing strategy is an improvement in CAGR above both the monthly rebalanced portfolio and the 20% tolerance band portfolio.  In addition, this strategy improves the Sharpe Ratio and decreases the maximum drawdown of the portfolio compared to both prior portfolios as well. This rebalancing strategy makes clear that being aware of momentum in stocks can provide a small but meaningful improvement in rebalancing results. The addition of momentum informed rebalancing does increase the total transactions relative to the 20% tolerance band approach but is still more efficient than the monthly rebalanced system.

### Let’s Go Crazy: Extreme Momentum Informed Tolerance Bands

The final rebalancing strategy I tested is another one of my own design (but it is very similar to other strategies), which I call Extreme Momentum Informed Tolerance Bands (or “20% Tol, Mom Extreme” in the tables, below).  The idea behind this strategy is to use absolute momentum in stocks to inform (i.e., market time) which extreme end of the tolerance band the stock allocation should be.  
Here are the rules:

1. If stocks have positive absolute momentum (stock returns are greater than cash returns over the prior 12 months), the stock allocation should be 60% of the portfolio.
2. If stocks have negative absolute momentum, the stock allocation should be 40% of the portfolio.

This strategy likely wouldn’t be implemented in this fashion as it would involve placing a rebalancing trade every month.  If one were serious about using a strategy similar to this I have a couple of ideas/comments:

1. Use some kind of trade buffer, i.e., if the actual stock allocation is within 2% or 5% (or whatever buffer you choose) of the target allocation then no trade is placed.  This would have the impact of reducing the number of trades required.
2. This rebalancing strategy is similar to using relative momentum on a monthly basis to allocate between two different asset allocation funds with a difference in stock allocations of 20% (examples being fixed allocation funds or target date retirement funds).

The results of this strategy (as well as previous ones) are shown in the table, below:

![](https://alphaarchitect.com/wp-content/uploads/2017/05/Extreme-20-Tol-Mom.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Here is a visualization of the same data:

![](https://alphaarchitect.com/wp-content/uploads/2017/05/Perf-Stats.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

These results show that using absolute momentum to be at one extreme of a tolerance band or the other provides a meaningful increase in CAGR and Sharpe Ratio over the benchmark portfolio as well as all the previous rebalancing strategies. This strategy doesn’t appear to have a meaningful change in either the maximum drawdown or sum of all drawdowns versus the prior “20% Tol, Mom” rebalancing strategy.  This would seem to indicate that the improvement in performance is due to better capturing some kind of momentum premium in the timing and amount of the rebalancing trades.

## Regression Analysis of the Portfolio Rebalancing Strategies Tested

In order to better understand what each of the previous rebalancing strategies is doing to improve risk-adjusted returns, we need to have some method of evaluating the performance.  The reason this might be important is that each rebalancing strategy has a different average stock allocation over time.  I have listed the average end-of-month stock allocation from 1/1927 through 4/2017 in the tables, above.  You can see from the table that each strategy had a successively slightly higher stock allocation.

*Is it possible that the improvement in performance is simply due to a higher than average stock allocation?*  
We can’t/shouldn’t create a benchmark for each rebalancing strategy that uses the rebalancing strategies average stock allocation and rebalance back to this target each month.  The reason for this is that we would be using ex-post allocation averages to compare to ex-ante performance.

Therefore, I use regression analysis to evaluate each rebalancing strategy.  Specifically, I did the following:

1. I took the return difference every month between each rebalancing strategy and the 50% stock and 50% bond monthly rebalanced portfolio (the benchmark).
2. There are only 4 possible ways that a rebalancing strategy can create excess returns
   1. Higher average stock allocation or exposure to the MKT factor
   2. Historically bought stocks low and sold them high or exposure to the value factor or HML
   3. Historically been able to capture some kind of momentum premium or has exposure to the UMD factor
   4. Actually generating some kind of alpha which means it should have a statistically significant intercept in the regression.
3. Therefore, I used the return stream created in item 1, above, and regressed each return stream against the MKT, HML & UMD factor return series.

The results from the regression analysis are below:

![](https://alphaarchitect.com/wp-content/uploads/2017/05/Regression-Results.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Here is a visualization of the same data:

![](https://alphaarchitect.com/wp-content/uploads/2017/05/Factor-Loadings.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

There are some very interesting things to note from the regression results:

* Even though each rebalancing strategy generated a return stream that exceed the monthly rebalanced benchmark portfolio, none of the rebalancing strategies generated a statistically significant intercept (alpha).  This means that all of the extra return can either be explained by the rebalancing strategies exposure to buying low and selling high (value or HML), use of momentum (UMD) or higher average stock exposure (MKT).
* Each rebalancing strategy generated some return from having higher stock exposure than the benchmark (i.e., all the MKT betas were statistically significantly greater than 0).
* Although each rebalancing strategy generated additional return from having a positive beta to MKT, the MKT betas were less than the difference in average stock exposure over time.  For example, the 20% Tolerance Band rebalancing strategy had an average stock exposure of 52.51% compared to the benchmark average of 50.10%.  This would lead me to believe that the regression analysis should have a .0241 (52.51% – 50.10%) beta to MKT.  However, the 20% Tolerance Band rebalancing strategy only has a .007 beta to MKT.
* All the strategies had a positive factor loading to HML (value) but the 20% Tolerance Band rebalancing strategy was the only one to have a statistically significant factor loading to HML.  This makes sense as it is the only strategy which is designed to systematically buy low and sell high.  I was surprised that the beta to HML was as low as it was at .008.
* All of the strategies had a positive and statistically significant factor loading to UMD (momentum).  However, each rebalancing strategy had a very different size beta to UMD.
* The 20% Tolerance Band rebalancing strategy had the smallest beta of .015 to UMD.  I was surprised that it this rebalancing strategy had a positive factor loading to UMD as this strategy could best be described as systematically buying low and selling high.  Perhaps the beta of a pure tolerance band rebalancing strategy to UMD is determined by the size of the tolerance band range (the small the the tolerance band the more beta to HML and the smaller the beta to UMD).
* The 20% Tol, Mom rebalancing strategy had a .042 beta to UMD which is expected given that this strategy explicitly uses momentum to help inform the portfolio about which half of the tolerance band to be in given the absolute momentum of stocks.
* The 20% Tol, Mom Extreme rebalancing strategy had the largest beta to UMD at .067.  This is also to be expected given that this strategy uses absolute momentum in stocks to make the biggest or smallest allocation it can inside of the tolerance band.

## Conclusion

The rebalancing strategy that one chooses to implement shouldn’t be taken for granted as any decision to rebalancing is an active market timing decision.  Knowing that a decision to rebalance is an active market timing decision, one can use prior research to help develop a rebalancing strategy to improve portfolio performance.  Using prior research on optimal rebalancing strategies (20% Tolerance Bands) and prior research on market timing strategies (trend following or absolute momentum) can create a rebalancing strategy that has historically improved results.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | Corey has a cool [piece on rebalancing](https://blog.thinknewfound.com/2017/05/big-little-details/) as well, but it is more related to rebalance timing |

 function footnote\_expand\_reference\_container\_28347\_43() { jQuery('#footnote\_references\_container\_28347\_43').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_28347\_43').text('−'); } function footnote\_collapse\_reference\_container\_28347\_43() { jQuery('#footnote\_references\_container\_28347\_43').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_28347\_43').text('+'); } function footnote\_expand\_collapse\_reference\_container\_28347\_43() { if (jQuery('#footnote\_references\_container\_28347\_43').is(':hidden')) { footnote\_expand\_reference\_container\_28347\_43(); } else { footnote\_collapse\_reference\_container\_28347\_43(); } } function footnote\_moveToReference\_28347\_43(p\_str\_TargetID) { footnote\_expand\_reference\_container\_28347\_43(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_28347\_43(p\_str\_TargetID) { footnote\_expand\_reference\_container\_28347\_43(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
