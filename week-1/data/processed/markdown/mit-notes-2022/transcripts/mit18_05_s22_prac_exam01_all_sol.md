# Mit18 05 S22 Prac Exam01 All Sol

---

Exam 1 Practice Exam 1: Long List –solutions, 18.05, Spring
2022
This is a big list of practice problems for Exam 1. It includes all the problems
in other sets of practice problems and many more!
1 Counting and Probability
Problem 1. A full house in poker is a hand where three cards share one rank and two cards
share another rank. How many ways are there to get a full-house? What is the probability
of getting a full-house?
Solution: We build a full-house in stages and count the number of ways to make each
stage:
13
Stage 1. Choose the rank of the pair: ( ).
1
4
Stage 2. Choose the pair from that rank, i.e. pick 2 of 4 cards: ( ).
2
12
Stage 3. Choose the rank of the triple (from the remaining 12 ranks): ( ).
1
4
Stage 4. Choose the triple from that rank: ( ).
3
13 4 12 4
Number of ways to get a full-house: ( )( )( )( )
1 2 1 3
52
Number of ways to pick any 5 cards out of 52: ( )
5
13 4 12 4
( )( )( )( )
1 2 1 3
Probability of a full house: ≈ 0.00144
52
( )
5
Problem 2. There are 3 arrangements of the word DAD, namely DAD, ADD, and DDA.
How many arrangements are there of the word PROBABILITY?
Solution: Sort the letters: A BB II L O P R T Y. There are 11 letters in all. We build
arrangements by starting with 11 ‘slots’ and placing the letters in these slots, e.g
A B I B I L O P R T Y
Create an arrangement in stages and count the number of possibilities at each stage:
11
Stage 1: Choose one of the 11 slots to put the A: ( )
1
10
Stage 2: Choose two of the remaining 10 slots to put the B’s: ( )
2
8
Stage 3: Choose two of the remaining 8 slots to put the I’s: ( )
2
6
Stage 4: Choose one of the remaining 6 slots to put the L: ( )
1
1
Practice Exam 1: All Questions, Spring 2022 2
5
Stage 5: Choose one of the remaining 5 slots to put the O: ( )
1
4
Stage 6: Choose one of the remaining 4 slots to put the P: ( )
1
3
Stage 7: Choose one of the remaining 3 slots to put the R: ( )
1
2
Stage 8: Choose one of the remaining 2 slots to put the T: ( )
1
1
Stage 9: Use the last slot for the Y: ( )
1
Number of arrangements:
11 10 8 6 5 4 3 2 1 10⋅9 8⋅7
( )( )( )( )( )( )( )( )( ) = 11 ⋅ ⋅ ⋅ 6 ⋅ 5 ⋅ 4 ⋅ 3 ⋅ 2 ⋅ 1 = 9979200
1 2 2 1 1 1 1 1 1 2 2
Note: choosing 11 out of 1 is so simple we could have immediately written 11 instead of
11
belaboring the issue by writing ( ). We wrote it this way to show one systematic way to
1
think about problems like this.
Problem 3. (a) How many ways can you arrange the letters in the word STATISTICS?
(e.g. SSSTTTIIAC counts a one arrangement.)
(b) If all arrangements are equally likely, what is the probabilitiy the two ’i’s are next to
each other.
Solution: (a) Create an arrangement in stages and count the number of possibilities at
each stage:
10
Stage 1: Choose three of the 10 slots to put the S’s: ( )
3
7
Stage 2: Choose three of the remaining 7 slots to put the T’s: ( )
3
4
Stage 3: Choose two of the remaining 4 slots to put the I’s: ( )
2
2
Stage 4: Choose one of the remaining 2 slots to put the A: ( )
1
1
Stage 5: Use the last slot for the C: ( )
1
Number of arrangements:
10 7 4 2 1
( )( )( )( )( ) = 50400.
3 3 2 1 1
10
(b) The are ( ) = 45 equally likely ways to place the two I’s.
2
There are 9 ways to place them next to each other, i.e. in slots 1 and 2, slots 2 and 3, …,
slots 9 and 10.
So the probability the I’s are adjacent is 9/45 = 0.2.
Practice Exam 1: All Questions, Spring 2022 3
Problem 4. In a ballroom dancing class the students are divided into group 𝐴 and group
𝐵. There are six people in group 𝐴 and seven in group 𝐵. If four 𝐴s and four 𝐵s are
chosen and paired off, how many pairings are possible?
Solution: Build the pairings in stages and count the ways to build each stage:
6
Stage 1: Choose the 4 from group 𝐴: ( ).
4
7
Stage 2: Choose the 4 from group 𝐵: ( )
4
We need to be careful because we don’t want to build the same 4 couples in multiple ways.
Line up the 4 𝐴’s 𝐴 , 𝐴 , 𝐴 , 𝐴
1 2 3 4
Stage 3: Choose a partner from the 4 𝐵s for 𝐴 : 4.
1
Stage 4: Choose a partner from the remaining 3 𝐵s for 𝐴 : 3
2
Stage 5: Choose a partner from the remaining 2 𝐵s for 𝐴 : 2
3
Stage 6: Pair the last 𝐵 with 𝐴 : 1
4
6 7
Number of possible pairings: ( )( )4!.
4 4
Note: we could have done stages 3-6 in one go as: Stages 3-6: Arrange the 4 𝐵s opposite
the 4 𝐴s: 4! ways.
Problem 5. Suppose you pick two cards from a deck of 52 playing cards. What is the
probability that they are both queens?
Solution: Using choices (order doesn’t matter):
4 52
Number of ways to pick 2 queens: ( ). Number of ways to pick 2 cards: ( ).
2 2
4
( )
2
All choices of 2 cards are equally likely. So, probability of 2 queens =
52
( )
2
Using permutations (order matters):
Number of ways to pick the first queen: 4. No. of ways to pick the second queen: 3.
Number of ways to pick the first card: 52. No. of ways to pick the second card: 51.
All arrangements of 2 cards are equally likely. So, probability of 2 queens: 4⋅3 .
52⋅51
Problem 6. Suppose that there are ten students in a classroom. What is the probability
that no two of them have a birthday in the same month?
Solution: We assume each month is equally likely to be a student’s birthday month.
Number of ways ten students can have birthdays in 10 different months:
12!
12⋅11⋅10… ⋅3 =
2!
Number of ways 10 students can have birthday months: 1210.
12!
Probability no two share a birthday month: = 0.00387.
2! 1210
Problem 7. 20 politicians are having a tea party, 6 Democrats and 14 Republicans. To
prepare, they need to choose:
Practice Exam 1: All Questions, Spring 2022 4
3 people to set the table, 2 people to boil the water, 6 people to make the scones.
Each person can only do 1 task. (Note that this doesn’t add up to 20. The rest of the people
don’t help.)
(a) In how many different ways can they choose which people perform these tasks?
(b) Suppose that the Democrats all hate tea. If they only give tea to 10 of the 20 people,
what is the probability that they only give tea to Republicans?
(c) If they only give tea to 10 of the 20 people, what is the probability that they give tea to
9 Republicans and 1 Democrat?
Solution: (a) There are (20) ways to choose the 3 people to set the table, then (17) ways
3 2
to choose the 2 people to boil water, and (15) ways to choose the people to make scones.
6
So the total number of ways to choose people for these tasks is
20 17 15 20! 17! 15! 20!
( )( )( ) = ⋅ ⋅ = = 775975200.
3 2 6 3!17! 2!15! 6!9! 3!2!6!9!
(b) The number of ways to choose 10 of the 20 people is (20) The number of ways to choose
10
10 people from the 14 Republicans is (14) . So the probability that you only choose 10
10
Republicans is
(14) 14!
10 = 10! 4! ≈ 0.00542
(20) 20!
10 10! 10!
Alternatively, you could choose the 10 people in sequence and say that there is a 14/20
probability that the first person is a Republican, then a 13/19 probability that the second
one is, a 12/18 probability that third one is, etc. This gives a probability of
14 13 12 11 10 9 8 7 6 5
⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ ⋅ .
20 19 18 17 16 15 14 13 12 11
(You can check that this is the same as the other answer given above.)
(c) You can choose 1 Democrat in (6) = 6 ways, and you can choose 9 Republicans in (14)
1 9
ways, so the probability equals
6⋅ (14 ) 6⋅ 14! 6⋅14!10!10!
9 = 9!5! = .
(20 ) 20! 9! 5! 20!
10 10! 10!
Problem 8. Let 𝐴 and 𝐵 be two events. Suppose the probability that neither 𝐴 or 𝐵 occurs
is 2/3. What is the probability that one or both occur?
Solution: We are given 𝑃(𝐴𝑐 ∩ 𝐵𝑐) = 2/3 and asked to find 𝑃(𝐴 ∪ 𝐵).
𝐴𝑐 ∩ 𝐵𝑐 = (𝐴 ∪ 𝐵)𝑐 ⇒ 𝑃(𝐴 ∪ 𝐵) = 1−𝑃(𝐴𝑐 ∩ 𝐵𝑐) = 1/3.
Problem 9. Let 𝐶 and 𝐷 be two events with 𝑃(𝐶) = 0.25, 𝑃 (𝐷) = 0.45, and 𝑃(𝐶 ∩𝐷) =
0.1. What is 𝑃(𝐶𝑐 ∩𝐷)?
Solution: 𝐷 is the disjoint union of 𝐷 ∩ 𝐶 and 𝐷 ∩ 𝐶𝑐.
Practice Exam 1: All Questions, Spring 2022 5
𝐶 𝐷
So, 𝑃(𝐷 ∩ 𝐶)+𝑃(𝐷 ∩ 𝐶𝑐) = 𝑃(𝐷) 𝐷∩𝐶𝑐
⇒ 𝑃(𝐷 ∩ 𝐶𝑐) = 𝑃(𝐷)−𝑃(𝐷 ∩ 𝐶) = 0.45−0.1 = 0.35.
0.1 0.45−0.1
(We never use 𝑃(𝐶) = 0.25.)
Problem 10. You roll a four-sided die 3 times. For this problem we’ll use the sample
space with 64 equally likely outcomes.
(a) Write down this sample space in set notation.
(b) List all the outcomes in each of the following events.
(i) A = ‘Exactly 2 of the 3 rolls are fours’
(ii) B = ‘At least 2 of the 3 rolls are fours’
(iii) C = ’Exactly 1 of the second and third rolls is a 4’
(iv) 𝐴 ∩ 𝐶
Solution: (a) Writing all 64 possibilities is too tedius. Here’s a more compact representa-
tion
{(𝑖, 𝑗, 𝑘) | 𝑖, 𝑗, 𝑘 are integers from 1 to 4}
(b) (i) Here we’ll just list all 9 possibilities
{(4,4,1), (4,4,2), (4,4,3), (4,1,4), (4,2,4), (4,3,4), (1,4,4), (2,4,4), (3,4,4)}
(ii) This is the same as (i) with the addition of (4,4,4).
{ (4,4,1), (4,4,2), (4,4,3), (4,1,4), (4,2,4), (4,3,4), (1,4,4), (2,4,4), (3,4,4), (4,4,4)}
(iii) This is list is a little longer. If we’re systematic about it we can still just write it out.
{(1,4,1), (2,4,1), (3,4,1), (4,4,1),
(1,4,2), (2,4,2), (3,4,2), (4,4,2),
(1,4,3), (2,4,3), (3,4,3), (4,4,3),
(1,1,4), (2,1,4), (3,1,4), (4,1,4),
(1,2,4), (2,2,4), (3,2,4), (4,2,4),
(1,3,4), (2,3,4), (3,3,4), (4,3,4)}
(iv) {(4,4,1), (4,4,2), (4,4,3), (4,1,4), (4,2,4), (4,3,4)}
Problem 11. Suppose we have 8 teams labeled 𝑇 , …, 𝑇 . Suppose they are ordered by
1 8
placing their names in a hat and drawing the names out one at a time.
(a) How many ways can it happen that all the odd numbered teams are in the odd numbered
slots and all the even numbered teams are in the even numbered slots?
Solution: Slots 1, 3, 5, 7 are filled by 𝑇 , 𝑇 , 𝑇 , 𝑇 in any order: 4! ways.
1 3 5 7
Slots 2, 4, 6, 8 are filled by 𝑇 , 𝑇 , 𝑇 , 𝑇 in any order: 4! ways.
2 4 6 8
Solution: 4!⋅4! = 576.
(b) What is the probability of this happening?
Solution: There are 8! ways to fill the 8 slots in any way.
Practice Exam 1: All Questions, Spring 2022 6
4!⋅4! 576
Since each outcome is equally likely the probabilitiy is = = 0.143 = 1.43%.
8! 40320
2 Conditional Probability and Bayes’ Theorem
Problem 12. More cards! Suppose you want to divide a 52 card deck into four hands with
13 cards each. What is the probability that each hand has a king?
Solution: Let 𝐻 be the event that the 𝑖𝑡ℎ hand has one king. We have the conditional
𝑖
probabilities
4 48 3 36 2 24
( )( ) ( )( ) ( )( )
1 12 1 12 1 12
𝑃 (𝐻 ) = ; 𝑃 (𝐻 |𝐻 ) = ; 𝑃 (𝐻 |𝐻 ∩ 𝐻 ) =
1 52 2 1 39 3 1 2 26
( ) ( ) ( )
13 13 13
𝑃 (𝐻 |𝐻 ∩ 𝐻 ∩ 𝐻 ) = 1
4 1 2 3
𝑃 (𝐻 ∩ 𝐻 ∩ 𝐻 ∩ 𝐻 ) = 𝑃 (𝐻 |𝐻 ∩ 𝐻 ∩ 𝐻 ) 𝑃 (𝐻 |𝐻 ∩ 𝐻 ) 𝑃 (𝐻 |𝐻 ) 𝑃 (𝐻 )
1 2 3 4 4 1 2 3 3 1 2 2 1 1
2 24 3 36 4 48
( )( )( )( )( )( )
1 12 1 12 1 12
= .
26 39 52
( )( )( )
13 13 13
Problem 13. Suppose you are taking a multiple-choice test with 𝑐 choices for each question.
In answering a question on this test, the probability that you know the answer is 𝑝. If you
don’t know the answer, you choose one at random. What is the probability that you knew
the answer to a question, given that you answered it correctly?
Solution: The following tree shows the setting
𝑝 1−𝑝
Know Guess
1 0 1/𝑐 1−1/𝑐
Correct Wrong Correct Wrong
Let 𝐶 be the event that you answer the question correctly. Let 𝐾 be the event that you
actually know the answer. The left circled node shows 𝑃(𝐾 ∩𝐶) = 𝑝. Both circled nodes
together show 𝑃(𝐶) = 𝑝 +(1−𝑝)/𝑐. So,
𝑃(𝐾 ∩𝐶) 𝑝
𝑃(𝐾|𝐶) = =
𝑃(𝐶) 𝑝+(1−𝑝)/𝑐
Or we could use the algebraic form of Bayes’ theorem and the law of total probability: Let
𝐺 stand for the event that you’re guessing. Then we have,
𝑃(𝐶|𝐾) = 1, 𝑃(𝐾) = 𝑝, 𝑃(𝐶) = 𝑃(𝐶|𝐾)𝑃(𝐾)+𝑃(𝐶|𝐺)𝑃(𝐺) = 𝑝+(1−𝑝)/𝑐. So,
𝑃(𝐶|𝐾)𝑃(𝐾) 𝑝
𝑃(𝐾|𝐶) = =
𝑃(𝐶) 𝑝+(1−𝑝)/𝑐
Practice Exam 1: All Questions, Spring 2022 7
Problem 14. Corrupted by their power, the judges running the popular game show Amer-
ica’s Next Top Mathematician have been taking bribes from many of the contestants. Each
episode, a given contestant is either allowed to stay on the show or is kicked off.
If the contestant has been bribing the judges they will be allowed to stay with probability 1.
If the contestant has not been bribing the judges, they will be allowed to stay with probability
1/3.
Suppose that 1/4 of the contestants have been bribing the judges. The same contestants
bribe the judges in both rounds, i.e., if a contestant bribes them in the first round, they bribe
them in the second round too (and vice versa).
(a) If you pick a random contestant who was allowed to stay during the first episode, what
is the probability that they were bribing the judges?
(b) If you pick a random contestant, what is the probability that they are allowed to stay
during both of the first two episodes?
(c) If you pick random contestant who was allowed to stay during the first episode, what is
the probability that they get kicked off during the second episode?
Solution: The following tree shows the setting. Stay means the contestant was allowed
1
to stay during the first episode and stay means the they were allowed to stay during the
2
second.
1/4 3/4
Bribe Honest
1 0 1/3 2/3
Stay Leave Stay Leave
1 1 1 1
1 0 1/3 2/3
Stay Leave Stay Leave
2 2 2 2
Let’s name the relevant events:
𝐵 = the contestant is bribing the judges
𝐻 = the contestant is honest (not bribing the judges)
𝑆 = the contestant was allowed to stay during the first episode
1
𝑆 = the contestant was allowed to stay during the second episode
2
𝐿 = the contestant was asked to leave during the first episode
1
𝐿 = the contestant was asked to leave during the second episode
2
(a) We first compute 𝑃 (𝑆 ) using the law of total probability.
1
1 1 3 1
𝑃(𝑆 ) = 𝑃(𝑆 |𝐵)𝑃(𝐵)+𝑃(𝑆 |𝐻)𝑃(𝐻) = 1⋅ + ⋅ = .
1 1 1 4 3 4 2
𝑃(𝐵) 1/4 1
We therefore have (by Bayes’ rule) 𝑃(𝐵|𝑆 ) = 𝑃(𝑆 |𝐵) = 1 ⋅ = .
1 1 𝑃(𝑆 ) 1/2 2
1
(b) Using the tree we have the total probability of 𝑆 is
2
1 3 1 1 1
𝑃(𝑆 ) = + ⋅ ⋅ =
2 4 4 3 3 3
Practice Exam 1: All Questions, Spring 2022 8
𝑃 (𝐿 ∩ 𝑆 )
(c) We want to compute 𝑃 (𝐿 |𝑆 ) = 2 1 .
2 1 𝑃 (𝑆 )
1
From the calculation we did in part (a), 𝑃 (𝑆 ) = 1/2. For the numerator, we have (see the
1
tree)
1 2 3 1
𝑃(𝐿 ∩ 𝑆 ) = 𝑃(𝐿 ∩ 𝑆 |𝐵)𝑃(𝐵)+𝑃(𝐿 ∩ 𝑆 |𝐻)𝑃(𝐻) = 0⋅ + ⋅ =
2 1 2 1 2 1 4 9 4 6
1/6 1
Therefore 𝑃 (𝐿 |𝑆 ) = = .
2 1 1/2 3
Problem 15. Consider the Monty Hall problem. Let’s label the door with the car behind
it 𝑎 and the other two doors 𝑏 and 𝑐. In the game the contestant chooses a door and then
Monty chooses a door, so we can label each outcome as ‘contestant followed by Monty’, e.g
𝑎𝑏 means the contestant chose 𝑎 and Monty chose 𝑏.
(a) Make a 3×3 probability table showing probabilities for all possible outcomes.
(b) Make a probability tree showing all possible outcomes.
(c) Suppose the contestant’s strategy is to switch. List all the outcomes in the event ‘the
contestant wins a car’. What is the probability the contestant wins?
(d) Redo part (c) with the strategy of not switching.
Solution: (a) and (b) In the tree the first row is the contestant’s choice and the second
row is the host’s (Monty’s) choice.
Viewed as a table Viewed as a tree
Contestant
1 1 1
a b c 3 3 3
a 0 0 0 a b c
Host b 1/6 0 1/3 0 1
2 2
1 0 0 1 0 1 0
c 1/6 1/3 0
a b c a b c a b c
(b) With this strategy the contestant wins with {bc, cb}. The probability of winning is
𝑃 (𝑏𝑐) + 𝑃 (𝑐𝑏) = 2/3. (Both the tree and the table show this.)
(c) {𝑎𝑏, 𝑎𝑐}, probability = 1/3.
Problem 16. Two dice are rolled.
𝐴 = ‘sum of two dice equals 3’
𝐵 = ‘sum of two dice equals 7’
𝐶 = ‘at least one of the dice shows a 1’
(a) What is 𝑃 (𝐴|𝐶)?
(b) What is 𝑃 (𝐵|𝐶)?
(c) Are 𝐴 and 𝐶 independent? What about 𝐵 and 𝐶?
Solution: Sample space =
Ω = {(1,1), (1,2), (1,3), …, (6,6)} = {(𝑖,𝑗) |𝑖,𝑗 = 1, 2, 3, 4, 5, 6}.
Practice Exam 1: All Questions, Spring 2022 9
(Each outcome is equally likely, with probability 1/36.)
𝐴 = {(1, 2), (2, 1)},
𝐵 = {(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)}
𝐶 = {(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1)}
𝑃(𝐴 ∩ 𝐶) 2/36 2
(a) 𝑃(𝐴|𝐶) = = = ..
𝑃(𝐶) 11/36 11
𝑃(𝐵 ∩ 𝐶) 2/36 2
(b) 𝑃(𝐵|𝐶) = = = ..
𝑃(𝐶) 11/36 11
(c) 𝑃(𝐴) = 2/36 ≠ 𝑃(𝐴|𝐶), so they are not independent. Similarly, 𝑃 (𝐵) = 6/36 ≠
𝑃 (𝐵|𝐶), so they are not independent.
Problem 17. There is a screening test for prostate cancer that looks at the level of PSA
(prostate-specific antigen) in the blood. There are a number of reasons besides prostate
cancer that a man can have elevated PSA levels. In addition, many types of prostate cancer
develop so slowly that that they are never a problem. Unfortunately there is currently no
test to distinguish the different types and using the test is controversial because it is hard to
quantify the accuracy rates and the harm done by false positives.
For this problem we’ll call a positive test a true positive if it catches a dangerous type of
prostate cancer. We’ll assume the following numbers:
Rate of prostate cancer among men over 50 = 0.0005
True positive rate for the test = 0.9
False positive rate for the test = 0.01
Let 𝑇 be the event a man has a positive test and let 𝐷 be the event a man has a dangerous
type of the disease. Find 𝑃 (𝐷|𝑇 ) and 𝑃 (𝐷|𝑇 𝑐).
Solution: You should write this out in a tree! (For example, see the solution to the next
problem.)
We compute all the pieces needed to apply Bayes’ rule. We’re given
𝑃 (𝑇 |𝐷) = 0.9 ⇒ 𝑃 (𝑇 𝑐|𝐷) = 0.1, 𝑃(𝑇|𝐷𝑐) = 0.01 ⇒ 𝑃(𝑇 𝑐|𝐷𝑐) = 0.99.
𝑃(𝐷) = 0.0005 ⇒ 𝑃(𝐷𝑐) = 1−𝑃(𝐷) = 0.9995.
We use the law of total probability to compute 𝑃 (𝑇 ):
𝑃(𝑇) = 𝑃(𝑇|𝐷)𝑃(𝐷)+𝑃(𝑇|𝐷𝑐)𝑃(𝐷𝑐) = 0.9⋅0.0005+0.01 ⋅0.9995 = 0.010445
Now we can use Bayes’ rule to answer the questions:
𝑃 (𝑇 |𝐷) 𝑃 (𝐷) 0.9 × 0.0005
𝑃 (𝐷|𝑇 ) = = = 0.043
𝑃 (𝑇 ) 0.010445
𝑃(𝑇 𝑐|𝐷)𝑃(𝐷) 0.1×0.0005
𝑃(𝐷|𝑇 𝑐) = = = 5.0×10−5
𝑃 (𝑇 𝑐) 0.989555
Problem 18. A multiple choice exam has 4 choices for each question. A student has
studied enough so that the probability they will know the answer to a question is 0.5, the
probability that they will be able to eliminate one choice is 0.25, otherwise all 4 choices seem
Practice Exam 1: All Questions, Spring 2022 10
equally plausible. If they know the answer they will get the question right. If not they have
to guess from the 3 or 4 choices.
As the teacher you want the test to measure what the student knows. If the student answers
a question correctly what’s the probability they knew the answer?
Solution: We show the probabilities in a tree:
1/2 1/4
1/4
Know Eliminate 1 Total guess
1 0 1/3 2/3 1/4 3/4
Correct Wrong Correct Wrong Correct Wrong
For a given problem let 𝐶 be the event the student gets the problem correct and 𝐾 the
event the student knows the answer.
The question asks for 𝑃 (𝐾|𝐶).
We’ll compute this using Bayes’ rule:
𝑃(𝐶|𝐾)𝑃(𝐾) 1⋅1/2 24
𝑃(𝐾|𝐶) = = = ≈ 0.774 = 77.4%
𝑃(𝐶) 1/2+1/12+1/16 31
Problem 19. Suppose you have an urn containing 7 red and 3 blue balls. You draw three
balls at random. On each draw, if the ball is red you set it aside and if the ball is blue you
put it back in the urn. What is the probability that the third draw is blue?
(If you get a blue ball it counts as a draw even though you put it back in the urn.)
Solution: Here is the game tree, 𝑅 means red on the first draw etc.
1
7/10 3/10
𝑅 𝐵
1 1
6/9 3/9 7/10 3/10
𝑅 𝐵 𝑅 𝐵
2 2 2 2
5/8 3/8 6/9 3/9 6/9 3/9 7/10 3/10
𝑅 𝐵 𝑅 𝐵 𝑅 𝐵 𝑅 𝐵
3 3 3 3 3 3 3 3
Summing the probability to all the 𝐵 nodes we get
3
7 6 3 7 3 3 3 7 3 3 3 3
𝑃(𝐵 ) = ⋅ ⋅ + ⋅ ⋅ + ⋅ ⋅ + ⋅ ⋅ = 0.350.
3 10 9 8 10 9 9 10 10 9 10 10 10
Problem 20. Some games, like tennis or ping pong, reach a state called deuce. This means
that the score is tied and a player wins the game when they get two points ahead of the other
player. Suppose the probability that you win a point is 𝑝 and this is true independently for
all points. If the game is at deuce what is the probability you win the game?
This is a tricky problem, but amusing if you like puzzles.
Solution: Let 𝑊 be the event you win the game from deuce and 𝐿
deuce
Practice Exam 1: All Questions, Spring 2022 11
p 1-p
+1 −1
the event you lose. For convenience, define 𝑤 = 𝑃(𝑊).
p 1-p p 1-p
The figure shows the complete game tree through 2 points. In the
third level we just abreviate by indicating the probability of winning deuce deuce
𝑊 𝐿
from deuce. w w
The nodes marked +1 and -1, indicate whether you won or lost the
𝑊 𝑊
first point.
Summing all the paths to 𝑊 we get
𝑝2
𝑤 = 𝑃(𝑊) = 𝑝2+𝑝(1−𝑝)𝑤+(1−𝑝)𝑝𝑤 = 𝑝2+2𝑝(1−𝑝)𝑤 ⇒ 𝑤 = .
1 − 2𝑝(1 − 𝑝)
Problem 21. (Bayes formula)
A student takes a multiple-choice exam. Suppose for each question they either know the
answer or gamble and choose an option at random. Further suppose that if they knows the
answer, the probability of a correct answer is 1, and if they gamble, this probability is 1/4.
To pass, students need to answer at least 60% of the questions correctly. The student has
“studied for a minimal pass,” i.e., with probability 0.6 they know the answer to a question.
For a single question, given that they answers it correctly, what is the probability that they
actually knew the answer?
For a given problem let 𝐶 be the event the student gets the problem correct and 𝐾 the
event the student knows the answer.
The question asks for 𝑃 (𝐾|𝐶).
𝑃 (𝐶|𝐾) 𝑃 (𝐾)
We’ll compute this using Bayes’ rule: 𝑃(𝐾|𝐶) = .
𝑃 (𝐶)
We’re given: 𝑃(𝐶|𝐾) = 1, 𝑃(𝐾) = 0.6.
Law of total prob.:
𝑃(𝐶) = 𝑃(𝐶|𝐾)𝑃(𝐾) + 𝑃(𝐶|𝐾𝑐)𝑃(𝐾𝑐) = 1⋅0.6 + 0.25 ⋅0.4 = 0.7.
0.6
Therefore 𝑃(𝐾|𝐶) = = 0.857 = 85.7%.
0.7
3 Independence
Problem 22. Suppose that 𝑃 (𝐴) = 0.4, 𝑃 (𝐵) = 0.3 and 𝑃((𝐴∪𝐵)𝐶) = 0.42. Are 𝐴 and
𝐵 independent?
Solution: We have 𝑃(𝐴∪𝐵) = 1−0.42 = 0.58 and we know because of the inclusion-
exclusion principle that
𝑃(𝐴∪𝐵) = 𝑃(𝐴)+𝑃(𝐵)−𝑃(𝐴∩𝐵).
Thus,
𝑃 (𝐴 ∩ 𝐵) = 𝑃 (𝐴) + 𝑃 (𝐵) − 𝑃 (𝐴 ∪ 𝐵) = 0.4 + 0.3 − 0.58 = 0.12 = (0.4)(0.3) = 𝑃 (𝐴)𝑃 (𝐵).
So, 𝐴 and 𝐵 are independent.
Practice Exam 1: All Questions, Spring 2022 12
Problem 23. Suppose now that events 𝐴, 𝐵 and 𝐶 are mutually independent with
𝑃(𝐴) = 0.3, 𝑃(𝐵) = 0.4, 𝑃(𝐶) = 0.5.
Compute the following: (Hint: Use a Venn diagram)
(i) 𝑃(𝐴∩𝐵 ∩𝐶𝑐) (ii) 𝑃(𝐴∩𝐵𝑐 ∩𝐶) (iii) 𝑃(𝐴𝑐 ∩𝐵 ∩𝐶)
Solution: By the mutual independence we have
𝑃(𝐴∩𝐵∩𝐶) = 𝑃(𝐴)𝑃(𝐵)𝑃(𝐶) = 0.06 𝑃(𝐴∩𝐵) = 𝑃(𝐴)𝑃(𝐵) = 0.12
𝑃(𝐴∩𝐶) = 𝑃(𝐴)𝑃(𝐶) = 0.15 𝑃(𝐵∩𝐶) = 𝑃(𝐵)𝑃(𝐶) = 0.2
We show this in the following Venn diagram
𝐴 𝐵
0.06
0.09 0.14
0.06
0.09 0.14
0.21
𝐶
Note that, for instance, 𝑃 (𝐴 ∩ 𝐵) is split into two pieces. One of the pieces is 𝑃 (𝐴 ∩ 𝐵 ∩ 𝐶)
which we know and the other we compute as 𝑃(𝐴∩𝐵)−𝑃(𝐴∩𝐵∩𝐶) = 0.12−0.06 = 0.06.
The other intersections are similar.
We can read off the asked for probabilities from the diagram.
(i) 𝑃(𝐴∩𝐵 ∩𝐶𝑐) = 0.06
(ii) 𝑃(𝐴∩𝐵𝑐 ∩𝐶) = 0.09
(iii) 𝑃(𝐴𝑐 ∩𝐵 ∩𝐶) = 0.14.
Problem 24. You roll a twenty-sided die. Determine whether the following pairs of events
are independent.
(a) ‘You roll an even number’ and ‘You roll a number less than or equal to 10’.
(b) ‘You roll an even number’ and ‘You roll a prime number’.
Solution: 𝐸 = even numbered = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}.
𝐿 = roll ≤ 10 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}.
𝐵 = roll is prime = {2, 3, 5, 7, 11, 13, 17, 19} (We use 𝐵 because 𝑃 is not a good choice.)
(a) 𝑃(𝐸) = 10/20, 𝑃(𝐸|𝐿) = 5/10. These are the same, so the events are independent.
(b) 𝑃 (𝐸) = 10/20. 𝑃(𝐸|𝐵) = 1/8. These are not the same so the events are not indepen-
dent.
Problem 25. Suppose 𝐴 and 𝐵 are events with 0 < 𝑃(𝐴) < 1 and 0 < 𝑃(𝐵) < 1.
Practice Exam 1: All Questions, Spring 2022 13
(a) If 𝐴 and 𝐵 are disjoint can they be independent?
(b) If 𝐴 and 𝐵 are independent can they be disjoint?
(c) If 𝐴 ⊂ 𝐵 can they be independent?
Solution: The answer to all three parts is ‘No’. Each of these answers relies on the fact
that the probabilities of 𝐴 and 𝐵 are strictly between 0 and 1.
To show 𝐴 and 𝐵 are not independent we need to show either 𝑃(𝐴 ∩ 𝐵) ≠ 𝑃(𝐴) ⋅𝑃(𝐵)
or 𝑃 (𝐴|𝐵) ≠ 𝑃 (𝐴).
(a) No, they cannot be independent: 𝐴 ∩ 𝐵 = ∅ ⇒ 𝑃(𝐴 ∩ 𝐵) = 0 ≠ 𝑃(𝐴) ⋅𝑃(𝐵).
(b) No, they cannot be disjoint: same reason as in part (a).
(c) No, they cannot be independent: 𝐴 ⊂ 𝐵 ⇒ 𝐴 ∩ 𝐵 = 𝐴
⇒ 𝑃(𝐴 ∩ 𝐵) = 𝑃(𝐴) > 𝑃(𝐴) ⋅𝑃(𝐵). The last inequality follows because 𝑃(𝐵) < 1.
4 Expectation and Variance
Problem 26. Directly from the definitions of expected value and variance, compute 𝐸[𝑋]
and Var(𝑋) when 𝑋 has probability mass function given by the following table:
X -2 -1 0 1 2
pmf 1/15 2/15 3/15 4/15 5/15
Solution: We compute
1 2 3 4 5 2
𝐸[𝑋] = −2⋅ +−1 ⋅ +0 ⋅ +1 ⋅ +2 ⋅ = .
15 15 15 15 15 3
Thus
2
Var(𝑋) = 𝐸[(𝑋 − )2]
3
2 2 1 2 2 2 2 2 3 2 2 4 2 2 5
= (−2− ) ⋅ +(−1− ) ⋅ +(0− ) ⋅ +(1− ) ⋅ +(2− ) ⋅
3 15 3 15 3 15 3 15 3 15
14
= .
9
Problem 27. Suppose that 𝑋 takes values between 0 and 1 and has probability density
function 2𝑥. Compute Var(𝑋) and Var(𝑋2).
Solution: We will make use of the formula Var(𝑌 ) = 𝐸[𝑌 2] − 𝐸[𝑌 ]2. First we compute
1 2
𝐸[𝑋] = ∫ 𝑥 ⋅ 2𝑥𝑑𝑥 =
3
0
1 1
𝐸[𝑋2] = ∫ 𝑥2 ⋅ 2𝑥𝑑𝑥 =
2
0
1 1
𝐸[𝑋4] = ∫ 𝑥4 ⋅ 2𝑥𝑑𝑥 = .
3
0
Practice Exam 1: All Questions, Spring 2022 14
Thus,
1 4 1
Var(𝑋) = 𝐸[𝑋2] − (𝐸[𝑋]) 2 = − =
2 9 18
and
Var(𝑋2) = 𝐸[𝑋4] − (𝐸[𝑋2])
2
=
1
−
1
=
1
.
3 4 12
Problem 28. The random variable 𝑋 takes values -1, 0, 1 with probabilities 1/8, 2/8, 5/8
respectively.
(a) Compute 𝐸[𝑋].
(b) Give the pmf of 𝑌 = 𝑋2 and use it to compute 𝐸[𝑌 ].
(c) Instead, compute 𝐸[𝑋2] directly from an extended table.
(d) Compute Var(𝑋).
(a) Solution: We have
𝑋 values: -1 0 1
prob: 1/8 2/8 5/8
𝑋2 1 0 1
So, 𝐸[𝑋] = −1/8 + 5/8 = 1/2.
𝑌 values: 0 1
(b) Solution: ⇒ 𝐸[𝑌 ] = 6/8 = 3/4.
prob: 2/8 6/8
(c) Solution: The change of variables formula just says to use the bottom row of the table
in part (a): 𝐸[𝑋2] = 1⋅(1/8)+0 ⋅(2/8)+1 ⋅(5/8) = 3/4 (same as part (b)).
(d) Solution: Var(𝑋) = 𝐸[𝑋2] − 𝐸[𝑋]2 = 3/4 − 1/4 = 1/2.
Problem 29. Suppose 𝑋 is a random variable with 𝐸[𝑋] = 5 and Var(𝑋) = 2. What is
𝐸[𝑋2]?
Solution: Use Var(𝑋) = 𝐸[𝑋2] − 𝐸[𝑋]2 ⇒ 2 = 𝐸[𝑋2] − 25 ⇒ 𝐸[𝑋2] = 27.
Problem 30. Compute the expectation and variance of a Bernoulli(𝑝) random variable.
Solution: Make a table:
𝑋: 0 1
prob: (1-p) p
𝑋2 0 1.
From the table, 𝐸[𝑋] = 0⋅(1−𝑝)+1 ⋅𝑝 = 𝑝.
Since 𝑋 and 𝑋2 have the same table 𝐸[𝑋2] = 𝐸[𝑋] = 𝑝.
Therefore, Var(𝑋) = 𝑝−𝑝2 = 𝑝(1−𝑝).
Problem 31. Suppose 100 people all toss a hat into a box and then proceed to randomly
pick out of a hat. What is the expected number of people to get their own hat back.
Practice Exam 1: All Questions, Spring 2022 15
Hint: express the number of people who get their own hat as a sum of random variables
whose expected value is easy to compute.
Solution: Let 𝑋 be the number of people who get their own hat.
Following the hint: let 𝑋 represent whether person 𝑗 gets their own hat. That is, 𝑋 = 1
𝑗 𝑗
if person 𝑗 gets their hat and 0 if not.
100 100
We have, 𝑋 = ∑𝑋 , so 𝐸[𝑋] = ∑𝐸[𝑋 ].
𝑗 𝑗
𝑗=1 𝑗=1
Since person 𝑗 is equally likely to get any hat, we have 𝑃 (𝑋 = 1) = 1/100. Thus, 𝑋 ∼
𝑗 𝑗
Bernoulli(1/100) ⇒ 𝐸[𝑋 ] = 1/100 ⇒ 𝐸[𝑋] = 1.
𝑗
Problem 32. Suppose I play a gambling game with even odds. So, I can wager 𝑏 dollars
and I either win or lose 𝑏 dollars with probability 𝑝 = 0.5.
I employ the following strategy to try to guarantee that I win some money.
I bet $1; if I lose, I double my bet to $2, if I lose I double my bet again. I continue until
I win. Eventually I’m sure to win a bet and net $1 (run through the first few rounds and
you’ll see why this is the net).
If this really worked casinos would be out of business. Our goal in this problem is to
understand the flaw in the strategy.
(a) Let 𝑋 be the amount of money bet on the last game (the one I win). 𝑋 takes values 1,
2, 4, 8, …. Determine the probability mass function for 𝑋. That is, find 𝑝(2𝑘), where 𝑘 is
in {0, 1, 2, …}.
1
Solution: It is easy to see that (e.g. look at the probability tree) 𝑃 (2𝑘) = .
2𝑘+1
(b) Compute 𝐸[𝑋].
∞ 1 1
Solution: 𝐸[𝑋] = ∑2𝑘 = ∑ = ∞. Technically, 𝐸[𝑋] is undefined in this case.
2𝑘+1 2
𝑘=0
(c) Use your answer in part (b) to explain why the stategy is a bad one.
Solution: Technically, 𝐸[𝑋] is undefined in this case. But the value of ∞ tells us what
is wrong with the scheme. Since the average last bet is infinite, I need to have an infinite
amount of money in reserve.
This problem and solution is often referred to as the St. Petersburg paradox
Problem 33. Suppose you roll a fair 6-sided die 100 times (independently), and you get
$3 every time you roll a 6.
Let 𝑋 be the number of dollars you win on rolls 1 through 25.
1
Let 𝑋 be the number of dollars you win on rolls 26 through 50.
2
Let 𝑋 be the number of dollars you win on rolls 51 through 75.
3
Let 𝑋 be the number of dollars you win on rolls 76 throught 100.
4
Let 𝑋 = 𝑋 +𝑋 +𝑋 +𝑋 be the total number of dollars you win over all 100 rolls.
1 2 3 4
(a) What is the probability mass function of 𝑋?
Practice Exam 1: All Questions, Spring 2022 16
(b) What is the expectation and variance of 𝑋?
(c) Let 𝑌 = 4𝑋 . (So instead of rolling 100 times, you just roll 25 times and multiply your
1
winnings by 4.)
(i) What are the expectation and variance of 𝑌 ?
(ii) How do the expectation and variance of 𝑌 compare to those of 𝑋? (That is, are they
bigger, smaller, or equal?) Explain (briefly) why this makes sense.
Solution: (a) There are a number of ways to present this.
Let 𝑇 be the total number of times you roll a 6 in the 100 rolls. We know 𝑇 ∼ Binomial(100, 1/6).
Since you win $3 every time you roll a 6, we have 𝑋 = 3𝑇 . So, we can write
100 1 𝑘 5 100−𝑘
𝑃(𝑋 = 3𝑘) = ( )( ) ( ) , for 𝑘 = 0, 1, 2, …, 100.
𝑘 6 6
Alternatively we could write
100 1 𝑥/3 5 100−𝑥/3
𝑃(𝑋 = 𝑥) = ( ) ( ) ( ) , for 𝑥 = 0, 3, 6, …, 300.
𝑥/3 6 6
(b) 𝐸[𝑋] = 𝐸[3𝑇] = 3𝐸[𝑇] = 3⋅100⋅ 1 = 50,
6
Var(𝑋) = Var(3𝑇) = 9Var(𝑇) = 9⋅100⋅ 1 ⋅ 5 = 125.
6 6
(c) (i) Let 𝑇 be the total number of times you roll a 6 in the first 25 rolls. So, 𝑋 = 3𝑇
1 1 1
and 𝑌 = 12𝑇 .
1
Now, 𝑇 ∼ Binomial(25, 1/6), so
1
𝐸[𝑌] = 12𝐸[𝑇 ] = 12⋅25⋅16 = 50.
1
and
1 5
Var(𝑌) = 144Var(𝑇 ) = 144⋅25⋅ ⋅ = 500.
1 6 6
(ii) The expectations are the same by linearity because 𝑋 and 𝑌 are the both
3 × 100 × a Bernoulli(1/6) random variable.
For the variance, Var(𝑋) = 4Var(𝑋 ) because 𝑋 is the sum of 4 independent variables all
1
identical to 𝑋 . However Var(𝑌) = Var(4𝑋 ) = 16Var(𝑋 ). So, the variance of 𝑌 is 4
1 1 1
times that of 𝑋. This should make some intuitive sense because 𝑋 is built out of more
independent trials than 𝑋 .
1
Another way of thinking about it is that the difference between 𝑌 and its expectation is
four times the difference between 𝑋 and its expectation. However, the difference between
1
𝑋 and its expectation is the sum of such a difference for 𝑋 , 𝑋 , 𝑋 , and 𝑋 . It’s probably
1 2 3 4
the case that some of these deviations are positive and some are negative, so the absolute
value of this difference for the sum is probably less than four times the absolute value of this
difference for one of the variables, i.e. the deviations are likely to cancel to some extent.
5 Probability Mass Functions, Probability Density Functions
and Cumulative Distribution Functions
Problem 34. Suppose that 𝑋 ∼ Bin(𝑛, 0.5). Find the probability mass function of 𝑌 = 2𝑋.
Practice Exam 1: All Questions, Spring 2022 17
Solution: For 𝑦 = 0,2,4,…,2𝑛,
𝑦 𝑛 1 𝑛
𝑃(𝑌 = 𝑦) = 𝑃(𝑋 = ) = ( )( ) .
2 𝑦/2 2
Problem 35. (a) Suppose that 𝑋 is uniform on [0, 1]. Compute the pdf and cdf of 𝑋.
(b) If 𝑌 = 2𝑋+5, compute the pdf and cdf of 𝑌 .
(a) Solution: We have 𝑓 (𝑥) = 1 for 0 ≤ 𝑥 ≤ 1. The cdf of 𝑋 is
𝑋
𝑥 𝑥
𝐹 (𝑥) = ∫ 𝑓 (𝑡)𝑑𝑡 = ∫ 1𝑑𝑡 = 𝑥.
𝑋 𝑋
0 0
(b) Solution: Since 𝑋 is between 0 and 1 we have 𝑌 is between 5 and 7. Now for 5 ≤ 𝑦 ≤ 7,
we have
𝑦−5 𝑦−5 𝑦−5
𝐹 (𝑦) = 𝑃(𝑌 ≤ 𝑦) = 𝑃(2𝑋+5 ≤ 𝑦) = 𝑃(𝑋 ≤ ) = 𝐹 ( ) = .
𝑌 2 𝑋 2 2
Differentiating 𝑃(𝑌 ≤ 𝑦) with respect to 𝑦, we get the probability density function of 𝑌 ,
for 5 ≤ 𝑦 ≤ 7,
1
𝑓 (𝑦) = .
𝑌 2
Problem 36. (a) Suppose that 𝑋 has probability density function 𝑓 (𝑥) = 𝜆e−𝜆𝑥 for
𝑋
𝑥 ≥ 0. Compute the cdf, 𝐹 (𝑥).
𝑋
(b) If 𝑌 = 𝑋2, compute the pdf and cdf of 𝑌 .
(a) Solution: We have cdf of 𝑋,
𝑥
𝐹 (𝑥) = ∫ 𝜆e−𝜆𝑥𝑑𝑥 = 1 − e−𝜆𝑥.
𝑋
0
Now for 𝑦 ≥ 0, we have
(b) Solution:
√ √
𝐹 (𝑦) = 𝑃(𝑌 ≤ 𝑦) = 𝑃(𝑋2 ≤ 𝑦) = 𝑃(𝑋 ≤ 𝑦) = 1− e−𝜆 𝑦.
𝑌
Differentiating 𝐹 (𝑦) with respect to 𝑦, we have
𝑌
𝜆 √
𝑓
𝑌
(𝑦) =
2
𝑦− 1
2
e−𝜆 𝑦.
Problem 37. Suppose that 𝑋 is a random variable that takes on values 0, 2 and 3 with
probabilities 0.3, 0.1, 0.6 respectively. Let 𝑌 = 3(𝑋−1)2.
(a) What is the expectation of 𝑋?
(b) What is the variance of 𝑋?
(c) What is the expection of 𝑌 ?
Practice Exam 1: All Questions, Spring 2022 18
(d) Let 𝐹 (𝑡) be the cumulative density function of 𝑌 . What is 𝐹 (7)?
𝑌 𝑌
(a) Solution: We first make the probability tables
𝑋 0 2 3
prob. 0.3 0.1 0.6
𝑌 3 3 12
So, 𝐸[𝑋] = 0⋅0.3+2 ⋅0.1+3 ⋅0.6 = 2
(b) Solution: 𝐸[𝑋2] = 0⋅0.3+4 ⋅0.1+9 ⋅0.6 = 5.8 ⇒ Var(𝑋) = 𝐸[𝑋2] − 𝐸[𝑋]2 =
5.8−4 = 1.8.
(c) Solution: 𝐸[𝑌] = 3⋅0.3+3 ⋅0.1+12 ⋅6 = 8.4.
(d) Solution: From the table we see that 𝐹 (7) = 𝑃(𝑌 ≤ 7) = 0.4.
𝑌
Problem 38. Let 𝑇 be the waiting time for customers in a queue. Suppose that 𝑇 is
exponential with pdf 𝑓(𝑡) = 2e−2𝑡 on [0, ∞).
Find the pdf of the rate at which customers are served 𝑅 = 1/𝑇 .
Solution: The CDF for 𝑇 is
𝑡
𝑡
𝐹 (𝑡) = 𝑃(𝑇 ≤ 𝑡) = ∫ 2e−2𝑢 𝑑𝑢 = −e−2𝑢∣ = 1 − e−2𝑡.
𝑇 0
0
Next, we find the CDF of 𝑅. 𝑅 takes values in (0, ∞).
For 0 < 𝑟,
𝐹 (𝑟) = 𝑃(𝑅 ≤ 𝑟) = 𝑃(1/𝑇 < 𝑟) = 𝑃(𝑇 > 1/𝑟) = 1−𝐹 (1/𝑟) = e−2/𝑟.
𝑅 𝑇
𝑑 2
We differentiate to get 𝑓 (𝑟) = (e−2/𝑟) = e−2/𝑟.
𝑅 𝑑𝑟 𝑟2
Problem 39. A continuous random variable 𝑋 has PDF 𝑓(𝑥) = 𝑥 + 𝑎𝑥2 on [0,1]
Find 𝑎, the CDF and 𝑃(0.5 < 𝑋 < 1).
Solution: First we find the value of 𝑎:
1 1 1 𝑎
∫ 𝑓(𝑥)𝑑𝑥 = 1 = ∫ 𝑥+𝑎𝑥2𝑑𝑥 = + ⇒ 𝑎 = 3/2.
2 3
0 0
The CDF is 𝐹 (𝑥) = 𝑃(𝑋 ≤ 𝑥). We break this into cases:
𝑋
(i) 𝑏 < 0, so 𝐹 (𝑏) = 0.
𝑋
(ii) 0 ≤ 𝑏 ≤ 1, so 𝐹 (𝑏) = ∫ 𝑏 𝑥+ 3𝑥2𝑑𝑥 = 𝑏2 + 𝑏3.
𝑋 0 2 2 2
(iii) 1 < 𝑥, so 𝐹 (𝑏) = 1.
𝑋
Using 𝐹 we get
𝑋
0.52+0.53 13
𝑃(0.5 < 𝑋 < 1) = 𝐹 (1)−𝐹 (0.5) = 1−( ) = .
𝑋 𝑋 2 16
Problem 40. (PMF of a sum)
Suppose 𝑋 and 𝑌 are independent and 𝑋 ∼ Bernoulli(1/2) and 𝑌 ∼ Bernoulli(1/3).
Determine the pmf of 𝑋 +𝑌
Practice Exam 1: All Questions, Spring 2022 19
Solution: First we’ll give the joint probability table:
\𝑋 0 1
𝑌
0 1/3 1/3 2/3
1 1/6 1/6 1/3
1/2 1/2 1
We’ll use the joint probabilities to build the probability table for the sum.
𝑋 + 𝑌 0 1 2
(𝑋, 𝑌 ) (0,0) (0,1), (1,0) (1,1)
prob. 1/3 1/6 + 1/3 1/6
prob. 1/3 1/2 1/6
Problem 41. Let 𝑋 be a discrete random variable with pmf 𝑝 given by:
𝑥 −2 −1 0 1 2
𝑝(𝑥) 1/15 2/15 3/15 4/15 5/15
(a) Let 𝑌 = 𝑋2. Find the pmf of 𝑌 .
(b) Find the value the cdf of 𝑋 at -3/2, 3/4, 7/8, 1, 1.5, 5.
(c) Find the value the cdf of 𝑌 at -3/2, 3/4, 7/8, 1, 1.5, 5.
Solution: (a) Note: 𝑌 = 1 when 𝑋 = 1 or 𝑋 = −1, so
𝑃(𝑌 = 1) = 𝑃(𝑋 = 1)+𝑃(𝑋 = −1).
Values 𝑦 of 𝑌 0 1 4
pmf 𝑝 (𝑦) 3/15 6/15 6/15
𝑌
(b) and (c) To distinguish the distribution functions we’ll write 𝐹 and 𝐹 .
𝑋 𝑌
Using the tables in part (a) and the definition 𝐹 (𝑎) = 𝑃 (𝑋 ≤ 𝑎) etc. we get
𝑋
𝑎 -3/2 3/4 7/8 1 1.5 5
𝐹 (𝑎) 1/15 6/15 6/15 10/15 10/15 1
𝑋
𝐹 (𝑎) 0 3/15 3/15 9/15 9/15 1
𝑌
Problem 42. Suppose that the cdf of 𝑋 is given by:
⎧ 0 for 𝑎 < 0
{
{ 1 for 0 ≤ 𝑎 < 2
𝐹(𝑎) = 5
⎨ 2 for 2 ≤ 𝑎 < 4
{ { 5
⎩ 1 for 𝑎 ≥ 4.
Determine the pmf of 𝑋.
Solution: The jumps in the distribution function are at 0, 2, 4. The value of 𝑝(𝑎) at a
jump is the height of the jump:
𝑎 0 2 4
𝑝(𝑎) 1/5 1/5 3/5
Problem 43. For each of the following say whether it can be the graph of a cdf. If it can
be, say whether the variable is discrete or continuous.
Practice Exam 1: All Questions, Spring 2022 20
(i) (ii) (iii)
𝐹 (𝑥) 𝐹 (𝑥) 𝐹 (𝑥)
1 1 1
0.5 0.5 0.5
𝑥 𝑥 𝑥
(iv) (v) (vi)
𝐹 (𝑥) 𝐹 (𝑥) 𝐹 (𝑥)
1 1 1
0.5 0.5 0.5
𝑥 𝑥 𝑥
(vii) (viii)
𝐹 (𝑥) 𝐹 (𝑥)
1 1
0.5 0.5
𝑥 𝑥
Solution: (i) yes, discrete, (ii) no, (iii) no, (iv) no, (v) yes, continuous
(vi) no (vii) yes, continuous, (viii) yes, continuous.
Problem 44. Suppose 𝑋 has range [0,1] and has cdf
𝐹 (𝑥) = 𝑥2 for 0 ≤ 𝑥 ≤ 1.
Compute 𝑃(1 < 𝑋 < 3).
2 4
Solution: 𝑃 (1/2 ≤ 𝑋 ≤ 3/4) = 𝐹 (3/4) − 𝐹 (1/2) = (3/4)2 − (1/2)2 = 5/16 .
Problem 45. Let 𝑋 be a random variable with range [0, 1] and cdf
𝐹 (𝑋) = 2𝑥2 − 𝑥4 for 0 ≤ 𝑥 ≤ 1.
(a) Compute 𝑃(1 ≤ 𝑋 ≤ 3).
4 4
(b) What is the pdf of 𝑋?
Solution: (a) 𝑃(1/4 ≤ 𝑋 ≤ 3/4) = 𝐹(3/4)−𝐹(1/4) = 11/16 = 0.6875.
(b) 𝑓(𝑥) = 𝐹 ′(𝑥) = 4𝑥 − 4𝑥3 in [0,1].
6 Distributions with Names
Problem 46. Exponential Distribution
Suppose that buses arrive are scheduled to arrive at a bus stop at noon but are always 𝑋
minutes late, where 𝑋 is an exponential random variable with probability density function
𝑓 (𝑥) = 𝜆e−𝜆𝑥. Suppose that you arrive at the bus stop precisely at noon.
𝑋
Practice Exam 1: All Questions, Spring 2022 21
(a) Compute the probability that you have to wait for more than five minutes for the bus
to arrive.
Solution: We compute
5
𝑃(𝑋 ≥ 5) = 1−𝑃(𝑋 < 5) = 1−∫ 𝜆e−𝜆𝑥𝑑𝑥 = 1 − (1 − e−5𝜆) = e−5𝜆.
0
(b) Suppose that you have already waiting for 10 minutes. Compute the probability that you
have to wait an additional five minutes or more.
Solution: We want 𝑃 (𝑋 ≥ 15|𝑋 ≥ 10). First observe that 𝑃(𝑋 ≥ 15,𝑋 ≥ 10) = 𝑃(𝑋 ≥
15). From similar computations in (a), we know
𝑃(𝑋 ≥ 15) = e−15𝜆 𝑃 (𝑋 ≥ 10) = e−10𝜆.
From the definition of conditional probability,
𝑃(𝑋 ≥ 15,𝑋 ≥ 10) 𝑃(𝑋 ≥ 15)
𝑃(𝑋 ≥ 15|𝑋 ≥ 10) = = = e−5𝜆
𝑃(𝑋 ≥ 10) 𝑃(𝑋 ≥ 10)
Note: This is an illustration of the memorylessness property of the exponential distribu-
tion.
Problem 47. Normal Distribution: Throughout these problems, let 𝜙 and Φ be the pdf
and cdf, respectively, of the standard normal distribution Suppose 𝑍 is a standard normal
random variable and let 𝑋 = 3𝑍 +1.
(a) Express 𝑃(𝑋 ≤ 𝑥) in terms of Φ
Solution: We have
𝑥−1 𝑥−1
𝐹 (𝑥) = 𝑃(𝑋 ≤ 𝑥) = 𝑃(3𝑍 +1 ≤ 𝑥) = 𝑃(𝑍 ≤ ) = Φ( ).
𝑋 3 3
(b) Differentiate the expression from (𝑎) with respect to 𝑥 to get the pdf of 𝑋, 𝑓(𝑥).
Remember that Φ′(𝑧) = 𝜙(𝑧) and don’t forget the chain rule
Solution: Differentiating with respect to 𝑥, we have
d 1 𝑥 − 1
𝑓 (𝑥) = 𝐹 (𝑥) = 𝜙( ).
𝑋 dx 𝑋 3 3
Since 𝜙(𝑥) = (2𝜋)−
2
1 e− 𝑥
2
2 , we conclude
𝑓 𝑋 (𝑥) = √ 1 e − (𝑥 2 − ⋅3 1 2 )2 ,
3 2𝜋
which is the probability density function of the 𝑁(1, 9) distribution. Note: The arguments
in (a) and (b) give a proof that 3𝑍 +1 is a normal random variable with mean 1 and variance
9. See Problem Set 3, Question 5.
(c) Find 𝑃(−1 ≤ 𝑋 ≤ 1)
Practice Exam 1: All Questions, Spring 2022 22
Solution: We have
2 2
𝑃(−1 ≤ 𝑋 ≤ 1) = 𝑃 (− ≤ 𝑍 ≤ 0) = Φ(0)−Φ(− ) ≈ 0.2475
3 3
(d) Recall that the probability that 𝑍 is within one standard deviation of its mean is approx-
imately 68%. What is the probability that 𝑋 is within one standard deviation of its mean?
Solution: Since 𝐸[𝑋] = 1, Var(𝑋) = 9, we want 𝑃(−2 ≤ 𝑋 ≤ 4). We have
𝑃(−2 ≤ 𝑋 ≤ 4) = 𝑃(−3 ≤ 3𝑍 ≤ 3) = 𝑃(−1 ≤ 𝑍 ≤ 1) ≈ 0.68.
Problem 48. Transforming Normal Distributions
Suppose 𝑍 ∼ N(0,1) and 𝑌 = e𝑍 .
(a) Find the cdf 𝐹 (𝑎) and pdf 𝑓 (𝑦) for 𝑌 . (For the CDF, the best you can do is write it
𝑌 𝑌
in terms of Φ the standard normal cdf.)
Solution: Note, 𝑌 follows what is called a log-normal distribution.
𝐹 (𝑎) = 𝑃(𝑌 ≤ 𝑎) = 𝑃(𝑒𝑍 ≤ 𝑎) = 𝑃(𝑍 ≤ ln(𝑎)) = Φ(ln(𝑎)).
𝑌
Differentiating using the chain rule:
𝑑 𝑑 1 1
𝑓 (𝑎) = 𝐹 (𝑎) = Φ(ln(𝑎)) = 𝜙(ln(𝑎)) = √ e−(ln(𝑎))2/2.
𝑦 𝑑𝑎 𝑌 𝑑𝑎 𝑎 2𝜋 𝑎
(b) We don’t have a formula for Φ(𝑧) so we don’t have a formula for quantiles. So we have
to write quantiles in terms of Φ−1.
(i) Write the 0.33 quantile of 𝑍 in terms of Φ−1
(ii) Write the 0.9 quantile of 𝑌 in terms of Φ−1.
(iii) Find the median of 𝑌 .
Solution: (i) The 0.33 quantile for 𝑍 is the value 𝑞 such that 𝑃 (𝑍 ≤ 𝑞 ) = 0.33.
0.33 0.33
That is, we want
Φ(𝑞 ) = 0.33 ⇔ 𝑞 = Φ−1(0.33) .
0.33 0.33
(ii) We want to find 𝑞 where
0.9
𝐹 (𝑞 ) = 0.9 ⇔ Φ(ln(𝑞 )) = 0.9 ⇔ 𝑞 = eΦ−1(0.9) .
𝑌 0.9 0.9 0.9
(iii) As in (ii) 𝑞 = eΦ−1(0.5) = e0 = 1 .
0.5
Problem 49. (Random variables derived from normal random variables)
Let 𝑋 , 𝑋 , …𝑋 be i.i.d. N(0, 1) random variables.
1 2 𝑛
Let 𝑌 = 𝑋2 + … + 𝑋2 .
𝑛 1 𝑛
(a) Use the formula Var(𝑋 ) = 𝐸[𝑋2] − 𝐸[𝑋 ]2 to show 𝐸[𝑋2] = 1.
𝑗 𝑗 𝑗 𝑗
Solution: Var(𝑋 ) = 1 = 𝐸[𝑋2] − 𝐸[𝑋 ]2 = 𝐸[𝑋2]. QED
𝑗 𝑗 𝑗 𝑗
Practice Exam 1: All Questions, Spring 2022 23
(b) Set up an integral in 𝑥 for computing 𝐸[𝑋4].
𝑗
For 3 extra credit points, use integration by parts show 𝐸[𝑋4] = 3.
𝑗
(If you don’t do this, you can still use this result in part c.)
1 ∞
Solution: 𝐸[𝑋4] = √ ∫ 𝑥4e−𝑥2/2 𝑑𝑥.
𝑗
2𝜋
−∞
(Extra credit) By parts: let 𝑢 = 𝑥3, 𝑣′ = 𝑥e−𝑥2/2 ⇒ 𝑢′ = 3𝑥2, 𝑣 = −e−𝑥2/2
1 ∞ 1 ∞
𝐸[𝑋4] = √ [𝑥3e−𝑥2/2∣ + √ ∫ 3𝑥2e−𝑥2/2 𝑑𝑥]
𝑗
2𝜋 𝑖𝑛𝑓𝑡𝑦 2𝜋
−∞
The first term is 0 and the second term is the formula for 3𝐸[𝑋2] = 3 (by part (a)). Thus,
𝑗
𝐸[𝑋4] = 3.
𝑗
(c) Deduce from parts (a) and (b) that Var(𝑋2) = 2.
𝑗
Solution: Var(𝑋2) = 𝐸[𝑋4] − 𝐸[𝑋2]2 = 3 − 1 = 2. QED
𝑗 𝑗 𝑗
(d) Use the Central Limit Theorem to approximate 𝑃 (𝑌 > 110).
100
Solution: 𝐸[𝑌 ] = 𝐸[100𝑋2] = 100. Var(𝑌 ) = 100Var(𝑋 ) = 200.
100 𝑗 100 𝑗
The CLT says 𝑌 is approximately normal. Standardizing gives
100
𝑌 −100 10 √
𝑃(𝑌 > 110) = 𝑃 ( 10√0 > √ ) ≈ 𝑃(𝑍 > 1/ 2) = 0.24 .
100
200 200
This last value was computed using R: 1 - pnorm(1/sqrt(2),0,1).
Problem 50. More Transforming Normal Distributions
(a) Suppose 𝑍 is a standard normal random variable and let 𝑌 = 𝑎𝑍+𝑏, where 𝑎 > 0 and
𝑏 are constants.
Show 𝑌 ∼ N(𝑏, 𝑎2) (remember our notation for normal distributions uses mean and vari-
ance).
Solution: Let 𝜙(𝑧) and Φ(𝑧) be the PDF and CDF of 𝑍.
𝐹 (𝑦) = 𝑃 (𝑌 ≤ 𝑦) = 𝑃 (𝑎𝑍 + 𝑏 ≤ 𝑦) = 𝑃 (𝑍 ≤ (𝑦 − 𝑏)/𝑎) = Φ((𝑦 − 𝑏)/𝑎).
𝑌
Differentiating:
𝑑 𝑑 1 1
𝑓 (𝑦) = 𝐹 (𝑦) = Φ((𝑦−𝑏)/𝑎) = 𝜙((𝑦−𝑏)/𝑎) = √ e−(𝑦−𝑏)2/2𝑎2.
𝑌 𝑑𝑦 𝑌 𝑑𝑦 𝑎 2𝜋𝑎
Since this is the density for N(𝑏, 𝑎2) we have shown 𝑌 ∼ N(𝑏, 𝑎2).
𝑌 −𝜇
(b) Suppose 𝑌 ∼ N(𝜇, 𝜎2). Show follows a standard normal distribution.
𝜎
Solution: By part (a), 𝑌 ∼ N(𝜇,𝜎2) ⇒ 𝑌 = 𝜎𝑍 +𝜇. But, this implies (𝑌 −𝜇)/𝜎 = 𝑍 ∼
N(0, 1). QED
Problem 51. (Sums of normal random variables)
Let 𝑋, 𝑌 be independent random variables where 𝑋 ∼ 𝑁(2,5) and 𝑌 ∼ 𝑁(5,9) (we use the
notation 𝑁(𝜇, 𝜎2)). Let 𝑊 = 3𝑋−2𝑌 +1.
(a) Compute 𝐸[𝑊 ] and Var(𝑊 ).
Practice Exam 1: All Questions, Spring 2022 24
Solution: 𝐸[𝑊] = 3𝐸[𝑋]−2𝐸[𝑌]+1 = 6−10+1 = −3
Var(𝑊) = 9Var(𝑋) + 4Var(𝑌) = 45+36 = 81
(b) It is known that the sum of independent normal distributions is normal. Compute
𝑃(𝑊 ≤ 6).
Solution: Since the sum of independent normal is normal part (a) shows: 𝑊 ∼ 𝑁(−3,81).
𝑊 +3 9
Let 𝑍 ∼ 𝑁(0,1). We standardize 𝑊 : 𝑃(𝑊 ≤ 6) = 𝑃 ( ≤ ) = 𝑃(𝑍 ≤ 1) ≈ 0.84.
9 9
Problem 52. Let 𝑋 ∼ U(𝑎, 𝑏). Compute 𝐸[𝑋] and Var(𝑋).
Solution: Method 1
1
𝑈(𝑎, 𝑏) has density 𝑓(𝑥) = on [𝑎,𝑏]. So,
𝑏 − 𝑎
𝑏 1 𝑏 𝑥2 𝑏 𝑏2 − 𝑎2 𝑎 + 𝑏
𝐸[𝑋] = ∫ 𝑥𝑓(𝑥)𝑑𝑥 = ∫ 𝑥𝑑𝑥 = ∣ = = .
𝑏−𝑎 2(𝑏−𝑎) 2(𝑏−𝑎) 2
𝑎 𝑎 𝑎
𝑏 1 𝑏 𝑥3 𝑏 𝑏3 − 𝑎3
𝐸[𝑋2] = ∫ 𝑥2𝑓(𝑥)𝑑𝑥 = ∫ 𝑥2𝑑𝑥 = ∣ = .
𝑏−𝑎 3(𝑏−𝑎) 3(𝑏−𝑎)
𝑎 𝑎 𝑎
Finding Var(𝑋) now requires a little algebra,
𝑏3 − 𝑎3 (𝑏 + 𝑎)2
Var(𝑋) = 𝐸[𝑋2] − 𝐸[𝑋]2 = −
3(𝑏 − 𝑎) 4
4(𝑏3 − 𝑎3) − 3(𝑏 − 𝑎)(𝑏 + 𝑎)2 𝑏3 − 3𝑎𝑏2 + 3𝑎2𝑏 − 𝑎3 (𝑏 − 𝑎)3 (𝑏 − 𝑎)2
= = = = .
12(𝑏 − 𝑎) 12(𝑏 − 𝑎) 12(𝑏 − 𝑎) 12
Method 2
There is an easier way to find 𝐸[𝑋] and Var(𝑋).
Let 𝑈 ∼ U(𝑎, 𝑏). Then the calculations above show 𝐸[𝑈] = 1/2 and (𝐸[𝑈2] = 1/3 ⇒
Var(𝑈) = 1/3 − 1/4 = 1/12.
Now, we know 𝑋 = (𝑏−𝑎)𝑈 +𝑎, so 𝐸[𝑋] = (𝑏 − 𝑎)𝐸[𝑈] + 𝑎 = (𝑏 − 𝑎)/2 + 𝑎 = (𝑏 + 𝑎)/2
and Var(𝑋) = (𝑏 − 𝑎)2Var(𝑈) = (𝑏 − 𝑎)2/12.
Problem 53. In 𝑛 + 𝑚 independent Bernoulli(𝑝) trials, let 𝑆 be the number of successes
𝑛
in the first 𝑛 trials and 𝑇 the number of successes in the last 𝑚 trials.
𝑚
(a) What is the distribution of 𝑆 ? Why?
𝑛
Solution: 𝑆 ∼ Binomial(𝑛, 𝑝), since it is the number of successes in 𝑛 independent
𝑛
Bernoulli trials.
(b) What is the distribution of 𝑇 ? Why?
𝑚
Solution: 𝑇 ∼ Binomial(𝑚, 𝑝), since it is the number of successes in 𝑚 independent
𝑚
Bernoulli trials.
(c) What is the distribution of 𝑆 + 𝑇 ? Why?
𝑛 𝑚
Solution: 𝑆 + 𝑇 ∼ Binomial(𝑛 + 𝑚, 𝑝), since it is the number of successes in 𝑛 + 𝑚
𝑛 𝑚
independent Bernoulli trials.
Practice Exam 1: All Questions, Spring 2022 25
(d) Are 𝑆 and 𝑇 independent? Why?
𝑛 𝑚
Solution: Yes, 𝑆 and 𝑇 are independent. We haven’t given a formal definition of inde-
𝑛 𝑚
pendent random variables yet. But, we know it means that knowing 𝑆 gives no information
𝑛
about 𝑇 . This is clear since the first 𝑛 trials are independent of the last 𝑚.
𝑚
Problem 54. Compute the median for the exponential distribution with parameter 𝜆.
Solution: The density for this distribution is 𝑓(𝑥) = 𝜆 e−𝜆𝑥. We know (or can compute)
that the distribution function is 𝐹(𝑎) = 1− e−𝜆𝑎. The median is the value of 𝑎 such that
𝐹 (𝑎) = 0.5. Thus, 1− e−𝜆𝑎 = 0.5 ⇒ 0.5 = e−𝜆𝑎 ⇒ log(0.5) = −𝜆𝑎 ⇒ 𝑎 = log(2)/𝜆.
Problem 55. Pareto and the 80-20 rule.
Pareto was an economist who used the Pareto distribution to model the wealth in a society.
For a fixed baseline 𝑚, the Pareto density with parameter 𝛼 is
𝛼 𝑚𝛼
𝑓(𝑥) = for 𝑥 ≥ 𝑚.
𝑥𝛼+1
Assume 𝑋 is a random variable that follows such a distribution.
(a) Compute 𝑃(𝑋 > 𝑎) (you may assume 𝑎 ≥ 𝑚).
∞ 𝛼𝑚𝛼 𝑚𝛼 ∞ 𝑚𝛼
Solution: 𝑃(𝑋 > 𝑎) = ∫ = − ∣ = .
𝑥𝛼+1 𝑥𝛼 𝑎𝛼
𝑎 𝑎
(b) Pareto’s principle is often paraphrased as the 80-20 rule. That is, 80% of the wealth
is owned by 20% of the people. The rule is only exact for a Pareto distribution with
𝛼 = log(5)/ log(4) = 1.16.
Suppose 𝛼 = 𝑚 = 1. Compute the 0.80 quantile for the Pareto distribution.
In general, many phenomena follow the power law described by 𝑓(𝑥). You can look up
’Pareto principle’ in Wikipedia to read more about this.
Solution: We want the value 𝑞 where 𝑃 (𝑋 ≤ 𝑞 ) = 0.8.
0.8 0.8
This is equivalent to 𝑃 (𝑋 > 𝑞 ) = 0.2. Using part (a) and the given values of 𝑚 and 𝛼
0.8
1
we have = 0.2 ⇒ 𝑞 = 5.
𝑞 0.8
0.8
7 Joint Probability, Covariance, Correlation
Problem 56. (Another Arithmetic Puzzle)
Let 𝑋 and 𝑌 be two independent Bernoulli(0.5) random variables. Define 𝑆 and 𝑇 by:
𝑆 = 𝑋+𝑌 and 𝑇 = 𝑋−𝑌.
(a) Find the joint and marginal pmf’s for 𝑆 and 𝑇 .
(b) Are 𝑆 and 𝑇 independent.
Solution: (a) 𝑆 = 𝑋+𝑌 takes values 0, 1, 2 and 𝑇 = 𝑋−𝑌 takes values -1, 0, 1.
First we make two tables: the joint probability table for 𝑋 and 𝑌 and a table given the values
(𝑆, 𝑇 ) corresponding to values of (𝑋,𝑌 ), e.g. (𝑋,𝑌) = (1,1) corresponds to (𝑆,𝑇) = (2,0).
Practice Exam 1: All Questions, Spring 2022 26
\𝑌 0 1 \𝑌 0 1
𝑋 𝑋
0 1/4 1/4 0 0,0 1,-1
1 1/4 1/4 1 1,1 2,0
Joint probabilities of 𝑋 and 𝑌 Values of (𝑆, 𝑇 ) corresponding to 𝑋 and 𝑌
We can use the two tables above to write the joint probability table for 𝑆 and 𝑇 . The
marginal probabilities are given in the table.
\𝑇 -1 0 1
𝑆
0 0 1/4 0 1/4
1 1/4 0 1/4 1/2
2 0 1/4 0 1/4
1/4 1/2 1/4 1
Joint and marginal probabilities of 𝑆 and 𝑇
(b) No probabilities in the table are the product of the corresponding marginal probabilities.
(This is easiest to see for the 0 entries.) So, 𝑆 and 𝑇 are not independent
Problem 57. Data is taken on the height and shoe size of a sample of MIT students.
Height is coded by 3 values: 1 (short), 2 (average), 3 (tall) and shoe size is coded by 3
values 1 (small), 2 (average), 3 (large). The joint counts are given in the following table.
Shoe \ Height 1 2 3
1 234 225 84
2 180 453 161
3 39 192 157
Let 𝑋 be the coded shoe size and 𝑌 the height of a random person in the sample.
(a) Find the joint and marginal pmf of 𝑋 and 𝑌 .
(b) Are 𝑋 and 𝑌 independent?
Solution: (a) The joint distribution is found by dividing each entry in the data table by
the total number of people in the sample. Adding up all the entries we get 1725. So the
joint probability table with marginals is
\ 𝑋 1 2 3
𝑌
1 234 225 84 543
1725 1725 1725 1725
2 180 453 161 794
1725 1725 1725 1725
3 39 192 157 388
1725 1725 1725 1725
453 839 433 1
1725 1725 1725
The marginal distribution of 𝑋 is at the right and of 𝑌 is at the bottom.
(b) 𝑋 and 𝑌 are dependent because, for example,
234
𝑃(𝑋 = 1 and 𝑌 = 1) = ≈ 0.136
1725
is not equal to
453 543
𝑃(𝑋 = 1)𝑃(𝑌 = 1) = ⋅ ≈ 0.083.
1725 1725
Practice Exam 1: All Questions, Spring 2022 27
Problem 58. Let 𝑋 and 𝑌 be two continuous random variables with joint pdf
𝑓(𝑥,𝑦) = 𝑐𝑥2𝑦(1+𝑦) for 0 ≤ 𝑥 ≤ 3 and 0 ≤ 𝑦 ≤ 3,
and 𝑓(𝑥,𝑦) = 0 otherwise.
(a) Find the value of 𝑐.
(b) Find the probability 𝑃(1 ≤ 𝑋 ≤ 2, 0 ≤ 𝑌 ≤ 1).
(c) Determine the joint cdf, 𝐹 (𝑎, 𝑏), of 𝑋 and 𝑌 for 𝑎 and 𝑏 between 0 and 3.
(d) Find marginal cdf 𝐹 (𝑎) for 𝑎 between 0 and 3.
𝑋
(e) Find the marginal pdf 𝑓 (𝑥) directly from 𝑓(𝑥, 𝑦) and check that it is the derivative of
𝑋
𝐹 (𝑥).
𝑋
(f) Are 𝑋 and 𝑌 independent?
Solution: (a) Total probability must be 1, so
3 3 3 3 243
1 = ∫ ∫ 𝑓(𝑥,𝑦)𝑑𝑦𝑑𝑥 = ∫ ∫ 𝑐(𝑥2𝑦+𝑥2𝑦2)𝑑𝑦𝑑𝑥 = 𝑐⋅ ,
2
0 0 0 0
2
(Here we skipped showing the arithmetic of the integration) Therefore, 𝑐 = .
243
(b)
2 1
𝑃(1 ≤ 𝑋 ≤ 2, 0 ≤ 𝑌 ≤ 1) = ∫ ∫ 𝑓(𝑥,𝑦)𝑑𝑦𝑑𝑥
1 0
2 1
= ∫ ∫ 𝑐(𝑥2𝑦 + 𝑥2𝑦2) 𝑑𝑦 𝑑𝑥
1 0
35
= 𝑐 ⋅
18
70
= ≈ 0.016
4374
(c) For 0 ≤ 𝑎 ≤ 3 and 0 ≤ 𝑏 ≤ 3. we have
𝑎 𝑏 𝑎3𝑏2 𝑎3𝑏3
𝐹(𝑎,𝑏) = ∫ ∫ 𝑓(𝑥,𝑦)𝑑𝑦𝑑𝑥 = 𝑐( + )
6 9
0 0
(d) Since 𝑦 = 3 is the maximum value for 𝑌 , we have
9𝑎3 9 𝑎3
𝐹 (𝑎) = 𝐹(𝑎,3) = 𝑐( +3𝑎3) = 𝑐𝑎3 =
𝑋 6 2 27
(e) For 0 ≤ 𝑥 ≤ 3, we have, by integrating over the entire range for 𝑦,
3 32 33 27 1
𝑓 (𝑥) = ∫ 𝑓(𝑥,𝑦)𝑑𝑦 = 𝑐𝑥2( + ) = 𝑐 𝑥2 = 𝑥2.
𝑋 2 3 2 9
0
This is consistent with (c) because 𝑑 (𝑥3/27) = 𝑥2/9.
𝑑𝑥
Practice Exam 1: All Questions, Spring 2022 28
(f) Since 𝑓(𝑥, 𝑦) separates into a product as a function of 𝑥 times a function of 𝑦 we know
𝑋 and 𝑌 are independent.
Problem 59. Let 𝑋 and 𝑌 be two random variables and let 𝑟, 𝑠, 𝑡, and 𝑢 be real numbers.
(a) Show that Cov(𝑋+𝑠,𝑌 +𝑢) = Cov(𝑋, 𝑌 ).
(b) Show that Cov(𝑟𝑋,𝑡𝑌) = 𝑟𝑡Cov(𝑋,𝑌 ).
(c) Show that Cov(𝑟𝑋 + 𝑠, 𝑡𝑌 + 𝑢) = 𝑟𝑡Cov(𝑋,𝑌 ).
Solution: (a) First note by linearity of expectation we have 𝐸[𝑋 + 𝑠] = 𝐸[𝑋] + 𝑠, thus
𝑋 +𝑠−𝐸[𝑋 +𝑠] = 𝑋 −𝐸[𝑋].
Likewise 𝑌 +𝑢−𝐸[𝑌 +𝑢] = 𝑌 −𝐸[𝑌].
Now using the definition of covariance we get
Cov(𝑋+𝑠,𝑌 +𝑢) = 𝐸[(𝑋+𝑠−𝐸[𝑋+𝑠]) ⋅(𝑌 +𝑢−𝐸[𝑌 +𝑢])]
= 𝐸[(𝑋 − 𝐸[𝑋]) ⋅ (𝑌 − 𝐸[𝑌 ])]
= Cov(𝑋,𝑌 ).
(b) This is very similar to part (a).
We know 𝐸[𝑟𝑋] = 𝑟𝐸[𝑋], so 𝑟𝑋−𝐸[𝑟𝑋] = 𝑟(𝑋−𝐸[𝑋]). Likewise 𝑡𝑌 −𝐸[𝑡𝑌 ] = 𝑠(𝑌 −𝐸[𝑌 ]).
Once again using the definition of covariance we get
Cov(𝑟𝑋,𝑡𝑌) = 𝐸[(𝑟𝑋−𝐸[𝑟𝑋])(𝑡𝑌 −𝐸[𝑡𝑌])]
= 𝐸[𝑟𝑡(𝑋 − 𝐸[𝑋])(𝑌 − 𝐸[𝑌 ])]
(Now we use linearity of expectation to pull out the factor of 𝑟𝑡)
= 𝑟𝑡𝐸[(𝑋 − 𝐸[𝑋](𝑌 − 𝐸[𝑌 ]))]
= 𝑟𝑡Cov(𝑋,𝑌 )
(c) This is more of the same. We give the argument with far fewer algebraic details
Cov(𝑟𝑋 + 𝑠, 𝑡𝑌 + 𝑢) = Cov(𝑟𝑋,𝑡𝑌 ) (by part (a))
= 𝑟𝑡Cov(𝑋,𝑌 ) (by part (b))
Problem 60. Derive the formula for the covariance: Cov(𝑋,𝑌) = 𝐸[𝑋𝑌 ]−𝐸[𝑋]𝐸[𝑌].
Solution: Using linearity of expectation, we have
Cov(𝑋,𝑌) = 𝐸[(𝑋−𝐸[𝑋])(𝑌 −𝐸[𝑌])]
= 𝐸 [𝑋𝑌 − 𝐸[𝑋]𝑌 − 𝐸[𝑌 ]𝑋 + 𝐸[𝑋]𝐸[𝑌 ]]
= 𝐸[𝑋𝑌 ] − 𝐸[𝑋]𝐸[𝑌 ] − 𝐸[𝑌 ]𝐸[𝑋] + 𝐸[𝑋]𝐸[𝑌 ]
= 𝐸[𝑋𝑌 ] − 𝐸[𝑋]𝐸[𝑌 ].
Problem 61. (Arithmetic Puzzle)
Practice Exam 1: All Questions, Spring 2022 29
The joint and marginal pmf’s of 𝑋 and 𝑌 are partly given in the following table.
\𝑌 1 2 3
𝑋
1 1/6 0 … 1/3
2 … 1/4 … 1/3
3 … … 1/4 …
1/6 1/3 … 1
(a) Complete the table.
(b) Are 𝑋 and 𝑌 independent?
Solution: (a) The marginal probabilities have to add up to 1, so the two missing marginal
probabilities can be computed: 𝑃(𝑋 = 3) = 1/3, 𝑃(𝑌 = 3) = 1/2. Now each row and
column has to add up to its respective margin. For example, 1/6+0+𝑃(𝑋 = 1,𝑌 = 3) =
1/3, so 𝑃(𝑋 = 1,𝑌 = 3) = 1/6. Here is the completed table.
\𝑌 1 2 3
𝑋
1 1/6 0 1/6 1/3
2 0 1/4 1/12 1/3
3 0 1/12 1/4 1/3
1/6 1/3 1/2 1
(b) No, 𝑋 and 𝑌 are not independent.
For example, 𝑃(𝑋 = 2,𝑌 = 1) = 0 ≠ 𝑃(𝑋 = 2)⋅𝑃(𝑌 = 1).
Problem 62. (Simple Joint Probability)
Let 𝑋 and 𝑌 each have range {1,2,3,4}. The following formula gives their joint pmf
𝑖 + 𝑗
𝑃(𝑋 = 𝑖,𝑌 = 𝑗) =
80
Compute each of the following:
(a) 𝑃(𝑋 = 𝑌).
(b) 𝑃 (𝑋𝑌 = 6).
(c) 𝑃(1 ≤ 𝑋 ≤ 2, 2 < 𝑌 ≤ 4).
Solution: First we’ll make the table for the joint pmf. Then we’ll be able to answer the
questions by summing up entries in the table.
\𝑌 1 2 3 4
𝑋
1 2/80 3/80 4/80 5/80
2 3/80 4/80 5/80 6/80
3 4/80 5/80 6/80 7/80
4 5/80 6/80 7/80 8/80
(a) 𝑃(𝑋 = 𝑌) = 𝑝(1,1)+𝑝(2,2)+𝑝(3,3)+𝑝(4,4) = 20/80 = 1/4.
(b) 𝑃(𝑋𝑌 = 6) = 𝑝(2,3)+𝑝(3,2) = 10/80 = 1/8.
Practice Exam 1: All Questions, Spring 2022 30
(c) 𝑃(1 ≤ 𝑋 ≤ 2,2 < 𝑌 ≤ 4) = sum of 4 orange probabilities in the upper right corner of
the table = 20/80 = 1/4.
Problem 63. Toss a fair coin 3 times. Let 𝑋 = the number of heads on the first toss, 𝑌
the total number of heads on the last two tosses, and 𝐹 the number of heads on the first two
tosses.
(a) Give the joint probability table for 𝑋 and 𝑌 . Compute Cov(𝑋,𝑌 ).
Solution: (a) 𝑋 and 𝑌 are independent, so the table is computed from the product of the
known marginal probabilities. Since they are independent, Cov(𝑋,𝑌) = 0.
\𝑋 0 1 𝑃
𝑌 𝑌
0 1/8 1/8 1/4
1 1/4 1/4 1/2
2 1/8 1/8 1/4
𝑃 1/2 1/2 1
𝑋
(b) Give the joint probability table for 𝑋 and 𝐹 . Compute Cov(𝑋, 𝐹 ).
Solution: (b) The sample space is Ω = {HHH, HHT, HTH, HTT, THH, THT, TTH,
TTT}.
𝑃(𝑋 = 0,𝐹 = 0) = 𝑃({𝑇𝑇𝐻,𝑇𝑇𝑇}) = 1/4.
𝑃(𝑋 = 0,𝐹 = 1) = 𝑃({𝑇𝐻𝐻,𝑇𝐻𝑇}) = 1/4. \𝑋 0 1 𝑃
𝐹 𝐹
𝑃(𝑋 = 0,𝐹 = 2) = 0. 0 1/4 0 1/4
𝑃(𝑋 = 1,𝐹 = 0) = 0. 1 1/4 1/4 1/2
2 0 1/4 1/4
𝑃(𝑋 = 1,𝐹 = 1) = 𝑃({𝐻𝑇𝐻,𝐻𝑇𝑇}) = 1/4.
𝑃 1/2 1/2 1
𝑃(𝑋 = 1,𝐹 = 2) = 𝑃({𝐻𝐻𝐻,𝐻𝐻𝑇}) = 1/4. 𝑋
Cov(𝑋,𝐹) = 𝐸[𝑋𝐹 ]−𝐸[𝑋]𝐸[𝐹].
𝐸[𝑋] = 1/2, 𝐸[𝐹] = 1, 𝐸[𝑋𝐹 ] = ∑𝑥 𝑦 𝑝(𝑥 ,𝑦 ) = 3/4.
𝑖 𝑗 𝑖 𝑗
⇒ Cov(𝑋,𝐹) = 3/4−1/2 = 1/4.
Problem 64. Covariance and Independence
Let 𝑋 be a random variable that takes values -2, -1, 0, 1, 2; each with probability 1/5. Let
𝑌 = 𝑋2.
(a) Fill out the following table giving the joint frequency function for 𝑋 and 𝑌 . Be sure to
include the marginal probabilities.
𝑋 -2 -1 0 1 2 total
𝑌
0
1
4
total
Solution:
Practice Exam 1: All Questions, Spring 2022 31
𝑋 -2 -1 0 1 2
𝑌
0 0 0 1/5 0 0 1/5
1 0 1/5 0 1/5 0 2/5
4 1/5 0 0 0 1/5 2/5
1/5 1/5 1/5 1/5 1/5 1
Each column has only one nonzero value. For example, when 𝑋 = −2 then 𝑌 = 4, so in
the 𝑋 = −2 column, only 𝑃(𝑋 = −2,𝑌 = 4) is not 0.
(b) Find 𝐸[𝑋] and 𝐸[𝑌 ].
Solution: Using the marginal distributions: 𝐸[𝑋] = 1(−2−1+0+1+2) = 0.
5
1 2 2
𝐸[𝑌] = 0⋅ +1 ⋅ +4 ⋅ = 2.
5 5 5
(c) Show 𝑋 and 𝑌 are not independent.
Solution: We show the probabilities don’t multiply:
𝑃(𝑋 = −2, 𝑌 = 0) = 0 ≠ 𝑃(𝑋 = −2)⋅𝑃(𝑌 = 0) = 1/25.
Since these are not equal 𝑋 and 𝑌 are not independent. (It is obvious that 𝑋2 is not
independent of 𝑋.)
(d) Show Cov(𝑋,𝑌) = 0.
This is an example of uncorrelated but non-independent random variables. The reason this
can happen is that correlation only measures the linear dependence between the two variables.
In this case, 𝑋 and 𝑌 are not at all linearly related.
Solution: Using the table from part (a) and the means computed in part (d) we get:
Cov(𝑋,𝑌) = 𝐸[𝑋𝑌 ]−𝐸[𝑋]𝐸[𝑌]
1 1 1 1 1
= (−2)(4) + (−1)(1) + (0)(0) + (1)(1) + (2)(4)
5 5 5 5 5
= 0.
Problem 65. Continuous Joint Distributions
Suppose 𝑋 and 𝑌 are continuous random variables with joint density function 𝑓(𝑥,𝑦) = 𝑥+𝑦
on the unit square [0,1] × [0,1].
(a) Let 𝐹 (𝑥, 𝑦) be the joint CDF. Compute 𝐹 (1, 1). Compute 𝐹 (𝑥, 𝑦).
𝑎 𝑏
Solution: 𝐹(𝑎,𝑏) = 𝑃(𝑋 ≤ 𝑎,𝑌 ≤ 𝑏) = ∫ ∫ (𝑥+𝑦)𝑑𝑦𝑑𝑥.
0 0
𝑦2
𝑏
𝑏2
Inner integral: 𝑥𝑦+ ∣ = 𝑥𝑏+ .
2 2
0
𝑥2 𝑏2
𝑎
𝑎2𝑏 + 𝑎𝑏2
Outer integral: 𝑏 + 𝑥∣ = .
2 2 2
0
𝑥2𝑦 + 𝑥𝑦2
So 𝐹 (𝑥, 𝑦) = and 𝐹(1,1) = 1.
2
Practice Exam 1: All Questions, Spring 2022 32
(b) Compute the marginal densities for 𝑋 and 𝑌 .
1 1 𝑦2 1 1
Solution: 𝑓 (𝑥) = ∫ 𝑓(𝑥,𝑦)𝑑𝑦 = ∫ (𝑥+𝑦)𝑑𝑦 = 𝑥𝑦+ ∣ = 𝑥+ .
𝑋 2 2
0 0 0
By symmetry, 𝑓 (𝑦) = 𝑦 + 1/2.
𝑌
(c) Are 𝑋 and 𝑌 independent?
Solution: To see if they are independent we check if the joint density is the product of the
marginal densities.
𝑓(𝑥,𝑦) = 𝑥+𝑦, 𝑓 (𝑥)⋅𝑓 (𝑦) = (𝑥+1/2)(𝑦+1/2).
𝑋 𝑌
Since these are not equal, 𝑋 and 𝑌 are not independent.
(d) Compute 𝐸[𝑋], 𝐸[𝑌 ], 𝐸[𝑋2 + 𝑌 2], Cov(𝑋,𝑌 ).
1 1 1 𝑦2 1 1 𝑥 7
Solution: 𝐸[𝑋] = ∫ ∫ 𝑥(𝑥+𝑦)𝑑𝑦𝑑𝑥 = ∫ [𝑥2𝑦+𝑥 ∣ ] 𝑑𝑥 = ∫ 𝑥2+ 𝑑𝑥 = .
2 2 12
0 0 0 0 0
1 1
(Or, using (b), 𝐸[𝑋] = ∫ 𝑥𝑓 (𝑥)𝑑𝑥 = ∫ 𝑥(𝑥+1/2)𝑑𝑥 = 7/12.)
𝑋
0 0
By symmetry 𝐸[𝑌 ] = 7/12.
1 1 5
𝐸[𝑋2+𝑌 2] = ∫ ∫ (𝑥2+𝑦2)(𝑥+𝑦)𝑑𝑦𝑑𝑥 = .
6
0 0
1 1 1
𝐸[𝑋𝑌 ] = ∫ ∫ 𝑥𝑦(𝑥+𝑦)𝑑𝑦𝑑𝑥 = .
3
0 0
1 49 1
Cov(𝑋,𝑌) = 𝐸[𝑋𝑌 ]−𝐸[𝑋]𝐸[𝑌] = − = − .
3 144 144
Problem 66. Correlation
Flip a coin 3 times. Use a joint pmf table to compute the covariance and correlation between
the number of heads on the first 2 and the number of heads on the last 2 flips.
Solution: Let 𝑋 = the number of heads on the first 2 flips and 𝑌 the number in the last
2. Considering all 8 possibe tosses: 𝐻𝐻𝐻, 𝐻𝐻𝑇 etc we get the following joint pmf for 𝑋
and 𝑌
𝑌 /𝑋 0 1 2
0 1/8 1/8 0 1/4
1 1/8 1/4 1/8 1/2
2 0 1/8 1/8 1/4
1/4 1/2 1/4 1
Using the table we find
1 1 1 1 5
𝐸[𝑋𝑌 ] = +2 +2 +4 = .
4 8 8 8 4
We know 𝐸[𝑋] = 1 = 𝐸[𝑌 ] so
5 1
Cov(𝑋,𝑌) = 𝐸[𝑋𝑌 ]−𝐸[𝑋]𝐸[𝑌] = −1 = .
4 4
Practice Exam 1: All Questions, Spring 2022 33
Since 𝑋 is the sum of 2 independent Bernoulli(0.5) we have 𝜎 = √2/4
𝑋
Cov(𝑋,𝑌) 1/4 1
Cor(𝑋,𝑌) = = = .
𝜎 𝜎 (2)/4 2
𝑋 𝑌
Problem 67. Correlation
Flip a coin 5 times. Use properties of covariance to compute the covariance and correlation
between the number of heads on the first 3 and last 3 flips.
Solution: As usual let 𝑋 = the number of heads on the 𝑖th flip, i.e. 0 or 1.
𝑖
Let 𝑋 = 𝑋 +𝑋 +𝑋 the sum of the first 3 flips and 𝑌 = 𝑋 +𝑋 +𝑋 the sum of the
1 2 3 3 4 5
last 3. Using the algebraic properties of covariance we have
Cov(𝑋,𝑌) = Cov(𝑋 + 𝑋 + 𝑋 , 𝑋 + 𝑋 + 𝑋 )
1 2 3 3 4 5
= Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 )
1 3 1 4 1 5
+ Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 )
2 3 2 4 2 5
+ Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 )
3 3 3 4 3 5
1
Because the 𝑋 are independent the only non-zero term in the above sum is Cov(𝑋 𝑋 ) = Var(𝑋 ) =
𝑖 3 3 3 4
Therefore, Cov(𝑋,𝑌) = 1.
4
We get the correlation by dividing by the standard deviations. Since 𝑋 is the sum of 3
independent Bernoulli(0.5) we have 𝜎 = √3/4
𝑋
Cov(𝑋,𝑌) 1/4 1
Cor(𝑋,𝑌) = = = .
𝜎 𝜎 (3)/4 3
𝑋 𝑌
8 Law of Large Numbers, Central Limit Theorem
Problem 68. (Table of normal probabilities)
Use the table of standard normal probabilities to compute the following. (𝑍 is the standard
normal.)
(a) (i) 𝑃 (𝑍 ≤ 1.5) (ii) 𝑃 (−1.5 < 𝑍 < 1.5) 𝑃 (𝑍 > −0.75).
(b) Suppose 𝑋 ∼ N(2, (0.5)2). Find (i) 𝑃(𝑋 ≤ 2) (ii) 𝑃(1 < 𝑋 ≤ 1.75).
Solution: (a) (i) 0.9332 (ii) 0.9332 - 0.0668 = 0.8664
(iii) By symmetry = 𝑃 (𝑍 < 0.75) = 0.7734. (Or we could have used 1 − 𝑃 (𝑍 > −0.75.))
(b) (i) Since 2 is the mean of the normal distribution, 𝑃(𝑋 ≤ 2) = 0.5.
(ii) Standardizing,
1−2 1.75−2
𝑃(1 < 𝑋 ≤ 1.75) = 𝑃 ( < 𝑍 ≤ ) = 𝑃(−2 < 𝑍 < −0.5) = 0.3085−0.0228 = 0.2857 .
0.5 0.5
Problem 69. Suppose 𝑋 , … , 𝑋 are i.i.d. with mean 1/5 and variance 1/9. Use the
1 100
central limit theorem to estimate 𝑃 (∑ 𝑋 < 30).
𝑖
Practice Exam 1: All Questions, Spring 2022 34
Solution: Standardize:
∑𝑋 −𝜇 30 − 𝑛𝜇
𝑃 (∑ 𝑋 < 30) = 𝑃 ( √𝑖 < √ )
𝑖 𝑛𝜎 𝑛𝜎
𝑖
30−20
≈ 𝑃 (𝑍 < ) (by the central limit theorem)
10/3
= 𝑃(𝑍 < 3)
= 0.9987 (from the table of normal probabilities)
Problem 70. All or None
You have $100 and, never mind why, you must convert it to $1000. Anything less is no
good. Your only way to make money is to gamble for it. Your chance of winning one bet is
𝑝.
Here are two extreme strategies:
Maximum strategy: bet as much as you can each time. To be smart, if you have less than
$500 you bet it all. If you have more, you bet enough to get to $1000.
Minimum strategy: bet $1 each time.
If 𝑝 < 0.5 (the odds are against you) which is the better strategy?
What about 𝑝 > 0.5?
Solution: If 𝑝 < 0.5 your expected winnings on any bet is negative, if 𝑝 = 0.5 it is 0, and
if 𝑝 > 0.5 is is positive. By making a lot of bets the minimum strategy will ’win’ you close
to the expected average. So if 𝑝 ≤ 0.5 you should use the maximum strategy and if 𝑝 > 0.5
you should use the minumum strategy.
Problem 71. (Central Limit Theorem)
Let 𝑋 , 𝑋 , … , 𝑋 be i.i.d., each with expected value 𝜇 = 𝐸[𝑋 ] = 5, and variance 𝜎2 =
1 2 81 𝑖
Var(𝑋 ) = 4. Approximate 𝑃(𝑋 +𝑋 +⋯𝑋 > 369), using the central limit theorem.
𝑖 1 2 81
Solution: Let 𝑇 = 𝑋 +𝑋 +…+𝑋 . The central limit theorem says that
1 2 81
𝑇 ≈ N(81∗5,81∗4) = N(405, 182)
Standardizing we have
𝑇 −405 369 − 405
𝑃(𝑇 > 369) = 𝑃 ( > )
18 18
≈ 𝑃 (𝑍 > −2)
≈ 0.975
The value of 0.975 comes from the rule-of-thumb that 𝑃(|𝑍| < 2) ≈ 0.95. A more exact
value (using R) is 𝑃 (𝑍 > −2) ≈ 0.9772.
Problem 72. (Binomial ≈ normal)
Let 𝑋 ∼ binomial(100,1/3).
An ‘exact’ computation in R gives 𝑃 (𝑋 ≤ 30) = 0.2765539. Use the central limit theorem
to give an approximation of 𝑃(𝑋 ≤ 30)
Practice Exam 1: All Questions, Spring 2022 35
Solution: 𝑋 ∼ binomial(100, 1/3) means 𝑋 is the sum of 100 i.i.d. Bernoulli(1/3) random
variables 𝑋 .
𝑖
We know 𝐸[𝑋 ] = 1/3 and Var(𝑋 ) = (1/3)(2/3) = 2/9. Therefore the central limit theorem
𝑖 𝑖
says
𝑋 ≈ N(100/3, 200/9)
Standardization then gives
𝑋−100/3 30 − 100/3
𝑃(𝑋 ≤ 30) = 𝑃 ( ≤ ) ≈ 𝑃(𝑍 ≤ −0.7071068) ≈ 0.239751
√200/9 √200/9
We used R to do these calculations The approximation agrees with the ‘exact’ number to 2
decimal places.
Problem 73. (More Central Limit Theorem)
The average IQ in a population is 100 with standard deviation 15 (by definition, IQ is
normalized so this is the case). What is the probability that a randomly selected group of
100 people has an average IQ above 115?
Solution: Let 𝑋 be the IQ of a randomly selected person. We are given 𝐸[𝑋 ] = 100 and
𝑗 𝑗
𝜎 = 15.
𝑋
𝑗
Let 𝑋 be the average of the IQ’s of 100 randomly selected people. Then we know
√
𝐸[𝑋] = 100 and 𝜎 = 15/ 100 = 1.5.
𝑋
The problem asks for 𝑃 (𝑋 > 115). Standardizing we get 𝑃(𝑋 > 115) ≈ 𝑃(𝑍 > 10).
This is effectively 0.
Problem 74. Hospitals (binomial, CLT, etc)
• A certain town is served by two hospitals.
• Larger hospital: about 45 babies born each day.
• Smaller hospital about 15 babies born each day.
• For a period of 1 year, each hospital recorded the days on which more than 60% of the
babies born were boys.
(a) Which hospital do you think recorded more such days?
(i) The larger hospital.
(ii) The smaller hospital.
(iii) About the same (that is, within 5% of each other).
(b) Let 𝐿 (resp., 𝑆 ) be the Bernoulli random variable which takes the value 1 if more
𝑖 𝑖
than 60% of the babies born in the larger (resp., smaller) hospital on the 𝑖th day were boys.
Determine the distribution of 𝐿 and of 𝑆 .
𝑖 𝑖
Practice Exam 1: All Questions, Spring 2022 36
(c) Let 𝐿 (resp., 𝑆) be the number of days on which more than 60% of the babies born in
the larger (resp., smaller) hospital were boys. What type of distribution do 𝐿 and 𝑆 have?
Compute the expected value and variance in each case.
(d) Via the CLT, approximate the 0.84 quantile of 𝐿 (resp., 𝑆). Would you like to revise
your answer to part (a)?
(e) What is the correlation of 𝐿 and 𝑆? What is the joint pmf of 𝐿 and 𝑆? Visualize the
region corresponding to the event 𝐿 > 𝑆. Express 𝑃(𝐿 > 𝑆) as a double sum.
(a) Solution: When this question was asked in a study, the number of undergraduates
who chose each option was 21, 21, and 55, respectively. This shows a lack of intuition for
the relevance of sample size on deviation from the true mean (i.e., variance).
(b) Solution: The random variable 𝑋 , giving the number of boys born in the larger
𝐿
hospital on day 𝑖, is governed by a Bin(45, 0.5) distribution. So 𝐿 has a Ber(𝑝 ) distribution
𝑖 𝐿
with
45
45
𝑝 = 𝑃(𝑋 > 27) = ∑ ( )0.545 ≈ 0.068
𝐿 𝑘
𝑘=28
Similarly, the random variable 𝑋 , giving the number of boys born in the smaller hospital
𝑆
on day 𝑖, is governed by a Bin(15, 0.5) distribution. So 𝑆 has a Ber(𝑝 ) distribution with
𝑖 𝑆
15
15
𝑝 = 𝑃(𝑋 > 9) = ∑ ( )0.515 ≈ 0.151
𝑆 𝑆 𝑘
𝑘=10
We see that 𝑝 is indeed greater than 𝑝 , consistent with (𝑖𝑖).
𝑆 𝐿
365 365
(c) Solution: Note that 𝐿 = ∑ 𝐿 and 𝑆 = ∑ 𝑆 . So 𝐿 has a Bin(365, 𝑝 ) distribu-
𝑖=1 𝑖 𝑖=1 𝑖 𝐿
tion and 𝑆 has a Bin(365, 𝑝 ) distribution. Thus
𝑆
𝐸[𝐿] = 365𝑝 ≈ 25
𝐿
𝐸[𝑆] = 365𝑝 ≈ 55
𝑆
Var(𝐿) = 365𝑝 (1 − 𝑝 ) ≈ 23
𝐿 𝐿
Var(𝑆) = 365𝑝 (1 − 𝑝 ) ≈ 47
𝑆 𝑆
(d) Solution: mean + sd in each case:
√
For 𝐿, 𝑞 ≈ 25 + 23.
0.84
√
For 𝑆, 𝑞 ≈ 55 + 47.
0.84
(e) Since 𝐿 and 𝑆 are independent, their joint distribution is determined by multiplying
their individual distributions. Both 𝐿 and 𝑆 are binomial with 𝑛 = 365 and 𝑝 and 𝑝
𝐿 𝑆
computed above. Thus
365 365
𝑝 𝑃 (𝐿 = 𝑖 and 𝑆 = 𝑗) = 𝑝(𝑖,𝑗) = ( )𝑝𝑖 (1−𝑝 )365−𝑖( )𝑝𝑗 (1−𝑝 )365−𝑗
𝑙,𝑠 𝑖 𝐿 𝐿 𝑗 𝑆 𝑆
Thus
364 365
𝑃(𝐿 > 𝑆) = ∑ ∑ 𝑝(𝑖,𝑗) ≈ 0.0000916
𝑖=0 𝑗=𝑖+1
(We used R to do the computations.)
Practice Exam 1: All Questions, Spring 2022 37
9 R Problems
R will not be on the exam. However, these problems will help you understand the concepts
we’ve been studying.
Problem 75. R simulation
Consider 𝑋 , 𝑋 , …all independent and with distribution N(0, 1). Let 𝑋 be the average of
1 2 𝑚
𝑋 , …𝑋 .
1 𝑛
(a) Give 𝐸[𝑋 ] and 𝜎 exactly.
𝑛 𝑋
𝑛
Solution: 𝐸[𝑋 ] = 0 ⇒ 𝐸[𝑋 ] = 0.
𝑗 𝑛
𝑋 +…+𝑋 1 1
Var(𝑋 ) = 1 ⇒ Var ( 1 𝑛 ) = ⇒ 𝜎 = √ .
𝑗 𝑛 𝑛 𝑋 𝑛 𝑛
(b) Use a R simulation to estimate 𝐸[𝑋 ] and Var(𝑋 ) for 𝑛 = 1,9,100. (You should use
𝑛 𝑛
the rnorm function to simulate 1000 samples of each 𝑋 .)
𝑗
Solution: Here’s my R code:
x = rnorm(100*1000,0,1)
data = matrix(x, nrow=100, ncol=1000)
data1 = data[1,]
m1 = mean(data1)
v1 = var(data1)
data9 = colMeans(data[1:9,])
m9 = mean(data9)
v9 = var(data9)
data100 = colMeans(data)
m100 = mean(data100)
v100 = var(data100)
#display the results
print(m1)
print(v1)
print(m9)
print(v9)
print(m100)
print(v100)
∑ 𝑥 ∑ 𝑥
Note if 𝑥 = [𝑥 , 𝑥 , … , 𝑥 ] then var(x) actually computes 𝑘 instead of 𝑘 . There is
1 2 𝑛 𝑛 − 1 𝑛
a good reason for this which we will learn in the statistics part of the class. For now, it’s
enough to note that if 𝑛 = 1000 the using 𝑛 or 𝑛 − 1 won’t make much difference.
Problem 76. R Exercise
Let 𝑋 , 𝑋 , 𝑋 , 𝑋 , 𝑋 be independent 𝑈(0, 1) random variables.
1 2 3 4 5
Let 𝑋 = 𝑋 +𝑋 +𝑋 and 𝑌 = 𝑋 +𝑋 +𝑋 .
1 2 3 3 4 5
Use the runif() function to simulate 1000 trials of each of these variables. Use these to
estimate Cov(𝑋, 𝑌 ).
Solution: a = runif(5*1000,0,1)
Practice Exam 1: All Questions, Spring 2022 38
data = matrix(a,5,1000)
x = colSums(data[1:3,])
y = colSums(data[3:5,])
print(cov(x,y))
Extra Credit
Compute this covariance exactly.
Solution: Method 1 (Algebra)
First, if 𝑖 ≠ 𝑗 we know 𝑋 and 𝑋 are independent, so Cov(𝑋 , 𝑋 ) = 0.
𝑖 𝑗 𝑖 𝑗
Cov(𝑋,𝑌) = Cov(𝑋 + 𝑋 + 𝑋 , 𝑋 + 𝑋 + 𝑋 )
1 2 3 3 4 5
= Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 )
1 3 1 4 1 5
+ Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 )
2 3 2 4 2 5
+ Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 )
3 3 3 4 3 5
(most of these terms are 0)
= Cov(𝑋 , 𝑋 )
3 3
= Var(𝑋 )
3
1
= (known variance of a uniform(0,1) distribution)
12
Method 2 (Multivariable calculus)
In 5 dimensional space we have the joint distribution
𝑓(𝑥 ,𝑥 ,𝑥 ,𝑥 ,𝑥 ) = 1.
1 2 3 4 5
Computing directly
1 1 1 1 1
𝐸[𝑋] = 𝐸[𝑋 +𝑋 +𝑋 ] = ∫ ∫ ∫ ∫ ∫ (𝑥 +𝑥 +𝑥 )𝑑𝑥 𝑑𝑥 𝑑𝑥 ,𝑑𝑥 𝑑𝑥
1 2 3 1 2 3 1 2 3 4 5
0 0 0 0 0
1
first integral = +𝑥 +𝑥
2 2 3
1 1
second integral = + +𝑥 = 1+𝑥
2 2 3 3
3
third integral =
2
3
fourth integral =
2
3
fifth integral =
2
So, 𝐸[𝑋] = 3/2, likewise 𝐸[𝑌 ] = 3/2.
1 1 1 1 1
𝐸[𝑋𝑌 ] = ∫ ∫ ∫ ∫ ∫ (𝑥 +𝑥 +𝑥 )(𝑥 +𝑥 +𝑥 )𝑑𝑥 𝑑𝑥 𝑑𝑥 𝑑𝑥 𝑑𝑥
1 2 3 3 4 5 1 2 3 4 5
0 0 0 0 0
= 7/3.
Cov(𝑋,𝑌) = 𝐸[𝑋𝑌 ]−𝐸[𝑋]𝐸[𝑌] = 1 = 0.08333.
12
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
