# Mit18 05 S22 Pset11 Sol

---

18.05 Problem Set 11, Spring 2022 Solutions
Problem 1. (20: 10,5,5 pts.) (Height)
Suppose 𝜇 is the average height of a college male. You measure the heights (in inches) of
twenty college men, getting data 𝑥 , … , 𝑥 , with sample mean 𝑥 = 69.55 in. and sample
1 20
variance 𝑠2 = 14.26 in2. Suppose that the 𝑥 are drawn from a normal distribution with
𝑖
unknown mean 𝜇 and unknown variance 𝜎2.
(a) Using 𝑥 and 𝑠2, construct a 90% 𝑡–confidence interval for 𝜇.
Solution: We have 𝑛 = 20 and 𝛼 = 0.1 so
𝑡 = qt(0.05,19) = 1.7291.
𝛼/2
Thus the 90% 𝑡-confidence interval is given by
𝑠 𝑠
[𝑥 − 𝑡 ⋅ √ , 𝑥 + 𝑡 ⋅ √ ] ≈ [68.09, 71.01]
𝛼/2 𝑛 𝛼/2 𝑛
(b) Now suppose you are told that the height of a college male is normally distributed with
standard deviation 3.77 in. Using the same data as in part (a), construct a 90% 𝑧–confidence
interval for 𝜇.
Solution: We have
𝑧 = qnorm(0.05) = 1.6448.
𝛼/2
So the 90% 𝑧-confidence interval is given by
𝜎 𝜎
[𝑥 − 𝑧 ⋅ √ , 𝑥 + 𝑧 ⋅ √ ] ≈ [68.16, 70.94]
𝛼/2 𝑛 𝛼/2 𝑛
(c) In (b), how many people in total would you need to measure to bring the width of the
90% z–confidence interval down to 1 inch?
√
Solution: We need 𝑛 such that 2 ⋅ 𝑧 ⋅ 𝜎/ 𝑛 = 1. So
0.05
𝑛 = (2 ⋅ 𝑧 ⋅ 𝜎)2 = (2 ⋅ 1.6448 ⋅ 3.77)2 ≈ 153.8.
0.05
Since you need a whole number of people the answer is 𝑛 = 154 .
Problem 2. (10 pts.) Confidence intervals from standardized statistics
The Beta distribution arises in a surprising way: draw a sample of size 𝑛 from a uniform(0,1)
distribution and let 𝑤 be the second smallest value. Then it turns out that
2
𝑤 ∼ Beta(2,𝑛 − 1).
2
Now suppose you draw a sample of size 𝑛 from a uniform(0, 𝑎) distribution, where 𝑎 is
unknown. If we let 𝑦 be the second smallest data value then the standardized order statistic
2
𝑦 /𝑎 ∼ Beta(2,𝑛 − 1).
2
Use 𝑦 and qbeta in R, to define a 95% confidence interval for 𝑎. (Because 𝑛 and 𝑦 are
2 2
not given this will be a general formula not numbers.)
1
18.05 Problem Set 11, Spring 2022 Solutions 2
Finally, supposing 𝑛 = 9 and 𝑦 = 1.5, give the 95% confidence interval for 𝑎.
2
Solution: This is a problem about using a standardized statistic and ‘pivoting’ to compute
confidence intervals. We are told that 𝑦 /𝑎 ∼ Beta(2,𝑛 − 1). If 𝑐 amd 𝑐 are the
2 0.025 0.975
critical values for Beta(2,𝑛 − 1) then this means that
𝑦
𝑃 (𝑐 < 2 < 𝑐 | 𝑎) = 0.95.
0.975 𝑎 0.025
Here, in R notation, 𝑐 = qbeta(0.025, 2, n-1) and 𝑐 = qbeta(0.975, 2, n-1).
0.975 0.025
Doing some algebra to isolate 𝑎 in the middle, this becomes
𝑦 𝑦
𝑃 ( 2 < 𝑎 < 2 |𝑎) = 0.95.
𝑐 𝑐
0.025 0.975
If 𝑛 = 9 we have
𝑐 = qbeta(0.975, 2, 8) = 0.482, 𝑐 = qbeta(0.025, 2, 8) = 0.0281
0.025 0.975
So, in this case, the 95% confidence interval is
𝑦 1.5 1.5 1.5
[ 2 , ] ≈ [ , ] ≈ [3.1, 53.3] .
𝑐 𝑐 0.482 0.0281
0.025 0.975
Problem 3. (35: 15,10,10 pts.) Various variances
Consider a sample of size 𝑛 drawn from a Bernoulli(𝜃) distribution. (That is, a draw from a
binomial(𝑛, 𝜃) distribution.) In constructing a confidence interval the conservative estimate
is that the variance of the underlying Bernoulli distribution is 𝜎2 = 1/4 –this is conservative
because for any 𝜃 we know that 𝜎2 ≤ 1/4.
(a) In this problem we want to compare how well normal distribution using the conservative
estimate matches the one using the true variance
(i) Let 𝜃 = 0.5 and 𝑛 = 250. Make a plot that includes
• the pmf 𝑝(𝑥|𝜃) of the binomial(𝑛, 𝜃) distribution.
• the pdf of the normal distribution with the same mean and variance as the binomial((𝑛, 𝜃))
distribution
• the normal distribution with the same mean (as the binomial distribution) and conservative
variance to your plot.
Note: The conservative variance for a Bernoulli(𝜃) distribution is 1/4. So the conservative
variance for a binomial(𝑛, 𝜃) is 𝑛/4.
Note. It is not reasonable to compare the probabilities in a pmf to the densities in a pdf.
In order to make them comparable, but also to make the graphs readable, you should plot
the pmf as points, but think of them as the top of a density histogram with bin width 1 and
breaks on the half integers.
(ii) Make a similar plot for 𝜃 = 0.3 and 𝑛 = 250.
(iii) Make a similar plot for 𝜃 = 0.1 and 𝑛 = 250.
18.05 Problem Set 11, Spring 2022 Solutions 3
In each case, how close are each of the normal distributions to the binomial distribution?
How do the two normal distributions differ? Based on your plots, for what range of 𝜃 do you
think the conservative normal distribution is a reasonable approximation for binomial(𝑛, 𝜃)
with large 𝑛?
Solution: We have 𝑥 ∼ binomial(𝑛, 𝜃), so 𝐸[𝑋] = 𝑛𝜃 and Var(𝑋) = 𝑛𝜃(1 − 𝜃). The
conservative variance is just 𝑛. So the distributions being plotted are
4
binomial(250, 𝜃), N(250𝜃, 250𝜃(1 − 𝜃)), N(250𝜃, 250/4).
Note, the whole range is from 0 to 250, but we only plotted the parts where the graphs
were not essentially 0.
lll
l l
l l
l l l l
l l
l l
l l
l l
l l
l l
l l
l l l l
l l
l l l l llllllllllllllllllllllllllll llllllllllllllllllllllllllll
80 100 120 140 160
50.0
40.0
30.0
20.0
10.0
00.0
q= 0.5
True variance l
lll
l
Conservative variance l l
l Binomial pmf l l l
l
l
l
l
l
l l
l l
l l
l l
l l l l
l l
l l lllllllllllllllllll l l lllllllllllllllllllllllllllll
40 60 80 100 120
x
50.0
40.0
30.0
20.0
10.0
00.0
q= 0.3
True variance
Conservative variance
l Binomial pmf
x
ll
l l
l
l
l
l
l
l
l
l
l
l
l
l l
l l
l l l
llllllllllllll l lllllllllllllllllll
0 10 20 30 40 50
80.0
60.0
40.0
20.0
00.0
q= 0.1
True variance
Conservative variance
l Binomial pmf
x
We notice that for each 𝜃 the blue dots lie very close to the green (true variance) curve. So
the N(𝑛𝜃, 𝑛𝜃(1 − 𝜃)) distribution is quite close to the binomial(𝑛, 𝜃) distribution for each
of the values of 𝜃 considered. In fact, this is true for all 𝜃 by the Central Limit Theorem.
For 𝜃 = 0.5 the conservative variance is the exact variance. For 𝜃 = 0.3 the conservative
variance works well: it has smaller peak and slightly fatter tail. For 𝜃 = 0.1 the conservative
approximation breaks down and is not very good.
18.05 Problem Set 11, Spring 2022 Solutions 4
In summary we can say two things about the conservative variance:
1. It gives good results for 𝜃 near 0.5 and breaks down for extreme values of 𝜃.
2. Since the conservative variance overestimates the variance (the conservative graphs are
shorter and wider) it gives us a confidence interval that is larger than is strictly necessary.
That is a nominal 95% conservative interval actually has a greater than 95% confidence
level.
(b) Suppose 𝜃 is the probability of success, and that the result of an experiment was 140 suc-
cesses out of 250 trials. Find 80% and 95% confidence intervals for 𝜃 using the conservative
variance. (For the 95% interval use the rule-of-thumb that 𝑧 = 2.)
0.025
Solution: Using the conservative variance, we know that 𝑥̄ is approximately N(𝜃, 1/4𝑛).
For an 80% confidence interval, we have 𝛼 = 0.2 so
𝑧 = qnorm(0.9,0,1) = 1.2815.
𝛼/2
So the 80% confidence interval for 𝜃 is given by
𝑧 𝑧
[ 𝑥 ̄ − √0.1 , 𝑥 ̄ + √0.1 ] = [0.5195,0.6005]
2 𝑛 2 𝑛
For the 95% confidence interval, we use the rule-of-thumb that 𝑧 ≈ 2. So the confidence
0.025
interval is
1 1
[𝑥̄ − √ ,𝑥̄+ √ ] = [0.497,0.623]
𝑛 𝑛
It’s okay to have used the exact value of 𝑧 . This gives a confidence interval:
0.025
1.96 1.96
[𝑥 ̄ − √ , 𝑥̄ + √ ] = [0.498,0.622]
2 𝑛 2 𝑛
(c) Using the same data as in part (b), find an 80% posterior probability interval for 𝜃
using a flat prior, i.e. Beta(1, 1). Center your interval between the 0.1 and 0.9 quantiles.
Compare this with the 80% confidence interval in part (b).
Hint: Use qbeta(p, a, b) to do the computation.
Solution: With prior Beta(1, 1), if we observe 𝑥 successes in 250 trials, then the posterior
is Beta(1 + 𝑥,1 + 250 − 𝑥). In our case 𝑥 = 140. So, using R we get the 80% posterior
probability interval:
prob_interval = [qbeta(0.1, 141, 111), qbeta(0.9, 141, 111)] ≈ [0.52, 0.60]
This is quite close to the 80% confidence interval. Though the two intervals have very
different technical meanings, we see that they are consistent (and numerically close). Both
give a type of estimate of 𝜃.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
