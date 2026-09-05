---
title: "Stale Performance Chasing: Beware of Horizon Effects"
slug: "stale-performance-chasing-beware-of-horizon-effects"
date: "2016-07-21"
modified: "2022-05-11"
url: "https://alphaarchitect.com/stale-performance-chasing-beware-of-horizon-effects/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Stale Performance Chasing: Beware of Horizon Effects

> Investors talk a big game when describing how they evaluate mutual funds. They say they consider things like the objectives of the fund, its size, and […]

Investors talk a big game when describing how they evaluate mutual funds. They *say* they consider things like the objectives of the fund, its size, and the longevity of its managers. But there’s one factor that looms larger than all the others: Performance.

We wrote [here](https://alphaarchitect.com/2016/02/20/chasing-returns-and-avoiding-spaghetti-against-the-wall-fund-companies/#gs.vqXHIQo) about how investors tend to “chase” the performance of funds, allocating to funds that have done well, and redeeming from funds that have done poorly. We also wrote [here](https://alphaarchitect.com/2015/11/20/beware-of-the-value-investing-return-gap/#gs.KBs81eg) about the so-called “investor return gap” that occurs when investors invest and redeem at just the wrong time.

In “[Past Performance may be an illusion: Performance, flows, and fees in mutual funds](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2168768&download=yes),” by Phillips and Rau, the authors take a novel look at how investors react to strong recent performance. In particular, they explore how established standard performance horizons can affect fund flows.

### Holding Period Performance Reporting

The Securities Act of 1933 specifies that when advertising past performance, mutual funds must report holding period return (HPR) for several distinct periods: Specifically, they must show 1-, 5-, and 10-year average annual returns, as of the most recent calendar quarter. The mutual fund rating agencies, such as Morningstar and Lipper, also rank funds based on these horizons, and in addition, they report the 3-year HPR. These standardized reporting “horizons” are used across the industry, and make it difficult for funds to “cherry pick” stretches of performance to make themselves look good.

### Horizon Effects

One peculiarity of this HPR reporting system is that at any given moment in time, investors will tend to be highly focused on these specific reported performance horizons (i.e., 1, 3, 5, 10 year), since they are in a salient form, widely reported, and easy to access. But this can create distortions as returns move through the horizon.

For example, first consider the 4-quarter return series below (taken from the paper):  
[![2016-06-02 10_35_24-gray_stale_performance_chasing_v01.docx - Microsoft Word (Product Activation Fai](https://alphaarchitect.com/wp-content/uploads/2016/06/2016-06-02-10_35_24-gray_stale_performance_chasing_v01.docx-Microsoft-Word-Product-Activation-Fai.png)](https://alphaarchitect.com/wp-content/uploads/2016/06/2016-06-02-10_35_24-gray_stale_performance_chasing_v01.docx-Microsoft-Word-Product-Activation-Fai.png)  
When we calculate the one-year HPR (quarters 1 through 4), it is 7.9%.

Now let’s move forward in time by one quarter. Now when calculating our one-year HPR, we are going to drop our Period 1 return of -4%, and add a new Period 5 return, which is -2%, as set forth below:  
[![2016-06-02 10_35_36-gray_stale_performance_chasing_v01.docx - Microsoft Word (Product Activation Fai](https://alphaarchitect.com/wp-content/uploads/2016/06/2016-06-02-10_35_36-gray_stale_performance_chasing_v01.docx-Microsoft-Word-Product-Activation-Fai.png)](https://alphaarchitect.com/wp-content/uploads/2016/06/2016-06-02-10_35_36-gray_stale_performance_chasing_v01.docx-Microsoft-Word-Product-Activation-Fai.png)  
Now when we calculate the one-year HPR (quarters 2 through 5, representing our new “one year” return), it is 10.2%.

Note that the HPR has *changed* based on two factors: 1) the elimination of “stale information,” consisting of the -4% return, which drops from the horizon, and 2) the addition of “new information” to the horizon, consisting of the new -2% return.

Although the fund experienced a negative return in the new quarter, the fund’s HPR still increased because the return that was dropped was *even more* negative.

Did this change in reported HPR provide investors with a whole lot of new information about future fund performance? Not really.  In the new quarter, all that happened was the fund did a slightly less badly than it did during the quarter that is rolling off.

### So Does Horizon Matter?

The use of some particular horizon should not really matter, given a longer-run backdrop of performance. So it seems reasonable to conclude that the addition of a single quarter should not add a lot of information that would help us to assess the fund. However, the HPR still *looks much better*, in the frame of the new horizon. After all, the one-year HPR has gone from 7.9% to 10.2%. So does anyone think it matters?

### Well…Mutual Fund Managers Seem to Think it Matters

Mutual fund managers can be very focused on the change in HPR. Why? They love a new horizon when it means they get to drop a particularly bad quarter. Consider the following WSJ quote from 2007 (taken from the paper):

> …[The] wait is finally over for many mutual-fund managers. That is because 2007 marks a milestone that could greatly help their funds: It will have been five long years since the late-2002 bear market bottom. This means that five-year performance numbers no longer will reflect the market’s steep slide…January 2002…was a particular low for Old Mutual Focused fund, which had a sinking, large position in Adelphia Communications Corp., a cable company that eventually filed for bankruptcy protection. ‘I’m very anxious to roll off that quarter specifically,’ says Jerome Heppelmann, manager of the fund.

Mr. Heppelmann clearly looked forward to showing an improvement in his fund’s reported performance for the high profile, 5-year HPR horizon.  All he had to do to show a better 5-year HPR was improve returns, even slightly, over his very poor returns in 2002, when he got badly hurt by owning a dog stock.

But why should Heppelmann care? The choice of a 5-year HPR horizon is arbitrary – you could look at any horizon from the time series. Past return information does not really go “stale,” simply because it dropped out of a particular 5-year HPR horizon. If investors have access to the entire time series of returns, the addition of a new quarter shouldn’t have a big impact on what they think about the fund.

Is Heppelmann right to care? Weirdly, the answer is “yes,” because investors, programmed to be ad-hoc performance chasers, actually react to stale information.

### Investors Also React to Stale Performance

In the paper referred to earlier, the authors examine the universe of actively managed domestic mutual funds, using mutual fund data from the CRSP Mutual Fund Database, over the period 1992 to 2010.

The authors find that investors tend to allocate to funds with strong recent performance, and react to the stale information component of HPRs.

Since, as discussed earlier, mutual funds report HPRs over specific horizons, the authors examine how sensitive fund flows in month *t* are to returns on the cusp of those horizons (i.e, the 13th, 37th, and 61st months prior to month t). Note that in these “cusp” months, performance figures are rolling off the horizon.

Note in the below panel, how the t-stats in months 13 and 37 have t-statistics with high statistical significance (P values < 0.0001).

[![2016-06-16 10_12_55-Past performance may be an illusion_ Performance, flows, and fees in mutual fund](https://alphaarchitect.com/wp-content/uploads/2016/06/2016-06-16-10_12_55-Past-performance-may-be-an-illusion_-Performance-flows-and-fees-in-mutual-fund.png)](https://alphaarchitect.com/wp-content/uploads/2016/06/2016-06-16-10_12_55-Past-performance-may-be-an-illusion_-Performance-flows-and-fees-in-mutual-fund.png)  
They find there is a high sensitivity to returns realized just outside of the horizon. Put another way, investors appear to allocate heavily to funds when poor performance falls out of the horizon. They react to these stale fund returns.

### Mutual Funds Know That Investors Chase Stale Performance

The authors also find that mutual funds exploit this behavior by ramping up advertising during periods when HPRs move higher. In fact, they find an incremental increase in ad spending when performance measures benefit as a period of poor performance drops off the horizon.

Pretty sneaky…To make matters worse, the authors also find that mutual funds tend to *increase their expense ratios* (by reducing waivers) during times when poor returns are dropping out of the HPR horizon. They find that a one standard deviation increase in stale performance equates to a 20% increase in a fund’s expense ratio!

Even more sneaky.

In the end, investors tend to focus on information as it is presented, rather than on a total return series. When negative performance drops from the HPR horizon for funds, investors react by allocating to those funds. Thus, in a perverse sense, investors can be said to “chase” stale performance, by allocating when they lose focus on poor stale performance. The mutual funds know this, and take advantage of it during those times, by increasing their advertising and increasing their expense ratios.

Don’t you just love Wall Street?
