# Mit18 05 S22 Class17 Pset

---

Class 17 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. What would a frequentist say?
Each day Jaam arrives 𝑋 hours late to class, with 𝑋 ∼ uniform(0, 𝜃), where 𝜃 is unknown.
Jon models his initial belief about 𝜃 by a prior pdf 𝑓(𝜃). After Jaam arrives 𝑥 hours late to
the next class, Jon computes the likelihood function 𝜙(𝑥|𝜃) and the posterior pdf 𝑓(𝜃|𝑥).
Which of these probability computations would the frequentist consider valid?
1. none 5. prior and posterior
2. prior 6. prior and likelihood
3. likelihood 7. likelihood and posterior
4. posterior 8. prior, likelihood and posterior.
Concept question 2. Is it a statistic. Suppose 𝑥 , … , 𝑥 is a sample from N(𝜇, 𝜎2),
1 𝑛
where 𝜇 and 𝜎 are unknown.
Is each of the following a statistic?
(a) The median of 𝑥 , … , 𝑥 .
1 𝑛
(b) The interval from the 0.25 quantile to the 0.75 quantile of N(𝜇, 𝜎2).
𝑥 ̄ − 𝜇
(c) The standardized mean √ .
𝜎/ 𝑛
(d) The set of sample values less than 1 unit from 𝑥.̄
𝑥 − 5
(e) The 𝑧 = √ .
3/ 𝑛
𝑥 − 𝜇
(f) 𝑧 = √0, where 𝜇 and 𝜎 are given values,
𝜎 / 𝑛 0 0
0
Concept question 2. Picture the significance. The null and alternate pdfs are
shown on the following plot
𝜙(𝑥|𝐻 ) 𝜙(𝑥|𝐻 )
𝐴 0
𝑅
𝑅 3
2
𝑅 𝑅
1 4
𝑥
reject𝐻 region . non-reject𝐻 region
0 0
The significance level of the test is given by the area of which region?
1. 𝑅 5. 𝑅
1 2
2. 𝑅 6. 𝑅
3 4
3. 𝑅 + 𝑅 7. 𝑅 + 𝑅
1 2 2 3
4. 𝑅 +𝑅 +𝑅 8. None of these
2 3 4
1
18.05 class 17 problems, Spring 2022 2
Board questions
Problem 1. Testing coins
Suppose we have a coin with an unknown probability of heads 𝜃.
Test statistic 𝑥 = number of heads in 10 tosses.
Null hypothesis 𝐻 : 𝜃 = 0.5 (fair coin).
0
Alternative hypothesis 𝐻 : 𝜃 ≠ 0.5 (unfair coin, two-sided).
𝐴
(a) The rejection region is are the values of 𝑥 shown in orange. What’s the significance
level?
𝑝(𝑥|𝐻 )
0
.25
.15
.05
𝑥
0 1 2 3 4 5 6 7 8 9 10
𝑥 0 1 2 3 4 5 6 7 8 9 10
𝑝(𝑥|𝐻 ) 0.001 0.010 0.044 0.117 0.205 0.246 0.205 0.117 0.044 0.010 0.001
0
(b) For significance level 𝛼 = 0.05, find a two-sided rejection region.
Problem 2. z statistic
Suppose we know the following about our null hypothesis significance test.
• 𝐻 : data follows a 𝑁(5, 102)
0
• 𝐻 : data follows a 𝑁(𝜇, 102) where 𝜇 ≠ 5.
𝐴
• Test statistic: 𝑧 = standardized 𝑥.
• Data: 64 data points with 𝑥 = 6.25.
• Significance level set to 𝛼 = 0.05.
(a) Find the rejection region; draw a picture.
(b) Find the 𝑧-value; add it to your picture.
(c) Decide whether or not to reject 𝐻 in favor of 𝐻 .
0 𝐴
(d) Find the 𝑝-value for this data; add to your picture.
(e) What’s the connection between the answers to (b), (c) and (d)?
Problem 2. More coins
Two coins: probability of heads is 0.5 for 𝐶 ; and 0.6 for 𝐶 .
1 2
We pick one at random, flip it 8 times and get 6 heads.
Here are the probability tables for the two coins
18.05 class 17 problems, Spring 2022 3
k 0 1 2 3 4 5 6 7 8
𝑝(𝑘|𝜃 = 0.5) 0.004 0.031 0.109 0.219 0.273 0.219 0.109 0.031 0.004
𝑝(𝑘|𝜃 = 0.6) 0.001 0.008 0.041 0.124 0.232 0.279 0.209 0.090 0.017
(a) 𝐻 = ’The coin is 𝐶 ’ 𝐻 = ’The coin is 𝐶 ’
0 1 𝐴 2
Do you reject 𝐻 at the significance level 𝛼 = 0.05?
0
(Hint: First decide if this test is two-sided, left-sided or right-sided. Then determine the
rejection region.)
(b) 𝐻 = ’The coin is 𝐶 ’ 𝐻 = ’The coin is 𝐶 ’
0 2 𝐴 1
Do you reject 𝐻 at the significance level 𝛼 = 0.05?
0
(c) Do your answers to (a) and (b) seem paradoxical
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
