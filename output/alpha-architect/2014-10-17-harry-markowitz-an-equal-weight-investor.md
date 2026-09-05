---
title: "Harry Markowitz: An Equal-Weight Investor?"
slug: "harry-markowitz-an-equal-weight-investor"
date: "2014-10-17"
modified: "2022-05-03"
url: "https://alphaarchitect.com/harry-markowitz-an-equal-weight-investor/"
categories: ["Research Insights", "Tactical Asset Allocation Research"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Harry Markowitz: An Equal-Weight Investor?

> Jason Zweig’s book, “Your Money and Your Brain” highlights an interesting conversation with Harry Markowitz. Dr. Markowitz is a Nobel Prize winner and his work […]

Jason Zweig’s book, “[Your Money and Your Brain](http://books.google.com/books?id=gRdOBrus_9wC&pg=PA4&lpg=PA4&dq=your+money+and+your+brain+harry+markowitz&source=bl&ots=awRnIfjIl7&sig=Kj1dFG2J6FX96I7uan8AYs2jp5w&hl=en&sa=X&ei=gkU3VOSbFevesASY64LQBA&ved=0CB4Q6AEwAA#v=onepage&q=your%20money%20and%20your%20brain%20harry%20markowitz&f=false)” highlights an interesting conversation with Harry Markowitz. Dr. Markowitz is a Nobel Prize winner and his work on mean-variance-analysis laid the foundation for all of modern portfolio theory.

Not too shabby for a financial economist.

We’ll come back to the quote in a moment, but first let’s review some general observations on [Markowitz’s mathematically sophisticated approach to asset allocation](https://www.math.ust.hk/~maykwok/courses/ma362/07F/markowitz_JF.pdf).

Although Markowitz did win a Nobel Prize, and this was partly based on his elegant mathematical solution to identifying mean-variance efficient portfolios, a funny thing happened when his ideas were applied in the real world: [**mean-variance performed poorly**.](http://faculty.london.edu/avmiguel/DeMiguel-Garlappi-Uppal-RFS.pdf)

The fact  that a Nobel-Prize winning idea translated into a no-value-add-situation for investors is something to keep in mind when considering any optimization method for asset allocation.

The cautionary tale regarding mean-variance-based model performance heavily influenced the lecture I gave a few weeks ago at the [Morningstar ETF conference](https://alphaarchitect.com//2014/09/29/complexity-doesnt-equal-value-morningstar-video/#.VDdEHvldVMU) where I presented the [following slides](https://alphaarchitect.com//2014/09/23/morningstar-2014-etf-conference-slides/).  
My key takeaway from the chat was that **COMPLEXITY DOES NOT EQUAL VALUE.**

I supported this statement by highlighting that a variety of complex tactical asset allocation frameworks can’t stand toe-to-toe with the simple 1/n, or equal-weight asset allocation model.

### **Why Do Complex Models Fail?**

Estimating the covariance matrix is notoriously unstable, so therefore, the “optimized” weights spit out from a model influenced by an unstable covariance matrix would also end up being unstable and unreliable. (For a detailed discussion of this issue, you can review the “Complexity” section in this [post](/2014/09/a-framework-for-investment-manager-selection-stick-to-the-facts/) from about a month ago)

The proof is in the pudding: [equal-weight allocations seem to reliably beat complicated allocations.](http://faculty.london.edu/avmiguel/DeMiguel-Garlappi-Uppal-RFS.pdf)

Not soon after the Morningstar event, one of my partners–[Jack Vogel](https://alphaarchitect.com/user/jack.vogel%2c.phd/)–ran across a quote by Harry Markowitz that was fairly amusing:

> I should have computed the historical covariance of the asset classes and drawn an efficient frontier…I split my contributions 50/50 between bonds and equities.

In this context, Markowitz’s discussion is meant to highlight the power of behavior over reason. Markowitz pokes fun at himself: he knew he should have followed his own elegant model, but instead he ignored it. There’s an irony here: in light of a few more decades of out-of-sample evidence, it turns out his behaviorally-driven decision (i.e., equal-weight simplicity) probably really was the correct approach after all.  
[![Your Money and Your Brain_ How the New Science of Neuroeconomics Can Help ... - _2014-10-09_22-24-46](https://alphaarchitect.com/wp-content/uploads/2014/10/Your-Money-and-Your-Brain_-How-the-New-Science-of-Neuroeconomics-Can-Help-...-_2014-10-09_22-24-46.png)](http://books.google.com/books?id=gRdOBrus_9wC&pg=PA4&lpg=PA4&dq=your+money+and+your+brain+harry+markowitz&source=bl&ots=awRnIfiMs4&sig=sY4wPziYOjm9oB5f3MN_z7gloMw&hl=en&sa=X&ei=bEM3VKT9MIjIsATj_4Fw&ved=0CB4Q6AEwAA#v=onepage&q=your%20money%20and%20your%20brain%20harry%20markowitz&f=false)  
So the founder of modern portfolio theory uses an equal-weight allocation. And one of the central assumptions underlying mean-variance optimization is that investors care about risk and return trade-offs. Yet, as Markowitz highlights, his decision-making framework has little to do with risk and return trade-offs. In the year 2014, now that we have a long enough data trail, we can show that Markowitz’s model doesn’t outperform a simple equal-weight allocation. The reason for this underperformance is a not critique on the model, which is clearly an incredible intellectual achievement, but has everything to do with the practical realities of accurately estimating a covariance matrix. So Markowitz’s 1/N approach was right, but for the wrong reasons. He was right that a simple 1/n allocation strategy was appropriate, but his reason – that he wanted to minimize his future regret – was the wrong one. The right answer is that good models don’t necessary translate into good practical ideas.

Holy cow. Someone should write a financial economic soap opera on this story…
