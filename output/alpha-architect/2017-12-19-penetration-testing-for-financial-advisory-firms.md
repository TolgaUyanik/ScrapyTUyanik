---
title: "Cybersecurity Series: Penetration Testing for Financial Advisors"
slug: "penetration-testing-for-financial-advisory-firms"
date: "2017-12-19"
modified: "2022-05-13"
url: "https://alphaarchitect.com/penetration-testing-for-financial-advisory-firms/"
categories: ["Cyber Security Programs", "Investment Advisor Education"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Cybersecurity Series: Penetration Testing for Financial Advisors

> Cybersecurity is much like boxing, combat, or discussing finances with your spouse: You can train all you want, but you never really know your true […]

Cybersecurity is much like boxing, [combat](https://alphaarchitect.com/2015/05/25/from-the-frontlines-to-finance-how-the-marines-shaped-our-investment-philosophy/), or discussing finances with your spouse: You can train all you want, but you never really know your true grit until you face your adversary face to face.

![](https://alphaarchitect.com/wp-content/uploads/2017/11/boxing.jpg)

Can your cybersecurity program take a punch to the face?

All of the compliance manuals, processes, and employee training are meaningless if they can not protect client data in the face of an attack.

But how do Advisors know if their cybersecurity program is robust? What should clients themselves be asking to ensure their data is safeguarded? In this post, we will outline how financial advisors can (and should) test their cybersecurity program in real time with penetration testing. We will outline what a penetration test is, why it matters, how to select a pen testing firm, and how the testing process works. Please share your feedback via the comments section.

Note: Here is a preview of what happens when individuals at Alpha Architect break cybersecurity rules!

## Punching Yourself in the Face: An Introduction to Penetration Testing

At the most basic level, penetration testing (“pen testing”) is quite simple. You pay someone to try and break into your network and compromise your data. This is commonly referred to as “ethical hacking” or “white hat” hacking. Once you have developed a robust cybersecurity program, implemented your processes, and established your defenses, pen testing firms will (with your permission) test your defenses and see if an advisor’s system is as robust as they think it is.

![](https://alphaarchitect.com/wp-content/uploads/2017/11/battering-ram-1.jpg)

The first known penetration test of a financial advisor, circa 1956

Within the wonderful world of penetration testing there are three types of testing:

* External penetration test
* Internal penetration test
* Social engineering penetration test

The concept of external versus internal penetration testing is relatively simple (see Figure A below). In an external penetration test, you provide the pen testing firm with your externally facing IP address (e.g., the publicly available IP address to locate your router or modem). Armed with this information, an external tester will try and “crack” your network firewall and get into your network. It’s somewhat similar to telling an “ethical” burglar where your home address is and seeing if they can get inside…

![](https://alphaarchitect.com/wp-content/uploads/2017/11/External-Pen-Test.png)

Figure A: An external pen test – focus on the router and external firewall Source: National Institute for Bad Clipart Because We are Too Cheap to Buy Diagrams

Your router is the most critical piece of your external network and can present [serious cyber threats to your business](https://www.wsj.com/articles/rarely-patched-software-bugs-in-home-routers-cripple-security-1453136285). This humble little box is where the chaos of the internet meets your advisory practice’s personal files, data, and trading systems. In the past, internet service providers would send routers to new clients with virtually all access points enabled. The factory default setting would be set to “please come in” and they were a goldmine for any hacker. Imagine having a front door installed in your home, but all of the locks have been removed…not good.

Thankfully, router manufacturers and internet providers are getting smarter and setting more stringent security settings *by default* on their machines. Nevertheless, there are a host of cyber risks associated with a router. The external penetration test will attack these settings and determine if any open ports or default settings enable an intruder to get into your network.

An internal penetration test, on the other hand, assumes a hacker has breached your router somehow and can access your machines. This test is an assessment of your internal defenses against hacking (malware, unencrypted machines, etc.). See Figure B for a high tech visualization of an internal penetration test. For a truly robust assessment, it is best to assume your first line of defense is breached or compromised and deploy an internal test to determine the vulnerability of your network.

![](https://alphaarchitect.com/wp-content/uploads/2017/11/Internal-Pen-Test.png)

Figure B: An internal pen test – focus on internal networks and data sourcesSource: Ibid

The third, and most important, aspect of penetration testing is called “social engineering.” This type of test seeks to assess the most vulnerable aspect of any advisor’s cyber program….the human. Social engineering testing is very simple: someone impersonates another employee, a broker-dealer, a client, etc. and tries to get access or install malware directly onto an employee’s machine. Unlike internal and external pen testing, social engineering focuses on the human element of cybersecurity, which I consistently find to be the weakest link. Social engineering can range from very crude attacks (remember those Nigerian prince email scams) to highly sophisticated, well-funded impersonations deployed by trained professionals. Robust, ongoing cyber training is the best defense for your advisory employees from these type of attacks.

![](https://alphaarchitect.com/wp-content/uploads/2017/11/wolf-in-sheeps-clothing.jpg)

Social engineering: I’ll give you a hint…it’s not a sheep

I recommend Advisors take a balanced approach to social engineering. It is pointless to retain a varsity level social engineering firm if employees are not well versed in what to watch out for and what the consequences are (we will get to training in a later post). In short, make sure your training is rigorous, robust, and understood first (and then test). You can also run several low-level social engineering tests internally. Example: create a Gmail account that looks similar to your existing personal account (e.g., JohnTDoe1@gmail) and send a request to your team.

> Hey, I can’t get into the sharedrive, can someone send me the account number for our master account?

Any responses? You can apply the same logic to hardware. Let’s take thumb drives for example. Want to test employees to see if they follow a “no unauthorized thumb drive policy?” Leave a few blank thumb drives around the office and see where they go. For bonus points, try putting a funny image or picture on one and see if you get any takers. If your teammates stumble into your office with: “That holiday party picture on this thumb drive is hilarious…where did you get that?” you have found the weakest link.

Of course, the ideal solution is a professional social engineering effort, but I recommend training your team on the basics first to avoid a high dollar service before employees can rise to the challenge.

The perfect penetration test is the trifecta of all three methods above. Testing the perimeter, internal safeguards, and social engineering…combined. This approach will provide a holistic, comprehensive overview of your [defense in depth](https://www.us-cert.gov/bsi/articles/knowledge/principles/defense-in-depth).

## Why Advisors and Third-Party Service Providers Need to Care

The SEC expects advisors to run penetration tests (and they have been since 2014). Check out the Appendix, page 2 of the [OCIE’s 2015 Cyber Examination Initiative](https://www.sec.gov/ocie/announcement/ocie-2015-cybersecurity-examination-initiative.pdf). 2015 too recent for you? Let’s go back to 2014 and the [OCIE Cybersecurity Initiative White Paper](https://www.sec.gov/ocie/announcement/Cybersecurity-Risk-Alert--Appendix---4.15.14.pdf). You can also check out my prior post on [establishing a robust cybersecurity program](https://alphaarchitect.com/2017/11/07/how-to-build-an-investment-advisor-cybersecurity-program/) and review the resources therein. All of the recommended templates and source literature mention penetration testing in some manner.

Here is a direct quote from the SEC regarding sample questions that could be found on your next exam:

> For each of the following practices employed by the Firm to assist in detecting unauthorized activity on its networks and devices, please briefly explain how [your Firm conducts]…**penetration tests and vulnerability scans**…please identify the month and year of the most recent penetration test and recent vulnerability scan, whether they were conducted by Firm employees or third parties, and describe any findings from the most recent test and / or assessment that were deemed to be potentially moderate or high risk but have not yet been addressed.
>
> OCIE Cybersecurity Initiative, National Exam Program Risk Alert, Volume IV, Issue 2 (emphasis added).

Despite crystal clear guidance from the referees (SEC and FINRA), we routinely come across advisors that have yet to understand what pen testing is, let alone deploy a pen testing firm to assess their defenses. Ignore pen testing requirements at your peril. This also applies to any third party service providers you may be relying upon to sstore/process client data.

![](https://alphaarchitect.com/wp-content/uploads/2017/11/see-no-evil.jpg)

A typical Advisor ecosystem response to Pen Testing

Cyber continues to take an [increasingly prominent role with regulators](http://www.thinkadvisor.com/2017/11/08/sec-shows-off-cybersecurity-muscle-following-edgar?page=2&slreturn=1510245460). I would argue that this focus will eventually eclipse more traditional compliance requirements in terms of scrutiny going forward. Think about it. Most advisors use a single platform (e.g., Schwab or Interactive Brokers) for their trades which somewhat neutralizes the ability to steer deal flow to competing brokers (best execution). Similarly, technology is streamlining billing, trade authorizations, KYC documentation, and records / retention requirements. Old risks are fading, while new cyber risks are rising to take their place.

Granted, compliance requirements will always be with us. One only needs to refer to Messrs. Belfort and Madoff to recall the importance of compliance 101; however, the risks presented by cyber attacks, in my view, will continue to outpace their “traditional” compliance counterparts. In short – don’t gloss over cyber.

## How to retain a Pen Testing Firm

Penetration testing costs can vary wildly. Are you doing an internal test? External? Social? All three? How many red cell hackers are you deploying? When advisors ask me how much penetration testing costs, I ask them how much a car costs, or a house costs….it depends. That said, if you are paying $25 for heart surgery…something’s up. At a minimum, I have seen Pen tests go for as little as $500 and beyond $20k depending on scope.

Do your homework and follow these tips below:

* Get multiple bids and ask for references
* Ask for a sanitized sample of the final report (is it easy to read? follow? clear action plans?)
* Confirm the national footprint of the firm (I am biased, but I remain a fan of US / Canadian firms for broader cybersec reasons)
* Seek out US gov’t certified firms / firms that have to meet Federal standards
* Confirm the test will be “two-staged”. The initial stage will identify weaknesses and then the second stage will be a “remediation” test to be completed after the Adviser attempts to correct issues identified in the first stage.
* Seek firms that have some experience in asset management / advisory and can tailor their tests accordingly
* Confirm the “Rules of Engagement” process (how they are set, who goes where, who gets notified, etc.).

While not an exhaustive list, this should give you a sense for what to look for as you begin your search.

## How the pen testing process works

A decent penetration testing firm will provide the following:

* A clear scope of work
* A document that outlines how the pen test will be done
* A conference call that will confirm and authorize all “rules of engagement”
* Clear escalation procedures if a breach is identified (e.g., “if we can break into your computer, we will stop, notify you, then XYZ”)
* A remediation test that follows the test itself (see above – basically, give you a chance to fix the vulnerability, then test again to make sure it’s fixed)
* A clear, well written work product that references the [NIST framework](https://www.nist.gov/cyberframework) for regulatory documentation

Typically, a kickoff call will be scheduled to gain an understanding of how your network is organized, what you are looking to accomplish, and highlight any initial items to be addressed prior to commencing the test. For example, any third party service provider that houses client data will need to provide permission for testing of their perimeter (and thus, you may need additional documentation following the call).

Thereafter, the Advisor will provide any follow up items identified in the kickoff. Typically 2-3 days prior to the test, a final “ROE” (Rules of Engagement) call will be scheduled to go through what will actually be tested, how, and where the Advisor will be involved. It is critical that you establish clear “go/no-go” criteria for pen testers to follow.

For example, my personal network at home was part of our Pen Test since we often work remotely. I did not want the pen test team to discover my treasure trove of Charles in Charge episodes stored on our family’s personal drive. During the kickoff call, I outlined for the pen testers what areas were on and off limits. Thereafter, the team clearly delineated what they would do if they found a vulnerability, and what permissions I would have to grant them to enable them to move forward. Professional files were fair game, Charles in Charge episodes were not.

![](https://alphaarchitect.com/wp-content/uploads/2017/11/kickoff-calls.jpg)

A typical kickoff call meeting with a penetration testing firm

Note: Pen testers will not take all of your files and compromise them. That said, you should have an encryption plan in place for all of your machines to render your data secure in the face of a breach (more on that later).

On test day, you will receive a “warning email” to let you know the test will be live within a certain time window. Thereafter, a “test complete” notice is typically provided.

A few days later, you will likely have a debrief call with the white hackers themselves. You should receive a nice, clean, regulator-ready report that outlines everything that was done, not done, and any deficiencies identified. During your retest phase (if applicable) you should have an opportunity to fix anything that is “broken” and do another, final debrief.

## Conclusion: Build out your program and start pen testing

Now we understand that pen testing is important, is required by regulators, is relatively straightforward, and most importantly, is tremendously helpful in maintaining a robust cybersecurity program. The keys to success are ensuring clear expectations are outlined up front, performing robust due diligence on reputable pen testing firms, and having a clear timeline for the test itself. Good luck!

Follow. The. Program. Cybersecurity is a big deal. Take it seriously or Chief Compliance Officer, Patrick Cleary, will come after you!
