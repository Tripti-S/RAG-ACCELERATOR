# Mit18 05 S22 Prac Exam01B Sol

---

Exam 1 Practice Questions II –solutions, 18.05, Spring 2022
Notes.
Not every possible question be covered in 11 problems. Look at the other review problems
as well as the readings, psets and class problems.
Even the first 11 problems are much longer than the actual test will be,
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
Problem 2. Let 𝐶 and 𝐷 be two events with 𝑃(𝐶) = 0.25, 𝑃 (𝐷) = 0.45, and 𝑃(𝐶 ∩𝐷) =
0.1. What is 𝑃(𝐶𝑐 ∩𝐷)?
Solution: 𝐷 is the disjoint union of 𝐷 ∩ 𝐶 and 𝐷 ∩ 𝐶𝑐.
𝐶 𝐷
So, 𝑃(𝐷 ∩ 𝐶)+𝑃(𝐷 ∩ 𝐶𝑐) = 𝑃(𝐷) 𝐷∩𝐶𝑐
⇒ 𝑃(𝐷 ∩ 𝐶𝑐) = 𝑃(𝐷)−𝑃(𝐷 ∩ 𝐶) = 0.45−0.1 = 0.35.
0.1 0.45−0.1
(We never use 𝑃(𝐶) = 0.25.)
Problem 3. Corrupted by their power, the judges running the popular game show America’s
Next Top Mathematician have been taking bribes from many of the contestants. Each
episode, a given contestant is either allowed to stay on the show or is kicked off.
If the contestant has been bribing the judges they will be allowed to stay with probability 1.
If the contestant has not been bribing the judges, they will be allowed to stay with probability
1/3.
1
Exam 1 Practice II, Spring 2022 2
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
𝑃 (𝐵) 1/4 1
We therefore have (by Bayes’ rule) 𝑃 (𝐵|𝑆 ) = 𝑃 (𝑆 |𝐵) = 1 ⋅ = .
1 1 𝑃(𝑆 ) 1/2 2
1
(b) Using the tree we have the total probability of 𝑆 is
2
1 3 1 1 1
𝑃(𝑆 ) = + ⋅ ⋅ =
2 4 4 3 3 3
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
Exam 1 Practice II, Spring 2022 3
1/6 1
Therefore 𝑃 (𝐿 |𝑆 ) = = .
2 1 1/2 3
Problem 4. Suppose now that events 𝐴, 𝐵 and 𝐶 are mutually independent with
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
Problem 5. Suppose 𝑋 is a random variable with 𝐸[𝑋] = 5 and Var(𝑋) = 2. What is
𝐸[𝑋2]?
Solution: Use Var(𝑋) = 𝐸[𝑋2] − 𝐸[𝑋]2 ⇒ 2 = 𝐸[𝑋2] − 25 ⇒ 𝐸[𝑋2] = 27.
Problem 6. (a) Suppose that 𝑋 has probability density function 𝑓 (𝑥) = 𝜆e−𝜆𝑥 for 𝑥 ≥ 0.
𝑋
Compute the cdf, 𝐹 (𝑥).
𝑋
(b) If 𝑌 = 𝑋2, compute the pdf and cdf of 𝑌 .
(a) Solution: We have cdf of 𝑋,
𝑥
𝐹 (𝑥) = ∫ 𝜆e−𝜆𝑥𝑑𝑥 = 1 − e−𝜆𝑥.
𝑋
0
Exam 1 Practice II, Spring 2022 4
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
Problem 7. For each of the following say whether it can be the graph of a cdf. If it can
be, say whether the variable is discrete or continuous.
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
Problem 8. Compute the median for the exponential distribution with parameter 𝜆.
Solution: The density for this distribution is 𝑓(𝑥) = 𝜆 e−𝜆𝑥. We know (or can compute)
that the distribution function is 𝐹(𝑎) = 1− e−𝜆𝑎. The median is the value of 𝑎 such that
𝐹 (𝑎) = 0.5. Thus, 1− e−𝜆𝑎 = 0.5 ⇒ 0.5 = e−𝜆𝑎 ⇒ log(0.5) = −𝜆𝑎 ⇒ 𝑎 = log(2)/𝜆.
Problem 9. (Another Arithmetic Puzzle)
Let 𝑋 and 𝑌 be two independent Bernoulli(0.5) random variables. Define 𝑆 and 𝑇 by:
𝑆 = 𝑋+𝑌 and 𝑇 = 𝑋−𝑌.
(a) Find the joint and marginal pmf’s for 𝑆 and 𝑇 .
Exam 1 Practice II, Spring 2022 5
(b) Are 𝑆 and 𝑇 independent.
Solution: (a) 𝑆 = 𝑋+𝑌 takes values 0, 1, 2 and 𝑇 = 𝑋−𝑌 takes values -1, 0, 1.
First we make two tables: the joint probability table for 𝑋 and 𝑌 and a table given the values
(𝑆, 𝑇 ) corresponding to values of (𝑋,𝑌 ), e.g. (𝑋,𝑌) = (1,1) corresponds to (𝑆,𝑇) = (2,0).
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
Problem 10. Let 𝑋 and 𝑌 be two random variables and let 𝑟, 𝑠, 𝑡, and 𝑢 be real numbers.
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
Exam 1 Practice II, Spring 2022 6
(c) This is more of the same. We give the argument with far fewer algebraic details
Cov(𝑟𝑋 + 𝑠, 𝑡𝑌 + 𝑢) = Cov(𝑟𝑋,𝑡𝑌 ) (by part (a))
= 𝑟𝑡Cov(𝑋,𝑌 ) (by part (b))
Problem 11. (More Central Limit Theorem)
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
More problems
Problem 12. 20 politicians are having a tea party, 6 Democrats and 14 Republicans. To
prepare, they need to choose:
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
Exam 1 Practice II, Spring 2022 7
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
Problem 13. More cards! Suppose you want to divide a 52 card deck into four hands with
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
Problem 14. There is a screening test for prostate cancer that looks at the level of PSA
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
Exam 1 Practice II, Spring 2022 8
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
Problem 15. Let 𝑋 be a discrete random variable with pmf 𝑝 given by:
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
Problem 16. Suppose I play a gambling game with even odds. So, I can wager 𝑏 dollars
and I either win or lose 𝑏 dollars with probability 𝑝 = 0.5.
I employ the following strategy to try to guarantee that I win some money.
I bet $1; if I lose, I double my bet to $2, if I lose I double my bet again. I continue until
I win. Eventually I’m sure to win a bet and net $1 (run through the first few rounds and
you’ll see why this is the net).
If this really worked casinos would be out of business. Our goal in this problem is to
understand the flaw in the strategy.
Exam 1 Practice II, Spring 2022 9
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
Problem 17. Normal Distribution: Throughout these problems, let 𝜙 and Φ be the pdf
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
Solution: We have
2 2
𝑃(−1 ≤ 𝑋 ≤ 1) = 𝑃 (− ≤ 𝑍 ≤ 0) = Φ(0)−Φ(− ) ≈ 0.2475
3 3
(d) Recall that the probability that 𝑍 is within one standard deviation of its mean is approx-
imately 68%. What is the probability that 𝑋 is within one standard deviation of its mean?
Exam 1 Practice II, Spring 2022 10
Solution: Since 𝐸[𝑋] = 1, Var(𝑋) = 9, we want 𝑃(−2 ≤ 𝑋 ≤ 4). We have
𝑃(−2 ≤ 𝑋 ≤ 4) = 𝑃(−3 ≤ 3𝑍 ≤ 3) = 𝑃(−1 ≤ 𝑍 ≤ 1) ≈ 0.68.
Problem 18. Toss a fair coin 3 times. Let 𝑋 = the number of heads on the first toss, 𝑌
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
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
