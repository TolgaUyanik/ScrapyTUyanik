---
title: "Maximum Drawdown Excel VBA Code"
slug: "maximum-drawdown-excel-vba-code"
date: "2013-03-06"
modified: "2023-11-06"
url: "https://alphaarchitect.com/maximum-drawdown-excel-vba-code/"
categories: ["Video Learning Series"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Maximum Drawdown Excel VBA Code

> TKA readers, I’ve been thinking a lot about drawdowns recently. In fact, I was thinking so hard about them I wrote a paper with Jack […]

TKA readers,

I’ve been thinking a lot about drawdowns recently. In fact, I was thinking so hard about them I wrote a paper with Jack Vogel on the subject!

<http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2226689>

> We propose the use of maximum drawdown, the maximum peak to trough loss across a time series of compounded returns, as a simple method to capture an element of risk unnoticed by linear factor models: tail risk. Unlike other tail-risk metrics, maximum drawdown is intuitive and easy-to-calculate. We look at maximum drawdowns to assess tail risks associated with market neutral strategies identified in the academic literature. Our evidence suggests that academic anomalies are not anomalous: all strategies endure large drawdowns at some point in the time series. Many of these losses would trigger margin calls and investor withdrawals, forcing an investor to liquidate.

**Here is the source code for the MaxDD function:**  
Function drawdown(port\_series As Range)  
Application.EnableCancelKey = xlDisabled  
‘ Find the biggest cumulative drawdown for a performance series  
‘ dates = dates typically alongside the returns  
‘ port\_series = port\_series returns in % \* 100 format  
Dim counter As Integer  
Dim cume As Double  
Dim max As Double  
counter = 1  
cume = 1  
max = 1  
For counter = 1 To port\_series.Count  
If port\_series(counter).Value <> “–” Then  
cume = (cume \* (port\_series(counter).Value + 1))  
End If  
If cume >= 1 Then  
cume = 1  
End If  
If cume < max Then  
max = cume  
End If  
Next counter  
‘If there never was a drawdown  
If max = 1 Then  
drawdown = “N/A”  
Else  
drawdown = (max – 1)  
End If  
End Function
