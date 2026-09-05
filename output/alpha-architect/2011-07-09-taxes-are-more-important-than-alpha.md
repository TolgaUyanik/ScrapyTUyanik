---
title: "Taxes are more important than alpha."
slug: "taxes-are-more-important-than-alpha"
date: "2011-07-09"
modified: "2026-02-17"
url: "https://alphaarchitect.com/taxes-are-more-important-than-alpha/"
categories: ["Research Insights", "Tax Efficient Investing"]
tags: ["Taxes", "tax efficient rebalancing"]
best_of: false
source: "alphaarchitect.com"
---

# Taxes are more important than alpha.

> Paying taxes is my least favorite topic. Figuring out how to not pay taxes is my favorite topic. Before I continue, if you want to read […]

**Paying taxes** is my least favorite topic.

Figuring out how to **not pay taxes** is my favorite topic.

Before I continue, if you want to read a detailed study on the subject, see the following:  
<https://www.vanguard.com/pdf/icrpr.pdf>

If you want to read my [“Barney Style”](http://www.urbandictionary.com/define.php?term=barney%20style) study, keep on reading…

### **Quick study on tax efficient rebalancing:**

Let’s pretend you have an annually rebalanced quant strategy–go long top 200 low asset growers in the investment universe, for example. The strategy seems simple enough, but how does one rebalance the portfolio each year?

I went ahead and did a simplified study of tax-efficient yearly rebalancing vs. tax-inefficient rebalancing.

Here is a summary of the approach (which isn’t meant to reflect perfect reality, but to prove a basic point):

* I do 1000 simulations of 10 years of annual returns with a mean of 10% and a standard deviation of 20% (roughly what the market does each year).
* I assume long-term cap gains are 20%, and short-term cap gains are 40%.
* The efficient portfolio works as follows: if it is a loser year, the portfolio liquidates at 364 days, pays taxes, and rebalances the next day; if the portfolio is a winner year, it liquidates at 366 days, pays taxes at the end of the tax year (build in deferral), and rebalances that next day.
  + I assume there is 100% turnover to avoid wash sale complications (e.g., none of the stocks in the previous portfolio, show up in the ‘fresh’ portfolio).
  + I also allow realized losses to carry over from year to year to be applied against gains within the 10-year window of each simulation (so each 10-year simulation outcome is path dependent).
* The inefficient portfolio liquidates at 365 days each year, eats a 40% tax bill, and rebalances.

Here is a histogram of the simulation results:

[![](https://alphaarchitect.com/wp-content/uploads/2011/07/tax.png)](https://alphaarchitect.com/wp-content/uploads/2011/07/tax.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

In this simple setup, simply rebalancing in a tax efficient way adds 2-5%+ CAGR to your after-tax return–over a 10, 20, or 30-year period, that is some SERIOUS MONEY!

### **Key Takeaway?**

1. Stop reading this blog trying to find alpha…
2. Go out there and find a great tax attorney and CPA!
