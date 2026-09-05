---
title: "Value investing backtests: Our analysis of 13 AAII Value Strategies"
slug: "value-investing-backtests-our-analysis-of-13-aaii-value-strategies"
date: "2014-10-20"
modified: "2022-05-31"
url: "https://alphaarchitect.com/value-investing-backtests-our-analysis-of-13-aaii-value-strategies/"
categories: ["Research Insights", "Value Investing Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Value investing backtests: Our analysis of 13 AAII Value Strategies

> Having spent 15+ years conducting value investing backtests to find the holy grail of systematic value investing, I sometimes wonder the following: Is there any […]

Having spent 15+ years conducting value investing backtests to find the holy grail of systematic value investing, I sometimes wonder the following: Is there any concept or idea out there that **we HAVE NOT examined**?

The problem is that most of the ideas we test come from internal ideas/discussions and/or academic research articles. We rarely look to practitioners as a source for ideas.

A while ago, [Meb Faber](http://mebfaber.com/2013/03/18/aaii-updates/) suggested that we examine the value strategies posted to the [American Association of Individual Investors](http://www.aaii.com/authors/wesley-gray) value-based stock screens:

[![The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.](https://alphaarchitect.com/wp-content/uploads/2014/10/Portfolio-Characteristics-_-AAII_-The-American-Association-of-Individual-Investo_2014-10-20_07-32-53-1030x635.png)](https://alphaarchitect.com/wp-content/uploads/2014/10/Portfolio-Characteristics-_-AAII_-The-American-Association-of-Individual-Investo_2014-10-20_07-32-53.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### [Does Complexity Imply Value? AAII Value Strategies from 1963 to 2013](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2511090)

* Gray, Vogel, and Xu
* A PDF version of the paper can be found [here.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2511090)
* Want a summary of academic papers with alpha? Check out our [Academic Research Recap Category](https://alphaarchitect.com/category/academic-research/).

### **Abstract:**

> We compare the performance of 13 value investing screens used by practitioners against a simple model based on buying stocks with the lowest enterprise multiple. Our sample of value investing screens underperform the simple lowest enterprise multiple strategy. The one exception is the Piotroski F-Score screen, which has similar performance relative to the enterprise multiple strategy. **Overall, the evidence suggests that simple value investing models can perform just as well as, if not better than, more complex value investing models.**

### **Alpha Highlight:**

Before we discuss the results of our research, let’s first define what a value investing backtest is.

A **value investing backtest** looks to examine how a specific value strategy performed over a certain period of time in the past. The goal is to get a sense for how it is likely to respond to certain variables, so you can optimize its potential to outperform.

We analyzed 13 different value screens posted to the site and our favorite valuation metric–EBITDA/TEV.

We assessed all of these strategies using our best-in-class backtesting technology and procedures.  At times our approach differs, at the margin, relative to the AAII screens. We also focus on a large liquid universe and incorporate delisting information using [the appropriate algorithms.](http://richardp.bus.usu.edu/research/bmp_delistings.pdf) In other words, our study serves as a “second opinion” on the various value strategies proposed on the website.

The strategies we analyzed are as follows:

1. **Fundamental Rule of Thumb (FRT).**  This screen excludes ADRs, financials, and real estate firms. Passing firms need to have their total liabilities to total assets ratio less than or equal to the universe’s median ratio. The fundamental rule of thumb is constructed by adding earnings yield, retained earnings to book value, and dividend yield. Earnings yield is earnings per share divided by the price of the common stock. Retained earnings to book value is earnings per share minus dividends per share divided by book value per share. Dividend yield is dividend per share divided by the price of the common stock. Final results are top 50 companies with highest fundamental rule of thumb values.
2. **Graham Enterprising Screen (GR\_ES).** This strategy is loosely based on Ben Graham writings. Criteria are as follows: price to earnings ratio’s rank is less than or equal to 10th percentile (lowest 10% of the universe); current ratio is greater than or equal to 1.5; long-term debt to working capital is between 0 and 1.1; EPS in each of the last five years have been positive; EPS of last fiscal year (and trailing 12 months) is greater than EPS from five years ago; company has paid a dividend over the last 12 months; price-to-book ratio is less than or equal to 1.2.
3. **Graham Defensive Utility (GR\_D\_U).**  This screen only includes companies in the utility sector. Criteria are as follows: long-term debt-to-equity ratio of the last fiscal year is less than 2; EPS in each of the last seven fiscal years have been positive; seven years EPS geometric growth rate is greater than 3%; a dividend has been paid in the last seven fiscal years; price-to-earnings ratio (using average of past 3 year earnings) is less than or equal to the inverse of the AAA yield plus 2; the product of the price-to-earnings ratio multiplied by the price-to-book ratio is less than or equal to 1.5 times the inverse of the AAA yield plus 2.
4. **Graham Defensive Non-Utility (GR\_D\_NU).**  This screen excludes companies in utility sector. Criteria are as follows: long-term debt-to-equity ratio of the last fiscal year is less than 2; long-term debt to working capital is between 0 and 1.1, exclusive; EPS in each of the last seven fiscal years have been positive; seven years EPS geometric growth rate is greater than 3%; dividend has been paid in the current year and in each of the last seven fiscal years; price-to-earnings ratio (using average of past 3 year earnings) is less than or equal to the inverse of the AAA yield plus 2; the product of the price-to-earnings ratio multiplied by the price-to-book ratio is less than or equal to 1.5 times the inverse of the AAA yield plus 2.
5. **Graham Enterprising Investor Revised (GR\_E\_I).**  This screening is slight revision of the Graham Enterprising Screen. Criteria are as follows: price to earnings ratio’s rank is less than or equal to 25th percentile (lowest 25% of the universe); current ratio is greater than or equal to 1.5; long-term debt to working capital is less than 1.1; EPS in each of the last five years have been positive; EPS of the last fiscal year (and trailing 12 months) is greater than EPS from five years ago; company has paid a dividend over the last 12 months; price-to-book ratio is less than or equal to 1.2.
6. **Magic Formula (MF).** This screen seeks to find the best combination of value and quality. The screen excludes financial and utility companies. First, companies need to have return on capital greater than 25% (return on capital is calculated from earnings before interests and taxes divided by total tangible capital). Finally, the screen selects 30 stocks with the highest earnings yield (earnings yield is EBIT divided by enterprise value).
7. **Dogs of the Dow 10 (DOW 10).** This screen only includes Dow Jones industrial average composite companies. The screen only includes the 10 highest dividend yielding stocks.
8. **Dogs of the Dow 5 (DOW 5).**  This screen only includes Dow Jones industrial average composite companies. The screen only includes the 5 highest dividend yielding stocks.
9. **Cash Rich Firms (CRF).** This screen excludes financial, utility and real estate firms. Criteria are as follows: EPS of the last fiscal year is positive; stock price is higher than $5.00; total liabilities to total assets ratio of the last fiscal year is less than the industry’s median ratio; long-term debt to total capital ratio of the last fiscal year is less than the industry’s median ratio; cash to price is greater than 20; cash per share is at least 20% of the stock price; net cash (cash after current liabilities) to price is greater than 20; net cash per share is at least 20% of the stock price.
10. **Piotroski High F-Score (FSCORE).**  This screen is based on the methodology in Piotroski and So (2012).  Their methodology involves computing 9 signals. Of the nine financial performance signals, four of the signals are based on profitability; three are based on changes in financial leverage and liquidity; and two are based on operational efficiency.   Firms need to be in the top 20% of the universe based on book to market to be included. Firms also need to score an 8 or a 9 on the Piotroski 9 point scale.
11. **Price to Free Cash Flow (PFCF).** Financial and real estate companies are excluded. Criteria are as follows: free cash flow per share of each of the last five fiscal years has been positive; price to free cash flow per share ratio is lower than the industry’s median ratio; price to free cash flow per share ratio is lower than the company’s five year average ratio. Final companies are those 30 companies with the lowest price-to-free cash flow per share ratio.
12. **Weiss Blue Chip Dividend Yield (WEISS).** Real estate companies are excluded. Criteria are as follows: dividends have been paid in each of the last seven fiscal years; dividends have been increased at least three times and have never been decreased in the last seven fiscal years; numbers of share outstanding in the last fiscal year is greater than or equal to five millions; institutional ownership is greater than 50%; EPS have increased at least four times over the last seven fiscal years; current dividend yield is within 10% of the seven year average dividend yield; current ratio of last fiscal year is greater than or equal to 2; for utility companies the dividend payout ratio of the last fiscal year is less than or equal to 0.85; for non-utility companies, the long-term debt to equity ratio of the last fiscal year is less than or equal to 0.5 and the dividend payout ratio of the last fiscal year is less than or equal to 0.5.
13. **O’Shaughnessy Value Screen (O’SH\_V).** Utility companies are excluded. Criteria are as follows: the market capitalization is greater than the average market capitalization of the universe; the numbers of shares outstanding from the last fiscal year is greater than the average of the universe; cash flow per share of the last fiscal year is greater than the average of the universe; total sales of the last fiscal year is greater than 1.5 times the average of the universe. Final companies are those 50 companies with the highest dividend yield.
14. **EBITDA/TEV (EBITDA/TEV).** All financial firms are excluded. Similar to the Loughran and Wellman (2011), we compute Total Enterprise Value (TEV) as Market Capitalization + Short-term Debt + Long-term Debt + Preferred Stock Value – Cash and Short-term Investments. Earnings before interest and taxes and depreciation and amortization (EBITDA) is computed as Operating Income Before Depreciation  + Non-operating Income. The simple value strategy involves selecting the top decile of firms ranked on EBITDA/TEV (enterprise multiple).

### Now, for the value investing backtest results!

Here are the main results of the value investing backtests:

[![AAII_horserace_v01.docx - Microsoft Word_2014-10-20_07-44-00](https://alphaarchitect.com/wp-content/uploads/2014/10/AAII_horserace_v01.docx-Microsoft-Word_2014-10-20_07-44-00-1030x427.png)](https://alphaarchitect.com/wp-content/uploads/2014/10/AAII_horserace_v01.docx-Microsoft-Word_2014-10-20_07-44-00.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

We also run a horse race between EBITDA/TEV and FSCORE–the two top-performing metrics in this study. FSCORE wins!

[![AAII_horserace_v01.docx - Microsoft Word_2014-10-20_07-45-56](https://alphaarchitect.com/wp-content/uploads/2014/10/AAII_horserace_v01.docx-Microsoft-Word_2014-10-20_07-45-56-1030x640.png)](https://alphaarchitect.com/wp-content/uploads/2014/10/AAII_horserace_v01.docx-Microsoft-Word_2014-10-20_07-45-56.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### Concluding thoughts on value investing backtests

We’ll simply quote our own paper:

> We find that more complex value strategies on AAII, on average, underperform the simple EBITDA/TEV ratio. However, the “Piotroski High F-Score Screen (FSCORE),” which is a close approximation to the strategy outlined in Piotroski (2000) and Piotroski and So (2012), has similar performance.
>
> For mid and large-cap firms, an annually rebalanced equal-weight portfolio of FSCORE firms earns 16.74% a year, a 0.70 Sharpe Ratio, and a 0.332% monthly 4-factor alpha. These results are similar for a simple EBITDA/TEV value stock screen, which earns 16.52% a year, a 0.65 Sharpe Ratio, and a 0.370% monthly 4-factor alpha. Overall, the evidence suggests that simple value models can perform just as well, if not better, than more complex value models.

If you are looking to understand how to backtest value investment strategies, there is no set formula. We would suggest that you experiment with your own data set and process. And of course, being open to new ideas and thoughts you may encounter along the way never hurts…

In summary, when it comes to value investing backtests, complexity doesn’t seem to add much value. However, focusing on cheap stocks and using some element of fundamental analysis to separate winners from losers does seem to add value, at the margin.
