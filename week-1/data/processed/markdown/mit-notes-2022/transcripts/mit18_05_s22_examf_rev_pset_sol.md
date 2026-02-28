# Mit18 05 S22 Examf Rev Pset Sol

---

Review for final exam: in-class solutions
MIT 18.05 Spring 2022
Problem 1. Basketball
Suppose that against a certain opponent the number of points the MIT basketball team scores
is normally distributed with unknown mean 𝜃 and unknown variance, 𝜎2.
Suppose that over the course of the last 10 games between the two teams MIT scored the
following points:
59, 62, 59, 74, 70, 61, 62, 66, 62, 75
(a) Compute a 95% 𝑡–confidence interval for 𝜃. Does 95% confidence mean that the proba-
bility 𝜃 is in the interval you just found is 95%?
Solution: We compute the data mean and variance 𝑥̄ = 65, 𝑠2 = 35.778. The number of
degrees of freedom is 9. We look up the critical value 𝑡 = 2.262 in the 𝑡-table The
9,0.025
95% confidence interval is
𝑡 𝑠 𝑡 𝑠 √ √
[ 𝑥 ̄ −
9,√0.025
, 𝑥 ̄ +
9,√0.025
] = [65 − 2.262 3.5778, 65 + 2.262 3.5778] = [60.721, 69.279]
𝑛 𝑛
On the exam you will be expected to be able to use the 𝑡-table. We won’t ask you to
compute by hand the mean and variance of 10 numbers.
95% confidence means that in 95% of experiments the random interval will contain the
true 𝜃. It is not the probability that 𝜃 is in the given interval. That depends on the prior
distribution for 𝜃, which we don’t know.
(b) Now suppose that you learn that 𝜎2 = 25. Compute a 95% 𝑧–confidence interval for 𝜃.
How does this compare to the interval in (a)?
Solution: We can look in the 𝑧-table or simply remember that 𝑧 = 1.96. The 95%
0.025
confidence interval is
𝑧 𝜎 𝑧 𝜎 1.96⋅5 1.96 ⋅5
[𝑥 ̄ − 0√.025 , 𝑥 ̄ + 0√.025 ] = [65 − √ , 65 + √ ] = [61.901, 68.099]
𝑛 𝑛 10 10
This is a narrower interval than in part (a). There are two reasons for this, first the true
variance 25 is smaller than the sample variance 35.8 and second, the normal distribution
has narrower tails than the 𝑡 distribution.
(c) Let 𝑋 be the number of points scored in a game. Suppose that your friend is a confirmed
Bayesian with a priori belief 𝜃 ∼ 𝑁(60,16) and that 𝑋 ∼ 𝑁(𝜃,25). He computes a 95%
probability interval for 𝜃, given the data in part (a). How does this interval compare to the
intervals in (a) and (b)?
Solution: We use the normal-normal update formulas to find the posterior pdf for 𝜃.
1 10 𝑎60 + 𝑏65 1
𝑎 = , 𝑏 = , 𝜇 = = 64.3, 𝜎2 = = 2.16.
16 25 post 𝑎+𝑏 post 𝑎+𝑏
The posterior pdf is 𝑓(𝜃|data) = N(64.3, 2.16). The posterior 95% probability interval for 𝜃
is
√ √
[64.3 − 𝑧 2.16, 64.3 + 𝑧 2.16] = [61.442, 67.206]
0.025 0.025
1
(d) Which of the three intervals constructed above do you prefer? Why?
Solution: There’s no one correct answer; each method has its own advantages and disad-
vantages. In this problem they all give similar answers.
Problem 2. Confidence interval 2
The volume in a set of wine bottles is known to follow a N(𝜇, 25) distribution. You take a
sample of the bottles and measure their volumes. How many bottles do you have to sample
to have a 95% confidence interval for 𝜇 with width 1?
Solution: Suppose we have taken data 𝑥 , … , 𝑥 with mean 𝑥.̄ The 95% confidence interval
𝜎
1 𝑛
𝜎
for the mean is 𝑥 ± 𝑧 √ . This has width 2 𝑧 √ . Setting the width equal to 1 and
0.025 𝑛 0.025 𝑛
substitituting values 𝑧 = 1.96 and 𝜎 = 5 we get
0.025
5 √
2 ⋅ 1.96√ = 1 ⇒ 𝑛 = 19.6.
𝑛
So, 𝑛 = (19.6)2 = 384. .
√
If we use our rule of thumb that 𝑧 = 2 we have 𝑛/10 = 2 ⇒ 𝑛 = 400.
0.025
Problem 3. Polling confidence intervals
You do a poll to see what fraction 𝑝 of the population supports candidate A over candidate
B.
(a) How many people do you need to poll to know 𝑝 to within 1% with 95% confidence.
√
Solution: The rule-of-thumb is that a 95% confidence interval is 𝑥 ̄ ± 1/ 𝑛. To be within
1% we need
1
√ = 0.01 ⇒ 𝑛 = 10000.
𝑛
Using 𝑧 = 1.96 instead the 95% confidence interval is
0.025
𝑧
𝑥 ̄ ± 0√.025.
2 𝑛
To be within 1% we need
𝑧
0√.025 = 0.01 ⇒ 𝑛 = 9604.
2 𝑛
Note, we are still using the standard Bernoulli approximation 𝜎 ≤ 1/2.
(b) Let 𝑝 be the fraction of the population who prefer candidate A. If you poll 400 people,
how many have to prefer candidate A so that the 90% confidence interval is entirely above
𝑝 = 0.5.
Solution: The 90% confidence interval is 𝑥 ± 𝑧 ⋅ √1 . Since 𝑧 = 1.64 and 𝑛 = 400
0.05 2 𝑛 0.05
our confidence interval is
1
𝑥±1.64 ⋅ = 𝑥±0.041
40
If this is entirely above 0.5 we have 𝑥 − 0.041 > 0.5, so 𝑥 > 0.541. Let 𝑇 be the number
out of 400 who prefer A. We have 𝑥 = 𝑇 > 0.541, so 𝑇 > 216 .
400
2
Problem 4. Confidence intervals 3
Suppose you made 40 confidence intervals with confidence level 95%. About how many of
them would you expect to be “wrong’? That is, how many would not actually contain the
parameter being estimated? Should you be surprised if 10 of them are wrong?
Solution: A 95% confidence means about 5% = 1/20 will be wrong. You’d expect about
2 to be wrong.
With a probability 𝑝 = 0.05 of being wrong, the number wrong follows a Binomial(40, 𝑝)
distribution. This has expected value 2, and standard deviation √40(0.05)(0.95) = 1.38. 10
wrong is (10-2)/1.38 = 5.8 standard deviations from the mean. This would be surprising.
Problem 5. (Confidence intervals)
A statistician chooses 20 randomly selected class days and counts the number of students
present in 18.05. They find a standard deviation of 4.06 students If the number of students
present is normally distributed, find the 95% confidence interval for the population standard
deviation of the number of students in attendance.
Solution: We have 𝑛 = 20 and 𝑠2 = 4.062. If we fix a hypothesis for 𝜎2 we know
(𝑛 − 1)𝑠2
∼ 𝜒2
𝜎2 𝑛−1
We used R to find the critical values. (Or use the 𝜒2 table.)
c025 = qchisq(0.975,19) = 32.852
c975 = qchisq(0.025,19) = 8.907
The 95% confidence interval for 𝜎2 is
(𝑛−1) ⋅𝑠2 (𝑛−1) ⋅𝑠2 19⋅4.062 19⋅4.062
[ , ] = [ , ] = [9.53, 35.16]
𝑐 𝑐 32.852 8.907
0.025 0.975
We can take square roots to find the 95% confidence interval for 𝜎
[3.09, 5.93]
Problem 6. Linear regression (least squares)
(a) Set up fitting the least squares line through the points (1, 1), (2, 1), and (3, 3).
(a) Solution: The model is 𝑦 = 𝑎 + 𝑏𝑥 + 𝜀 , where 𝜀 is random error. We assume the
𝑖 𝑖 𝑖 𝑖
errors are independent with mean 0 and the same variance for each 𝑖 (homoscedastic).
The total error squared is
𝐸2 = ∑(𝑦 −𝑎−𝑏𝑥 )2 = (1−𝑎−𝑏)2+(1−𝑎−2𝑏)2+(3−𝑎−3𝑏)2
𝑖 𝑖
The least squares fit is given by the values of 𝑎 and 𝑏 which minimize 𝐸2. We solve for
them by setting the partial derivatives of 𝐸2 with respect to 𝑎 and 𝑏 to 0. In R we found
that 𝑎 = −1/3, 𝑏 = 1.
Problem 7. Empirical bootstrap
Suppose we had 100 data points 𝑥 , … 𝑥 with sample median 𝑞 ̂ = 3.3.
1 100 0.5
3
(a) Outline the steps needed to generate an empirical percentile bootstrap 90% confidence
interval for the median 𝑞 .
0.5
Solution: For the percentile bootstrap, we don’t have to pivot, so the algebra is a little
shorter.
Step 1. We have the point estimate 𝑞 ≈ 𝑞̂ = 3.3.
0.5 0.5
Step 2. Use the computer to generate many (say 10000) size 100 resamples of the original
data.
Step 3. For each bootstrap sample compute and save the bootstrap median 𝑞∗ .
0.5
Step 4. Find the quantiles 𝑐 and 𝑐 . (Remember 𝑐 is the 5th percentile in the list
0.05 0.95 0.05
of bootstrap medians, etc.)
Step 5. The 90% percentile bootstrap confidence interval for 𝑞 is
0.5
[𝑐 , 𝑐 ]
0.05 0.95
(b) Suppose now that the sorted list in the previous problem consists of 200 empirical
bootstrap medians computed from resamples of size 100 drawn from the original data. Use
the list to construct a 90% precentile CI for 𝑞 .
0.5
Solution: The list covers steps 1-3 in part (a). Since it is sorted, step 4 is straightforward.
The 5th and 95th percentiles for 𝑞∗ are
0.5
2.89, 3.72
(Here we just took the 10th and 190th values. We could have interpolated between the
9th and 10th, and 190th and 191st entries, but this would not change our answer to two
decimal places.)
The above interval is our empirical percentile bootstrap confidence interval for the median.
Problem 8. Parametric bootstrap
Suppose we have a sample of size 100 drawn from a geom(𝑝) distribution with unknown
𝑝. The MLE estimate for 𝑝 is given by by 𝑝̂ = 1/𝑥.̄ Assume for our data 𝑥̄ = 3.30, so
𝑝̂ = 1/𝑥̄ = 0.30303.
(a) Outline the steps needed to generate a parametric basic bootstrap 90% confidence interval.
Solution: Step 1. We have the point estimate 𝑝 ≈ 𝑝̂ = 0.30303.
Step 2. Use the computer to generate many (say 10000) size 100 samples. (These are called
the bootstrap samples.)
Step 3. For each sample compute 𝑝∗ = 1/𝑥∗̄ and 𝛿∗ = 𝑝∗−𝑝̂ .
Step 4. Sort the 𝛿∗ and find the critical values 𝛿 and 𝛿 . (Remember 𝛿 is the 5th
0.95 0.05 0.95
percentile etc.)
Step 5. The 90% bootstrap confidence interval for 𝑝 is
[𝑝 ̂ − 𝛿 , 𝑝 ̂− 𝛿 ]
0.05 0.95
4
(b) Suppose the following sorted list consists of 200 bootstrap means computed from a sample
of size 100 drawn from a geometric(0.30303) distribution. Use the list to construct a 90%
basic CI for 𝑝.
2.68 2.77 2.79 2.81 2.82 2.84 2.84 2.85 2.88 2.89
2.91 2.91 2.91 2.92 2.94 2.94 2.95 2.97 2.97 2.99
3.00 3.00 3.01 3.01 3.01 3.03 3.04 3.04 3.04 3.04
3.04 3.05 3.06 3.06 3.07 3.07 3.07 3.08 3.08 3.08
3.08 3.09 3.09 3.10 3.11 3.11 3.12 3.13 3.13 3.13
3.13 3.15 3.15 3.15 3.16 3.16 3.16 3.16 3.17 3.17
3.17 3.18 3.20 3.20 3.20 3.21 3.21 3.22 3.23 3.23
3.23 3.23 3.23 3.24 3.24 3.24 3.24 3.25 3.25 3.25
3.25 3.25 3.25 3.26 3.26 3.26 3.26 3.27 3.27 3.27
3.28 3.29 3.29 3.30 3.30 3.30 3.30 3.30 3.30 3.31
3.31 3.32 3.32 3.34 3.34 3.34 3.34 3.35 3.35 3.35
3.35 3.35 3.36 3.36 3.37 3.37 3.37 3.37 3.37 3.37
3.38 3.38 3.39 3.39 3.40 3.40 3.40 3.40 3.41 3.42
3.42 3.42 3.43 3.43 3.43 3.43 3.44 3.44 3.44 3.44
3.44 3.45 3.45 3.45 3.45 3.45 3.45 3.45 3.46 3.46
3.46 3.46 3.47 3.47 3.49 3.49 3.49 3.49 3.49 3.50
3.50 3.50 3.52 3.52 3.52 3.52 3.53 3.54 3.54 3.54
3.55 3.56 3.57 3.58 3.59 3.59 3.60 3.61 3.61 3.61
3.62 3.63 3.65 3.65 3.67 3.67 3.68 3.70 3.72 3.72
3.73 3.73 3.74 3.76 3.78 3.79 3.80 3.86 3.89 3.91
Solution: The basic interval requires an algebraic pivot, so it’s tricky to keep the sides
straight here. We work slowly and carefully:
The 5th and 95th percentiles for 𝑥∗̄ are the 10th and 190th entries
2.89, 3.72
(Here again there is some ambiguity on which entries to use. We will accept using the 11th
or the 191st entries or some interpolation between these entries.)
So the 5th and 95th percentiles for 𝑝∗ are
1/3.72 = 0.26882, 1/2.89 = 0.34602
So the 5th and 95th percentiles for 𝛿∗ = 𝑝∗−𝑝̂ are
−0.034213, 0.042990
These are also the 0.95 and 0.05 critical values.
So the 90% basic CI for 𝑝 is
[0.30303 − 0.042990, 0.30303 + 0.034213] = [0.26004, 0.33724]
Problem 9. (NHST chi-square)
A study of recidivism (repeat offenses) of juvenile offenders used an experimental design with
5
random assignment of juveniles to experimental intervention (Family Group Counseling) or
control group (diversion programs). 70 out of 200 people in the control group re-offended
and 30 out of 200 people in the experimental group re-offended.
Use a chi-square significance test to test whether the recidivism rates within 6 months for
the two experimental groups are significantly different at a significance level of 0.05.
Solution: We will use a chi-square test for homogeneity. Remember we need to use all the
data!. For hypotheses we have:
𝐻 : the re-offense rate is the same for both groups.
0
𝐻 : the rates are different.
𝐴
Here is the table of counts. The computation of the expected counts is explained below.
Control group Experimental group
observed expected observed expected
Re-offend 70 50 30 50 100
Don’t re-offend 130 150 170 150 300
200 200 400
The expected counts are computed as follows. Under 𝐻 the re-offense rates are the same,
0
say 𝜃. To find the expected counts we find the MLE of 𝜃 using the combined data:
total re-offend 100
𝜃̂= = .
total subjects 400
Then, for example, the expected number of re-offenders in the control group is 200⋅𝜃̂= 50.
The other expected counts are computed in the same way.
The chi-square test statistic is
(observed - expected)2 202 202 202 202
𝑋2 = ∑ = + + + ≈ 8+2.67+8+2.67 ≈ 21.33.
expected 50 150 50 150
Finally, we need the degrees of freedom: 𝑑𝑓 = 1 because this is a two-by-two table and
(2− 1) ⋅ (2 −1) = 1. (Or because we can freely fill in the count in one cell and still be
consistent with the marginal counts 200, 200, 100, 300, 400 used to compute the expected
counts.)
From the 𝜒2 table: 𝑝 = 𝑃(𝑋2 > 21.33|𝑑𝑓 = 1) < 0.01.
Conclusion: we reject 𝐻 in favor of 𝐻 . The experimental intervention appears to be
0 𝐴
effective.
6
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
