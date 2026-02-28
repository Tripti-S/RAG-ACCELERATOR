# Mit18 05 S22 Prac Exam02A Sol

---

Exam 2 Practice Questions –solutions, 18.05, Spring 2022
1 Topics
• Statistics: data, MLE
• Bayesian inference: prior, likelihood, posterior, predictive probability, probability in-
tervals
• Frequentist inference: NHST
2 Using the probability tables
You should become familiar with the probability tables at the end of these notes.
Problem 1. Use the standard normal table to find the following values. In all the problems
𝑍 is a standard normal random variable.
(a) (i) 𝑃 (𝑍 < 1.5) (ii) 𝑃 (𝑍 > 1.5) (iii) 𝑃 (−1.5 < 𝑍 < 1.5) (iv) 𝑃 (𝑍 ≤ 1.625)
Solution: (i) The table gives this value as 𝑃 (𝑍 < 1.5) = 0.9332.
(ii) This is the complement of the answer in (i): 𝑃 (𝑍 > 1.5) = 1 − 0.9332 = 0.0668. Or by
symmetry we could use the table for -1.5.
(iii) We want 𝑃(𝑍 < 1.5)−𝑃(𝑍 < −1.5) = 𝑃(𝑍 < 1.5)−𝑃(𝑍 > 1.5). This is the difference
of the answers in (i) and (ii): 0.8664.
(iv) A rough estimate is the average of 𝑃 (𝑍 < 1.6) and 𝑃 (𝑍 < 1.65). That is,
𝑃 (𝑍 < 1.6) + 𝑃 (𝑍 < 1.65) 0.9452 + 0.9505
𝑃 (𝑍 < 1.625) ≈ = = 0.9479.
2 2
(b) (i) The right-tail with probability 𝛼 = 0.05.
(ii) The two-sided rejection region with probability 𝛼 = 0.2.
(iii) Find the range for the middle 50% of probability.
Solution: (i) We are looking for the table entry with probability 0.95. This is between the
table entries for 𝑧 = 1.65 and 𝑧 = 1.60 and very close to that of 𝑧 = 1.65. Answer: the
region is [1.64, ∞). (R gives the ‘exact’ lower limit as 1.644854.)
(ii) We want the table entry with probability 0.1. The table probabilities for 𝑧 = −1.25 and
𝑧 = −1.30 are 0.1056 and 0.0968. Since 0.1 is about 1/2 way from the first to the second
we take the left critical value as -1.275. Our region is
(−∞, −1.275) ∪ (1.275, ∞).
(R gives qnorm(0.1, 0, 1) = -1.2816.)
(iii) This is the range from 𝑞 to 𝑞 . With the table we estimate 𝑞 is about 1/2 of
0.25 0.75 0.25
the way from -0.65 to -0.70, i.e. ≈ −0.675. So, the range is [−0.675, 0.675].
1
Exam 2 Practice 2, Spring 2022 2
Problem 2. The 𝑡-tables are different. They give the right critical values corresponding
to probabilities. To save space we only give critical values for 𝑝 ≤ 0.5. You need to use
the symmetry of the 𝑡-distribution to get them for 𝑝 < 0.5. That is, 𝑡 = −𝑡 , e.g.
𝑑𝑓,𝑝 𝑑𝑓,1−𝑝
𝑡 = −𝑡 .
5, 0.975 5, 0.025
Use the 𝑡-table to estimate the following values. In all the problems 𝑇 is a random variable
drawn from a 𝑡-distribution with the indicated number of degrees of freedom.
(a) (i) 𝑃 (𝑇 > 1.6), with 𝑑𝑓 = 3
(ii) 𝑃 (𝑇 < 1.6) with 𝑑𝑓 = 3
(iii) 𝑃 (−1.68 < 𝑇 < 1.68) with 𝑑𝑓 = 49
(iv) 𝑃 (−1.6 < 𝑇 < 1.6) with 𝑑𝑓 = 49
Solution: (i) The question asks to find which 𝑝-value goes with 𝑡 = 1.6 when 𝑑𝑓 = 3. We
look in the 𝑑𝑓 = 3 row of the table and find 1.64 goes with 𝑝 = 0.100 So, 𝑃(𝑇 > 1.6 |𝑑𝑓 =
3) ≈ 0.1. (The true value is a little bit greater.)
(ii) 𝑃(𝑇 < 1.6 |𝑑𝑓 = 3) = 1−𝑃(𝑇 > 1.6 |𝑑𝑓 = 3) ≈ 0.9.
(iii) Using the 𝑑𝑓 = 49 row of the 𝑡-table we find 𝑃(𝑇 > 1.68 |𝑑𝑓 = 49) = 0.05.
Now, by symmetry 𝑃 (𝑇 < −1.68 | 𝑑𝑓 = 49) = 0.05 and 𝑃(−1.68 < 𝑇 < 1.68 |𝑑𝑓 = 49) = 0.9 .
(iv) Using the 𝑑𝑓 = 49 row of the 𝑡-table we find 𝑃(𝑇 > 1.68 |𝑑𝑓 = 49) = 0.05 and
𝑃(𝑇 > 1.30 |𝑑𝑓 = 49) = 0.1. We can do a rough interpolation: 𝑃(𝑇 > 1.6 |𝑑𝑓 = 49) ≈ 0.06.
Now, by symmetry 𝑃(𝑇 < −1.6 |𝑑𝑓 = 49) ≈ 0.06 and 𝑃(−1.6 < 𝑇 < 1.6 |𝑑𝑓 = 49) ≈ 0.88 .
(R gives 0.8839727.)
(b) (i) The critical value for probability 𝛼 = 0.05 for 8 degrees of freedom.
(ii) The two-sided rejection region with probability 𝛼 = 0.2 for 16 degrees of freedom.
(iii) Find the range for the middle 50% of probability with 𝑑𝑓 = 20.
Solution: (i) This is a straightforward lookup: The 𝑝 = 0.05, 𝑑𝑓 = 8 entry is 1.86 .
(ii) For a two-sided rejection region we need 0.1 probability in each tail. The critical value
at 𝑝 = 0.1, 𝑑𝑓 = 16 is 1.34. So (by symmetry) the rejection region is
(−∞, −1.34) ∪ (1.34, ∞).
(iii) This is the range from 𝑞 to 𝑞 , i.e. from critical values 𝑡 to 𝑡 . The ta-
0.25 0.75 0.75 0.25
ble only gives critical for 0.2 and 0.3 For 𝑑𝑓 = 20 these are 0.86 and 0.53. We average
these to estimate the 0.25 critical value as 0.7. Answer: the middle 50% of probability is
approximately between 𝑡-values −0.7 and 0.7.
(If we took into account the bell shape of the 𝑡-distribution we would estimate the 0.25
critical value as slightly closer to 0.53 than 0.86. Indeed R gives the value 0.687.)
Problem 3. The chi-square tables are different. They give the right critical values corre-
sponding to probabilities.
Use the chi-square tables table to find the following values. In all the problems 𝑋2 is
a random variable drawn from a 𝜒2-distribution with the indicated number of degrees of
freedom.
Exam 2 Practice 2, Spring 2022 3
(a) (i) 𝑃(𝑋2 > 1.6), with 𝑑𝑓 = 3
(ii) 𝑃(𝑋2 > 20) with 𝑑𝑓 = 16
Solution: (i) Looking in the 𝑑𝑓 = 3 row of the chi-square table we see that 1.6 is about
1/5 of the way between the values for 𝑝 = 0.7 and 𝑝 = 0.5. So we approximate 𝑃(𝑋2 >
1.6) ≈ 0.66. (The true value is 0.6594.)
(ii) Looking in the 𝑑𝑓 = 16 row of the chi-square table we see that 20 is about 1/4 of the
way between the values for 𝑝 = 0.2 and 𝑝 = 0.3. We estimate 𝑃(𝑋2 > 20) = 0.25. (The
true value is 0.220)
(b) (i) The right critical value for probability 𝛼 = 0.05 for 8 degrees of freedom.
(ii) The two-sided rejection region with probability 𝛼 = 0.2 for 16 degrees of freedom.
Solution: (i) This is in the table in the 𝑑𝑓 = 8 row under 𝑝 = 0.05. Answer: 15.51
(ii) We want the critical values for 𝑝 = 0.9 and 𝑝 = 0.1 from the 𝑑𝑓 = 16 row of the table.
[0, 9.31] ∪ [23.54, ∞).
3 Data
Problem 4. The following data is from a random sample: 5, 1, 3, 3, 8.
Compute the sample mean, sample standard deviation and sample median.
Solution: Sample mean 20/5 = 4.
12 + (−3)2 + (−1)2 + (−1)2 + 42
Sample variance = = 7.
5−1
√
Sample standard deviation = 7.
Sample median = 3.
4 MLE
Problem 5. (a) A coin is tossed 100 times and lands heads 62 times. Find the maximum
likelihood estimate for the probability 𝜃 of heads.
Solution: The likelihood function is
100
𝑝(data|𝜃) = ( )𝜃62(1 − 𝜃)38 = 𝑐𝜃62(1 − 𝜃)38.
62
To find the MLE we find the derivative of the log-likelihood and set it to 0.
ln(𝑝(data|𝜃)) = ln(𝑐) + 62 ln(𝜃) + 38 ln(1 − 𝜃).
𝑑 ln(𝑝(data|𝜃)) 62 38
= − = 0.
𝑑𝜃 𝜃 1−𝜃
The algebra leads to the MLE 𝜃 = 62/100 .
Exam 2 Practice 2, Spring 2022 4
(b) A coin is tossed 𝑛 times and lands heads 𝑘 times. Find the maximum likelihood estimate
for the probability 𝜃 of heads.
Solution: The computation is identical to part (a). The likelihood function is
𝑛
𝑝(data|𝜃) = ( )𝜃𝑘(1 − 𝜃)𝑛−𝑘 = 𝑐𝜃𝑘(1 − 𝜃)𝑛−𝑘.
𝑘
To find the MLE we set the derivative of the log-likelihood and set it to 0.
ln(𝑝(data|𝜃)) = ln(𝑐) + 𝑘 ln(𝜃) + (𝑛 − 𝑘) ln(1 − 𝜃).
𝑑 ln(𝑝(data|𝜃)) 𝑘 𝑛 − 𝑘
= − = 0.
𝑑𝜃 𝜃 1−𝜃
The algebra leads to the MLE 𝜃 = 𝑘/𝑛 .
Problem 6. Suppose the data set 𝑦 , … , 𝑦 is a drawn from a random sample consisting
1 𝑛
of i.i.d. discrete uniform distributions with range 1 to 𝑁. Find the maximum likelihood
estimate of 𝑁 .
Solution: If 𝑁 < max(𝑦 ) then the likelihood 𝑝(𝑦 ,…,𝑦 |𝑁) = 0. So the likelihood
𝑖 1 𝑛
function is
0 if 𝑁 < max(𝑦 )
𝑝(𝑦 ,…,𝑦 |𝑁) = { 𝑖
1 𝑛 (1 ) 𝑛 if 𝑁 ≥ max(𝑦 )
𝑁 𝑖
This is maximized when 𝑁 is as small as possible. Since 𝑁 ≥ max(𝑦 ) the MLE is
𝑖
𝑁 = max(𝑦 ).
𝑖
Problem 7. Suppose data 𝑥 , … , 𝑥 is drawn from an exponential distribution exp(𝜆).
1 𝑛
Find the maximum likelihood for 𝜆.
Solution: The pdf of exp(𝜆) is 𝑝(𝑥|𝜆) = 𝜆e−𝜆𝑥. So the likelihood and log-likelihood
functions are
𝑝(data|𝜆) = 𝜆𝑛e−𝜆(𝑥 1 +⋯+𝑥 𝑛 ), ln(𝑝(data|𝜆)) = 𝑛 ln(𝜆) − 𝜆 ∑ 𝑥 .
𝑖
Taking a derivative with respect to 𝜆 and setting it equal to 0:
𝑑 ln(𝑝(data|𝜆)) 𝑛 1 ∑𝑥
= −∑𝑥 = 0 ⇒ = 𝑖 = 𝑥.̄
𝑑𝜆 𝜆 𝑖 𝜆 𝑛
So the MLE is 𝜆 = 1/𝑥̄ .
Problem 8. Suppose 𝑥 , … , 𝑥 is a data set drawn from a geometric(1/𝑎) distribution.
1 𝑛
Find the maximum likelihood estimate of 𝑎. Here, geometric(𝑝) means the probability of
success is 𝑝 and we run trials until the first success and report the total number of trials,
including the success. For example, the sequence 𝐹 𝐹 𝐹 𝐹 𝑆 is 4 failures followed by a success,
which produces 𝑥 = 5.
1 𝑥 𝑖 −1 1 𝑎−1 𝑥 𝑖 −1 1
Solution: 𝑃 (𝑥 |𝑎) = (1 − ) . = ( ) .
𝑖 𝑎 𝑎 𝑎 𝑎
Exam 2 Practice 2, Spring 2022 5
So, the likelihood function is
𝑎−1 ∑𝑥 𝑖 −𝑛 1 𝑛
𝑃 (data|𝑎) = ( ) ( )
𝑎 𝑎
The log likelihood is
ln(𝑃 (data|𝑎)) = (∑ 𝑥 − 𝑛) (ln(𝑎 − 1) − ln(𝑎)) − 𝑛 ln(𝑎).
𝑖
Taking the derivative
𝑑 ln(𝑃 (data|𝑎)) 1 1 𝑛 ∑𝑥
= (∑𝑥 −𝑛)( − )− = 0 ⇒ 𝑖 = 𝑎.
𝑑𝑎 𝑖 𝑎−1 𝑎 𝑎 𝑛
The maximum likelihood estimate is 𝑎 = 𝑥̄ .
Problem 9. You want to estimate the size of an MIT class that is closed to visitors. You
know that the students are numbered from 1 to 𝑛, where 𝑛 is the number of students. You
call three random students out of the classroom and ask for their numbers, which turn out to
be 1, 3, 7. Find the maximum likelihood estimate for 𝑛. (Hint: the student #’s are drawn
from a discrete uniform distribution.)
Solution: If there are 𝑛 students in the room then for the data 1, 3, 7 (occuring in any
order) the likelihood is
⎧0 for 𝑛 < 7
{
𝑝(data |𝑛) = 𝑛
⎨ { 1/( ) = 3! for 𝑛 ≥ 7
⎩ 3 𝑛(𝑛−1)(𝑛−2)
Maximizing this does not require calculus. It clearly has a maximum when 𝑛 is as small as
possible. Answer: 𝑛 = 7 .
5 Bayesian updating: discrete prior, discrete likelihood
Problem 10. Twins
(a) Suppose 1/4 of twins are identical and 3/4 of twins are fraternal. If you are pregnant
with twins of the same sex, what is the probability that they are identical?
Solution: This is a Bayes’ theorem problem. The likelihoods are
P(same sex | identical) = 1 P(different sex | identical) = 0
P(same sex | fraternal) = 1/2 P(different sex | fraternal) = 1/2
The data is ‘the twins are the same sex’. We find the answer with an update table
hyp. prior likelihood Bayes numer. posterior
identical 1/4 1 1/4 2/5
fraternal 3/4 1/2 3/8 3/5
Tot. 1 5/8 1
So P(identical | same sex) = 2/5 = 0.4 .
Exam 2 Practice 2, Spring 2022 6
(b) Find the posterior odds the twins are identical. Do this by multiplying the prior odds
by the Bayes factor (likelihood ratio). Check this by computing the odds directly from your
answer to part (a).
𝑃 (identical) 1/4
Solution: The prior odds 𝑂(identical) = = = 1/3.
𝑃 (fraternal) 3/4
𝑃 (same sex | identical) 1
The Bayes factor 𝐵𝐹 = = = 2.
𝑃 (same sex|fraternal) 1/2
1 2
So, posterior odds 𝑂(identical | same sex) = 𝑂(identical)⋅𝐵𝐹 = ⋅2 = .
3 3
2/5 2
In part (a) we found the posterior odds 𝑂(identical | same sex) = = . This is the same
3/5 3
as above.
Problem 11. Dice.
You have a drawer full of 4, 6, 8, 12 and 20-sided dice. You suspect that they are in
proportion 1:2:10:2:1. Your friend picks one at random and rolls it twice getting 5 both
times.
(a) What is the probability your friend picked the 8-sided die?
Solution: The data is 5. Let 𝐻 be the hypothesis the die is 𝑛-sided. Here is the update
𝑛
table.
hyp. prior likelihood Bayes numer. posterior
𝐻 1 0 0 0
4
𝐻 2 (1/6)2 2/36 0.243457
6
𝐻 10 (1/8)2 10/64 0.684723
8
𝐻 2 (1/12)2 2/144 0.060864
12
𝐻 1 (1/20)2 1/400 0.010956
20
Tot. 16 0.22819 1
So 𝑃 (𝐻 |data) = 0.685.
8
(b) (i) What is the probability the next roll will be a 5?
(ii) What is the probability the next roll will be a 15?
Solution: We are asked for posterior predictive probabilities. Let 𝑥 be the value of the
next roll. We have to compute the total probability
𝑝(𝑥|data) = ∑𝑝(𝑥|𝐻)𝑝(𝐻|data) = ∑ likelihood × posterior.
The sum is over all hypotheses. We can organize the calculation in a table where we multiply
the posterior column by the appropriate likelihood column. The total posterior predictive
probability is the sum of the product column.
Exam 2 Practice 2, Spring 2022 7
hyp. posterior likelihood post. to (i) likelihood post. to (ii)
to data (i) 𝑥 = 5 (ii) 𝑥 = 15
𝐻 0 0 0 0 0
4
𝐻 0.243457 1/6 0.04058 0 0
6
𝐻 0.684723 1/8 0.08559 0 0
8
𝐻 0.060864 1/12 0.00507 0 0
12
𝐻 0.010956 1/20 0.00055 1/20 0.00055
20
Tot. 0.22819 0.13179 0.00055
So, (i) 𝑝(𝑥 = 5|data) = 0.132 and (ii) 𝑝(𝑥 = 15|data) = 0.00055.
Problem 12.
Sameer has two coins: one fair coin and one biased coin which lands heads with probability
3/4. He picks one coin at random (50-50) and flips it repeatedly until he gets a tails.
Assume that he observes 3 heads before the first tails.
(a) What are the prior and posterior odds for the fair coin?
𝑃 (fair) 1/2
Solution: The prior odds are 𝑂(fair) = = = 1.
𝑃 (not fair) 1/2
The posterior odds are the product of the prior odds and the Bayes factor (likelihood ratio).
The data is 𝐻𝐻𝐻𝑇 . So, the Bayes factor is
𝑃 (data | fair) (1/2)3(1/2) 16
𝐵𝐹 = = = .
𝑃 (data | unfair) (3/4)3(1/4) 27
16 16
So the posterior odds 𝑂(fair | not fair) = 𝑂(fair)⋅𝐵𝐹 = 1⋅ = ≈ 0.593.
27 27
(b) What are the prior and posterior predictive probabilities of heads on the next flip? Here
prior predictive means prior to considering the data of the first four flips.
Solution: The prior predictive probability of heads is
𝑃 (fair)𝑃 (heads | fair) + 𝑃(3/4 coin)𝑃 (heads | 3/4 coin) = 0.5⋅0.5+0.5 ⋅0.75 = 0.625
The posterior predictive probability of heads is
𝑃 (fair | data)𝑃 (heads | fair) + 𝑃(3/4 coin | data)𝑃 (heads | 3/4 coin)
From part (a), we have the posterior odds the coin is fair are 16/27. This tells us the
posterior probabilities are
16 27
𝑃 (fair | data) = , 𝑃(unfair | data) =
43 43
In this problem, the coin is unfair is the same as the coin has a 0.75 probability of heads.
16 27
So, the posterior predictive probability of heads is ⋅0.5+ ⋅0.75 ≈ 0.657
43 43
Method 2: We can also find the posterior probabilities needed to make the prediction
using a Bayesian update table.
Let 𝜃 be the probability of the selected coin landing on heads. We have two hypothese:
𝜃 = 1/2 and 𝜃 = 3/4
Exam 2 Practice 2, Spring 2022 8
Hyp. Prior Likelihood Bayes numer. Posterior
𝜃 = 1/2 1/2 (1/2)3(1/2) 1/25 16/43
𝜃 = 3/4 1/2 (3/4)3(1/4) 33/(2 ⋅ 44) 27/43
Total 1 – 43/512 1
These are the same probabilities we got using odds. So, they will give the same posterior
prediction for heads on the next toss.
6 Bayesian Updating: continuous prior, discrete likelihood
Problem 13. Peter and Jerry disagree over whether 18.05 students prefer Bayesian or
frequentist statistics. They decide to pick a random sample of 10 students from the class
and get Shelby to ask each student which they prefer. They agree to start with a prior
𝑓(𝜃) ∼ Beta(2, 2), where 𝜃 is the percent that prefer Bayesian.
(a) Let 𝑥 be the number of people in the sample who prefer Bayesian statistics. What is
1
the pmf of 𝑥 ?
1
Solution: 𝑥 ∼ Bin(10, 𝜃).
1
(b) Compute the posterior distribution of 𝜃 given 𝑥 = 6.
1
Solution: We have prior:
𝑓(𝜃) = 𝑐 𝜃(1 − 𝜃)
1
and likelihood:
10
𝑝(𝑥 = 6 | 𝜃) = 𝑐 𝜃6(1 − 𝜃)4, where 𝑐 = ( ).
1 2 2 6
The Bayes numerator is 𝑓(𝜃)𝑝(𝑥 |𝜃) = 𝑐 𝑐 𝜃7(1 − 𝜃)5. So the normalized posterior is
1 1 2
𝑓(𝜃|𝑥 ) = 𝑐 𝜃7(1 − 𝜃)5
1 3
Since the posterior has the form of a Beta(8, 6) distribution it must be a Beta(8, 6) distri-
bution. We can look up the normalizing coeﬀicient 𝑐 = 13! .
3 7!5!
(c) Use R to compute 50% and 90% probability intervals for 𝜃. Center the intervals so that
the leftover probability in both tails is the same.
Solution: The 50% interval is
[qbeta(0.25,8,6), qbeta(0.75,8,6)] = [0.48330, 0.66319]
The 90% interval is
[qbeta(0.05,8,6), qbeta(0.95,8,6)] = [0.35480, 0.77604]
(d) The maximum a posteriori (MAP) estimate of 𝜃 (the peak of the posterior) is given by
𝜃̂ = 7/12, leading Jerry to concede that a majority of students are Bayesians. In light of
your answer to part (c) does Jerry have a strong case?
Solution: If the majority prefer Bayes then 𝜃 > 0.5. Since the 50% interval includes 𝜃 < 0.5
and the 90% interval covers a lot of 𝜃 < 0.5 we don’t have a strong case that 𝜃 > 0.5.
As a further test we compute 𝑃 (𝜃 < 0.5|𝑥 ) = pbeta(0.5,8,6) = 0.29053. So there is
1
still a 29% posterior probability that the majority prefers frequentist statistics.
Exam 2 Practice 2, Spring 2022 9
(e) They decide to get another sample of 10 students and ask Neil to poll them. Write
down in detail the expression for the posterior predictive probability that the majority of the
second sample prefer Bayesian statistics. The result will be an integral with several terms.
Don’t bother computing the integral.
Solution: Let 𝑥 be the result of the second poll. We want 𝑝(𝑥 > 5|𝑥 ). We can compute
2 2 1
this using the law of total probability:
1
𝑝(𝑥 > 5|𝑥 ) = ∫ 𝑝(𝑥 > 5|𝜃)𝑝(𝜃|𝑥 ) 𝑑𝜃.
2 1 2 1
0
The two factors in the integral are:
10 10 10
𝑝(𝑥 > 5|𝜃) = ( )𝜃6(1 − 𝜃)4 + ( )𝜃7(1 − 𝜃)3 + ( )𝜃8(1 − 𝜃)2
2 6 7 8
10 10
+ ( )𝜃9(1 − 𝜃)1 + ( )𝜃10(1 − 𝜃)0
9 10
13!
𝑝(𝜃|𝑥 ) = 𝜃7(1 − 𝜃)5
1 7!5!
This can be computed exactly or numerically in R using the integrate() function. The
answer is 𝑃 (𝑥 > 5 |𝑥 = 6) = 0.5521.
2 1
Problem 14. Coins
We have a ‘bent’ coin with an unknown probability 𝜃 of heads. Assume the following:
• Prior for the value of 𝜃: 𝑓(𝜃) = 2(1 − 𝜃) on [0, 1].
• Data: toss once and get tails.
(a) Find the posterior pdf to this data.
Solution: Here’s the update table.
Bayes
hypoth. prior likelihood numerator posterior
𝜃 2(1 − 𝜃) 𝑑𝜃 1 − 𝜃 2(1 − 𝜃)2 𝑑𝜃 3(1 − 𝜃)2 𝑑𝜃
Total 1 𝑇 = ∫ 1 2(1 − 𝜃)2 𝑑𝜃 = 2/3 1
0
Posterior pdf: 𝑓(𝜃|𝑥) = 3(1 − 𝜃)2. (Graph below.)
Note: We don’t really need to compute 𝑇 . Once we know the posterior density is of the
form 𝑐𝜃2 we only have to find the value of 𝑐 which makes it have total probability 1.
(b) Suppose you toss again and get tails. Update your posterior from part (a) using this
data.
Solution: We use the posterior from part (a) as the prior for this part. Here’s the table.
Bayes
hypoth. prior likelihood numerator posterior
𝜃 3(1 − 𝜃)2 𝑑𝜃 1 − 𝜃 3(1 − 𝜃)3, 𝑑𝜃 4(1 − 𝜃)3 𝑑𝜃
Total 1 ∫ 1 3(1 − 𝜃)3 𝑑𝜃 = 3/4 1
0
Exam 2 Practice 2, Spring 2022 10
Posterior pdf: 𝑓(𝜃|𝑥) = (1 − 𝜃)3.
(c) On one set of axes graph the prior and the posteriors from parts (a) and (b).
(c) Solution: Here is the plot of the prior and the two posteriors.
0.0 0.2 0.4 0.6 0.8 1.0
4
3
2
1
0
Prior, posterior a, posterior b
Posterior b
Posterior a
Prior
q
Problem 15. Take your medicine
A lab has an experimental treatment for a disease. The treatment will cure an unknown
fraction 𝜃 of the patients it’s used on. Because it is brand new, they have no idea what 𝜃 is,
so they use a flat prior 𝑓(𝜃) = 1.
In a small preliminary study, the treatment cured 16 out of 20 patients.
Use this data to find the posterior pdf for 𝜃.
Write an integral formula for the normalizing factor (total probability of the data), but do
not compute it. Call its value 𝑇 and give the posterior pdf in terms of 𝑇 .
Solution: Here’s the update table.
Bayes
hypoth. prior likelihood numerator posterior
𝜃 1 ⋅ 𝑑𝜃 (20)𝜃16(1 − 𝜃)4 (20)𝜃16(1 − 𝜃)14 𝑑𝜃 𝑐𝜃16(1 − 𝜃)4 𝑑𝜃
16 16
Total 1 𝑇 = ∫ 1 (20)𝜃16(1 − 𝜃)4 𝑑𝜃 1
0 16
(20)
So, 𝑓(𝜃|𝑥) = 𝑐𝜃16(1 − 𝜃)4, where 𝑐 = 16 .
𝑇
21
A computation (or Wikipedia) would show 𝑐 =
16! 4!
(This is called a Beta distribution.) Here is a plot of the prior and posterior
Exam 2 Practice 2, Spring 2022 11
0.0 0.2 0.4 0.6 0.8 1.0
4
3
2
1
0
Prior and posterior
Posterior
Prior
q
7 Bayesian Updating: normal-normal conjugate pairs
Problem 16. Suppose that you have a cable whose exact length is 𝜃. You have a ruler
with known error normally distributed with mean 0 and variance 10−4. Using this ruler, you
measure your cable, and the resulting measurement 𝑥 is distributed as 𝑁(𝜃, 10−4).
(a) Suppose your prior on the length of the cable is 𝜃 ∼ 𝑁(9,1). If you then measure
𝑥 = 10, what is your posterior pdf for 𝜃?
Solution: We have 𝜇 = 9,𝜎2 = 1 and 𝜎2 = 10−4. The normal-normal updating
prior prior
formulas are
1 𝑛 𝑎𝜇 + 𝑏𝑥̄ 1
𝑎 = 𝑏 = , 𝜇 = prior , 𝜎2 = .
𝜎2 𝜎2 post 𝑎+𝑏 post 𝑎+𝑏
prior
So we compute 𝑎 = 1/1, 𝑏 = 10000, 𝜎2 = 1/(𝑎 + 𝑏) = 1/10001 ≈ 9.999 × 10−5 and
𝑝𝑜𝑠𝑡
𝑎𝜇 + 𝑏𝑥 100009
𝜇 =
prior
= ≈ 9.9999
post 𝑎 + 𝑏 10001
So we have posterior distribution 𝑓(𝜃|𝑥 = 10) ∼ 𝑁(9.9999,9.999×10−5).
(b) With the same prior as in part (a), compute the total number of measurements needed
so that the posterior variance of 𝜃 is less than 10−6.
Solution: We have 𝜎2 = 1 and 𝜎2 = 10−4. The posterior variance of 𝜃 given observations
prior
𝑥 , … , 𝑥 is given by
1 𝑛
1 1
=
1 + 𝑛 1 + 𝑛 ⋅ 104
𝜎2 𝜎2
prior
We wish to find 𝑛 such that the above quantity is less than 10−6. It is not hard to see that
𝑛 = 100 is the smallest value such that this is true.
Exam 2 Practice 2, Spring 2022 12
8 NHST
Problem 17. 𝑧-test
Suppose we have 49 data points with sample mean 6.25 and sample variance 12. We want
to test the following hypotheses
𝐻 : the data is drawn from a 𝑁(4, 102) distribution.
0
𝐻 : the data is drawn from 𝑁(𝜇, 102) where 𝜇 ≠ 4.
𝐴
(a) Test for significance at the 𝛼 = 0.05 level. Use the tables at the end of this file to
compute 𝑝-values.
Solution: Our 𝑧-statistic is
𝑥 ̄ − 𝜇 6.25 − 4
𝑧 = √ = = 1.575
𝜎/ 𝑛 10/7
Under the null hypothesis 𝑧 ∼ N(0, 1) The two-sided 𝑝-value is
𝑝 = 2×𝑃(𝑍 > 1.575) = 2×0.0576 = 0.1152
The probability was computed from the 𝑧-table. We interpolated between 𝑧 = 1.57 and
𝑧 = 1.58 Because 𝑝 > 𝛼 we do not reject 𝐻 .
0
(b) Draw a picture showing the null pdf, the rejection region and the area used to compute
the 𝑝-value.
Solution: The null pdf is standard normal as shown. The orange shaded area is over the
rejection region. The area used to compute significance is shown in orange. The area used
to compute the 𝑝-value is shown with blue stripes. Note, the 𝑧-statistic outside the rejection
region corresponds to the blue completely covering the orange.
𝜙(𝑧|𝐻 )∼N(0,1)
0
𝑧
−1.96 𝑧 =1.575 1.96
reject 𝐻 do not reject 𝐻 reject 𝐻
0 0 0
Problem 18. 𝑡-test
Suppose we have 49 data points with sample mean 6.25 and sample variance 36. We want
to test the following hypotheses:
(a) 𝐻 : the data is drawn from 𝑁(4, 𝜎2), where 𝜎 is unknown.
0
𝐻 : the data is drawn from 𝑁(𝜇, 𝜎2) where 𝜇 ≠ 4.
𝐴
Test for significance at the 𝛼 = 0.05 level. Use the 𝑡-table to find the 𝑝 value.
Solution: Our 𝑡-statistic is
𝑥 ̄ − 𝜇 6.25 − 4
√ = = 2.625
𝑠/ 𝑛 6/7
Exam 2 Practice 2, Spring 2022 13
Under the null hypothesis 𝑡 ∼ 𝑡 . Using the 𝑡-table we find the two-sided 𝑝-value is
48
𝑝 = 2×𝑃(𝑡 > 2.625) < 2×0.005 = 0.01
Because 𝑝 < 𝛼 we reject 𝐻 .
0
(b) Draw a picture showing the null pdf, the rejection region and the area used to compute
the 𝑝-value for part (a).
Solution: The null pdf is a 𝑡-distribution as shown. The rejection region is shown. The
area used to compute significance is shown in orange. The area used to compute the 𝑝-value
is shown with blue stripes. Note, the 𝑡-statistic is inside the rejection region corresponds.
This corresponds to the orange completely covering the blue. The critical values for 𝑡
48
we’re looked up in the table.
𝜙(𝑡|𝐻 )∼𝑡
0 48
𝑧
−2.011 2.011 𝑡=2.625
reject 𝐻 do not reject 𝐻 reject 𝐻
0 0 0
Problem 19. There are lots of good NHST problems in psets 7 and 8, the reading and
in-class problems, including two-sample t test, chi-square, ANOVA, and F-test for equal
variance.
Solution: See the psets 7 and 8.
Problem 20. Probability, MLE, goodness of fit
There was a multicenter test of the rate of success for a certain medical procedure. At each
of the 60 centers the researchers tested 12 subjects and reported the number of successes.
(a) Assume that 𝜃 is the probability of success for one patient and let 𝑥 be the data from
one center. What is the probability mass function of 𝑥?
Solution: This is a binomial distribution. Let 𝜃 be the Bernoulli probability of success in
one test.
12
𝑝(𝑥 = 𝑘) = ( )𝜃𝑘(1 − 𝜃)12−𝑘, for 𝑘 = 0,1,…,12.
𝑘
(b) Assume that the probability of success 𝜃 is the same at each center and the 60 centers
produced data: 𝑥 , 𝑥 , … , 𝑥 . Find the MLE for 𝜃. Write your answer in terms of 𝑥̄
1 2 60
Solution: The likelihood function for the combined data from all 60 centers is
12 12 12
𝑝(𝑥 ,𝑥 ,…,𝑥 |𝜃) = ( )𝜃𝑥 1(1−𝜃)12−𝑥 1( )𝜃𝑥 2(1−𝜃)12−𝑥 2⋯( )𝜃𝑥 60(1−𝜃)12−𝑥 60
1 2 60 𝑥 𝑥 𝑥
1 2 60
= 𝑐𝜃∑𝑥 𝑖(1−𝜃)∑12−𝑥 𝑖
Exam 2 Practice 2, Spring 2022 14
To find the maximum we use the log likelihood. At the same time we make the substitution
60 ⋅ 𝑥̄ for ∑ 𝑥 .
𝑖
ln(𝑝(data | 𝜃)) = ln(𝑐) + 60𝑥̄ ln(𝜃) + 60(12 − 𝑥)̄ ln(1 − 𝜃).
Now we set the derivative to 0:
𝑑 ln(𝑝(data | 𝜃)) 60𝑥̄ 60(12 − 𝑥)̄
= − = 0.
𝑑𝜃 𝜃 1−𝜃
Solving for 𝜃 we get
𝑥̄
𝜃̂ = .
12
Parts (c-e) use the following table which gives counts from 60 centers, e.g. 𝑥 = 2 occurred
in 17 out of 60 centers.
𝑥 0 1 2 3 4 5
counts 4 15 17 10 8 6
Note, the possible values of 𝑥 are 0 to 12. The table shows that 𝑥 > 5 never occurred.
(c) Compute 𝑥̄ the average number of successes over the 60 centers.
Solution: The sample mean is
∑(count × 𝑥)
𝑥̄ =
∑ counts
4 ⋅ 0 + 15 ⋅ 1 + 17 ⋅ 2 + 10 ⋅ 3 + 8 ⋅ 4 + 6 ⋅ 5
=
60
= 2.35
(d) Assuming the probability of success at each center is the same, show that the MLE for
𝜃 is 𝜃̂= 0.1958.
Solution: Just plug 𝑥̄ = 2.35 into the formula from part (b): 𝜃̂= 𝑥/̄ 12 = 2.35/12 = 0.1958
(e) Do a 𝜒2 goodness of fit to test the assumption that the probability of success is the same
at each center. Find the 𝑝-value and use a significance level of 0.05.
In this test the number of degrees of freedom is the number of bins - 2.
Solution: There were 60 trials in all. Our hypotheses are:
𝐻 = the probability of success is the same at all centers. (This determines the probabilities
0
of the counts in each cell of our table.)
𝐻 = the probabilities for the cell counts can be anything as long as they sum to 1, i.e. 𝑥
𝐴
follows an arbitrary multinomial distribution.
Using the the value for 𝜃̂ in part (d) we have the table below. Here are some details of the
computation
Since, in principle, 𝑥 can take any values between 0 and 12, the last cell in the counts is
really for 𝑥 ≥ 5. Thus, the probabilities for 𝑥 = 0,1,2,3,4 are computed using R by 𝑝(𝑥) =
dbinom(x, 12, 0.1958). The last probability for 𝑥 ≥ 5 is computed by sum(dbinom(5:12,
12, 0.1058)). (It could have been computed using pbinom.)
Exam 2 Practice 2, Spring 2022 15
The expected counts are just the probabilities times the number of centers, 60. The com-
ponents of 𝑋2 are computed using the formula 𝑋2 = (𝐸 − 𝑂 )2/𝐸 .
𝑖 𝑖 𝑖 𝑖
𝑥 0 1 2 3 4 ≥ 5
prob 0.0731 0.2137 0.2863 0.2324 0.1273 0.0671
Observed 4 15 17 10 8 6
Expected 4.39 12.82 17.18 13.94 7.64 4.03
𝑋2 0.0344 0.3692 0.0018 1.1149 0.0170 0.9643
𝑖
The 𝜒2 statistic is 𝑋2 = ∑𝑋2 = 2.502. There are 6 cells, so 4 degrees of freedom. The
𝑖
𝑝-value is
𝑝 = 1-pchisq(2.502, 4) = 0.644
With this 𝑝-value we do not reject 𝐻 .
0
The reason the degrees of freedom is two less than the number of cells is that there are two
constraints on assigning cell counts assuming 𝐻 but consistent with the statistics used to
𝐴
compute the expected counts. They are the total number of observations = 60, and the
grand mean 𝑥 = 2.35.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
