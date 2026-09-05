---
title: "Labor Unions are Hazardous to Your Wealth!"
slug: "labor-unions-are-hazardous-to-your-wealth"
date: "2011-02-26"
modified: "2022-06-04"
url: "https://alphaarchitect.com/labor-unions-are-hazardous-to-your-wealth/"
categories: ["Research Insights"]
tags: ["abnormal returns", "Unions", "Long-Run Impact"]
best_of: false
source: "alphaarchitect.com"
---

# Labor Unions are Hazardous to Your Wealth!

> Long-Run Impacts of Unions on Firms: New Evidence from Financial Markets, 1961-1999 David S. Lee & Alexandre Mas A version of the paper can be […]

### Long-Run Impacts of Unions on Firms: New Evidence from Financial Markets, 1961-1999

* David S. Lee & Alexandre Mas
* A version of the paper can be found [here](http://www.princeton.edu/~ceps/workingpapers/182lee.pdf).
* Lots of cool background research can be found [here](http://finance.sauder.ubc.ca/~ortizmolina/).

### **Abstract:**

> We estimate the effect of new unionization on firms’ equity value over the 1961-1999 period using a newly assembled sample of National Labor Relations Board (NLRB) representation elections matched to stock market data. Event-study estimates show an average union effect on the equity value of the firm equivalent to a cost of at least $40,500 per unionized worker. At the same time, point estimates from a regression-discontinuity design—comparing the stock market impact of close union election wins to close losses—are considerably smaller and close to zero. We find a negative relationship between the cumulative abnormal returns and the vote share in support of the union, allowing us to reconcile these seemingly contradictory findings. Using the magnitudes from the analysis, we calibrate a structural “median voter” model of endogenous union determination in order to conduct counterfactual policy simulations of policies that would marginally increase the ease of unionization.

### **Data Sources:**

This paper collects the election results data on all firms with [NLRB](http://www.nlrb.gov/) union representation elections between 1961-1999. Stock prices and fundamental data are collected from CRSP/Compustat.

### **Discussion:**

Labor unions have created quite a stir recently. As firm believers in competitive free markets, you won’t find us promoting union causes. There is certainly a reasonable argument to be made that unions in the context of *private* markets may be socially optimal, however, I cannot think of a sensible argument why unions are needed in the public sphere.

Public employee unions create an extreme [agency](http://en.wikipedia.org/wiki/Principal-agent_problem) problem–the union members have a capability to vote into office the very people with whom they bargain…Huh? To make matters worse, the better the union bargains the more money it has to support those candidates that it will be bargaining with. This leads to a perverse cycle of win-win for public union and elected official. The cost is a huge LOSE-LOSE for the taxpayer. Any public union employee cannot logically support public unions and simultaneously NOT support a large corporation’s right to buy votes in Washington and setup sweetheart deals. In both cases, the system creates a huge agency problem that is simply wrong. End the public employee unions and end the lobby problem in Washington–we’ll all be better off.

An alternative way of looking at unions is as a monopolist provider of a good. In this case, that good is a specific type of labor (e.g. all the teachers in a state). Economists have determined that monopolies are bad for consumers, so why is labor different? The union and unionized/employed worker is obviously better off (getting all those nice monopoly benefits) but the whole pie for society is smaller. (Boy, this sounds like one of those crazy [Chicago economists](http://www.goodreads.com/quotes/show/69390)‘ arguments. Sure glad we aren’t affiliated with any of those jokers.)

But who cares about the unions anyway? **This is a blog about figuring out how to make money.**  
Fortunately for Empirical Finance Blog*™* readers, we’ve dug up an interesting paper that looks at how labor unions affect investment returns. The basic idea of the paper is to test exactly how unions affect stock prices. One argument is that unions are bad for businesses: for example, [this paper](http://finance.sauder.ubc.ca/~ortizmolina/unions_icoe.pdf), which finds that labor unions threaten future profitability, lower operating flexibility, and raise the cost of equity. Another argument might suggest that unionization would have little effect on a firm, because union bosses are rational enough to understand that the NPV of their members’ wages are actually lower if they screw over the company, forcing it into bankruptcy or a non-competitive position. This, of course, assumes union bosses have incentives aligned with those of their constituents.

In the end, how unions affect stock prices is an empirical question: Does the market fully discount the expected negative effects associated with a union? Or perhaps the market prices the bad news appropriately? Or maybe the market doesn’t react at all because unions have no negative effects?  
To kick the paper off the authors present an anecdotal example of how unions affect future stock returns:

![](https://alphaarchitect.com/wp-content/uploads/2011/02/Untitled8.png "Untitled")

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The figure shows NLS stock before the union election, and after the union election. Before the election, NLS held its own against the broad market index; afterwards it took a beating. A keen empirical observer would immediately note that there could be any number of reasons for NLS’ underperformance that is unrelated to the union vote (perhaps company strategy/management changed, it was a turning point in the industry, the broad market return is not a proper benchmark, etc.). The rest of the paper is dedicated to digging deeper into the “union underperformance” anomaly to see if the market is systematically unable to efficiently price the bad news associated with unions and firm performance.

We recommend everyone actually read the source document, since there are a ton of interesting results and discussions in the paper. Also, as a caveat, it is incredibly difficult to control for every imaginable variable, and due to the “hot” nature of the topic, one can surely poke holes in the analysis if they desire. But we don’t care about the politics as much as we care about how the results relate to portfolio strategy, investment, and creating wealth.

Table 2 highlights the 24 month CARs associated with a strategy that goes long firms with a publically announced union victory. **Not** a recommended strategy unless you want to lose around 10% a year to the benchmark (the authors provide 3 benchmark variations).

[![](https://alphaarchitect.com/wp-content/uploads/2011/02/Untitled9.png "Untitled")](https://alphaarchitect.com/about/team/cliff/184-revision-16/)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Next up, calendar-time portfolio analysis. If you are unfamiliar with this sort of portfolio construction stay-tuned for our future series called “Empirical Finance Boot Camp*™.*” Until then, imagine a calendar-time portfolio as a strategy that invests in all ‘event’ firms over time in a rolling, monthly rebalanced fashion (note: one could rebalance however they choose). The nice thing about calendar-time tests is that they don’t suffer from “cross-sectionally correlated abnormal returns.”

What the F&\*% is that you may ask?

Well, if you look at Table 2, all the authors are really doing is looking at every single event firm (a firm that endures a union victory) throughout time, assuming they are independent events, figuring out their abnormal returns relative to a benchmark, and presenting the averages/p-values. However, one can imagine a situation where there was one outlying year where all the union-victory firms went to the dogs and lost -100% (perhaps it wasn’t even union related, but something specific to that set of firms that the benchmark returns couldn’t capture). Now, it also may be the case that for the remaining years the performance was roughly flat. If we just look at the averages from Table 2, we may think that the strategy of shorting firms with recent union victories would be a great idea, when the reality is that there just happened to be one time period when it was good. And to make matters worse, when we calculate the standard deviation of the average, we are going to consider all the observations as independent observations, when in reality the group of -100% observations are really one “big” observation of the same thing!  So to make a long story short and to end the boredom, the bottom line is the stats may be screwed up if we use the technique in Table 2.

The beauty of using calendar-time portfolios to test performance is that they don’t suffer from this ‘one-hit wonder’ syndrome, since the CT portfolios capture the performance and cross-sectional correlation of a portfolio of event firms throughout time. So check out the results:

[![](https://alphaarchitect.com/wp-content/uploads/2011/02/Untitled12.png "Untitled")](https://alphaarchitect.com/about/team/wes/181-revision-28/)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The firms that have a union win earn monthly 3-factor alphas in the -50bp, range–roughly 6% a year underperformance, yuck!

To wrap up, here is a picture of the results from Table 2 for the “quantitatively challenged”. As the figure shows, union-victory firms underperform a benchmark by nearly 10% after the first year.

[![](https://alphaarchitect.com/wp-content/uploads/2011/02/Untitled11.png "Untitled")](https://alphaarchitect.com/about/team/wes/181-revision-27/)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Investment Strategy:**

1. Find out what the NLRB board has to say about a union, and/or maintain a live database like [we](http://www.empiricalfinancellc.com/) do.
2. Sell stocks that you own when they encounter a union-victory, and/or short stocks that have a union-victory and use it as part of your “short book.”
3. Wait for the bad news about efficiency, operations, productivity, etc. to make its way through the company and onto the front steps of Wall Street analysts.
4. Make money when everyone finds out what you already know–unions kill business. Estimates range from 6-10% a year in “alpha” relative to a benchmark.

### **Commentary:**

Actually implementing this strategy in a quant context may not be the best way to go on this “anomaly.” That said, it’s certainly not a bad way to find good “short candidates” for value investors who are always looking to balance their long book.

A better takeaway from this research is to put it in your “rule of thumb” basket along with other favorite trading rules like, “Never buy a lawsuit,” or “Sell in May and go away.”

And I would like to reiterate, we are not “anti-union,” per se, we are simply “anti-losing money,” and anti-bad economics. Shame on us for being greedy free-market loving capitalists that proudly welcome the challenge and benefits of fairly competing in a world full of “softies.”
