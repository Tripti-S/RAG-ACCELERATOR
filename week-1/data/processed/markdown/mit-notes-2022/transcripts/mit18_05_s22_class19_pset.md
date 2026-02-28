# Mit18 05 S22 Class19 Pset

---

Class 19 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. t-test odds
We run a two-sample 𝑡-test for equal means, with 𝛼 = 0.05, and obtain a 𝑝-value of 0.04.
What are the odds that the two samples are drawn from distributions with the same mean?
(a) 19/1 (b) 1/19 (c) 1/20 (d) 1/24 (e) unknown
Concept question 2. Multiple testing
(a) Suppose we have 6 treatments and want to know if the average recovery time is the
same for all of them. If we compare two at a time, how many two-sample 𝑡-tests do we need
to run?
(i) 1 (ii) 2 (iii) 6 (iv) 15 (v) 30
(b) Suppose we use the significance level 0.05 for each of the 15 tests. Assuming the null
hypothesis, what is the best estimate of the probability that we reject at least one of the
15 null hypotheses?
(i) < 0.05 (ii) 0.05 (iii) 0.10 (iv) > 0.25
Board questions
Problem 1. Khan’s restaurant
Sal is thinking of buying a restaurant and asks about the distribution of lunch customers.
The owner provides row one below. Sal records the data in row two himself one week.
M T W R F S
Owner’s distribution 0.1 0.1 0.15 0.2 0.3 0.15
Observed # of cust. 30 14 34 45 57 20
Set the significance level ahead of time.
𝐻 : the owner’s distribution is correct.
0
𝐻 : the owner’s distribution is not correct.
𝐴
Compute both 𝐺 and 𝑋2.
Run a chi-square goodness-of-fit test on the null hypotheses:
Problem 2. Genetic linkage
In 1905, William Bateson, Edith Saunders, and Reginald Punnett were examining flower
color and pollen shape in sweet pea plants by performing crosses similar to those carried
out by Gregor Mendel.
The genes for color and shape are given by:
Purple flowers (P) is dominant over red flowers (p).
Long seeds (L) is dominant over round seeds (l).
1
18.05 class 19 problems, Spring 2022 2
In the first generation there were only two genetic types PPLL and ppll. There initial cross
was always PPLL with ppll. So this always resulted in PpLl in the second generation. The
second generation plants were then crossed randomly with each other to make the third
generation.
F0: PPLL x ppll (initial cross)
F1: PpLl x PpLl (all second generation plants were PpLl)
F2: 2132 plants (third generation)
𝐻 = independent assortment: color and shape are inherited independently.
0
Here is the data from their experiment.
purple, long purple, round red, long red, round
Expected ? ? ? ?
Observed 1528 106 117 381
Determine the expected counts for 𝐹 under 𝐻 and find the 𝑝-value for a Pearson chi-square
2 0
test. Explain your findings biologically.
Problem 3. Recovery
The table shows recovery time in days for three medical treatments.
(a) Set up and run an F-test testing if the average recovery time is the same for all three
treatments. Use significance level 0.05.
(b) Based on the test, what might you conclude about the treatments?
𝑇 𝑇 𝑇
1 2 3
6 8 13
8 12 9
4 9 11
5 11 8
3 6 7
4 8 12
Note: For 𝛼 = 0.05, the critical value of 𝐹 is 3.68.
2,15
Problem 4. Chi-square for independence
(From Rice, Mathematical Statistics and Data Analysis, 2nd ed. p.489)
Consider the following contingency table of counts
Education Married once Married multiple times Total
College 550 61 611
No college 681 144 825
Total 1231 205 1436
Use a chi-square test with significance level 0.01 to test the hypothesis that the number of
marriages and education level are independent.
Question not used in class: z-test
We have 16 independent sample values 𝑥 , … , 𝑥 drawn from a Normal(𝜃, 82) distribution.
1 16
18.05 class 19 problems, Spring 2022 3
Suppose the sample mean 𝑥̄= 4. Run a 𝑧-test on this data for the null hypothesis 𝜃 = 2 vs
the alternative 𝜃 ≠ 2. Choose a significance of 𝛼 = 0.04.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
