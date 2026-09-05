---
title: "Reproducible Finance with R: Code Flows and Shiny Apps for Portfolio Analysis"
slug: "reproducible-finance-with-r-code-flows-and-shiny-apps-for-portfolio-analysis"
date: "2019-03-12"
modified: "2022-05-17"
url: "https://alphaarchitect.com/reproducible-finance-with-r-code-flows-and-shiny-apps-for-portfolio-analysis/"
categories: ["Book Reviews"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Reproducible Finance with R: Code Flows and Shiny Apps for Portfolio Analysis

> R is a programming language that owes it’s lineage to S, a language designed in it’s own developers words, “to turn ideas into software, quickly […]

R is a programming language that owes it’s lineage to S, a language designed in it’s own developers words, “to turn ideas into software,  quickly and faithfully.”(1) Shiny is an “interactive web technology” that makes it easy to take R models and publish them to the web.

Jonathan L. Regenstein, Jr., the director of financial services at RStudio (an integrated development environment for R), walks us through both technologies in a portfolio analysis setting.

![](https://alphaarchitect.com/wp-content/uploads/2019/02/r-book.png)

* The book can be found [here](https://www.amazon.com/Reproducible-Finance-Portfolio-Analysis-Chapman/dp/1138484032/).
* Want to see all our [book reviews](https://alphaarchitect.com/category/continuous-content/book-reviews/#gs.ayZ0uqE)?

## What do I like about the book?

When I first joined Alpha Architect many of our financial models were exclusively in Excel and augmented with VBA code. Coming from Amazon, I was overwhelmed with VBA code and my eyes (and heart) started to bleed. Excel makes it very easy to write one-off simple programs and very difficult to write reproducible, maintainable programs.

R and Shiny fill this niche effectively. The book starts off with a crash course in a few common R packages. From there it dives into using those packages in a financial context. There are examples using the common data table libraries including *xts, tidyverse, tidyquant,* and *tibbletime.*

The book moves quickly from pulling down, cleaning, and producing returns data from the web to computing common statistical measures (standard deviation, skewness, kurtosis). The remainder of the book focuses on Portfolio theory including calculating Sharpe ratios, the CAPM, the Fama-French 3-factor model (including code that works verbatim for downloading data from the Fama French website), component contributions to standard deviation, and culminates in a full-blown web app running monte-carlo simulations.

We found the book compelling enough that we are planning on migrating many of our internal and external tools to R and the Shiny framework.

## Constructive Criticism

This is a book for practitioners; if you have not programmed in another language before this book will be very difficult. The book also moves through the Financial material very quickly.

In the author’s own words:

> The book seeks to be a resource for R coders interested in finance, or financiers who are interested in R or quantitative work generally.

The book also “prioritizes code that is understandable over code that is theoretically brilliant”. The code does have quite a bit of copy-paste and there are areas where adding a function or module would have cleaned up the code. Those who have an obsession for elegance, you have been warned.

## Summary

This book achieves it’s mission to teach finance professionals and programmers how to use R in a financial setting. While I’m still a far-cry from mastering R, the book did give me enough knowledge that we will be using it for modelling purposes going forward.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | *Chambers, John M (1998). Programming with Data: A Guide to the S Language. Springer.* [ISBN](https://en.wikipedia.org/wiki/International_Standard_Book_Number)[978-0-387-98503-9](https://en.wikipedia.org/wiki/Special:BookSources/978-0-387-98503-9)*.* |

 function footnote\_expand\_reference\_container\_45644\_157() { jQuery('#footnote\_references\_container\_45644\_157').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_45644\_157').text('−'); } function footnote\_collapse\_reference\_container\_45644\_157() { jQuery('#footnote\_references\_container\_45644\_157').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_45644\_157').text('+'); } function footnote\_expand\_collapse\_reference\_container\_45644\_157() { if (jQuery('#footnote\_references\_container\_45644\_157').is(':hidden')) { footnote\_expand\_reference\_container\_45644\_157(); } else { footnote\_collapse\_reference\_container\_45644\_157(); } } function footnote\_moveToReference\_45644\_157(p\_str\_TargetID) { footnote\_expand\_reference\_container\_45644\_157(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_45644\_157(p\_str\_TargetID) { footnote\_expand\_reference\_container\_45644\_157(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
