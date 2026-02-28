# Mit18 05 S22 Class15 Pset Sol

---

Class 15 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. More Beta
Suppose your prior 𝑓(𝜃) in the bent coin example is Beta(6, 8). You flip the coin 7 times,
getting 2 heads and 5 tails. What is the posterior pdf 𝑓(𝜃|𝑥)?
(a) Beta(2,5)
(b) Beta(11,10)
(c) Beta(6,8)
(d) Beta(8,13)
Solution: We saw in the first board question that 2 heads and 5 tails will update a
Beta(𝑎, 𝑏) prior to a Beta(𝑎 + 2,𝑏 + 5) posterior.
So the answer is (d), Beta(8, 13).
Concept question 2. Strong priors
Say we have a bent coin with unknown probability of heads 𝜃.
We are convinced that 𝜃 ≤ 0.7.
Our prior is uniform on [0, 0.7] and 0 from 0.7 to 1.
We flip the coin 65 times and get 60 heads.
Which of the graphs below is the posterior pdf for 𝜃?
0.0 0.2 0.4 0.6 0.8 1.0
08
06
04
02
0
A B C D E F
Solution: Graph C, the blue graph spiking near 0.7.
Sixty heads in 65 tosses indicates the true value of 𝜃 is close to 1. Our prior was 0 for
𝜃 > 0.7. So no amount of data will make the posterior non-zero in that range. That is, we
have foreclosed on the possibility of deciding that 𝜃 is close to 1. The Bayesian updating
puts 𝜃 near the top of the allowed range.
Concept question 3. Normal priors, normal likelihood
(a)
1
18.05 class 15 problems, Spring 2022 2
0 2 4 6 8 10 12 14
8.0
6.0
4.0
2.0
0.0
Plot 3 Plot 5
Plot 2
Prior
Plot 4
Plot 1
x_1 x_2 x_3
Blue graph = prior, Red lines = data in order: 3, 9, 12
Which plot is the posterior to just the first data value?
Solution: Plot 2: The first data value is 3. Therefore the posterior must have its mean
between 3 and the mean of the blue prior. The only possibilites for this are plots 1 and 2.
We also know that the variance of the posterior is less than that of the posterior. Between
the plots 1 and 2 graphs only plot 2 has smaller variance than the prior.
Concept question 4. Normal priors, normal likelihood
(b)
0 2 4 6 8 10 12 14
8.0
6.0
4.0
2.0
0.0
Plot 3 Plot 5
Plot 2
Prior
Plot 4
Plot 1
x_1 x_2 x_3
Blue graph = prior, Red lines = data in order: 3, 9, 12
Which graph is posterior to all 3 data values?
Plot 3: The average of the 3 data values is 8. Therefore the posterior must have mean
between the mean of the blue prior and 8. Therefore the only possibilities are the plots 3
and 4. Because the posterior is posterior to the magenta graph (plot 2) it must have smaller
variance. This leaves only the Plot 3.
18.05 class 15 problems, Spring 2022 3
Board questions
Problem 1. Beta priors
Suppose you are testing a new medical treatment with unknown probability of success 𝜃. You
don’t know 𝜃, but your prior belief is that it’s probably not too far from 0.5. You capture
this intuition with a Beta(5,5) prior on 𝜃.
0.0 0.2 0.4 0.6 0.8 1.0
0.2
0.1
0.0
q
Beta(5,5) for
To sharpen this distribution you take data and update the prior.
(𝑎+𝑏 −1)!
• Beta(𝑎, 𝑏): 𝑓(𝜃) = 𝜃𝑎−1(1 − 𝜃)𝑏−1
(𝑎 − 1)!(𝑏 − 1)!
• Treatment has prior 𝑓(𝜃) ∼ Beta(5, 5)
(a) Suppose you test it on 25 patients and have 20 successes.
– Find the posterior distribution on 𝜃.
– Identify the type of the posterior distribution.
(b) Suppose you recorded the order of the results and got
𝑆𝑆𝑆𝑆𝐹 𝑆𝑆𝑆𝑆𝑆𝐹 𝐹 𝑆𝑆𝑆𝐹 𝑆𝐹 𝑆𝑆𝑆𝑆𝑆𝑆𝑆
(20 S and 5 F). Find the posterior based on this data.
(c) Using your answer to (b) give an integral for the posterior predictive probability of
success with the next patient.
(d) Don’t do in class. Use what you know about pdf’s to evaluate the integral without
computing it directly
Solution: (a) Prior pdf is 𝑓(𝜃) = 9! 𝜃4(1−𝜃)4 = 𝑐 𝜃4(1−𝜃)4.
4!4! 1
hyp. prior likelihood Bayes numer. posterior
𝜃 𝑐 𝜃4(1 − 𝜃)4 𝑑𝜃 (25)𝜃20(1 − 𝜃)5 𝑐 𝜃24(1 − 𝜃)9 𝑑𝜃 Beta(25, 10)
1 20 3
Beta(5, 5) binom. prob. Beta(25, 10)
We know the normalized posterior is a Beta distribution because it has the form of a
Beta distribution (𝑐𝜃𝑎−1(1 − 𝜃)𝑏−1 on [0,1]) so by our earlier observation it must be a Beta
distribution.
(b) The answer is the same. The only change is that the likelihood has a coeﬀicient of 1
instead of a binomial coeﬀicent.
18.05 class 15 problems, Spring 2022 4
(c) The posterior on 𝜃 is Beta(25, 10) which has density
34!
𝑓(𝜃 |, data) = 𝜃24(1−𝜃)9.
24!9!
The law of total probability says that the posterior predictive probability of success is
1
𝑃 (success | data) = ∫ 𝑓(success |𝜃) ⋅ 𝑓(𝜃 | data) 𝑑𝜃
0
1 34! 1 34!
= ∫ 𝜃⋅ 𝜃24(1−𝜃)9𝑑𝜃 = ∫ 𝜃25(1−𝜃)9𝑑𝜃
24!9! 24!9!
0 0
(d) We compute the integral in (c) by relating it to the pdf of Beta(26, 10). That pdf is
35!
𝜃25(1 − 𝜃)9. Since any pdf integrates to 1 we have
25!9!
1 35! 1 25! 9!
∫ 𝜃25(1−𝜃)9 = 1 ⇒ ∫ 𝜃25(1−𝜃)9 = .
25!9! 35!
0 0
Thus, we can compute the integral in part (c):
1 34! 34! 25! 9! 25
𝑃 (Success | data) = ∫ 𝜃25(1−𝜃)9𝑑𝜃 = ⋅ . = ≈ 0.71 .
24!9! 24! 9! 35! 35
0
Problem 2. Normal-normal updating
For data 𝑥 , … , 𝑥 with data mean 𝑥 ̄ = 𝑥 1 +…+𝑥 𝑛
1 𝑛 𝑛
1 𝑛 𝑎𝜇 + 𝑏𝑥̄ 1
𝑎 = , 𝑏 = , 𝜇 = prior , 𝜎2 = .
𝜎2 𝜎2 post 𝑎+𝑏 post 𝑎+𝑏
prior
Suppose we have one data point 𝑥 = 2 drawn from N(𝜃, 32)
Suppose 𝜃 is our parameter of interest with prior 𝜃 ∼ N(4, 22).
(a) Identify 𝜇 , 𝜎 , 𝜎, 𝑛, and 𝑥.̄
prior prior
(b) Make a Bayesian update table, but leave the posterior as an unsimplified product.
(c) Use the updating formulas to find the posterior.
Solution: (a) 𝜇 = 4, 𝜎 = 2, 𝜎 = 3, 𝑛 = 1, 𝑥̄ = 2.
prior prior
(b)
hypoth. prior likelihood posterior
𝜃 𝑓(𝜃) ∼ N(4, 22) 𝜙(𝑥|𝜃) ∼ N(𝜃, 32) 𝑓(𝜃|𝑥) ∼ N(𝜇 , 𝜎2 )
post post
𝜃 𝑐 exp
(−(𝜃−4)2
) 𝑐 exp
(−(2−𝜃)2
) 𝑐 exp
(−(𝜃−4)2
) exp
(−(2−𝜃)2
)
1 8 2 18 3 8 18
(c) We have 𝑎 = 1/4, 𝑏 = 1/9, 𝑎+𝑏 = 13/36. Therefore
𝜇 = (1 + 2/9)/(13/36) = 44/13 = 3.3846
post
𝜎2 = 36/13 = 2.7692
post
18.05 class 15 problems, Spring 2022 5
The posterior pdf is 𝑓(𝜃|𝑥 = 2) ∼ N(3.3846, 2.7692).
Problem 2. Normal/normal
Question. On a basketball team the average career free throw percentage over all players
follows a N(75, 62) distribution. In a given year individual players free throw percentage is
N(𝜃, 42) where 𝜃 is their career average.
This season Sophie Lie made 85 percent of her free throws. What is the posterior expected
value of her career percentage 𝜃?
Solution: This is a normal/normal conjugate prior pair, so we use the update formulas.
Parameter of interest: 𝜃 = career average.
Data: 𝑥 = 85 = this year’s percentage.
Prior: 𝜃 ∼ N(75, 36)
Likelihood 𝑥 ∼ N(𝜃, 16). So 𝜙(𝑥|𝜃) = 𝑐 e−(𝑥−𝜃)2/2⋅16.
1
The updating weights are
𝑎 = 1/36, 𝑏 = 1/16, 𝑎 + 𝑏 = 52/576 = 13/144.
Therefore
𝜇 = (75/36 + 85/16)/(13/144) ≈ 81.9, 𝜎2 = 144/13 ≈ 11.1.
post post
The posterior pdf is 𝑓(𝜃|𝑥 = 85) ∼ N(81.9, 11.1).
In class examples and discussion
1. Likelihood principle
Suppose the prior has been set. Let 𝑥 and 𝑥 be two sets of data. Which of the following
1 2
are true?
(a) If the likelihoods 𝜙(𝑥 |𝜃) and 𝜙(𝑥 |𝜃) are the same then they result in the same posterior.
1 2
(b) If the likelihoods 𝜙(𝑥 |𝜃) and 𝜙(𝑥 |𝜃) are proportional (as functions of 𝜃) then they
1 2
result in the same posterior.
(c) If two likelihood functions are proportional then they are equal.
Solution: a: true;
b: true, scale factors don’t matter
c: false
Extra problems
Extra 1. Conjugate priors
Which of the following likelihood/prior pairs are conjugate?
18.05 class 15 problems, Spring 2022 6
hypothesis data prior likelihood
(a)Exponential/Normal 𝜃∈[0,∞) 𝑥 N(𝜇 ,𝜎2 ) exp(𝜃)
prior prior
𝜃 𝑥 𝑐 exp(−(𝜃−𝜇 prior )2 ) 𝜃e−𝜃𝑥
1 2𝜎2
prior
(b)Exponential/Gamma 𝜃∈[0,∞) 𝑥 Gamma(𝑎,𝑏) exp(𝜃)
𝜃 𝑥 𝑐 𝜃𝑎−1e−𝑏𝜃 𝜃e−𝜃𝑥
1
(c) Binomial/Normal 𝜃∈[0,1] 𝑥 N(𝜇 ,𝜎2 ) binomial(𝑁,𝜃)
prior prior
(fixed𝑁) 𝜃 𝑥 𝑐 exp(−(𝜃−𝜇 prior )2 ) 𝑐 𝜃𝑥(1−𝜃)𝑁−𝑥
1 2𝜎2 2
prior
1. none 2. a 3. b 4. c
5. a,b 6. a,c 7. b,c 8. a,b,c
Solution: (b) is the only conjugate pair.
We have a conjugate prior if the posterior as a function of 𝜃 has the same form as the prior.
(a) Exponential/Normal posterior:
−
(𝜃−𝜇prior)2
−𝜃 𝑥
𝑓(𝜃|𝑥) = 𝑐 𝜃e 2𝜎p 2 rior
1
The factor of 𝜃 before the exponential means this is not the pdf of a normal distribution.
Therefore it is not a conjugate prior.
(b) Exponential/Gamma posterior: Note, we have never learned about Gamma distribu-
tions, but it doesn’t matter. We only have to check if the posterior has the same form:
𝑓(𝜃|𝑥) = 𝑐 𝜃𝑎e−(𝑏+𝑥)𝜃
1
The posterior has the form Gamma(𝑎 + 1,𝑏 + 𝑥). This is a conjugate prior.
(c) Binomial/Normal: It is clear that the posterior does not have the form of a normal
distribution.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
