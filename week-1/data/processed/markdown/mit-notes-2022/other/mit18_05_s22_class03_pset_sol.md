# Mit18 05 S22 Class03 Pset Sol

---

Class 3 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1.
Toss a coin 4 times. Let 𝐴 = ‘at least three heads’ and 𝐵 = ‘first toss is tails’.
1. What is 𝑃 (𝐴|𝐵)?
(a) 1/16 (b) 1/8 (c) 1/4 (d) 1/5
2. What is 𝑃 (𝐵|𝐴)?
(a) 1/16 (b) 1/8 (c) 1/4 (d) 1/5
Solution: 1. (b) 1/8. 2. (d) 1/5.
Counting we find |𝐴| = 5, |𝐵| = 8 and |𝐴 ∩ 𝐵| = 1. Since all sequences are equally likely
𝑃(𝐴 ∩ 𝐵) |𝐴 ∩ 𝐵| |𝐵 ∩ 𝐴|
𝑃 (𝐴|𝐵) = = = 1/8. 𝑃 (𝐵|𝐴) = = 1/5.
𝑃 (𝐵) |𝐵| |𝐴|
Concept question 2. Trees 1.
𝑥
𝐴 𝑦 𝐴
1 2
𝐵 𝑧 𝐵 𝐵 𝐵
1 2 1 2
𝐶 𝐶 𝐶 𝐶 𝐶 𝐶 𝐶 𝐶
1 2 1 2 1 2 1 2
1. The probability 𝑥 represents
(a) 𝑃 (𝐴 ) (b) 𝑃 (𝐴 |𝐵 ) (c) 𝑃 (𝐵 |𝐴 ) (d) 𝑃 (𝐶 |𝐵 ∩ 𝐴 ).
1 1 2 2 1 1 2 1
Solution: (a) 𝑃 (𝐴 ).
1
Concept question 3. Trees 2.
2. The probability 𝑦 represents
(a) 𝑃 (𝐵 ) (b) 𝑃 (𝐴 |𝐵 ) (c) 𝑃 (𝐵 |𝐴 ) (d) 𝑃 (𝐶 |𝐵 ∩ 𝐴 ).
2 1 2 2 1 1 2 1
Solution: (c) 𝑃 (𝐵 |𝐴 ).
2 1
Concept question 4. Trees 3.
3. The probability 𝑧 represents
(a) 𝑃 (𝐶 ) (b) 𝑃 (𝐵 |𝐶 ) (c) 𝑃 (𝐶 |𝐵 ) (d) 𝑃 (𝐶 |𝐵 ∩ 𝐴 ).
1 2 1 1 2 1 2 1
Solution: (d) 𝑃 (𝐶 |𝐵 ∩ 𝐴 ).
1 2 1
Concept question 5. Trees 4.
4. The circled node represents the event
(a) 𝐶 (b) 𝐵 ∩ 𝐶 (c) 𝐴 ∩ 𝐵 ∩ 𝐶 (d) 𝐶 |𝐵 ∩ 𝐴 .
1 2 1 1 2 1 1 2 1
Solution: (c) 𝐴 ∩ 𝐵 ∩ 𝐶 .
1 2 1
1
18.05 class 3 problems, Spring 2022 2
In class examples
Class example 1.
• Organize computations
• Compute total probability
• Compute Bayes’ formula
Example. Game: 5 orange and 2 blue balls in an urn. A random ball is selected and
replaced by a ball of the other color; then a second ball is drawn.
1. What is the probability the second ball is orange?
2. What is the probability the first ball was orange given the second ball was orange?
5/7 2/7
First draw 𝑂 𝐵
1 1
4/7 3/7 6/7 1/7
Second draw
𝑂 𝐵 𝑂 𝐵
2 2 2 2
Solution: 1. Let 𝑂 be the event the first ball is orange. Likewise for 𝑂 , 𝐵 , 𝐵 . The
1 2 1 2
5 4 2 6 32
law of total probability gives 𝑃(𝑂 ) = ⋅ + ⋅ =
2 7 7 7 7 49
𝑃 (𝑂 ∩ 𝑂 ) 20/49 20
2. Bayes’ rule gives 𝑃 (𝑂 |𝑂 ) = 1 2 = =
1 2 𝑃 (𝑂 ) 32/49 32
2
Board questions
Problem 1. Monty Hall
• One door hides a car, two hide goats.
• The contestant chooses any door.
• Monty always opens a different door with a goat. (He can do this because he knows
where the car is.)
• The contestant is then allowed to switch doors if they want.
What is the best strategy for winning a car?
(a) Switch (b) Don’t switch (c) It doesn’t matter
18.05 class 3 problems, Spring 2022 3
Organize the Monty Hall problem into a tree and compute the probability of winning if you
always switch.
Hint first break the game into a sequence of actions.
Solution: Let 𝑃 be the probability function when the contestant uses the switching
switch
strategy. Let 𝐶 represent a car and 𝐺 a goat.
We will see that 𝑃 (𝐶) = 2/3
switch
One way to show this is with a tree representing the switching strategy: First the contestant
chooses a door, (then Monty shows a goat), then the contestant switches doors.
Probability Switching Wins the Car
1/3 2/3
Chooses
𝐶 𝐺
0 1 1 1 1 0
Switches
𝐶 𝐺 𝐶 𝐺
2 2 2 2
The (total) probability of 𝐶 is 𝑃 (𝐶) = 1 ⋅0+ 2 ⋅1 = 2 .
switch 3 3 3
Writing this in symbols using the law of total probability: Here 𝐺 represents a goat is
1
behind the original door chosen and 𝐺 means a goat is behind the door that is switched
2
to. Likewise 𝐶 and 𝐶 .
1 2
1 2 2
𝑃 (𝐶 ) = 𝑃 (𝐶 |𝐶 )𝑃 (𝐶 ) + 𝑃 (𝐶 |𝐺 )𝑃(𝐺 ) = 0⋅ +1 ⋅ = .
switch 2 switch 2 1 1 switch 2 1 1 3 3 3
Problem 2. Independence
Roll two dice and consider the following events
• 𝐴 = ‘first die is 3’
• 𝐵 = ‘sum is 6’
• 𝐶 = ‘sum is 7’
𝐴 is independent of
(a) 𝐵 and 𝐶 (b) 𝐵 alone (c) 𝐶 alone (d) Neither 𝐵 or 𝐶.
Solution: (c). (Explanation below)
𝑃 (𝐴) = 1/6, 𝑃 (𝐴|𝐵) = 1/5. Not equal, so not independent.
𝑃 (𝐴) = 1/6, 𝑃(𝐴|𝐶) = 1/6. Equal, so independent.
18.05 class 3 problems, Spring 2022 4
Notice that knowing 𝐵, removes 6 as a possibility for the first die and makes 𝐴 more
probable. So, knowing 𝐵 occurred changes the probability of 𝐴.
But, knowing 𝐶 does not change the probabilities for the possible values of the first roll;
they are still 1/6 for each value. In particular, knowing 𝐶 occured does not change the
probability of 𝐴.
We could also have done this problem by showing
𝑃 (𝐵|𝐴) ≠ 𝑃 (𝐵) or 𝑃 (𝐴 ∩ 𝐵) ≠ 𝑃 (𝐴)𝑃 (𝐵).
Problem 3. Evil Squirrels
Of the one million squirrels on MIT’s campus most are good-natured. But one hundred of
them are pure evil! An enterprising student in Course 6 develops an “Evil Squirrel Alarm”
which they offer to sell to MIT for a passing grade. MIT decides to test the reliability of
the alarm by conducting trials.
© Bigmacthealmanac. Some rights reserved. License: CC BY-SA. This content is excluded
from our Creative Commons license. For more information, see https://ocw.mit.edu/fairuse.
• When presented with an evil squirrel, the alarm goes off 99% of the time.
• When presented with a good-natured squirrel, the alarm goes off 1% of the time.
(a) If a squirrel sets off the alarm, what is the probability that it is evil?
(b) Should MIT co-opt the patent rights and employ the system?
One solution
(This is a base rate fallacy problem)
We are given:
𝑃 (nice) = 0.9999,𝑃 (evil) = 0.0001 (base rate)
𝑃 (alarm | nice) = 0.01,𝑃 (alarm | evil) = 0.99
18.05 class 3 problems, Spring 2022 5
𝑃 (alarm | evil)𝑃 (evil)
𝑃 (evil | alarm) =
𝑃 (alarm)
𝑃 (alarm | evil)𝑃 (evil)
=
𝑃 (alarm | evil)𝑃 (evil) + 𝑃(alarm | nice)𝑃 (nice)
(0.99)(0.0001)
=
(0.99)(0.0001) + (0.01)(0.9999)
≈ 0.01
Summary:
Probability a random test is correct = 0.99
Probability a positive test is correct ≈ 0.01
These probabilities are not the same!
Alternative method of calculation:
Evil Nice
Alarm 99 9999 10098
No alarm 1 989901 989902
100 999900 1000000
Solution: (a) This is the same solution as above, but in a more compact notation. Let 𝐸
be the event that a squirrel is evil. Let 𝐴 be the event that the alarm goes off. By Bayes’
Theorem, we have:
𝑃 (𝐴 | 𝐸)𝑃 (𝐸)
𝑃(𝐸 |𝐴) =
𝑃(𝐴 |𝐸)𝑃(𝐸) + 𝑃(𝐴 |𝐸𝑐)𝑃(𝐸𝑐)
0.99 100
= 1000000
(0.99)⋅( 100 )+(0.01) ⋅ ( 999900 )
1000000 1000000
≈ 0.01.
(b) No. The alarm would be more trouble than its worth, since for every true positive there
are about 99 false positives.
Problem 4. Dice Game
1. The Randomizer holds the 6-sided die in one fist and the 8-sided die in the other.
2. The Roller selects one of the Randomizer’s fists and covertly takes the die.
3. The Roller rolls the die in secret and reports the result to the table.
Given the reported number, what is the probability that the 6-sided die was chosen? (Find
the probability for each possible reported number.)
Solution: If the number rolled is 1-6 then 𝑃 (six-sided) = 4/7.
18.05 class 3 problems, Spring 2022 6
If the number rolled is 7 or 8 then 𝑃 (six-sided) = 0.
This is a Bayes’ formula problem. For concreteness let’s suppose the roll was a 4. What we
want to compute is 𝑃 (6-sided|roll 4). But, what is easy to compute is 𝑃 (roll 4|6-sided).
Bayes’ formula says
𝑃 (roll 4|6-sided)𝑃 (6-sided)
𝑃 (6-sided|roll 4) =
𝑃 (4)
(1/6)(1/2)
= = 4/7.
(1/6)(1/2) + (1/8)(1/2)
The denominator is computed using the law of total probability:
1 1 1 1
𝑃(4) = 𝑃(4|6-sided)𝑃 (6-sided) + 𝑃 (4|8-sided)𝑃 (8-sided) = ⋅ + ⋅ .
6 2 8 2
Note that any roll of 1,2,…6 would give the same result. A roll of 7 (or 8) would give clearly
give probability 0. This is seen in Bayes’ formula because the term 𝑃 (roll 7|6-sided) = 0.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
