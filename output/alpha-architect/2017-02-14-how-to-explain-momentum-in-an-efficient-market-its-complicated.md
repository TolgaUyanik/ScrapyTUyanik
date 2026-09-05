---
title: "How to Explain Momentum with Rational Investors — It’s complicated."
slug: "how-to-explain-momentum-in-an-efficient-market-its-complicated"
date: "2017-02-14"
modified: "2022-05-11"
url: "https://alphaarchitect.com/how-to-explain-momentum-in-an-efficient-market-its-complicated/"
categories: ["Research Insights", "Momentum Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# How to Explain Momentum with Rational Investors — It’s complicated.

> A recent theory paper from researchers at NYU and Rutgers attempts to explain the empirical evidence on stock serial correlation (e.g., short-term reversal, long-term stock reversal, and classic […]

A [recent theory paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2910570) from researchers at NYU and Rutgers attempts to explain the empirical evidence on stock serial correlation (e.g., [short-term reversal](https://alphaarchitect.com/2015/01/14/quantitative-momentum-research-short-term-return-reversal/), [long-term stock reversal](https://alphaarchitect.com/2015/01/09/quantitative-momentum-research-long-term-return-reversal/), and [classic stock momentum](https://alphaarchitect.com/2014/07/16/momentum-investing-ride-winners-and-cut-losers-period/)).

The interesting wrinkle with this paper is the authors don’t need to assume irrational trading behavior to generate momentum effects.

The core assumptions are as follows:

* The authors assume a group of traders who don’t always trade based purely on fundamentals. For example, a trader may trade for liquidity reasons because they need money for a down payment on a house.
* The authors also need the assumption that a liquidity trader’s demands can’t be perfectly equated to supply/demand in real-time and thus might move prices away from fundamental value in unpredictable ways.

The “noise” created by liquidity traders moving prices away from their efficient level can create a level of uncertainty. The authors then show that this uncertainty can give rise to serial correlation effects such as momentum and reversals.(1)

To highlight the relationship, the authors rely on some simple concepts and mathematics that are *completely transparent and intuitive* (har har).(2)

For example, proposition 1 is as follows:

[![prop1](https://alphaarchitect.com/wp-content/uploads/2017/02/prop1-1030x500.png)](https://alphaarchitect.com/wp-content/uploads/2017/02/prop1.png)  
The authors are kind enough to map out their multi-page proof in the appendix — below is a simple highlight:  
![](https://alphaarchitect.com/wp-content/uploads/2017/02/proof1-1.png)

As the analysis highlights, proving that momentum effects can be derived in a world without irrational traders and improper expectation formation is straight forward…Yikes!

---

## [The Dynamics of Belief Formation and Price Momentum](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2910570)

* Alex Dontoh
* Johua Ronen
* Bharat Sarath

> In classical perfect and complete markets, prices form a Martingale and stock returns (or equivalently, successive price changes) are serially uncorrelated. However, there is considerable evidence in the finance literature showing that stock returns are serially correlated both in the short and the long-term. This empirical phenomenon has been viewed as a violation of semistrong efficiency and has resulted in considerable discussion in the literature. In this paper we demonstrate that within a multi-period noisy rational expectations equilibrium framework, a first order autoregressive (AR-1) liquidity trading process, by itself, suffices to give rise to systematic correlations in price changes, either positive or negative, depending on the specific parameters of the process, even if the (unknown) underlying liquidation value is fixed. That is, unsystematic random fluctuations in observed prices arising from factors such as liquidity trading affect Bayesian belief formation, and thereby trading strategies, in such a way that equilibrium price changes can manifest both momentum and reversals.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | The mechanism seems similar to the [limit of arbitrage](https://ms.mcmaster.ca/~grasselli/DeLongShleiferSummersWaldmann90.pdf) argument put forth by De Long, Shleifer, Summers, and Waldmann. Also the mechanism outlined in [John Hussman’s article](http://www.hussmanfunds.com/pdf/jedcree.pdf) |
| ↑2 | Note, what follows is mostly tongue in cheek. The paper is actually quite interesting and I respect the thought leadership from the authors. Nonetheless, this paper highlights the massive effort academic researchers invest in order to try and explain various empirical phenomenon in the stock market. |

 function footnote\_expand\_reference\_container\_27045\_129() { jQuery('#footnote\_references\_container\_27045\_129').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_27045\_129').text('−'); } function footnote\_collapse\_reference\_container\_27045\_129() { jQuery('#footnote\_references\_container\_27045\_129').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_27045\_129').text('+'); } function footnote\_expand\_collapse\_reference\_container\_27045\_129() { if (jQuery('#footnote\_references\_container\_27045\_129').is(':hidden')) { footnote\_expand\_reference\_container\_27045\_129(); } else { footnote\_collapse\_reference\_container\_27045\_129(); } } function footnote\_moveToReference\_27045\_129(p\_str\_TargetID) { footnote\_expand\_reference\_container\_27045\_129(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_27045\_129(p\_str\_TargetID) { footnote\_expand\_reference\_container\_27045\_129(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
