---
title: "Trend-Following Filters – Part 9"
slug: "trend-following-filters-part-9"
date: "2025-06-19"
modified: "2025-06-16"
url: "https://alphaarchitect.com/trend-following-filters-part-9/"
categories: ["Empirical Methods", "Research Insights", "Trend Following", "Guest Posts"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Trend-Following Filters – Part 9

> This article examines and compares, from a digital signal processing (DSP) time domain perspective, several filters that are modeled on the assumption that the input follows a second order process, i.e., the input contains a linear trend. These filters are, by design, better able to track linear trends than some other more commonly-used filters, such as moving average, exponential smoothing, etc., which exhibit lag, or a time delay, in response to trends. Filters modeled on a second order process are commonly referred to in the technical analysis literature as “zero lag” filters.

## 1. Introduction

A previous article, “Trend-Following Filters – Part 7” [1], examined several digital filters, commonly used by technical analysts to aid in making trading decisions, from a digital signal processing (DSP) time domain perspective. The filters include moving average (MA),linear weighted moving average (LWMA), and exponential smoothing (ES), which are low pass filters modeled on the assumption that the input follows a first order process, i.e., one that has a locally constant mean value *a* and is contaminated with normally distributed random noise ε(t) where ε(t) ~ N(0, σε2):

first order process – mean *a*:   x(t) = *a* + ε(t)

These filters are designed to estimate the mean value *a* of the input by attenuating the random noise ε(t).

This article examines, also from a time domain perspective, several low pass filters modeled on the assumption that the input follows a second order process. A second order process consists of a mean *a* and a linear trend *b* which is contaminated with random normally distributed noise ε(t) where ε(t) ~ N(0, σε2):

second order process – mean *a* and linear trend *b*:   x(t) = *a* + *b*\*t + ε(t)

Among the filters examined are:

* double moving average (DMA) mean filter
* double linear weighted moving average (DLWMA) mean filter
* double exponential smoothing (DES) mean filter.

These filters were previously analyzed from a DSP frequency domain perspective in “Trend-Following Filters – Part 1/2” [2]. The second order process mean regression (SOMR) filter is also included in the analysis. SOMR is a low pass filter based on a second order process time series regression model and was analyzed in the frequency domain in “Trend-Following Filters – Part 8” [3]. Brief overviews of the four filters are provided in Section 3.

As discussed in [1], the output of low pass filters modeled on a first order process exhibit lag, or time delay, relative to the input if the input contains a trend. Since financial time series typically contain trends, these filters can have limited usefulness in identifying the beginning and ending of trends on a timely basis. Filters modeled on a second order process are, by design, better able to track linear trends and are commonly referred to in the technical analysis literature as “zero lag” filters.

In this article, the four second order low pass filters are examined using several time response specifications, including ones used in control system engineering [4]. The specifications are grouped into *transient response* and *steady-state response*categories:

* *Transient response* is defined as the temporary behavior of a system or filter after a change in the input that affects its equilibrium condition.
* *Steady-state response* is defined as the behavior of a system or filter when it is in an equilibrium condition. Steady-state occurs after all transient effects have subsided and the system or filter has settled into a stable state.

The specifications included are:

* transient response – delay time, rise time, peak time, peak overshoot, settling time, and trend reversal time
* steady-state response – lag, unit ramp steady-state error, and unit quadratic parabola steady-state error.

Technical analysts are interested in the ability of indicators not only to rapidly respond to changes in trend direction but also to minimize noise that can result in “whipsaw” trading losses. So, in addition to these specifications, variance reduction ratio (VRR), a measure of noise rejection, is included.

The specifications are defined in Section 4. In Section 5, the filter responses and VRR are shown graphically and compared, illustrating the inherent trade-off between filter responsiveness and noise minimization. Additionally, the second order filter specifications are compared, on an equivalent basis, to those of the three first order filters mentioned above. The specification equations for each filter can be found in the respective appendices.

## 2.    Note on Underlying Concepts

The characteristics of financial time series, along with the concepts of time domain and frequency domain, finite impulse response (FIR) and infinite impulse response (IIR) filters, low pass filters, difference equations, unit pulse response, and related topics, are discussed in “An Introduction to Digital Signal Processing for Trend Following” [5]. In addition, the various inputs used to determine the filter specifications are described in Section 2 of [1], including unit step, unit ramp, and trend reversal.

This article assumes familiarity with these concepts.

## 3. Overview of the Filters

This section provides brief overviews of the four filters analyzed in this article.

### Double Moving Average (DMA) Mean Filter

The double moving average (DMA) mean filter is a time series forecasting and process control method that uses two single moving averages to estimate the mean of time series that contain linear trends, as defined by Brown in [8]. (See [5] for more details regarding the single moving average.) The DMA mean filter FIR difference equation is:

![](https://alphaarchitect.com/wp-content/uploads/2025/05/DMA-Mean-Filter-Difference-Equation.png)

where the parameter N (N > 1) is the length of the two single moving averages used to calculate the double moving average and x(t) represents the input at integer time t. See [2] for additional details of the DMA mean filter, including the derivation of the difference equation.

### Double Linear Weighted Moving Average (DLWMA) Mean Filter

The double linear weighted moving average (DLWMA) mean filter is a modified form of the double moving average which uses two single linear weighted moving averages instead of two single moving averages to estimate the mean. (See [5] for more details regarding the single linear weighted moving average.) The DLWMA mean filter FIR difference equation is:

![](https://alphaarchitect.com/wp-content/uploads/2025/05/DLWMA-Mean-Filter-Difference-Equation.png)

where the parameter M (M > 1) is the length of the two single linear weighted moving averages used to calculate the double linear weighted moving average and x(t) represents the input at integer time t. See [2] for additional details of the DLWMA mean filter, including the derivation of the difference equation.

### Double Exponential Smoothing (DES) Mean Filter

The double exponential smoothing (DES) mean filter is similar to the double moving average, except that it uses two single exponential smoothings instead of two moving averages to estimate the mean, as defined by Brown in [8]. The DES mean filter IIR difference equation is:

![](https://alphaarchitect.com/wp-content/uploads/2025/05/DES-Mean-Filter-IIR-Difference-Equation.png)

where the parameter α (0 <= α <= 1) is the exponential smoothing constant of the two single exponential smoothings used to calculate the double exponential smoothing and x(t) represents the input at integer time t. (See [5] for more details regarding single exponential smoothing.) The corresponding FIR difference equation is:

![](https://alphaarchitect.com/wp-content/uploads/2025/05/DES-Mean-Filter-FIR-Difference-Equation.png)

See [2] for additional details of the DES mean filter, including the derivation of the difference equation.

### Second Order Process Mean Regression (SOMR) Filter

Section 5 of [3] shows the derivation of the second order process mean regression (SOMR) filter FIR difference equation, which is:

![](https://alphaarchitect.com/wp-content/uploads/2025/05/SOMR-Mean-Filter-Difference-Equation.png)

where the parameter n (n > 2) is the filter length and x(t) represents the input at integer time t. This filter is sometimes called an “end point moving average” or a “least squares moving average”.

### Example Filter Unit Pulse Response Coefficients

The graphs below show representative examples of the unit pulse response coefficients h(i) of the four filters, using the indicated parameter values, i.e., DMA parameter N = 10, DLWMA parameter M = 10, DES smoothing constant α = 0.1818, and SOMR parameter n = 10, with the DES coefficients displayed limited to the first 21.

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Example-Filter-Unit-Pulse-Response-Coefficient-Graphs.png)

## 4.    Filter Time Domain Specifications

This section defines the filter time domain specifications used in this article. The specification equations for each of the filters can be found in the respective appendices.

Note: Due to the complexity of the second order filter difference equations, it is difficult to derive closed-form analytic equations as functions of the filter parameters for many of the specifications. As an alternative, a number of the specification equations that appear in the appendices were determined by applying least squares regression to a series of measurements of the filter responses to the inputs across a wide range of parameter values. All of the resulting regression models have coefficients of determination R2 very close to 1 and small standard errors of estimate S, as indicated in the appendices.

### 4.1 Transient Response Specifications

### Delay Time

Delay time τd is measured as the number of time steps, starting at t = 0, required for the filter output to rise from 0% to 50% (0.5) of its final steady-state value in response to a unit step input. The graph below illustrates the delay times of the four filters, using the example filter parameter values. The delay time is observed when the filter output reaches the 0.5 level.

Note: The markers in the following specification graphs indicate the discrete values at each integer time t. The connecting lines have been added for visual enhancement and do not represent continuous values.

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Unit-Step-Response-Graph.png)

### Rise Time

Rise time τr is measured as the number of time steps, starting at t = 0, required for the filter output to rise from 0% to 90% (0.9) of its final steady-state value in response to a unit step input.The graph above illustrates the rise times of the four filters, using the example filter parameter values. The rise time is observed when the filter output reaches the 0.9 level.

### Damping Response

There are four types of damping response that can occur in the output of filters modeled on second and higher order processes during a transient state, depending on the filter design:

* overdamped – the output gradually approaches the final steady-state value without any overshoot of the final steady-state value or any oscillation
* critically damped – the output approaches the final steady-state value in the minimum amount of time without any overshoot or oscillation
* underdamped – the output overshoots the final steady-state value and possibly oscillates, with the overshoot or oscillation gradually decreasing as it approaches the final steady-state value
* undamped – output oscillation continues indefinitely with no decrease, or possibly even an increase, in amplitude over time, so no final steady-state value is reached.

The following graph illustrates examples of overdamped, critically damped, and underdamped responses to a unit step input.

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Example-Unit-Step-Damping-Responses.png)

See, for example, [7] and [9] for additional details regarding the damping response of second order systems and filters.

### Peak Time

Peaking occurs in filter response if the filter design results in underdamping, in which case the output overshoots the final steady-state value before returning to it. The responses of the four second order filters analyzed in this article are all underdamped. In contrast, the responses of the first order low pass filters analyzed in [1] are either overdamped or critically damped, and, as a result, do not exhibit peaking or oscillation.

Peak time τp is measured as the number of time steps, starting at t = 0, for the filter output to reach its maximum peak value before settling at the final steady-state value in response to a unit step input. The unit step response graph above illustrates the peak times of the four filters, using the example filter parameter values.

### Peak Overshoot

Peak overshoot Mp is measured as the percentage difference between the maximum peak value and the final steady-state value in response to a unit step input. The unit step response graph above illustrates the peak overshoot of the four filters, using the example filter parameter values, which occurs at their respective peak times.

### Settling Time

Settling time τs is measured as the number of time steps, starting at t = 0, required for the filter output to reach and remain at the final steady-state value or, in some cases, within a specified tolerance of the final steady-state value, in response to a unit step input. In general, settling time is the number of time steps until the unit step input has reached all the filter coefficients.

The unit step response graph above illustrates the settling times of the four filters, using the example filter parameter values. For the DMA, DLWMA, and SOMR filters, settling time is observed when the filter output reaches the 1.0 level following the peak. Since the DES filter has an infinite unit step transient response time, settling time is considered here to occur when the output is within 1% of its steady-state value following the peak, i.e., at the 1.01 level.

### Trend Reversal Time

For the first order low pass filters analyzed in [1], trend reversal time τtr is measured as the number of time steps, starting at t = 0, required for the filter output to intercept the trend reversal input following the point where the trend changes direction. Using this measure for the four second order low pass filters, trend reversal occurs at t = 1 for all parameter values, due to the filters having a unit ramp steady-state error of zero up to t = 0, followed by a peak overshoot due to underdamping, as shown in the graph below.

An alternate trend reversal time measure is the number of time steps between the time of the trend reversal input peak at t = 0 and the time at which filter output reverses direction following its own peak. This alternate measure, denoted by τtr’, is used in this analysis. The graph below illustrates the trend reversal times of the four filters, using the example filter parameter values. Note that using a trend reversal input with slopes other than +1 and -1 results in the same relative filter responses.

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Trend-Reversal-Response-Graph.png)

### 4.2 Steady-State Response Specifications

### Lag

Lag, the time delay of the filter output relative to the filter input, is typically measured by the response of a filter to a unit ramp input, once the filter output has reached a steady-state condition. Lag can be calculated as the sum of the time-weighted filter unit pulse response coefficients h(i), as defined by Brown in [8]:

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Lag-Equation.png)

where k = number of filter unit pulse response coefficients and h(i) = unit pulse response coefficient for i = 0, 1, 2, …, k-1.  Note that the time weights are the same as the unit ramp input.

As shown graphically below, for the DMA, DLWMA, and SOMR filters, in response to a unit ramp input, lag is zero, starting at steady-state, i.e., settling time. For the DES filter, lag asymptotically approaches zero as t increases. Note that using a ramp input with a slope other than +1 results in the same relative filter responses.

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Unit-Ramp-Response-Graph.png)

As discussed in [1], low pass filters modeled on a first order process, such as MA, LWMA, and ES, exhibit non-zero lag in steady-state if the input contains a trend. On the other hand, low pass filters modeled on a second order process, such as DMA, DLWMA, DES, and SOMR, exhibit zero lag in steady-state to an input containing a linear trend. As a result, these filters are often referred to as “zero lag” filters. However, these filter have non-zero lag in response to inputs that contain higher order trends, as shown below.

### Unit Ramp Steady-State Error

Steady-state error ess is defined as the difference between the input x(t) and output y(t) of a system or filter when the output has reached steady-state in response to a unit input. Different unit inputs are used to measure different types of steady-state error. For example, unit ramp steady-state error ess\_rmeasures the difference between the filter input and output in response to a unit ramp input when the filter has reached steady-state at settling time.

For low pass filters modeled on a first order process, the unit ramp steady-state error ess\_r equals the lag [1]. As shown in the graph above, for the DMA, DLWMA, and SOMR filters, the unit ramp steady-state error ess\_r equals zero, starting at settling time. For the DES filter, the unit ramp steady-state error asymptotically approaches zero as t increases. Note that using a ramp input with a slope other than +1 results in the same relative filter responses.

### Unit Quadratic Parabola Steady-State Error

An additional specification, unit quadratic parabola steady-state error ess\_qp measures the difference between the filter input and output in response to a discrete-time unit quadratic parabola input when the filter response reaches steady-state at settling time. The unit quadratic parabola input is based on a second-degree quadratic polynomial function and is denoted by qp(t) where:

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Unit-Quadratic-Parabola-Function-Equation.png)

The unit quadratic parabola function is illustrated in the following graph.

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Unit-Quadratic-Parabola.png)

As shown in the graph below, for the four filters, the unit quadratic parabola steady-state error is non-zero and is a function of the filter parameter value, similar to the lag and unit ramp steady-state error of filters modeled on a first order process. Note that using a quadratic parabola input with a coefficient other than ½ results in the same relative filter responses.

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Unit-Quadratic-Parabola-Response-Graph.png)

### 4.3 Variance Reduction Ratio

For time series containing normally distributed random noise ε(t) ~ N(0, σε2), the variance reduction ratio (VRR) of a filter measures the reduction in the variance of the filter output y(t) relative to the variance of the filter input σε2 and is calculated by summing the squares of the filter unit pulse coefficients h(i), as defined by Brown in [8]. VRR is the ratio of the filter output variance σy2 to the input variance οε2:

![](https://alphaarchitect.com/wp-content/uploads/2025/05/VRR-Equation.png)

where k = number of filter unit pulse response coefficients and h(i) = filter unit pulse response coefficient for i = 0, 1, 2, …, k-1. The smaller the ratio, the greater the noise reduction. For example, VRR = 0 indicates complete noise reduction, whereas VRR = 1 indicates no noise reduction.

## 5.    Filter Specification Comparison

In general, for low pass filters modeled on a second order process:

* The speed with which a filter responds to a change in the input can be measured by delay time, rise time, settling time, and trend reversal time.
* Filter tracking error, i.e., how closely the filter output follows the input, can be measured by peak time, peak overshoot, lag, unit ramp steady-state error, and unit quadratic parabola steady-state error.
* Filter noise rejection can be measured by the variance reduction ratio (VRR).

The following graphs show the specifications of the four second order filters across a range of filter parameter values. Note that lag and unit ramp steady-state error are not shown since they are both zero for these filters.

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Filter-Specification-Graphs-1.png)

The graphs indicate that, in general, the larger the filter parameters N, M, and n, or the smaller the smoothing constant α, the smaller the VRR but also the greater the delay time, rise time, peak time, peak overshoot, settling time, and trend reversal time.

In order for the specifications to be comparable across the filters, the filter parameter values need to be standardized. As discussed in [5], an important metric for analyzing and comparing the time domain characteristics of filters is the average age of the data (AAD) passing through them, as defined by Brown in [8]. The graphs below show the AADs of the four filters across a range of parameter values. The AAD equations are shown in the respective appendices.

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Filter-AAD-Graphs.png)

Note that the DLWMA filter AAD values are very close, although not identical, to those of the SOMR filter for parameter values M = n.

Since AAD is commonly used in the technical analysis literature to calculate equivalent filter parameters, the method chosen here is to convert the parameters values to the corresponding single moving average filter length, denoted by N1, so they have equivalent AAD. The filter parameter conversion equations are shown below.

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Equivalent-AAD-Filter-Parameters-1.png)

The graphs below show the specifications for the four filters standardized on the corresponding equivalent-AAD single moving average filter length N1.

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Eqivalent-AAD-Filter-Specification-Graphs-1.png)

The graphs indicate that:

* DMA has the shortest delay time, rise time, peak time, settling time, and trend reversal time but the largest peak overshoot and the highest VRR.
* DES has the longest delay time, rise time, peak time, settling time, and trend reversal time but the smallest peak overshoot and the lowest VRR.

Comparing the three low pass filters modeled on a first order process (see [1]) and the four low pass filters modeled on a second order process, using the specifications they have in common, indicates that, on an equivalent-AAD basis:

* DMA has the shortest delay time and rise time but the highest VRR.
* MA has the longest delay time.
* ES has the longest rise time.
* LWMA has the lowest VRR.

Using the alternate trend reversal time specification for all the filters, on an equivalent-AAD basis:

* DMA has the shortest trend reversal time.
* MA has the longest trend reversal time.

The alternate trend reversal time equations for the three first order low pass filters are shown in Appendix 5.

## 6.    Comments

Low pass filters modeled on first order processes, such as MA, LWMA, and ES, exhibit non-zero lag and non-zero steady-state error in response to linear, quadratic parabola, and higher order trends.

Low pass filters modeled on second order processes, such as DMA, DLWMA, DES, and SOMR, are often referred to as “zero lag” filters, due to their ability to track linear trends in steady-state with no lag. However, they exhibit non-zero lag and non-zero steady-state error in response to quadratic parabola and higher order trends.

From a practical standpoint, all low pass filters, when operating on financial time series, are often, if not usually, in a transient state, due to the volatility and non-stationarity of those time series [5]. As a result, the output of all of these filters generally display some amount of lag for much of the time, whether they are labeled as “zero lag” or not.

## Appendix 1 – Double Moving Average (DMA) Mean Filter Specifications

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Appendix-1.png)

## Appendix 2 – Double Linear Weighted Moving Average (DLWMA) Mean Filter Specifications

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Appendix-2a.png)

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Appendix-2b.png)

## Appendix 3 – Double Exponential Smoothing (DES) Mean Filter Specifications

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Appendix-3a.png)

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Appendix-3b.png)

## Appendix 4 – Second Order Process Mean Regression (SOMR) Filter Specifications

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Appendix-4.png)

## Appendix 5 – First Order Filter Alternate Trend Reversal Time Specifications

![](https://alphaarchitect.com/wp-content/uploads/2025/05/Appendix-5.png)

## References

[1] Stern, H., “Trend-Following Filters – Part 7”, October 2023, updated: March 2025; available online at <https://alphaarchitect.com/2023/10/trend-following-filters-part-7/>.

[2] Stern, H., “Trend-Following Filters – Part 1/2”, December 2020; available online at <https://alphaarchitect.com/2020/12/29/trend-following-filters-part-1-2/>.

[3] Stern, H., “Trend-Following Filters – Part 8”, September 2024; available online at <https://alphaarchitect.com/2024/09/trend-following-filters-part-8/>.

[4] Gowda, K., “Control Systems 2.4 – Time Response Specifications”, March 2021; available online at <https://www.circuitbread.com/tutorials/time-response-specifications-2.4>.

[5] Stern, H., “An Introduction to Digital Signal Processing for Trend Following”, August 2020, updated: March 2025; available online at <https://alphaarchitect.com/2020/08/an-introduction-to-digital-signal-processing-for-trend-following/>.

[6] Schwarz, R. J. and Friedland, B., *Linear Systems*, McGraw-Hill, 1965.

[7] Oppenheim, A. V., Willsky, A. S., and Young, I. T., *Signals and Systems*, Prentice Hall, 1983.

[8] Brown, R. G., *Smoothing, Forecasting, and Prediction of Discrete Time Series*, Prentice Hall, 1962.

[9] Gowda, K., “Control Systems 2.3 – Second Order Systems”, January 2021; available online at <https://www.circuitbread.com/tutorials/second-order-systems-2-3>.
