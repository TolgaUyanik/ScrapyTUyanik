---
title: "Flexible Asset Allocation"
slug: "flexible-asset-allocation"
date: "2013-01-03"
modified: "2022-06-04"
url: "https://alphaarchitect.com/flexible-asset-allocation/"
categories: ["Research Insights", "Momentum Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Flexible Asset Allocation

> Generalized Momentum and Flexible Asset Allocation (FAA) An Heuristic Approach Wouter J. Keller and Hugo S.van Putten A recent version of the paper can be […]

### Generalized Momentum and Flexible Asset Allocation (FAA) An Heuristic Approach

* Wouter J. Keller and Hugo S.van Putten
* A recent version of the paper can be found [here](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2193735).
* Note: [CXO Advisory](http://www.cxoadvisory.com/subscription-options/?wlfrom=%2F22480%2Fvolatility-effects%2Fasset-allocation-combining-momentum-volatility-correlation-and-crash-protectio%2F) has a recent post on this, but I was 90% done with this post so I’m posting anyway. CXO has a more detailed analysis for subscribers to their site.

### **Abstract:**

> In this paper we extend the timeseries momentum (or trendfollowing) model towards a generalized momentum model, called Flexible Asset Allocation (FAA). This is done by adding new momentum factors to the traditional momentum factor R based on the relative returns among assets. These new factors are called Absolute momentum (A), Volatility momentum (V) and Correlation momentum (C). Each asset is ranked on each of the four factors R, A, V and C. By using a linearised representation of a loss function representing risk/return, we are able to arrive at simple closed form solutions for our flexible asset allocation strategy based on these four factors. We demonstrate the generalized momentum model by using a 7 asset portfolio model, which we backtest from 1998-2012, both in- and out-of-sample.

### **Data Sources:**

1998-2012

### **Strategy Summary:**

* Test a few different signals for market and asset class timing.  The authors then combine these signals.  They are using 7 asset classes described here:
  + Our example universe consists of 7 index funds (so U=7), i.e. 3 for global stocks (VTSMX, FDIVX, VEIEX) covering US, EAFE and EM regions, 2 for US bonds (VFISX, VBMFX) and a commodity and REIT index fund (QRAAX, VGSIX). Users only interested in recent years can use the corresponding ETFs (eg. VTI, VEA, VWO, SHY, BND, GSG, and VNQ) which follow the same indices as our index funds.
* They use a 4 month lookback for prices in the paper.
* Each month, rank all 7 based on relative momentum (higher is better), volatility (lower is better), and correlations (lower is better).  So each of the seven assets has a rank from 1-7 for the 3 factors.
* Then rank using this equation:
  + Li = wR \* rank(ri) + wV \* rank(vi) + wC \* rank (ci)
  + Authors arbitrarilly set wR=1, wV=0.5, and wC=0.5.
* This new variable “Li” now ranks all the assets on relative momentum, volatility, and correlations.  Pick the top 3 assets each month and equal weight these.
  + Last, for each of the top 3 assets chosen above, check their absolute momentum – if this is negative, just go into cash.
* Make money!

### **Strategy Commentary:**

* Simple way to combine absolute momentum, relative momentum, volatility, and correlations.
* Paper also shows better returns when not equal weighting the top 3 assets, but this is more complicated.
* Cool paper…but one gripe…

Translation of the very obtuse abstract:

> We mix momentum, risk parity, and correlation factors–factors all known to work in sample for tactical asset allocation models–and compile them into a model that tells us what we already know: these factors work historically. We forgot to include a test of our model against [Meb Faber’s](http://www.mebanefaber.com/) ridiculously easy long-term moving average rule as a benchmark comparison (instead opting to include the buy&hold benchmark, which sucks), because that would make all our complicated models seem worthless.

One paper you might want to explore if this sort of stuff turns you on is [Gary Antonacci’s piece:](http://optimalmomentum.blogspot.com/)  
<http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2042750>
