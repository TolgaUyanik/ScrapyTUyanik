---
title: "The Long Volatility Premium: Short the Market, Get Paid?"
slug: "the-long-volatility-premium-short-the-market-get-paid"
date: "2026-02-06"
modified: "2026-05-21"
url: "https://alphaarchitect.com/the-long-volatility-premium-short-the-market-get-paid/"
categories: ["Crisis Alpha", "Volatility (e.g., VIX)", "Options", "Best of Other", "Research Insights", "Factor Investing", "Podcasts and Video"]
tags: ["tail hedging", "long volatility"]
best_of: true
source: "alphaarchitect.com"
best_of_section: "Other"
---

# The Long Volatility Premium: Short the Market, Get Paid?

> Long volatility should be considered a factor that earns positive returns over the long term. At least that’s what One River Asset Management’s Patrick Kazley suggests in his piece “Heretical Thinking: The Long Volatility Premium”

We can list some facts[1](#d3fb529c-492e-44c0-a887-bd0f066ec1ad) of life: death, taxes… and buying puts results in portfolio drag.

Then burn the list.[2](#f4cbe19a-8df3-489f-ab1f-9ed23b5e3de1)

At least that’s what One River Asset Management’s Patrick Kazley suggests we should do. According to Kazley, long volatility should be considered a factor (much like our beloved value, momentum and trend factors) that earns *positive* returns over the long term. And he’s brought the receipts.

In this piece, I wanted to break down the paper titled *Heretical Thinking: The Long Volatility Premium* in a digestible manner so investors can think more clearly about how to fit tail hedging exposures in a broader portfolio context. If you believe the answer is that investors should just eat the cost of hedging… keep on reading.

Or better yet, keep watching. I asked Joe DeSipio of Arin Risk Advisors to join me to discuss how investors might go about targeting tail-hedging exposures in their own portfolios in light of the paper’s findings. If you’re interested, you can check out that conversation here:

Let’s begin.

### **Long/Short or Long/Long?**

When constructing factors, academics typically go long a portfolio of stocks with a high loading to that factor and then short the opposite side of that bet, all to neutralize the effect of beta, or the risk premium to the market. By doing this, one can see what the factor has done while muting the returns of the market.

In the same manner, dissecting a long volatility premium requires one to neutralize the effects of beta. Because put options have a huge embedded short beta bet, instead of going long/short, one can go long puts/long the market. The results show that the negative bleed associated with put-buying can be more accurately ascribed to the implied to the short beta position, not to long volatility, per se.

> *“the source of this negative return isn’t fully intrinsic to long volatility itself, but rather comes primarily (perhaps almost entirely) from the negative exposure to the equity risk premium.”*[3](#e665b2a6-13c9-4386-a2a2-fdf8cb8282ed)

This decomposition allows us to peek into how long volatility should behave after accounting for its short beta exposure.

## **Neutralizing Beta… Not as Easy as it Sounds**

One of the major conundrums in this construction is that decoupling beta from options is much harder than doing so in plain-vanilla equities.

Because puts gain greatly when the market crashes, including the entire return series to estimate the negative beta loading of the put portfolio would greatly overestimate the amount of negative beta present. In other words, one could easily mistake returns that belong to our precious long volatility factor and misattribute them to short beta.

Kazley seeks to adjust for this phenomenon by winsorizing (capping) the most extreme observations and forming a “benign beta” factor that can be used in the regression.

![](https://alphaarchitect.com/wp-content/uploads/2026/01/image.png)

Source: Kazley, Patrick. *Heretical Thinking: The Long Volatility Premium*. One River Asset Management, October 2025. *The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

## **The Results**

In the fourth column (B), the author seeks to combine the market with the long volatility factor to achieve an ex-ante beta loading of one. By doing this, one can estimate not just the returns attributable to long volatility, but also any rebalancing premium returns. The fifth column (B − A) displays the results of this portfolio minus the returns of the market, while the sixth column—the standalone long volatility factor return—directly offsets the “benign beta” from a put portfolio to arrive at a purer factor return series.

![](https://alphaarchitect.com/wp-content/uploads/2026/01/image-1.png)

Source: Kazley, Patrick. *Heretical Thinking: The Long Volatility Premium*. One River Asset Management, October 2025. *The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged and do not reflect management or trading fees, and one cannot invest directly in an index*.

## **The Takeaway**

The issue with put options is not that they tend to lose money over the long term. We already knew that. The actual problem is that, more often than not, a portfolio of stocks and put options gets compared with a portfolio of just stocks.  
  
Kazley’s research brings a refreshing take to an often misunderstood[4](#55904812-2b52-4d2d-8f8b-97779c2e494e) asset. In light of these findings, there are two main ways one could implement tail hedging:

1. **As a diversifier**: Convexity is not an easy thing to come by. Unless you’re willing to use options to directly offset the “benign beta” in a put portfolio, it’s okay to use some of the equity in your portfolio as a “hedge” to your hedge. Either way, convexity seems to provide diversification benefits to a portfolio not easily available elsewhere, even if it eats away at returns[5](#578443a8-f01d-450a-b58f-628a558f8744). Alternatively, one can find ways to neutralize the negative cost of carry to get a purer factor exposure and bolt it onto a portfolio of stocks and bonds.
2. **As an avenue to take in more risk:** In my conversation with Joe, he suggested that investors who already use puts should find creative ways to add risk back on. Yes, the most no-brainer way to do this is to lever up stocks. Personally, that makes me a bit queasy. But whether you add alternatives on top of your equity portfolio, concentrate in fewer and fewer stocks, or target higher-volatility alts, hedging is a permission to take on meaningful amounts of risk.

Whichever way one decides to go, it’s important to remember that tail hedging is another tool in your toolbox. If you do use it, make sure to use it wisely.

Source: Kazley, Patrick. *Heretical Thinking: The Long Volatility Premium—How Investors Are Paid to Protect Themselves*. One River Asset Management, October 2025.

1. I must reiterate: this is a joke . [↩︎](#d3fb529c-492e-44c0-a887-bd0f066ec1ad-link)
2. As Dwight Schrute once said. [↩︎](#f4cbe19a-8df3-489f-ab1f-9ed23b5e3de1-link)
3. Kazley, Patrick. *Heretical Thinking: The Long Volatility Premium*. One River Asset Management, October 2025. 4. [↩︎](#e665b2a6-13c9-4386-a2a2-fdf8cb8282ed-link)
4. Don’t worry, I struggle too. [↩︎](#55904812-2b52-4d2d-8f8b-97779c2e494e-link)
5. Whether that’s directly, or in the form of opportunity cost. [↩︎](#578443a8-f01d-450a-b58f-628a558f8744-link)
