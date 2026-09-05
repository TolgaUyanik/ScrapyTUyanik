---
title: "Beware of Target Date Funds – Their Aim May be Way Off"
slug: "target-date-funds-aim-may-way-off"
date: "2015-11-03"
modified: "2015-11-03"
url: "https://alphaarchitect.com/target-date-funds-aim-may-way-off/"
categories: ["Guest Posts", "Behavioral Finance"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Beware of Target Date Funds – Their Aim May be Way Off

> We like to use rules of thumb, or heuristics, when facing choices. We often default to rules of thumb because when finding the optimal choice […]

We like to use rules of thumb, or heuristics, when facing choices.  We often default to rules of thumb because when finding the optimal choice is difficult, rules of thumb allow us to solve a problem quickly and move on in life.

While attending a lunch presentation by Charles Ellis at the recent Morningstar ETF Conference (which was a fantastic presentation and I am looking forward to reading his book “Falling Short”), I noticed that two investing/retirement rules of thumb were used in his presentation:

1. Use Target Date Retirement funds
2. The 4% withdrawal rule.

Being a geek, specifically regarding withdrawal rates in retirement, I immediately noticed an issue with these rules of thumb – they aren’t likely to be true if people follow both at the same time!  To understand why, we will need to 1) briefly review the history of withdrawal rates, then 2) move on to review some of the assumptions underlying the 4% withdrawal rule, and finally 3) do some Monte-Carlo simulations to see what the future might hold.

### History

The field of withdrawal rate research is fairly young.  Prior to 1994, financial advisers would estimate a rate of return for a portfolio and, using an amortization table, solve for the annual withdrawal that would leave a balance of $0 at the end of 30 years.

Not pleased with the previous method, in 1994 Bill Bengen wrote an article in the Journal of Financial Planning that was the source of the 4% withdrawal rule of thumb.  Specifically, Bengen used historical Ibbotson data and simulated a person starting retirement in 1926 who lived to 1956.  The portfolio was composed of *50% large cap stocks and 50% intermediate term government bonds*.  He solved for what starting percentage of the portfolio the person could withdrawal and then adjust that dollar amount up or down by inflation (subsequent years would have withdrawal rates very different than the initial percentage).  He then repeated this with a person starting retirement in 1927 through 1957 and continued repeating until he was out of historical data.  This produced a graph that looked like the following:

[![Target Date Funds_Begen Intial Withdrawal rates](https://alphaarchitdev.wpengine.com/wp-content/uploads/2015/11/Target-Date-Funds_Begen-Intial-Withdrawal-rates.jpg)](http://alphaarchitdev.wpengine.com/wp-content/uploads/2015/11/Target-Date-Funds_Begen-Intial-Withdrawal-rates.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Bengen noted that a **“safe”** withdrawal rate would be the lowest of these, which is approximately 4%.  This 4% withdrawal rate has since been tested by others using similar historical data and the 4% initial withdrawal rate finding was validated.

After several more years, people began to use Monte Carlo simulation to test the 4% initial withdrawal rate.  The assumptions for Monte Carlo used historical data (i.e., they assumed that stock and bond returns, variation in returns and correlations would be the same as history).  The Monte Carlo simulations, using historical data as inputs, showed that a *4% initial withdrawal rate worked in 95% of the simulations.*

The finding of the 4% initial withdrawal rate by Bengen and all subsequent studies are what is used as support for the 4% rule of thumb.  However, it is important to remember the **assumption** underlying the 4% rule of thumb:

1. 50% stock portfolio & 50% intermediate term government bond portfolio re-balanced annually every year through retirement. Even at age 94 you would have the same 50% stock & 50% bond allocation that you started with at age 65.

2. Withdrawals only have to last 30 years. Even if a 4% initial withdrawal rate would lead to bankruptcy after 31 years it wouldn’t matter because the money only had to last for 30 years.

3. One must assume that stock and bond returns will be the same as history.

There are **two issues** that I see that affect the assumptions of the 4% withdrawal rule 1) Target Date funds and 2) current yields.

### 1. Target Date Funds

Target date funds have a noble goal – to provide a low cost asset allocation solution in one fund for a person saving for and in retirement.  They are the ultimate “set it and forget it” investment choice.  I think this is a great tool and I have no issues with a Target Date fund per se.  In fact, they actually appear to improve the [behavior gap of investor](http://alphaarchitdev.wpengine.com/2015/08/17/the-sustainable-active-investing-framework-simple-but-not-easy/)s – that is Target Date fund investors appear to not jump in and out of the funds at the wrong times.

However, when it comes to taking a retirement nest egg and expecting a Target Date retirement fund to support an initial 4% withdrawal rate, investors might get a bit of a surprise.  This is because Target Date funds break one of the assumptions that was used to calculate the 4% initial withdrawal rate – they don’t maintain a constant 50% stock and 50% bond portfolio.  I graph the stock allocation of a typical target date fund, below:

[![Target Date Funds_Allocation in a typical target retirement date fund by age](https://alphaarchitdev.wpengine.com/wp-content/uploads/2015/11/Target-Date-Funds_by-age.jpg)](http://alphaarchitdev.wpengine.com/wp-content/uploads/2015/11/Target-Date-Funds_by-age.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

As you can see in the graph, above, a typical Target Date Retirement fund has a 50% allocation to stocks at the target retirement date (age 65), but it quickly decreases this allocation to about 30% allocation to stocks and keeps the 30% allocation to stocks through the remainder of retirement.

The difference in stock allocation changes the amount of an initial portfolio withdrawal rate.  Using the same method as Bengen, I solved for the initial withdrawal rate if one were to use a typical Target Date Retirement fund and graphed the results, below:

[![Target Date Funds_Initial withdrawal rates for typical target date retirement fund](https://alphaarchitdev.wpengine.com/wp-content/uploads/2015/11/Target-Date-Funds_Initial-withdrawal-rates-for-typical-target-date-retirement-fund.jpg)](http://alphaarchitdev.wpengine.com/wp-content/uploads/2015/11/Target-Date-Funds_Initial-withdrawal-rates-for-typical-target-date-retirement-fund.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The smallest initial withdrawal rate using a typical Target Date fund allocation is actually *3.5%* using historical data not the 4% rule of thumb.  In addition, the initial withdrawal rate using a typical Target Date fund is actually smaller every year than for a constant 50% stock and 50% bond portfolio.

I also tested the typical Target Date fund allocation using Monte Carlo analysis with historical data as inputs.  The Monte Carlo analysis shows that the typical Target Date fund *supports an initial withdrawal rate of 3.7% not the 4% rule of thumb* (this was calculated at a 95% success rate to make the two comparisons equivalent).

The finding of a lower withdrawal rate for allocations that decrease stock exposure over time (i.e., Target Date funds or glide paths) is not a new finding.  Bengen noted this in his original research and it has also been found by other researchers as well.

### 2. Current Yields

The 4% initial withdrawal rate assumes that stock and bond returns will be the same in the future as they were in the past.  However, we know that current intermediate term government bonds are priced to deliver a return of 0% above inflation compared to a historical return of 2.1% above inflation.

In addition, assuming that stock returns in excess of bonds (equity risk premium) doesn’t permanently increase in the future, the lower bond yields mean lower future stock returns as well.  The decreased returns from stocks and bonds will affect initial withdrawal rates in the future.

The effect of lower returns on withdrawal rates has been studied by [Pfau, Finke & Blanchett](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2201323) in a recent paper in the Journal of Financial Planning.  However, they studied the effect on portfolios with constant allocations to stocks and not a glide path used by Target Date funds.

Using the same Monte Carlo input assumptions as Pfau, Finke & Blanchett for bonds (0% real return) and stocks (4.8% real return), a typical Target Date fund would have a safe withdrawal rate of 2.7% at a 95% success rate (success rate chosen to be comparable to previous studies)!  Even if one were willing to accept a success rate of only 80% the initial withdrawal rate only increases to 3.3%.

The withdrawal rates using current yields and a typical Target Date fund are far less than the 4% initial withdrawal rate rule of thumb.

So what happens if people use a 4% initial withdrawal rate, a typical Target Date fund and we adjust return assumptions for current yields?  This person would be expected to run out of money 43% of the time before 30 years!  At current yields, using a typical Target Date allocation and the 4% rule is the financial equivalent of playing Russian roulette with half the chambers filled with live rounds.

### Conclusion

Low cost Target Date funds are an easy tool for investors to use when they are saving for and in retirement.  Target Date funds may even help people overcome poor investment behavior.  However, one should be aware of Target Date fund’s glide path and how that inter-plays with what initial withdrawal rate a retiree should be taking from their portfolio.  If they aren’t aware of those issues they risk playing Russian roulette with their retirement.

If you have any questions, [feel free to reach out](http://alphaarchitdev.wpengine.com/contact) and Wes will put us in touch.
