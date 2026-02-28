# Mit18 05 S22 Pset08 Sol

---

18.05 Problem Set 8, Spring 2022 Solutions
Problem 1. (35: 5,5,5,5,5,5,5 pts.) (Confident coin: III)
When spun on edge 250 times a certain coin came up heads 140 times and tails 110. We
can make the statement: ‘if the coin is unbiased then the probability of getting a result at
least this extreme is 7%.’
(a) Let 𝜃 be the probability of coming up heads. Consider the null hypothesis that the coin
is fair, 𝐻 ∶ 𝜃 = 0.5. Carefully explain how the 7% figure arises. What term describes this
0
value in NHST? Does it correspond to a one-sided or two-sided test?
Solution: 𝐻 : 𝜃 = 0.5
0
Test statistic: 𝑥 = number of heads in 250 spins.
Data: 𝑥 = 140.
The probability of geting a result at least as extreme as seen is the 𝑝-value.
We’ll show how to compute this value and decide if the test is one or two-sided at the same
time.
A one-sided test would have alternative hypothesis 𝐻 : 𝜃 > 0.5. In this case, data at least
𝐴
as extreme means 𝑥 ≥ 140. Using R we compute the one-sided 𝑝-value:
𝑝 = 𝑃(𝑥 ≥ 140 |𝐻 ) = 1 - pbinom(139, 250, 0.5) = 0.03321
0
This is not the 7% value we were looking for. So let’s consider the two-sided test.
A two-sided test would have alternate hypothesis 𝐻 : 𝜃 ≠ 0.5. Since the null distribution,
𝐴
binomial(250,0.5), is symmetric around 0, each tail in the rejection region will have proba-
bility 𝛼/2 and the two-sided 𝑝-value is computed by doubling the smaller of the one-sided
𝑝-values. We computed the right tail 𝑝-value just above. This is the smaller of the two
𝑝-values so our two-sided 𝑝-value is 2×0.03321 = 0.06642. This rounds to 0.07, so the figure
of 7% is the two-sided 𝑝-value.
Note: We could have used the normal approximation binomial(250, 0.5) ≈ N(125, 250/4),
and the 𝑧-statistic 𝑧 = 𝑥−125 ≈ N(0, 1). In this case, our 𝑝-values would be: one-sided:
√250/4
15 15
𝑝 = 𝑃(𝑧 ≥ ) ≈ 0.02889 and two-sided: 𝑝 = 𝑃(|𝑧| ≥ ) ≈ 0.05778.
√250/4 √250/4
(b) Would you reject 𝐻 at a significance level of 𝛼 = 0.1? What about 𝛼 = 0.05? (For
0
this problem assume the test has the same sidedness as the one used to get the 7% 𝑝-value
in part (a).)
Solution: As instructed, we use a two-sided rejection region as in part (a). The exact
𝑝-value was 𝑝 = 0.066. Since 0.05 < 𝑝 < 0.1 we reject 𝐻 at significance 𝛼 = 0.1 and don’t
0
reject at 𝛼 = 0.05.
1
18.05 Problem Set 8, Spring 2022 Solutions 2
80 100 120 140 160 180
50.0
30.0
10.0
10.0−
x
borp
q = 0.5
The figure shows the null distribution, the 𝛼 = 0.1 rejection region (blue-green) and the
𝛼 = 0.05 rejection region (orange). Notice that the data 𝑥 = 140 is in the 0.1 rejection
region but not the 0.05 rejection region.
(c) How many heads would you need to have observed out of 250 spins to reject at a
significance of 𝛼 = 0.01? (Again assume the same sidedness as the test used to get the 7%
𝑝-value in part (a).)
Solution: Again, we use two-sided rejection region. The problem asks us to find the
rejection region for 𝛼 = 0.01. We use R to find the endpoints for the rejection region (called
critical values):
critical_value_left = qbinom(0.005,250,0.5) - 1 = 104
critical_value_right = qbinom(0.995,250,0.5) + 1 = 146
Note: we added or subtracted one to the value returned by qbinom. For a discrete distri-
bution like the binomial there is not an exact critical value. So qbinom(x, n, p) returns
the smallest integer with more than 𝑥 probability in its left tail. Since the rejection region
must have at most 𝛼/2 in either tail we have to move the R answer by one towards the tail.
Conclusion: we reject for greater than or equal to 146 heads or less than or equal to 104
heads.
(d) (i) Fix the significance level at 𝛼 = 0.05. Compute and compare the power of the test
for values of the alternative hypothesis 𝜃 = 0.55 and 𝜃 = 0.6? (Again assume the same
sidedeness as in part (a). Here, 𝐻 is composite, so the power is different for different
𝐴
values of the hypothesis.)
(ii) Sketch the pmf of each hypothesis and use it to explain the change in power observed in
part (i).
Solution: (i) Again we use a two-sided rejection region. For 𝛼 = 0.05 the rejection region
is given by the critical values
critical_value_left = qbinom(0.025,250,0.5) - 1 = 109
critical_value_right = qbinom(0.975,250,0.5) + 1 = 141
18.05 Problem Set 8, Spring 2022 Solutions 3
power when 𝜃 = 0.55 = 𝑃(reject | 𝜃 = 0.55)
= 𝑃 (𝑥 ≤ 109 or 𝑥 ≥ 141 |𝜃 = 0.55)
= sum(dbinom(0:109, 250, 0.55)) + sum(dbinom(141:250, 250,0.55)) = 0.35237
Likewise
power when 𝜃 = 0.6 = 𝑃(reject | 𝜃 = 0.6)
= 𝑃 (𝑥 ≤ 109 or 𝑥 ≥ 141 |𝜃 = 0.6)
= sum(dbinom(0:109, 250, 0.6)) + sum(dbinom(141:250, 250,0.6)) = 0.88963
Note: We could have used pbinom. Doing the sums with dbinom was an easy way of avoiding
off-by-one errors with pbinom.
(ii) The two plots below show the null distribution and the distribution of 𝐻 for 𝜃 = 0.55
𝐴
and 𝜃 = 0.6 The blue line below the graphs shows the rejection region. The greater power
when 𝜃 = 0.6 is explained by its greater separation from 𝐻 . Most of the probability of
0
𝑝(𝑥 | 𝜃 = 0.6) is over the right side of the rejection region.
80 100 120 140 160 180
50.0
30.0
10.0
10.0−
x
borp
q = 0.55
Distributions of 𝐻 and 𝐻 with 𝜃 = 0.55
0 𝐴
80 100 120 140 160 180
50.0
30.0
10.0
10.0−
x
borp
q = 0.6
Distributions of 𝐻 and 𝐻 with 𝜃 = 0.6
0 𝐴
18.05 Problem Set 8, Spring 2022 Solutions 4
(e) (i) Again fix 𝛼 = 0.05. What is the smallest number of spins necessary for the test to
have a power of 0.9 when 𝐻 ∶ 𝜃 = 0.55? (Again, use the sidedness from part (a).)
𝐴
(ii) As in part (d), draw sketches and explain how they illustrate the change in power.
Solution: The answer is 𝑛 = 1055 with 𝐻 giving a power of 0.9003.
𝐴
To get this we need to compute the power for various values of 𝑛. The steps for each 𝑛 are:
1. Find the rejection region.
2. Compute the power.
Here is the R-code for one value of 𝑛. We ran this code in a loop to check through all values
of 𝑛 until we found the first with power = 0.9. The full code is in mit18_05_s22_ps8_sol.r,
which is posted in the usual place.
theta = 0.55
n = 300;
# Find critical values for rejection region (based on theta=0.5)
critical_value_left = qbinom(0.025,n,0.5) - 1;
critical_value_right = qbinom(0.975,n,0.5) + 1;
rejection_region = c(0:critical_value_left, critical_value_right:n)
power = sum(dbinom(rejection_region, n, theta))
print(power)
See the two plots with part (d): power increases as 𝑛 increases because the distributions
become more separated.
500 550 600
520.0
510.0
500.0
500.0−
x
borp
q = =
0.55 n 1055
Plot for 𝑛 = 1055 of the 𝐻 and 𝐻 ∶ 𝜃 = 0.55 distributions. The blue lines show the
0 𝐴
rejection region.
An alternative approach approximating the exact answer with normal distributions is given
at the end of these solutions.
(f) Let 𝐻 ∶ 𝜃 = 0.55. Suppose we have only two hypotheses 𝐻 and 𝐻 , and a flat prior
𝐴 0 𝐴
𝑃 (𝐻 ) = 𝑃 (𝐻 ) = 0.5. What is the posterior probability of 𝐻 given the data? (In this
0 𝐴 𝐴
part 𝐻 is different from in the previous parts; it consists of one specific value of 𝜃.)
𝐴
Solution: We use the usual Bayesian update table.
18.05 Problem Set 8, Spring 2022 Solutions 5
Hypothesis prior likelihood posterior
𝜃 = 0.5 1/2 𝑐 (0.5)250 𝑐 (0.5)250 = 0.14757
1 2
𝜃 = 0.55 1/2 𝑐 (0.55)140(0.45)110 𝑐 (0.55)140(0.45)110 = 0.85243
1 2
1
The normalizing factor 𝑐 = .
2 (0.5)250 + (0.55)140(0.45)110
The posterior probability that 𝜃 = 0.55 is 0.85.
(g) Given the data, what probability would you personally place on the coin being biased
toward heads? Why? There is no one right answer, we are simply interested in your
thinking.
Solution: This is a question about the probability of hypotheses. That’s a Bayesian, not a
frequentist, idea. I’d go with 90% probability the coin is biased towards heads. My Bayesian
analysis is as follows.
If we used the Beta(1, 1) (flat) prior on 𝜃 in [0,1]. Then the posterior for 𝜃 is a Beta(141, 111)
distribution. With this posterior
𝑃(𝜃 > 0.5 | data) = 1 − pbeta(0.5, 141, 111) ≈ 0.97.
This is 97%. Likewise, 𝑃(𝜃 > 0.53 | data) = 83%.
Strictly speaking bias means 𝜃 > 0.5. Leaving a small margin of error we can require
𝜃 > 0.53. My answer is between these two probabilities.
Problem 2. (15: 10,5 pts.) Polygraph analogy.
In an experiment on the accuracy of polygraph tests, 140 people were instructed to tell the
truth and 140 people were instructed to lie. Testers used a polygraph to guess whether or
not each person was lying. By analogy, let’s say 𝐻 corresponds to the testee telling the
0
truth and 𝐻 corresponds to the testee lying.
𝐴
(a) Describe the meaning of type I and type II errors in this context, and estimate their
probabilities based on the table.
Testee is truthful Testee is lying
Tester thinks testee is truthful 131 15
Tester thinks testee is lying 9 125
Solution: Type I error is rejecting the null-hypothesis when it is indeed true. This corre-
sponds to thinking someone is lying when they are in fact being truthful. The experiment
had 9 type I errors. This is our estimate of the probability of a type I error.
140
Type II error is not rejecting the null-hypothesis when it is indeed false. This corresponds
to thinking someone is telling the truth when they are in fact lying. Based on the data our
estimate of the probability of a Type II error is 15 .
140
(b) In NHST, what relationships exist between the terms significance level, power, type I
error, and type II error?
Solution: Significance = 𝑃 (type I error) = 𝑃 (reject 𝐻 | 𝐻 ).
0 0
Power = 1 - 𝑃 (type II error) = 𝑃 (reject 𝐻 | 𝐻 ).
0 𝐴
18.05 Problem Set 8, Spring 2022 Solutions 6
Problem 3. (25: 10,10,5 pts.) z-test
Suppose three radar guns are set up along a stretch of road to catch people driving over the
speed limit of 40 miles per hour. Each radar gun is known to have a normal measurement
error modeled on 𝑁(0, 52). For a passing car, let 𝑥̄ be the average of the three readings.
Our default assumption for a car is that it is not speeding.
(a) Describe the above story in the context of NHST. Are the most natural null and alter-
native hypotheses simple or composite?
Solution: Let 𝜇 be the actual speed of a given driver. We are given that
𝑥 ∼ N(𝜇,52) ⇒ 𝑥 ̄∼ N(𝜇, 52/3).
𝑖
The most natural hypotheses are:
𝐻 : the driver is not speeding, i.e. 𝜇 ≤ 40.
0
𝐻 : the driver is speeding, i.e. 𝜇 > 40.
𝐴
Both are composite.
Note: we will work with 𝐻 : 𝜇 = 40, which is simple.
0
(b) The police would like to set a threshold on 𝑥̄ for issuing tickets so that no more than 4%
of law abiding, non-speeders are mistakenly given tickets. You should assume this means
that they set the threshold conservatively, so that no more 4% of drivers going exactly 40
mph get a ticket.
(i) Use the NHST description in part (a) to help determine what threshold should they set.
(ii) Sketch a graph illustrating your reasoning in part (i).
(iii) What is the probability that a person getting a ticket was not speeding?
(iv) Suppose word gets out about the speed trap and no one speeds along it anymore. What
percentage of tickets are given in error?
Solution: (i) Giving a ticket to a non-speeder is a type I error (rejecting 𝐻 when it is
0
true). 𝐻 is composite, but we can do all our computations with the most extreme value
0
𝜇 = 40 because the one-sided rejection region will have its largest significance level when
𝜇 = 40.
So the null distribution is 𝑥 ̄∼ N(40, 52/3). The critical value is
𝑐 = qnorm(0.96,40,5/sqrt(3)) = 45.054
0.04
(Equivalently 𝑐 = 40 + 𝑧 √5 = 45.054.)
0.04 0.04 3
That is, they should issue a ticket if the average of the three guns is more than 45.054.
(ii) Here is a plot of the null distribution N(40, 52/3). The rejection region with probability
of 0.04 is shown.
18.05 Problem Set 8, Spring 2022 Solutions 7
Null distribution for x_bar
0.16
0.14
0.12
0.1
0.08
0.06
0.04
0.02
0
30 35 40 45 50
(iii) (See (iv).) We don’t know this probability. To find it out would require a prior
probability that a random driver is speeding.
(iv) If no one is speeding then 100% of tickets are given in error.
(c) What is the power of this test with the alternative hypothesis that the car is traveling at
45 miles per hour? How many cameras are needed to achieve a power of 0.9 with 𝛼 = 0.04?
Solution: Power = 𝑃 (rejection | 𝐻 ). So to find the power we first must find the rejection
𝐴
region. For 𝑛 = 3 this was done in part (b): rejection region = [45.054, ∞). So
power = 𝑃(rejection |𝜇 = 45) = 1 - pnorm(45.054, 45, 5/sqrt(3)) = 0.493
With 𝑛 cameras (guns) let’s write 𝑥 for the sample mean. The null distribution is
𝑛
𝑥̄ ∼ N(40, 52/𝑛)
𝑛
The critical value, i.e. the left endpoint of the rejection region and power depends on 𝑛.
We can use R to compute: The code for computing the power when 𝑛 = 3 is shown below.
You only have to change the first line to compute power for different values of 𝑛.
n = 3
mu = 40
sigma = 5/sqrt(n)
alpha = 0.04
xcrit = qnorm(1-alpha, mu, sigma)
power = 1-pnorm(xcrit, 45, sigma)
We can now use R to compute power for increasing values of 𝑛 and find the first value of 𝑛
gives power more than 0.9. We find that 𝑛 = 10 .
Alternative, algebraic approach.
In order to do the computations algebraically we need to write everything in terms of
standard normal values.
√ 5
𝑐 = qnorm(0.96, 40, 5/ 𝑛) = 40 + 𝑧 √
0.04 0.04 𝑛
where 𝑧 is the standard normal critical value
0.04
𝑧 = qnorm(0.96, 0, 1) = 1.751.
0.04
18.05 Problem Set 8, Spring 2022 Solutions 8
We want
power = 𝑃(𝑥 ≥ 𝑐 |𝜇 = 45) = 0.9
0.04
Standardizing and doing some algebra we get
𝑥−45 𝑐 − 45 −5
𝑃 ( √ ≥ 0.04√ ) = 0.9 ⇒ 𝑃 (𝑧 ≥ √ + 𝑧 ) = 0.9
5/ 𝑛 5/ 𝑛 5/ 𝑛 0.04
−5
Thus √ + 𝑧 = 𝑧 . We get
5/ 𝑛 0.04 0.9
𝑛 = (𝑧 − 𝑧 )2 = (1.7507 − (−1.2816))2 = 9.1945.
0.04 0.9
Setting 𝑛 to be the next biggest integer we get 𝑛 = 10.
Problem 4. (10: 5,5 pts.) One generates a number 𝑥 from a uniform distribution on the
interval [0, 𝜃]. One decides to test 𝐻 ∶ 𝜃 = 2 against 𝐻 ∶ 𝜃 ≠ 2 by rejecting 𝐻 if 𝑥 ≤ 0.1
0 𝐴 0
or 𝑥 ≥ 1.9.
(a) Compute the probability of a type I error.
0.2
Solution: 𝑃 (type I) = 𝑃 (reject 𝐻 | 𝐻 ) = 𝑃(𝑥 ≤ 0.1 or 𝑥 ≥ 1.9 |𝜃 = 2) = = 0.1.
0 0 2
(b) Compute the probability of a type II error if the true value of 𝜃 is 2.5.
Solution: 𝑃 (type II) = 𝑃 (don’t reject 𝐻 |𝜃 = 2.5) = 𝑃(0.1 < 𝑥 < 1.9 |𝜃 = 2.5) = 1.8 =
0 2.5
0.72.
Problem 5. (Optional – for learning and fun. 0 pts.)
Give a careful, accurate and precise explanation of the following XKCDs.
(a) https://xkcd.com/1132/
Solution: We have hypotheses 𝐻 = ‘the sun is okay’ and 𝐻 = ‘the sun has gone nova’
0 𝐴
The data is either ‘yes’ or ‘no’ from the detector.
We have the following likelihood table.
data yes no
𝑝(data | 𝐻 ) 1/36 35/36
0
𝑝(data | 𝐻 ) 35/36 1/36
𝐴
The frequentist chooses the rejection region ‘yes’, which has significance 1/36. (Note: 1/36
is really 0.02777 … ≈ 0.028 not 0.027.)
The experimental data is ‘yes’, which is in the rejection region, so the frequentist correctly
rejects 𝐻 in favor of 𝐻 .
0 𝐴
The Bayesian views this as silly, since, from their perspective, the posterior odds that the
sun has gone nova are
𝑝(yes | 𝐻 ) 35
prior odds × likelihood ratio = prior odds × 𝐴 = prior odds × .
𝑝(yes | 𝐻 ) 1
0
If we conservatively put the prior odds at 1/108 then the posterior odds are still very small.
Besides, if the sun has gone nova, losing the bet is the least of the Bayesian’s problem.
18.05 Problem Set 8, Spring 2022 Solutions 9
(b) https://xkcd.com/882/
Solution: The comic is pointing out the flaw of multiple testing or what’s sometimes called
data mining. (The bad type of data mining, there is also a good type.) A significance level
of 0.05 means that in 20 experiments where 𝐻 is true we’d expect to reject it once. The
0
scientists test 20 colors. So even if no jelly bean color causes cancer there is a high probability
(well, 64%) that one of the tests will produce a test statistic in the rejection region.
The fix is to plan on doing 𝑛 tests and set the significance level for any one test to 𝛼/𝑛.
Then, assuming 𝐻 is true for all the tests, the probability that at least one of them will
0
reject is roughly 𝑛⋅𝛼/𝑛 = 𝛼. This is called the Bonferroni correction. (Actually, because
of the possibility of multiple rejections the probabilitiy at least one will reject is less than
or equal to 𝛼.)
Normal approximation approach to problem 1(e).
Here is the alternative approach to 1(e) mentioned at the end of the solution to that problem.
We use the normal approximation binomial(𝑛, 𝜃) ≈ N(𝑛𝜃, 𝑛𝜃(1 − 𝜃)). The normal approxi-
mation introduces some error, but we can compute 𝑛 directly instead of needing to search
through a sequence of possible values.
The algebra is a little involved and it requires that we keep all our definitions straight. I
find it easiest to work with symbols and substitute values at the end.
We have the null and alternative values of 𝜃 are 𝜃 = 0.5 and 𝜃 = 0.55.
0 𝐴
The null distribution is 𝑁(𝑛𝜃 ,𝑛𝜃 (1 − 𝜃 )).
0 0 0
The alternative distribution is 𝑁(𝑛𝜃 ,𝑛𝜃 (1 − 𝜃 )).
𝐴 𝐴 𝐴
The left critical value for the rejection region is 𝑥 . This can be computed in terms of
0.975
the standard normal critical value 𝑧 . Similarly for the right critical value 𝑥 .
0.975 0.025
𝑥 = 𝑛𝜃 + √𝑛𝜃 (1 − 𝜃 ) 𝑧
0.025 0 0 0 0.025
𝑥 = 𝑛𝜃 + √𝑛𝜃 (1 − 𝜃 ) 𝑧 .
0.975 0 0 0 0.975
Power is the probability of our test statistic 𝑥 is in the rejection region assuming 𝐻 . That
𝐴
is,
power = 𝑃 (𝑥 ≤ 𝑥 | 𝜃 = 𝜃 ) + 𝑃 (𝑥 > 𝑥 | 𝜃 = 𝜃 )
0.975 𝐴 0.025 𝐴
For 𝑛 large the left hand probability is essentially 0. So we can ignore it. Thus, to get
power = 0.9 we need
𝑃 (𝑥 > 𝑥 | 𝜃 = 𝜃 ) = 0.9. (1)
0.025 𝐴
Let 𝑐 be the critical value for the alternative distribution. By the usual linearity of normal
0.9
distributions we have
𝑐 = 𝑛𝜃 + √𝑛𝜃 (1 − 𝜃 ) 𝑧 ,
0.9 𝐴 𝐴 𝐴 0.9
where 𝑧 is the standard normal critical point.
0.9
Equation 1 can be restated as 𝑥 = 𝑐 . Now, rewriting both of these values in terms
0.025 0.9
of 𝑛, 𝜃 and 𝜃 , we get
0 𝐴
𝑛𝜃 + √𝑛𝜃 (1 − 𝜃 ) 𝑧 = 𝑛𝜃 + √𝑛𝜃 (1 − 𝜃 ) 𝑧
𝐴 𝐴 𝐴 0.9 0 0 0 0.025
18.05 Problem Set 8, Spring 2022 Solutions 10
This is easily solved for 𝑛:
√ √𝜃 (1 − 𝜃 ) 𝑧 − √𝜃 (1 − 𝜃 ) 𝑧
𝑛 = 0 0 0.025 𝐴 𝐴 0.9.
𝜃 − 𝜃
𝐴 0
We used R to compute 𝑧 = 1.96 and 𝑧 = −1.28. Putting this in the formula above,
0.025 0.9
with 𝜃 = 0.5 and 𝜃 = 0.55 we get 𝑛 = 1046.582 ≈ 1047. This is not too far off from the
0 𝐴
exact answer of 1055 found in problem 1(e).
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
