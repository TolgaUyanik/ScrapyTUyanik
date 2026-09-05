---
title: "The Hidden Cost of Index Replication"
slug: "index-replication-cost"
date: "2024-10-04"
modified: "2024-09-30"
url: "https://alphaarchitect.com/index-replication-cost/"
categories: ["Transaction Costs", "Research Insights", "Larry Swedroe", "Other Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# The Hidden Cost of Index Replication

> An index-tracking approach generally lacks flexibility, which detracts from performance, leaving returns on the table. Intelligent design can overcome such issues. For example, an S&P 500 Index could choose to rebalance one month ahead of the scheduled reconstitution, minimizing the impact of reconstitution. Direct index funds are already engaging in such strategies with ETFs.

As the annual [SPIVA](https://url.avanan.click/v2/___https:/www.spglobal.com/spdji/en/research-insights/spiva/about-spiva/___.YXAzOnNhcmFncmlsbG86YTpnOjY3MDIyNDE5YWNlYjU2MTVjNzM4ZTJkZmRjNmNmYzkzOjY6MTM2MjoyNGNiYWU3Y2Q1YzA5NDg4YWI5NWIzOGU5MTcxMTZhZTc2NDc5NGZjNTkwMWE1ODc0MDRhNzRjZTI0YTc0YTg2OnA6VDpO) studies demonstrate, index funds persistently outperform the vast majority of actively managed funds, even before considering taxes. With that said, most investors are unaware that there are weaknesses of index funds that result from their strategy to replicate the return of an index. Those weaknesses, which result from the desire to minimize what is called “tracking error” (returns that deviate from the return of the benchmark index), can lead to constraints and implementation costs that hurt returns. The weaknesses that can be minimized or avoided include:

* Sensitivity to risk factors varies over time, subjecting investors to unintentional style drift. Because indexes typically reconstitute annually, they lose exposure to their asset class/factor over time, as stocks migrate across asset classes during the course of a year. For example, according to a study by [Dimensional Fund Advisors](https://www.dimensional.com/us-en/insights/measuring-the-costs-of-index-reconstitution-a-10-year-perspective), on average from 2010 through June 2023, roughly 25% of the Russell 2000 Index, positioned as a small cap index, was composed of the largest 1,000 stocks in the Russell 3000 Index. Similarly, the overlap between the Russell 1000 Value and Growth indices averaged about 300 companies over that period. Non-index, but systematic, portfolios (like those of firms such as AQR, Avantis, Bridgeway, and Dimensional) typically reconstitute monthly, allowing them to maintain more consistent exposure to their asset class. That allows them to capture a greater percentage of the risk premiums in the asset classes in which they invest.

* Forced transactions as stocks enter and leave an index when indices rebalance/reconstitute, resulting in higher trading costs, costs which are not transparent.

* Risk of exploitation through front-running. Active managers can exploit the knowledge that index funds must trade on certain dates. Systematic portfolios avoid this risk by not trading in a manner that simply replicates the return of the index, trading consistently throughout the year.

* Inclusion of all stocks in the index. Research has found that very low-priced (“penny”) stocks, stocks in bankruptcy, extreme small growth stocks with high investment and low profitability, and IPOs have poor risk-adjusted returns. A systematic portfolio could exclude such stocks, using a simple filter to screen them *all* out.

* Limited ability to pursue tax-saving strategies, including avoiding intentionally taking any short‐term gains and offsetting capital gains with capital losses.

Another advantage of systematic funds, in return for accepting tracking error risk, is that they can gain greater exposure to the factors for which there is persistent and pervasive evidence of a return premium (such as size, value, momentum, profitability/quality, momentum, carry, and term). For example, a small-value fund could be structured to own smaller and more “valuey” stocks than a small-cap value index fund. It can also be structured to have more exposure to highly profitable companies, and it can screen for the momentum effect (avoiding buying stocks that are exhibiting negative momentum and delaying selling stocks with positive momentum).

**Rebalancing/Reconstitution**

Rebalancing of major indices is generally centered around three major events; the measurement date, announcement date, and effective date.

**Measurement Date**: The index provider gathers the necessary data for the rebalancing, for market cap weighted indices this includes the free float and closing price. Using this data, the index provider calculates the updated index holdings based on the index methodology.

**Announcement Date**: The index provider announces the upcoming changes to the wider market. The index continues to be calculated using the previous index weightings until the effective date.

**Effective Date**: The index provider updates the index according to the weightings published at the effective date. From this point onwards, index values are calculated using the updated index weightings.

These events are generally staggered by a few days or weeks, depending on how the index is designed. While providing transparency and predictability, index tracking products are designed to have as little deviation as possible from the index performance. Thus, they concentrate their trading on the effective date, demanding liquidity from the market—with negative consequences.

**Empirical Research on the Hidden Costs of Index Replication**

Kaitlin Hendrix, Jerry Liu, and Trey Roberts, authors of the study “[Measuring the Costs of Index Reconstitution: A 10-Year Perspective,](https://url.avanan.click/v2/___https:/www.dimensional.com/us-en/insights/measuring-the-costs-of-index-reconstitution-a-10-year-perspective___.YXAzOnNhcmFncmlsbG86YTpnOjY3MDIyNDE5YWNlYjU2MTVjNzM4ZTJkZmRjNmNmYzkzOjY6YjU5NDo3OGYwYWY4MGJhYTMyMmQ1NjQ5MmJhNjE5MGViM2Q4YmNmOTkzZGFjMDk4OGNlYTYzODNlODQ5NjYyMjkzNmZhOnA6VDpO)” examined the impact of trading costs that result from the reconstitution of an index. They measured the costs of index reconstitution from 2014 to 2023 for 10 US indices. In their analysis, they restricted adds and deletes to nonmigrating securities, i.e., stocks that are added to (or deleted from) an index and are not also deleted from (or added to) another index from the same index family on the same reconstitution date. By focusing on these “pure” additions and deletions, they were able to more cleanly identify the cost of demanding immediacy associated with tracking an index. They examined the reconstitution events for 10 widely tracked US equity indices—the S&P 500 index, S&P MidCap 400 (S&P 400) index, S&P SmallCap 600 (S&P 600) index, Russell 1000 Growth Index, Russell 1000 Value Index, Russell 2000 Index, CRSP US Large Cap Growth Index, CRSP US Large Cap Value Index, CRSP US Mid Cap Index, and CRSP US Small Cap Index—from 2014 through 2023. Their sample included a total of 3,488 additions and 2,517 deletions.

Following is a summary of their key findings:

* There is abnormally high [trade volume](https://alphaarchitect.com/2024/01/crowded-trades/) on reconstitution dates for stocks added to or deleted from the indices.
* Consistent with fund managers trying to minimize tracking error, the spike in trade volume tends to be highly concentrated at the time of market close on reconstitution dates—ranging from 3 times for the CRSP US Mid Cap Index to over 27 times for the S&P 500 index.
* The typical span between the last trade and the closing auction is 10 seconds or less and there is a strong price reversal for those stocks by market open the following morning.
* For the S&P indices, the S&P 600 exhibited the greatest volume increase, at around 112x trading volume at 4 pm on reconstitution day in rebalanced stocks compared to the trading volume in the same stocks during the same 15-minute window averaged over the prior month.
* The greatest volume pressure occurred for the Russell 2000 Index, with 120 times volume on rebalance day compared to the prior month.
* Additions rise in price relative to the index before rebalancing, while deletes fall in price. After reconstitution, both adds and deletes experience price reversals, with the effect being greater for adds on average.
* Over the period 2019-2023, price for additions on average went up by 9 bps, relative to nonrebalanced stocks, in the roughly 10 seconds between 4 pm on reconstitution day and market close, and then reversed by a relative –13 bps by market open the next morning.
* On average, the price for deletions fell relative to nonrebalanced stocks by 30 bps from 4 pm to market close on reconstitution day, just before they were “sold” from the index, with a reversal of a relative 63 bps by market open the following day.
* On average prices moved adversely for additions/deletions by more than 4% over the 20 trading days leading up to reconstitution, with a reversal of –5.7% in the next month.

Their findings led Hendrix, Liu, and Roberts to conclude: “With respect to transaction costs, adhering to an index reconstitution schedule can result in relatively poor execution prices—buying higher and selling lower—which are in turn reflected in investors’ returns.”

In their study on the [costs of rebalancing](/Users/Sara%2520Grillo/Downloads/Rebalancing%2520Whitepaper.pdf) the Russell 1000 Index over the period 2012-2021, the research team at direct index provider [Index One](https://url.avanan.click/v2/___https:/indexone.io/___.YXAzOnNhcmFncmlsbG86YTpnOjY3MDIyNDE5YWNlYjU2MTVjNzM4ZTJkZmRjNmNmYzkzOjY6NThjOTowMmM4YjAwMjk3OWM3N2Y3ZWIyNTU3OTkxODc1YTA3MGQwNjNlNTc0MDMwMjA4Yjk5YWNkYmRkYmIyYjJkNGU1OnA6VDpO) found that the hidden cost of rebalancing the Index was 7.5 basis points, or a total loss to investors of $11 billion per year. Rebalancing a week before or two weeks after would have been more efficient.

**Investor Takeaways**

An index-tracking approach generally lacks flexibility, which detracts from performance, leaving returns on the table. Intelligent design can overcome such issues. For example, an S&P 500 Index could choose to rebalance one month ahead of the scheduled reconstitution, minimizing the impact of reconstitution. Direct index funds are already engaging in such strategies with ETFs.

A superior approach, the one taken by such research-oriented investment firms such as AQR, Avantis, Bridgeway, and Dimensional would be to use a daily process that consistently focuses on owning stocks with higher expected returns and spreads turnover across all trading days with flexibility across stocks and quantities. Such an approach minimizes the cost of demanding immediacy from the market.

*Larry Swedroe is the author or co-author of 18 books on investing, including his latest Enrich Your Future.*
