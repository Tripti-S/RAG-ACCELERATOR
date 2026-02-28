# Mit18 05 S22 Pset05 Sol

---

18.05 Problem Set 5, Spring 2022 Solutions
Problem 1. (35: 5,10,5,10,5 pts.) Aching joints
Suppose 𝑋 and 𝑌 have joint pdf 𝑓(𝑥,𝑦) = 𝑐(𝑥2 +𝑥𝑦) on [0,1] × [0,1].
(a) Find 𝑐 and the joint cdf 𝐹 (𝑥, 𝑦).
Solution: We have
1 1 1 𝑥 1 1 7𝑐
1 = ∫ ∫ 𝑐(𝑥2+𝑥𝑦)𝑑𝑦𝑑𝑥 = 𝑐∫ 𝑥2+ 𝑑𝑥 = 𝑐( + ) = .
2 3 4 12
0 0 0
12
Thus, 𝑐 = . We have:
7
12 𝑥 𝑦
𝐹(𝑥,𝑦) = 𝑃(𝑋 ≤ 𝑥,𝑌 ≤ 𝑦) = ∫ ∫ 𝑢2+𝑢𝑣𝑑𝑦𝑑𝑥
7
0 0
12 𝑥 𝑢𝑦2
= ∫ 𝑢2𝑦 + 𝑑𝑢
7 2
0
12 𝑥3𝑦 𝑥2𝑦2
= ( + ) .
7 3 4
(b) Find the marginal cumulative distribution functions 𝐹 and 𝐹 and the marginal pdf
𝑋 𝑦
𝑓 and 𝑓 .
𝑋 𝑌
Solution: The marginal cdf’s are:
12 𝑥3 𝑥2
𝐹 (𝑥) = 𝐹(𝑥,1) = ( + )
𝑋 7 3 4
12 𝑦 𝑦2
𝐹 (𝑦) = 𝐹 (1, 𝑦) = ( + ) .
𝑌 7 3 4
The marginal pdf’s are found by differentiating the marginal cdf:
12 𝑥 12 1 𝑦
𝑓 (𝑥) = (𝑥2+ ) 𝑓 (𝑦) = ( + ).
𝑋 7 2 𝑌 7 3 2
We could also have found them by integrating the joint pdf:
1 12 𝑥 1 12 1 𝑦
𝑓 (𝑥) = ∫ 𝑓(𝑥,𝑦)𝑑𝑦 = (𝑥2 + ) 𝑓 (𝑦) = ∫ 𝑓(𝑥,𝑦)𝑑𝑥 = ( + ) .
𝑋 7 2 𝑌 7 3 2
0 0
(c) Find 𝐸[𝑋] and Var(𝑋).
Solution: The computation is slightly easier if we use the formula Var(𝑋) = 𝐸[𝑋2]−𝐸[𝑋]2.
1 12 1 𝑥 12 1 1 5
𝐸[𝑋] = ∫ 𝑥𝑓 (𝑥)𝑑𝑥 = ∫ 𝑥(𝑥2 + )𝑑𝑥 = ( + ) = ≈ 0.7143
𝑋 7 2 7 4 6 7
0 0
1 39
𝐸[𝑋2] = ∫ 𝑥2𝑓 (𝑥)𝑑𝑥 = ≈ 0.5571.
𝑋 70
0
1
18.05 Problem Set 5, Spring 2022 Solutions 2
Thus Var(𝑋) = 𝐸[𝑋2] − 𝐸[𝑋]2 ≈ 0.0469 .
(d) Find the covariance and correlation of 𝑋 and 𝑌 .
Solution: First we’ll need 𝐸[𝑌 ] and Var[𝑌 ]. The computations are similar to those in part
(c).
1 12 1 1 𝑦 4
𝐸[𝑌] = ∫ 𝑦𝑓 (𝑦)𝑑𝑦 = ∫ 𝑦( + ) 𝑑𝑦 = ≈ 0.5714
𝑌 7 3 2 7
0 0
1 12 1 1 𝑦 17
𝐸[𝑌 2] = ∫ 𝑦2𝑓 (𝑦) = ∫ 𝑦2 ( + ) 𝑑𝑦 = ≈ 0.4048
𝑌 7 3 2 42
0 0
Var(𝑌 ) = 𝐸[𝑌 2] − 𝐸[𝑌 ]2 ≈ 0.0782
Now, covariance is defined as Cov(𝑋,𝑌) = 𝐸[(𝑋 −𝜇 )(𝑌 −𝜇 )]. We could compute this
𝑥 𝑌
directly, but it’s slightly easier to use the formula Cov(𝑋,𝑌) = 𝐸[𝑋𝑌 ]−𝐸[𝑋]𝐸[𝑌].
1 1 12 1 1 17
𝐸[𝑋𝑌 ] = ∫ ∫ 𝑥𝑦𝑓(𝑥,𝑦)𝑑𝑦𝑑𝑥 = ∫ ∫ 𝑥3𝑦+𝑥2𝑦2𝑑𝑦𝑑𝑥 = ≈ 0.4048
7 42
0 0 0 0
Cov(𝑋,𝑌) = 𝐸[𝑋𝑌 ]−𝐸[𝑋]𝐸[𝑌] ≈ −0.0034
Cov(𝑋,𝑌 )
Cor(𝑋,𝑌) = = −0.0561
𝜎 𝜎
𝑋 𝑌
(e) Are 𝑋 and 𝑌 independent?
Solution: No they are not independent. We can see this in two ways. First, their joint
pdf is not the product of the marginal pdfs. Second, their covariance is not 0.
Problem 2. (10 pts.) Independence
Suppose 𝑋 and 𝑌 are random variables with the following joint pmf. Are 𝑋 and 𝑌 inde-
pendent?
𝑋\𝑌 1 2 3
1 1/18 1/9 1/6
2 1/9 1/6 1/18
3 1/6 1/18 1/9
Solution: To check independence we have to check if all the cell probabilities are the prod-
uct of marginal probabilities. So, first we compute the marginal probabilities by summing
along rows and columns.
𝑋\𝑌 1 2 3 𝑝(𝑥)
1 1/18 1/9 1/6 1/3
2 1/9 1/6 1/18 1/3
3 1/6 1/18 1/9 1/3
𝑝(𝑦) 1/3 1/3 1/3 1
Now, we can easily check that the joint distribution is not the product of the marginals.
For example,
1 1
𝑃(𝑋 = 1,𝑌 = 1) = , but 𝑃(𝑋 = 1)𝑃(𝑌 = 1) = .
18 9
18.05 Problem Set 5, Spring 2022 Solutions 3
So, 𝑋 and 𝑌 are not independent.
Problem 3. (20: 10,10 pts.) Correlation
Suppose 𝑋 and 𝑌 are random variables with
1 1
𝑃(𝑋 = 1) = 𝑃(𝑋 = −1) = ; 𝑃(𝑌 = 1) = 𝑃(𝑌 = −1) = .
2 2
Let 𝑐 = 𝑃(𝑋 = 1 and 𝑌 = 1).
(a) Determine the joint distribution of 𝑋 and 𝑌 , Cov(𝑋,𝑌 ), and Cor(𝑋,𝑌 ).
Solution: We make the joint distribution table by starting with the marginal distributions
and putting 𝑐 in the 𝑋 = 1, 𝑌 = 1 cell. The other three cells in the table are then
determined.
𝑋\𝑌 1 −1 𝑝(𝑥)
1 𝑐 0.5−𝑐 0.5
−1 0.5−𝑐 𝑐 0.5
𝑝(𝑦) 0.5 0.5 1
We easily compute: 𝐸[𝑋] = 0, 𝐸[𝑌] = 0, Var(𝑋) = 1, Var(𝑌) = 1. Computing directly:
𝐸[𝑋𝑌 ] = (1 ⋅ 1)𝑐 + (−1 ⋅ 1)(0.5 − 𝑐) + (1 ⋅ −1)(0.5 − 𝑐) + (−1 ⋅ −1)𝑐
= 4𝑐−1
Thus,
Cov(𝑋,𝑌) = 𝐸[𝑋𝑌 ]−𝐸[𝑋]𝐸[𝑌] = 4𝑐−1
Cor(𝑋,𝑌 )
Cor(𝑋,𝑌) = = 4𝑐−1.
𝜎 𝜎
𝑋 𝑌
(b) For what value(s) of 𝑐 are 𝑋 and 𝑌 independent? For what value(s) of 𝑐 are 𝑋 and 𝑌
100% correlated?
Solution: Note that the correlation runs from −1 to 1 as 𝑐 runs from 0 to 0.5.
If 𝑋 and 𝑌 are independent then we must have Cov(𝑋,𝑌) = 0. This only happens when
𝑐 = 1 . Covariance equal 0 does not guarantee independence, but for this value of 𝑐, it is
4
easy to check that all four probabilities in the table are 0.25 and 𝑋 and 𝑌 are, indeed,
independent.
When 𝑐 = 0 the correlation is -1, which means 𝑋 and 𝑌 are fully correlated (sometimes
called fully anti-correlated). When 𝑐 = 0.5 the correlation is 1.0 and 𝑋 and 𝑌 are fully
correlated.
Problem 4. (40: 5,5,10,10,10 pts.) Don’t be late!
Alicia and Bernardo are trying to meet for lunch and both will arrive, independently of each
other, uniformly and at random between noon and 1pm. Let 𝐴 and 𝐵 be the number of
minutes after noon at which Alicia and Bernardo arrive, respectively. Then 𝐴 and 𝐵 are
independent uniformly distributed random variables on [0, 60].
18.05 Problem Set 5, Spring 2022 Solutions 4
Hint: For parts (c-e) you might find it easiest to find the fraction of the square [0, 60]×[0, 60]
filled by the event.
(a) Find the joint pdf 𝑓(𝑎, 𝑏) and joint cdf 𝐹 (𝑎, 𝑏).
Solution: The joint probability density function is 𝑓(𝑎,𝑏) = 1 and the joint cumulative
3600
distribution function is
𝑎 𝑏 𝑎𝑏
𝐹(𝑎,𝑏) = ∫ ∫ 𝑓(𝑠,𝑡)𝑑𝑠𝑑𝑡 =
3600
0 0
(b) Find the probability that Alicia arrives before 12:30.
Solution: Since 𝐴 is uniformly distributed on [0,60], 𝑃(𝐴 ≤ 30) = 1.
2
(c) Find the probability that Alicia arrives before 12:15 and Bernardo arrives between 12:30
and 12:45 in two ways:
(i) By using the fact that 𝐴 and 𝐵 are independent.
(ii) By shading the corresponding area of the square [0, 60] × [0, 60] and finding what pro-
portion of the square is shaded.
Solution: (i) 𝑃(𝐴 ≤ 15,30 ≤ 𝐵 ≤ 45) = 𝑃(𝐴 ≤ 15)𝑃(30 ≤ 𝐵 ≤ 45) = 0.0625
(ii) The range of (𝐴, 𝐵) is the square [0, 60] × [0, 60]. The event ‘Alicia arrives before 12:15
and Bernardo arrives between 12:30 and 12:45’ is represented by the solid blue rectangle.
Since the probability distribution is uniform the probability of the blue rectangle is just the
fraction of the entire square that it covers.
Area of blue rectangle = 15×15 = 225. Fraction of the entire square = 225/3600 = 0.0625.
(0, 60)
(60, 60)
𝐴
(15, 45)
(60, 0)
(0, 0) (0, 30)
𝐵
(d) Find the probability that Alicia arrives less than five minutes after Bernardo. (Hint:
use method (ii) from part (c).)
Solution: The shaded area in the figure below corresponds to the event ‘𝐴 ≤ 𝐵+5’. (Note:
if Alicia arrives before Bernardo then she arrives less than 5 minutes after him.) That is,
it corresponds to all pairs of arrival times (𝑎, 𝑏) such that 𝑎 ≤ 𝑏+5. 𝑃(𝐴 ≤ 𝐵+5) is then
just the area of the blue region divided by the area of the entire square. The area of the
blue region is the area of the full square minus the area of the unshaded triangle. The area
552
of the white region is . So,
2
1 552
𝑃(𝐴 ≤ 𝐵+5) = (3600− ) = 0.5799 .
3600 2
18.05 Problem Set 5, Spring 2022 Solutions 5
(0, 60) (55, 60)
(60, 60)
5
+
𝐵
𝐴
=
𝐴
(0, 5)
(60, 0)
(0, 0)
𝐵
(e) Now suppose that Alicia and Bernardo are both rather impatient and will leave if they
have to wait more than 15 minutes for the other to arrive. What is the probability that
Alicia and Bernardo will have lunch together?
Solution: Alicia and Bernardo arrive within 15 minutes of each other is event
𝐸 = 𝐵−15 ≤ 𝐴 ≤ 𝐵+15.
This is the blue shaded region in the figure below. We see that the area of each white
452
triangle is . So, the combined white area is 452 and
2
3600 − 452 7
𝑃(𝐸) = = .
3600 16
(0, 60) (45, 60)
(60, 60)
(60, 45)
𝐴
𝐴 > 𝐵 + 15
5
1
+
𝐵
=
𝐴
5
1
+
𝐴
=
(0, 15)
𝐵
𝐵 > 𝐴 + 15
(60, 0)
(0, 0) (15, 0)
𝐵
Problem 5. (10 pts.) Overlapping sums
Suppose 𝑋 , 𝑋 , … are independent exponential(2) random variables. Suppose also that 𝑋
1 2
is the sum of the first 𝑛 and 𝑌 is the sum of 𝑋 to 𝑋 . Compute Cov(𝑋,𝑌 ) and
𝑛−7 2𝑛−8
Cor(𝑋, 𝑌 ). You should assume that 𝑛 ≥ 8.
Hints: The variance of an exponential(𝜆) random variable is 1/𝜆2. Use the linearity rules
for covariance. What is the size of the overlap?
18.05 Problem Set 5, Spring 2022 Solutions 6
Solution: The problem states that
𝑛 2𝑛−8
𝑋 = ∑𝑋 𝑌 = ∑ 𝑋
𝑖 𝑖
𝑖=1 𝑖=𝑛−7
Notice that 𝑋 and 𝑌 have an overlap of 8 terms. We can use the linearity rules for
covariance:
𝑛 2𝑛−8 𝑛 2𝑛−8
Cov(𝑋,𝑌) = Cov (∑𝑋 , ∑ 𝑋 ) = ∑ ∑ Cov(𝑋 , 𝑋 ).
𝑖 𝑗 𝑖 𝑗
𝑖=1 𝑗=𝑛−7 𝑖=1 𝑗=𝑛−7
That is, Cov(𝑋,𝑌 ) is the sum of all pairs consisting of a term from 𝑋 and a term from 𝑌 .
Since the different terms are independent we know that Cov(𝑋 , 𝑋 ) = 0 if 𝑖 ≠ 𝑗. So only
𝑖 𝑗
the overlap contributes to the covariance:
𝑛 𝑛 𝑛 1
Cov(𝑋,𝑌) = ∑ Cov(𝑋 ,𝑋 ) = ∑ Var(𝑋 ) = ∑
𝑖 𝑖 𝑖 4
𝑖=𝑛−7 𝑖=𝑛−7 𝑖=𝑛−7
There are 8 such terms, all with the variance 1/4, so Cov(𝑋,𝑌) = 8⋅1/4 = 2.
Since 𝑋 is the sum of 𝑛 independent variables with variance 1/4 we have Var(𝑋) = 𝑛/4.
Likewise Var(𝑌) = 𝑛/4. So
Cov(𝑋,𝑌) 2 8
Cor(𝑋,𝑌) = = = .
𝜎 𝜎 𝑛/4 𝑛
𝑋 𝑌
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
