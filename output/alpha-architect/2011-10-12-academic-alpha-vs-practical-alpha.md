---
title: "Academic Alpha vs. Practical Alpha"
slug: "academic-alpha-vs-practical-alpha"
date: "2011-10-12"
modified: "2022-06-03"
url: "https://alphaarchitect.com/academic-alpha-vs-practical-alpha/"
categories: ["Research Insights"]
tags: ["Academic Alpha", "Practical Alpha"]
best_of: false
source: "alphaarchitect.com"
---

# Academic Alpha vs. Practical Alpha

> WARNING: After reading this you will no longer believe money grows on trees. I love working on this blog–great outlet to discuss cool research, share […]

### WARNING: After reading this you will no longer believe money grows on trees.

I love working on this blog–great outlet to discuss cool research, share knowledge, meet interesting people, and monitor spam comments for 2 hours a day. Nonetheless, I fear a lot of people who read this blog walk away thinking: “Oh wow, this is so awesome. This idiotic professor spells out the secret ingredients on how to invest in amazing equity strategies that earn 20% alpha a year. I’m going to set up a quant hedge fund and be a billionaire in no time. Yipee!!!”

So the point of this post is to lower expectations and set our anchor a bit lower–this will limit overconfidence, increase diligence, and be better for me and all my fellow alpha-hunter friends out here in the blogosphere.

### The Setting

College campuses always put me in a good mood: everyone is beautiful (I would mention that the chicks are hot, but my wife sometimes reads this blog), campus is perfect, and nobody has a real job. What’s not to love?

Then you have the corporate world, which always puts me in a bad mood: everyone is pissed and stressed, there is no campus–only your cubicle–and everyone has a real job. Ugg.

### The Experience

Although I hate to admit it, academic research is sometimes like the university experience–wonderful for the senses, but not exactly in touch with the real world.

A recent trading experience shows us why the pages of the Journal of Finance aren’t the gospel (those of you out there who actually try this quant stuff on a regular basis can skip this entire blog post).

A few months back I was fascinated with the Campbell Hilscher and Szilagyi distress model–we even highlighted it on the blog at <https://alphaarchitect.com/2011/07/stop-using-altman-z-score/>. The punchline was that stocks identified by the distress model were in a serious hurt locker (which is definitely true) and the market was unable to fully recognize this (also true). Shorting the worst stocks could generate 15% plus in alpha each year. And of course, there was the token paragraph and data analysis regarding ‘implementation costs.’ We were further intrigued by this line of research when a friend–who happens to also be a Wharton finance professor–send me an interesting paper from a recent PhD student: <http://assets.wharton.upenn.edu/~parkjam/Distress.pdf>.  The bottom line from this excellent research piece is that you can juice up the distress alpha by simply focusing on the highest distressed firms that also happened to have issued equity in the recent past.

Well, being the proud free market capitalist that I am, we decided to try and implement this strategy to try and make a few bucks on the short side (if this market environment isn’t a good time to be long/short, then I don’t know when there is a good time!)

After spending the entire weekend building the distress model and figuring out how the heck to get the data from our data systems, I was proud to pass along the model portfolio trades (pre-liquidity screening process) to our trading and execution desk–currently my brother’s cabin in Eagle, CO (close to Vail). Yes, life sometimes isn’t fair, but I’m not complaining.

Upon receiving the model trades, Cliff responsed: “Wes, what the F&$# do you want me to do with these names? Stare at them or trade them? A quarter of the names you sent me have short rebates greater than 15%???”

[![](https://alphaarchitect.com/wp-content/uploads/2011/10/rebates-1024x625.png "rebates")](https://alphaarchitect.com/wp-content/uploads/2011/10/rebates.png)

The results are hypothetical results and are NOT an indicator of future results and do NOT represent returns that any investor actually attained. Indexes are unmanaged, do not reflect management or trading fees, and one cannot invest directly in an index. Additional information regarding the construction of these results is available upon request.

Here was my response after reading the output: “Oh. Sh\*&. I’ll get back to you on that one.”

If you want to dive further into the numbers, here is the entire spreadsheet [distress\_stats](https://alphaarchitect.com/wp-content/uploads/2011/10/distress_stats.xlsx) . Have fun. The realistic transaction costs to try and implement this short book are out of this world bonkers.

### Lessons (Re) Learned

Trust, but verify–soak in the numbers from the academic papers, but always redo the results to ensure they ‘smell’ right.

Be wary of the short side–always double or even triple the author’s estimate of  short side costs…so interpret the statement, the alpha is 10% a year after 5% costs as “the alpha is 0% after 15% transaction costs”.

Things that are too good to be true, often are.

For every 100 alpha ideas, only 1 or 2 actually work in practice.

Despite your utter contempt and dismay for the efficient market hypothesis, always remember that [Eugene Fama](http://en.wikipedia.org/wiki/Eugene_Fama) is ***always*** right.
