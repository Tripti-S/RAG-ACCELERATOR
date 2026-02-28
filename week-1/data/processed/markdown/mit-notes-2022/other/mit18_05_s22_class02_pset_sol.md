# Mit18 05 S22 Class02 Pset Sol

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
Solution: : (2) B.
The event “exactly two heads” determines a unique subset, containing all outcomes that
have exactly two heads.
Concept question 2. (Describe the event.)
(Connecting words and set notation.)
Experiment: toss a coin 3 times.
Which of the following describes the event {𝑇 𝐻𝐻, 𝐻𝑇 𝐻, 𝐻𝐻𝑇 }?
(1) “exactly one head”
(2) “exactly one tail”
(3) “at most one tail”
(4) none of the above
Solution: (2) “exactly one tail”
Notice that the same event 𝐸 may be described in words in multiple ways, e.g. “exactly 2
heads” or “exactly 1 tail”.
Concept question 3. (Are they disjoint?)
(Connecting words and set notation.)
Experiment: toss a coin 3 times.
The events “exactly 2 heads” and “exactly 2 tails” are disjoint is.
(1) True (2) False
Solution: True: {𝑇𝐻𝐻,𝐻𝑇𝐻,𝐻𝐻𝑇}∩{𝑇𝑇𝐻,𝑇𝐻𝑇,𝐻𝑇𝑇} = ∅.
Concept question 4. (Does A imply B?)
(Connecting words and set notation)
Consider two events: 𝐴 and 𝐵.
Are the words “𝐴 implies 𝐵” equivalent to 𝐴 ⊆ 𝐵?
(1) True (2) False
1
18.05 class 2 problems, Spring 2022 2
Solution: True.
For example: If you tossed “exactly 2 heads”, then you know you tossed “at least two
heads”. This says exactly the same thing as
{𝑇𝐻𝐻,𝐻𝑇𝐻,𝐻𝐻𝑇} ⊂ {𝑇𝐻𝐻,𝐻𝑇𝐻,𝐻𝐻𝑇,𝐻𝐻𝐻}.
Board problems
Problem 1. Poker hands
Deck of 52 cards
• 13 ranks: 2, 3, … , 9, 10, J, Q, K, A
• 4 suits: ♡, ♠, ♢, ♣,
A poker hand consists of 5 cards
A one-pair hand consists of two cards having one rank and the remaining three cards having
three other ranks
Example: {2♡, 2♠, 5♡, 8♣, K♢}
(a) How many different 5 card hands have exactly one pair?
Hint: practice with how many 2 card hands have exactly one pair.
Hint for hint: use the rule of product.
(b) What is the probability of getting a one pair poker hand?
(a) Solution: We need a systematic algorithm that produces every possible hand exactly
once.
We can do this two ways: as combinations or as permutations. The keys are:
1. Be consistent.
2. Break the problem into a sequence of actions and use the rule of product.
Note, there are many ways to organize this. We will break it into very small steps in order
to make the process clear.
Combinations approach
Consider a hand as a set of 5 cards, i.e. order doesn’t matter.
Count the number of one-pair hands, by describing a procedure to make each one exactly
once.
Action 1. Choose the rank of the pair: 13 different ranks, choosing 1, so (13) ways to do
1
this.
Action 2. Choose 2 cards from this rank: 4 cards in a rank, choosing 2, so (4) ways to do
2
this.
Action 3. Choose the 3 cards of different ranks: 12 remaining ranks, so (12) ways to do this.
3
Action 4. Choose 1 card from each of these ranks: 4 cards in each rank so 43 ways to do
this.
18.05 class 2 problems, Spring 2022 3
Answer (Using the rule of product.)
13 4 12
( )⋅( )⋅ ( )⋅43 = 1098240
1 2 3
(b) To compute the probability we have to count all possible 5 card hands. We must stay
consistent and count combinations.
To make a 5 card hand we choose 5 cards out of 52, so there are
52
( ) = 2598960
5
possible hands. Since each hand is equally probable, the probability of a one-pair hand is
1098240/2598960 = 0.42257.
We redo the problem using a permutation approach.
This approach is a little trickier. We include it to show that there is usually more than one
way to count something.
(a) Count the number of one-pair hands, where we keep track of the order they are dealt.
Action 1. (This one is tricky.) Choose the positions in the hand that will hold the pair: 5
different positions, so (5) ways to do this.
2
Action 2. Put a card in the first position of the pair: 52 cards, so 52 ways to do this.
Action 3. Put a card in the second position of the pair: since this has to match the first
card, there are only 3 ways to do this.
Action 4. Put a card in the first open slot: this can’t match the pair so there are 48 ways
to do this.
Action 5. Put a card in the next open slot: this can’t match the pair or the previous card,
so there 44 ways to do this.
Action 6. Put a card in the last open slot: there are 40 ways to do this.
Answer: (Using the rule of product.)
5
( )⋅52⋅3⋅48⋅44⋅40 = 131788800
2
ways to deal a one-pair hand where we keep track of order.
(b) There are
𝑃 = 52⋅51⋅50⋅49⋅48 = 311875200
52 5
five card hands where order is important. Thus, the probability of a one-pair hand is
131788800/311875200 = 0.42257.
(Both approaches give the same answer.)
18.05 class 2 problems, Spring 2022 4
Problem 2. (Inclusion-exclusion)
Supposes a class has 50 students: 20 male (M), 25 brown-eyed (B)
For a randomly chosen student, what is the range of possible values for 𝑝 = 𝑃(𝑀 ∪𝐵)?
(a) 𝑝 ≤ 0.4
(b) 0.4 ≤ 𝑝 ≤ 0.5
(c) 0.4 ≤ 𝑝 ≤ 0.9
(d) 0.5 ≤ 𝑝 ≤ 0.9
(e) 0.5 ≤ 𝑝
Solution: (d) 0.5 ≤ 𝑝 ≤ 0.9
Explanation:
The easy way to answer this is that 𝐴 ∪ 𝐵 has a minumum of 25 members (when all males
are brown-eyed) and a maximum of 45 members (when no males have brown-eyes). So, the
probability ranges from 0.5 to 0.9
Thinking about it in terms of the inclusion-exclusion principle we have
𝑃(𝑀 ∪𝐵) = 𝑃(𝑀)+𝑃(𝐵)−𝑃(𝑀 ∩𝐵) = 0.9−𝑃(𝑀 ∩𝐵).
So the maximum possible value of 𝑃 (𝑀 ∪𝐵) happens if M and B are disjoint, so 𝑃 (𝑀 ∩𝐵) =
0. The minimum happens when 𝑀 ⊂ 𝐵, so 𝑃(𝑀 ∩𝐵) = 𝑃(𝑀) = 0.4.
Problem 3. D20
Consider the following experiment. Roll a 20-sided die (D20) 9 times. What is the probability
that all 9 rolls are distinct.
(In class we could actually run this experiment many times with a real die and see how
well the experimental data matched the theoretical probability. Later, we will learn how to
simulate this experiment in R.)
For this experiment, how would you define the sample space, probability function, and event?
Compute the probability that all rolls (in one trial of 9 rolls) are distinct.
20 ⋅ 19⋯13 ⋅ 12
Solution: = 0.119.
209
Reasoning
For the sample space 𝑆 we take all sequences of 9 numbers between 1 and 20. We find the
size of 𝑆 using the rule of product. There are 20 ways to choose the first number in the
sequence, followed by 20 ways to choose the second, etc. Thus, |𝑆| = 209. Of course, each
of these outcomes is equally likely.
In our case, 𝐴 is the event ‘all 9 numbers in the sequence are distinct’.
We can use the rule of product to compute |𝐴| as follows. There are 20 ways to choose the
first number, then 19 ways to choose the second, etc. down to 12 ways to choose the ninth
number. Thus, we have
|𝐴| = 20⋅19⋅18⋅17⋅16⋅15⋅14⋅13⋅12
That is |𝐴| = 𝑃 .
20 9
18.05 class 2 problems, Spring 2022 5
Putting this all together
20 ⋅ 19 ⋅ 18 ⋅ 17 ⋅ 16 ⋅ 15 ⋅ 14 ⋅ 13 ⋅ 12
𝑃 (𝐴) = ≈ 0.119
209
Problem 4. Jon’s Dice
Jon has three six-sided dice with unusual numbering.
A game consists of two players each choosing a die. They roll once and the highest number
wins.
Which die would you choose?
1. Make probabilitiy tables for the the blue and white dice.
2. Make a probability table for the product sample space of blue and white. That is, suppose
you roll both dice and record the result as an ordered pair, (blue value, white value). List
all the possible outcomes and their probabilities.
3. Use the table to compute the probability that blue beats white.
4. Pair up with another group. Have one group compare blue vs. orange and the other
compare orange vs. white. Based on the three comparisons, rank the dice from best to worst.
Solution: Here are the probability tables we can use to compare the dice.
Blue die White die Orange die
Outcomes 3 6 2 5 1 4
Probability 5/6 1/6 3/6 3/6 1/6 5/6
• The 2×2 tables show pairs of dice.
• Each entry is the probability of seeing the pair of numbers corresponding to that
entry.
• The color and letter gives the winning die for that pair of numbers. (We use black
instead of white when the white die wins.)
White Orange
2 5 1 4
Blue 3 15/36 (B) 15/36 (W) 5/36 (B) 25/36 (O)
6 3/36 (B) 3/36 (B) 1/36 (B) 5/36 (B)
Orange 1 3/36 (W) 3/36 (W)
4 15/36 (O) 15/36 (W)
18.05 class 2 problems, Spring 2022 6
The three comparisons are:
P(blue beats white) = 21/36 = 7/12
P(white beats orange) = 21/36 = 7/12
P(orange beats blue) = 25/36
Thus: blue is better than white is better than orange is better than blue.
There is no best die: the property of being ‘better than’ is not transitive.
Problem 5. Lucky Lucy
This is doable, but challenging problem. You should be able to compute 𝑃 (𝐴) and 𝑃 (𝐵).
It takes a bit of algebraic cleverness to decide if one is always bigger than the other.
Lucky Lucy has a coin that you’re quite sure is not fair.
• They will flip the coin twice
• Let 𝐴 be the event the tosses are the same, i.e. {𝐻𝐻, 𝑇𝑇}
• Let 𝐵 be the event the tosses are the different, i.e. {𝐻𝑇, 𝑇𝐻}
Let 𝑝 be the probability of heads. Compute and compare 𝑃 (𝐴) and 𝑃 (𝐵).
(If you don’t see the symbolic algebra try p = 0.2, p=0.5)
Solution: We’re given 𝑃(𝐻) = 𝑝. It’s probably easiest to introduce a new letter: let
𝑃(𝑇) = 𝑞. Of course, 𝑞 = 1−𝑝, or 𝑝+𝑞 = 1.
We have the following table for two tosses
Outcomes HH TT HT TH
Probability 𝑝2 𝑞2 𝑝𝑞 𝑞𝑝
So, 𝑃(𝐴) = 𝑝2 +𝑞2 and 𝑃 (𝐵) = 2𝑝𝑞.
Here’s the trick: Since the coin is unfair, 𝑝 ≠ 𝑞. Thus (𝑝−𝑞)2 > 0. Now expand this out:
(𝑝−𝑞)2 > 0 ⇒ 𝑝2−2𝑝𝑞+𝑞2 > 0 ⇒ 𝑝2+𝑞2 > 2𝑝𝑞.
The last inequality shows, as long as 𝑝 ≠ 𝑞, 𝑃 (𝐴) > 𝑃 (𝐵). That is, Lucy is more likely to
have both tosses the same.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
