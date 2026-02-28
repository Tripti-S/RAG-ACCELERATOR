# Mit18 05 S22 Pset09 Sol

---

18.05 Problem Set 9, Spring 2022 Solutions
Problem 1. (15: 10,5 pts.)
We perform a 𝑡-test for the null hypothesis 𝐻 ∶ 𝜇 = 10 at significance level 𝛼 = 0.05 by
0
means of a dataset consisting of 𝑛 = 16 elements with sample mean 11 and sample variance
4.
(a) Should we reject the null hypothesis in favor of 𝐻 ∶ 𝜇 ≠ 10?
𝐴
Solution: This is a two-sided alternative. The 𝑡-statistic is
𝑥 ̄− 𝜇 1
√ = = 2.
𝑠/ 𝑛 2/4
Since we have 𝑛 = 16 our 𝑡 statistic has 15 degrees of freedom.
We have the two-sided 𝑝-value
𝑝 = 𝑃 (|𝑡| > 2|𝐻 ) = 2*(1-pt(2,15)) = 0.063945.
0
Since 𝑝 > 𝛼 = 0.05 we don’t reject the null hypothesis.
Alternatively we could have done the problem in terms of rejection regions. We are given
𝑥̄= 11, 𝑠2 = 4, and 𝑛 = 16. The null hypothesis is 𝜇 = 10. Using 𝑥̄ as our test statistic the
rejection region is
𝑠 𝑠
(−∞,10−𝑡 √ ] ∪ [10+𝑡 √ ,∞) = (−∞,8.93] ∪ [11.07,∞)
15,0.025 𝑛 15,0.025 𝑛
Here 𝑡 means a critical value, i.e. the value with right tail probability 0.025: for
15,0.025
𝑇 ∼ 𝑡(15) we have 𝑃 (𝑡 > 𝑡 ) = 0.025.
15,0.025
Since 11 lies outside the rejection region, we should not reject the null-hypothesis.
(b) What if we test against 𝐻′ ∶ 𝜇 > 10?
𝐴
Solution: This is a one-sided alternative. The 𝑡-statistic is the same
𝑥 ̄− 𝜇 1
√ = = 2.
𝑠/ 𝑛 2/4
So we have the one-sided 𝑝-value
𝑝 = 𝑃(𝑡 > 2|𝐻 ) = 1-pt(2,15) = 0.031973.
0
Since 𝑝 < 𝛼 = 0.05 we reject the null hypothesis in favor of the alternative.
Again looking at rejection regions. We use the critical value 𝑡 ≈ 1.753. The rejection
15,0.05
region for 𝑥̄ is
𝑠
[10+𝑡 √ ,∞) = [10.876,∞).
15,0.05 𝑛
Since 11 lies inside the rejection region, we should reject the null-hypothesis in favor of
𝐻 ∶ 𝜇 > 10.
1
Problem 2. (40: 10,10,5,10,5 pts.)
Jerry took a JP Licks token and asked Jon to perform a test at significance level 𝛼 = 0.05
1
18.05 Problem Set 9, Spring 2022 Solutions 2
to investigate whether the coin is fair or biased toward tails (the side that says ‘Token’).
Jon recorded the following data
THTTHTTTTTTH
showing 3 heads and 9 tails.
Before Jon could compute the one-sided 𝑝-value for 𝐻 ∶ 𝜃 = 0.5 versus 𝐻 ∶ 𝜃 < 0.5, he
0 𝐴
needed to take Aviva to the playground.
(a) Erika believes that Jon’s intention was to count the number of heads in twelve flips.
Let’s call this Experiment 1. Compute the rejection region and 𝑝-value. Sketch the null-
distribution and rejection region. What does Erika conclude?
Solution: Let 𝑥 = number of heads
Model: 𝑥 ∼ binomial(12, 𝜃).
Null distribution binomial(12, 0.5).
Data: 3 heads in 12 tosses.
Since 𝐻 is one-sided the rejection region is one-sided. Since 𝐻 says that 𝜃 is small it
𝐴 𝐴
predicts a small number of heads in 12 tosses. That is, we reject 𝐻 on a small number of
0
heads.
So, rejection region = left tail of null distribution.
𝑐 = qbinom(0.05, 12, 0.5) - 1 = 2
0.95
Rejection region is 0 ≤ 𝑥 ≤ 2.
𝑝 = pbinom(3, 12, 0.5) = 0.072998
0 2 4 6 8 10 12
02.0
01.0
00.0
x
Binomial(12,15) null distribution and rejection region 𝑥 ≤ 2.
Erika concludes there is not enough evidence to reject the null hypothesis at the significance
level 0.05.
(b) Ruthi believes that Jon’s intention was to stop after the third heads and report the
number of tails, e.g., in the data the third head came on flip 12 so the number of tails is
9. Let’s call this Experiment 2. Compute and sketch the corresponding null-distribution,
18.05 Problem Set 9, Spring 2022 Solutions 3
rejection region, and 𝑝-value. What does Ruthi conclude? Hint: if a counting argument
eludes you, google “negative binomial distribution”.
The R functions dnbinom, pnbinom, etc. might be helpful. For example, dnbinom(5, 3, 0.2)
gives the probability of seeing 5 tails before the third head in a sequence of tosses of a coin
with probability 0.2 of heads.
Solution: Let 𝑛 = number of tosses that were tails before the third that is heads
Probability model: Choose two tosses in the first n+2 for heads; the 𝑛 + 3rd toss must be
heads:
𝑛 + 2
𝑝(𝑛) = ( )(1 − 𝜃)𝑛𝜃3.
2
This is called the negative binomial distribution with parameters 3 and 𝜃.
Our data is: 9 tails to get 3 heads.
Since 𝐻 is one-sided the rejection region is one-sided. Since 𝐻 has 𝜃 small (< 0.5), it
𝐴 𝐴
predicts a large number of tails before 3 heads. So we reject on a large number of tails.
Rejection region = right tail of null distribution.
𝑐 = qnbinom(0.95, 3, 0.5) + 1 = 9
0.05
Rejection region is 𝑛 ≥ 9.
𝑝 = 1 - pnbinom(8, 3, 0.5) = 0.032715
0 5 10 15 20
01.0
00.0
x
Negative binomial null distribution and rejection region
Ruthi rejects the null hypothesis in favor of 𝐻 at significance level 0.05.
𝐴
(c) Jerry actually told Jon to count the number of heads in 100 flips (Experiment 3), so
Jerry figures that Jon must have gotten bored and quit right after the 12th flip. Strictly
speaking, can Jerry compute a 𝑝-value from Jon’s partial data? Why or why not?
Solution: No. Computing a 𝑝-value requires that the experiment be fully specified ahead
of time so that the definition of ’data at least as extreme’ is clear.
Having said that, it’s a shame to waste good data. You can still analyze the data for
suggestive results. As long as you report everything honestly people can reach their own
conclusions.
18.05 Problem Set 9, Spring 2022 Solutions 4
(d) Let’s reexamine the same data from the Bayesian perspective. What is the likelihood
function in Experiment 1? What is the likelihood function in Experiment 2? How are these
likelihood functions related? Given the prior Beta(𝑛,𝑚), find the posterior in each case.
How are they related?
Solution: Prior: Beta(𝑛, 𝑚) has pdf 𝑐 𝜃𝑛−1(1 − 𝜃)𝑚−1
12
Likelihood experiment 1: ( )𝜃3(1 − 𝜃)9
3
11
Likelihood experiment 2: ( )𝜃3(1 − 𝜃)9
2
Since the likelihoods are the same up to a constant factor the posterior has the same form
𝑐 𝜃𝑛+3−1(1 − 𝜃)𝑚+9−1
which is the pdf of a Beta(𝑛 + 3,𝑚 + 9) distribution.
The two posteriors are identical. In the Bayesian framework the same data produces the
same posterior.
(e) Read https://en.wikipedia.org/wiki/Likelihood_principle, appreciate the volt-
meter story, and summarize the main points we are getting at via the earlier parts of this
problem regarding frequentist and Bayesian experiments.
Solution: The main point is that in the frequentist framework the decision to reject or
accept 𝐻 depends on the exact experimental design because it uses the probabilities of
0
unseen data as well as those of the actually observed data.
Problem 3. (10 pts.) (Chi-square for variance)
The following data comes from a normal distribution which you suspect has variance equal
to 1. You want to test this against the alternative that the variance is greater than 1.
1.76, -2.28, -0.56, 1.46, 0.59, 1.26,
-1.94, -0.79, -0.86, -1.41, 2.07, 1.30
There is a chi-square test for this. Look at
https://www.itl.nist.gov/div898/handbook/eda/section3/eda358.htm
and run the test with significance level 0.05. You can use R for the computations, but
explain what you are doing and give the value of the test statistic, and the 𝑝-value.
Solution: We use the 𝜒2 statistic with hypotheses 𝐻 : 𝜎2 = 1, 𝐻 : 𝜎2 > 1.
0 𝐴
So, we have 𝜎2 = 1 and 𝑠2 = sample variance = var(data) = 2.34.
0
𝑛 = 12 = number of data points.
𝜒2-statistic: 𝑋2 = (𝑛 − 1)𝑠2/𝜎2 = 25.74
0
Since the alternative hypothesis is 𝜎 > 𝜎 , this is a right-sided test. The right-sided 𝑝-value
0
is p = 1 - pchisq(𝑋2 , n-1) = 0.0071.
Since 𝑝 < 0.05 we reject the null hypothesis 𝐻 in favor of the alternative that 𝜎2 > 1.
0
Problem 4. (10 pts.) (Chi-squared for categorical data)
Jon and Jerry spent a fortune on dice and and bent coins for 18.05, so they decide to submit
an invoice to the math department for reimbursement. The math department suspects that
18.05 Problem Set 9, Spring 2022 Solutions 5
their six figure expense report is made up, so they call you to test the data for fraud. You
do some research and learn that accounting data should follow something called Benford’s
law. This states that the relative frequency of the first digits of each entry should have the
following distribution:
First digit 𝑘 1 2 3 4 5 6 7 8 9
probability 𝑝(𝑘) 0.301 0.176 0.125 0.097 0.079 0.067 0.058 0.051 0.046
You go back to the math department and tell them that the only data you need is the counts
of all the first digits in their invoice. They are skeptical, but they know you have taken
18.05 and, so, must know what you are doing. They give you the following counts.
First digit 𝑘 1 2 3 4 5 6 7 8 9
count 7 13 12 9 9 13 11 10 16
The math department doesn’t want to unjustly accuse Jon and Jerry, so they ask you to test
at 0.001 significance level. Run a significance test to see how well this data fits Benford’s
distribution and make a recommendation to the math department.
See https://en.wikipedia.org/wiki/Benford%27s_law
Solution: We do a 𝜒2 test of goodness of fit comparing the observed counts with the counts
expected from Benford’s distribution.
You can use either test statistic
𝑂
𝐺 = 2∑𝑂 ln ( 𝑖 ) .
𝑖 𝐸
𝑖
or
(𝑂 − 𝐸 )2
𝑋2 = ∑ 𝑖 𝑖
𝐸
𝑖
where 𝑂 are the observed counts and 𝐸 are the expected counts from Benford’s distribu-
𝑖 𝑖
tion. The total count = 100.
First digit 𝑘 1 2 3 4 5 6 7 8 9
observed 7 13 12 9 9 13 11 10 16
expected 30.103 17.609 12.494 9.691 7.918 6.695 5.7992 5.1153 4.5757
𝑋2 components 17.731 1.206 0.200 0.049 0.148 5.939 4.664 4.665 28.523
The 𝜒2-statistics are 𝐺 = 56.3919 and 𝑋2 = 62.6998.
There are 9 cells that must sum to 100 so the degrees of freedom = 8.
The 𝑝-value using 𝐺 is
𝑝 = 𝑃(G test stat > 56.3919 | 𝐻 ) = 1-pchisq(56.3919, 8) = 2.4 × 10−9
0
The 𝑝-value using 𝑋2
𝑝 = 𝑃(X2 test stat > 62.6998 | 𝐻 ) = 1-pchisq(62.6998, 8) = 1.4 × 10−10
0
Since 𝑝 < 𝛼 we reject 𝐻 in favor of the notion that Jon and Jerry were trying to embezzle
0
money.
Problem 5. (20: 10,10 pts.) (Two-sample F test for equal variances)
In this problem, we want you to become comfortable using the web to learn about new
18.05 Problem Set 9, Spring 2022 Solutions 6
tests and R commands. There are dozens of statistical software packages used by labs and
industry, so being able to learn new commands is probably more important than trying to
memorize them all. Look at the help file in R for var.test
We used R to secretly create a vector 𝑥 of 20 random samples from an N(0, 1) distribution
and a vector 𝑦 of 20 random samples from a N(10, 1) distribution. These are listed below.
With a tiny bit of editing you should be able to copy and paste these into R.
-0.802, 0.457, 0.972, 0.044, 0.318, -1.380, 0.111,
-0.023, -0.700, -1.977, -0.497, 1.471, -1.314, -0.078,
-0.505, 0.583, 1.363, -1.863, -2.105, 0.488
9.019, 9.852, 7.947, 9.465, 10.060, 10.508, 9.506,
9.540, 10.218, 9.407, 11.455, 11.422, 7.698, 9.972,
10.928, 11.577, 10.376, 8.605, 9.347, 10.715
(a) Temporarily erase from your mind the variances used in generating the data. We want
to test the null hypothesis that the normal distributions which generated 𝑥 and 𝑦 have equal
variances. Now use var.test to find the 𝑝-value for the test for equal variances. (You may
need to go back and look at the documentation for var.test to see how to do this.)
Solution: We let 𝑥 = the first set of 20 numbers and 𝑦 the second. R makes it almost too
easy. We give the command
var.test(x,y).
R then prints out
F test to compare two variances
data: x and y
F = 0.97034, num df = 19, denom df = 19, p-value = 0.9484
alternative hypothesis: true ratio of variances is not equal to 1
95 percent confidence interval:
0.3840737 2.4515249
sample estimates:
ratio of variances
0.9703434
So, the 𝑝-value is 0.9484 with 𝐹 -statistic 0.9703. With this 𝑝-value we do not reject the null
hypothesis that the variances are the same.
(b) You should look up the F-test for equal variances. Give the formula and compute the F
statistic and 𝑝-value directly. You can use R to compute sample means, sample variances
and do arithmetic as needed, but you can’t use var.test to do all the work. You will need
the R function pf to compute probabilities for the F distribution
Should you reject the null-hypothesis at 𝛼 = 0.05?
Note: here is how you get a two-sided 𝑝-value for this test.
If the 𝐹 -statistic is greater than 1 then
𝑝 = 2× the right tail probability
18.05 Problem Set 9, Spring 2022 Solutions 7
If the 𝐹 -statistic is less than 1 then
𝑝 = 2× the left tail probability
Solution: We found the formula for the F statistic for this test at
https://en.wikipedia.org/wiki/F-test_of_equality_of_variances
𝑠2 = var(x) = 1.1302
𝑥
𝑠2 = var(y) = 1.1647
𝑦
Our 𝐹 -statistic is
𝑠2
fstat = 𝑥 = 0.9703
𝑠2
𝑦
The degrees are freedom are both 19. We are running a two-sided test. So,
𝑝 = 2*min(pf(fstat, 19, 19), 1-pf(fstat, 19, 19)) = 0.9484
which matches our result in part (a).
Problem 6. (20: 10,10 pts.) (One-way ANOVA)
Read the abstract of the following paper:
https://www.sciencedirect.com/science/article/pii/S1090513813000226
Barnaby J. Dixson, Robert C. Brooks. The role of facial hair in women’s perceptions of
men’s attractiveness, health, masculinity and parenting abilities. Evolution and Human
Behavior, Volume 34, Issue 3, May 2013, Pages 236-241
Note that one of the authors may have a personal bias:
https://www.researchgate.net/profile/Barnaby_Dixson
For this problem you will need the F-test for equal means from the reading for class 19. For
the purposes of the problem, we made a slight simplification to the experimental protocol
and data.
(a) The table below records the mean attractiveness rating for 351 heterosexual or bisexual
women who rated the attractiveness of one male face of each type from 0 (very low) to 5
(very high). So we have four groups with 351 samples per group.
facial hair state clean 5-day 10-day full
sample mean 1.32 1.26 1.53 1.39
sample variance 0.56 0.80 0.93 0.82
Run a one-way ANOVA (F-test) at 𝛼 = 0.01 for equal means “by hand”. That is, compute
the 𝐹 -statistic and corresponding 𝑝 value using the data in the table, and decide whether to
reject the null hypothesis.
Solution: Let’s specify the assumptions and hypotheses for this test.
We have 4 groups of data: Clean, 5-day, 10-day, full
18.05 Problem Set 9, Spring 2022 Solutions 8
Assumptions: Each group of data is drawn from a normal distribution with the same
variance 𝜎2; all data is drawn independently.
𝐻 : the means of all the normal distributions are equal.
0
𝐻 : not all the means are equal.
𝐴
The test compares the between group variance with the within group variance. Under the
null hypothesis both are estimates of 𝜎2, so their ratio should be about 1. We’ll reject 𝐻
0
if this ratio is far from 1.
We used R to do the computation. Here’s the code.
mns = c(1.32, 1.26, 1.53, 1.39)
v = c(0.56, 0.80, 0.93, 0.82)
m = 351 # number of samples per group
n = length(mns) # number of groups
msb = m*var(mns) # between group variance
msw = mean(v) # within group variance
fstat = msb/msw
df1 = n-1;
df2 = n*(m-1)
p = 1 - pf(fstat, df1,df2)
print(fstat)
print(p)
This produced an 𝐹 -statistic of 6.09 and 𝑝 = 0.00041. Since the 𝑝-value is much smaller
than 0.05 we reject 𝐻 .
0
(b) Following up, use 3 two-sample t-tests to investigate the hypothesis that the mean for
10-day is higher than the each of the others. For each test use significance level 𝛼 = 0.01.
(The two-sample 𝑡-test is described in the reading for class 19.)
If exactly one of these tests resulted in a rejection, would it be appropriate to conclude that
we have rejected the null hypothesis in part (a) at significance level 𝛼 = 0.01?
Solution: We compare 10-day beards with each of the others. In each case we have: 𝐻 :
0
the means are the same
𝐻 : the 10-day mean is greater than the other mean.
𝐴
Note carefully that this is a one-sided test while the 𝐹 -test in part (b) is a two-sided test.
From the class 19 reading we have the 𝑡-statistic for two samples. Since both samples have
the same size 𝑚 = 351 the formula looks a little simpler.
𝑥 ̄ − 𝑦̄
𝑡 = ,
𝑠
𝑃
where the pooled sample variance is
𝑠2 + 𝑠2
𝑠2 = 𝑥 𝑦
𝑃 𝑚
Note: the test assumes equal variances which we should verify in each case. This raises the
issue of multiple tests from the same data, but it is legitimate to do this as exploratory
analysis which merely suggests directions for further study.
18.05 Problem Set 9, Spring 2022 Solutions 9
The following table shows the one-sided, 2-sample 𝑡-test comparing the mean of the 10-day
growth against the other three states.
𝑡-stat one-sided 𝑝-value 𝐹 -stat
clean 3.22 0.00066 10.39
5-day 3.85 0.00007 14.79
full 1.98 0.0239 3.93
We also give the 𝐹 -statistic for the two samples. You can check that the 𝐹 -statistic for
two-samples is just the square of the 𝑡-statistic.
If one of the tests has significance level less than 0.01, it is not proper to reject the null
hypothesis. This is because the significance level of the entire experiment is greater than
0.01. That is, since we ran 3 tests each with probability 0.01 of a type I error the total
probability of type I error is greater than 0.01 –it will be close to 0.03.
We reiterate that with multiple testing the true significance level of the test is larger than
the significance level for each individual test.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
