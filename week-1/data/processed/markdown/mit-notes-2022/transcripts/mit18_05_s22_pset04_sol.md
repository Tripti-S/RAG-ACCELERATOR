# Mit18 05 S22 Pset04 Sol

---

18.05 Problem Set 4, Spring 2022 Solutions
Problem 1. (25: 5,5,10,5 pts.) Time to failure
Recall that an exponential random variable 𝑋 ∼ exp(𝜆) has pdf given by 𝑓(𝑥) = 𝜆𝑒−𝜆𝑥 on
𝑥 ≥ 0.
(a) Compute 𝑃 (𝑋 ≥ 𝑥).
Solution:
𝑥
𝑃(𝑋 ≥ 𝑥) = 1−𝑃(𝑋 < 𝑥) = 1−∫ 𝜆e−𝜆𝑥𝑑𝑥 = 1 − (1 − e−𝜆𝑥) = e−𝜆𝑥.
0
(b) Compute the mean and standard deviation of 𝑋. You need to set up the necessary
integrals, but you can use Wolfram Alpha or another application to do the computation. (Of
course, it will be good for you if you compute the integrals by hand!)
Solution: First we compute the mean
∞ ∞ e−𝜆𝑥 ∞ 1
𝐸[𝑋] = ∫ 𝑥𝑓(𝑥)𝑑𝑥 = ∫ 𝜆𝑥e−𝜆𝑥 𝑑𝑥 = −𝑥e−𝜆𝑥 − ∣ = .
𝜆 𝜆
0 0 0
For the variance, we use the formula Var(𝑋) = 𝐸[𝑋2] − 𝐸[𝑋] 2.
∞ ∞ 2𝑥e−𝜆𝑥 2e−𝜆𝑥 ∞ 2
𝐸[𝑋2] = ∫ 𝑥2𝑓(𝑥)𝑑𝑥 = ∫ 𝜆𝑥2e−𝜆𝑥 𝑑𝑥 = −𝑥2e−𝜆𝑥 − − ∣ =
𝜆 𝜆2 𝜆2
0 0 0
2 1 1 1
So, Var(𝑋) = − = . So, standard deviation 𝜎 = .
𝜆2 𝜆2 𝜆2 𝜆
(c) Suppose that 𝑋 and 𝑋 are independent exp(𝜆) random variables. Let 𝑇 = min(𝑋 , 𝑋 ).
1 2 1 2
Find the cdf and pdf of 𝑇 . (Hint: first find a formula for 𝑃(𝑇 ≥ 𝑡)?)
Note: for independent continuous random variables 𝑋 , 𝑋 , you can assume the following
1 2
formula:
𝑃 (𝑋 ≥ 𝑥 , 𝑋 ≥ 𝑥 ) = 𝑃 (𝑋 ≥ 𝑥 )𝑃 (𝑋 ≥ 𝑥 ).
1 1 2 2 1 1 2 2
Solution: For 𝑡 ≥ 0, we know that 𝑇 ≥ 𝑡 if and only if both 𝑋 ≥ 𝑡 and 𝑋 ≥ 𝑡. So
1 2
𝑃(𝑇 ≥ 𝑡) = 𝑃(𝑋 ≥ 𝑡,𝑋 ≥ 𝑡). Since 𝑋 and 𝑋 are independent, using part (a) we get,
1 2 1 2
𝑃 (𝑋 ≥ 𝑡, 𝑋 ≥ 𝑡) = 𝑃 (𝑋 ≥ 𝑡)𝑃 (𝑋 ≥ 𝑡) = 𝑒−2𝜆𝑡.
1 2 1 2
Thus, 𝐹 (𝑡) = 𝑃 (𝑇 ≤ 𝑡) = 1 − 𝑒−2𝜆𝑡. Differentiating with respect to 𝑡 to get the pdf, we
𝑇
find
𝑓 (𝑡) = 𝐹 ′ (𝑡) = 2𝜆𝑒−2𝜆𝑡.
𝑇 𝑇
That is, 𝑇 is an exponential random variable with mean 1 .
2𝜆
(d) Suppose we are testing 3 different brands of light bulbs 𝐵 , 𝐵 , and 𝐵 whose lifetimes
1 2 3
are exponential random variables with mean 1/2, 1/3, and 1/5 years, respectively. Assuming
1
18.05 Problem Set 4, Spring 2022 Solutions 2
that all of the bulbs are independent, what is the expected time before one of the bulb fails.
(Hint: part (c) was a warmup for this problem.)
Solution: Let 𝑋 , 𝑋 , and 𝑋 be the lifetimes of bulbs 𝐵 , 𝐵 and 𝐵 , respectively. Then
1 2 3 1 2 3
we know 𝑋 ∼ exp(2), 𝑋 ∼ exp(3), 𝑋 ∼ exp(5). Let 𝑇 = min(𝑋 , 𝑋 , 𝑋 ). Then 𝑇 is the
1 2 3 1 2 3
time to the first failure of a bulb. Following the same argument as in (c), we have
𝑃 (𝑇 ≥ 𝑡) = 𝑃 (𝑋 ≥ 𝑡)𝑃 (𝑋 ≥ 𝑡)𝑃 (𝑋 ≥ 𝑡) = e−10𝑡.
1 2 3
Thus, the cdf of 𝑇 is 𝐹 (𝑡) = 1 − 𝑒−10𝑡 and the pdf, 𝑓 (𝑡) is given by
𝑇 𝑇
𝑓 (𝑡) = 𝐹 ′ (𝑡) = 10𝑒−10𝑡.
𝑇 𝑇
We found that 𝑇 ∼ exp(10). Therefore, 𝐸[𝑇] = 1 .
10
Problem 2. (20: 10,10 pts.) Elections
To head the newly formed US Dept. of Statistics, suppose that 50% of the population
supports Alessandre, 20% supports Sarah, and the rest are split between Gabriel, Sarah and
So Hee. A poll asks 400 random people who they support.
(a) Use the central limit theorem to estimate the probability that at least 52.5% of those
polled prefer Alessandre?
Solution: Let 𝑋 be the result of polling person 𝑖:
𝑖
1 if person 𝑖 supports Alessandre
𝑋 = {
𝑖
0 if person 𝑖 does not support Alessandre
Then 𝑋 ∼ Bern(0.5) and the number of people who prefer Alessandre is
𝑖
𝑆 = 𝑋 +⋯+𝑋 .
1 400
We know 𝐸[𝑋 ] = 1/2 and Var(𝑋 ) = 1/4. This implies 𝐸[𝑆] = 200 and Var(𝑆) = 100.
𝑖 𝑖
Thus, the central limit theorem tells us that
𝑆 ≈ N(200, 100).
The problem asks for 𝑃 (𝑆 > 210):
𝑆 −200 210 − 200
𝑃(𝑆 > 210) = 𝑃 ( > ) ≈ 𝑃(𝑍 > 1) ≈ 0.16 .
10 10
(b) Use the central limit theorem to estimate the probability that less than 31% of those
polled prefer Gabriel, Sarah or So Hee?
Solution: Now let 𝑌 = 1 if person 𝑖 prefers one of Gabriel, Sarah or So Hee and 0
𝑖
otherwise. We have 𝑌 , … , 𝑌 are independent Bern(0.3). So 𝐸[𝑌 ] = 𝜇 = 0.3 and
1 400 𝑖
Var(𝑌 ) = (0.3)(0.7) = 0.21. If 𝑌 = 1 (𝑌 + ⋯ + 𝑌 ), the Central Limit Theorem tells us
𝑖 400 1 400
√
𝑌 − 𝜇 (𝑌 − 0.3) 400
√ = √
𝜎/ 400 0.21
18.05 Problem Set 4, Spring 2022 Solutions 3
is approximately standard normal. Thus, using 𝑍 for a standard normal random variable,
√
(0.31−0.3) 400
𝑃(𝑌 ≤ 0.31) ≈ 𝑃 (𝑍 < √ ) = 𝑃(𝑍 < 0.4364358) ≈ 0.67.
0.21
Problem 3. (10 pts.) A penny for your thoughts
To save a mint, in 2012 Canada decided to do away with its pennies. The Chubby Chef
in Equality, Illinois wants to be ready should the United States decide to pass a similar
law. The Chubby Chef processes 𝑛 = 1000 orders of assorted baked goods each day, and will
round the price of each order to the nearest nickel (e.g., $3.57 rounds to $3.55 while $3.58
rounds to $3.60). Let 𝑝 be the probability that the total rounding error over the course of a
day is either greater than 100 or less than -100 cents, i.e. exceeds 100 in absolute value.
Estimate 𝑝 using the central limit theorem.
Solution: Let 𝑆 be the total rounding error for a day. The problems asks for
𝑃(|𝑆| > 100).
Let 𝑋 be the rounding error (in cents) of the 𝑖th order. Then 𝑋 takes values −2, −1, 0, 1, 2,
𝑖 𝑖
each with probability 1. We compute
5
𝐸[𝑋 ] = 𝜇 = 0, Var(𝑋 ) = 𝜎2 = 2.
𝑖 𝑖
The total rounding error 𝑆 = 𝑋 +⋯+𝑋 . By the Central Limit Theorem, we know
1 1000
that 𝑆 ≈ N(0, 2000).
|𝑆 − 0| 100−0 100
𝑃(|𝑆| ≥ 100) = 𝑃 (√ ≥ √ ) ≈ 𝑃 (|𝑍| ≥ √ ) = 0.0253 .
2000 2000 2000
Extra credit 5 points Simulate this in R with 10000 trials. (Each trial involves 1000
orders.) Print out or hand copy your code and include it. Give the result of running your
code 3 times,
Solution: Here’s my code.
ntrials = 10000
n_orders = 1000
threshold = 100
cnt_above_threshold = 0
for (j in 1:ntrials) {
# The rounding error is 0, -1, -2, 2, 1 depending on if the price modulo 5
is 0, 1, 2, 3, 4
# Generate 1000 random orders, just keep the rounding error
x = sample(c(0,-1,-2,2,1), n_orders, replace=TRUE)
total_error = sum(x)
if (abs(total_error) > threshold) {
cnt_above_threshold = cnt_above_threshold + 1
}
}
18.05 Problem Set 4, Spring 2022 Solutions 4
prob_above_thresh = cnt_above_threshold/ntrials
print(prob_above_thresh)
In three runs it gave 0.0245, 0.0263, 0.0216. This agrees nicely with the CLT estimate.
Problem 4. (30: 10,10,10 pts.) Change of scale.
In this problem we will look at scaling random variables. This is a simple, but common
thing to do. As usual with transformations, if you don’t approach it systematically, it is
easy to make mistakes.
(a) Suppose the random variable 𝑋 has an exponential distribution with parameter 1, i.e.
𝑋 ∼ exp(1). Give the range and pdf for the variables 𝑋 and 𝑌 = 3𝑋
Sketch the graph of the density functions for each of these variables.
Solution: 𝑋: The range of 𝑋 is [0, ∞). The pdf is 𝑓 (𝑥) = e−𝑥, for 𝑥 inside the range and
𝑋
0 elsewhere.
𝑌 = 3𝑋: The range of 𝑌 is [0, ∞). To find 𝑓 , we work with the cumulative distributions.
𝑌
𝐹 (𝑦) = 𝑃 (𝑌 ≤ 𝑦) definition of CDF
𝑌
= 𝑃 (3𝑋 ≤ 𝑦) because 𝑌 = 3𝑋
= 𝑃 (𝑋 ≤ 𝑦/3) algebra
= 𝐹 (𝑦/3) definition of CDF
𝑋
Now for the pdf:
𝑑 1 𝑑 1 1
𝑓 (𝑦) = 𝐹 (𝑦) = 𝐹 (𝑦/3) = 𝐹′ (𝑦/3) = 𝑓 (𝑦/3).
𝑌 𝑑𝑦 𝑌 3 𝑑𝑦 𝑋 3 𝑋 3 𝑋
The second to last equality used the chain rule. The last equality is the fact that the pdf is
the derivative of the cdf, i.e. 𝑓 = 𝐹′ .
𝑋 𝑋
Since we know 𝑓 (𝑦/3) = e−𝑦/3, we have
𝑋
1
𝑓 (𝑦) = e−𝑦/3 for 𝑦 between 0 and ∞.
𝑌 3
0 2 4 6 8 10
0.1
8.0
6.0
4.0
2.0
0.0
f (t)
X
f (t)
Y
t
18.05 Problem Set 4, Spring 2022 Solutions 5
(b) For the random variable 𝑋 from part (a), find the range and pdf of 𝑊 = 𝑎𝑋+𝑏, where
𝑎 and 𝑏 are constants. Assume 𝑎 > 0.
Solution: We find the range and pdf by following the same pattern as in part (a). The
range of 𝑊 is [𝑏, ∞).
𝑤−𝑏 𝑤 − 𝑏
𝐹 (𝑤) = 𝑃(𝑊 ≤ 𝑤) = 𝑃(𝑎𝑋+𝑏 ≤ 𝑤) = 𝑃 (𝑋 ≤ ) = 𝐹 ( ).
𝑊 𝑎 𝑋 𝑎
Taking the derivative:
𝑑 𝑑 𝑤 − 𝑏 1 𝑤 − 𝑏 1 𝑤 − 𝑏
𝑓 (𝑤) = 𝐹 (𝑤) = 𝐹 ( ) = 𝐹′ ( ) = 𝑓 ( ).
𝑊 𝑑𝑤 𝑊 𝑑𝑤 𝑋 𝑎 𝑎 𝑋 𝑎 𝑎 𝑋 𝑎
Since we know 𝑓 (𝑤−𝑏) = e−(𝑤−𝑏)/𝑎, we have
𝑋 𝑎
1
𝑓 (𝑤) = e−(𝑤−𝑏)/𝑎 for 𝑤 between 𝑏 and ∞.
𝑊 𝑎
(c) Let 𝑉 = 𝑋3. Find the range and pdf of 𝑉 .
Solution: We follow the same pattern as in the previous parts. The range of 𝑉 is [0, ∞).
𝐹 (𝑣) = 𝑃(𝑉 ≤ 𝑣) = 𝑃(𝑋3 ≤ 𝑣) = 𝑃(𝑋 ≤ 𝑣1/3) = 𝐹 (𝑣1/3).
𝑉 𝑋
Taking the derivative:
𝑑 𝑑 1 1 1
𝑓 (𝑣) = 𝐹 (𝑣) = 𝐹 (𝑣1/3) = 𝑣−2/3𝐹′ (𝑣1/3) = 𝑣−2/3𝑓 (𝑣1/3) = 𝑣−2/3e−𝑣1/3.
𝑉 𝑑𝑣 𝑉 𝑑𝑣 𝑋 3 𝑋 3 𝑋 3
Problem 5. (30: 10,10,10 pts.) In this problem we will explore how the transformations in
the previous problem affect the mean and median.
(a) For the variables 𝑋, 𝑌 , 𝑊 in the previous problem, assume each of the variables are
given in units of minutes. Find the expected value, variance and standard deviation of each
variable. Be sure to include units in your answer.
What are the units on 𝑎 and 𝑏 in the defnition of 𝑊 ?
Solution: Since 𝑋 ∼ Exponential(1) we know
𝐸[𝑋] = 1 min., Var(𝑋) = 1 min.2, 𝜎 = 1 min.
𝑋
Since expected value is linear,
𝐸[𝑌 ] = 𝐸[3𝑋] = 3𝐸[𝑋] = 3 min., 𝐸[𝑊] = 𝑎𝐸[𝑋]+𝑏 = (𝑎+𝑏) min.
Likewise, the variance is invariant under translation and scales by the square of the multi-
plier:
Var(𝑌) = 9⋅ Var(𝑋) = 9 min.2, 𝜎 = 3 min.,
𝑌
Var(𝑊) = 𝑎2 ⋅ Var(𝑋) = 𝑎2 min.2, 𝜎 = 𝑎 min..
𝑊
18.05 Problem Set 4, Spring 2022 Solutions 6
Because both 𝑋 and 𝑊 are in units of minutes, 𝑎 must be dimensionless and 𝑏 has units of
minutes.
(b) For 𝑉 from the previous problem, compute 𝐸[𝑉 ]. As usual, you must set up the integral,
but you can use a package like Wolfram Alpha to compute the integral.
∞ 1 ∞
Solution: 𝐸[𝑉] = ∫ 𝑣𝑓 (𝑣)𝑑𝑣 = ∫ 𝑣1/3e−𝑣1/3 𝑑𝑣. This integral can be computed
𝑉 3
0 0
using the change of variable 𝑢 = 𝑣1/3, i.e. 𝑢3 = 𝑣. The final answer is 𝐸[𝑉] = 6. (Wolfram
Alpha agrees!)
(c) Compute the median value of both 𝑋 and 𝑉 .
Solution: For 𝑋, the median value is the value 𝑞 such that 𝐹 (𝑞 ) = 0.5. Now,
0.5 𝑋 0.5
𝑞 𝑞
𝐹 (𝑞) = ∫ 𝑓 (𝑥) 𝑑𝑥 = ∫ e−𝑥𝑑𝑥 = −e−𝑥| 𝑞 = 1 − e−𝑞.
𝑋 𝑋 0
0 0
Solving 1− e−𝑞 = 0.5 gives the median of 𝑋 is 𝑞 = ln(2) .
0.5
Since as we saw in the previous problem, 𝐹 (𝑣) = 𝐹 (𝑣1/3), we have
𝑉 𝑋
𝐹 (𝑣) = 0.5 ⇔ 𝐹 (𝑣1/3) = 0.5 ⇔ 𝑣1/3 = 𝑞 .
𝑉 𝑋 0.5
That is, the median of 𝑉 = 𝑋3 is just (the median of 𝑋)3, i.e. ln(2)3.
Problem 6. (30: 5,5,10,10 pts.) Fat tails
This problem will explore the tails of two distributions. The tails are important when we
want to think about probabilities of extreme events.
(a) As an example, in the general population IQ has mean 100 and standard deviation of
15. IQ is normally distributed. Use the R function pnorm to give the probability that a
randomly chosen person has IQ greater than 160, i.e. more than 4 standard deviations
above the mean.
Solution: We use the R code p = 1 - pnorm(160, 100, 15). This gives the probability
𝑝 = 3.167124 × 10−5.
(b) Now, in order to be able to use R or Wolfram Alpha without a lot of distracting algebraic
manipulation, we’ll modify the definition of IQ. Suppose that Modified_IQ has mean 0 and
√
standard deviation 3.
Assuming Modified_IQ is normally distributed, find the probability that a randomly chosen
person has Modified_IQ more than 4 standard deviations above the mean.
Solution: One of the important facts about normal distributions, is that, when measured
in standard deviations above the mean they all give the same probabilities. That is, the
answer is exactly the same as in part (a)
(c) Now assume that Modified_IQ follows a t-distribution with 3 degrees of freedom. Later
in the class we will work extensively with t-distributions. Here, it will be enough for us to
know the following about this distribution.
• Range: (−∞, ∞)
18.05 Problem Set 4, Spring 2022 Solutions 7
−2
2 𝑥2
• PDF: 𝑓(𝑥) = (1+ )
3𝜋 3
• Mean: 𝜇 = 0
√
• Standard deviation: 𝜎 = 3
(So this has the same mean and standard deviation as in part (b).)
For this problem, you can work with this pdf directly or you can look up how to use the R
functions dt and pt.
Assuming it follows this t-distribution, find the probability that a randomly chosen person
has Modified_IQ more than 4 standard deviations above the mean.
You can use R or another calculation package to do the calculation, but you must explicitly
show the integral in terms of the probability density.
Compare this value with the probability in part (b)
Solution: If 𝐼 is the Modified_IQ of a randomly chosen person, we want to compute
√
𝑃(𝐼 > 4∗ 3). In terms of the pdf this is
√ ∞ ∞ 2 𝑥2 −2
𝑃(𝐼 > 4 3) = ∫ 𝑓(𝑥)𝑑𝑥 = ∫ (1+ ) 𝑑𝑥
√ √ 3𝜋 3
4 3 4 3
We computed this in R with the code p = 1 - pt(4*sqrt(3), 3). This gives the proba-
bility 𝑝 = 0.003082687.
This is a small probability, but it is about 100 times the probability in parts (a) and (b).
(d) For this problem, compute probabilities using both the normal distribution in part (b)
and the t-distribution in part (c). Do this for the following probabilities.
(i) 𝑃 (Modified_IQ > 20), (ii) 𝑃 (Modified_IQ > 40), (iii) 𝑃 (Modified_IQ > 200).
Why do we say that the t-distribution has a ‘fat tail’?
Hence the moral of this problem: Knowing the mean and standard deviation of a quantity
is often not enough for predicting the frequency of extreme events (high IQ, 100-year floods,
etc.); you need to know the underlying distribution itself (which often requires finding out
the underlying geophysics, geochemistry, and biology). In the solutions we will show you
graphs of these distributions zoomed in around 4𝜎 above the mean. If you do that yourself,
you will see that they look very different.
Solution: For 𝑥 = 20, 40, 200, we use the R code p_t = 1 - pt(x, 3), p_normal = 1 -
pnorm(x, 0, sqrt(3)). We get
(i) 𝑥 = 20: p_t = 0.00014, p_normal = 0
(ii) 𝑥 = 40: p_t = 1.7e-5, p_normal = 0
(iii) 𝑥 = 200: p_t = 1.4e-7, p_normal = 0
All three examples show that for 𝑥 far from the mean, i.e. in the tail, the t-distribution
probability is many orders of magnitude greater than the normal distribution probability
We say the t-distribution has a fat tail, because the its tail contains much more probability
than the normal distribution. That is, extreme events are much more likely for the t-
distribution.
18.05 Problem Set 4, Spring 2022 Solutions 8
Graphically, the following figures show the tail of the t-distribution is much greater, i.e.
fatter, than that of the normal distribution.
−4 −2 0 2 4
3.0
2.0
1.0
0.0
t−distribution
Normal
5 6 7 8 9 10
x
300.0
200.0
100.0
000.0
t−distribution
normal
x
Left: Center of distributions, Right: tails from 3𝜎 to 6𝜎 above mean
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
