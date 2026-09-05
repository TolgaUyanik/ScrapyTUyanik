---
title: "The Robust Asset Allocation (RAA) Index"
slug: "the-robust-asset-allocation-raa-index"
date: "2014-12-02"
modified: "2026-05-21"
url: "https://alphaarchitect.com/the-robust-asset-allocation-raa-index/"
categories: ["Best of Factor Investing", "Research Insights", "Introduction Course", "Key Research", "Tactical Asset Allocation Research"]
tags: []
best_of: true
source: "alphaarchitect.com"
best_of_section: "Factor Investing"
---

# The Robust Asset Allocation (RAA) Index

> Robust asset allocation solutions should be relatively simple, minimize complexity, and be robust across different market regimes. Simultaneous to these requirements, the solution must be affordable, liquid, simple, tax-efficient, and transparent, otherwise, many of the benefits of the solution will flow to the croupiers and Uncle Sam. We recommend that investors explore our robust asset allocation framework and go for the do-it-yourself solution. You’ll be paying yourself 1%+ a year via saved RIA fees. Is this the only solution? No. But any solution must be robust, simple, tax-manageable, and low-cost. This is our best effort to develop a simple model. Developing a complicated model is easy; simple is difficult.

This article discusses the Robust Asset Allocation (RAA) index, a dynamic algorithm we have developed.

**Robust:** capable of performing without failure under a wide range of conditions

–[Merriam-Webster Dictionary](https://www.merriam-webster.com/dictionary/robust)

## The Investor’s Dilemma

Many investors face a fundamental problem: **What should I do with my money?**

People usually pursue one of four broad solutions to this problem:

1. Hire an expensive investment advisor that invests in overpriced active management.
2. Hire an affordable advisor that invests in what amounts to a 60/40-ish portfolio.
3. Hire a cheap robo-advisor that invests in what amounts to a 60/40-ish portfolio.
4. Hire an affordable advisor that invests in *something different* than the 60/40-ish portfolio.

Option #1 (hire an expensive investment advisor) is clearly a bad idea, but the options #2, #3, and #4 are all worth consideration.

As far as option #2 (hire an affordable advisor), plenty of affordable, honest, independent advisors charge reasonable prices for the value they deliver. You’ll probably get a portfolio that mirrors a 60/40-ish portfolio, but you’ll also have access to financial planning, behavioral coaching, and peace of mind (~50-125bps all-in).

Option #3 (hire a cheap robo-advisor) is interesting as well, and there are plenty of dirt-cheap automated options that may not deliver the peace of mind a human advisor can deliver (at least not yet), but they also don’t charge that much for their 60/40-ish options. (~30-60bps all-in).

Finally, option #4 (hire an affordable advisor that invests in something different than the 60/40-ish portfolio) is also reasonable if the differentiated investment approach is affordable *and* better at helping an investor achieve an investment goal relative to the 60/40-ish portfolio (~50-200bps all-in).

Options #2 and #3 are probably best for a wide swath of financial consumers, but option #4 is certainly interesting for those with specialized investment goals and sound discipline. Option #4 is the topic of this piece.

(1)

## A 60/40-ish Portfolio Isn’t Gonna Cut it For My Situation. What Should I do?

First, we recommend all investors trying to tackle the, “What should I do with my money?” question, grab a copy of our book [DIY Financial Advisor](http://www.amazon.com/gp/offer-listing/111907150X/ref=tmm_hrd_new_olp_sr?ie=UTF8&condition=new&qid=1441113002&sr=1-1), which outlines the concepts discussed in this post but in much greater detail.  The book will prepare you with the knowledge to ask the right questions if you are interviewing financial advisors and/or it will give you the necessary tools to be a successful Do-It-Yourself investor.

(2)

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/diybook.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/diybook.png)

DIY Financial Advisor

Okay, so you’ve powered through the DIY book or punted on that option since you’d instead just read this blog post. Either way, you are faced with an investment decision and you consider the following:

Easiest solution:  60% global equity; 40% global bond  (or your own special weights depending on individual circumstances).

* Cheap. Easy.
* A reasonable approach. Totally DIY-able.
* This is a personal question, but something one should always consider: *Is this portfolio achieving your objectives?*

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/simple-allocation-1030x607.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/simple-allocation.png)

Easy solution:

Meb Faber and Eric Richardson (RIP) in their book, The Ivy Portfolio, hint at a do-it-yourself model that is a simple portfolio that allocates across US equity, developed equity, REITs, commodities, and US Treasury bonds. These 5 asset classes are commonly called the “IVY 5,” since they form the basic building blocks for the endowments of the Ivy League schools and others. This can be a reasonable allocation to achieve some investor’s goals. We’ll discuss this framework and why it is an exciting starting point for those trying to achieve an objective that may differ from those blindly allocating to a generic 60/40 portfolio.

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/meb-solution-1-1030x561.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/meb-solution-1.png)

## Robust Asset Allocation (RAA) Index:

The Robust Asset Allocation (RAA) Index is a dynamic algorithm we built with a specific goal: **RAA seeks capital appreciation with downside protection.** (3)

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/raa-goal-1030x123.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/raa-goal.png)

The tactical objectives of our RAA indexes are as follows:

* Portfolio growth that keeps up with inflation (principal growth)
* Downside protection (avoid large drawdowns)
* Superior tax efficiency (tax-savvy investing)
* Liquidity (facilitates flexibility)

Different investors have different objectives, but if your goal is to capture global asset returns, but at the same time you’d like to minimize the chance of a complete meltdown, our fully transparent RAA Indexes may be an interesting approach to explore.

There are three flavors of the RAA Index — balanced, moderate, and aggressive.

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/3-flavors-of-raa-1030x412.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/3-flavors-of-raa.png)

Let’s start understanding the nuts and bolts of our RAA Indexes.

## Core Premise: Financial Advice can be Simple and Effective

Our seed investor, who also happens to be a multi-billionaire and knows a lot more about investing than we could ever hope to achieve, has a great quote:

> Wealth is *built* by concentrated holdings, but wealth is *protected* by diversification.

In short, if the goal is to get super rich, diversification and risk-management are arguably terrible ideas. A better idea is to concentrate on a single holding (i.e., build a business) and shoot for the stars. Of course, if your goal is to protect your wealth, diversification is a much more prudent approach. But there is no right answer. Goals are dependent on the investor and the specific objectives they want to achieve.

Once goals are established, we need financial advice to identify an investment solution that will achieve our goal. Remarkably, financial advice does not need to be complex to be effective. Our belief is based on a robust view of the evidence and my Marine Corps brainwashing to focus on having “brilliance in the basics.”

Complexity is often a smokescreen that hides a conflict of interest. For example, there are [known incentives](https://alphaarchitect.com/2015/03/11/understanding-wall-streets-conflict-of-interest-problem/) for financial firms to generate complexity in order to justify their existence. There are also [well-established dangers](https://alphaarchitect.com/2017/03/03/evidence-based-investing-take-alpha-shove/) associated with data-mining and whipping the data until it says what you want. Good financial advice should minimize both scenarios, if possible.

To summarize, we are biased towards simplicity because it works and also has the following benefits:

1. Simple processes are less susceptible to data-mining.
2. Simple processes are harder to disguise as black-box solutions that charge higher fees.

Our beliefs serve as the cornerstone of how we build investment algorithms. We aim to keep things simple and effective.

### Three Elements of Simple and Effective Financial Advice

We break our discussion into three sections:

1. **Asset Allocation:** Instead of complex asset allocation, use simple allocation.
2. **Security Selection:** Instead of story-based stock selection, use evidence-based stock selection.
3. **Risk Management:** Instead of buy-and-hold, use a downside-protection system.

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/3-steps-1030x538.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/3-steps.png)

Charts presented are for illustrative purposes only. Our downside protection models may not work in all situations and could fail to achieve their objectives.

Each of these elements form the building blocks of the Robust Asset Allocation Index, which we discuss in the following three sections.

## #1 Asset Allocation:  Instead of complex asset allocation, use simple allocation

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/step-1.-simple-asset-allocation.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/step-1.-simple-asset-allocation.png)

Charts presented are for illustrative purposes only. Our downside protection models may not work in all situations and could fail to achieve their objectives.

> “Of the 14 models we evaluate across seven empirical datasets, none is consistently better than the 1/N rule…”
>
> — DeMiguel, Garlappi and Uppal.

Victor DeMiguel and his colleagues have explored many sophisticated methodologies to [optimize asset allocation](http://faculty.london.edu/avmiguel/papers.html). They have solutions that can possibly beat an equal-weight allocation, but these alternative solutions add a high degree of [complexity](http://faculty.london.edu/avmiguel/DPUV-JFQA-2014.pdf). Prof. DeMiguel has an outstanding outline of [data-driven investment management](http://faculty.london.edu/avmiguel/Data-Driven-Investment-Management-CMS-unabridged.pdf) if you’d like to explore further. We’ve discussed the academic rationale for following a simple asset allocation model in the past, [here](https://alphaarchitect.com//2014/10/17/harry-markowitz-an-equal-weight-investor/#.VHPBO4vF9MU), and [here](https://alphaarchitect.com//2012/11/05/tactical-asset-allocation-series-part-2-equal-weight/#.VHPBYYvF9MU).

An equal-weight portfolio–also suggested by DeMiguel et al.–would seem to fly in the face of modern portfolio management, which in general has suggested that investors rely on mean-variance type allocation, or other highly engineered schemes. However, while mean-variance-analysis has reverse engineered the best historical Sharpe ratio (i.e. the tangency portfolio), this solution relies on a correlation matrix input, which is highly unstable and difficult to estimate. Indeed other approaches have this same weakness.(4)

DeMiguel et al. are not the only researchers suggesting that simplicity often rules the day when it comes to asset allocation. Even the great [Harry Markowitz](https://alphaarchitect.com/2014/10/harry-markowitz-an-equal-weight-investor/#.VHPhRIvF9MV), a Nobel Prize winner and the founder of portfolio management, is quoted as saying:

> “I should have computed the historical covariance of the asset classes and drawn an efficient frontier, [but] I split my contributions 50/50 between bonds and equities.”

A few quotes attributed to Einstein sum up the key lessons learned from piles of disinterested research compiled on the subject of asset allocation.

1. Keep it simple.
2. Complexity does not imply value.

#### 

#### [Robust Asset Allocation_Keep it simple](https://alphaarchitect.com/wp-content/uploads/2014/12/Robust-Asset-Allocation_Keep-it-simple.png)

### Complexity is Suspect. Is Equal-Weight the Answer?

> “Don’t try anything fancy. Stick to a simple diversified portfolio, keep your costs down and rebalance periodically to keep your asset allocations in line with your long-term goals.”
>
> –David Swensen, Yale Endowment CIO.

The point of the DeMiguel et al. research cited above is not to imply that equal-weight allocations are always optimal and/or sensible. For example, if a portfolio consists of two assets — 1) call options on 3x leveraged S&P 500 ETFs and 2) 90-day T-bills — an equal-weight allocation may not make sense because the assets involved have dramatically different risk profiles and the 50% allocation to the call options on 3x levered S&P will obviously dominate all the action in the portfolio. So perhaps 50/50 isn’t the answer, but neither is dynamic risk-parity with machine-learning Q-theory Black-Litterman Whiz-bang mousetrap optimization across these 2 assets. Maybe a static 20/80 allocation will fit the bill? The main point of their research is that the signals generated by whiz-bang asset allocation models typically reflect noise, not actual signal.  And that brings us to the so-called benchmark for asset allocation, which is often considered the 60/40 portfolio, which is 60% allocated to global equities and 40% allocated to global bonds.(5) This portfolio reflects the essence of the advice gleaned from DeMiguel et al.’s work — keep it simple. That said, “experts” will put forth hundreds of arguments for why the 60/40 portfolio is sub-optimal, won’t work, and so forth, but the reality is that the portfolio does follow the [FACTS framework](https://alphaarchitect.com/2014/09/a-framework-for-investment-manager-selection-stick-to-the-facts/) and does provide some reasonable diversification. We can all argue why 60/40 is broken (I’m happy to provide those arguments), but for many investors this is an option worth considering.

So how can we possibly improve upon the baseline 60/40 benchmark without going down the complexity railroad, which often is a bridge to nowhere?

One approach is to look at the 60/40 portfolio as essentially 60% equity and 40% “diversifiers.” Bonds are often dumped in the diversifier bucket because they are relatively easy to understand. But bonds only represent one form of a diversifier — there are many others — but will bonds always be an [effective diversifier](https://alphaarchitect.com/2016/06/will-bonds-deliver-crisis-alpha-in-the-next-crisis/)? We’re not sure. Should we really put all our eggs in the bond diversification bucket? Possibly, but it seems prudent to at least consider a more robustly designed diversifier bucket.

We need to be careful when we explore a more complex diversifier allocation — the cure may be worse than the disease. When it comes to diversifiers, often labeled “alternatives,” one can go nuts trying to compile unique risk/return premiums. Perhaps this effort is appropriate for some investors with the time, resources, and buying power to create a solution that is in line with the FACTS and achieves their specific objectives. However, for the rest of us (and maybe even the pros), we may be better off trying to replicate what larger more sophisticated investors can achieve, but without all the brain damage and costs. The “IVY 5” portfolio, described by [Faber (2007)](http://www.trendfollowing.com/whitepaper/CMT-Simple.pdf) and then further elaborated by [Faber and Richardson (2009)](http://www.theivyportfolio.com/), is a great example of this approach. The authors highlight that the largest endowments have highly complex portfolios that extend well beyond the 60/40 benchmark with respect to their levels of complexity. Nonetheless, the performance of a simple endowment replication model, consisting of five core asset classes, does a pretty reasonable job at capturing their performance. The five core asset classes are as follows:

* **US Stocks**= SP500 Total Return Index
* **Int’l Stocks**= MSCI EAFE Total Return Index
* **REIT**= FTSE NAREIT All Equity REITS Total Return Index
* **Comm.**= Goldman Sachs Commodity Index (GSCI) Index
* **Bonds**= Merrill Lynch 7-10 year Government Bond Index

With a shift away from equal-weights across the five assets, we can augment the IVY 5 concept to create a 60/40 portfolio, where the key difference is the “diversifier” bucket is no longer entirely dependent on bonds, but has a mix of real assets and bonds. We refer to this portfolio as “RAA Simple.” The goal of RAA Simple is to capture expected returns associated with a diversified pool of global assets.

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/ivy-5-augment-1030x356.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/ivy-5-augment.png)

Arguably, this slightly more complex 60/40 allocation is structurally more robust to various economic regimes in the future and doesn’t have all the diversifier eggs in the “bond basket.”

RAA Simple achieves its goal of capturing global risk premiums without the chaos of any individual asset class.

Another thing to point out is that RAA Simple doesn’t curb your drawdown that much via diversification. But US 60/40 is also not the sure-fire answer, as the table in our “[world’s longest trend following backtest highlights](https://alphaarchitect.com/2015/11/09/the-worlds-longest-trend-following-backtest/).”

We’ll talk about potential methods to solve the limits of diversification when discussing risk management, but first, let’s move on to security selection.

## #2 Security Selection: Instead of story-based stock selection, use evidence-based stock selection

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/step-2.-evidence-based-security-selection.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/step-2.-evidence-based-security-selection.png)

Charts presented are for illustrative purposes only. Our downside protection models may not work in all situations and could fail to achieve their objectives.

RAA Simple deploys passive equity investments in the form of the large-cap domestic equity and large-cap developed equity. This is a fine approach and is easy to understand and implement. However, when it comes to security selection methods, there are arguably ways to potentially improve the overall profile of the investment portfolio, without getting too far out on the complexity curve. In this section we focus entirely on the equity component of the portfolio, however, as discussed in our DIY book and throughout blog, there is research to suggests that one can leverage selection algorithms to differentiate REIT, commodity, and bond exposures. We think the juice generated from the additional complexity may not be worth the squeeze in most cases, but this is certainly something an investor could explore.

(6)

In case you haven’t noticed, we have droned on and on over the potential benefits and sustainability of focused value and momentum equity exposures. We’ve even spent the time to write entire books dedicated to both of these subjects, which we encourage you to read. However, the synopsis is simple and will save you a lot of time:

* **Value:** Buy cheap stuff everyone hates.
* **Momentum:** Buy winners.
* Have a 10+yr horizon and stick with the strategies through thick and thin.

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/value-and-momentum-books.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/value-and-momentum-books.png)

The key thing to consider with any simulated index is that they look good on paper — there was never a backtest published that didn’t look great. But what generated these excess returns? And why can we hypothesize that these excess returns will be captured in the future? This is a debate that still rages on in academic research circles, but essentially excess expected returns are driven by 2 potential sources: 1) additional risk, and/or 2) systematic mispricing. With value and momentum in particular, there is arguably some mispricing built into the premiums, but exploiting these premiums is not a free lunch. An investor will likely be asked to take on more risk, and one can expect to endure epic episodes of relative performance pain (See here on [momentum](https://alphaarchitect.com/2016/09/07/is-momentum-investing-dead-or-is-it-just-painful/) and here on [value](https://alphaarchitect.com/2016/09/14/why-value-investing-is-a-terrible-idea/)).

Bottom line: no pain, no gain is a good motto to live by when it comes to setting financial investment expectations for focused factor investments such as our flavor of systematic value and momentum.

So let’s assume that the evidence is compelling enough for our quantitative value and quantitative momentum processes and you are a long-term buyer. Great. Let’s integrate these into the RAA framework.

## #3 Risk Management: instead of no downside protection, use downside protection.

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/step-3.-risk-management-1030x530.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/step-3.-risk-management.png)

Charts presented are for illustrative purposes only. Our downside protection models may not work in all situations and could fail to achieve their objectives.

As we saw above, diversification is a prudent thing to implement in a portfolio. However, if the goal of your investment program is to capture global risk premiums *and* minimize permanent loss of capital, diversification isn’t going to cut it when correlations go to 1. Even the RAA Simple portfolio, which diversifies across a broad swath of assets, ate a 40%+ drawdown in 2008. Yikes.

If diversification isn’t going to help some investors achieve their goal of minimizing extreme tail risks, what can an investor do? Unfortunately, we enter a murky world of complexity, which should automatically raise our spidey sense. In fact,  any effort to minimize tail risk almost necessarily requires that the portfolio be 1) diversified and 2) be dynamic.  A 60/40 portfolio or a RAA Simple portfolio are both diversified, but their allocations aren’t dynamic.

Having reviewed and considered an incredible number of dynamic timing systems, the sad truth is it difficult to identify robustness.

(7)

However, there are one class of models that are fairly simple and have historically achieved the goal of capturing risk premiums, while simultaneously minimizing the risk or large drawdowns. These models generally fall under the category of “trend-following,” and include things like moving averages and channel breakouts.

The application of simple moving average rules has been demonstrated to protect investors from large market drawdowns, which is defined as the peak-to-trough decline experienced by an investor. For example, Jeremy Siegel, in his book, *Stocks for the Long Run*, explores the effect on performance on the Dow Jones Industrial Average from 1886 to 2006, when applying a 200-day moving average rule. Applying the rule is straightforward. If the market is above the 200-day moving average rule, hold, otherwise, go to cash. Siegel found that this simple technical rule outperforms a buy-and-hold approach, both in absolute terms and on a risk-adjusted basis. Meb also highlights similar [results in his paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461) on the subject of long-term moving averages.

We’ve conducted a [similar analysis](https://alphaarchitect.com/2015/11/09/the-worlds-longest-trend-following-backtest/) on the US stock market from 1801 to 2015 and found that trend-following rules applied on the generic stock market have been effective at minimizing tail risk events. [We’ve extended the analysis](https://alphaarchitect.com/2015/08/13/avoiding-the-big-drawdown-downside-protection-investment-strategies/) to every asset class where we could get our hands on the numbers and investigated the results. Same conclusion: trend-following minimizes tail risk.

Got it. This so-called trend-following aspect helps minimize large drawdowns, but 1) why should I care? and 2) can you explain the voodoo behind it?

### Why Tail-Risk Management Matters

For some investors with multi-decade horizons, managing large drawdown risks, especially if it comes at an expense to long-term compounding, may not be a great idea. However, for some investors, who have shorter horizons and/or more immediate liquidity needs, risk-management is really important if they want to achieve their investment goals. The chart below highlights why large drawdowns are hazardous to your wealth.

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/large-drawdowns.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/large-drawdowns.png)

Charts presented are for illustrative purposes only. Our downside protection models may not work in all situations and could fail to achieve their objectives.

The chart on the left shows what happens to an investment portfolio when it is cut in half. Just to get back to even requires 11 years at a 7% return. Perhaps some people don’t need to tap that capital for 11 years so compounding out of the drawdown isn’t a big deal. But what if the plan was to live off your nest egg? Taking a 4% yield on $100 is one thing — taking a 4% yield on $50 is entirely different and may no longer meet the investor’s needs. The chart on the right shows what happens when there is a less severe drawdown of 15%. This is obviously not the ideal outcome, but if an investor seeks capital appreciation, they must take on risk, which means drawdowns and volatility are inevitable. But a 15% drawdown is much more manageable and only requires 3 years at 7% compounding to get back to even. A lot of investors can wait out 3 years of pain, but few can deal with 11 years of pain.

### Roger That — I Get Why I Want to Control My Drawdowns. Can You Explain the Voodoo Magic of Trend-Following?

The depth of research on trend-following is mind-blowing. You can quickly go down the dark rabbit hole of backtesting and generate charts that would make Bernie Madoff blush. Of course, these systems are clearly over-optimized and unlikely to be robust out of sample. Moreover, having reviewed and thought about hundreds of trend-following systems, there is one clear message — nothing works all the time. The goal is to find the simplest and most robust approaches out there and then have the conviction to follow these systems to the grave. The figure below outlines our approach:

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/trend-following-model.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/trend-following-model.png)

Charts presented are for illustrative purposes only. Our downside protection models may not work in all situations and could fail to achieve their objectives.

We have a time series, or absolute momentum rule, and we have a long-term moving average rule.

We define each of the rules below:

***1. Time Series Momentum Rule (TMOM)***

This rule is meant to avoid assets with poor absolute performance.

* Excess return = total return over past x months less return of T-bill
  + If Excess return >0, go long risky assets. Otherwise, go alternative assets (T-bills or Zero).
  + Popularized by [Gary Antonacci](http://www.dualmomentum.net/) and rigorously examined by [Moskowitz et al.](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2089463)

***2. Simple Moving Average Rule (MA)***

This rule is meant to avoid assets with poor trending performance.

* Moving Average (N) = average N month prices
  + If Current Price – Moving Average (N) > 0, go long risky assets. Otherwise, go alternative assets (T-bills or Zero).

As the equations highlight, MOM and MA rules are tied together: Time-series momentum rules (MOM) are a function of MA rules. And while MOM and MA triggers are highly correlated, there are circumstances where the rules have a difference of opinion.

TMOM and MA rules are actually mathematically related.

(8)

However, while these rules are similar, we’ve found evidence that these rules sometimes have a “difference of opinion,” where one rule says “risk” and the other says “no risk.” We also find that spreading our trend-following bet across these two systems is more robust than simply relying on one or the other.

(9)

Step 1 outlined the idea that we don’t need overly complex asset allocation frameworks to capture global risk premiums. Step 2 suggested that we can maximize our chance of the highest expected equity risk premium via focused value and momentum exposures. In step 3 we apply trend following to each component of the RAA system — equity trend, commodity trend, bond trend, and real estate trend.

## Robust Asset Allocation — Putting It All Together

RAA is our best effort to develop a simple model. Developing a complicated model would have been easier, but simple was a considerably more difficult challenge. We’ve discussed the three building blocks of the RAA Index methodology: simple asset allocation, evidence-based security selection, and a trend-following based downside protection mechanism.

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/checklist-of-3-raa-items-1030x546.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/checklist-of-3-raa-items.png)

Charts presented are for illustrative purposes only. Our downside protection models may not work in all situations and could fail to achieve their objectives.

Here is a detailed visualization of the RAA Index process (moderate shown).

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/RAA-process-details-1030x587.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/RAA-process-details.png)

Charts presented are for illustrative purposes only. Our downside protection models may not work in all situations and could fail to achieve their objectives.

We start with a more robust 60/40 framework that splits the traditional bond-only 40% diversifier bucket across real and bond assets.

Next, we replace passive stock exposures with focused value and momentum exposures.

Then, we calculate trend-following rules for each asset class to determine their respective exposures.

Finally, we implement the model.

## The Robust Asset Allocation Index – is it the Holy Grail?

Is the Robust Asset Allocation Index process a holy grail? Is the RAA Index appropriate for all investors? Highly unlikely.

Here are some reasons why the RAA concept is a bad idea:

* The RAA multi-asset focus can drag on returns relative to generic 60/40 portfolios
* Downside protection can drag on returns relative to 60/40 portfolios

Value/momentum can drag on returns relative to passive equity portfolios

* Global equity can drag on returns relative to domestic-centric portfolios

Long story short, RAA will not always work and will often underperform standard benchmarks. But that is baked in the cake.

* The RAA Index mission is goal-oriented and seeks to provide capital appreciation with downside protection.
* The RAA Index is not meant to track the 60/40 index or closely track generic benchmarks.
* The RAA Index is not meant to outperform X, Y, or Z.

The systems are simply our best attempt to achieve the goal of capturing global risk premiums, while simultaneously minimizing the chance of a permanent loss of capital. Simple as that.

[![](https://alphaarchitect.com/wp-content/uploads/2014/12/raa-mission-and-goals-1030x442.png)](https://alphaarchitect.com/wp-content/uploads/2014/12/raa-mission-and-goals.png)

We want to emphasize that RAA is merely one proposed solution to achieve a specific investment goal.  There are a set of other solutions in the marketplace that seek to do similar thing and we recommend that investors explore all of these options. However, we suggest that investors can narrow their solutions down to those options that are simple, liquid, transparent,  affordable, and tax-efficient (if applicable).

Sounds great — What’s the next step?

## Getting start with the Robust Asset Allocation Indexes

Investors have a few options with the Robust Asset Allocation Indexes:

* **DIY investor:** we provide [free tools](https://alphaarchitect.com/tools/) to help investors facilitate various tactical asset allocation strategies (including the RAA Indexes).
* **Managed Accounts:** We seek to track the performance of our RAA Indexes via managed accounts.
* **Ask Your Advisor:** Are you currently a client of an advisor, and you’d like them to explore our solution? Let us know — we’ll help them get up and running.

As always, feel free to [contact us](https://alphaarchitect.com/about#tabs-3a) if you have any questions or thoughts.

References[+]

References

|  |  |
| --- | --- |
| ↑1 | Of course, as the authors of the book, *[DIY Financial Advisor](https://www.amazon.com/gp/offer-listing/111907150X/ref=tmm_hrd_new_olp_sr?ie=UTF8&condition=new&qid=&sr=)*, we’d be remiss if we failed to mention that another option for investors is to simply Do-It-Yourself. This is a fine option if one has the 1) time, 2) sophistication, and 3) discipline to identify an investment goal, build a portfolio to achieve that goal, and can stick to the program through thick and thin. |
| ↑2 | I have a [Google Talk](https://www.youtube.com/watch?v=rVjlXzWwxXk) on the book if you want a video version of the DIY philosophy. If this is too much brain damage, simply head over to our [active robo advisor](https://alphaarchitect.com/robo) and we’ll implement a strategy that attempts to follow the RAA Index most suitable for your investment profile. |
| ↑3 | Past performance is no guarantee of future results. Any historical returns, expected returns, or probability projections may not reflect actual future performance. All securities involve risk and may result in loss. Our downside protection models may not work in all situations and could fail to achieve their objectives. |
| ↑4 | The results below, taken from the DeMiguel et al. paper on asset allocation, highlight the incredible robustness associated with an equal-weight, or 1/N, type of asset allocation regime. (we have our own version of this in “[Tactical Asset Allocation: Beware of Geeks Bearing Formulas](https://alphaarchitect.com/2015/05/19/tactical-asset-allocation-beware-geeks-bearing-formulas/)“) [Robust Asset Allocation_Optimal vs Naive Diversification](https://alphaarchitect.com/wp-content/uploads/2014/12/Robust-Asset-Allocation_Optimal-vs-Naive-Diversification.png)  Source: DeMiguel, V., L. Garlappi, and R. Uppal, 2009, Optimal Versus Naïve Diversification: How Inefficient is the 1/N Portfolio Strategy? Review of Financial Studies 5, 1915-1953. The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.  The chart above is visualized below. Sharpe ratio is on the X-axis for the various asset allocation systems trading with S&P sectors. Note that the simple 1/N strategy works as well, and often better, than more complex approaches.  [https://alphaarchitect.com/wp-content/uploads/2014/12/complexity.png 1405w" sizes="(max-width: 1030px) 100vw, 1030px" />](https://alphaarchitect.com/wp-content/uploads/2014/12/complexity.png)  The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request. |
| ↑5 | Why this portfolio structure became the benchmark solution is beyond me and perhaps there is someone who has done the history of how this came to be. |
| ↑6 | The most compelling argument is with respect to the commodity exposure, which we benchmark using the GSCI index, however, there are [economic](https://alphaarchitect.com/2016/12/21/commodity-investing-is-complex-and-volatile-but-unique/) and [evidence-based reasons](http://www.cftc.gov/idc/groups/public/@swaps/documents/file/plstudy_33_yu.pdf) why in practical implementation GSCI may not be the desired vehicle. |
| ↑7 | We have examined hundreds of risk-management platforms over the years. You name it–we’ve backtested it, thought about it, and/or considered implementing it. We’ll keep testing new ideas and trying to identify the holy grail, but we haven’t found it yet. ***Conclusion: Asset allocation models are 99% noise; 1% signal.***  Here is a sampling of the various ideas we have tested:  **Macroeconomic Fundamental Indicators**   * [Wealth Ratio](http://faculty.haas.berkeley.edu/lettau/papers/LettauLudvigsonJF2001.pdf) — Lettau and Ludvigson (2001) , “Consumption, Aggregate Wealth, and Expected Stock Returns” * [Adaptive Macro Indexes](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1692740) — Bai (2010) ,”Equity Premium Predictions with Adaptive Macro Indexes” * [Sum of Macro Variables](https://www.sciencedirect.com/science/article/abs/pii/S0304405X11000365) — Ferreira and Santa-Clara (2011),  “Forecasting Stock Market Returns: The Sum of the Parts is More than the Whole” * [Industrial Mental Return](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1660864) — Jacobsen, Marshall and Visaltanachoti (2013)[,](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1660864) “Stock Market Predictability and Industrial Metal Returns” * [Implied Cost of Capital](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1787285) — Li, Ng and Swaminathan (2013), “Predicting Market Returns Using Aggregate Implied Cost of Capital” * [Oil Factor](https://www.jstor.org/stable/25621509) — Kilian and Park (2007), “The Impact of Oil Price Shocks on the U.S. Stock Market” * [CAPE](http://www.econ.yale.edu/~shiller/data.htm) — Robert Shiller (2013)   **Technical Indicators**   * [Historical Data Forecast](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=996696)— Maheu and McCurdy (2006), “How Useful are Historical Data for Forecasting the Long-Run Equity Return Distribution?” * [Time-Varying Sharpe Ratio](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1938613) — Tang and Whitelaw (2011), “Time-Varying Sharpe Ratios and Market Timing” * [Return Dispersion](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1986791) — Maio (2012), “Return dispersion and the predictability of stock returns” * [Mean Reversion Indicator](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2188989) — Huang, Jinag, Tu and Zhou (2012), “Mean Reversion, Momentum and Return Predictability” * [Cross-sectional Technical Analysis](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1656460)–Han, Yang, Zhou, “A New Anomaly: The Cross-Sectional Profitability of Technical Analysis” * [Simple MA Rule](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461) –Faber (2007), “A Quantitative Approach to Tactical Asset Allocation.” * [Challenging MA rule](https://ideas.repec.org/p/zbw/cpqfwp/29.html) #1 –Scholz and Walther (2011), “The trend is not your friend! Why empirical timing success is determined by the underlying’s price characteristics and market efficiency is irrelevant” * [Challenging MA Rule #2](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2242795)–Zakamulin, “The Real-Life Performance of Market Timing with Moving Average and Time-Series Momentum Rules” * [Challenging MA Rule #3](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1476225)–Marmi, Pacati, Risso, Reno, “A Quantitative Approach to Faber’s Tactical Asset Allocation” * [Overview of Technical Analysis](http://chesler.us/resources/academia/AgMAS04_04.pdf)— Park and Irwin (2007), “What we know about the profitability of technical analysis?”   **Sentiment and Variance Indicators**   * [Investor Sentiment](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2311618)— Huang, Tu, Jiang and Zhou (2014), “Investor Sentiment Aligned: A Powerful Predictor of Stock Returns” * [Cross-Section of Volatility](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=681343)— Ang, Hodrick, Xing and Zhang (2006), “The Cross-Section of Volatility and Expected Returns” * [Variance Risk Premia](http://public.econ.duke.edu/~boller/Published_Papers/rfs_09.pdf) — Bollerslev, Tauchen and Zhou (2009), “Expected Stock Returns and Variance Risk Premia” * [VIX Term Structure](https://www.bauer.uh.edu/departments/finance/documents/seminars/Johnson_020712.pdf)— Johnson (2011), “Equity Risk Premia and the VIX Term Structure” * [Equity Shares](http://www.people.hbs.edu/mbaker/cv/papers/equityshare.pdf) — Baker and Wurgler (2000), “The Equity Share in New Issues and Aggregate Stock Returns” * [Broker-Dealer Leverage](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr464.pdf) — Adrian, Etula and Muir (2013), “Financial Intermediaries and the Cross-Section of Asset Returns” * [Implied Volatility Spread](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1993289) — Atilgan, Bali and Demirtas (2011), “Implied Volatility Spreads, Skewness and Expected Market Returns”   **Comprehensive Summary of Different Predictors**   * [Gupta, Modise and Uwilingiye (2012)](https://repository.up.ac.za/handle/2263/49877) — “Out-of-Sample Equity Premium Predictability in South Africa: Evidence from a Large Number of Predictors” * [Welch and Goyal (2008)](http://www.hec.unil.ch/agoyal/docs/Predictability_RFS.pdf) — “A Comprehensive Look at The Empirical Performance of Equity Premium Prediction” * [Rapach and Zhou (2011)](https://www.sciencedirect.com/science/article/abs/pii/B9780444536839000062) — “Forecasting Stock Returns” * [Combo](http://research.stlouisfed.org/wp/2010/2010-008.pdf) — Neely, Rapach, Tu and Zhou (2011), “Forecasting the Equity Risk Premium: The Role of Technical Indicators”   The sad conclusion is that none of these ideas stand up to intense robustness tests, except for the simplest, technical rules. You just can’t beat them. |
| ↑8 | We have actually identified the mathematical relationship between MOM and MA Rules, outlined in the chart below: [Robust Asset Allocation_Momentum and MA rule](https://alphaarchitect.com/wp-content/uploads/2014/12/Robust-Asset-Allocation_Momentum-and-MA-rule.png) |
| ↑9 | [Here is an extensive study](https://alphaarchitect.com/2015/08/13/avoiding-the-big-drawdown-downside-protection-investment-strategies/) on these rules and their historical performance on a slew of generic return data series. |

 function footnote\_expand\_reference\_container\_15175\_48() { jQuery('#footnote\_references\_container\_15175\_48').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_15175\_48').text('−'); } function footnote\_collapse\_reference\_container\_15175\_48() { jQuery('#footnote\_references\_container\_15175\_48').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_15175\_48').text('+'); } function footnote\_expand\_collapse\_reference\_container\_15175\_48() { if (jQuery('#footnote\_references\_container\_15175\_48').is(':hidden')) { footnote\_expand\_reference\_container\_15175\_48(); } else { footnote\_collapse\_reference\_container\_15175\_48(); } } function footnote\_moveToReference\_15175\_48(p\_str\_TargetID) { footnote\_expand\_reference\_container\_15175\_48(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_15175\_48(p\_str\_TargetID) { footnote\_expand\_reference\_container\_15175\_48(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
