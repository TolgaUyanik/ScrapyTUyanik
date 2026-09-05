---
title: "Math Is Magic: A Weekend Brain Teaser"
slug: "math-is-magic-a-weekend-brain-teaser"
date: "2020-06-19"
modified: "2022-05-20"
url: "https://alphaarchitect.com/math-is-magic-a-weekend-brain-teaser/"
categories: ["Academic Research Insight", "Behavioral Finance"]
tags: []
best_of: false
source: "alphaarchitect.com"
---

# Math Is Magic: A Weekend Brain Teaser

> In the course of some research on costs and constraints on momentum strategies, I came across a couple of dueling talks by Wesley Gray and […]

In the course of some research on costs and constraints on momentum strategies, I came across a couple of dueling talks by Wesley Gray and Gary Antonacci, hosted by QuantCon NYC in 2017.  During his talk, Wes performed a number-magic trick to demonstrate how obscure and non-intuitive numerical analysis can be – to the point that it can seem like magic.

Of course, it’s more dramatic in person (feel free to check out the talk or try it yourself after reading this) [Video Link](https://www.youtube.com/watch?v=F2TTfZzigYk), but the trick works as follows:

1. You pick a number between 1 and 60
2. You tell me which of the following cards it appears on
3. I pause for a moment, look psychic, then tell you what your number is!

For example, if you tell me your number appears on cards 1 and 6, I can tell you that your number is 18.  The surprise of the trick is that it seems to make way too specific of a conclusion given how general the provided hint is.

![](https://alphaarchitect.com/wp-content/uploads/2020/01/image-42.png)

Internecine conflict between momentum strategists and mathematics-based magic tricks are each pretty interesting, but Wes further chummed the waters by claiming that this stumped someone with a math PhD for a week: an irresistible distraction.  As it turns out, the disconnect between how the trick works and how it’s operated is also pretty interesting.

First, being a skeptical sort of person, it made sense to make sure that the trick could be done (there was something suspicious about Wes saying “this guy isn’t a plant,” and a magician’s arsenal is full of audience-compliance tactics with colorful names like “instant stooge”).

In this case what “possible” really means is, does the audience member actually supply enough information to uniquely specify a number between 1 and 60 regardless of how that information may have been distorted by the phrasing of the trick.  At first glance, it seems not.  The person who picked the number might identify three, four, even six cards on which their secret number appears, but there are sixty possibilities for the number itself.

However, when you specify which cards your number is on what you’ve actually done, from an information-theoretical standpoint is to give six bits (as in the computer science, “binary digits,” bits) of data.  If the trick was done via a questionnaire, it would be easier to see this:

* “Was your number on the red card?” Yes/No
* “Was your number on the blue card?” Yes/No
* “Was your number on the pink card?” Yes/No, and so forth…

That is, even if you only list two cards to the mentalist performing the trick, you’ve implicitly answered four other questions in the negative.

How much information is in six Yes or No questions?  Six bits worth since there are two possible outcomes for each question.  Therefore, there are 2\*2\*2\*2\*2\*2 = 2^6 unique combinations of Nos and Yeses and therefore 2^6 possible unique answers.  Lo and behold, 2^6 = 64.  Enough information with some numbers to spare (notice the four empty spots on the cards).

Further, it turns out that this not only proves that the trick is possible but also explains also how it’s done.  Each of those questions is just a concealed way of asking something else, something useful and precise like:

* “What is the value of your number’s (base 2) fours place?” 1/0
* “What is the value of your number’s (base 2) eights place?” 1/0
* “What is the value of your number’s (base 2) twos place?” 1/0, and so forth….

Let’s create a smaller version of the trick, using the numbers 1 to 7, for a tidier example.  The table below lists the numbers 1 to 7 in both their decimal (usual, base 10) and binary (base 2) representations.  As a reminder, instead of the powers of ten, the ones, tens, hundreds… places used in base 10, binary numbers are expressed as a sum of the powers of two; the ones, twos, fours, eights… places.  Five is the sum of one 1, no 2, and one 4, therefore five is “101” in base 2.

![](https://alphaarchitect.com/wp-content/uploads/2022/04/image-43.jpg)

Source: Author

Now, create cards A, B, and C, such that each of the four numbers with a “1” in that letter’s column appears on that card.  For example, card B contains 2, 3, 6, and 7, and card C contains 1, 3, 5, and 7.

Stated another way, and this will be important in a moment, the C card is the ones place card, all the numbers on card C have a “+1” in their binary representation, aka the odd numbers.  Likewise, the B card is the twos place card, and the A card is the fours place card.

Say your audience member picks 5, they find it on the A and C card and tell you so.  What you now know is that this number that answers “Yes” to the two questions “Am I on the ones place card?” and “Am I on the fours place card?”  That number is, therefore, the sum of those binary places:  1 + 4 = 5.  Okay, but what if you get nervous on stage and forget which card is which?  No problem, the first number on each card tells you which place the card represents.   As much by definition as design, one is the first number on the ones card, two the first number on the twos card, et cetera.

So after all that, the final answer is: to guess the audience member’s number, you just add up the first numbers that appear on the cards they listed.  Voila, you are a mathemagician.

This trick has an unusual feature that, in the context of a talk on algorithmic (or algorithmic-adjacent) trading, is particularly interesting.  The curious nature of this trick is that, the magician/mentalist doesn’t need to know how the trick works in order to perform it – I would guess that the instructions simply say “add the first number on each card that the subject lists.  That is the answer.”  Do you get annoyed by the idea of a trick you can’t understand?  Are you sure it works?  Should you rest easy with black box, machine learning, ensembled, inscrutable algorithms making decisions on our behalf without offering any fundamental insight – also just a trick that works without our needing to understand how?
