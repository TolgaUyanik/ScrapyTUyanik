---
title: "Interest Rates, Tax-Selling, and Stock Return Seasonality"
slug: "interest-rates-tax-selling-stock-return-seasonality"
date: "2016-01-08"
modified: "2023-08-17"
url: "https://alphaarchitect.com/interest-rates-tax-selling-stock-return-seasonality/"
categories: ["Seasonality", "Uncategorized"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Interest Rates, Tax-Selling, and Stock Return Seasonality

> Stock prices under pressure: How tax and interest rates drive seasonal variation in expected returns Kang, Pekkala, and et al. A version of the paper […]

### Stock prices under pressure: How tax and interest rates drive seasonal variation in expected returns

* Kang, Pekkala, and et al.
* A version of the paper can be found [here](http://personal.lse.ac.uk/polk/research/tax20150214.pdf).
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category](https://alphaarchitect.com/category/academic-research/).

### Abstract:

> We show that **interest rates drive mispricing at the turn of a tax period** as investors face the trade-off between selling a temporarily-depressed stock this period and selling next period at fundamental value, but with tax implications delayed accordingly. We confirm these patterns in US returns, volume, and individual selling behavior as well as in UK data where tax and calendar years differ. At quarter-end, the trade-off is only present following recessions, consistent with the tax code. We then link a significant portion of the variation in the risks and abnormal returns of size, value, and momentum to tax-motivated trading.

### Alpha Highlight:

Previous research has argued that tax-motivated trading at the turn of the year drives return seasonality and the January effect ([Sias 2007](https://alphaarchitect.com/2015/11/30/momentum-seasonality/)). In December, investors sell losers to realize embedded tax losses, and then when selling pressure recedes in January, prices of these stocks rebound. The amount of this rebound varies with the size of the embedded capital gain, or the “overhang.” This paper hypothesizes that for a given level of capital gains overhang, stock return  seasonality should depend on **both capital gains tax rates and on interest rates.**

The paper includes a good example that clarifies the intuition behind the analysis:

> 1. Consider a US investor who is in the 15% capital gains tax bracket;
> 2. The investor bought a stock at $100 several years ago;
> 3. Currently the stock is trading at $4.

**Option 1:**Sell the stock at $4 on 12/31 –>This would generate a capital loss of $96 and offer a tax deduction of $14.40 (15%\*$96). Thus, the total present value is $18.40 ($4+$14.40.)

**Option 2:**Wait to sell the stock on 1/1 –> The tax benefit won’t occur until one year later and thus must be discounted by the appropriate one-year interest rate. Assuming the interest rate is 5%, and the total PV (present value) of the tax benefit one year later is $17.71 ($4+$15%\*96/1.05).  
Thus, waiting until 1/1 to sell the stock results in a PV loss of $0.69, as compared with selling it at 12/31. This example illustrates that the time value of money impact of tax-motivated selling, but critically it also depends on the level of interest rates! Recall the opportunity cost of not earning 5% interest on the tax savings.

In the above example, what’s the price that would make the investor **indifferent** between selling in 12/31 versus 1/1? To be indifferent, the present value of selling today must equal the present value of selling next year. The following equation allows us to answer this question: P-15%\*(P-$100) = $4-15%\*($4-$100)/1.05.  Solving for P in this equation yields $3.19.

Thus, for a rational investor:

* Below $3.19, he would delay selling the stock;
* At $3.19, he would be indifferent;
* Above $3.19, he would sell now rather than waiting.

This time-series variation of the tax benefit was ignored in previous literature and the authors devise a novel empirical prediction:  “As interest rates rise, our formulation predicts that the January effect should reappear.”

### Conclusion:

We are huge believers in [tax minimization](https://alphaarchitect.com/2014/12/09/etf-vs-mutual-fund-tax-efficiency-education/) and tax consequences influence our decision-making. As this paper highlights, many other professionals are concerned about the same thing and this creates predictable seasonality effects. What is interesting and unique about this paper is how the authors map the size of the tax-related seasonality to interest rates, or opportunity cost of capital. Interesting stuff for the geeks in the crowd.
