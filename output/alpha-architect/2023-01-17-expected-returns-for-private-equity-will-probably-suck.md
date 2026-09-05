---
title: "Expected Returns for Private Equity Will Probably Suck"
slug: "expected-returns-for-private-equity-will-probably-suck"
date: "2023-01-17"
modified: "2023-01-19"
url: "https://alphaarchitect.com/expected-returns-for-private-equity-will-probably-suck/"
categories: ["Private Equity", "Research Insights", "Basilico and Johnsen", "Academic Research Insight"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Expected Returns for Private Equity Will Probably Suck

> The illiquid nature of the asset class makes the demystifying of private equity returns difficult to achieve under any circumstances, but the framework presented in this article should move the reader closer to the goal.

This article attempts to demystify the approach and methodology used to characterize the risk and return relationship in private equity today. The illiquid nature of the asset class makes the demystification of private equity returns difficult to achieve under any circumstances. Still, the framework presented in this article should move the reader closer to the goal.

## Demystifying Illiquid Assets: Expected Returns for Private Equity

* Antti Ilmanen, Swati Chandra, and Nicholas McQuinn
* Journal of Alternative Assets
* A version of this paper can be found [here](https://www.aqr.com/Insights/Research/Journal-Article/Demystifying-Illiquid-Assets-Expected-Returns-for-Private-Equity)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category.

## What are the research questions?

As investors increasingly avail themselves of the “benefits” of private equity (PE), the calculation of risk and returns to PE is under increased scrutiny.  This asset class’s illiquid nature challenges the industry’s approach and methodology today. The mark-to-market quality of public markets is not present in the case of private markets. As a result, the calculation of traditional risk measures, such as volatility and beta, is understated.  Nevertheless, the email folders of wealth managers are swamped with PowerPoint presentations that tout the lower risk of illiquid assets and expected returns sufficiently high to compensate for illiquidity. The credibility of such claims is questionable, and the direct comparison to public markets is problematic.

1. How large is the historical illiquidity premium?
2. Why is PE promoted as an asset class that will diversify an allocation to public equity?
3. How much error is introduced into measures of correlation and risk in private equity?
4. What is the framework for estimating expected returns for PE?

## What are the Academic Insights?

1. NOT VERY. The return and excess return performance of PE and various public indices from 1986 to 2017, are presented in Exhibit 1.  Note that the illiquidity premium ranges from -1.6% to 2.3% (arithmetic) or 0.4% to 4.3% (geometric), depending on the specific public index.  Although the excess returns are not zero, they are not as large as expected.
2. SMOOTHED RETURNS. The key to understanding how this result has come about is recognizing that PE prices are not marked-to-market as in the public markets. PE appears to have a low or negative correlation with public equities, which results from the method in which PE returns are calculated.  As an illiquid asset class, prices and returns to investing in PE are self-reported IRRs or appraisal-based.  This practice results in a return series that does not reflect normal fluctuations observed on a daily basis in the public markets.  They are “artificially smoothed.”  If that feature is extended to statistical risk measures, correlation and variance, the result significantly understates the actual relationship.  Smoothed returns will result in understated beta measures, correlation, etc.  Accordingly, it only *appears* that private equity provides diversification benefits.
3. QUITE A BIT. Turning to application, a series of unsmoothed PE returns is needed to determine risk exposures accurately.  Most would agree that it is essential to undo the smoothness embedded in self-reported or appraisal-based PE returns.  One approach, described by Junying Shen et al. (2022) has 2 components: 1. Estimate the autocorrelation coefficient embedded in the self-reported data and calculate an uncorrelated return series from the estimate.  That estimate is identified and verified by the Durbin-Watson test. 2. Inflate the variance of the unsmoothed returns by using the ratio of self-reported and marked-to-market returns, which is easily 30% higher.  Betas and variances estimated from this approach can be twice as large as betas using smoothed returns.
4. The framework developed in this article is illustrated in Exhibit 3 below. The unlevered expected return equals the sum of the [dividend yield](https://alphaarchitect.com/2019/11/dividends-are-different/) and real earnings per share growth rate.  The theoretical required return is then adjusted by the debt-to-equity ratio and the cost of debt.  Finally, the expected multiple expansion *m* is added to obtain the gross PE expected return. The assumptions for each component are described in detail in the article.

## Why does it matter?

The authors of this article have presented a framework for communicating the mathematics currently used in the industry to estimate returns to private equity.  Despite the increased interest on the part of institutions and other investors, the illiquidity premium appears to be substantially less attractive than it was 20 years ago.  This may or may not be a reflection of the lack of transparency around performance that produces biased estimates of returns, risk, and diversification benefits both historically and on an expected basis.

## The most important chart from the paper

![In this article, we explore the relationship between institutional investors and noise traders.](https://alphaarchitect.com/wp-content/uploads/2022/12/2022-12-26-17_14_00-JAI-Demystifying-Illiquid-Assets-Expected-Returns-for-Private-Equity_AQR.pdf-and-1200x500.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained.  Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> The growing interest in private equity means that allocators must carefully evaluate its risk and return. The challenge is that modeling private equity is not straightforward, due to a lack of good quality data and artificially smooth returns. We try to demystify the subject, considering theoretical arguments, historical average returns, and a forward-looking analysis. For institutional investors trying to calibrate their asset allocation decisions for private equity, we lay out a framework for expected returns, albeit one hampered by data limitations, that is based on a discounted cash-flow framework similar to what we use for public stocks and bonds.
>
> In particular, we attempt to assess private equity’s realized and estimated expected return edges over lower-cost public equity counterparts. Our estimates display a decreasing trend over time, which does not seem to have slowed the institutional demand for private equity. We conjecture that this is due to investors’ preference for the return-smoothing properties of illiquid assets in general.
