---
title: "Can Machine Learning Predict Factor Returns?"
slug: "predict-factor-returns"
date: "2025-10-17"
modified: "2025-10-13"
url: "https://alphaarchitect.com/predict-factor-returns/"
categories: ["Research Insights", "Factor Investing", "Larry Swedroe", "Other Insights"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Can Machine Learning Predict Factor Returns?

> Can machine learning techniques improve the prediction of cross-sectional factor returns in equity markets?

Nusret Cakici, Christian Fieberg, Carlos Osorio, Thorsten Poddig, and Adam Zaremba, authors of the study “Picking Winners in Factorland: A Machine Learning Approach to Predicting Factor Returns,” published in the April 2025 issue of [The Journal of Portfolio Management](https://www.pm-research.com/content/iijpormgmt/51/6/96), set out to answer a critical question: Can machine learning techniques improve the prediction of cross-sectional factor returns in equity markets? They focus on the cross-sectional predictability—that is, whether it’s possible to forecast which factors (like value, momentum, size, etc.) will outperform others in the future using advanced data-driven methods rather than traditional statistical approaches. To do this, they applied a variety of popular machine learning algorithms commonly employed in prominent asset pricing studies on the returns data of 242 factor characteristics, aiming to extract predictive signals that might not be captured by conventional models. Their analysis spanned the period January 1972 to December 2021 and examined the 153 long-short anomaly portfolios in the US market from the 2023 [study](https://url.avanan.click/v2/r01/___https:/research-api.cbs.dk/ws/portalfiles/portal/95651880/theis_ingerslev_jensen_et_al_is_there_a_replication_crisis_in_finance_publishersversion.pdf___.YXAzOnNhcmFncmlsbG86YTpnOjEzZWY5ZGQ3MGQ4MTQ2MGVjMzVkMmJlZTUxNDE3ODhkOjc6YzUwNzo5ZDI3M2M4OWRlOWQ5MTRlM2U4ZTA2YzM3ZmU5NTllYjEzMGZjNDM3NmVlYzQ2M2YwM2YwNGE0YTU3YzE4NTY4OnA6VDpO) “Is There a Replication Crisis in Finance?”

> “Given the study period of January 1972 to December 2021 (600 months), the first training period is January 1972 to December 1981, the first validation period is January 1982 to December 1986, and the subsequent test period covers data from January to December 1987.”

For each annual reestimation, “we extend the training window by one year while keeping the validation and test periods fixed. The entire test period spans from January 1987 to December 2021, or 420 months.”

**Key Findings**

* There was strong cross-sectional predictability of factor returns using machine learning techniques, focusing on past returns, risks, and spreads. The magnitude of return predictability at the factor level compared favorably with the evidence at the US equity level.
* Return predictability can be translated into successful factor selection strategies—the decile of factors with the highest returns outperformed the decile with the worst prospects by 0.27% to 1.39% per month, depending on the prediction algorithm. For the forecast combination model, which aggregated the predictions of all the individual models in the study, the monthly return on such a spread portfolio was 1.08%. The alphas were robust to many considerations—although return predictability remained strong and significant, its magnitude declined by about half compared to the earlier years.
* Most alphas—excluding [OLS](https://url.avanan.click/v2/r01/___https:/www.xlstat.com/solutions/features/ordinary-least-squares-regression-ols___.YXAzOnNhcmFncmlsbG86YTpnOjEzZWY5ZGQ3MGQ4MTQ2MGVjMzVkMmJlZTUxNDE3ODhkOjc6MWZhYjpjODIyNTM2YTMyZjY1NDZjZGM0NTZjMWVkNDAwNzlkMjNmMjk3Zjk3ZTZkZjM1MmQ1ZDJjYWM4MGUzODA4MmUyOnA6VDpO#:~:text=Ordinary%20Least%20Squares%20regression%20(OLS)%20is%20a%20common%20technique%20for,often%20evaluated%20using%20r%2Dsquared.)—showed t-values exceeding 3 and, in some cases, even surpassing 4—the abnormal returns are unlikely to be mere statistical artifacts.
* The cross-sectional patterns in anomaly returns were remarkably robust and could not be explained by common asset pricing factors. They also outperformed a naive benchmark that equally weighted all anomalies in the sample.
* Factor momentum was the main driver of cross-sectional variation in anomaly returns, capturing most of the predictability the machine learning strategy— returns comoved with factor momentum. Other characteristics, such as characteristic (or value) spreads or risk measures, played minor roles. Specifically, once factor momentum was controlled for, no long–short machine learning portfolio generated significant alpha.
* The machine learning strategies required substantial portfolio rotation—each month, an investor needs to replace 37% to 66% of all factors, depending on the strategy.

Their findings led the authors to conclude: “Machine learning models capture a significant amount of return predictability, allowing them to pick winners and avoid losers among factor strategies.” They added: “Factor characteristics—including factor momentum in particular— contain valuable information about their future returns, allowing one to separate the wheat from the chaff. As a result, one can potentially pick the future winners and avoid the losers in the factor space.”

These findings on the predictive power of factor momentum provide further support to prior empirical research on the predictive power of factor momentum.

**Factor Momentum Research**

Prior empirical research on factor momentum, including the 2019 studies “[Factor Momentum Everywhere](https://url.avanan.click/v2/___https:/www.aqr.com/Insights/Research/Working-Paper/Factor-Momentum-Everywhere___.YXAzOnNhcmFncmlsbG86YTpnOjZlMTExNzIzNzI0NzI0MWM2ZWQyNGVjZGMyNGQ3ZGUyOjY6OTdjODpiMjgzYzQ3N2M5OGQyN2RkZGJjOWQ0ZDc0NTdjNGY2MTAzYzNmNjNjYTg5YWE1ZWM1YWU4NmI5Y2Y5NzIxZGIxOnA6VA)” and “[Is there Momentum in Factor Premia? Evidence from International Equity Markets](https://url.avanan.click/v2/___https:/papers.ssrn.com/sol3/papers.cfm?abstract_id=3332927___.YXAzOnNhcmFncmlsbG86YTpnOjZlMTExNzIzNzI0NzI0MWM2ZWQyNGVjZGMyNGQ3ZGUyOjY6OWFkMzpmY2M2YmJlNTU1ZDIzM2ZlYWMzZGNjZWZkNDU5MmI4Njc3ODJhOTIwNjA5MzJlZDJmNGY1YTc2YTQ3YWQ3ODkwOnA6VA),” the 2020 study “[Factor Momentum and the Momentum Factor](https://url.avanan.click/v2/___https:/papers.ssrn.com/sol3/papers.cfm?abstract_id=3014521___.YXAzOnNhcmFncmlsbG86YTpnOjZlMTExNzIzNzI0NzI0MWM2ZWQyNGVjZGMyNGQ3ZGUyOjY6ZjQ0Nzo0NjdhNzg3NjViYzMyMTY0OTcyZjU1ZDNiNjliYjhjOTY0NTE0ZjIwYjYxMzk0MmFjNGVhNjQ3MDU0OWIwN2YxOnA6VA),” and the 2021 studies “[Factor Momentum](https://url.avanan.click/v2/___https:/papers.ssrn.com/sol3/papers.cfm?abstract_id=3116974___.YXAzOnNhcmFncmlsbG86YTpnOjZlMTExNzIzNzI0NzI0MWM2ZWQyNGVjZGMyNGQ3ZGUyOjY6ZGRlMTo4MGNkNGIwZDIxMjcxNDZkNTI5ZmE4NDFmNTU3YmU0NDA3MTk0ZDBlMmJlMDYzODQxOTNmYzI3NzViY2UxZDhlOnA6VA),” [“Is Factor Momentum More than Stock Momentum](https://url.avanan.click/v2/___https:/www.risk.net/journal-of-investment-strategies/7936101/is-factor-momentum-greater-than-stock-momentum___.YXAzOnNhcmFncmlsbG86YTpnOjZlMTExNzIzNzI0NzI0MWM2ZWQyNGVjZGMyNGQ3ZGUyOjY6YzQxYzo4Y2MxOTNjNzJmN2YwZmIzMjliNGQxODQ2MmJmYTIzOWIyNjgzNTlmZjI4MzM4NGIxN2E1MzU1MzA2NzMzYWVhOnA6VA)?” and “[Momentum-Managed Equity Factors](https://url.avanan.click/v2/___https:/papers.ssrn.com/sol3/papers.cfm?abstract_id=3423287___.YXAzOnNhcmFncmlsbG86YTpnOjZlMTExNzIzNzI0NzI0MWM2ZWQyNGVjZGMyNGQ3ZGUyOjY6ZDlmOToxOWVhYmJmNmI4ODU2M2M0MjdkYjEwYTYzN2M2N2Q4NGIwZjZiNDBiYjU5MzU2ZDJlMzcxZWQwNzlkYWJkNjQyOnA6VA),” has examined whether momentum can be found in factors as well and found:

* Time-series (trend) factor momentum has been a pervasive property of factors—a strategy that buys the recent top-performing factors and sells poor-performing factors achieved significant investment performance above and beyond traditional stock momentum.
* Factor momentum explained all forms of individual stock momentum—[stock momentum](https://alphaarchitect.com/absolute-momentum-and-stock-momentum-strategies-friends-not-enemies/) strategies indirectly timed factors; they profited when the factors remained autocorrelated and crashed when those autocorrelations broke down.
* Demonstrating pervasiveness, factor momentum has been a global phenomenon. And cross-country factor momentum exists (if the value factor in Germany recently outpaced the U.S. value factor, it is likely that this trend will continue).
* Factor momentum could have been captured by trading almost any set of factors.
* Industry momentum stemmed from factor momentum.
* The value-added induced by factor management via short-term momentum was a robust empirical phenomenon that survived transaction costs and carried over to multifactor portfolios—while managing factors based on last month’s momentum increased turnover, the increase in turnover induced by timing did not outweigh the benefits of timing. In addition, turnover could have been reduced using a smoothed version of the timing signal, and timing still would have yielded significant benefits.

**Summary**

The convergence of machine learning capabilities with factor momentum research represents an advancement in quantitative investment management. However, while the Cakici et al. study demonstrates that sophisticated algorithms can indeed predict factor returns with economically meaningful magnitudes, the underlying driver remained surprisingly straightforward: factors that have performed well recently tend to continue performing well in the near term. This finding validates decades of factor momentum research while highlighting both the opportunities and challenges facing modern portfolio managers.

For practitioners, these results suggest that factor selection strategies based on momentum signals can generate alpha, though success comes at the cost of high turnover and associated transaction costs. The robustness of factor momentum across different machine learning models, time periods, and international markets indicates this is not merely a statistical artifact but a persistent market phenomenon worthy of serious consideration in factor allocation decisions.

Perhaps most importantly, this research underscores that in an era of increasingly complex quantitative methods, some of the most powerful investment insights may still stem from relatively simple behavioral patterns—in this case, the tendency for winning factors to keep winning, at least in the short run.

*Larry Swedroe is the author or co-author of 18 books on investing, including his latest*[*Enrich Your Future*](https://url.avanan.click/v2/___https:/www.amazon.com/Enrich-Your-Future-Successful-Investing/dp/1394245440/___.YXAzOnNhcmFncmlsbG86YTpnOmM4MzhlMWE2MGMwMzRlMjUyOTg4YmEwNTExZDI2OWIwOjY6ODMxMjo0YzA5ZDM0ZGJlZGNiNTQ2NDdjNDFhZWUzZmY0MTI4Nzc0NmFhMjNmNTc3N2M4N2E1ZjZmMzM5MmVlODdiMzQzOnA6VDpO)*. He is also a consultant to RIAs as an educator on investment strategies.*
