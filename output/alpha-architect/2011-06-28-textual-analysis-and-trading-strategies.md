---
title: "Textual Analysis and Trading Strategies"
slug: "textual-analysis-and-trading-strategies"
date: "2011-06-28"
modified: "2022-06-04"
url: "https://alphaarchitect.com/textual-analysis-and-trading-strategies/"
categories: ["Research Insights", "Behavioral Finance"]
tags: ["abnormal returns", "Textual Analysis", "Dictionaries"]
best_of: false
source: "alphaarchitect.com"
---

# Textual Analysis and Trading Strategies

> When is a Liability not a Liability? Textual Analysis, Dictionaries, and 10-Ks. Tim Loughran and Bill McDonald A published version of the paper can be […]

### When is a Liability not a Liability? Textual Analysis, Dictionaries, and 10-Ks.

* Tim Loughran and Bill McDonald
* A published version of the paper  can be found [here](http://www.afajof.org/afa/forthcoming/6989p.pdf).
* The authors keeps a version of the paper [here](http://www.nd.edu/~tloughra/Liability.pdf).
* The authors keep a financial dictionary database [here](http://www.nd.edu/~mcdonald/Word_Lists.html).

### **Abstract:**

> Previous research uses negative word counts to measure the tone of a text. We show that word lists developed for other disciplines misclassify common words in financial text. In a large sample of 10-Ks during 1994-2008, almost three-fourths of the word count identified as negative by the commonly used Harvard Dictionary represents words that typically do not have negative meaning in a financial context. Words like tax, board, foreign, vice, and liability, simply describe company operations. Two potential solutions are explored. First, we develop an alternative negative word list that better reflects the tone of financial text. Second, we show that using a common term weighting scheme reduces the noise introduced by misclassifications. Without term weighting, our list generally outperforms the Harvard list; with weighting the performance appears comparable. However, we also find evidence that some of the power of the Harvard list could be attributable to misclassified words that proxy for other effects. Five other word classifications (positive, uncertainty, litigious, strong modal, and weak modal) are also considered. We link the word lists to 10-K filing returns, trading volume, subsequent return volatility, fraud, material weakness, and unexpected earnings.

### **Data Sources:**

The authors examine 10-Ks between 1994 and 2008. In total they have 50,115 firm-year data points. They also create a financial dictionary that better classifies words as ‘negative’ or ‘positive’ in a financial context. The dictionary can be found [here](http://www.nd.edu/~mcdonald/Word_Lists.html). Their dictionary is compared to the ‘standard’ word classification dictionary called the Harvard Psychosociological Dictionary which can be found [here](http://www.nd.edu/~mcdonald/Word_Lists.html). Pricing data comes from CRSP.

### **Discussion:**

Cutting edge research is investigating how sentiment/tone/qualitative information can affect financial markets. A favorite tool of researchers to assess these factors is textual analysis. Put simply, textual analysis involves pouring a bunch of text into a computer program outfitted with an algorithm that can determine if the text is “negative”, “positive”, or something in between. Once the researcher has classified sentiment, they can examine how this qualitative information affects various factors: Does poor sentiment predict poor returns? Do market participants pay attention to the tone of conference calls? Do managers have predictable patterns when they are releasing good/bad news? …and so forth. Lot’s of interesting work!

One of the more popular studies that really blazed a trail for textual analysis comes from Paul Tetlock, at Columbia University. His paper, [“Giving Content to Investor Sentiment,”](http://www0.gsb.columbia.edu/faculty/ptetlock/papers/Tetlock_JF_07_Giving_Content_to_Investor_Sentiment.pdf) looks at the tone of the “Abreast of the Market” column in the Wall Street Journal. Among other interesting tidbits, Paul finds that high pessimism (as measured via textual analysis algorithms) are followed by lower returns for the next trading day.

Wow, so this sounds really cool, right? Professors are somehow using computers to identify how we feel and how to predict stock market returns–Judgement Day must be approaching.

Well, like everything in life, if it sounds to good to be true, it probably is. In this paper, the authors question the underlying methodologies employed by previous researchers who use textual analysis as a research tool.

The authors find the following key results:

* Traditional textual analysis dictionaries misclassify words in a financial construct. In fact, almost 74% of the negative words in the traditional classification schemes consider words negative, but these words are not negative in a financial context.
* Using proper financial word classification, the authors find that more negative 10-Ks result in lower returns, whereas using traditional word classification schemes, the results between 10-K textual tone and returns are non-existent.
* The authors expand the word classification categories and create additional word lists. These word lists are helpful in predicting a variety of financial phenomenon. The lists can be found on their website.

If none of that made sense, perhaps this little made-up example will put a little more “meat on the bone.”

Consider the following 10-K release: “Last quarter we cured CANCER. In addition, because the COST of capital decreased for our firm, we were able to increase our CAPITAL base. We also hired a new VICE president named Jack Welch. Finally, because we are so special, our TAX LIABILITY fell to zero.”  
Any analyst reading the above fictional paragraph from a 10-K would fall over themselves trying to buy stock in the company that made this announcement. And yet, traditional textual analysis would consider this paragraph extremely negative in tone. However, using the text algorithms developed by the authors, this paragraph would not be considered “negative.”

While the example above is silly, the point is clear: proper word classification is paramount if one is to engage in textual analysis.

Here is another example to prove the point (taken directly from the paper).

[![](https://alphaarchitect.com/wp-content/uploads/2011/06/texts.png "texts")](https://alphaarchitect.com/wp-content/uploads/2011/06/texts.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

The figure shows how well textual analysis techniques predict filing period excess returns. Theoretically, a good textual analysis tool should be able to determine when a 10-K is negative, and a negative 10-K, on average, should also be associated with negative returns on the filing date. What the authors find is that the traditional textual analysis tool (H4N-Inf in the graph) can barely decipher when a 10-K is actually negative or positive, whereas their financially-focused textual analysis (Fin-Neg) tools has solid predictive ability.

This is all fine and dandy; the professors found out that proper textual analysis requires a proper analysis of the text actually being analyzed…Duh.

*On to the more important question:* Can we make any money using this fancy textual analysis created by the professors?

The authors don’t really go into great depth exploring this question (although I’m sure many hedge funds hit them up for consulting projects to investigate further.) One study the authors do perform is analyzing whether or not the amount of negativity in the 10-K predicts returns over the following year. What the authors find that there is no alpha associated with a strategy that goes long “low negativity” and short “high negativity”.

No alpha? ugg.

Well, the authors do highlight that their measure of negativity can predict earnings surprises for quarterly results reported within three months of the 10-K filing. Surprisingly, more negativity actually predicts positive earnings surprises! The hypothesis behind this finding is that managers attempt to lower expectations via language and analysts are unable to pick up on this queue. Perhaps a smart trader could isolate this predictability and figure out how to profitably trade on the idea. Unfortunately, the authors don’t appear to explore this further (maybe because it works too well?).

### **Investment Strategy:**

Nothing explicitly stated. 

### **Commentary:**

There really isn’t a standardized trading strategy associated with this paper; however, I highlighted this piece of work for three reasons:

1. To get the creative juices flowing.
2. To ensure readers recognize that “garbage in=garbage out” is very true in the context of textual analysis and the trading strategies proposed.
3. This paper is really cool.

I personally think there are some profitable avenues to explore in this area of trading, and it just so happens that a couple of professors have done a lot of the heavy lifting…

AND they offer their data up for free–holy cow.

Best of luck and if you have any good trading ideas or thoughts related to textual analysis please send them along and share them with the readership.
