---
title: "Backtesting Ben Graham"
slug: "backtesting-ben-graham"
date: "2011-04-17"
modified: "2022-06-04"
url: "https://alphaarchitect.com/backtesting-ben-graham/"
categories: ["Research Insights", "Value Investing Research"]
tags: ["backtest", "Ben Graham"]
best_of: false
source: "alphaarchitect.com"
---

# Backtesting Ben Graham

> Charles Mizrahi, over at http://www.hiddenvaluesalert.com/, suggested we backtest a simple Ben Graham strategy mentioned in a 1976 article he dug up in Medical Economics. Charles has been […]

Charles Mizrahi, over at <http://www.hiddenvaluesalert.com/>, suggested we backtest a simple Ben Graham strategy mentioned in a 1976 article he dug up in *Medical Economics*. Charles has been implementing Ben Graham related strategies for many years and the live performance of his recommendations are monitored by the [Hulbert Financial Digest](http://store.marketwatch.com/webapp/wcs/stores/servlet/PremiumNewsletters_HulbertFinancialDigest) (HFD), which helps investors sift between the “good”, “bad”, and “ugly” of the newsletter world.(1)

[Here](http://medicaleconomics.modernmedicine.com/memag/issue/issueList.jsp?id=484) is a link to the modern day version of the *Medical Economics* magazine where Ben Graham mentions how to implement his simple strategy.

So what’s Graham’s secret to achieve 15%+ returns over long horizons?

Well, below is an excerpt from the original 1976 article with all important points highlighted:

[Click to get the pdf file.](https://alphaarchitect.com/wp-content/uploads/2011/04/Simple-and-Easy-Approach-Medical-Economics-Graham-1976.pdf)

We decided to keep it simple and backtest the low P/E (<10), shareholder equity > .5 strategy from 1965–2010. We also backtested the results in accordance with the “trading rules” alluded to by Graham: stocks entering the portfolio are held for 2 years, or if they appreciate >50%. For robustness, we tested a variety of P/E and shareholder equity combinations–all results are very similar.

Here are some highlights from the analysis:

[Click to get the pdf file.](https://alphaarchitect.com/wp-content/uploads/2011/04/postdata1.pdf)

We plan to write up an academic article this summer that goes into the details of our final results and analysis. We wanted to share the “hot off the press” results with readers of the Empirical Finance Blog™.

Enjoy!

References[+]

References

|  |  |
| --- | --- |
| ↑1 | His newsletter, “[Inevitable Wealth Portfolio](https://www.hiddenvaluesalert.com/index.aspx?page=Signup13)” (IWP) is worth a look for dedicated deep value investors. According to HFD, IWP is up +107.4 versus the +S&P 500 73.1% from Feb. 1, 2009 through Apr. 30, 2011. |

 function footnote\_expand\_reference\_container\_1723\_152() { jQuery('#footnote\_references\_container\_1723\_152').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_1723\_152').text('−'); } function footnote\_collapse\_reference\_container\_1723\_152() { jQuery('#footnote\_references\_container\_1723\_152').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_1723\_152').text('+'); } function footnote\_expand\_collapse\_reference\_container\_1723\_152() { if (jQuery('#footnote\_references\_container\_1723\_152').is(':hidden')) { footnote\_expand\_reference\_container\_1723\_152(); } else { footnote\_collapse\_reference\_container\_1723\_152(); } } function footnote\_moveToReference\_1723\_152(p\_str\_TargetID) { footnote\_expand\_reference\_container\_1723\_152(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_1723\_152(p\_str\_TargetID) { footnote\_expand\_reference\_container\_1723\_152(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
