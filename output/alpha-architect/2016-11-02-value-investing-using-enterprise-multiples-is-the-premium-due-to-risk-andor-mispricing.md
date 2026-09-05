---
title: "Value Investing using Enterprise Multiples — Is the Premium Due to Risk and/or Mispricing?"
slug: "value-investing-using-enterprise-multiples-is-the-premium-due-to-risk-andor-mispricing"
date: "2016-11-02"
modified: "2022-05-10"
url: "https://alphaarchitect.com/value-investing-using-enterprise-multiples-is-the-premium-due-to-risk-andor-mispricing/"
categories: ["Research Insights", "Value Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Value Investing using Enterprise Multiples — Is the Premium Due to Risk and/or Mispricing?

> At Alpha Architect, we are big fans of Value investing (and Momentum). In the past, Wes and I examined which valuation measure had the largest spread […]

At Alpha Architect, we are big fans of [Value investing](https://alphaarchitect.com/2015/12/01/quantitative-momentum-investing-philosophy/#gs.c815gus) (and Momentum). In the past, Wes and I examined ***which valuation measure*** had the largest spread between Value and Growth firms. The [evidence](https://alphaarchitect.com/2014/10/27/quantitative-value-research-a-summary-of-various-value-metrics-1013/#.VPoOKvnF9MU) showed (updated results [here](https://alphaarchitect.com/2016/04/06/update-on-the-valuation-metric-horserace-2012-2015/#gs.gvQBsJs)) that Enterprise Multiples had the largest spread between Value and Growth firms. We define Enterprise Multiples as the Total Enterprise Value (TEV) of the firm divided by EBITDA (EBIT performs similarly). The TEV equals Market Capitalization + Debt + Preferred Stock Value – Cash and Short-term Investments. While the other value measure work, and combining the measures is also a good idea, our main “Value” sort that we use is EBIT/TEV.

And we aren’t the only authors who find that enterprise multiples are more effective than traditional value measures such as book-to-market. Other authors have found similar results in the [US](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1481279) and [International](https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/div-classtitlethe-enterprise-multiple-investment-strategy-international-evidencediv/5C34D118442E97817DCF9C9F354026A2) markets. Other market participants are also big fans — e.g., [Toby Carlisle](https://greenbackd.com/) and [Joel Greenblatt](https://www.gothamfunds.com/).

That all sounds great, but we wanted to know ***why*** Enterprise Multiples (EM) performed better than other valuation metrics, historically.

To address this question we teamed up with [Steve Crawford](http://www.bauer.uh.edu/search/directory/profile.asp?firstname=Steve&lastname=Crawford) from University of Houston. We have a new working paper, titled “[Why do Enterprise Multiples Predict Expected Stock Returns?](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2847874)**”**which can be found on SSRN [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2847874).

**Bottomline:** Our collective evidence suggests that the Enterprise Multiple (EM) effect can be attributed to mispricing, and not due to higher systematic risk. Although we will not deny that higher risk likely plays some role in the higher expected returns.

### First, an Introduction to Enterprise Multiples

One of the first items we highlight in our paper is the spread in expected returns across low EM firms (value) and high EM firms (glamour or growth).

Figure 1 below highlights this fact:

[![enterprise-multiples-figure-1](https://alphaarchitect.com/wp-content/uploads/2016/11/Enterprise-Multiples-figure-1.png)](https://alphaarchitect.com/wp-content/uploads/2016/11/Enterprise-Multiples-figure-1.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Risk or Mispricing?

The bigger question, and how we hope this paper adds to the literature, is in understanding why EM works. In academia, there is a constant argument over the “reason” for the value premium (commonly examined using the book-to-market B/M ratio). In one camp (initially Fama and French 1993, others have followed), there is an argument that value stocks are riskier, so the higher returns are a compensation for taking on additional risk. In another camp (initially LSV 1994, others have followed) is that investors make behavioral errors and the higher returns to Value stocks is due to mispricing.

Our paper attempts to test what the evidence says regarding Enterprise Multiples (EM).

To test this, we create portfolios similar to [Piotroski and So (2012)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1757025). Using a variety of measures to proxy for the firm’s fundamental value (see the paper for full details), we create two portfolios:

1. **Low-mispricing Portfolio**: Long Value stocks with lower expected fundamental value, and Short Growth stocks with high expected fundamental value. Here the EM L/S portfolio is in line (or “congruent”) with the fundamental value proxy, leading to little expected expectation errors.
2. **High-mispricing Portfolio**: Long Value stocks with high expected fundamental value, and Short Growth stocks with low expected  fundamental value. Here the EM L/S portfolio is **not** in line (or “incongruent”) with the expected fundamental value proxy, leading to high expected expectation errors.

The basic idea is the following — examine the long/short returns to two value/growth portfolios, one where the expected fundamental values are in line with the price (congruent) and one where the expected fundamental values are not in line with the price (high-mispricing). If risk drives the EM value premium, both portfolios should have similar return profiles (since ***both portfolios***are ***long value*** and ***short growth***). However, if mispricing explains the EM value premium, one should expect the high-mispricing portfolio (where expectation errors are expected to be the highest) to have a higher return compared to the low-mispricing portfolio (where expectation errors are expected to be the lowest).

Figure 2 below highlights the main result of the paper:

[![enterprise-multiples-figure-2](https://alphaarchitect.com/wp-content/uploads/2016/11/Enterprise-Multiples-figure-2.png)](https://alphaarchitect.com/wp-content/uploads/2016/11/Enterprise-Multiples-figure-2.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The high-mispricing portfolio (incongruent) has a significant outperformance compared to the low-mispricing portfolio (congruent). In fact, the EM Long Value/Short Growth congruent portfolio has a negative return from 1974-2015 — remember this is a *long value and short growth portfolio* with negative returns. In Table 2 of the paper, we show that the 4-factor alpha on the congruent portfolio is an insignificant negative 0.17% per month, while the 4-factor alpha on the incongruent portfolio is a positive and significant 0.97% per month (~11.64% per year).

Please See Tables 2 and 3 of the paper for all the alpha loadings and the full details on the tests.

So it appears that mispricing hypothesis may have some legs to stand on; however, there are some additional tests we run.

#### Test 1: Earnings Announcements

If mispricing is driving the EM value effect, we should see higher earnings announcement returns when expectation errors are high (value firms with high expected fundamental value) than when they are low (glamour firms with low expeced fundamental values). Furthermore, we should see a positive spread in forecast errors and forecast revisions across high and low expectation errors firms, controlling for valuation (i.e., EM quintile). The results to our test are shown below (Table 4 in the paper):

[![enterprise-multiples-figure-3](https://alphaarchitect.com/wp-content/uploads/2016/11/Enterprise-Multiples-figure-3.png)](https://alphaarchitect.com/wp-content/uploads/2016/11/Enterprise-Multiples-figure-3.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The results in Table 4 also support the mispricing hypothesis:

1. **Panel A**: Using Earning Announcement returns, there are higher long/short returns to the high-mispricing portfolio relative to the low-mispricing portfolio.
2. **Panel B**: Using Analyst Forecast Errors, we find that analysts following value firms with the highest fundamental values are much less optimistic than analysts following glamour firms with low fundamental values, which is consistent with mispricing driving the returns in the high-mispricing portfolio (here a negative value indicates that analysts are less optimistic).
3. **Panel C**: Using Analyst Forecast Revisions, in the high-mispricing portfolio, we observe small negative forecast revisions for value firms with high fundamental value relative to glamour firms with low fundamental value. (here a negative value indicates that the analyst has revised down their forecast).

All three of these results are consistent with the mispricing hypothesis.

#### Test 2: Investor Sentiment

We test the effect on investor sentiment using two measures in the literature ([here](http://people.stern.nyu.edu/jwurgler/papers/wurgler_baker_cross_section.pdf) and [here](http://rfs.oxfordjournals.org/content/early/2014/10/31/rfs.hhu080)). Specifically, we examine the long/short portfolio returns in 3 different regimes of investor sentiment (low, mid, high).

[![enterprise-multiples-figure-4](https://alphaarchitect.com/wp-content/uploads/2016/11/Enterprise-Multiples-figure-4.png)](https://alphaarchitect.com/wp-content/uploads/2016/11/Enterprise-Multiples-figure-4.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

In support of the mispricing hypothesis, the returns to the high-mispricing EM strategy are significantly higher during periods of high investor sentiment relative to times of low investor sentiment while the same pattern is *not* observed for the low-mispricing EM portfolio.

#### Test 3: Limits of Arbitrage

Since the mispricing theory has some evidence behind it (as shown above), why haven’t market participants exploited this? We examine potential [limits to arbitrage](https://alphaarchitect.com/2014/05/20/introduction-behavioral-finance-part-2-limits-arbitrage/#gs.hsQMf5g) by examining the long and short alphas to the long/short portfolio. In Table 6 of the paper, we show that ~62% of the alpha comes from the short book. To the extent that managing short positions are costly, these results suggest that the mispricing associated with the high-mispricing EM portfolio is difficult to profitably exploit.

### Conclusions

Overall, we find evidence to suggest that the excess value returns to EM sorted portfolios is driven by mispricing. We are in the process of adding some additional robustness tests to the paper. Stay tuned!

A natural question given this research: Why do so many systematic value strategies avoid enterprise multiples? Most index methodologies in the market include B/M and some form of forward earnings/price — B/M is arguably the least effective valuation metric and forward-looking valuation metrics don’t even capture the value premium. Weird.

We’re sticking with enterprise multiples…

Comments/Suggestions are welcome!

---

### Why Do Enterprise Multiples Predict Expected Stock Returns?

Crawford, Gray, and Vogel

A version of the paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2847874).

Want a summary of academic papers with alpha? Check out our [Academic Research Recap](https://alphaarchitect.com/category/architect-academic-insights/academic-research/#gs.m4HqX7w) Category.

### Abstract:

> The enterprise multiple (EM) effect has been documented across global stock markets. EM is a robust predictor of expected average returns and generates a much stronger value effect than traditional value metrics. We find evidence the EM effect is primarily attributable to mispricing and not due to higher systematic risk. We document that earnings announcement returns, forecast errors, and forecast revisions all support the notion that the EM effect is driven by mispricing associated with predictable investor expectation errors. Finally, we show that the EM effect is stronger during times of strong market sentiment, which also supports the mispricing-based hypothesis.
