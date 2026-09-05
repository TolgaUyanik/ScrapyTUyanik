---
title: "The Amazing Unbeatable Poker Algorithm"
slug: "the-amazing-unbeatable-poker-algorithm"
date: "2015-01-15"
modified: "2022-05-04"
url: "https://alphaarchitect.com/the-amazing-unbeatable-poker-algorithm/"
categories: ["Uncategorized"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# The Amazing Unbeatable Poker Algorithm

> Everyone remembers when Deep Blue first defeated Gary Kasparov, but recently computers have begun quietly edging past humans in another human game: poker. The journal […]

Everyone remembers when Deep Blue first defeated Gary Kasparov, but recently computers have begun quietly edging past humans in another human game: poker.

The journal Science recently published an [article](http://www.sciencemag.org/content/347/6218/145) entitled, “Heads-up limit hold’em poker is solved,” which describes the recent progress made by computers in poker. Declaring this particular version of Texas hold’em, “essentially weakly solved,” the article describes how scientists have developed an algorithm that is virtually unbeatable (i.e., a lifetime of human play would win less than 5% of the time).

This is a big step, as it arguably represents the first time that a mainstream human game with imperfect information has been solved. To understand why this is significant, let’s review games of perfect and imperfect information.

In “perfect-information” games, players know everything that has already occurred in the game. Checkers is an example, and with 5\*1020 possible moves, it exhibits a high degree of “state-space” complexity (although it was solved in 2007). Computational algorithms have dominated humans for many years in many such games, where the complexity can be resolved with brute force computing power that works through every possible line of play. But as we all know, in some games, as with many real world situations, there is not always perfect information.

As John von Neumann, the father of game theory, observed:

> Real life is not like that. Real life consists of bluffing, of little tactics of deception, of asking yourself what is the other man going to think I mean to do. And that is what games are about in my theory.

Enter poker, which is a game of imperfect-information. In poker, players don’t know have complete information of the game as it is being played. For instance, a player doesn’t know what cards the opponent holds, or whether the opponent likes to bluff. These games are much harder for computers, due to their higher “decision complexity.” Players must consider statistics, assess changing risks on an ongoing basis, and deal with the idiosyncrasies of individual players, who have differing information, and differing styles of play, and who may be trying to mislead each other. There are numerous aspects of the game to consider that go beyond what a raw look-ahead tree search can consider.

Although heads-up limit Texas hold’em, with 3\*1014 possible states, has a lower state-space complexity than checkers (which, again, has 5\*1020), it has a higher decision complexity, because of the many varieties of imperfect information inherent in the game. By comparison, Chess has a state-space complexity of 1046.

The scientists addressed Poker’s decision complexity using a technique called, “counterfactual regret minimization.”

Under this approach, the algorithm plays thousands of simulated hands, and at the conclusion of each hand it assigns a “regret” value to it, based on a comparison to how well things could have gone. In future iterations, the algorithm chooses from among strategies that have minimized regret in the past. After many iterations, the dominant strategy emerges. Thus the algorithm eventually adjusts and refines its strategy to the point where the strategy becomes unexploitable. Note in the graph below (from the Science article) how the exploitability of the solution decreases with additional iterations as the learning algorithm converges on the optimal strategy.  
[![12](https://alphaarchitect.com/wp-content/uploads/2015/01/12.png)](https://alphaarchitect.com/wp-content/uploads/2015/01/12.png)  
Some interesting observations fell out of this research. In general, the algorithm tended to play a wider variety of hands than did humans. It almost never “capped” (made the final allowable raise) in the first round as the dealer, whereas humans do so much more frequently. It was also more likely to re-raise when holding lower pairs (<5s) than human players.

This suggests that even expert human judgment may be simply wrong about certain areas of poker.  
As the father of artificial intelligence Alan Turing noted:

> A computer would deserve to be called intelligent if it could deceive a human into believing it was human.

Perhaps the computer has now passed the so-called Turing Test with respect to heads up limit hold’em poker, as there is no way to distinguish its play from human play. Although you might be able to do so by observing that its play is better than human play.
