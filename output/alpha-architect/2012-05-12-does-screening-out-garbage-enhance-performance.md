---
title: "Does Screening out Garbage Enhance Performance?"
slug: "does-screening-out-garbage-enhance-performance"
date: "2012-05-12"
modified: "2022-06-10"
url: "https://alphaarchitect.com/does-screening-out-garbage-enhance-performance/"
categories: ["Research Insights", "Corporate Governance"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Does Screening out Garbage Enhance Performance?

> Jack and I are working on a new research paper that addresses a very simple question: Can investors improve their screening process by eliminating frauds, […]

Jack and I are working on a new research paper that addresses a very simple question:

> Can investors improve their screening process by eliminating frauds, manipulators, and financially distressed firms?

Answering this question appears easy, but as Cliff Asness and Andrea Frazzini point out in their recent paper, “[The Devil in HML’s Details](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2054749),” the devil is *REALLY* in the details.

* How does one identify frauds?
* How does one identify manipulators?
* How does one identify financially distressed firms?
* And *most importantly*, how does one identify frauds, manipulators, and financially distressed firms BEFORE the market has already priced in the risks of fraud, manipulation, or distress?

Luckily, we can stand on the shoulders of academic research ([and create our own!](http://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=432318)) and take a stab at addressing our original question. The academic literature describes techniques that help identify frauds, manipulators, and financially distressed firms before the market.

### Here is a helicopter tour of the literature we enjoy most:

**Frauds and manipulators:**

* [Beneish (1999)](http://myweb.ncku.edu.tw/~r16001205/w7.1_ProbM_Model.FAJ.1999.pdf): The Detection of Earnings Manipulation
* [Sloan (1996):](http://acct.tamu.edu/giroux/sloan(1996).pdf) Do Stock Prices Fully Reflect Information in Accruals and Cash Flows About Future Earnings?
* [Hirshleifer et al. (2004):](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=404120) Do Investors Overvalue Firms with Bloated Balance Sheets?

**Financial Distress:**

* [Campbell, Hilscher, and Szilagyi (2008)](http://kuznets.fas.harvard.edu/~campbell/papers/campbellhilscherszilagyi_jf2008.pdf): In Search of Distress Risk ([Discussion Piece](http://www.rhsmith.umd.edu/finance/pdfs_docs/Symposium2007/John.pdf) that is more “Barney Style”)
* [Campbell, Hilscher, and Szilagyi (2010):](http://scholar.harvard.edu/campbell/files/financialdistress_campbellhilscherszilagyi_joim.pdf) Predicting Financial Distress and the Performance of Distressed Stocks (similar to above but with data out to 2008, see Table 2 and compare to Table IV in older version)

### Preliminary Chart Porn:

First, a look at the entire distribution of firms’ 1-year Buy-and-hold 1-year returns from 1973 through 2011.

[![](https://alphaarchitect.com/wp-content/uploads/2012/05/Microsoft-Excel-histogramanalysis_v02-300x214.png "Microsoft Excel - histogramanalysis_v02")](https://alphaarchitect.com/wp-content/uploads/2012/05/Microsoft-Excel-histogramanalysis_v02.png "Microsoft Excel - histogramanalysis_v02")

[Click to Enlarge] The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Next, a detailed look at the left tail.

[![](https://alphaarchitect.com/wp-content/uploads/2012/05/closeup-204x300.png "closeup")](https://alphaarchitect.com/wp-content/uploads/2012/05/closeup.png "closeup")

[Click to Enlarge] The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Next, a simple robustness test: Here we present the same analysis as above, but only for stocks that are greater than the NYSE 40% market cap benchmark at a given point in time (this benchmark was ~$1.4B as of December 31, 2011).

[![](https://alphaarchitect.com/wp-content/uploads/2012/05/Fig0402-300x216.png "Fig0402")](https://alphaarchitect.com/wp-content/uploads/2012/05/Fig0402.png "Fig0402")

[Click to Enlarge] The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### How did we create this?

In short, it’s complicated.

We calculate scores on all the fraud, manipulation, and distress factors outlined in the papers above, and eliminate any firms in the bottom 5% (the real scum of the earth).

If you want a more detailed overview of the process, check out our book, Quantitative Value.
