# Mit18 05 S22 Class07 Pset Sol

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
Solution: Yes. Every cell probability is the product of the marginal probabilities.
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
Solution: No. The cells with probability zero are clearly not the product of the marginal
probabilities.
Concept question 3. Independence III
Which of the following joint pdfs are the variables independent? (Each of the ranges is a
rectangle chosen so that ∫∫𝑓(𝑥,𝑦)𝑑𝑥𝑑𝑦 = 1.)
(i) 𝑓(𝑥,𝑦) = 4𝑥2𝑦3.
(ii) 𝑓(𝑥,𝑦) = 1(𝑥3𝑦+𝑥𝑦3).
2
(iii) 𝑓(𝑥,𝑦) = 6𝑒−3𝑥−2𝑦
1
18.05 class 7 problems, Spring 2022 2
(a) i (b) ii (c) iii (d) i, ii
(e) i, iii (f) ii, iii (g) i, ii, iii (h) None
(i) Independent. The variables can be separated: the marginal densities are 𝑓 (𝑥) = 𝑎𝑥2
𝑋
and 𝑓 (𝑦) = 𝑏𝑦3 for some constants 𝑎 and 𝑏 with 𝑎𝑏 = 4.
𝑌
(ii) Not independent. 𝑋 and 𝑌 are not independent because there is no way to factor
𝑓(𝑥, 𝑦) into a product 𝑓 (𝑥)𝑓 (𝑦).
𝑋 𝑌
(iii) Independent. The variables can be separated: the marginal densities are 𝑓 (𝑥) =
𝑋
𝑎e−3𝑥 and 𝑓 (𝑦) = 𝑏e−2𝑦 for some constants 𝑎 and 𝑏 with 𝑎𝑏 = 6.
𝑌
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
Solution: (a) Validity: Clearly 𝑓(𝑥, 𝑦) is positive. Next we must show that total proba-
bility = 1:
1 1 1 1 1 1 1
∫ ∫ 𝑥+𝑦𝑑𝑥𝑑𝑦 = ∫ [ 𝑥2+𝑥𝑦] 𝑑𝑦 = ∫ +𝑦𝑑𝑦 = 1.
2 2
0 0 0 0 0
(b) Here’s the visualization
18.05 class 7 problems, Spring 2022 3
𝑦
1
𝐴
.5
𝑥
.3 1
The pdf is not constant so we must compute an integral
1 1
𝑃(𝐴) = ∫ ∫ 𝑥+𝑦𝑑𝑥𝑑𝑦 = 0.49 .
0.5 0.3
Make sure you are able to do this integral. Ask if you have any questions.
𝑦 𝑥 𝑥2𝑦 𝑥𝑦2
(c) 𝐹(𝑥,𝑦) = ∫ ∫ 𝑢+𝑣𝑑𝑢𝑑𝑣 = + .
2 2
0 0
(d) To find the marginal cdf 𝐹 (𝑥) we simply take 𝑦 to be the top of the 𝑦-range and
𝑋
𝑥2 𝑥
evalute 𝐹 : 𝐹 (𝑥) = 𝐹(𝑥,1) = + . So 𝑃 (𝑋 < 0.5) = 3/8.
𝑋 2 2
1
(e) 𝑓 (𝑥) = 𝐹′ (𝑥) = 𝑥 + .
𝑋 𝑋 2
1 𝑦2 1 1
Or, 𝑓 (𝑥) = ∫ 𝑥+𝑦𝑑𝑦 = [𝑥𝑦+ ] = 𝑥+ . So,
𝑋 2 2
0 0
0.5 0.5 1 1 1 0.5 3
𝑃(𝑋 < 0.5) = ∫ 𝑓 (𝑥)𝑑𝑥 = ∫ 𝑥+ 𝑑𝑥 = [ 𝑥2+ 𝑥] = .
𝑋 2 2 2 8
0 0 0
(f) 𝐹(3.5,4) = 𝑃(𝑋 ≤ 3.5,𝑌 ≤ 4).
𝑋\𝑌 1 2 3 4 5 6
1 1/36 1/36 1/36 1/36 1/36 1/36
2 1/36 1/36 1/36 1/36 1/36 1/36
3 1/36 1/36 1/36 1/36 1/36 1/36
4 1/36 1/36 1/36 1/36 1/36 1/36
5 1/36 1/36 1/36 1/36 1/36 1/36
6 1/36 1/36 1/36 1/36 1/36 1/36
Add the probability in the shaded squares: 𝐹 (3.5, 4) = 12/36 = 1/3.
Problem 2. Covariance and correlation
Flip a fair coin 11 times. (The tosses are all independent.)
Let 𝑋 = number of heads in the first 6 flips
Let 𝑌 = number of heads on the last 6 flips.
Compute Cov(𝑋, 𝑌 ) and Cor(𝑋, 𝑌 ).
Solution: Use the properties of covariance.
18.05 class 7 problems, Spring 2022 4
𝑋 = the number of heads on the 𝑖th flip. (So 𝑋 ∼ Bernoulli(0.5).)
𝑖 𝑖
𝑋 = 𝑋 +𝑋 +…+𝑋 and 𝑌 = 𝑋 +𝑋 +…+𝑋 .
1 2 6 6 7 11
We know Var(𝑋 ) = 1/4. Therefore, using Property 2 (linearity) of covariance
𝑖
Cov(𝑋,𝑌) = Cov(𝑋 +𝑋 +…+𝑋 , 𝑋 +𝑋 +…+𝑋 )
1 2 6 6 7 11
= Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 ) + … + Cov(𝑋 , 𝑋 )
1 6 1 7 1 11
+ Cov(𝑋 , 𝑋 ) + … + Cov(𝑋 , 𝑋 )
2 6 2 11
+ Cov(𝑋 , 𝑋 ) + … + Cov(𝑋 , 𝑋 )
3 6 3 11
+ Cov(𝑋 , 𝑋 ) + … + Cov(𝑋 , 𝑋 )
4 6 4 11
+ Cov(𝑋 , 𝑋 ) + … + Cov(𝑋 , 𝑋 )
5 6 5 11
+ Cov(𝑋 , 𝑋 ) + … + Cov(𝑋 , 𝑋 )
6 6 6 11
Since the different tosses are independent we know
Cov(𝑋 , 𝑋 ) = 0, Cov(𝑋 , 𝑋 ) = 0, Cov(𝑋 , 𝑋 ) = 0, etc.
1 6 1 7 1 8
Looking at the expression for Cov(𝑋, 𝑌 ) there is only one non-zero term
1
Cov(𝑋,𝑌) = Cov(𝑋 , 𝑋 ) = Var(𝑋 ) = .
6 6 6 4
For correlation we need 𝜎 and 𝜎 . Since each is the sum of 6 independent Bernoulli(0.5)
𝑋 𝑌
variables we have Var(𝑋) = Var(𝑌) = 6/4. So, 𝜎 = 𝜎 = √3/2.
𝑋 𝑌
Cov(𝑋,𝑌) 1/4
Thus Cor(𝑋,𝑌) = = = 1/6.
𝜎 𝜎 3/2
𝑋 𝑌
Problem 3. Even more tosses
Toss a fair coin 2𝑛 + 1 times. Let 𝑋 be the number of heads on the first 𝑛 + 1 tosses and
𝑌 the number on the last 𝑛 + 1 tosses.
Compute Cov(𝑋, 𝑌 ) and Cor(𝑋, 𝑌 ).
Solution: As usual let 𝑋 = the number of heads on the 𝑖th flip, i.e. 0 or 1. Then
𝑖
𝑛+1 2𝑛+1
𝑋 = ∑𝑋 , 𝑌 = ∑ 𝑋
𝑖 𝑖
1 𝑛+1
𝑋 is the sum of 𝑛 + 1 independent Bernoulli(1/2) random variables, so
𝑛+1 𝑛+1
𝜇 = 𝐸[𝑋] = , and Var(𝑋) = .
𝑋 2 4
𝑛+1 𝑛+1
Likewise, 𝜇 = 𝐸[𝑌 ] = , and Var(𝑌) = .
𝑌 2 4
Now,
𝑛+1 2𝑛+1 𝑛+1 2𝑛+1
Cov(𝑋,𝑌) = Cov (∑𝑋 ∑ 𝑋 ) = ∑ ∑ Cov(𝑋 𝑋 ).
𝑖 𝑗 𝑖 𝑗
1 𝑛+1 𝑖=1 𝑗=𝑛+1
18.05 class 7 problems, Spring 2022 5
1
Because the 𝑋 are independent the only non-zero term in the above sum is Cov(𝑋 𝑋 ) = Var(𝑋 ) =
𝑖 𝑛+1 𝑛+1 𝑛+1 4
Therefore,
1
Cov(𝑋,𝑌) = .
4
We get the correlation by dividing by the standard deviations.
Cov(𝑋,𝑌) 1/4 1
Cor(𝑋,𝑌) = = = .
𝜎 𝜎 (𝑛 + 1)/4 𝑛 + 1
𝑋 𝑌
This makes sense: as 𝑛 increases the correlation should decrease since the contribution of
the one flip they have in common becomes less important.
Extra
Discussion: Real-life correlations
• Over time, amount of ice cream consumption is correlated with number of pool drown-
ings.
• In 1685 (and today) being a student is the most dangerous profession. That is, the
average age of those who die is less than any other profession.
• In 90% of bar fights ending in a death the person who started the fight died.
• Hormone replacement therapy (HRT) is correlated with a lower rate of coronary heart
disease (CHD).
Discussion
• Ice cream does not cause drownings. Both are correlated with summer weather.
• In a study in 1685 of the ages and professions of deceased men, it was found that the
profession with the lowest average age of death was “student.” But, being a student
does not cause you to die at an early age. Being a student means you are young. This
is what makes the average of those that die so low.
• A study of fights in bars in which someone was killed found that, in 90% of the cases,
the person who started the fight was the one who died.
Of course, it’s the person who survived telling the story.
• In a widely studied example, numerous epidemiological studies showed that women
who were taking combined hormone replacement therapy (HRT) also had a lower-
than-average incidence of coronary heart disease (CHD), leading doctors to propose
that HRT was protective against CHD. But randomized controlled trials showed that
HRT caused a small but statistically significant increase in risk of CHD. Re-analysis of
the data from the epidemiological studies showed that women undertaking HRT were
more likely to be from higher socio-economic groups (ABC1), with better-than-average
diet and exercise regimens. The use of HRT and decreased incidence of coronary heart
disease were coincident effects of a common cause (i.e. the benefits associated with a
higher socioeconomic status), rather than cause and effect, as had been supposed.
18.05 class 7 problems, Spring 2022 6
Edward Tufte: ”Empirically observed covariation is a necessary but not suﬀicient condition
for causality.”
Extra problem 1: Hospitals, binomial, CLT etc.
Here’s one more problem. We won’t do this in class.
• A certain town is served by two hospitals.
• Larger hospital: about 45 babies born each day.
• Smaller hospital about 15 babies born each day.
• For a period of 1 year, each hospital recorded the days on which more than 60% of the
babies born were boys.
(a) Which hospital do you think recorded more such days?
(i) The larger hospital. (ii) The smaller hospital.
(iii) About the same (that is, within 5% of each other).
(b) Assume exactly 45 and 15 babies are born at the hospitals each day. Let 𝐿 (resp., 𝑆 ) be
𝑖 𝑖
the Bernoulli random variable which takes the value 1 if more than 60% of the babies born
in the larger (resp., smaller) hospital on the 𝑖th day were boys. Determine the distribution
of 𝐿 and of 𝑆 .
𝑖 𝑖
(c) Let 𝐿 (resp., 𝑆) be the number of days on which more than 60% of the babies born in
the larger (resp., smaller) hospital were boys. What type of distribution do 𝐿 and 𝑆 have?
Compute the expected value and variance in each case.
(d) Via the CLT, approximate the 0.84 quantile of 𝐿 (resp., 𝑆). Would you like to revise
your answer to part (a)?
(e) What is the correlation of 𝐿 and 𝑆? What is the joint pmf of 𝐿 and 𝑆? Visualize the
region corresponding to the event 𝐿 > 𝑆. Express 𝑃(𝐿 > 𝑆) as a double sum.
Solution: (a) When this question was asked in a study, the number of undergraduates
who chose each option was 21, 21, and 55, respectively. This shows a lack of intuition for
the relevance of sample size on deviation from the true mean (i.e., variance).
(b) The random variable 𝑋 , giving the number of boys born in the larger hospital on day
𝐿
𝑖, is governed by a Bin(45, 0.5) distribution. So 𝐿 has a Ber(𝑝 ) distribution with
𝑖 𝐿
45
45
𝑝 = 𝑃 (𝑋 > 27) = ∑ ( ) 0.545 ≈ 0.068.
𝐿 ∶ 𝑘
𝑘=28
Similarly, the random variable 𝑋 , giving the number of boys born in the smaller hospital
𝑆
on day 𝑖, is governed by a Bin(15, 0.5) distribution. So 𝑆 has a Ber(𝑝 ) distribution with
𝑖 𝑆
15
15
𝑝 = 𝑃 (𝑋 > 9) = ∑ ( ) 0.515 ≈ 0.151.
𝑆 𝑆 𝑘
𝑘=10
18.05 class 7 problems, Spring 2022 7
We see that 𝑝 is indeed greater than 𝑝 , consistent with (𝑖𝑖).
𝑆 𝐿
365 365
(c) Note that 𝐿 = ∑ 𝐿 and 𝑆 = ∑ 𝑆 . So 𝐿 has a Bin(365, 𝑝 ) distribution and 𝑆
𝑖=1 𝑖 𝑖=1 𝑖 𝐿
has a Bin(365, 𝑝 ) distribution. Thus
𝑆
𝐸[𝐿] = 365𝑝 ≈ 25
𝐿
𝐸[𝑆] = 365𝑝 ≈ 55
𝑆
Var(𝐿) = 365𝑝 (1 − 𝑝 ) ≈ 23
𝐿 𝐿
Var(𝑆) = 365𝑝 (1 − 𝑝 ) ≈ 47
𝑆 𝑆
(d) By the CLT, the 0.84 quantile is approximately the mean + one sd in each case:
√
For 𝐿, 𝑞 ≈ 25 + 23.
0.84
√
For 𝑆, 𝑞 ≈ 55 + 47.
0.84
(e) Since 𝐿 and 𝑆 are independent, their correlation is 0 and theirjoint distribution is
determined by multiplying their individual distributions. Both 𝐿 and 𝑆 are binomial with
𝑛 = 365 and 𝑝 and 𝑝 computed above. Thus
𝐿 𝑆
365 365
𝑃(𝐿 = 𝑖 and 𝑆 = 𝑗) = 𝑝(𝑖,𝑗) = ( )𝑝𝑖 (1−𝑝 )365−𝑖( )𝑝𝑗(1−𝑝 )365−𝑗
𝑖 𝐿 𝐿 𝑗 𝑆 𝑆
Thus
364 365
𝑃(𝐿 > 𝑆) = ∑ ∑ 𝑝(𝑖,𝑗) ≈ 0.0000916
𝑖=0 𝑗=𝑖+1
We used the R code below to do the computations.
pL = 1 - pbinom(0.6*45, 45, 0.5)
pS = 1 - pbinom(0.6*15, 15, 0.5)
print(pL)
print(pS)
pLGreaterS = 0
for(i in 0:365) {
for(j in 0:(i-1)) {
pLGreaterS = pLGreaterS + dbinom(i,365,pL)*dbinom(j,365,pS)
}
}
print(pLGreaterS)
Extra problem 2: Correlation
(a) Flip a coin 3 times. Use a joint pmf table to compute the covariance and correlation
between the number of heads on the first 2 and the number of heads on the last 2 flips.
(b) Flip a coin 5 times. Use properties of covariance to compute the covariance and
correlation between the number of heads on the first 3 and last 3 flips.
Solution: (a) Let 𝑋 = the number of heads on the first 2 flips and 𝑌 the number in the
last 2. Considering all 8 possibe tosses: 𝐻𝐻𝐻, 𝐻𝐻𝑇 etc we get the following joint pmf for
𝑋 and 𝑌
18.05 class 7 problems, Spring 2022 8
𝑌 /𝑋 0 1 2
0 1/8 1/8 0 1/4
1 1/8 1/4 1/8 1/2
2 0 1/8 1/8 1/4
1/4 1/2 1/4 1
Using the table we find
1 1 1 1 5
𝐸[𝑋𝑌 ] = +2 +2 +4 = .
4 8 8 8 4
We know 𝐸[𝑋] = 1 = 𝐸[𝑌 ] so
5 1
Cov(𝑋,𝑌) = 𝐸[𝑋𝑌 ]−𝐸[𝑋]𝐸[𝑌] = −1 = .
4 4
Since 𝑋 is the sum of 2 independent Bernoulli(0.5) we have 𝜎 = √2/4
𝑋
Cov(𝑋,𝑌) 1/4 1
Cor(𝑋,𝑌) = = = .
𝜎 𝜎 (2)/4 2
𝑋 𝑌
(b) As usual let 𝑋 = the number of heads on the 𝑖th flip, i.e. 0 or 1.
𝑖
Let 𝑋 = 𝑋 +𝑋 +𝑋 the sum of the first 3 flips and 𝑌 = 𝑋 +𝑋 +𝑋 the sum of the
1 2 3 3 4 5
last 3. Using the algebraic properties of covariance we have
Cov(𝑋,𝑌) = Cov(𝑋 + 𝑋 + 𝑋 , 𝑋 + 𝑋 + 𝑋 )
1 2 3 3 4 5
= Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 )
1 3 1 4 1 5
+ Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 )
2 3 2 4 2 5
+ Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 ) + Cov(𝑋 , 𝑋 )
3 3 3 4 3 5
1
Because the 𝑋 are independent the only non-zero term in the above sum is Cov(𝑋 𝑋 ) = Var(𝑋 ) = .
𝑖 3 3 3 4
Therefore, Cov(𝑋,𝑌) = 1.
4
We get the correlation by dividing by the standard deviations. Since 𝑋 is the sum of 3
independent Bernoulli(0.5) we have 𝜎 = √3/4
𝑋
Cov(𝑋,𝑌) 1/4 1
Cor(𝑋,𝑌) = = = .
𝜎 𝜎 (3)/4 3
𝑋 𝑌
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
