# Mit18 05 S22 Class02 Pset

---

Class 2 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. (What’s the event?)
(Connecting words and set notation.)
Experiment: toss a coin 3 times.
Which of following equals the event “exactly two heads”?
𝐴 = {𝑇𝐻𝐻,𝐻𝑇𝐻,𝐻𝐻𝑇,𝐻𝐻𝐻}
𝐵 = {𝑇𝐻𝐻,𝐻𝑇𝐻,𝐻𝐻𝑇}
𝐶 = {𝐻𝑇𝐻,𝑇𝐻𝐻}
(1) A (2) B (3) C (4) B or C
Concept question 2. (Describe the event.)
(Connecting words and set notation.)
Experiment: toss a coin 3 times.
Which of the following describes the event {𝑇 𝐻𝐻, 𝐻𝑇 𝐻, 𝐻𝐻𝑇 }?
(1) “exactly one head”
(2) “exactly one tail”
(3) “at most one tail”
(4) none of the above
Concept question 3. (Are they disjoint?)
(Connecting words and set notation.)
Experiment: toss a coin 3 times.
The events “exactly 2 heads” and “exactly 2 tails” are disjoint is.
(1) True (2) False
Concept question 4. (Does A imply B?)
(Connecting words and set notation)
Consider two events: 𝐴 and 𝐵.
Are the words “𝐴 implies 𝐵” equivalent to 𝐴 ⊆ 𝐵?
(1) True (2) False
Board problems
Problem 1. Poker hands
Deck of 52 cards
• 13 ranks: 2, 3, … , 9, 10, J, Q, K, A
• 4 suits: ♡, ♠, ♢, ♣,
1
18.05 class 2 problems, Spring 2022 2
A poker hand consists of 5 cards
A one-pair hand consists of two cards having one rank and the remaining three cards having
three other ranks
Example: {2♡, 2♠, 5♡, 8♣, K♢}
(a) How many different 5 card hands have exactly one pair?
Hint: practice with how many 2 card hands have exactly one pair.
Hint for hint: use the rule of product.
(b) What is the probability of getting a one pair poker hand?
Problem 2. (Inclusion-exclusion)
Supposes a class has 50 students: 20 male (M), 25 brown-eyed (B)
For a randomly chosen student, what is the range of possible values for 𝑝 = 𝑃(𝑀 ∪𝐵)?
(a) 𝑝 ≤ 0.4
(b) 0.4 ≤ 𝑝 ≤ 0.5
(c) 0.4 ≤ 𝑝 ≤ 0.9
(d) 0.5 ≤ 𝑝 ≤ 0.9
(e) 0.5 ≤ 𝑝
Problem 3. D20
Consider the following experiment. Roll a 20-sided die (D20) 9 times. What is the proba-
bility that all 9 rolls are distinct.
(In class we could actually run this experiment many times with a real die and see how
well the experimental data matched the theoretical probability. Later, we will learn how to
simulate this experiment in R.)
For this experiment, how would you define the sample space, probability function, and
event?
Compute the probability that all rolls (in one trial of 9 rolls) are distinct.
Problem 4. Jon’s Dice
Jon has three six-sided dice with unusual numbering.
A game consists of two players each choosing a die. They roll once and the highest number
wins.
Which die would you choose?
18.05 class 2 problems, Spring 2022 3
1. Make probabilitiy tables for the the blue and white dice.
2. Make a probability table for the product sample space of blue and white. That is, suppose
you roll both dice and record the result as an ordered pair, (blue value, white value). List
all the possible outcomes and their probabilities.
3. Use the table to compute the probability that blue beats white.
4. Pair up with another group. Have one group compare blue vs. orange and the other
compare orange vs. white. Based on the three comparisons, rank the dice from best to
worst.
Problem 5. Lucky Lucy
This is doable, but challenging problem. You should be able to compute 𝑃 (𝐴) and 𝑃 (𝐵). It
takes a bit of algebraic cleverness to decide if one is always bigger than the other.
Lucky Lucy has a coin that you’re quite sure is not fair.
• They will flip the coin twice
• Let 𝐴 be the event the tosses are the same, i.e. {𝐻𝐻, 𝑇𝑇}
• Let 𝐵 be the event the tosses are the different, i.e. {𝐻𝑇, 𝑇𝐻}
Let 𝑝 be the probability of heads. Compute and compare 𝑃 (𝐴) and 𝑃 (𝐵).
(If you don’t see the symbolic algebra try p = 0.2, p=0.5)
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
