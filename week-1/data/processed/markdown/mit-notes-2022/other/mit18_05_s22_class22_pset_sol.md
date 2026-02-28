# Mit18 05 S22 Class22 Pset Sol

---

Class 22 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. Critical values
𝑃(𝑍 ≤𝑞 ) 𝑃(𝑍 >𝑧 )
𝛼 𝛼
𝛼 𝛼
𝑧
𝑞 𝑧
𝛼 𝛼
1. 𝑧 =
0.025
(a) -1.96 (b) -0.95 (c) 0.95 (d) 1.96 (e) 2.87
2. −𝑧 =
0.16
(a) -1.33 (b) -0.99 (c) 0.99 (d) 1.33 (e) 3.52
1. Solution: 𝑧 = 1.96. By definition 𝑃 (𝑍 > 𝑧 ) = 0.025. This is the same as
0.025 0.025
𝑃 (𝑍 ≤ 𝑧 ) = 0.975. Either from memory, a table or using the R function qnorm(0.975)
0.025
we get the result.
2.Solution: −𝑧 = −0.99. We recall that 𝑃(|𝑍| < 1) ≈ 0.68. Since half the leftover
0.16
probability is in the right tail we have 𝑃(𝑍 > 1) ≈ 0.16. Thus 𝑧 ≈ 1, so −𝑧 ≈ −1.
0.16 0.16
Board questions
Problem 1. Computing confidence intervals
The data 4, 1, 2, 3 is drawn from N(𝜇, 𝜎2) with 𝜇 unknown.
(a) Find a 90% 𝑧 confidence interval for 𝜇, given that 𝜎 = 2.
For the remaining parts, suppose 𝜎 is unknown.
(b) Find a 90% 𝑡 confidence interval for 𝜇.
(c) Find a 90% 𝜒2 confidence interval for 𝜎2.
(d) Find a 90% 𝜒2 confidence interval for 𝜎.
(e) Given a normal sample with 𝑛 = 100, 𝑥 = 12, and 𝑠 = 5,
find the rule-of-thumb 95% confidence interval for 𝜇.
√ √
Solution: 𝑥 = 2.5, 𝑠2 = 1.667, 𝑠 = 1.29, 𝜎/ 𝑛 = 1, 𝑠/ 𝑛 = 0.645.
(a) 𝑧 ≈ 1.645: 90% 𝑧 confidence interval for 𝜇 is
0.05
𝜎 𝜎
[𝑥−𝑧 ⋅ √ , 𝑥+𝑧 ⋅ √ ] ≈ [0.856,4.144] = 2.5±1.645.
0.05 𝑛 0.05 𝑛
(b) 𝑡 ≈ 2.353 (3 degrees of freedom): 90% 𝑡 confidence interval for 𝜇 is
0.05
𝑠 𝑠
[𝑥 − 𝑡 ⋅ √ , 𝑥 + 𝑡 ⋅ √ ] ≈ [0.981, 4.019] = 2.5 ± 1.519
0.05 𝑛 0.05 𝑛
1
18.05 class 22 problems, Spring 2022 2
(c) 𝑐 ≈ 7.815, 𝑐 ≈ 0.352 (3 degrees of freedom): 90% 𝜒2 confidence interval for 𝜎2 is
0.05 0.95
(𝑛 − 1)𝑠2 (𝑛 − 1)𝑠2
[ , ] ≈ [0.640, 14.211].
𝑐 𝑐
0.05 0.95
(d) Take the square root of the interval in 3. [0.780, 3.770].
(e) The rule of thumb is written for 𝑧, but with 𝑛 = 100 the 𝑡(99) and standard normal
distributions are very close, so we can assume that 𝑡 ≈ 2. Thus the 95% confidence
0.025
interval is 12±2 ⋅5/10 = [11, 13].
Problem 2. Confidence intervals and non-rejection regions
Suppose 𝑥 ,…,𝑥 ∼ N(𝜇, 𝜎2) with 𝜎 known.
1 𝑛
Consider two intervals:
1. The 𝑧 confidence interval around 𝑥 at confidence level 1 − 𝛼.
2. The 𝑧 non-rejection region for 𝐻 ∶ 𝜇 = 𝜇 at significance level 𝛼.
0 0
Compute and sketch these intervals to show that:
𝜇 is in the first interval ⇔ 𝑥 is in the second interval.
0
Solution:
𝜎
Confidence interval: 𝑥 ± 𝑧 ⋅ √
𝛼/2 𝑛
𝜎
Non-rejection region: 𝜇 ± 𝑧 ⋅ √
0 𝛼/2 𝑛
Since the intervals are the same width they either both contain the other’s center or neither
one does.
𝑁(𝜇 ,𝜎2/𝑛)
0
𝑥
𝜇 −𝑧 ⋅ √𝜎 𝜇 +𝑧 ⋅ √𝜎
𝑥 2 0 𝛼/2 𝑛 𝜇 0 𝑥 1 0 𝛼/2 𝑛
Problem 3. Polling
For a poll to find the proportion 𝜃 of people supporting X we know that a (1 − 𝛼) confidence
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
18.05 class 22 problems, Spring 2022 3
√
Solution: (a) Need 1/ 𝑛 = 0.01 So 𝑛 = 10000.
𝑧
𝛼/2
(b) 𝛼 = 0.2, so 𝑧 = qnorm(0.9) = 1.2816. So we need √ = 0.01. This gives
𝛼/2 2 𝑛
𝑛 = 4106.
1 1
(c) 95% interval: 𝑥± √ = 𝑥± = 𝑥±0.0333
𝑛 30
1 1
80% interval: 𝑥 ± 𝑧 ⋅ √ = 𝑥 ± 1.2816 ⋅ = 𝑥 ± 0.021.
0.1 2 𝑛 60
Discussion questions
1. Width of confidence intervals
The quantities 𝑛, 𝑐 = confidence, 𝑥, 𝜎 all appear in the 𝑧 confidence interval for the mean.
How does the width of a confidence interval for the mean change if:
1. We increase 𝑛 and leave the others unchanged?
2. We increase 𝑐 and leave the others unchanged?
3. We increase 𝜇 and leave the others unchanged?
4. We increase 𝜎 and leave the others unchanged?
(A) it gets wider (B) it gets narrower (C) it stays the same.
Solution: 1. Narrower. More data decreases the variance of 𝑥̄
2. Wider. Greater confidence requires a bigger interval.
3. No change. Changing 𝜇 will tend to shift the location of the intervals.
4. Wider. Increasing 𝜎 will increase the uncertainty about 𝜇.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
