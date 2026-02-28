# Mit18 05 S22 Class16 Pset Sol

---

Class 16 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. Increasing probability
To convert an 80% probability interval to a 90% interval should you shrink it or stretch it?
1. Shrink 2. Stretch.
Solution: 2. Stretch. A bigger probability requires a bigger interval.
Board questions
Problem 1. Treating severe respiratory failure*
Two treatments for newborns with severe respiratory failure.
1. CVT: conventional therapy (hyperventilation and drugs)
2. ECMO: extracorporeal membrane oxygenation (invasive procedure)
In 1983 in Michigan:
19/19 ECMO babies survived and 0/3 CVT babies survived.
Later Harvard ran a randomized study:
28/29 ECMO babies survived and 6/10 CVT babies survived.
*Adapted from Statistics: a Bayesian Perspective by Donald Berry
Name the probabilites of survival:
𝜃 = probability that an ECMO baby survives
𝐸
𝜃 = probability that a CVT baby survives.
𝐶
Consider the values 0.125, 0.375, 0.625, 0.875 for 𝜃 and 𝜃 .
𝐸 𝐶
(a) Make the 4×4 prior table for a flat prior.
(b) Based on the Michigan results, create a reasonable informed prior table for analyzing
the Harvard results (unnormalized is fine).
(c) Make the likelihood table for the Harvard results. (You might use R to compute some
of the values.)
(d) Find the posterior table for the informed prior.
(e) Using the informed posterior, compute the probability that ECMO is better than CVT.
(f) Also compute the posterior probability that 𝜃 − 𝜃 ≥ 0.6.
𝐸 𝐶
(The posted solutions will also show 4-6 for the flat prior.)
Solution: (a) Flat prior
1
18.05 class 16 problems, Spring 2022 2
𝜃
𝐸
0.125 0.375 0.625 0.875
0.125 0.0625 0.0625 0.0625 0.0625
𝜃 0.375 0.0625 0.0625 0.0625 0.0625
𝐶
0.625 0.0625 0.0625 0.0625 0.0625
0.875 0.0625 0.0625 0.0625 0.0625
(b) Informed prior (This table is unnormalized)
𝜃
𝐸
0.125 0.375 0.625 0.875
0.125 18 18 32 32
𝜃 0.375 18 18 32 32
𝐶
0.625 18 18 32 32
0.875 18 18 32 32
Rationale: Since 19/19 ECMO babies survived we believe 𝜃 is probably near 1.0. That
𝐸
0/3 CVT babies survived is not enough data to move from a uniform distribution. (Or we
might distribute a little more probability to larger 𝜃 .) So for 𝜃 we split 64% of probability
𝐶 𝐸
in the two higher values and 36% for the lower two. Our prior is the same for each value of
𝜃 .
𝐶
(c) Likelihood
Entries in the likelihood table: 𝑐𝜃28(1 − 𝜃 )𝜃6 (1 − 𝜃 )4. The constant 𝑐 is computed from
𝐸 𝐸 𝐶 𝐶
binomial coeﬀicients. It is unimportant for updating. The table was computed using R.
𝜃
𝐸
0.125 0.375 0.625 0.875
0.125 6.160e-28 1.007e-14 9.835e-09 4.048e-05
𝜃 0.375 1.169e-25 1.910e-12 1.866e-06 7.682e-03
𝐶
0.625 3.247e-25 5.306e-12 5.184e-06 2.134e-02
0.875 3.019e-26 4.932e-13 4.819e-07 1.984e-03
Extra: flat posterior
The posterior table is found by multiplying the prior and likelihood tables and normalizing
so that the sum of the entries is 1. We call the posterior derived from the flat prior the flat
posterior. (Of course the flat posterior is not itself flat.)
𝜃
𝐸
0.125 0.375 0.625 0.875
0.125 1.984e-26 3.242e-13 3.167e-07 0.001
𝜃 0.375 3.765e-24 6.152e-11 6.011e-05 0.247
𝑐
0.625 1.046e-23 1.709e-10 1.670e-04 0.687
0.875 9.721e-25 1.588e-11 1.552e-05 0.0639
The boxed entries represent most of the probability where 𝜃 > 𝜃 .
𝐸 𝐶
All our computations were done in R. For the flat posterior:
Probability ECMO is better than CVT is
𝑃 (𝜃 > 𝜃 | Harvard data) = 0.936
𝐸 𝐶
𝑃 (𝜃 − 𝜃 ≥ 0.6 | Harvard data) = 0.001
𝐸 𝐶
18.05 class 16 problems, Spring 2022 3
(d) Informed posterior
𝜃
𝐸
0.125 0.375 0.625 0.875
0.125 1.116e-26 1.823e-13 3.167e-07 0.001
𝜃 0.375 2.117e-24 3.460e-11 6.010e-05 0.2473
𝐶
0.625 5.882e-24 9.612e-11 1.669e-04 0.6871
0.875 5.468e-25 8.935e-12 1.552e-05 0.0638
For the informed posterior:
𝑃 (𝜃 > 𝜃 | Harvard data) = 0.936
𝐸 𝐶
𝑃 (𝜃 − 𝜃 ≥ 0.6 | Harvard data) = 0.001
𝐸 𝐶
Note: Since both flat and informed prior gave essentially the same answers, we gain con-
fidence that these calculations are robust. That is, they are not too sensitive to our exact
choice of prior.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
