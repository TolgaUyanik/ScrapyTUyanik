---
title: "Fixed Income Factors: An Overlooked Corner of the Market"
slug: "fixed-income-factors-an-overlooked-corner-of-the-market"
date: "2018-10-09"
modified: "2018-10-09"
url: "https://alphaarchitect.com/fixed-income-factors-an-overlooked-corner-of-the-market/"
categories: ["Research Insights", "Factor Investing", "Guest Posts", "Fixed Income"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Fixed Income Factors: An Overlooked Corner of the Market

> Factors, or “style” investing, seems to be all the rage these days, including the use of factors in fixed income (here, here and here are good […]

Factors, or “style” investing, seems to be all the rage these days, including the use of factors in fixed income ([here](/2018/02/02/factors-in-fixed-income/), [here](https://www.aqr.com/Insights/Research/Alternative-Thinking/Style-Investing-in-Fixed-Income) and [here](https://www.robeco.com/en/insights/2018/05/graham-and-dodd-award-puts-robecos-research-on-credit-factor-investing-in-the-spotlight.html) are good places to start). However, many of these strategies focus on CUSIP level bond selection.  This means executing a strategy with a fair amount of turnover in a bond market that can (at times) be illiquid and expensive to trade.  Sadly, this means that fixed-income factors are likely out of reach for most individual investors.

But who cares about factors in fixed income, most active bond managers beat the benchmark anyway, *right?*

Well, not so fast…Dr. Asness points out in a recent [post](https://www.aqr.com/Insights/Perspectives/Fixed-Income-Fantasies), that, yes, active managers beat the index but they do it while taking on more credit risk than the benchmark.

## So what’s the big deal? Active Bond Managers Beat the Index, Right?

The issue, as Dr. Asness points out, is that credit risk and equity risk are very correlated so beating the bond benchmark while taking more credit risk looks good on paper, but when viewed from the perspective of a portfolio, it is destroying some of the diversification benefits that bonds provide.  To drill into more detail, let’s look at a couple of the conclusions from the [paper](https://images.aqr.com/-/media/AQR/Documents/Insights/Alternative-Thinking/Alternative-Thinking-Style-Investing-in-Fixed-Income.pdf), “The Illusion of Active Fixed Income Diversification:”

![](https://alphaarchitect.com/wp-content/uploads/2018/07/Illusion-of-Fixed-Income-800x521.jpg)  
This is where the benefit of factors in fixed income can shine – they provide an opportunity to add sources of returns to a portfolio, but do so in a way that adds to the diversification of a portfolio not by doubling down on the same risk (equity or credit risk).  The challenge for individual investors is how to add styles in their fixed income portfolio without CUSIP level selection (which could be problematic given illiquidity and trading costs).

## Sell Vol ‘Til You Ball

One of the oldest (and I would argue least appreciated) factor/style is volatility selling.  I discuss the concept in the equity market [here](http://alphaarchitdev.wpengine.com/2017/08/08/volatility-premium-covered-call-selling-and-knowing-what-you-own/).  However, one of the oldest fixed income asset classes also involves volatility selling – mortgage bonds.

Mortgage bonds are implicitly short interest rate volatility because most mortgages allow the borrower to prepay the mortgage at any time without penalty (i.e., they have sold a call option to the borrower).  In return for giving the borrower the right to prepay at any time without penalty, mortgages typically charge a higher interest rate than a U.S. Treasury bond of similar duration (they earn a premium).  In this way, owning a mortgage bond (or mortgage bond fund) is similar to a call writing strategy on equity markets.

To see if selling this option (owning mortgage bonds) provides a historical premium we can use regression analysis.  I have used the PortfolioVisualizer.com factor regression tool, below, to analyze the return of the Vanguard GNMA fund (GNMA mortgage bond principal is guaranteed by the U.S. Government), below:

![](https://alphaarchitect.com/wp-content/uploads/2018/07/VFIIX-800x408.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

As you can see from the regression, above, the Vanguard GNMA fund has a factor loading of 0.18 to changes in interest rates (20-year interest rates) and a 0.06 beta loading to credit risk.  In addition, it has a statistically significant alpha of 1.5% per year.  In this example, one could argue that the alpha is not manager skill, it is the result of having a misspecified regression analysis because there isn’t a factor in the regression for volatility selling (if a factor for volatility selling were added, it would likely show a sensitivity of close to 1.0 for that factor and an alpha of about 0%).

However, the fact that this index has an alpha is a benefit we can utilize to help potentially provide index-beating returns without doubling-down on credit/equity risk.

## Know Your Foe

In order to construct a portfolio designed to beat a fixed income benchmark without taking more credit risk, we have to understand the index portfolio composition or factors.  In recent history, the Vanguard Total Bond Market Index fund has been composed of approximately 1/3 US Treasuries (of various maturities), 1/3 corporate bonds and 1/3 mortgage bonds (however, this hasn’t always been the case as, at times, the total bond market index looked more like a corporate bond index).

If we were to do a regression analysis on the Vanguard Total Bond Market Index fund, it would look like the following:

![](https://alphaarchitect.com/wp-content/uploads/2018/07/VBMFX-800x386.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

What this shows is that the index has approximately 50% more interest rate risk than the mortgage bond index (0.30 vs. 0.18 loading to interest rates) and about triple the credit risk (0.17 vs. 0.06 loading to interest rates).  In addition, the total bond market index also has about half the alpha of the mortgage bond index (0.67% vs. 1.5%) as the total bond market index has less mortgage bond exposure.

With this information, we know that if we can increase the dollar exposure to mortgage bonds (while keeping the interest rate and credit exposure approximately equal to the index), we should see a portfolio that behaves similarly to the total bond market index (i.e., keeps the diversification benefit) but with a chance of outperformance (due to having more exposure to volatility selling).

## Eating Our Pudding

As they say, the proof of the pudding is in the eating…so let’s test our thesis and see if it works.

Below, I create a portfolio composed of 80% Vanguard GNMA fund (more allocation than the total bond market index, which should provide the factor/return which is uncorrelated to equities), 10% Vanguard High Yield Corporate fund (increase the credit exposure back to index levels) and 10% Vanguard Long-Term Treasury fund (increase the interest rate exposure back to index levels).

I show the back-tested results, below:

![](https://alphaarchitect.com/wp-content/uploads/2018/07/Portfolio-800x394.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

What we see is that the results are what we would have expected.  The portfolio (blue line) has performance that, over the time period studied, has exceeded the total bond market index.  Interestingly, it provides this excess performance without taking on more risk (the standard deviations of the portfolio are nearly identical at 3.79% for the portfolio vs. 3.82% for the index) and the correlation to the US equity markets hasn’t changed materially either (0.11 for the portfolio vs. 0.07 for the total bond market index).

## Conclusion

This portfolio isn’t a recommendation for what anyone should be doing in the bond portion of portfolios.  It is hopefully a call to think more critically about what you own in the bond portion of your portfolio, especially active fixed income managers because the outperformance of active fixed income managers seems to be appealing on the surface, but when one understands how they generate the outperformance (taking more credit risk) the benefits of their outperformance become debatable.

Factors in fixed income (value, momentum, carry, defensive) offer some hope for outperformance uncorrelated to equity markets, but they too come with some issues (CUSIP selection and turnover) that might make the factors tough for individual investors to harvest.

This article studies using volatility selling in fixed income markets (mortgage bonds) along with different forms of leverage (high yield bonds and long-term US Treasuries) to bring interest rate and credit risk factor exposures back up to index levels.  The results seem interesting and will hopefully provoke you to consider the factors you are including in your bond portfolio.
