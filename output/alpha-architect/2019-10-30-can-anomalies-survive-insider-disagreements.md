---
title: "Can Anomalies Survive Insider Disagreements"
slug: "can-anomalies-survive-insider-disagreements"
date: "2019-10-30"
modified: "2022-05-19"
url: "https://alphaarchitect.com/can-anomalies-survive-insider-disagreements/"
categories: ["Research Insights", "Behavioral Finance"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Can Anomalies Survive Insider Disagreements

> What is the relationship between insider trades and anomalies? Anginer, Hoberg and Seyhun A version of the paper can be found here. Want to read our […]

## What is the relationship between insider trades and anomalies?

* Anginer, Hoberg and Seyhun
* A version of the paper can be found [here](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2625614).
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight) category

## What are the research questions?

Anomalies such as [Value](https://alphaarchitect.com/2014/10/02/quantitative-value-research-low-pe/) and [Momentum](https://alphaarchitect.com/2015/01/06/quantitative-momentum-research-intermediate-term-momentum/) have been exploited for years, yet the source of these premiums emerged as a major unresolved puzzle. Potential explanations can be grouped into two broad categories: “compensation for risk” or “mispricing”.

This paper studies this puzzle by investigating the relationship between insider trades and stock anomalies. Here’s a [post](https://alphaarchitect.com/2015/05/04/a-unique-insider-trading-signal-that-generates-alpha/) about Insider trading pattern, from which we cite the definition of “Insiders”:

> “Insiders” are broadly defined under SEC regulations to be those who have “access to non-public, material, insider information.” We perceive “Insiders” as more like officers who hold C-level positions in a company and usually can get access to information earlier than anyone else.

In other words, insiders are known as the investors best positioned to exploit mispricing of their own firm’s stock. This paper hypothesizes that if insider trades systematically predict the direction of returns due to anomalies, then it is likely that anomalies are due to **mispricing/informational inefficiency**.

To be specific, the paper examines the predictability of anomalies when insiders agree or disagree with the direction of returns implied by a given anomaly.

* **AGREE:** if i) insiders are ‘buyers’ of the stock and the anomaly signal predicts high returns, or ii) insiders are ‘sellers’ of the stock and the anomaly signal predicts low returns.
* **DISAGREE:** if i) insiders are ‘sellers’ of the stock and the anomaly signal predicts high returns, or ii) insiders are ‘buyers’ of the stock and the anomaly signal predicts low returns.
* **NEUTRAL:** if If insiders are not buyers or sellers.

### The paper tests 13 anomalies:

1. Post-earnings announcement drift (PEAD) — [Livnat and Mendenhall (2006)](http://onlinelibrary.wiley.com/doi/10.1111/j.1475-679X.2006.00196.x/abstract)
2. Net operating assets — [Hirshleifer, Hou, Teoh and Zhang (2004)](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=404120)
3. Gross Profitability — [Novy-Marx (2013)](http://rnm.simon.rochester.edu/research/OSoV.pdf)
4. Return on assets —[Fama and French (2008)](http://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.2008.01371.x/abstract)
5. Investment in assets — [Titman, Wei, and Xie (2004)](http://www.nber.org/papers/w9951)
6. Assets growth — [Cooper, Gulen, and Schill (2008)](http://www.krannert.purdue.edu/faculty/hgulen/asset_growth.pdf)
7. Book-to-market — [Fama and French (1993)](http://rady.ucsd.edu/faculty/directory/valkanov/pub/classes/mfe/docs/fama_french_jfe_1993.pdf)
8. Net stock issuance — [Pontiff and Woodgate (2008)](https://www2.bc.edu/~pontiff/Documents/11_pontiff-woodgate.pdf)
9. Bankruptcy prediction scores (Ohlson’s O-Score) — [Ohlson (1980)](http://teaching.ust.hk/~ismt551j/project2/Ohlson.pdf)
10. Accruals — [Hirshleifer, Hou, Teoh, and Zhang (2004)](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=404120)
11. Composite equity issuance — [Daniel and Titman(2006)](http://www.kentdaniel.net/papers/published/jf_06.pdf)
12. Size — [Fama and French (1993)](http://rady.ucsd.edu/faculty/directory/valkanov/pub/classes/mfe/docs/fama_french_jfe_1993.pdf)
13. Momentum — [Jegadeesh and Titman (1993)](http://www.bauer.uh.edu/rsusmel/phd/jegadeesh-titman93.pdf)

## What are the academic insights?

Using stock price data from CRSP, financial statement data from COMPUSTAT, and insider trading data from Thomson Reuters Insider Filing Data Feed (1996 to 2013) the research team quantitatively measured insider trading, creating an “Insider score.” Then it form portfolios for both time-series and cross-sectional analyses based on this score on a monthly basis.

The table below shows the cross-sectional result:

* When insiders *agree*, anomalies are priced **significantly**.
* When insiders *disagree*, the predictive ability of the anomalies completely **disappears!** What’s more, 2 of the 13 anomalies switch signs.

As expected, the results are somewhat weaker when we value-weight the observations in the cross-sectional regressions. This is because insider trading is generally less informative for large firms.

## The most important chart from the paper

![](https://alphaarchitect.com/wp-content/uploads/2019/09/Insiders-800x554.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

## Why does it matter?

The conclusion of this paper is that the information content of insider trading is what dominates the anomaly, which explains why the predictive ability of anomaly variables disappears when insider disagrees. The findings provide support for the mispricing explanation of why anomalies persist.

## Abstract

> Many studies show that future stock returns are predictable. These findings are consistent with either mispricing or risk-based asset pricing models that capture the cross-section of expected returns. In this paper, we use a large backward-extended insider trading database from 1975 to 2013 to construct anomaly-specific measures of mispricing that are designed to be unrelated to risk. We find that the predictive ability of both insider trading and anomalies survives when the direction of insider trading agrees with the anomaly but the predictive ability of the anomalies completely disappears when insider trading disagrees with the anomaly. In all cases, insider trading continues to predict future abnormal returns. We conclude that mispricing is an important component of the predictive ability of all thirteen anomalies we consider.
