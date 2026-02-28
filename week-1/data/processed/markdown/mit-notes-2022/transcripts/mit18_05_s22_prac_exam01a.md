# Mit18 05 S22 Prac Exam01A

---

Exam 1 Practice Questions I, 18.05, Spring 2022
Notes.
Not every possible problem can be covered in 13 problems. Look at the other review
problems as well as the readings, psets and class problems.
Even the first 13 problems are much longer than the actual test will be,
Problem 1. In a ballroom dancing class the students are divided into group 𝐴 and group
𝐵. There are six people in group 𝐴 and seven in group 𝐵. If four 𝐴s and four 𝐵s are chosen
and paired off, how many pairings are possible?
Problem 2. Let 𝐴 and 𝐵 be two events. Suppose the probability that neither 𝐴 or 𝐵
occurs is 2/3. What is the probability that one or both occur?
Problem 3. Suppose you are taking a multiple-choice test with 𝑐 choices for each question.
In answering a question on this test, the probability that you know the answer is 𝑝. If you
don’t know the answer, you choose one at random. What is the probability that you knew
the answer to a question, given that you answered it correctly?
Problem 4. Two dice are rolled.
𝐴 = ‘sum of two dice equals 3’
𝐵 = ‘sum of two dice equals 7’
𝐶 = ‘at least one of the dice shows a 1’
(a) What is 𝑃 (𝐴|𝐶)?
(b) What is 𝑃 (𝐵|𝐶)?
(c) Are 𝐴 and 𝐶 independent? What about 𝐵 and 𝐶?
Problem 5. Suppose that 𝑃 (𝐴) = 0.4, 𝑃 (𝐵) = 0.3 and 𝑃((𝐴∪𝐵)𝐶) = 0.42. Are 𝐴 and
𝐵 independent?
Problem 6. Suppose that 𝑋 takes values between 0 and 1 and has probability density
function 2𝑥. Compute Var(𝑋) and Var(𝑋2).
Problem 7. Suppose 100 people all toss a hat into a box and then proceed to randomly
pick out of a hat. What is the expected number of people to get their own hat back.
Hint: express the number of people who get their own hat as a sum of random variables
whose expected value is easy to compute.
Problem 8. Let 𝑇 be the waiting time for customers in a queue. Suppose that 𝑇 is
exponential with pdf 𝑓(𝑡) = 2e−2𝑡 on [0, ∞).
Find the pdf of the rate at which customers are served 𝑅 = 1/𝑇 .
1
Exam 1 Practice I, Spring 2022 2
Problem 9. Suppose that the cdf of 𝑋 is given by:
⎧ 0 for 𝑎 < 0
{
{ 1 for 0 ≤ 𝑎 < 2
𝐹(𝑎) = 5
⎨ 2 for 2 ≤ 𝑎 < 4
{ { 5
⎩ 1 for 𝑎 ≥ 4.
Determine the pmf of 𝑋.
Problem 10. Exponential Distribution
Suppose that buses arrive are scheduled to arrive at a bus stop at noon but are always 𝑋
minutes late, where 𝑋 is an exponential random variable with probability density function
𝑓 (𝑥) = 𝜆e−𝜆𝑥. Suppose that you arrive at the bus stop precisely at noon.
𝑋
(a) Compute the probability that you have to wait for more than five minutes for the bus
to arrive.
(b) Suppose that you have already waiting for 10 minutes. Compute the probability that
you have to wait an additional five minutes or more.
Problem 11. Let 𝑋 and 𝑌 be two continuous random variables with joint pdf
𝑓(𝑥,𝑦) = 𝑐𝑥2𝑦(1+𝑦) for 0 ≤ 𝑥 ≤ 3 and 0 ≤ 𝑦 ≤ 3,
and 𝑓(𝑥,𝑦) = 0 otherwise.
(a) Find the value of 𝑐.
(b) Find the probability 𝑃(1 ≤ 𝑋 ≤ 2, 0 ≤ 𝑌 ≤ 1).
(c) Determine the joint cdf, 𝐹 (𝑎, 𝑏), of 𝑋 and 𝑌 for 𝑎 and 𝑏 between 0 and 3.
(d) Find marginal cdf 𝐹 (𝑎) for 𝑎 between 0 and 3.
𝑋
(e) Find the marginal pdf 𝑓 (𝑥) directly from 𝑓(𝑥, 𝑦) and check that it is the derivative of
𝑋
𝐹 (𝑥).
𝑋
(f) Are 𝑋 and 𝑌 independent?
Problem 12. (Table of normal probabilities)
Use the table of standard normal probabilities to compute the following. (𝑍 is the standard
normal.)
(a) (i) 𝑃 (𝑍 ≤ 1.5) (ii) 𝑃 (−1.5 < 𝑍 < 1.5) 𝑃 (𝑍 > −0.75).
(b) Suppose 𝑋 ∼ N(2, (0.5)2). Find (i) 𝑃(𝑋 ≤ 2) (ii) 𝑃(1 < 𝑋 ≤ 1.75).
Problem 13. (Central Limit Theorem)
Let 𝑋 , 𝑋 , … , 𝑋 be i.i.d., each with expected value 𝜇 = 𝐸[𝑋 ] = 5, and variance 𝜎2 =
1 2 81 𝑖
Var(𝑋 ) = 4. Approximate 𝑃(𝑋 +𝑋 +⋯𝑋 > 369), using the central limit theorem.
𝑖 1 2 81
Exam 1 Practice I, Spring 2022 3
More problems
Problem 14. There are 3 arrangements of the word DAD, namely DAD, ADD, and
DDA. How many arrangements are there of the word PROBABILITY?
Problem 15. A multiple choice exam has 4 choices for each question. A student has
studied enough so that the probability they will know the answer to a question is 0.5, the
probability that they will be able to eliminate one choice is 0.25, otherwise all 4 choices
seem equally plausible. If they know the answer they will get the question right. If not they
have to guess from the 3 or 4 choices.
As the teacher you want the test to measure what the student knows. If the student answers
a question correctly what’s the probability they knew the answer?
Problem 16. Compute the expectation and variance of a Bernoulli(𝑝) random variable.
Problem 17. Transforming Normal Distributions
Suppose 𝑍 ∼ N(0,1) and 𝑌 = e𝑍.
(a) Find the cdf 𝐹 (𝑎) and pdf 𝑓 (𝑦) for 𝑌 . (For the CDF, the best you can do is write
𝑌 𝑌
it in terms of Φ the standard normal cdf.)
(b) We don’t have a formula for Φ(𝑧) so we don’t have a formula for quantiles. So we have
to write quantiles in terms of Φ−1.
(i) Write the 0.33 quantile of 𝑍 in terms of Φ−1
(ii) Write the 0.9 quantile of 𝑌 in terms of Φ−1.
(iii) Find the median of 𝑌 .
Problem 18. Suppose that 𝑋 ∼ Bin(𝑛, 0.5). Find the probability mass function of
𝑌 = 2𝑋.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
