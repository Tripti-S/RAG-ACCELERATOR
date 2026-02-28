# Mit18 05 S22 Class23 Pset

---

Class 23 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. Overnight polling
During the presidential election season, pollsters often do ‘overnight polls’ and report a
‘margin of error’ of about ±4%.
The number of people polled is in which of the following ranges?
(a) 0 – 50
(b) 50 –100
(c) 100 – 500
(d) 300 – 600
(e) 600 – 1000
Board questions
Problem 1. Confidence intervals for a binomial
For a poll to find the proportion 𝜃 of people supporting X we know that a (1−𝛼) confidence
interval for 𝜃 is given by
𝑧 𝑧
𝛼/2 𝛼/2
[ 𝑥 ̄ − √ , 𝑥 ̄ + √ ].
2 𝑛 2 𝑛
(a) How many people would you have to poll to have a margin of error of 0.01 with 95%
confidence? (You can do this in your head.)
(b) How many people would you have to poll to have a margin of error of 0.01 with 80%
confidence. (You’ll want R or other calculator here.)
(c) If 𝑛 = 900, compute the 95% and 80% confidence intervals for 𝜃.
Problem 2. Pivoting: confidence intervals and non-rejection regions
This question gets at the relationship between confidence intervals and non-rejection regions.
Main point: For a sample with sample mean 𝑥, the confidence interval consists of all
values 𝜇 for which a NHST with null hypothesis mean = 𝜇 would not reject on seeing 𝑥.
Assume we have independent data 𝑥 ,…,𝑥 ∼ 𝑁(𝜇,𝜎2), where 𝜇 is unknown and 𝜎 is
1 𝑛
known.
(a) For null hypothesis 𝜇 = 𝜇 give the two-sided non-rejection region for significance level
0
𝛼.
(b) Call the data average 𝑥. Give the 1 − 𝛼 confidence interval for 𝜇.
(c) Use the 𝑥, 𝜇-plane below. Note the conveniently included guides.
(i) Plot the horizontal line segment at height 𝜇 showing the non-rejection region for 𝐻 ∶
0 0
𝜇 = 𝜇 (significance level = 𝛼).
0
(ii) Plot the horizontal line segment at other heights showing the non-rejection region for
the corresponding 𝜇.
1
18.05 class 23 problems, Spring 2022 2
(iii) Plot the vertical line segments showing the 1 − 𝛼 confidence intervals around 𝑥 and 𝑥
1 2
(iv) Plot the vertical line segment at other values of 𝑥 showing the corresponding confidence
interval.
𝑧 𝜎
𝜇 𝜇=𝑥+ 𝛼√/2
𝑛
𝑧 𝜎
𝜇=𝑥− 𝛼√/2
𝑛
𝜇
0
𝑥
𝑥 𝑥
2 1
Understand how the main point connects with your graph.
Problem 3. Exact binomial confidence interval
This was not used in class, but it is a nice problem, so we included it here.
Use this table of binomial(8,𝜃) probabilities to:
1. find the (two-sided) rejection region with significance level 0.10 for each value of 𝜃.
2. Given 𝑥 = 7, find the 90% confidence interval for 𝜃.
3. Repeat for 𝑥 = 4.
𝜃\𝑥 0 1 2 3 4 5 6 7 8
0.1 0.430 0.383 0.149 0.033 0.005 0.000 0.000 0.000 0.000
0.3 0.058 0.198 0.296 0.254 0.136 0.047 0.010 0.001 0.000
0.5 0.004 0.031 0.109 0.219 0.273 0.219 0.109 0.031 0.004
0.7 0.000 0.001 0.010 0.047 0.136 0.254 0.296 0.198 0.058
0.9 0.000 0.000 0.000 0.000 0.005 0.033 0.149 0.383 0.430
Problem 4. Pivoting: Chi square confidence intervals for variance
This was not used in class, but it is a nice problem, so we included it here.
Assume we have independent data 𝑥 ,…,𝑥 ∼ 𝑁(𝜇,𝜎2 ), where 𝜎 is unknown and our
1 𝑛 true true
parameter of interest.
(𝑛 − 1)𝑠2
Let 𝑠2 be the sample variance. We know that ∼ 𝜒2(𝑛 − 1). Thus,
𝜎2
true
(𝑛 − 1)𝑠2
𝑃 (𝑐 ≤ ≤ 𝑐 |, 𝜎 = 𝜎) = 1−𝛼.
1−𝛼/2 𝜎2 𝛼/2 true
Here, 𝑐 is the right critical point for the 𝜒2(𝑛 − 1) distribution.
𝛼/2
18.05 class 23 problems, Spring 2022 3
Using this, for a two-sided significance test with with 𝐻 ∶ 𝜎 = 𝜎, the non-rejection
0 true
region for 𝑠2 at significance level 𝛼 is
𝑐 𝜎2 𝑐 𝜎2
1−𝛼/2 ≤ 𝑠2 ≤ 𝛼/2
𝑛−1 𝑛−1
Pivoting, we get the 1 − 𝛼 confidence interval for 𝜎2 produced by the data is
(𝑛 − 1)𝑠2 (𝑛 − 1)𝑠2
≤ 𝜎2 ≤
𝑐 𝑐
𝛼/2 1−𝛼/2
Display this graphically on the 𝜎2-𝑠2 axes shown.
𝑐 ⋅𝜎2
𝜎2 𝑠2 = 1−𝛼/2
𝑛−1
𝑐 ⋅𝜎2
𝑠2 = 𝛼/2
𝑛−1
𝜎2
0
𝑠2
𝑠2 𝑠2
2 1
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
