---
title: "Absolute Momentum and Stock Momentum Strategies: Friends, not enemies"
slug: "absolute-momentum-and-stock-momentum-strategies-friends-not-enemies"
date: "2015-03-31"
modified: "2022-05-30"
url: "https://alphaarchitect.com/absolute-momentum-and-stock-momentum-strategies-friends-not-enemies/"
categories: ["Momentum Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Absolute Momentum and Stock Momentum Strategies: Friends, not enemies

> There is sometimes confusion associated with so-called “momentum” strategies–we want to clear the muddy waters. We break momentum into two categories to differentiate between the different […]

There is sometimes confusion associated with so-called “momentum” strategies–we want to clear the muddy waters. We break momentum into two categories to differentiate between the different approaches to momentum:

(1) **Absolute, or [time-series momentum](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2089463):** an asset classes’ own past return, considered independently from the returns of other asset classes, predicts its future performance. This could apply at the level of individual securities as well.

(2) **Relative Strength, “Stock momentum,” or [Cross-sectional momentum](http://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf)**: an asset classes’ performance, relative to other asset classes, predicts its future relative performance. This could also apply at the individual security level, when performance is compared versus the performance of comparable securities; thus, the term is not exclusive to “asset classes.”

This post highlights two facts found in the data:

1. Individual stock momentum has worked over the past 87 years. This is commonly labeled ***cross-sectional momentum***and is often used in momentum investing funds and/or ETFs.
2. Using a simple absolute return (i.e., time-series) signal, appears to limit drawdowns over the past 87 years. This is commonly referred to as ***time-series momentum*** and is often used as a risk-management overlay in tactical asset allocation systems.

We hope to educate everyone on the difference between the two ideas, and show that they are not competitors, but can be used in conjunction with one another.

## Cross-sectional Momentum

Cross-sectional momentum, at the individual stock level, is a technique to sort stocks based on some measure of past return. Most momentum-based ETFs or mutual funds trade based on this general approach.

At a high level, for individual stocks, cross-sectional momentum results can be summarized as follows:

* [Short-term](https://alphaarchitect.com//2015/01/14/quantitative-momentum-research-short-term-return-reversal/#.VRG_7I54rKM) (1-month look-back measurement, 1-month holding period) shows reversals
* [Intermediate-term](https://alphaarchitect.com//2015/01/06/quantitative-momentum-research-intermediate-term-momentum/#.VRG_7Y54rKM) (6 to 12-month look-back measurement, 1 to 12 month holding periods) shows continuation
* [Long-term](https://alphaarchitect.com//2015/01/09/quantitative-momentum-research-long-term-return-reversal/#.VRG_iY54rKM) (36-month look-back measurement, 3-year holding period) shows reversal.

Below we  document the intermediate-term momentum effect using Ken French’s [data.](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/det_10_port_form_pr_12_2.html) The momentum portfolios are formed monthly, by ranking all stocks on the past 12 months returns (ignoring last month — the academic 12\_2 momentum variable). We look at the value-weight returns to the top decile of all firms ranked on their past 12\_2 momentum, and compare this to the SP500, Long-term U.S. Bonds, and the risk-free rate.

Specifically, here are the four portfolios:

1. **MOM\_10 =**Value-weight returns to the top decile formed on 12\_2 momentum. Data is found [here](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/10_Portfolios_Prior_12_2.zip).
2. **SP500 =**Total return of the S&P 500 Index
3. **LTR** = Merrill Lynch 7-10 year Government Bond Index (prior to 6/1982, Amit Goyal Data)
4. **RF =**Total return to the risk-free asset (U.S. treasury bills).

The returns runs from 1/1/1928 to 12/31/2014. Results are gross of fees. All returns are total returns and include the reinvestment of distributions (e.g., dividends).

[![momentum funds (1)](https://alphaarchitect.com/wp-content/uploads/2015/05/momentum-funds-1.png)](https://alphaarchitect.com/wp-content/uploads/2015/05/momentum-funds-1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Takeaways:**

1. Cross-sectional momentum worked  well over the past 87 years. The strategy outperformed the index (SP500) by over 600 bps! Of course, the actual returns will be lower after transaction costs, which could be substantial due to the monthly rebalancing aspect of the strategy.
2. Stocks were a better bet than Treasury bonds (LTR) and bills (RF) over the past 87 years.

## Time-series Momentum

[Time series momentum](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2089463) is a way to measure an asset classes’ own past return. Market participants use this measure to time market exposures. The measure is related to the simple moving average rule popularized by [Meb Faber](http://mebfaber.com/timing-model/), which we point out in our [post](https://alphaarchitect.com/2014/12/02/the-robust-asset-allocation-raa-index/).

The time-series, or absolute momentum rule, popularized by [Gary Antonnaci](http://www.dualmomentum.net/2015/01/absolute-momentum-revisited.html), is assessed monthly as follows:

1. **Excess return** = total return over past 12 months less return of T-bill.
2. If Excess return >0, go long risky assets. Otherwise, go alternative assets (T-Bills)

The basic premise behind the time-series momentum trading rule (TSMOM) is that if the trend (over the past 12 months) is positive, stay in the risk assets (“the trend is your friend”). Otherwise, if the trend is negative, invest in risk-free assets. This rule is very similar to the simple moving average rule, as discussed [here](https://alphaarchitect.com//2014/12/02/our-robust-asset-allocation-raa-solution/#.VRL3S454rKM). (there are other applications in [futures that go long and short](https://alphaarchitect.com/2016/12/22/time-series-momentum-volatility-scaling-and-crisis-alpha/), but we are focused on equities here).

We use the time-series momentum (TSMOM) signal from the S&P 500 on both the S&P 500 and the cross-sectional momentum return series. This is in order to have the same “rule” applied to both return series. Comparing the performance of a cross-sectional momentum stock strategy against the S&P 500 with a TSMOM rule is like comparing apples to oranges. We want to run a proper horse race that highlights the benefits of both time-series–AND cross-sectional–momentum working together.

Here are the four portfolios we test:

1. **MOM\_10 =**Value-weight returns to the top decile formed on 12\_2 momentum. Data is found [here](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/10_Portfolios_Prior_12_2.zip).
2. **MOM\_10 TSMOM =**Depending on the TSMOM rule (using SP500 TSMOM rule), the portfolio is either invested in MOM\_10, or in the risk-free (RF) asset described above.
3. **SP500 =**Total return of the S&P 500 Index.
4. **SP500 TSMOM =**Depending on the TSMOM rule, the portfolio is either invested in the SP500, or in the risk-free (RF) asset described above.

The returns runs from 1/1/1928 to 12/31/2014. Results are gross of fees. All returns are total returns and include the reinvestment of distributions (e.g., dividends).

[![momentum funds (2)](https://alphaarchitect.com/wp-content/uploads/2015/05/momentum-funds-2.png)](https://alphaarchitect.com/wp-content/uploads/2015/05/momentum-funds-2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Takeaways:**

1. The Time-Series Momentum rule (TSMOM) helps to reduce volatility and increase the risk-adjusted returns as measured by the Sharpe ratio.
2. The drawdowns are decreased for both the SP500 and the MOM\_10 portfolios — the TSMOM rule helped to reduce drawdowns.
3. While the CAGR increases when used on the SP500, the CAGR is higher for the MOM\_10 portfolio compared to the MOM\_10 TSMOM portfolio — timing the market is difficult!

## Summary

Clearly, there are benefits–at least historically–to using both cross-sectional and time-series momentum. The 2 momentum effects are not competitors, but complements. Viewing them as competitors does a disservice to both types of momentum. Overall, we hope this post helped to clarify the difference between cross-sectional momentum and time-series momentum.

The main results are as follows:

* Using individual stock momentum has worked over the past 87 years. This is commonly labeled ***cross-sectional momentum.***
* Using a simple trend following rule appears to limit drawdowns over the past 87 years. This is commonly called ***time-series momentum.***
* Combining cross-sectional momentum and time-series momentum **has worked better than using either of the stand-alone elements.**

Go momentum!
