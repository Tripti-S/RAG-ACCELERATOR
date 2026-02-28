# Mit18 05 S22 Class06A Pset Sol

---

Class 6 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. Greatest median 1
Each of the curves is the density for a random variable. Where there is just one curve they
overlap.
The median of the black plot is at 𝑞. Which density has the greatest median?
(A)
Curvescoincidetohere.
q
1. Black 2. Orange 3. Blue 4. All the same 5. Impossible to tell
4. All three medians are the same. Remember that probability is computed as the area
under the curve. By definition the median 𝑞 is the point where the shaded area in Plot
A is 0.5. Since all three curves coincide up to 𝑞. That is, the shaded area in the figure is
represents a probability of 0.5 for all three densities. Thus, it is the median for all three
densities.
(A)
Curvescoincidetohere.
Areato
theleftof
theme-
dian=0.5
q
Concept question 2. Greatest median 2
Each of the curves is the density for a random variable. Where there is just one curve they
overlap.
The median of the black plot is at 𝑞. Which density has the greatest median?
(B)
q
1
18.05 class 6 problems, Spring 2022 2
1. Black 2. Orange 3. Blue 4. All the same 5. Impossible to tell
Solution: 2. The orange density has the greatest median. Since 𝑞 is the median for the
black density, the shaded area in Plot B is 0.5. Therefore the area under the blue curve
(up to 𝑞) is greater than 0.5 and that under the orange curve is less than 0.5. This means
the median of the blue density is to the left of 𝑞 (you need less area) and the median of the
orange density is to the right of 𝑞 (you need more area).
(B)
q
Concept question 3. Desperation
• You have $100. You need $1000 by tomorrow morning.
• Your only way to get it is to gamble.
• If you bet $k, you either win $k with probability 𝑝 or lose $k with probability 1 − 𝑝.
Maximal strategy: Bet as much as you can, up to what you need, each time.
Minimal strategy: Make a small bet, say $5, each time.
(a) If 𝑝 = 0.45, which is the better strategy?
(a) Maximal (b) Minimal (c) They are the same
(b) If 𝑝 = 0.8, which is the better strategy?
(a) Maximal (b) Minimal (c) They are the same
Solution: If 𝑝 = 0.45 use maximal strategy; If 𝑝 = 0.8 use minimal strategy.
If you use the minimal strategy the law of large numbers says your average winnings per
bet will almost certainly be the expected winnings of one bet. The two tables represent
𝑝 = 0.45 and 𝑝 = 0.8 respectively.
Win -5 5 Win -5 5
𝑝 0.55 0.45 𝑝 0.2 0.8
The expected value of a $5 bet when 𝑝 = 0.45 is -$0.50 Since on average you will lose $0.50
per bet you want to avoid making a lot of bets. You go for broke and hope to win big a few
times in a row. It’s not very likely, but the maximal strategy is your best bet.
The expected value of a $5 bet when 𝑝 = 0.8 is $3. Since this is positive you’d like to make a
lot of bets and let the law of large numbers (practically) guarantee you will win an average
of $3 per bet. So you use the minimal strategy.
18.05 class 6 problems, Spring 2022 3
Board questions
Problem 1.
The random variable 𝑋 has range [0,1] and pdf 𝑓(𝑥) = 𝑐𝑥2.
(a) Find 𝑐.
(b) Find the mean, variance and standard deviation of 𝑋.
(c) Find the median value of 𝑋.
(d) Suppose 𝑋 , … 𝑋 are independent identically-distributed copies of 𝑋. Let 𝑋 be their
1 16
average. What is the standard deviation of 𝑋?
(e) Suppose 𝑌 = 𝑋4. Compute 𝐸[𝑌 ]
(f) Find the pdf of 𝑌 .
1
(a) Solution: Total probability is 1: ∫ 𝑐𝑥2 𝑑𝑥 = 1 ⇒ 𝑐 = 3 .
0
1 1
(b) Solution: 𝜇 = ∫ 𝑥𝑓(𝑥)𝑑𝑥 = ∫ 3𝑥3𝑑𝑥 = 3/4.
0 0
1 1 3 9 9 3
𝜎2 = ∫ (𝑥−𝜇)2𝑓(𝑥)𝑑𝑥 = ∫ (𝑥−3/4)23𝑥2𝑑𝑥 = − + = .
5 8 16 80
0 0
𝜎 = √3/80 = 1√3/5 ≈ 0.194
4
(c) Solution: By definition: 𝐹 (𝑞 ) = 0.5, so we solve for 𝑞 .
0.5 0.5
𝑥
𝐹 (𝑥) = ∫ 3𝑢2 𝑑𝑢 = 𝑥3. Therefore, 𝐹 (𝑞 ) = 𝑞3 = 0.5.
0.5 0.5
0
We get, 𝑞 = (0.5)1/3 .
0.5
(d) Solution: Because they are independent
Var(𝑋 +…+𝑋 ) = Var(𝑋 ) + Var(𝑋 ) + … + Var(𝑋 ) = 16Var(𝑋).
1 16 1 2 16
Thus, Var(𝑋) = 16Var(𝑋) = Var(𝑋) .
162 16
𝜎
Finally, 𝜎 = 𝑋 = 0.194/4 .
𝑋 4
1 𝑐𝑥7 1 𝑐 3
(e) Solution: 𝐸[𝑌] = ∫ 𝑥4𝑐𝑥2𝑑𝑥 = ∣ = = .
7 7 7
0 0
(f) Method 1, use the cdf:
𝐹
𝑌
(𝑦) = 𝑃(𝑋4 < 𝑦) = 𝑃(𝑋 < 𝑦 1
4
) = 𝐹
𝑋
(𝑦1
4
) = 𝑦
4
3 .
3
Now differentiate. 𝑓
𝑌
(𝑦) = 𝐹
𝑌
′ (𝑦) =
4
𝑦−
4
1 .
Method 2, use the pdf:
We have 𝑦 = 𝑥4. So,
𝑑𝑦
𝑑𝑦 = 4𝑥3 𝑑𝑥 ⇒ = 𝑑𝑥.
4𝑦3/4
18.05 class 6 problems, Spring 2022 4
This implies
𝑑𝑦 3𝑦2/4 𝑑𝑦 3
𝑓 (𝑥)𝑑𝑥 = 𝑓 (𝑦1/4) = = 𝑑𝑦.
𝑋 𝑋 4𝑦3/4 4𝑦3/4 4𝑦1/4
3
Therefore. 𝑓 (𝑦) =
𝑌 4𝑦1/4
Problem 2.
(a) Make both a frequency and density histogram from the data below.
Use bins of width 0.5 starting at 0. The bins should be right closed.
1 1.2 1.3 1.6 1.6
2.1 2.2 2.6 2.7 3.1
3.2 3.4 3.8 3.9 3.9
(b) Same question using unequal width bins with edges 0, 1, 3, 4.
(c) For part (b), why does the density histogram give a more reasonable representation of
the data?
Solution:
ycneuqerF
0 1 2 3 4
0.3
0.2
0.1
0.0
ytisneD
0 1 2 3 4
4.0
2.0
0.0
Histograms with equal width bins
ycneuqerF
0 1 2 3 4
8
6
4
2
0
ytisneD
0 1 2 3 4
4.0
2.0
0.0
Histograms with unequal width bins
Extra problems
Extra 1. Quantiles using R
(a) Let 𝑍 be a standard normal variable (𝑍 ∼ N(0, 1)). Use the R function qnorm to find
the 0.25, 0.5, 0.75 quantiles for 𝑍.
Use the R help to learn about qnorm.
(b) Graph the pdf of the standard normal distribution. Place the quantiles from part (a) on
your graph. Also, indicate on the graph the probabilities connected to the quantiles.
18.05 class 6 problems, Spring 2022 5
(c) The R function pnorm is the CDF for the normal distribution. In its simplest form
pnorm(z) is the CDF for the standard normal distribution.
Apply pnorm to your quantiles from part (a). Check that the resulting probabilities are
exactly what you expect.
Solution: (a) Using qnorm(0.25), qnorm(0.5), qnorm(0.75) we find the quantiles 𝑞 ≈
0.25
−0.6744898, 𝑞 = 0.0, 𝑞 = 0.6744898.
0.5 0.5
(b) 𝑞 is the value of 𝑧 such that 𝑃 (𝑍 ≤ 𝑞 ) = 0.25. This is shown in the figure below.
0.25 0.25
Similar pictures hold for 𝑞 and 𝑞 .
0.5 0.75
𝑃(𝑍 ≤𝑞 )=0.25
0.25 𝜙(𝑧)
area = 0.25
𝑧
𝑞 𝑞 𝑞
0.25 0.5 0.75
(c) We find pnorm(q_0.25) = pnorm(-0.6744898) = 0.25, pnorm(q_0.5) = pnorm(0)
= 0.5, pnorm(q_0.75) = pnorm(0.6744898) = 0.75.
By definition, 𝑞 such that 𝑃 (𝑍 ≤ 𝑞 ) = 0.25.. So the values are just what we expect.
0.25 0.25
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
