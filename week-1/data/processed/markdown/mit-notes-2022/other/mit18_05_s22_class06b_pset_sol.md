# Mit18 05 S22 Class06B Pset Sol

---

Class 6b in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. Normal distributions
𝑋 has normal distribution, standard deviation 𝜎.
within 1⋅𝜎 ≈68%
Normal PDF within 2⋅𝜎 ≈95%
within 3⋅𝜎 ≈99%
68%
95%
99%
𝑧
𝜇−3𝜎 𝜇−2𝜎 𝜇−𝜎 𝜇 𝜇+𝜎 𝜇+2𝜎 𝜇+3𝜎
(a) 𝑃(−𝜎 < 𝑋 −𝜇 < 𝜎) is approximately
(i) 0.025 (ii) 0.16 (iii) 0.68 (iv) 0.84 (v) 0.95
(b) 𝑃 (𝑋 > 𝜇 + 2𝜎) is approximately
(i) 0.025 (ii) 0.16 (iii) 0.68 (iv) 0.84 (v) 0.95
Solution: (a) Correct answer is (iii). The rule of thumb says the probability that 𝑋 is
within one standard deviation of the mean is 0.68.
(b) Correct answer is (i). This question for the probability in the right tail, beyond 2
standard deviations above the mean. The rule of thumb is that about 95% of the probability
is within 2𝜎 of the mean. So about 5% is outside of that. Since this is split symmetrically
between two tails, the probability in the right tail is approximately 0.025.
Board questions
Problem 1. Standardization
Suppose 𝑋 is a random variable with mean 𝜇 and standard deviation 𝜎. Let 𝑍 be the
standardization of 𝑋.
(a) Give the formula for 𝑍 in terms of 𝑋, 𝜇 and 𝜎.
(b) Use the algebraic properties of mean and variance to show 𝑍 has mean 0 and standard
deviation 1.
𝑋 −𝜇
Solution: (a) 𝑍 = .
𝜎
(b) The problem asks us to verify that 𝐸[𝑍] = 0 and Var(𝑍) = 1.
We use the properties
𝐸[𝑎𝑋 + 𝑏] = 𝑎𝐸[𝑋] + 𝑏 = 𝑎𝜇 + 𝑏
Var(𝑎𝑋 + 𝑏) = 𝑎2Var(𝑋) = 𝑎2𝜎2.
1
18.05 class 6b problems, Spring 2022 2
In the following, don’t forget that 𝐸[𝑋] = 𝜇 and Var(𝑋) = 𝜎2.
𝑋−𝜇 1 1
𝐸[𝑍] = 𝐸[ ] = 𝐸 [𝑋−𝜇] = (𝐸[𝑋]−𝜇) = 0.
𝜎 𝜎 𝜎
𝑋−𝜇 1 1 1
Var(𝑍) = Var ( ) = Var(𝑋−𝜇) = Var(𝑋) = ⋅𝜎2 = 1.
𝜎 𝜎2 𝜎2 𝜎2
Problem 2. CLT
(a) Carefully write the statement of the central limit theorem.
(b) To head the newly formed US Dept. of Statistics, suppose that 50% of the population
supports the team of Alessandre, Gabriel, Sarah and So Hee, 25% support Jen and 25%
support Jerry.
A poll asks 400 random people who they support. What is the probability that at least 55%
of those polled prefer the team?
(c) What is the probability that less than 20% of those polled prefer Jen?
Solution: (b) Let 𝑋 be the fraction polled who support the team. So 𝑋 is the average of
400 Bernoulli(0.5) random variables. That is, let 𝑋 = 1 if the ith person polled prefers the
𝑖
team and 0 if not, so 𝑋 = average of the 𝑋 .
𝑖
The question asks for the probability 𝑋 > 0.55.
Each 𝑋 has 𝜇 = 0.5 and 𝜎2 = 0.25. So, 𝐸[𝑋] = 0.5 and 𝜎2 = 0.25/400 or 𝜎 =
𝑖 𝑋 𝑋
1/40 = 0.025.
Because 𝑋 is the average of 400 Bernoulli(0.5) variables, the CLT says it is approximately
normal and standardizing gives
𝑋 −0.5
≈ 𝑍
0.025
So,
𝑃 (𝑋 > 0.55) ≈ 𝑃 (𝑍 > 2) ≈ 0.025.
(c) Let 𝐽 ̄ be the fraction polled who support Jen. The question asks for the probability
that 𝐽 ̄< 0.2.
Similar to part (b), 𝐽 ̄ is the average of 400 Bernoulli(0.25) random variables. So,
√
𝐸[𝐽]̄ = 0.25 and 𝜎2 = (0.25)(0.75)/400 ⇒ 𝜎 = 3/80.
𝑆 𝑆
𝐽 ̄ − 0.25
So, √ ≈ 𝑍. Thus,
3/80
√
𝑃(𝐽 ̄< 0.2) ≈ 𝑃(𝑍 < −4/ 3) = pnorm(−4/sqrt(3), 0, 1) ≈ 0.0105
Problem 3. Sampling from the standard normal distribution
How would you approximate a single random sample from a standard normal distribution
using 9 rolls of a ten-sided die?
Note: 𝜇 = 5.5 and 𝜎2 = 8.25 for a single roll of a 10-sided die.
Hint: CLT is about averages.
18.05 class 6b problems, Spring 2022 3
Solution: The average of 9 rolls is a sample from the average of 9 independent random
variables. The CLT says this average is approximately normal with 𝜇 = 5.5 and 𝜎 =
√8.25/9 = 0.957
If 𝑥 is the average of 9 rolls then standardizing we get
𝑥 − 5.5
𝑧 =
0.957
is (approximately) one sample from N(0, 1).
So, to approximate a standard normal, we would roll 9 times and compute 𝑧.
Histogram of standardized 9 roll simulation
ytisneD
−6 −4 −2 0 2 4 6
4.0
3.0
2.0
1.0
0.0
Standard normal is shown in orange.
𝑋 = average of nine rolls: 𝜇 = 5.5, 𝜎 = √8.25/9.
𝑋 −𝜇
Standarized statistic: 𝑍 = ≈ 𝑁(0,1).
𝜎
Extra problems
Bonus problem
An accountant rounds to the nearest dollar. We’ll assume the error in rounding is uniform
on [-0.5, 0.5]. Estimate the probability that the total error in 300 entries is more than $5.
Solution: Let 𝑋 be the error in the 𝑗th entry, so, 𝑋 ∼ 𝑈(−0.5,0.5).
𝑗 𝑗
We have 𝐸[𝑋 ] = 0 and Var(𝑋 ) = 1/12.
𝑗 𝑗
The total error 𝑆 = 𝑋 +…+𝑋 has 𝐸[𝑆] = 0, Var(𝑆) = 300/12 = 25, and 𝜎 = 5.
1 300 𝑆
Standardizing we get, by the CLT, 𝑆/5 is approximately standard normal. That is, 𝑆/5 ≈ 𝑍.
So, 𝑃(𝑆 < −5 or 𝑆 > 5) ≈ 𝑃(𝑍 < −1 or 𝑍 > 1) ≈ 0.32 .
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
