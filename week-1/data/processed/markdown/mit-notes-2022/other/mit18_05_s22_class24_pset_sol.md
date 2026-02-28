# Mit18 05 S22 Class24 Pset Sol

---

Class 24 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. Which stat is easiest
Consider finding bootstrap confidence intervals for
I. the mean II. the median III. 47th percentile.
Which is easiest to find?
(a) I (b) II (c) III (d) I and II
(e) II and III (f) I and III (g) I and II and III
Solution: (g) The program is essentially the same for all three statistics. All that needs
to change is the code for computing the specific statistic.
Board questions
Problem 1. Empirical bootstrap
Data: 3 8 1 8 3 3
Bootstrap samples (each column is one bootstrap trial):
8 8 1 8 3 8 3 1
1 3 3 1 3 8 3 3
3 1 1 8 1 3 3 8
8 1 3 1 3 3 8 8
3 3 1 8 8 3 8 3
3 8 8 3 8 3 1 1
(a) Compute a bootstrap 80% percentile confidence interval for the mean.
(b) Compute a bootstrap 80% percentile confidence interval for the median.
(a) Solution: 𝑥 = 4.33
𝑥∗ : 4.33, 4.00, 2.83, 4.83, 4.33, 4.67, 4.33, 4.00
Sorted
𝑥∗ : 2.83, 4.00, 4.00, 4.33, 4.33, 4.33, 4.67, 4.83
So (quantiles), 𝑥∗ = 3.65, 𝑥∗ = 4.72.
0.1 0.9
(For 𝑥∗ we interpolated between the bottom two values. Likewise for 𝑥∗ . There are other
0.1 0.9
reasonable choices. In R see the quantile() function.)
80% percentile bootstrap CI for mean: [3.65, 4.72].
(b) Solution: 𝑚 = median(𝑥) = 3
𝑚∗ : 3.0, 3.0, 2.0, 5.5, 3.0, 3.0, 3.0, 3.0
Sorted 𝑚∗ : 2.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 5.5
(For 𝑚∗ we interpolated between the top two values –there are other reasonable choices.
0.1
In R see the quantile() function.)
1
18.05 class 24 problems, Spring 2022 2
80% bootstrap CI for median: [2.7, 3.75].
Problem 2. Parametric bootstrap
Data is taken from a Binomial(8, 𝜃) distribution. After 6 trials, the results are
6 5 5 5 7 4
(a) Estimate 𝜃.
(b) Write out the R code to generate data of 100 parametric bootstrap samples and compute
an 80% confidence interval for 𝜃.
(Try this without looking at your notes.)
(a) Solution: There are 𝑛 = 6 data points. The MLE for 𝜃 is given by
sum of data 32 2
= = .
𝑛⋅8 48 3
Here are the details done abstractly to verify the formula used above. The likelihood for
one trial getting 𝑘 is
8
𝑃 (𝑘 | 𝜃) = ( )𝜃𝑘(1 − 𝜃)8−𝑘.
𝑘
So the likelihood over 𝑛 trials with data 𝑘 , … , 𝑘 is the product of the individual likelihoods
1 𝑛
𝐿(𝜃) = 𝑐𝜃∑𝑛 𝑖= 1 𝑘 𝑖(1 − 𝜃)∑ 𝑖 𝑛 = 1 (8−𝑘 𝑖 )
Here we rolled all the binomial coeﬀicients into one constant called 𝑐.
As usual, we look at the log likelihood
𝑛 𝑛
𝑙(𝜃) = ln(𝑐) + (∑ 𝑘 ) ln(𝜃) + (∑(8 − 𝑘 )) ln(1 − 𝜃).
𝑖 𝑖
𝑖=1 𝑖=1
Taking the derivative and setting it equal to zero we get
𝑛
∑ 𝑘 ∑(𝑛 − 𝑘 ) ∑ 𝑘 ∑ 𝑘
𝑙′(𝜃) = 𝑖 − 𝑖 = 0 ⇒ 𝜃̂ = 𝑖=1 𝑖 = 𝑖 .
𝜃 1−𝜃 ∑ 𝑛 8 𝑛⋅8
𝑖=1
This is what we claimed at the start of the answer.
(b) Solution: Here’s the code with comments
data = c(6, 5, 5, 5, 7, 3)
size_binom = 8
n = length(data)
theta_hat = sum(data)/(n*size_binom) # from part a
n = length(sample) # number of sample points
# Generate the bootstrap samples using binom(size_binom, theta_hat)
# Each column is one bootstrap sample (of n resampled values)
n_boot = 100
18.05 class 24 problems, Spring 2022 3
x = rbinom(n*n_boot, size_binom, theta_hat)
bootstrap_sample = matrix(x, nrow=n, ncol=n_boot)
# Compute the bootstrap theta_star
theta_star = colSums(bootstrap_sample)/(n*size_binom)
# Compute the differences
delta_star = theta_star - theta_hat
# Find the 0.10 and 0.90 quantiles for delta_star
d = quantile(delta_star, c(0.1, 0.9))
# Calculate the 80% confidence interval for theta
ci = theta_hat - c(d[2], d[1])
s = sprintf("80%% confidence interval for theta: [%.3f, %.3f]", ci[1], ci[2])
cat(s, '\n')
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
