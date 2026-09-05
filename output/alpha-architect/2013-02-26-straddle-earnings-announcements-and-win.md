---
title: "Straddle Earnings Announcements and Win!"
slug: "straddle-earnings-announcements-and-win"
date: "2013-02-26"
modified: "2022-04-29"
url: "https://alphaarchitect.com/straddle-earnings-announcements-and-win/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Straddle Earnings Announcements and Win!

> Anticipating Uncertainty: Straddles Around Earnings Announcements Yuhang Xing and Xiaoyan Zhang A version of the paper can be found here. Want a summary of academic papers […]

### Anticipating Uncertainty: Straddles Around Earnings Announcements

* Yuhang Xing and Xiaoyan Zhang
* A version of the paper can be found [here.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2204549)
* Want a summary of academic papers with alpha? Check out our free [Academic Alpha Database](https://alphaarchitect.com/tools/)!

### **Abstract:**

> On average, straddles on individual stocks earn significantly negative returns: daily holding period return is -0.19% and weekly holding period return is -2.09%. In sharp contrast, straddle returns are significantly positive around earnings announcements: average at-the-money straddle returns from one day before earnings announcement to the earnings announcement date yields a highly significant 2.3% return. The positive straddle returns around earnings announcements are robust to different stock and option characteristics. This finding suggests that investors underestimate the magnitude of uncertainty during the earnings announcement period, consistent with the cognitive bias “conservatism.” Furthermore, we find the underestimation of uncertainty is more pronounced for smaller firms, firms with less analyst coverage, higher past jump frequency, higher kurtosis and more volatile past earnings surprises. This supports the notion that when there is more noise in the data, it is more likely for investors to display “conservatism.”

### **Data Sources:**

Option Metrics, IBES, CRSP, and COMPUSTAT from 1996 to 2010.

### **Alpha Highlight:**

[![ssrn-id2204549](https://alphaarchitect.com/wp-content/uploads/2013/02/ssrn-id2204549.png)](https://alphaarchitect.com/wp-content/uploads/2013/02/ssrn-id2204549.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

### **Strategy Summary:**

1. Using at-the-money (stock price/strike price between 0.95 and 1.05), create a delta neutral straddle around earnings announcments for each specific company. 
   * The paper uses different ranges for holding periods, such as [-6,1] and [-3,0].  Results are similar for different holding periods.
   * Only options included are those with maturities between 10 and 60 days.
2. Average EW holding period returns are 3.00% for straddle using [-3,0] as holding period!
3. To improve returns, paper shows that investing in small growth companies, firms with fewer analysts, firms with higher past return volatilities, firms with higher past jump intensities, firms with higher past earnings surprises, and firms with larger variance in historical earnings surprises appear to have better returns.
4. When accounting for transaction costs, returns decrease 
   * To account for this, a possible trading strategy would be to buy the straddle on day -3 and hold until maturity.
   * However, this only works when using options with maturities between 4 and 10 days.

### **Commentary:**

* Appears that after accounting for transaction costs, this only works for near-term straddles
* Only 18% of firms announce earnings within 10 days of option maturity, so this strategy may only be tradeable for a smaller subset of firms.
