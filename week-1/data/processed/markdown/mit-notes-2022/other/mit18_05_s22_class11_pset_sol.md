# Mit18 05 S22 Class11 Pset Sol

---

Class 11 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. Learning from experience
(a) Which treatment would you choose?
1. Treatment 1: cured 100% of patients in a trial.
2. Treatment 2: cured 95% of patients in a trial.
3. Treatment 3: cured 90% of patients in a trial.
Solution: No one correct answer.
(b) Which treatment would you choose?
1. Treatment 1: cured 3 out of 3 patients in a trial.
2. Treatment 2: cured 19 out of 20 patients treated in a trial.
3. Standard treatment: cured 90000 out of 100000 patients in clinical practice.
Solution: No one correct answer.
Board questions
Problem 1. Learning from data
• A certain disease has a prevalence of 0.005.
• A screening test has 2% false positives an 1% false negatives.
Suppose a random patient is screened and has a positive test.
(a) Represent this information with a tree and use Bayes’ theorem to compute the proba-
bilities the patient does and doesn’t have the disease.
(b) Identify the data, hypotheses, likelihoods, prior probabilities and posterior probabilities.
(c) Make a full likelihood table containing all hypotheses and possible test data.
(d) Redo the computation using a Bayesian update table. Match the terms in your table to
the terms in your previous calculation.
Solution: (a) Tree based Bayes computation
Let ℋ mean the patient has the disease and ℋ they don’t.
+ −
Let 𝒯 : they test positive and 𝒯 they test negative.
+ −
We can organize this in a tree:
0.005 0.995
ℋ ℋ
+ −
0.99 0.01 0.02 0.98
𝒯 𝒯 𝒯 𝒯
+ − + −
𝑃 (𝒯 | ℋ )𝑃 (ℋ )
Bayes’ theorem says 𝑃(ℋ |𝒯 ) = + + + .
+ + 𝑃 (𝒯 )
+
1
18.05 class 11 problems, Spring 2022 2
Using the tree, the total probability
𝑃 (𝒯 ) = 𝑃 (𝒯 | ℋ )𝑃 (ℋ ) + 𝑃 (𝒯 | ℋ )𝑃 (ℋ )
+ + + + + − −
= 0.99 ⋅ 0.005 + 0.02 ⋅ 0.995 = 0.02485
So,
𝑃 (𝒯 | ℋ )𝑃 (ℋ ) 0.99 ⋅ 0.005
𝑃(ℋ |𝒯 ) = + + + = = 0.199
+ + 𝑃 (𝒯 ) 0.02485
+
𝑃 (𝒯 | ℋ )𝑃 (ℋ ) 0.02 ⋅ 0.995
𝑃(ℋ |𝒯 ) = + − − = = 0.801
− + 𝑃 (𝒯 ) 0.02485
+
The positive test greatly increases the probability of ℋ , but it is still much less probable
+
than ℋ .
−
(b) Terminology
Data: The data are the results of the experiment. In this case, the positive test.
Hypotheses: The hypotheses are the possible answers to the question being asked. In this
case they are ℋ the patient has the disease; ℋ they don’t.
+ −
Likelihoods: The likelihood given a hypothesis is the probability of the data given that
hypothesis. In this case there are two likelihoods, one for each hypothesis
𝑃 (𝒯 | ℋ ) = 0.99 and 𝑃 (𝒯 | ℋ ) = 0.02.
+ + + −
We repeat: the likelihood is a probability given the hypothesis, not a probability of the
hypothesis.
Prior probabilities of the hypotheses: The priors are the probabilities of the hypotheses
prior to collecting data. In this case,
𝑃 (ℋ ) = 0.005 and 𝑃 (ℋ ) = 0.995
+ −
Posterior probabilities of the hypotheses: The posteriors are the probabilities of the hy-
potheses given the data. In this case
𝑃 (ℋ | 𝒯 ) = 0.199 and 𝑃 (ℋ | 𝒯 ) = 0.801.
+ + − +
Posterior Likelihood Prior
𝑃(𝒯 |ℋ ) ⋅ 𝑃(ℋ )
𝑃(ℋ |𝒯 ) = + + +
+ + 𝑃(𝒯 )
+
Total probability of the data
(c) Full likelihood table
The table holds likelihoods 𝑃 (𝒟|ℋ) for every possible hypothesis and data combination.
hypothesis ℋ likelihood 𝑃 (𝒟|ℋ)
disease state 𝑃 (𝒯 |ℋ) 𝑃 (𝒯 |ℋ)
+ −
ℋ 0.99 0.01
+
ℋ 0.02 0.98
−
18.05 class 11 problems, Spring 2022 3
Notice in the table below that the 𝑃(𝒯 |ℋ) column is exactly the likelihood column in
+
the Bayesian update table.
(d) Calculation using a Bayesian update table
ℋ = hypothesis: ℋ (patient has disease); ℋ (they don’t).
+ −
Data: 𝒯 (positive screening test).
+
Bayes
hypothesis prior likelihood numerator posterior
ℋ 𝑃 (ℋ) 𝑃 (𝒯 |ℋ) 𝑃 (𝒯 |ℋ)𝑃 (ℋ) 𝑃 (ℋ|𝒯 )
+ + +
ℋ 0.005 0.99 0.00495 0.199
+
ℋ 0.995 0.02 0.0199 0.801
−
total 1 NO SUM 𝑃 (𝒯 ) = 0.02485 1
+
Data 𝒟 = 𝒯
+
Total probability: 𝑃 (𝒯 ) = sum of Bayes numerator column = 0.02485
+
𝑃 (𝒯 |ℋ)𝑃 (ℋ) likelihood × prior
Bayes’ theorem: 𝑃 (ℋ|𝒯 ) = + =
+ 𝑃 (𝒯 ) total prob. of data
+
Problem 2. Dice
I have five dice: 4-sided, 6-sided, 8-sided, 12-sided, 20-sided.
I pick one at random, roll it and report that the roll was a 13.
Goal: Find the probabilities the die is 4, 6, 8, 12 or 20 sided.
(a) Identify the hypotheses.
(b) Make a likelihood table with columns for the data ‘rolled a 13’, ‘rolled a 5’ and ‘rolled
a 9’.
(c) Make a Bayesian update table and compute the posterior probabilities that the chosen
die is each of the five dice.
(d) Same question if I had reported a 5.
(e) Same question if I had reported a 9.
Solution: (a) The hypotheses are: ℋ , the chosen die was 4-sided; ℋ , the chosen die
4 6
was 6-sided; Likewise ℋ , ℋ , ℋ .
8 12 20
(b) The likelihoods for a roll of 5, 9 and 13 are
hypothesis ℋ 𝑃 (5|ℋ) 𝑃 (9|ℋ) 𝑃 (13|ℋ)
ℋ 0 0 0
4
ℋ 1/6 0 0
6
ℋ 1/8 1/8 0
8
ℋ 1/12 1/12 0
12
ℋ 1/20 1/20 1/20
20
18.05 class 11 problems, Spring 2022 4
(c) 𝒟 = ‘rolled a 13’. So our likelihood column uses the 𝑃 (13|ℋ) from part (b).
Bayes
hypothesis prior likelihood numerator posterior
ℋ 𝑃 (ℋ) 𝑃 (𝒟|ℋ) 𝑃 (𝒟|ℋ)𝑃 (ℋ) 𝑃 (ℋ|𝒟)
ℋ 1/5 0 0 0
4
ℋ 1/5 0 0 0
6
ℋ 1/5 0 0 0
8
ℋ 1/5 0 0 0
12
ℋ 1/5 1/20 1/100 1
20
total 1 1/100 1
The only possibility is the 20-sided die.
(d) 𝒟 = ‘rolled a 5’. So our likelihood column uses the 𝑃 (5|ℋ) from part (b).
Bayes
hypothesis prior likelihood numerator posterior
ℋ 𝑃 (ℋ) 𝑃 (𝒟|ℋ) 𝑃 (𝒟|ℋ)𝑃 (ℋ) 𝑃 (ℋ|𝒟)
ℋ 1/5 0 0 0
4
ℋ 1/5 1/6 1/30 0.392
6
ℋ 1/5 1/8 1/40 0.294
8
ℋ 1/5 1/12 1/60 0.196
12
ℋ 1/5 1/20 1/100 0.118
20
total 1 0.085 1
ℋ is impossible. The most probable hypothesis is ℋ .
4 6
(e) 𝒟 = ‘rolled a 9’. So our likelihood column uses the 𝑃 (9|ℋ) from part (b).
Bayes
hypothesis prior likelihood numerator posterior
ℋ 𝑃 (ℋ) 𝑃 (𝒟|ℋ) 𝑃 (𝒟|ℋ)𝑃 (ℋ) 𝑃 (ℋ|𝒟)
ℋ 1/5 0 0 0
4
ℋ 1/5 0 0 0
6
ℋ 1/5 0 0 0
8
ℋ 1/5 1/12 1/60 0.625
12
ℋ 1/5 1/20 1/100 0.375
20
total 1 0.0267 1
The most probable hypothesis is ℋ .
12
Problem 3. Iterated updates
Suppose I rolled a 9 and then a 5.
(a) Do the Bayesian update in two steps:
Step 1: First update for the 9.
Step 2: Then update the update for the 5.
(b) Do the Bayesian update in one step.
That is, the data is 𝒟 = ‘9 followed by 5’
Solution: (a) Tabular solution: two steps
18.05 class 11 problems, Spring 2022 5
𝒟 = ‘rolled a 9’, 𝒟 = ‘rolled a 5’
1 2
Bayes numerator = likelihood × prior.
1 1
Bayes numerator = likelihood × Bayes numerator
2 2 1
Bayes Bayes
hyp. prior likel. 1 num. 1 likel. 2 num. 2 posterior
ℋ 𝑃 (ℋ) 𝑃 (𝒟 |ℋ) ∗ ∗ ∗ 𝑃 (𝒟 |ℋ) ∗ ∗ ∗ 𝑃 (ℋ|𝒟 , 𝒟 )
1 2 1 2
ℋ 1/5 0 0 0 0 0
4
ℋ 1/5 0 0 1/6 0 0
6
ℋ 1/5 0 0 1/8 0 0
8
ℋ 1/5 1/12 1/60 1/12 1/720 0.735
12
ℋ 1/5 1/20 1/100 1/20 1/2000 0.265
20
total 1 0.0019 1
(b) Tabular solution: one step
𝒟 = ‘rolled a 9 then a 5’
Bayes
hypothesis prior likelihood numerator posterior
ℋ 𝑃 (ℋ) 𝑃 (𝒟|ℋ) 𝑃 (𝒟|ℋ)𝑃 (ℋ) 𝑃 (ℋ|𝒟)
ℋ 1/5 0 0 0
4
ℋ 1/5 0 0 0
6
ℋ 1/5 0 0 0
8
ℋ 1/5 1/144 1/720 0.735
12
ℋ 1/5 1/400 1/2000 0.265
20
total 1 0.0019 1
Problem 4. Probabilistic prediction (Probably won’t get here till next time)
With the same setup as before let:
𝒟 = result of first roll, 𝒟 = result of second roll
1 2
(a) Find 𝑃(𝒟 = 5).
1
(b) Find 𝑃 (𝒟 = 4|𝒟 = 5).
2 1
Solution: 𝒟 = ‘rolled a 5’, 𝒟 = ‘rolled a 4’
1 2
Bayes
hyp. prior likel. 1 num. 1 post. 1 likel. 2 post. 1 × likel. 2
ℋ 𝑃 (ℋ) 𝑃 (𝒟 |ℋ) ∗ ∗ ∗ 𝑃 (ℋ|𝒟 ) 𝑃 (𝒟 |ℋ, 𝒟 ) 𝑃 (𝒟 |ℋ, 𝒟 )𝑃 (ℋ|𝒟 )
1 1 2 1 2 1 1
ℋ 1/5 0 0 0 ∗ 0
4
ℋ 1/5 1/6 1/30 0.392 1/6 0.392 ⋅ 1/6
6
ℋ 1/5 1/8 1/40 0.294 1/8 0.294 ⋅ 1/40
8
ℋ 1/5 1/12 1/60 0.196 1/12 0.196 ⋅ 1/12
12
ℋ 1/5 1/20 1/100 0.118 1/20 0.118 ⋅ 1/20
20
total 1 0.085 1 0.124
The law of total probability tells us 𝑃 (𝒟 ) is the sum of the Bayes numerator 1 column in
1
the table: 𝑃 (𝒟 ) = 0.085 .
1
The law of total probability tells us 𝑃 (𝒟 |𝒟 ) is the sum of the last column in the table:
2 1
18.05 class 11 problems, Spring 2022 6
𝑃 (𝒟 |𝒟 ) = 0.124 Solution: 𝒟 = ‘rolled a 5’, 𝒟 = ‘rolled a 4’
2 1 1 2
Bayes
hyp. prior likel. 1 num. 1 post. 1 likel. 2 post. 1 × likel. 2
ℋ 𝑃 (ℋ) 𝑃 (𝒟 |ℋ) ∗ ∗ ∗ 𝑃 (ℋ|𝒟 ) 𝑃 (𝒟 |ℋ, 𝒟 ) 𝑃 (𝒟 |ℋ, 𝒟 )𝑃 (ℋ|𝒟 )
1 1 2 1 2 1 1
ℋ 1/5 0 0 0 ∗ 0
4
ℋ 1/5 1/6 1/30 0.392 1/6 0.392 ⋅ 1/6
6
ℋ 1/5 1/8 1/40 0.294 1/8 0.294 ⋅ 1/40
8
ℋ 1/5 1/12 1/60 0.196 1/12 0.196 ⋅ 1/12
12
ℋ 1/5 1/20 1/100 0.118 1/20 0.118 ⋅ 1/20
20
total 1 0.085 1 0.124
The law of total probability tells us 𝑃 (𝒟 ) is the sum of the Bayes numerator 1 column in
1
the table: 𝑃 (𝒟 ) = 0.085 .
1
The law of total probability tells us 𝑃 (𝒟 |𝒟 ) is the sum of the last column in the table:
2 1
𝑃 (𝒟 |𝒟 ) = 0.124
2 1
Extra problems
Extra 1. Bayesian updating: terminology, trees, tables
I have a bag with one 4-sided die and 999 6-sided dice. I pick one at random and roll it.
Suppose I get a 3.
Goal: find the probabilities the chosen die was 4-sided or 6-sided.
(a) Identify the hypotheses.
(b) Use Bayes’ theorem to compute the posterior probabilities. Organize the computation
using trees.
(c) Connect all the Bayesian updating terminology with the parts of the computation.
(d) Redo the computation using a Bayesian updating table.
Solution: (a) The hypotheses are: ℋ , the chosen die was 4-sided and ℋ , the chosen
4 6
die was 4-sided;
(b) Let 𝑅 be the value of the roll. Here is the probability tree:
Prior 1/1000 999/1000
Hypotheses ℋ ℋ
4 6
Likelihoods 1/4 3/4 1/6 5/6
𝑅=3 𝑅≠3 𝑅=3 𝑅≠3
𝑃 (𝑅 = 3 | ℋ )𝑃 (ℋ )
Bayes’ theorem says 𝑃(ℋ |𝑅 = 3) = 4 4 . Likewise for ℋ
4 𝑃(𝑅 = 3) 6
Using the tree, the total probability of 𝑅 = 3.
𝑃 (𝑅 = 3) = 𝑃 (𝑅 = 3 | ℋ )𝑃 (ℋ ) + 𝑃 (𝑅 = 3 | ℋ )𝑃 (ℋ ) = 1/4000 + 999/6000 = 0.167
4 4 6 6
18.05 class 11 problems, Spring 2022 7
So,
𝑃 (𝑅 = 3 | ℋ )𝑃 (ℋ ) 1/4000
𝑃(ℋ |𝑅 = 3) = 4 4 = ≈ 0.0015
4 𝑃(𝑅 = 3) 0.167
𝑃 (𝑅 = 3 | ℋ )𝑃 (ℋ ) 999/6000
𝑃(ℋ |𝑅 = 3) = 6 6 = ≈ 0.9985
6 𝑃 (𝑅 = 3) 0.167
The roll of 3 increases the probability of ℋ , but it is still much less probable than ℋ .
4 6
(c) Terminology
Data: The data are the results of the experiment. In this case, 𝑅 = 3.
Hypotheses: The hypotheses are the possible answers to the question being asked. In this
case they are ℋ the die is 4-sided and ℋ the die is 6-sided.
4 6
Likelihoods: The likelihood given a hypothesis is the probability of the data given that
hypothesis. In this case there are two likelihoods, one for each hypothesis
𝑃(𝑅 = 3|ℋ ) = 1/4 and 𝑃(𝑅 = 3|ℋ ) = 1/6.
4 6
We repeat: the likelihood is a probability given the hypothesis, not a probability of the
hypothesis.
Prior probabilities of the hypotheses: The priors are the probabilities of the hypotheses
prior to collecting data. In this case,
𝑃 (ℋ ) = 1/1000 and 𝑃 (ℋ ) = 999/1000.
4 6
Posterior probabilities of the hypotheses: The posteriors are the probabilities of the hy-
potheses given the data. In this case
𝑃(ℋ |𝑅 = 3) ≈ 0.0015 and 𝑃(ℋ |𝑅 = 3) ≈ 0.9985. (Computed below.)
4 6
Posterior Likelihood Prior
𝑃(𝑅 =3|ℋ )⋅𝑃(ℋ )
𝑃(ℋ |𝑅 =3) = 4 4
4 𝑃(𝑅=3)
Total probability of the data
(d) Calculation using a Bayesian update table
ℋ = hypothesis: ℋ (4-sided die); ℋ (6-sided die).
4 6
Data: 𝑅 = 3 (roll of 3).
Bayes
hypothesis prior likelihood numerator posterior
ℋ 𝑃 (ℋ) 𝑃 (𝑅 = 3|ℋ) 𝑃 (𝑅 = 3|ℋ)𝑃 (ℋ) 𝑃 (ℋ|𝑅 = 3)
ℋ 1/1000 1/4 1/4000 1/4000 ≈ 0.0015
4 0.167
ℋ 999/1000 1/6 999/6000 999/6000 ≈ 0.9985
6 0.167
total 1 NO SUM 𝑃 (𝑅 = 3) = 0.167 1
18.05 class 11 problems, Spring 2022 8
The Total probability of the data is 𝑃(𝑅 = 3) = sum of Bayes numerator column = 0.167.
𝑃 (𝑅 = 3|ℋ)𝑃 (ℋ) likelihood × prior
Bayes’ theorem: 𝑃(ℋ|𝑅 = 3) = =
𝑃(𝑅 = 3) total prob. of data
The posterior probabilities are identical to those from the tree based calculation.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
