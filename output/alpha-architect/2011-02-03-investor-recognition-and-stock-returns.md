---
title: "Investor Recognition and Stock Returns"
slug: "investor-recognition-and-stock-returns"
date: "2011-02-03"
modified: "2022-06-04"
url: "https://alphaarchitect.com/investor-recognition-and-stock-returns/"
categories: ["Research Insights", "Behavioral Finance"]
tags: ["Paper Reviews", "abnormal returns", "investor recognition"]
best_of: false
source: "alphaarchitect.com"
---

# Investor Recognition and Stock Returns

> “We analyze the relation between investor recognition and stock returns. Consistent with Merton’s (1987) theoretical analysis, we show that (i) contemporaneous stock returns are positively related to changes in investor recognition, (ii) future stock returns are negatively related to changes in investor recognition, (iii) the above relations are stronger for stocks with greater idiosyncratic risk and (iv) corporate investment and financing activities are both positively related to changes in investor recognition. Our results demonstrate that investor recognition is an important determinant of both stock returns and real corporate activity.” Abstract: “We analyze the relation between investor recognition and stock returns. Consistent with Merton’s (1987) theoretical analysis, we show that (i) contemporaneous stock returns are positively related to changes in investor recognition, (ii) future stock returns are negatively related to changes in investor recognition, (iii) the above relations are stronger for stocks with greater idiosyncratic risk and (iv) corporate investment and financing activities are both positively related to changes in investor recognition. Our results demonstrate that investor recognition is an important determinant of both stock returns and real corporate activity.”

### Investor Recognition and Stock Returns

* Reuven Lehavy and Richard G. Sloan
* The Review of Accounting Studies, Vol. 13,  2008.
* An older version of the paper can be found [here](http://w4.stern.nyu.edu/emplibrary/Lehavy_Sloan.pdf).

### **Abstract:**

> We analyze the relation between investor recognition and stock returns. Consistent with Merton’s (1987) theoretical analysis, we show that (i) contemporaneous stock returns are positively related to changes in investor recognition, (ii) future stock returns are negatively related to changes in investor recognition, (iii) the above relations are stronger for stocks with greater idiosyncratic risk and (iv) corporate investment and financing activities are both positively related to changes in investor recognition. Our results demonstrate that investor recognition is an important determinant of both stock returns and real corporate activity.

### **Data Sources:**

The data pertaining to institutional ownership are gathered from the CDA/Spectrum 13F Institutional Transaction files.  These files contain data on all 13F filings beginning in 1981, though the authors begin their sample period in 1982.  Stock return data come from the Center for Research in Securities Prices (CRSP), fundamental data come from Compustat.  As control variables, the authors also use  analyst data, which comes from I/B/E/S.

Free/cheap alternatives do accomplish the same mission can be found at <http://whalewisdom.com/> for the 13F data and <http://finance.yahoo.com/> for return data.

### **Discussion:**

The thesis of this paper is that investors prefer to choose companies with which they are familiar when constructing portfolios. Because “limited attention” results in some companies receiving scant attention from the investing public, some stocks are more efficiently priced than others.  The useful empirical finding in the paper is that those companies that receive the least recognition outperform those that receive the most.

This idea of investor recognition was first suggested by Robert Merton in 1987 in a paper called “A simple model of capital market equilibrium with incomplete information.”  Merton theorized that if investors avoid stocks with which they are unfamiliar, then the market for such stocks will be much smaller.  Other investors will therefore rationally demand a higher rate of return to compensate them for this increased firm-specific risk.

Because “investor recognition” is a rather nebulous concept, the authors choose to construct a proxy for this variable using easily accessible data.  The authors choose to observe the level of institutional ownership, defined as the proportion of all institutions submitting quarterly 13F filings that have a long position in the stock.  The assumption behind this proxy is that institutional money managers are victims of the same behavioral biases as individuals, and suffer from limited attention.  Further, we  should expect that the proportion of individuals that own the security is directly related to the proportion that are aware of the security.

The research methodology in the paper relies on a slightly different proxy than the proportion of institutions with a long position. Specifically, the authors look at *changes* in the proportion of institutional ownership from one quarter to the next.

![](https://alphaarchitect.com/wp-content/uploads/2011/02/Untitled.jpg "Investor Recognition Proxy")  
The reason they use changes as opposed to levels is for the statistical appeal.  According to Merton’s theory, the discount that investors demand of these “unrecognized” stocks will shrink as the stock becomes more recognized, and this results in higher returns.  Thus, by using the change variable we can identify those stocks that we actually expect to outperform, rather than those that are priced at a discount, but for which we have no reason to expect them to ever rise to fundamental value.

The authors break the universe of stocks in to deciles on the basis of the change in institutional ownership and then observe the stocks’ returns during the same quarter.  They find that those stocks in the decile of  stocks with the highest change in institutional ownership generate size-adjusted returns of 14.4% whereas the lowest decile generates returns of –11.0%.  As amazing as these results are, they are of little use to the investor because the returns and the change in institutional ownership are occur during the same quarter.  That is, the investor won’t know which stocks have the highest change until after the 14.4% return has already been generated.  Nevertheless, these results do indicate that an increase in recognition seems to correct an underpricing.

[![](https://alphaarchitect.com/wp-content/uploads/2011/02/Untitled.png "Untitled")](https://alphaarchitect.com/wp-content/uploads/2011/02/Untitled.png)

“The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.”

Next the authors consider the relation between change in institutional ownership and future returns.  These results are slightly more complicated because there is noticeable autocorrelation in the change variable, meaning a change in institutional ownership in the current quarter is generally preceded by a similar change in the previous quarter.  Without controlling for this autocorrelation, it appears the change in institutional ownership cannot predict future returns.  However, after implementing such controls the results are very different.   A regression of future returns on current and previous changes in institutional ownership produces a positive intercept—indicating that current changes and previous changes in institutional ownership, considered together, may be able to predict returns.

This paper fails to provide enough empirical evidence upon which to base a real-world trading strategy, yet its insights are very important.  Changes in investor recognition are likely related to higher returns.  Following from the theory, this occurs because underfollowed stocks are priced at a discount, and as institutions become aware of a stock, they begin buying them until the discount has been eliminated.

Ideally, we would be able to predict which stocks will see an increase in institutional ownership.  With the ability to do that, we could easily capture some of the phenomenal return difference between high recognition and low recognition stocks. Another idea is to look at analyst coverage initiations (I know there are already papers on this subject but they are slipping my mind at the moment). Unfortunately, this paper does not go in to depth on how to achieve this goal, but a little creativity and a powerful concept can often lead to interesting results.

### **Investment Strategy:**

1. Identify a proxy for investor recognition in real-time (if possible).
2. Long stocks with low recognition
3. Short stocks with high recognition.
4. Make money.

### **Commentary:**

The authors of this paper essentially show us the results for a strategy that front-runs institutional investors–woohoo! Moreover, it is hard to determine whether the proxy they use for “investor recognition” is really a proxy for investors not knowing about a particular stock or simply a proxy for stocks that have unexpected news and therefore abnormal returns that would be unpredictable before hand.

Despite some gripes, I think the theoretical idea underpinning this paper is excellent–stocks that spend $0 on investor relations and promotion are likely to be undervalued…now we just have to develop measures to find these companies!
