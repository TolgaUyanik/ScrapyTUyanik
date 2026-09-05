---
title: "How to Track Retail Investor Activity in TAQ"
slug: "subpenny-price-movements"
date: "2024-06-17"
modified: "2024-06-17"
url: "https://alphaarchitect.com/subpenny-price-movements/"
categories: ["Research Insights", "Basilico and Johnsen", "Academic Research Insight", "Other Insights", "Behavioral Finance"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# How to Track Retail Investor Activity in TAQ

> This paper explores the effectiveness of the BJZZ algorithm, developed by Boehmer, Jones, Zhang, and Zhang (2021), in identifying and signing retail trades executed off exchanges with subpenny price improvements.

This paper explores the effectiveness of the BJZZ algorithm, developed by Boehmer, Jones, Zhang, and Zhang (2021), in identifying and signing retail trades executed off exchanges with subpenny price improvements.

## A (Sub)penny For Your Thoughts: Tracking Retail Investor Activity in TAQ

* Barber, Huang, Jorion, Odean and Schwarz
* Journal of Finance ,2024
* A version of this paper can be found [here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4202874)
* Want to read our summaries of academic finance papers? Check out our [Academic Research Insight](https://alphaarchitect.com/category/architect-academic-insights/academic-research-insight/) category

## What are the Research Questions?

Boehmer, Jones, Zhang, and Zhang (2021), referred to as BJZZ, developed an algorithm to identify retail trades executed off exchanges, usually by wholesalers like Citadel or Virtu, which receive subpenny price improvements. This idea is based on Regulation NMS from 2005, which includes Rule 612 that bans displaying quotes with decimals smaller than one cent but allows transactions at these prices. Wholesalers often provide subpenny price improvements for many retail trades routed to them, while institutional orders are generally not executed by these wholesalers. Therefore, the BJZZ [algorithm](https://alphaarchitect.com/2014/05/algorithms-beat-intuition-evidence-everywhere/) assumes that only a small portion of subpenny off-exchange trades are institutional. To guide scholars using this method to study retail trading, the authors conducted a trading experiment from December 2021 to June 2022 to test the BJZZ algorithm’s effectiveness in identifying and accurately categorizing trades. They define the “identification rate” as the percentage of the retail trades that the algorithm correctly identifies, and the “accuracy rate” as the percentage of these identified trades that the algorithm correctly categorizes as buys or sells. The research questions are as follows:

1. How effective is the BJZZ algorithm in identifying retail trades executed off exchanges with subpenny price improvements?
2. How accurately does the BJZZ algorithm sign trades as buys or sell**s?**
3. How do the identification and accuracy rates of the BJZZ algorithm compare to the quote midpoint method?
4. What are the limitations of the BJZZ algorithm, especially in different market conditions and with varying spreads?

## What are the Academic Insights?

By analyzing data collected from through a trading experiment conducted from December 2021 to June 2022, the authors find:

1. The BJZZ algorithm is moderately effective in identifying retail trades executed off exchanges with subpenny price improvements. In fact, the algorithm correctly identified 35% of retail trades. This identification rate varies significantly across stocks, ranging from 20% to 50%, and is higher for trades with a spread of five cents or less. The algorithm’s effectiveness decreases for stocks with wider spreads, as subpenny price improvement is less common in these cases. Therefore, while the BJZZ algorithm can identify a substantial portion of retail trades, its performance is influenced by the specific characteristics of the trades and the market conditions.
2. It is variable and depends on the spread of the trades. The overall accuracy rate of the BJZZ algorithm was 72%, meaning it correctly signed 72% of the identified trades. The accuracy was higher for trades with narrower spreads, achieving 93% accuracy for trades with a one-cent spread. The accuracy significantly dropped for trades with wider spreads, falling to 52% for trades with spreads of ten cents or greater
3. Both the BJZZ algorithm and the quote midpoint method have similar identification rates because they both rely on subpenny execution to identify retail trades. However, the accuracy rates differ notably In fact, the BJZZ algorithm’s accuracy rate is 72%, meaning it correctly signs 72% of the identified trades as buys or sells. The accuracy of the BJZZ algorithm decreases significantly as the spread increases. It is 93% for trades with a one-cent spread but drops to 52% for trades with ten-cent spreads or greater. In contrast, the quote midpoint method has a much higher and more consistent accuracy rate of 95% across all spread levels. This method does not show significant variation in accuracy based on spread size.
4. The BJZZ algorithm has several limitations, particularly in different market conditions and with varying spreads: a) Accuracy Decline with Wider Spreads; b) Variability in Identification Rates, c) Market Structure Changes such as the removal of commissions and the introduction of the SEC Tick Size Pilot Program, which affected subpenny pricing, can impact the algorithm’s effectiveness in current market conditions, d) Dependence on Subpenny Execution, e) False Positives and False Negatives, f) Sensitivity to Spread Size.

## Why does this study matter?

This study is important because it shows the need to develop alternative methods. Also, while the BJZZ algorithm remains a useful tool, researchers must be mindful of its limitations and consider complementary methods to enhance the accuracy and reliability of their studies on retail trading and order imbalance.

## The Most Important Chart from the Paper:

![](https://alphaarchitect.com/wp-content/uploads/2024/06/2024-06-12-20_57_06-ssrn-4202874.pdf-800x628.png)

## Abstract

> We placed 85,000 retail trades in six retail brokerage accounts from December 2021 to June 2022 to validate the Boehmer et al. (2021) algorithm, which uses subpenny trade prices to identify and sign retail trades. The algorithm identifies 35% of our trades as retail, incorrectly signs 28% of identified trades, and yields uninformative order imbalance measures for 30% of stocks. We modify the algorithm by signing trades using the quoted spread midpoints. The quote midpoint method does not affect identification rates but reduces the signing error rates to 5% and provides informative order imbalance measures for all stocks.
