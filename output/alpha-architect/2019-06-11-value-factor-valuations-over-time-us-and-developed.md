---
title: "Value Factor Valuations Over Time: US and Developed"
slug: "value-factor-valuations-over-time-us-and-developed"
date: "2019-06-11"
modified: "2022-05-19"
url: "https://alphaarchitect.com/value-factor-valuations-over-time-us-and-developed/"
categories: ["Research Insights", "Factor Investing", "Value Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Value Factor Valuations Over Time: US and Developed

> We built a simple tool recently to review so-called value spreads over time. (1) This tool maps out the median valuations for the top decile […]

We built a simple tool recently to review so-called value spreads over time. (1)

This tool maps out the median valuations for the top decile and bottom decile “cheap stock” portfolios (e.g. [EBIT/TEV](https://alphaarchitect.com/2016/11/02/value-investing-using-enterprise-multiples-is-the-premium-due-to-risk-andor-mispricing/) or sales/price).

Why might this be useful?

This tool allows one to identify the “valuation” spread between the cheapest stocks and the most expensive stocks in the universe. Some research [suggests](https://alphaarchitect.com/2017/12/21/the-returns-to-value-strategies-when-valuation-spreads-are-wide/) this can be a useful prediction device.

The analysis to build the data works as follows:

* **Identify Universe:** Top 1500 stocks by market cap (US and EAFE)
* **Identify Valuation:** Calculate a valuation metric (e.g., EBIT/TEV) for all firms in the universe
* **Decile Splits:** Sort the 1500 stocks into 10 buckets, 150 stocks each, equal-weight, rebalance monthly
* **Calculate Median Valuation:** For each decile, calculate the median valuation metric (e.g., EBIT/TEV)
* **Plot the data**

We create the following time series (assuming EBIT/TEV is the value metric):

* **US Value** = Top Decile EBIT/TEV (1)
* **US Glamour** = Bottom Decile EBIT/TEV (10)
* **US Spread** = US Value – US Glamour
* **EAFE Value** = Top Decile EBIT/TEV (1)
* **EAFE Glamour** = Bottom Decile EBIT/TEV (10)
* **EAFE Spread** = US Value – US Glamour

Here is a chart of the spreads since 1992 for the US and EAFE. [You can dig in to the tool](https://alphaarchitect.com/visualfactors/) for the raw data and additional breakouts on the data.

[![](https://alphaarchitect.com/wp-content/uploads/2019/06/ebit-spread-800x309.png)](https://alphaarchitect.com/visualfactors/)

Source: <https://alphaarchitect.com/visualfactors/>

## Conclusions

Spreads aren’t crazy and fairly in line with historical norms. Surprising.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | something we’ve discussed in the past many times. Example [here](https://alphaarchitect.com/2014/09/12/valuation-spreads-over-time-a-unique-market-timing-signal/). |

 function footnote\_expand\_reference\_container\_48651\_53() { jQuery('#footnote\_references\_container\_48651\_53').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_48651\_53').text('−'); } function footnote\_collapse\_reference\_container\_48651\_53() { jQuery('#footnote\_references\_container\_48651\_53').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_48651\_53').text('+'); } function footnote\_expand\_collapse\_reference\_container\_48651\_53() { if (jQuery('#footnote\_references\_container\_48651\_53').is(':hidden')) { footnote\_expand\_reference\_container\_48651\_53(); } else { footnote\_collapse\_reference\_container\_48651\_53(); } } function footnote\_moveToReference\_48651\_53(p\_str\_TargetID) { footnote\_expand\_reference\_container\_48651\_53(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_48651\_53(p\_str\_TargetID) { footnote\_expand\_reference\_container\_48651\_53(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
