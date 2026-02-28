# Mit18 05 S22 Class05A Pset

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
Concept question 2. Zero variance
Suppose 𝑋 is a discrete random variable,
True or False: If Var(𝑋) = 0 then 𝑋 is constant.
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
Concept question 4.
Suppose 𝑋 is a continuous random variable.
(a) If the pdf of 𝑋 is 𝑓(𝑥) can there be an 𝑥 where 𝑓(𝑥) = 10?
(b) What is 𝑃(𝑋 = 𝑎)?
(c) Does 𝑃(𝑋 = 𝑎) = 0 mean 𝑋 never equals 𝑎?
1
18.05 class 5 problems, Spring 2022 2
Concept question 5.
Which of the following are graphs of valid cumulative distribution functions?
A. B. C. D.
1 1 1 1
𝑥 𝑥 𝑥 𝑥
−4 −2 2 4 −4 −2 2 4 −4 −2 2 4 −4 −2 2 4
−0.5 −0.5 −0.5 −0.5
Board questions
Problem 1.
(a) Let 𝑋 ∼ Bernoulli(𝑝). Compute Var(𝑋).
(b) Let 𝑌 ∼ Bin(𝑛, 𝑝). Show Var(𝑌) = 𝑛𝑝(1−𝑝).
(c) Suppose 𝑋 , 𝑋 , … , 𝑋 are independent and all have the same standard deviation 𝜎 = 2.
1 2 𝑛
Let 𝑋 be the average of 𝑋 , … , 𝑋 .
1 𝑛
What is the standard deviation of 𝑋?
Problem 2.
Suppose 𝑋 has range [0, 2] and pdf 𝑓(𝑥) = 𝑐 𝑥2.
(a) What is the value of 𝑐?
(b) Compute the cdf 𝐹 (𝑥).
(c) Compute 𝑃(1 ≤ 𝑋 ≤ 2).
(d) Plot the pdf and use it to illustrate part (c).
Problem 3.
Suppose 𝑌 has range [0, 𝑏] and cdf 𝐹 (𝑦) = 𝑦2/9.
(a) What is 𝑏?
(b) Find the pdf of 𝑌 .
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
18.05 class 5 problems, Spring 2022 3
In class examples and discussion
Example. Computation from tables
Compute the variance and standard deviation of 𝑋.
values 𝑥 1 2 3 4 5
pmf 𝑝(𝑥) 1/10 2/10 4/10 2/10 1/10
Example. A very useful formula
Recompute the previous example using the very useful formula for variance
𝑛
Var(𝑋) = 𝐸[𝑋2]−𝐸[𝑋]2 = (∑𝑝(𝑥 )𝑥2)−𝜇2.
𝑖 𝑖
𝑖=1
Extra problems
Extra 1. Let 𝑋 take value 1, with equal probability on {1, 2, 3, 4, 5} (𝑋 is a uniform
random variable). Compute Var(𝑋).
Let 𝑌 be uniform on {7, 8, 9, 10, 11}. What is the variance of 𝑌 ?
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
