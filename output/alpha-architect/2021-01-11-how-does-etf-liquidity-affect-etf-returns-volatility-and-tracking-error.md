---
title: "How Does ETF Liquidity Affect ETF Returns, Volatility, and Tracking Error?"
slug: "how-does-etf-liquidity-affect-etf-returns-volatility-and-tracking-error"
date: "2021-01-11"
modified: "2022-05-21"
url: "https://alphaarchitect.com/how-does-etf-liquidity-affect-etf-returns-volatility-and-tracking-error/"
categories: ["Transaction Costs", "Research Insights", "Basilico and Johnsen", "Academic Research Insight", "ETF Investing"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# How Does ETF Liquidity Affect ETF Returns, Volatility, and Tracking Error?

> Liquidity risk and exchange-traded fund returns, variances, and tracking errors Kyounghun Bae, Daejin Kim Journal of Financial Economics A version of this paper can be […]

## Liquidity risk and exchange-traded fund returns, variances, and tracking errors

* Kyounghun Bae, Daejin Kim
* Journal of Financial Economics
* A version of this paper can be found [here](https://www.sciencedirect.com/science/article/abs/pii/S0304405X20301276)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

Although the ETF market has grown exponentially over the recent 20 years, ETFs that are less popular are not always liquid. A majority of the dollars flowing into ETFs are concentrated in 3 products, accounting for 46.7% of total ETF trading volume (see Figure 3 below).  If the next 8 ETFs are included that percentage increases to 61.5%.  If that doesn’t astound the reader, consider that the AUM$ of the top 10 represent 36% of total AUM$ for ETFs.  That translates to roughly 64% of ETFs measured in terms of AUM$ are relatively “unpopular”.  In terms of trading volume, those ETFs excluding the top 10 represent only 38.5%.  Anyway you look at it, there is a potential liquidity challenge with a major portion of the ETF market.

**Why does this matter?** If the liquidity of the unpopular ETFs is insufficient, it may affect the proper functioning of the ETF market in those products with consequent increased transactions costs for investors.

**How might this happen?** The problem emanates from the unique structure of the ETF that results in two prices that are intricately related.  For example, although ETFs are traded on exchanges, the shares included in an ETF are first created and redeemed in the primary market. If you want to understand this process better I highly encourage you read Wes’s article titled, “[Understanding How ETFs Trade in the Secondary Market.](https://alphaarchitect.com/2014/12/03/trading-etfs-in-the-secondary-market/)” Now with a baseline understanding of how ETFs trade, we can recognize that there is a price for the ETF product on the exchange and another price or Net Asset Value (NAV) determined on the value of the underlying basket of stocks.  The returns on each should be very similar.  However, a number of factors can drive a wedge between them, resulting in differences in returns, and consequent differences in ETF variances and ETF tracking error.  Divergence in the ETF returns and the NAV returns should be eliminated by arbitrage efforts of “authorized participants” (APs) — essentially market makers.  However, under conditions of low liquidity, the APs may be incented to refrain from replicating the index (unprofitable prices) at the same time trading in the ETF basket occurs. Any delay in the timing of arbitrage activity, because APs prefer to wait for increased bid-ask spreads, for instance, will be accompanied by an increase in the tracking error of the ETF and increased transaction costs for investors. Not pretty, but it does motivate the authors to analyze the impact of illiquidity on ETF tracking error, variance, and returns in the secondary US ETF market.

The answers to the following 3 questions provide evidence on the degree of efficiency in the ETF market as well as to the magnitude of the problem. The data was comprised of all ETFs ever listed or traded on US exchanges between 1993-2012, where the country of domicile is limited to the US.  All delisted ETFs that traded during the sample period were included. Daily prices for ETFs, NAVs, and underlying indexes were obtained from Bloomberg.

1. Does ETF liquidity affect tracking error?
2. Does ETF liquidity affect returns?
3. Does liquidity affect ETF variance?

## What are the Academic Insights?

1. YES. The analyses conducted substantiate a causal link between illiquidity of the ETF, illiquidity of the underlying asset, and the consequent impact on tracking error.  Specifically, the presence of illiquidity in the underlying basket magnifies the impact of ETF illiquidity on tracking error. The authors present evidence that a positive relationship exists between ETF illiquidity and tracking error, using daily and annual data.  ETF illiquidity was measured as the *daily relative effective spread* = ratio of the effective half-spread to trade price; where the effective half-spread = absolute difference between quote midpoint and trade price. The structure (in-kind vs. cash) of ETFs also differed in terms of illiquidity, with in-kind exhibiting less sensitivity to ETF illiquidity than the cash method.  Non-leveraged ETFs were used to examine the impact of illiquidity of the underlying basket of stocks on ETF illiquidity. Not surprisingly, stocks with less liquidity have a larger impact, even if the asset classes and markets are identical.
  
2. YES. The empirical results suggest that liquidity is a priced risk factor in the US ETF market.  That is, the return on an ETF is dependent on the covariance of the ETF liquidity and return with the market liquidity and return. An ETF liquidity beta is estimated and determined to have a positive and significant risk premium of approximately 0.14% annualized. The authors discuss the application of the LCAPM to ETF returns and conclude the model is a good fit for the ETF market.
  
3. YES. Using the Lo and MacKinlay (1990) econometric model and derive the ETF variance with respect to the NAV variance. The empirical tests provided evidence for a positive relationship between the two variances. They interpret the difference between the two as risk due to infrequent trading in the secondary market, in addition to the risk of the underlying basket of stocks.

## Why does ETF liquidity matter?

Apparently, the illiquidity present in the ETF market increases the transaction costs for AP/market makers and ETF investors. If market makers (APs) fail to replicate the index immediately and properly in order to avoid increasing the costs of such market-making, they will undoubtedly increase tracking error of the product and fail to meet investor objectives. The illiquidity of the underlying constituents of an ETF and the tracking error that may result is something investors ought to be conscious of. One could consider investing in the underlying basket into their own hands and skipping the ETF structure altogether, however that exposes investors in active investment vehicles to high tax hurdles and increases in trading costs.

An excellent article if the reader is interested in understanding the microstructure foundations of trading in the ETF market.

## The most important chart from the paper

![This image shows trading volume by top exchange-traded funds, which is relevant to the discussion of ETF liquidity.](https://alphaarchitect.com/wp-content/uploads/2021/01/2021-01-05-14_16_58-ETFs_returns_risk_JFE.pdf-PDF-Annotator-1200x883.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

## Abstract

> We investigate the effect of exchange-traded fund (ETF) liquidity on ETF tracking errors, returns, and volatility in the US. We ﬁnd that illiquid ETFs have large tracking errors. The effect is more pronounced when underlying assets are less liquid. Returns and liquidity of illiquid ETFs are more sensitive to underlying index returns or ETF market liquidity, or both. Thus, a positive liquidity premium exists in US ETF markets. The ETF variance could be larger than its net asset value variance owing to infrequent trading. In summary, illiquid ETFs are more likely to deviate from their underlying indexes and could be riskier than underlying portfolios.
