# Mit18 05 S22 Class20 Pset Sol

---

Class 20 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. Significance tests
Three different tests are run, all with significance level 𝛼 = 0.05.
Experiment 1: finds 𝑝 = 0.003 and rejects its null hypothesis 𝐻 .
0
Experiment 2: finds 𝑝 = 0.049 and rejects its null hypothesis.
Experiment 3: finds 𝑝 = 0.15 and fails to rejects its null hypothesis.
Which result has the highest probability of being correct?
1. Experiment 1 2. Experiment 2
3. Experiment 3 4. Impossible to say.
Solution: Impossible to say. You can’t compute probabilities of hypotheses from 𝑝 values.
Concept question 2. Multiple testing
(a) Suppose we have 6 treatments and want to know if the average recovery time is the same
for all of them. If we compare two at a time, how many two-sample 𝑡-tests do we need to
run?
(i) 1 (ii) 2 (iii) 6 (iv) 15 (v) 30
(b) Suppose we use the significance level 0.05 for each of the 15 tests. Assuming the null
hypothesis, what is the best estimate of the probability that we reject at least one of the 15
null hypotheses?
(i) < 0.05 (ii) 0.05 (iii) 0.10 (iv) > 0.25
Solution: (a) (iv) 6 choose 2 = 15.
(b) (iv) Greater than 0.25.
Under 𝐻 the probability of rejecting for any given pair is 0.05. Because the tests aren’t
0
independent, i.e. if the group1-group2 and group2-group3 comparisons fail to reject 𝐻 ,
0
then the probability increases that the group1-group3 comparison will also fail to reject.
We can say that the following 3 comparisons: group1-group2, group3-group4, group5-group6
are independent. The number of rejections among these three follows a binom(3, 0.05)
distribution. The probability the number is greater than 0 is 1 − (0.95)3 ≈ 0.14.
Even though the other pairwise tests are not independent, they do increase the probability
of rejection. In simulations of this with normal data, the false rejection rate was about
0.36.
Board questions
Problem 1. Stop!
Experiments are run to test a coin that is suspected of being biased towards heads. The
significance level is set to 𝛼 = 0.1
Experiment 1: Toss a coin 5 times. Report the sequence of tosses.
1
18.05 class 20 problems, Spring 2022 2
Experiment 2: Toss a coin until the first tails. Report the sequence of tosses.
(a) Give the test statistic, null distribution and rejection region for each experiment. List all
sequences of tosses that produce a test statistic in the rejection region for each experiment.
(b) Suppose the data is 𝐻𝐻𝐻𝐻𝑇 .
(i) Do the significance test for both types of experiment.
(ii) Do a Bayesian update starting from a flat prior: Beta(1,1).
Draw some conclusions about the fairness of coin from your posterior. (Use R: pbeta for
computation in part (b).)
Solution: (a) Experiment 1: The test statistic is the number of heads 𝑥 out of 5 tosses.
The null distribution is binomial(5,0.5). The rejection region is {𝑥 = 5}.
The sequence of tosses 𝐻𝐻𝐻𝐻𝐻 is the only one that leads to rejection.
Experiment 2: The test statistic is the number of heads 𝑥 until the first tails. The null
distribution is geom(0.5), the rejection region {𝑥 ≥ 4}.
The sequences of tosses that lead to rejection are {𝐻𝐻𝐻𝐻𝑇,𝐻𝐻𝐻𝐻𝐻 ∗∗𝑇}, where ’∗∗’
means an arbitrary length string of heads.
(b) (i) For experiment 1 and the given data, ‘as or more extreme’ means 4 or 5 heads. So
for experiment 1 the 𝑝-value is 𝑃 (4 or 5 heads | fair coin) = 6/32 ≈ 0.20.
For experiment 2 and the given data ‘as or more extreme’ means at least 4 heads at the
start. So 𝑝 = 1 - pgeom(3,0.5) = 0.0625.
(ii) Since the likelihood functions are proportional, the Bayesian posterior will be the same
for both experiments. Let 𝜃 be the probability of heads, Since we have a conjugate pair
(beta-binomial or beta-geometric), Bayesian updating is just updating the parameters in
the Beta distribution. Four heads and a tail updates the prior Beta(1,1) to the posterior
Beta(5,2). Using R we can compute
𝑃 (Coin is biased to heads|data) = 𝑃 (𝜃 > 0.5|data) = 1 -pbeta(0.5, 5,2) = 0.89.
If the prior is reasonable then the probability the coin is biased towards heads is fairly high.
Problem 2. Stop!
For each of the following experiments (all done with 𝛼 = 0.05)
(a) Comment on the validity of the claims.
(b) Find the true probability of a type I error in each experimental setup.
1. Experiment 1. By design Alessandre did 50 trials and computed 𝑝 = 0.04.
They report 𝑝 = 0.04 with 𝑛 = 50 and declare it significant.
2. Experiment 2. Sara did 50 trials and computed 𝑝 = 0.06.
Since this was not significant, she then did 50 more trials and computed 𝑝 = 0.04
based on all 100 trials.
She reports 𝑝 = 0.04 with 𝑛 = 100 and declares it significant.
3. Experiment 3. Gabriel did 50 trials and computed 𝑝 = 0.06.
Since this was not significant, he started over and computed 𝑝 = 0.04 based on the
18.05 class 20 problems, Spring 2022 3
next 50 trials.
He reports 𝑝 = 0.04 with 𝑛 = 50 and declares it statistically significant.
Solution: Experiment 1. (a) This is a reasonable NHST experiment.
(b) The probability of a type I error is 0.05.
Experiment 2. (a) The actual experiment run:
(i) Do 50 trials.
(ii) If 𝑝 < 0.05 then stop.
(iii) If not run another 50 trials.
(iv) Compute 𝑝 again, pretending that all 100 trials were run without any possibility of
stopping.
This is not a reasonable NHST experimental setup because the second 𝑝-values are computed
using the wrong null distribution.
(b) If 𝐻 is true then the probability of rejecting is already 0.05 by step (ii). It can only
0
increase by allowing steps (iii) and (iv). So the probability of rejecting given 𝐻 is more
0
than 0.05. We can’t say how much more without doing a more complicated computation.
Experiment 3. (a) See answer to (2a).
(b) The total probability of a type I error is more than 0.05. We can compute it using
a probability tree. Since we are looking at type I errors all probabilities are computed
assuming 𝐻 is true.
0
First 50 trials .05 .95
Reject Continue
Second 50 trials 0.05
Reject Don’t reject
The total probability of falsely rejecting 𝐻 is 0.05 + 0.05 × 0.95 = 0.0975.
0
Problem 3. From Class 19: Chi-square for independence
(From Rice, Mathematical Statistics and Data Analysis, 2nd ed. p.489)
Consider the following contingency table of counts
Education Married once Married multiple times Total
College 550 61 611
No college 681 144 825
Total 1231 205 1436
Use a chi-square test with significance level 0.01 to test the hypothesis that the number of
marriages and education level are independent.
Solution: The null hypothesis is that the cell probabilities are the product of the marginal
probabilities. Assuming the null hypothesis we estimate the marginal probabilities in orange
and multiply them to get the cell probabilities in blue.
18.05 class 20 problems, Spring 2022 4
Education Married once Married multiple times Total
College 0.365 0.061 611/1436
No college 0.492 0.082 825/1436
Total 1231/1436 205/1436 1
We then get expected counts by multiplying the cell probabilities by the total number of
women surveyed (1436). The table shows the observed, expected counts:
Education Married once Married multiple times
College 550, 523.8 61, 87.2
No college 681, 707.2 144, 117.8
We then have
𝐺 = 16.55 and 𝑋2 = 16.01
The number of degrees of freedom is (2−1)(2−1) = 1. (We can count this: we needed the
marginal counts to compute the expected counts. Now setting any one of the cell counts
determines all the rest because they need to be consistent with the marginal counts from
the data.) So, we get
𝑝 = 1-pchisq(16.55,1) = 0.000047
Therefore we reject the null hypothesis in favor of the alternate hypothesis that number of
marriages and education level are not independent
Discussion questions
1. From Class 18: Type I errors Q1
Suppose a journal will only publish results that are statistically significant at the 0.05 level.
What percentage of the papers it publishes contain type I errors?
Solution: This is asking for 𝑃 (𝐻 |rejected 𝐻 ). This is the probabilitiy of a hypothesis.
0 0
Since we are not given a prior (baserates), we can’t know this. The percentage could be
anywhere from 0 to 100!
Remember: signifcance is the false positive rate, i.e 𝑃 (rejection|𝐻 ). You need the base
0
rate (prior) to know how often the test as a whole is wrong
2. From Class 18: Type I errors Q2
Jerry desperately wants to cure diseases but he is terrible at designing effective treatments.
He is however a careful scientist and statistician, so he randomly divides his patients into
control and treatment groups. The control group gets a placebo and the treatment group
gets the experimental treatment. His null hypothesis 𝐻 is that the treatment is no better
0
than the placebo. He uses a significance level of 𝛼 = 0.05. If his 𝑝-value is less than 𝛼 he
publishes a paper claiming the treatment is significantly better than a placebo.
(a) Since his treatments are never, in fact, effective what percentage of his experiments
result in published papers?
(b) What percentage of his published papers contain type I errors, i.e. describe treatments
that are no better than placebo?
Solution: (a) Since in all of his experiments 𝐻 is true, roughly 5%, i.e. the significance
0
level, of his experiments will have 𝑝 < 0.05 and be published.
18.05 class 20 problems, Spring 2022 5
(b) This is asking for 𝑃 (𝐻 |rejected 𝐻 ). This is the probabilitiy of a hypothesis. Since we
0 0
are given the prior (baserate), that is, since all his treatments are no better than placebo,
we can answer this: All of his published papers contain type I errors.
3. From Class 18: Type I errors Q3
Jen is a genius at designing treatments, so all of her proposed treatments are effective. She
is also a careful scientist and statistician, so she too runs double-blind, placebo controlled,
randomized studies. Her null hypothesis is always that the new treatment is no better than
the placebo. She also uses a significance level of 𝛼 = 0.05 and publishes a paper if 𝑝 < 𝛼.
(a) How could you determine what percentage of her experiments result in publications?
(b) What percentage of her published papers contain type I errors, i.e. describe treatments
that are, in fact, no better than placebo?
Solution: (a) The percentage that get published depends on the power of her treatments.
If they are only a tiny bit more effective than placebo then roughly 5% of her experiments
will yield a publication. If they are a lot more effective than placebo then as many as 100%
could be published.
(b) This is asking for 𝑃 (𝐻 |rejected). Since we are given the prior (baserate), that is,
0
since all her treatments are better than placebo, we can answer this: None of her published
papers contain type I errors.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
