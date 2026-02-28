# Mit18 05 S22 Class07 Pset

---

Class 7 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. Independence I
Roll two dice: 𝑋 = value on first, 𝑌 = value on second
𝑋\𝑌 1 2 3 4 5 6 𝑝(𝑥 )
𝑖
1 1/36 1/36 1/36 1/36 1/36 1/36 1/6
2 1/36 1/36 1/36 1/36 1/36 1/36 1/6
3 1/36 1/36 1/36 1/36 1/36 1/36 1/6
4 1/36 1/36 1/36 1/36 1/36 1/36 1/6
5 1/36 1/36 1/36 1/36 1/36 1/36 1/6
6 1/36 1/36 1/36 1/36 1/36 1/36 1/6
𝑝(𝑦 ) 1/6 1/6 1/6 1/6 1/6 1/6 1
𝑗
Are 𝑋 and 𝑌 independent? 1. Yes 2. No
Concept question 2. Independence II
Roll two dice: 𝑋 = value on first, 𝑇 = sum
𝑋\𝑇 2 3 4 5 6 7 8 9 10 11 12 𝑝(𝑥)
𝑖
1 1/36 1/36 1/36 1/36 1/36 1/36 0 0 0 0 0 1/6
2 0 1/36 1/36 1/36 1/36 1/36 1/36 0 0 0 0 1/6
3 0 0 1/36 1/36 1/36 1/36 1/36 1/36 0 0 0 1/6
4 0 0 0 1/36 1/36 1/36 1/36 1/36 1/36 0 0 1/6
5 0 0 0 0 1/36 1/36 1/36 1/36 1/36 1/36 0 1/6
6 0 0 0 0 0 1/36 1/36 1/36 1/36 1/36 1/36 1/6
𝑝(𝑦 ) 1/36 2/36 3/36 4/36 5/36 6/36 5/36 4/36 3/36 2/36 1/36 1
𝑗
Are 𝑋 and 𝑌 independent? 1. Yes 2. No
Concept question 3. Independence III
Which of the following joint pdfs are the variables independent? (Each of the ranges is a
rectangle chosen so that ∫∫𝑓(𝑥,𝑦)𝑑𝑥𝑑𝑦 = 1.)
(i) 𝑓(𝑥,𝑦) = 4𝑥2𝑦3.
(ii) 𝑓(𝑥,𝑦) = 1(𝑥3𝑦+𝑥𝑦3).
2
(iii) 𝑓(𝑥,𝑦) = 6𝑒−3𝑥−2𝑦
(a) i (b) ii (c) iii (d) i, ii
(e) i, iii (f) ii, iii (g) i, ii, iii (h) None
1
18.05 class 7 problems, Spring 2022 2
Board questions
Problem 1. Joint distributions
Suppose 𝑋 and 𝑌 are random variables and
• (𝑋, 𝑌 ) takes values in [0,1] × [0,1].
• the pdf is 𝑓(𝑥,𝑦) = 𝑥+𝑦.
(a) Show 𝑓(𝑥, 𝑦) is a valid pdf.
(b) Visualize the event 𝐴 = ‘𝑋 > 0.3 and 𝑌 > 0.5’. Find its probability.
(c) Find the cdf 𝐹 (𝑥, 𝑦).
(d) Use the cdf 𝐹 (𝑥, 𝑦) to find the marginal cdf 𝐹 (𝑥) and 𝑃 (𝑋 < 0.5).
𝑋
(e) Find the marginal pdf 𝑓 (𝑥). Use this to find 𝑃 (𝑋 < 0.5).
𝑋
(f) (New scenario) From the following table compute 𝐹 (3.5, 4).
𝑋\𝑌 1 2 3 4 5 6
1 1/36 1/36 1/36 1/36 1/36 1/36
2 1/36 1/36 1/36 1/36 1/36 1/36
3 1/36 1/36 1/36 1/36 1/36 1/36
4 1/36 1/36 1/36 1/36 1/36 1/36
5 1/36 1/36 1/36 1/36 1/36 1/36
6 1/36 1/36 1/36 1/36 1/36 1/36
Problem 2. Covariance and correlation
Flip a fair coin 11 times. (The tosses are all independent.)
Let 𝑋 = number of heads in the first 6 flips
Let 𝑌 = number of heads on the last 6 flips.
Compute Cov(𝑋,𝑌 ) and Cor(𝑋, 𝑌 ).
Problem 3. Even more tosses
Toss a fair coin 2𝑛 + 1 times. Let 𝑋 be the number of heads on the first 𝑛 + 1 tosses and
𝑌 the number on the last 𝑛 + 1 tosses.
Compute Cov(𝑋,𝑌 ) and Cor(𝑋, 𝑌 ).
Extra
Discussion: Real-life correlations
• Over time, amount of ice cream consumption is correlated with number of pool drown-
ings.
18.05 class 7 problems, Spring 2022 3
• In 1685 (and today) being a student is the most dangerous profession. That is, the
average age of those who die is less than any other profession.
• In 90% of bar fights ending in a death the person who started the fight died.
• Hormone replacement therapy (HRT) is correlated with a lower rate of coronary heart
disease (CHD).
Extra problem 1: Hospitals, binomial, CLT etc.
Here’s one more problem. We won’t do this in class.
• A certain town is served by two hospitals.
• Larger hospital: about 45 babies born each day.
• Smaller hospital about 15 babies born each day.
• For a period of 1 year, each hospital recorded the days on which more than 60% of
the babies born were boys.
(a) Which hospital do you think recorded more such days?
(i) The larger hospital. (ii) The smaller hospital.
(iii) About the same (that is, within 5% of each other).
(b) Assume exactly 45 and 15 babies are born at the hospitals each day. Let 𝐿 (resp.,
𝑖
𝑆 ) be the Bernoulli random variable which takes the value 1 if more than 60% of the
𝑖
babies born in the larger (resp., smaller) hospital on the 𝑖th day were boys. Determine the
distribution of 𝐿 and of 𝑆 .
𝑖 𝑖
(c) Let 𝐿 (resp., 𝑆) be the number of days on which more than 60% of the babies born in
the larger (resp., smaller) hospital were boys. What type of distribution do 𝐿 and 𝑆 have?
Compute the expected value and variance in each case.
(d) Via the CLT, approximate the 0.84 quantile of 𝐿 (resp., 𝑆). Would you like to revise
your answer to part (a)?
(e) What is the correlation of 𝐿 and 𝑆? What is the joint pmf of 𝐿 and 𝑆? Visualize the
region corresponding to the event 𝐿 > 𝑆. Express 𝑃(𝐿 > 𝑆) as a double sum.
Extra problem 2: Correlation
(a) Flip a coin 3 times. Use a joint pmf table to compute the covariance and correlation
between the number of heads on the first 2 and the number of heads on the last 2 flips.
(b) Flip a coin 5 times. Use properties of covariance to compute the covariance and corre-
lation between the number of heads on the first 3 and last 3 flips.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
