# Mit18 05 S22 Exam01 Sol

---

18.05 Exam 1 Solutions
Problem 0. (5 pts) Be sure to attach your cheat sheet to your test.
Problem 1. (10 pts: 4,6) Concept/Quick questions
(a) (No explanations are necessary.)
The plot shows the pdf for three independent random variables 𝑋, 𝑌 , 𝑊 . All use the same
horizontal and vertical scale.
𝑓
𝑌
𝑓
𝑊
𝑓
𝑋
Which random variable has the greatest variance?
Solution: 𝑋.(Variance measures the spread away from the mean.)
(b) Suppose 𝐴 and 𝐵 are two events and 𝑃 (𝐴) = 0.7, 𝑃 (𝐵) = 0.3 and 𝑃(𝐴∩𝐵) = 0.25.
Compute each of the following
(i) Compute 𝑃(𝐴 ∪ 𝐵)
(ii) Compute 𝑃 (𝐴|𝐵).
Solution: (i) Inclusion exclusion: 𝑃(𝐴∪𝐵) = 0.7+0.3−0.25 = 0.75.
(ii) 𝑃 (𝐴|𝐵) = 𝑃 (𝐴∩𝐵) = 0.25.
𝑃 (𝐵) 0.3
Problem 2. (15 pts: 10,5)
You create passwords as a string of 10 characters such that:
• 5 of the characters are letters (upper and lower case, i.e. 52 characters) with repetitions
allowed,
• 3 are numbers { 0,1,2,3,4,5,6,7,8,9 } with repetitions allowed, and
• 2 are distinct symbols from the list of 5 symbols: { !, @, #, $, & }.
(a) How many passwords are there? (No need to simplify your answer.)
Solution: First, choose the locations of the symbols (10).
2
Then choose the symbols, since they have to be different and order matters, we get 5⋅4.
Then, choose the locations of the letters: (8).
5
Then count the number of ways to choose 5 letters (with replacement) 525.
Then choose the locations of the numbers: (3) = 1.
3
Finally choose the numbers: 103.
So, the number of passwords (10)⋅(8)⋅20⋅103 ⋅525.
2 5
1
18.05 Exam 1 Solutions 2
(b) With all locations for symbols, letters, or numbers in your 10 character password being
equally likely, what is the probability that the two symbols are next to each other?
Solution: Count the ways to get a password where the two symbols are adjacent:
First choose locations for the two symbols: there are 9 adjacent positions.
Then there are 5⋅4 ways to choose the sequence of two symbols.
8
Then choose the locations of the letters: ( ).
5
Then count the number of ways to choose 5 upper or lower case letters (with replacement)
525.
3
Then choose the locations of the numbers: ( ).
3
Then choose the numbers: 103.
9⋅(8)⋅5⋅4⋅103⋅525 9 2
So, 𝑃 (two adjacent symbols) = 5 = =
(10)⋅(8)⋅5⋅4⋅103⋅525 (10) 10
2 5 2
Problem 3. (25 pts: 10,5,5,5)
You have 5 four-sided and 3 six-sided dice. You put them in a cup, choose one at random,
roll the die, and report the result.
Let 𝐷 be the number of sides on the chosen die and let 𝑅 be the result of the roll.
(a) Make a joint probability table for 𝐷 and 𝑅. Be sure to include the marginal probabilities
for 𝐷 and 𝑅.
Solution: Each element of the table is simply the probability of getting a die with the
indicated number of sides and then rolling the indicated number. For example,
1 3 1
𝑃(𝑅 = 3 and 𝐷 = 6) = 𝑃(𝑅 = 3|𝐷 = 6)𝑃(𝐷 = 6) = ⋅ = .
6 8 16
𝑅\𝐷 4-sided 6-sided
1 5/32 1/16 7/32
2 5/32 1/16 7/32
3 5/32 1/16 7/32
4 5/32 1/16 7/32
5 0 1/16 1/16
6 0 1/16 1/16
5/8 3/8
(b) What is the probability of rolling a 3?
Solution: This is the sum of the entries in the 𝑅 = 3 row of the table:
5/32 + 1/16 = 7/32
(Do you see why this has to be between 1/6 and 1/4?)
(c) Compute 𝑃(𝐷 = 4|𝑅 = 3).
Solution: We compute this as the fraction
𝑃(𝐷 = 4 and 𝑅 = 3) 5/32
= = 5/7.
𝑃 (𝑅 = 3) 7/32
18.05 Exam 1 Solutions 3
(d) Are 𝐷 and 𝑅 independent?
Solution: No, the joint probabilities in the table are not the products of the marginal
probabilities. The easiest way to see this is to note that 𝑃(𝑅 = 6 and 𝐷 = 4) = 0, which
does not equal 𝑃 (𝑅 = 6)𝑃 (𝐷 = 4) = 5/128.
Problem 4. (10 pts)
A quick screening test for a certain disease has three outcomes: positive, negative and
uncertain. Suppose it has the following percentages.
For someone with the disease: positive 70%, negative 10%, uncertain 20%.
For someone without the disease: positive 10%, negative 60%, uncertain 30%.
Suppose also, that the prevalence of the disease in the population is 2%.
What is the probability that a random person who tests positive has the disease?
Solution: We organize the problem in a tree. Here: 𝐷+ = has disease, 𝐷− = does not
have disease; 𝑇 + = test is positive, other = test is negative or uncertain.
0.02 0.98
𝐷+ 𝐷−
0.7 0.3 0.1 0.9
𝑇+ other 𝑇+ other
𝑃 (𝑇 +|𝐷+)𝑃 (𝐷+) 0.7 ⋅ 0.02 14 1
𝑃 (𝐷+|𝑇 +) = = = = = 0.125 .
𝑃(𝑇 +) 0.7⋅0.02+0.1 ⋅0.98 112 8
Problem 5. (25 pts: 5,5,5,5,5)
Two students, Xeno and Yolanda are meeting up for lunch. They plan on a time to meet
at noon. Both have class before so neither will be early. Both have class that starts at 1pm,
so they will both arrive between 0 and 1 hour late. Let 𝑋 be the time in hours that Xeno
arrives late and let 𝑌 be the time in hours that Yolanda arrives late.
Assume that the joint pdf of these random variables is 𝑓(𝑥,𝑦) = 5/4−𝑥𝑦.
(a) Find the two marginal pdfs.
Solution: To find the marginals we ‘integrate out’ the other variable.
1 1
𝑓 (𝑥) = ∫ 𝑓(𝑥,𝑦)𝑑𝑦 = ∫ 5/4−𝑥𝑦𝑑𝑦 = 5/4 − 𝑥/2.
𝑋
0 0
1 1
𝑓 (𝑦) = ∫ 𝑓(𝑥,𝑦)𝑑𝑥 = ∫ 5/4−𝑥𝑦𝑑𝑥 = 5/4 − 𝑦/2.
𝑌
0 0
We could have used symmetry to deduce 𝑓 (𝑦) without any integration.
𝑌
(b) Are 𝑋 and 𝑌 independent?
Solution: Since the joint pdf is not the product of the marginals, i.e. 𝑓(𝑥,𝑦) ≠ 𝑓 (𝑥)𝑓 (𝑦),
𝑋 𝑌
𝑋 and 𝑌 are not independent.
(c) Find 𝐸[𝑋], Var(𝑋). (For these, you need to simplify the fractions.)
18.05 Exam 1 Solutions 4
Solution: We compute both 𝐸[𝑋] and Var(𝑋) = 𝐸[𝑋2] − 𝐸[𝑋]2 using the marginal pdf
𝑓 (𝑋) found in part (a).
𝑋
1 1 5 1 11
𝐸[𝑋] = ∫ 𝑥𝑓 (𝑥)𝑑𝑥 = ∫ 5𝑥/4−𝑥2/2𝑑𝑥 = − = .
𝑋 8 6 24
0 0
1 1 5 1 7
𝐸[𝑋2] = ∫ 𝑥2𝑓 (𝑥)𝑑𝑥 = ∫ 5𝑥2/4−𝑥3/2𝑑𝑥 = − = .
𝑋 12 8 24
0 0
7 112 47
Var(𝑋) = 𝐸[𝑋2] − 𝐸[𝑋] 2 = − = .
24 242 242
(d) Compute the covariance Cov(𝑋, 𝑌 ) and correlation Cor(𝑋,𝑌 ).
Hint: By symmetry you know the mean and variance of 𝑌 are the same as those for 𝑋.
For this part, there is no need to simplify fractions.
Solution: By symmetry, we know 𝐸[𝑌 ] = 𝐸[𝑋] = 11/24 and Var(𝑌) = Var(𝑋) = 47/242.
We use the formula Cov(𝑋,𝑌) = 𝐸[𝑋𝑌 ]−𝐸[𝑋]𝐸[𝑌].
1 1 1 1 5 1 29
𝐸[𝑋𝑌 ] = ∫ ∫ 𝑥𝑦𝑓(𝑥,𝑦)𝑑𝑥𝑑𝑦 = ∫ ∫ 5𝑥𝑦/4−𝑥2𝑦2𝑑𝑥 = − = .
16 9 144
0 0 0 0
29 112 29 121 5
Cov(𝑋,𝑌) = 𝐸[𝑋𝑌 ]−𝐸[𝑋]𝐸[𝑌] = − = − = −
144 242 144 144⋅4 144⋅4
Cov(𝑋, 𝑌 ) Cov(𝑋, 𝑌 ) −5/242 −5
Cor(𝑋,𝑌) = = = =
𝜎 𝜎 47/242 47/242 47
𝑋 𝑌
(e) Set up, but do not compute an expression computing the probability that Xeno and
Yolanda arrive within 6 minutes (0.1 hours) of each other and that Yolanda arrives after
Xeno.
Your integral will be over a region 𝑅 in the unit square. You can leave your integral in the
form ∬ ℎ(𝑥, 𝑦) 𝑑𝑥 𝑑𝑦 and show 𝑅 in a figure elsewhere on the page. The function ℎ(𝑥, 𝑦)
𝑅
must be specified completely.
Solution: The integral is ∬𝑓(𝑥,𝑦)𝑑𝑥𝑑𝑦 = ∬5/4−𝑥𝑦𝑑𝑥𝑑𝑦.
𝑅 𝑅
The region 𝑅 is the part of the unit square where 𝑋 < 𝑌 and 𝑌 −𝑋 < 0.1. This is the
strip of the triangle shown in the picture
𝑦 𝑅 (𝑋<𝑌 <𝑋+0.1)
1
𝑥
1
18.05 Exam 1 Solutions 5
This was not asked for, but using 18.02 we get
0.9 𝑥+0.1 1 1
𝑃(𝑋 < 𝑌 < 𝑋+0.1) = ∫ ∫ 5/4−𝑥𝑦𝑑𝑦𝑑𝑥+∫ ∫ 5/4−𝑥𝑦𝑑𝑦𝑑𝑥
0 𝑥 0.9 𝑥
Problem 6. (10 pts)
A company manufactures solar panels. When homeowners install the panels, the state pays
50% of the cost. Because this subsidy is about to expire, the company wants to manufacture
as many panels as it can in the next 20 days.
For a variety of reasons the number of panels it can manufacture in a day is a random variable
with each day independent of the others. Suppose the daily output follows a so-called gamma
𝑥4
distribution. The pdf of this distribution is not that complicated (𝑓(𝑥) = e−𝑥/100),
4! ⋅ 1010
but we’ll let Wikipedia tell us the mean and variance: mean = 500, variance = 5 ⋅ 104.
Estimate the probability that they will be able to manufacture more than 10,500 panels in
the next 20 days.
Solution: Let 𝑆 be the total manufactured in 20 days. The problem asks for 𝑃 (𝑆 > 10500).
Since 𝑆 is a sum of 20 i.i.d. random variables, the central limit theorem tell us that it is
approximately normal. We know that one day has mean 500 and variance 5 ⋅ 104. So
𝐸[𝑆] = 20 ⋅ 500 = 10000 Var(𝑆) = 20⋅5⋅104 = 105 𝜎 = 103.
𝑆
Standardizing and using the CLT we get
𝑆 −10,000 10, 500 − 10, 000
𝑃(𝑆 > 10500) = 𝑃 ( > )
1000 1000
≈ 𝑃(𝑍 > 0.5) = 1−𝑃(𝑍 ≤ 0.5) ≈ 1−0.6915 = 0.3085
The decimal answer came by looking up 𝑃 (𝑍 < 0.5) ≈ 0.6915 in the standard normal
table.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
