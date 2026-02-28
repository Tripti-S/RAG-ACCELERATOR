# Mit18 05 S22 Class05A Pset Sol

---

Class 5 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. Order the variance
The graphs below give the pmf for 3 random variables.
(A) (B)
𝑥 𝑥
1 2 3 4 5 1 2 3 4 5
(C)
𝑥
1 2 3 4 5
Order them by size of standard deviation from biggest to smallest. (Assume 𝑥 has the same
units in all three.)
1. ABC 2. ACB 3. BAC 4. BCA 5. CAB 6. CBA
Solution: 5. CAB
All 3 variables have the same range from 1-5 and all of them are symmetric so their mean
is right in the middle at 3. (C) has most of its weight at the extremes, so it has the biggest
spread. (B) has the most weight in the middle so it has the smallest spread.
From biggest to smallest standard deviation we have (C), (A), (B).
Concept question 2. Zero variance
Suppose 𝑋 is a discrete random variable,
True or False: If Var(𝑋) = 0 then 𝑋 is constant.
Solution: True. If 𝑋 can take more than one value with positive probability, than Var(𝑋)
will be a sum of positive terms. So, 𝑋 is constant if and only if Var(𝑋) = 0.
Concept question 3. Standard deviation
Make an intuitive guess: Which pmf has the bigger standard deviation? (Assume 𝑤 and 𝑦
have the same units.)
pmffor𝑌 𝑝(𝑦) 𝑝(𝑊) pmffor𝑊
1/2
0.4
0.2
0.1
𝑦 𝑤
-3 0 3 10 20 30 40 50
1. 𝑌 2. 𝑊
1
18.05 class 5 problems, Spring 2022 2
Solution: The scales along the horizontal axis are so different, that, even though 𝑊 is
more packed towards the center, the bigger scale means its standard deviation is probably
larger.
You can compute that Var(𝑌) = 9 and Var(𝑊) = 120.
Concept question 4.
Suppose 𝑋 is a continuous random variable.
(a) If the pdf of 𝑋 is 𝑓(𝑥) can there be an 𝑥 where 𝑓(𝑥) = 10?
(b) What is 𝑃(𝑋 = 𝑎)?
(c) Does 𝑃(𝑋 = 𝑎) = 0 mean 𝑋 never equals 𝑎?
Solution: (a) Yes. This is a density, it can be greater than 1. Probabilities must be less
than 1.
(b) 0
(c) No. For a continuous distribution any single value has probability 0. Only a range of
values has non-zero probability.
Concept question 5.
Which of the following are graphs of valid cumulative distribution functions?
A. B. C. D.
1 1 1 1
𝑥 𝑥 𝑥 𝑥
−4 −2 2 4 −4 −2 2 4 −4 −2 2 4 −4 −2 2 4
−0.5 −0.5 −0.5 −0.5 Solution: Test 2
and Test 3.
Graph A is not a cdf: it takes negative values, but probabilities are positive.
Graph B is a cdf: it increases from 0 to 1.
Graph C is a cdf: it increases from 0 to 1.
Graph D is not a cdf because has a decreasing part. A cdf must be non-decreasing since it
represents accumulated probability.
Board questions
Problem 1.
(a) Let 𝑋 ∼ Bernoulli(𝑝). Compute Var(𝑋).
(b) Let 𝑌 ∼ Bin(𝑛, 𝑝). Show Var(𝑌) = 𝑛𝑝(1−𝑝).
(c) Suppose 𝑋 , 𝑋 , … , 𝑋 are independent and all have the same standard deviation 𝜎 = 2.
1 2 𝑛
Let 𝑋 be the average of 𝑋 , … , 𝑋 .
1 𝑛
What is the standard deviation of 𝑋?
(a) Solution: For 𝑋 ∼ Bernoulli(𝑝) we use a table. (We know 𝐸[𝑋] = 𝑝.)
18.05 class 5 problems, Spring 2022 3
𝑋 0 1
𝑝(𝑥) 1 − 𝑝 𝑝
(𝑋 − 𝜇)2 𝑝2 (1 − 𝑝)2
Var(𝑋) = 𝐸[(𝑋 − 𝜇)2] = (1 − 𝑝)𝑝2 + 𝑝(1 − 𝑝)2 = 𝑝(1 − 𝑝)
(b) 𝑌 ∼ bin(𝑛, 𝑝) means 𝑌 is the sum of 𝑛 independent Bernoulli(𝑝) random variables 𝑌 ,
1
𝑌 , …, 𝑌 . For independent variables, the variances add. Since Var(𝑌 ) = 𝑝(1 − 𝑝) we have
2 𝑛 𝑗
Var(𝑌) = Var(𝑌 ) + Var(𝑌 ) + … + Var(𝑌 ) = 𝑛𝑝(𝑝 − 1).
1 2 𝑛
(c) Since the variables are independent, we have
Var(𝑋 + … + 𝑋 ) = 4𝑛.
1 𝑛
𝑋 is the sum scaled by 1/𝑛 and the rule for scaling is Var(𝑎𝑋) = 𝑎2Var(𝑋), so
𝑋 +⋯+𝑋 1 4
Var(𝑋) = Var( 1 𝑛 ) = Var(𝑋 +…+𝑋 ) = .
𝑛 𝑛2 1 𝑛 𝑛
2
This implies 𝜎 = √ .
𝑋 𝑛
Note: this says that the average of 𝑛 independent measurements varies less than the indi-
vidual measurements.
Problem 2.
Suppose 𝑋 has range [0, 2] and pdf 𝑓(𝑥) = 𝑐 𝑥2.
(a) What is the value of 𝑐?
(b) Compute the cdf 𝐹 (𝑥).
(c) Compute 𝑃(1 ≤ 𝑋 ≤ 2).
(d) Plot the pdf and use it to illustrate part (c).
(a) Solution: Total probability must be 1. So
2 2 8 3
∫ 𝑓(𝑥)𝑑𝑥 = ∫ 𝑐𝑥2𝑑𝑥 = 𝑐 = 1 ⇒ 𝑐 = .
3 8
0 0
(b) The pdf 𝑓(𝑥) is 0 outside of [0, 2] so for 0 ≤ 𝑥 ≤ 2 we have
𝑥 𝑐 𝑥3
𝐹 (𝑥) = ∫ 𝑐𝑢2 𝑑𝑢 = 𝑥3 = .
3 8
0
𝐹 (𝑥) is 0 fo 𝑥 < 0 and 1 for 𝑥 > 2.
2
(c) We could compute the probability as ∫ 𝑓(𝑥)𝑑𝑥, but rather than redo the integral let’s
1
use the cdf:
1 7
𝑃(1 ≤ 𝑋 ≤ 2) = 𝐹(2)−𝐹(1) = 1− = .
8 8
18.05 class 5 problems, Spring 2022 4
Problem 3.
Suppose 𝑌 has range [0, 𝑏] and cdf 𝐹 (𝑦) = 𝑦2/9.
(a) What is 𝑏?
(b) Find the pdf of 𝑌 .
Solution: (a) Since the total probability is 1, we have
𝑏2
𝐹(𝑏) = 1 ⇒ = 1 ⇒ 𝑏 = 3 .
9
2𝑦
(b) 𝑓(𝑦) = 𝐹 ′(𝑦) = .
9
Problem 4.
I’ve noticed that taxis drive past 77 Mass. Ave. on the average of once every 10 minutes.
Suppose time spent waiting for a taxi is modeled by an exponential random variable
1
𝑋 ∼ Exponential(1/10); 𝑓(𝑥) = e−𝑥/10
10
(a) Sketch the pdf of this distribution
(b) Shade the region which represents the probability of waiting between 3 and 7 minutes
(c) Compute the probability of waiting between between 3 and 7 minutes for a taxi
(d) Compute and sketch the cdf.
Solution: Sketches for (a), (b), (d)
𝑃(3<𝑋<7)
0.1 𝐹(𝑥)=1−e−𝜆𝑥
1
𝑓(𝑥)=𝜆e−𝜆𝑥
𝑥 𝑥
2 4 6 8 10121416 2 4 6 8 10 12 14 16
(c)
7 1 7
(3 < 𝑋 < 7) = ∫ e−𝑥/10 𝑑𝑥 = −e−𝑥/10∣ = e−3/10 − e−7/10 ≈ 0.244
10 3
3
In class examples and discussion
Example. Computation from tables
Compute the variance and standard deviation of 𝑋.
values 𝑥 1 2 3 4 5
pmf 𝑝(𝑥) 1/10 2/10 4/10 2/10 1/10
Solution: From the table we compute the mean:
1 4 12 8 5
𝜇 = 𝐸[𝑋] = + + + + = 3.
10 10 10 10 10
18.05 class 5 problems, Spring 2022 5
Then we add a line to the table for (𝑋 − 𝜇)2.
values 𝑋 1 2 3 4 5
pmf 𝑝(𝑥) 1/10 2/10 4/10 2/10 1/10
(𝑋 − 𝜇)2 4 1 0 1 4
Using the new table we compute variance 𝐸[(𝑋 − 𝜇)2]:
1 2 4 2 1
⋅4+ ⋅1+ ⋅0+ ⋅1+ ⋅4 = 1.2
10 10 10 10 10
√
The standard deviation is then 𝜎 = 1.2.
Example. A very useful formula
Recompute the previous example using the very useful formula for variance
𝑛
Var(𝑋) = 𝐸[𝑋2]−𝐸[𝑋]2 = (∑𝑝(𝑥 )𝑥2)−𝜇2.
𝑖 𝑖
𝑖=1
Solution: Here is the table
values 𝑋 1 2 3 4 5
pmf 𝑝(𝑥) 1/10 2/10 4/10 2/10 1/10
𝑋2 1 4 9 16 25
We know 𝐸[𝑋] = 3. We compute
1 2 4 2 1 102
𝐸[𝑋2] = ⋅1+ ⋅4+ ⋅9+ ⋅16+ ⋅25 =
10 10 10 10 10 10
102 12
So Var(𝑋) = 𝐸[𝑋2] − 𝐸[𝑋] 2 = − 9 = = 1.2
10 10
Extra problems
Extra 1. Let 𝑋 take value 1, with equal probability on {1, 2, 3, 4, 5} (𝑋 is a uniform
random variable). Compute Var(𝑋).
Let 𝑌 be uniform on {7, 8, 9, 10, 11}. What is the variance of 𝑌 ?
1+2+3+4+5 1+4+9+16+25
Solution: 𝐸[𝑋] = = 3. 𝐸[𝑋2] = = 11. So,
5 5
Var(𝑋) = 𝐸[𝑋]2 − 𝐸[𝑋]2 = 11 − 9 = 2 .
Since 𝑌 = 𝑋+6, Var(𝑌) = Var(𝑋) = 2.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
