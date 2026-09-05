---
title: "Trend-Following with Valeriy Zakamulin: Anatomy of Trading Rules (Part 4)"
slug: "trend-following-valeriy-zakamulin-anatomy-trading-rules-part-4"
date: "2017-08-13"
modified: "2022-05-12"
url: "https://alphaarchitect.com/trend-following-valeriy-zakamulin-anatomy-trading-rules-part-4/"
categories: ["Trend Following", "Trend-Following Course", "Introduction Course", "Guest Posts", "Investor Education"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Trend-Following with Valeriy Zakamulin: Anatomy of Trading Rules (Part 4)

> In our context, a technical trading indicator can be considered as a combination of a specific technical trading rule with a particular moving average of […]

In our context, a technical trading indicator can be considered as a combination of a specific technical trading rule with a particular moving average of prices. In two preceding blog posts we showed that there are many technical trading rules, as well as there are many popular types of moving averages. As a result, there exist a vast number of potential combinations of a specific trading rule with a specific moving average of prices. So far, the development in this field has consisted in proposing new ad-hoc trading rules and using more elaborate types of moving averages in the existing rules. Each new proposed rule (or moving average) appears on the surface as something unique. Often this new proposed rule (or moving average) is said to be better than its competitors; such a claim is usually supported by colorful narratives and anecdotal evidence.

The existing situation in the field of market timing with moving averages is as follows. Technical traders are overwhelmed by the variety of choices between different trading indicators. Because traders do not really understand the response characteristics of the trading indicators they use, the selection of a trading indicator is made based mainly on intuition rather than any deeper analysis of commonalities and differences between miscellaneous choices for trading rules and moving averages. It would be no exaggeration to say that the existing situation resembles total chaos and mess from the perspective of a newcomer to this field. Therefore there is an urgent need to bring some order to the chaos in the field of market timing with moving averages.

In this blog post we uncover the anatomy of market timing rules with moving averages of prices. In particular, we are going to show that the computation of a technical trading indicator for every market timing rule can be interpreted as the computation of a weighted moving average of price changes over the averaging window. More formally, we will show that the computation of a technical trading indicator for every market timing rule can be written as

```
![   \text{Indicator}_t^{TR(n)} = \sum_{i=1}^{n-1} \pi_i \Delta P_{t-i}, ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-c71b8840b19efd57ab12706a991e7928_l3.png "Rendered by QuickLaTeX.com")
```

where, recall, *ΔPt-i=Pt-i+1-Pt-i* denotes the price change and *πi* is the weight of the price change *ΔPt-i* in the computation of a weighted moving average of price changes. Therefore, despite a great variety of trading indicators that are computed seemingly differently at the first sight, the only real difference between the diverse trading indicators lies in the weighting function used to compute a moving average of price changes. This result allows us to study the computation of trading indicators in many market timing rules and analyze the commonalities and differences between the rules.

## Momentum Rule

The computation of the technical trading indicator for the Momentum rule can be re-written as follows:

```
![ (1) \quad  \text{Indicator}_t^{\text{MOM}(n)} = P_t - P_{t-n+1}  = (P_t-P_{t-1}) + (P_{t-1}-P_{t-2}) + \ldots + (P_{t-n+2}-P_{t-n+1}) = \sum_{i=1}^{n-1}\Delta P_{t-i}. ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-63b425a9f8746233e80a83bf01dbeae0_l3.png "Rendered by QuickLaTeX.com")
```

Therefore,

```
![ (2) \quad  \text{Indicator}_t^{\text{MOM}(n)}\equiv \frac{1}{n-1}\sum_{i=1}^{n-1}\Delta P_{t-i} = \sum_{i=1}^{n-1}\frac{1}{n-1} \Delta P_{t-i}, ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-64b5b025b50f9629682053cd9e68f68f_l3.png "Rendered by QuickLaTeX.com")
```

where the mathematical symbol “≡” means “equivalence”. To see the equivalence of equations (1) and (2), observe that

```
![   \text{if } \sum_{i=1}^{n-1}\Delta P_{t-i}>0 \text{ then } \frac{1}{n-1}\sum_{i=1}^{n-1}\Delta P_{t-i}>0 ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-a469edbfe19ba8b166c38810e313387b_l3.png "Rendered by QuickLaTeX.com")
```

(since *n-1>0*) and vice versa. Consequently, equation (2) allows us to re-interpret the computation of the technical indicator for the Momentum rule as the computation of an equally weighted moving average of price changes (where the weight of each price change equals *1/(n-1)*).

## Price Minus Moving Average Rule

First of all, recall (from Part 1) the alternative representation of a general moving average:

```
![   MA_t(n)  = P_t - \sum_{i=1}^{n-1} \phi_i \Delta P_{t-i}, \quad \phi_i = \frac{\sum_{j=i}^{n-1} w_{j} }{\sum_{j=0}^{n-1} w_{j}}, ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-e5fa9a32455d192fa159e39b7998981e_l3.png "Rendered by QuickLaTeX.com")
```

where *wj* is the price weighting function and *φi* is the price-change weighting function of a moving average. Therefore,

```
![   \text{Indicator}_t^{\text{P-MA}(n)} = P_t - MA_t(n) = \sum_{i=1}^{n-1} \phi_i \Delta P_{t-i}. ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-cca239534de3afc9a57258ab476e253e_l3.png "Rendered by QuickLaTeX.com")
```

Consequently, the computation of the technical indicator for the Price Minus Moving Average rule can equivalently be interpreted as the computation of a weighted moving average of price changes.

In case all weights *wj* are strictly positive, the sequence of weights *φi* is decreasing with increasing *i*

```
![   \phi_1>\phi_2>\ldots>\phi_{n-1}. ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-5a5faad9efd02406355cc94313425d80_l3.png "Rendered by QuickLaTeX.com")
```

Therefore, in this case, regardless of the shape of the weighting function for prices *wj*, the weighting function *φi* always over-weights the most recent price changes.

The closed-form expression for the computation of the technical indicator for the Price Minus Simple Moving Average rule is given by (we skip the details of the derivation)

```
![ (3) \quad \text{Indicator}_{t}^{\text{P-SMA}(n)} \equiv \frac{\sum_{j=1}^{n-1} (n-j) \Delta P_{t-j}}{\sum_{j=1}^{n-1} (n-j)} =  \frac{(n-1)\Delta P_{t-1} + (n-2)\Delta P_{t-2} + \ldots + \Delta P_{t-n+1}}{(n-1) + (n-2) + \ldots + 1}. ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-4cbf91f47f6da3e6399828d5aaaf933f_l3.png "Rendered by QuickLaTeX.com")
```

The resulting formula suggests that we can alternatively interpret the computation of the technical indicator for the Price Minus Simple Moving Average rule as the computation of a Linearly Weighted

Moving Average of price changes.

When the Exponential Moving Average is used in this rule, the closed-form expression for the computation of the technical indicator is given by

```
![ (4) \quad \text{Indicator}_{t}^{\text{P-EMA}(n)} \equiv \frac{\sum_{j=1}^{\infty} \lambda^j \Delta P_{t-j}}{\sum_{j=1}^{\infty} \lambda^j} = (1-\lambda) \sum_{j=1}^{\infty} \lambda^{j-1} \Delta P_{t-j}. ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-b729c01a8d2b805e3766eeda1999ea8c_l3.png "Rendered by QuickLaTeX.com")
```

In words, the computation of the trading indicator for the Price Minus Exponential Moving Average rule is equivalent to the computation of an Exponential Moving Average of price changes.

For the sake of illustration, the figure below plots the shapes of the price change weighting functions in the Momentum (MOM) rule and three Price Minus Moving Average rules: Price Minus Simple Moving Average (P-SMA) rule, Price Minus Linear Moving Average (P-LMA) rule, and Price Minus Exponential Moving Average (P-EMA) rule. In all rules, the size of the averaging window equals *n=30*. Observe that in all but the Momentum rule the weighting function overweights the most recent price changes (note that Lag 1 denotes the most recent price change).

![](https://alphaarchitect.com/wp-content/uploads/2017/07/w-p-ma.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The interactive illustration of weighting in the Price Minus Moving Average rule [can be found here](https://tjeld.uia.no/shiny/valeriz/p-ma-rule/).

## Moving Average Change of Direction Rule

The value of this technical trading indicator is based on the difference between the values of the same weighted moving average computed at times *t* and *t-1* respectively. We assume that in the moving average the size of the averaging window equals *n-1*. The reason for this assumption is to ensure that the trading indicator is computed over the window of size *n*. The straightforward computation yields

```
![  \text{Indicator}_{t}^{\Delta\text{MA}(n-1)} = MA_t(n-1)-MA_{t-1}(n-1) = \frac{\sum_{i=0}^{n-2} w_{i} P_{t-i}}{\sum_{i=0}^{n-2} w_{i}} - \frac{\sum_{i=0}^{n-2} w_{i} P_{t-i-1}}{\sum_{i=0}^{n-2} w_{i}}    = \frac{\sum_{i=1}^{n-1} w_{i-1} \Delta P_{t-i}}{\sum_{i=1}^{n-1} w_{i-1}}. ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-e04e836e830badf826b9fa09b39264c8_l3.png "Rendered by QuickLaTeX.com")
```

Consequently, the computation of the technical indicator for the Moving Average Change of Direction rule can be interpreted as the computation of a weighted moving average of price changes. It is worth noting that the weighting function for price changes is virtually identical to the weighting function for computing the moving average of prices.

Three interesting relationships can be derived on the basis of the result above. First, when the Simple Moving Average is used (where *wi-1=1* for all *i*):

```
![  \text{Indicator}_{t}^{\Delta\text{SMA}(n-1)} = \frac{\sum_{i=1}^{n-1} \Delta P_{t-i}}{\sum_{i=1}^{n-1} 1} = \frac{1}{n-1}\sum_{i=1}^{n-1}\Delta P_{t-i} \equiv \text{Indicator}_{t}^{\text{MOM}(n)}, ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-dd80c040f785649bc5c8f3d262f45ea2_l3.png "Rendered by QuickLaTeX.com")
```

where the last equivalence follows from equation (2). Second, when the Linear Moving Average is used (where *wi-1=n-i*):

```
![  \text{Indicator}_{t}^{\Delta\text{LMA}(n-1)} \equiv \frac{\sum_{i=1}^{n-1} (n-i) \Delta P_{t-i}}{\sum_{i=1}^{n-1} (n-i)} \equiv \text{Indicator}_{t}^{\text{P-SMA}(n)}, ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-7f5e8d9c41f1dd76b4436268e28152db_l3.png "Rendered by QuickLaTeX.com")
```

where the last equivalence follows from equation (3). Third, when the Exponential Moving Average is used:

```
![  \text{Indicator}_{t}^{\Delta\text{EMA}(n)} = \frac{\sum_{i=1}^{\infty} \lambda^{i-1} \Delta P_{t-i}}{\sum_{i=1}^{\infty} \lambda^{i-1}}= (1-\lambda) \sum_{j=1}^{\infty} \lambda^{j-1} \Delta P_{t-j} \equiv \text{Indicator}_{t}^{\text{P-EMA}(n)}, ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-a514cbbe50eaabb968a7e0b70d52bab1_l3.png "Rendered by QuickLaTeX.com")
```

where the last equivalence follows from equation (4).

Putting it into words, these relationships mean the following:

* The Simple Moving Average Change of Direction rule is equivalent to the Momentum rule;
* The Linear Moving Average Change of Direction rule is equivalent to the Price Minus Simple Moving Average rule;
* The Exponential Moving Average Change of Direction rule is equivalent to the Price Minus Exponential Moving Average rule.

For the sake of illustration, the figure below plots the shapes of the price change weighting functions in four Moving Average Change of Direction rules: Simple Moving Average (SMA) Change of Direction rule, Linear (LMA) Moving Average Change of Direction rule, Exponential Moving Average (EMA) Change of Direction rule, and Double Exponential Moving Average (EMAEMA) Change of Direction rule. In all rules, the size of the averaging window equals *n=30*.

![](https://alphaarchitect.com/wp-content/uploads/2017/07/w-cdir.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The interactive illustration of weighting in the Moving Average Change of Direction rule [can be found here](https://tjeld.uia.no/shiny/valeriz/cdir-rule/).

## Moving Average Crossover Rule

Using the alternative representation of a general weighted moving average, the computation of the trading indicator in the Moving Average Crossover rule can be expressed as

```
![ \text{Indicator}_t^{\text{MAC}(s,l)} = MA_t(s) - MA_t(l)= \sum_{j=1}^{l-1} \phi_j^l \Delta P_{t-j} - \sum_{j=1}^{s-1} \phi_j^s \Delta P_{t-j}, ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-80b2b68dcd736e83f5c89ac5f8edd541_l3.png "Rendered by QuickLaTeX.com")
```

where *φjl* and *φjs* are the weights of the longer and shorter moving average respectively. Another alternative expression for the computation of the trading indicator in the Moving Average Crossover rule is given by

```
![ (5) \quad \text{Indicator}_t^{\text{MAC}(s,l)} =  \sum_{j=1}^{s-1} \left(\phi_j^l-\phi_j^s \right)\Delta P_{t-j} +  \sum_{j=s}^{l-1} \phi_j^l \Delta P_{t-j}. ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-2887ea326d736e1fff9a9950eca3e5cc_l3.png "Rendered by QuickLaTeX.com")
```

The computation of the trading indicator in the Moving Average Crossover rule is basically similar to the computation of the trading indicator in the Price Minus Moving Average rule; the only difference is that the shorter moving average is used instead of the last closing price. To understand the effect of using the shorter moving average instead of the last price, we present the computation of the trading indicator in the Price Minus Moving Average rule in the following form (assuming that *n=l*)

```
![ (6) \quad \text{Indicator}_t^{\text{P-MA}(l)} =  \sum_{j=1}^{s-1} \phi_j^l\Delta P_{t-j} +  \sum_{j=s}^{l-1} \phi_j^l \Delta P_{t-j}. ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-7f0356401262a6af2a8ef9dfb7ca1c0f_l3.png "Rendered by QuickLaTeX.com")
```

The comparison of equations (5) and (6) reveals that the price change weighting functions for both the rules, *MAC(s,l)* and *P-MA(l)*, are identical beginning from lag *s* and beyond. In contrast, as compared to the price change weighting function of *P-MA(l)* rule, the price change weighting function of *MAC(s,l)* rule assigns smaller weights to the most recent price changes (from lag 1 to lag *s-1*). Since most typically the price change weighting function in the *P-MA(l)* rule overweights the most recent price changes, the reduction of weights of the most recent price changes in the *MAC(s,l)* rule makes its price change weighting function to underweight both the most recent and the most distant price changes. As a result, in this rule the weighting function for price changes takes a hump-shaped form.

For the sake of illustration, the figure below plots the shapes of the price change weighting functions in four Moving Average Crossover rules: Simple Moving Average (SMA) Crossover rule, Linear (LMA) Moving Average Crossover rule, Exponential Moving Average (EMA) Crossover rule, and Double Exponential Moving Average (EMAEMA) Crossover rule. In all rules, the sizes of the shorter and longer averaging windows equal *s=10* and *l=30* respectively.

![](https://alphaarchitect.com/wp-content/uploads/2017/07/w-mac.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The interactive illustration of weighting in the Moving Average Crossover rule [can be found here](https://tjeld.uia.no/shiny/valeriz/mac-rule/).

## Moving Average Convergence/Divergence Rule

The computation of the technical trading indicator of the original MACD rule by Gerald Appel is based on using three Exponential Moving Averages:

```
![ MAC_t(s,l) = EMA_t(s) - EMA_t(l), ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-a113109a0d50b58d5579a0675a7c3f65_l3.png "Rendered by QuickLaTeX.com")
```

```
![   \text{Indicator}_t^{\text{MACD}(s,l,n)}= MAC_t(s,l) - EMA_t(n,MAC(s,l)). ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-9ccb476a0addbede098e9ff2bd457ecd_l3.png "Rendered by QuickLaTeX.com")
```

For this rule, the computation of the trading indicator, in terms of price changes, is given by (we skip the details of the derivation)

```
![   \text{Indicator}_t^{\text{MACD}(s,l,n)} = \sum_{j=1}^{\infty}\left( \left( \lambda_l^j - \lambda_s^j \right) - (1-\lambda) \left[ \frac{\lambda_l^j-\lambda^j}{1-\frac{\lambda}{\lambda_l}} - \frac{\lambda_s^j-\lambda^j}{1-\frac{\lambda}{\lambda_s}}  \right] \right) \Delta P_{t-j}, ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-6802e58c522f6fbfdc8c6a8183044041_l3.png "Rendered by QuickLaTeX.com")
```

where

```
![   \lambda_l=\frac{l-1}{l+1}, \quad \lambda_s=\frac{s-1}{s+1}, \quad \lambda=\frac{n-1}{n+1}. ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-4f6654084d38b77d0dfd44dcb574666d_l3.png "Rendered by QuickLaTeX.com")
```

Obviously, the computation of the trading indicator can also be interpreted as calculating a weighted average of price changes. When other types of moving averages is used in this rule, the computation of the trading indicator can again be interpreted as a computation of a moving average of price changes.

The figure below illustrates the shapes of the price change weighting functions in three Moving Average Convergence/Divergence rules where the first, second, and third one are based on SMA, LMA, and EMA respectively. In all rules, the sizes of the averaging windows equal *s=12*, *l=26*, and *n=9* respectively.

![](https://alphaarchitect.com/wp-content/uploads/2017/07/w-macd.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Observe that all price-change weighting functions first increase, attain a maximum, then decrease below zero, attain a minimum, and finally increase toward zero. The pattern of the alternation of weights in these functions resembles a damped harmonic oscillator (for example, a sine wave) which suggests that these rules are supposed to react to the changes in the price trend. For example, a strong Buy signal is generated when the prices first trend downward (the price changes are negative), then upward (the price changes are positive). Similarly, a strong Sell signal is generated when the prices first trend upward, then downward. Alternatively, these rules might work well when prices are mean-reverting.

The interactive illustration of weighting in the Moving Average Convergence/Divergence rule [can be found here](https://tjeld.uia.no/shiny/valeriz/macd-rule/).

## Moving Average Envelope

We remind the reader that a moving average envelope consists of two boundaries above and below a moving average *MAt(n)*. The lower (*Lt*) and upper (*Ut*) boundaries of the moving average envelope are computed as

```
![   L_t = MA_t(n)\times(1-p), \quad U_t = MA_t(n)\times(1+p), ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-23916bcb74eff290e5d425c7e1e6e2b0_l3.png "Rendered by QuickLaTeX.com")
```

where *p* (usually specified as a percentage) is the distance from the moving average and a boundary of the envelope. The trading signal in the *MAE(n,p)* rule is generated according to:

```
![   \text{Signal}_{t+1} =   \begin{cases}     \text{Buy} & \text{if } P_t>U_t, \\     \text{Sell} & \text{if } P_t<L_t , \\     \text{Signal}_{t} & \text{if } L_t\leq P_t\leq U_t.   \end{cases} ](https://alphaarchitect.com/wp-content/ql-cache/quicklatex.com-721c80a6198e780c8459320b925779d5_l3.png "Rendered by QuickLaTeX.com")
```

It is worth noting that in all previous rules the trading signal is generated on the basis of the value of the trading indicator: positive (negative) value is translated into a Buy (Sell) signal. In contrast, in the MAE rule the trading signal is generated without the computation of the value of the trading indicator. Therefore, for this rule there is no alternative expression for the value of the trading indicator in terms of a weighted average of price changes. However, this fact does not mean that we have absolutely no clue about the shape of the price-change weighting function in the MAE rule. Since the *MAE(n,p)* rule converges to the *P-MA(n)* rule when *p* approaches zero, we have good reason to believe that the shape of the price-change weighting function in the *MAE(n,p)* rule is close to that in the *P-MA(n)* rule, at least when *p* is small.

## Summary

Our analysis revealed that all considered technical trading indicators are computed in the same general manner. In particular, any trading indicator is computed as a weighted average of price changes over the averaging window. As a result, each trading rule based on one or multiple moving averages of prices can be uniquely characterized by a single moving average of price changes. Therefore any differences between trading rules can be attributed solely to the differences between their price change weighting functions. As a natural consequence to this result, two seemingly different trading rules can be equivalent when their price change weighting functions are alike.

Our methodology of analyzing the computation of trading indicators for the timing rules based on moving averages offers a broad and clear perspective on the relationship between different rules. Whereas moving averages of prices are indispensable in visualizing how the trading signals are generated, because there is a great variety of trading rules, it is virtually impossible to see the commonalities and differences between various trading rules. In addition, if more than two moving averages are used to generate a trading signal, in this case it is also cumbersome to understand how a trading signal is generated. In contrast, our methodology of presenting the computation of the trading indicator in terms of a single moving average of price changes, rather than one or multiple moving averages of prices, uncovers the anatomy of trading rules and provides very useful insights about popular trend rules. In addition, our analysis offers a new and very insightful re-interpretation of the existing market timing rules.

The list of the useful insights about the popular trend rules, uncovered by our analysis, includes, but is not limited to, the following. First of all, in spite of the fact that there is a great number of potential combinations of a specific trading rule with a specific price weighting function (that is, a moving average of prices), there are only four basic types (or shapes) of price change weighting functions:

1. Functions that assign equal weights to all price changes (as in the MOM and ΔSMA rules);
2. Functions that overweight the most recent price changes (as in virtually all P-MA rules, ΔMA rules with ordinary moving averages, and the MAE rules);
3. Hump-shaped functions that underweight both the most recent and the most distant price changes (as in virtually all MAC rules and ΔMA rules with moving averages of moving averages);
4. Functions that have a damped waveform (as in all MACD rules and MAC rules with moving averages with less lag time). Whereas in the previous types of weighting functions all price changes have non-negative weights, in this type the weights of price changes periodically change sign from positive to negative or vice versa.

The other important insights revealed by our analysis:

* The same type of shape of the price change weighting function can be created using several alternative trading rules;
* There are trading rules with exactly the same shape of the price change weighting function; hence these rules are equivalent;
* The trading rules that have either equal, decreasing, or hump-shaped form of the price change weighting function represent the “authentic” trend rules. These rules are designed to generate correct signals when prices trend steadily upward or downward;
* The trading rules that have the damped waveform shape of the price change weighting function are designed to react to the changes in the trend direction. These rules generate correct signals when trend either accelerates or decelerates. Such rules might be profitable when either the price trend often changes its direction or prices are mean-reverting.
