---
title: "The Implementation Costs of Indexed ETFs"
slug: "the-implementation-costs-of-indexed-etfs"
date: "2022-04-21"
modified: "2022-04-27"
url: "https://alphaarchitect.com/the-implementation-costs-of-indexed-etfs/"
categories: ["Research Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# The Implementation Costs of Indexed ETFs

> A common mistake made by many passive investors is that they view all index funds in the same asset class as “commodities,” often considering only the expense ratio when making their investment choices. However, not all index funds are alike, and not all passively managed funds (what I refer to as “systematically structured portfolios”) are index funds.

A common mistake made by many passive investors is that they view all index funds in the same asset class as “commodities(1)”, often considering only the expense ratio when making their investment choices. However, not all index funds are alike, and not all passively managed funds (what I refer to as “systematically structured portfolios”) are index funds.

Index funds and systematically structured portfolios that define their eligible universe and do not engage in individual security selection or market timing(2) are as similar as a rectangle is to a square. All squares are rectangles, but not all rectangles are squares. Similarly, while all index funds are passively managed (there is no individual stock selection or market timing), not all systematically structured funds attempt to replicate the returns of popular retail indexes like the S&P 500 or the Russell 2000. Systematically structured portfolios tend to use academic definitions of asset classes, building portfolios that seek to minimize the weaknesses of pure indexing. Those weaknesses, which result from the desire to minimize what is called “tracking variance,” or “tracking error” (returns that deviate from the return of the benchmark index),  include:

* Sensitivity to risk factors varies over time. Because indexes typically reconstitute annually, they lose exposure to their asset class over time, as stocks migrate across asset classes during the course of a year. Structured passive portfolios typically reconstitute monthly, allowing them to maintain more consistent exposure to their asset class. That allows them to capture a greater percentage of the risk premiums in the asset classes in which they invest.
* Forced transactions as stocks enter and leave an index, resulting in higher trading costs.
* Inclusion of all stocks in the index. Research has found that very low-priced (“penny”) stocks, stocks in bankruptcy, extreme small growth stocks with high investment and low profitability, and IPOs have poor risk-adjusted returns. A structured portfolio could exclude such stocks, using a filter to screen them out.
* Limited ability to pursue tax-saving strategies, including avoiding intentionally taking any short‐term gains and offsetting capital gains with capital losses.

Another advantage of systematically structured funds is that, in return for accepting tracking variance risk, they can gain greater exposure to the factors for which there is persistent and pervasive evidence of a return premium (such as [size](https://alphaarchitect.com/2020/12/is-size-a-useful-factor-or-not/), [value](https://alphaarchitect.com/2014/10/the-quantitative-value-investing-philosophy/), [momentum](https://alphaarchitect.com/2015/12/quantitative-momentum-investing-philosophy/), [profitability/quality](https://alphaarchitect.com/2020/06/diversifying-your-value-portfolio-quality-works-but-have-you-heard-of-momentum/), carry, term). For example, a systematic small-cap value fund could be structured to own smaller and more “valuey” stocks than a small-cap value index fund. It can also be structured to have more exposure to highly profitable companies, and it can screen for the momentum effect(3).

An often-overlooked disadvantage of index funds may result from the view that they tend to have low turnover and thus low trading costs. However, funds that attempt to replicate public indexes run the risk of exploitation through front-running—high-frequency traders and other active managers can exploit the knowledge that they must trade on certain dates. Structured portfolios avoid this risk by not trading in a manner that simply replicates the return of the index.

## **The Cost of Replication**

Sida Li contributes to the literature on trading costs of exchange-traded funds (ETFs) with her November 2021 study, “[Should Passive Investors Actively Manage Their Trades](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3967799)?” Her database covered all unlevered ETFs listed in the U.S. and Canada with no survivorship biases and the period 2012-2020. She began by noting that the passive investment strategy implicitly assumes that an investor holds a static buy-and-hold portfolio and that the portfolio constituents remain constant. In reality, passive funds need to trade in response to index constituent changes, IPOs, mergers, and acquisitions, and delistings—the median portfolio turnover rate in 2020 of a U.S.-indexed equity ETF was 16 percent. Therefore, even if an investor chooses to buy and hold an ETF, the ETF manager needs to trade on behalf of the investor.

Li identified three types of ETF trading strategies: a “sunshine trading” strategy; camouflaging *when* to trade (she called them “opaque ETFs,” as they only post holdings at month’s end instead of daily); and camouflaging *what* to trade (ETFs that invent their own indices to track, which she called “self-indexing,” and are required to disclose their positions daily). An example of a self-indexing ETF is the Schwab 1000 ETF, which tracks the Schwab 1000 Index and is 99 percent correlated with the S&P 500 Index. Unlike S&P indices—or any other index from index companies, such as FTSE Russell, MSCI, etc.—the Schwab 1000 Index does not offer subscriptions to external investors, nor does it announce the stocks to be rebalanced before a rebalance is executed. As a result, this ETF’s rebalancing trades are less transparent and less crowded. Following is a summary of her other main findings:

* Fifty-six percent of ETFs tracked public indices and preannounced their rebalancing trades, trading entirely on reconstitution days at closing prices. Their large, uninformed trades paid 67 basis points (bps) in execution costs, a figure that is three times higher than what was paid in similar-sized institutional trades. There was also a reversal of 20 bps after they traded.
* Camouflaged trading ETFs (performed by the opaque ETFs) spread out their trades across 10 days and saved 34 bps per trade or 7.3 bps per year.
* Thirty-seven percent of ETFs used self-designed indices to avoid preannouncements of rebalancing stocks and saved 30 bps per trade and 9.6 bps per year. The alternative rebalancing schedule did lead to a tracking error of 10.6 bps per year and an [information ratio](https://www.investopedia.com/terms/i/informationratio.asp) (a measurement of portfolio returns beyond the returns of a benchmark, usually an index, compared to the volatility of those returns) of 0.69.

![](https://alphaarchitect.com/wp-content/uploads/2022/04/tableA1.jpg)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index.

Investors should note that the savings from “intelligent” trading are not insignificant. Given that the AUM (assets under management) weighted-average expense ratio of U.S. equity ETFs was only 15.1 bps per year, the 9.6 bps execution cost reflects a hidden cost of 60 percent in management fees. As Li noted: “Vanguard believes that the daily reporting of ETF holdings can encourage frontrunning and free-riding by opportunistic traders. Therefore, Vanguard ETFs publish only month-end portfolio data with 15-day lags.” Thus, Li classified them as “opaque ETFs.”

While Li only examined ETFs, her findings are just as relevant to mutual fund investors.

## **Investor Takeaway**

When considering which index or systematically structured (passive) mutual fund or ETF to utilize to gain exposure to an asset class (or factor), there are many considerations beyond just the fund’s expense ratio. For example, Li found that trading costs can vary depending on the degree of transparency of the fund’s trading strategy. And then there are the negatives described earlier that are incurred by funds that have index replication as their main objective. And, as also discussed, you should consider the degree of exposure, aka [Active Share](https://alphaarchitect.com/2016/06/can-you-spot-the-closet-indexer-introducing-visual-active-share/), a fund has to the factors/asset class you are investing in. The differences in exposure to factors such as size, value, profitability/quality, and momentum can lead to significant differences in expected (and realized) returns. Thus, even when considering two passively managed funds from the same asset class, due diligence should go well beyond just the expense ratio.

Finally, when considering [between a mutual fund and an ETF](https://alphaarchitect.com/2019/10/etfs-vs-mutual-funds-who-wins-investors-ryan-kirlin/), while an ETF is likely to be more [tax-efficient](https://alphaarchitect.com/2014/01/etf-and-mutual-fund-taxation-remind-me-mutual-funds-exist/)(4), an ETF also incurs explicit trading costs when buying/selling that might be higher than the indirect trading costs incurred by a mutual fund.(5) While a mutual fund trades at its net asset value (NAV), when trading an ETF, you must consider not only the bid-offer spread but also the fact that you might be paying slightly above the NAV when buying, and you might receive less than the NAV when selling. This is particularly true for ETFs which hold less liquid underlying securities and when there are events that [impact market liquidity](https://alphaarchitect.com/2021/10/etf-liquidity-risks-a-discussion/).  That said, mutual funds only trade at NAV at the end of the day, so unless you put your order in at the close, the NAV you’re executed at could be materially different than when you placed your trade.

## Important Disclosures

*For informational and educational purposes only and should not be construed as specific investment, accounting, legal, or tax advice.  Certain information is based upon third party data which may become outdated or otherwise superseded without notice.  Third party information is deemed to be reliable, but its accuracy and completeness cannot be guaranteed. Indices are not available for direct investment. Their performance does not reflect the expenses associated with the management of an actual portfolio nor do indices represent results of actual trading. By clicking on any of the links above, you acknowledge that they are solely for your convenience, and do not necessarily imply any affiliations, sponsorships, endorsements or representations whatsoever by us regarding third-party websites. We are not responsible for the content, availability or privacy policies of these sites, and shall not be responsible or liable for any information, opinions, advice, products or services available on or through them. The opinions expressed by featured authors are their own and may not accurately reflect those of the Buckingham Strategic Wealth®. Neither the Securities and Exchange Commission (SEC) nor any other federal or state agency have approved or determined the accuracy or adequacy of this article.  LSR-21-195*

References[+]

References

|  |  |
| --- | --- |
| ↑1 | they are virtual substitutes for one another |
| ↑2 | though they can trade patiently using, for example, algorithm-based trading programs |
| ↑3 | avoiding buying stocks that are exhibiting negative momentum and delaying selling stocks with positive momentum |
| ↑4 | only important for taxable accounts |
| ↑5 | A mutual fund will still incur trading costs when they deploy the new cash to buy/sell securities, whereas an ETF is delivered securities and does not incur the trading costs because they are borne by the authorized participants. |

 function footnote\_expand\_reference\_container\_72342\_53() { jQuery('#footnote\_references\_container\_72342\_53').show(); jQuery('#footnote\_reference\_container\_collapse\_button\_72342\_53').text('−'); } function footnote\_collapse\_reference\_container\_72342\_53() { jQuery('#footnote\_references\_container\_72342\_53').hide(); jQuery('#footnote\_reference\_container\_collapse\_button\_72342\_53').text('+'); } function footnote\_expand\_collapse\_reference\_container\_72342\_53() { if (jQuery('#footnote\_references\_container\_72342\_53').is(':hidden')) { footnote\_expand\_reference\_container\_72342\_53(); } else { footnote\_collapse\_reference\_container\_72342\_53(); } } function footnote\_moveToReference\_72342\_53(p\_str\_TargetID) { footnote\_expand\_reference\_container\_72342\_53(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } } function footnote\_moveToAnchor\_72342\_53(p\_str\_TargetID) { footnote\_expand\_reference\_container\_72342\_53(); var l\_obj\_Target = jQuery('#' + p\_str\_TargetID); if (l\_obj\_Target.length) { jQuery( 'html, body' ).delay( 0 ); jQuery('html, body').animate({ scrollTop: l\_obj\_Target.offset().top - window.innerHeight \* 0.2 }, 380); } }
