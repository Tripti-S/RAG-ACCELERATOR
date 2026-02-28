# Mit18 05 S22 Class12 Pset Sol

---

Class 12 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. Three coins
• Type 𝐶 coins are fair, with probability 0.5 of heads
0.5
• Type 𝐶 coins have probability 0.6 of heads
0.6
• Type 𝐶 coins have probability 0.9 of heads
0.9
A drawer has one of each.
Pick one; toss 5 times; Suppose you get 1 head out of 5 tosses.
What’s your best guess for the probability of heads on the next toss?
(a) 0.1 (b) 0.2 (c) 0.3 (d) 0.4
(e) 0.5 (f) 0.6 (g) 0.7 (h) 0.8
(i) 0.9 (j) 1.0
Solution: Question is answered in the board questions.
Concept question 2. Suppose instead of saying 1 head in 4 tails, we told you the tosses,
in order, were THTTT. Does this affect posterior distribution of the coin type?
(a) Yes (b) No
Solution: No. When the order is not known, the likelihoods will all have a factor of (5),
1
which is absent when the order is known. This will not affect the posterior probabilities.
Board questions
Problem 1. Three coins
• We have 3 coins with probabilities 0.5, 0.6, and 0.9 of heads.
• Pick one at random; toss 5 times.
• Suppose you get 1 head out of 5 tosses.
Compute the posterior probabilities for the type of coin and the posterior predictive proba-
bilities for the results of the next toss.
(a) Specify clearly the set of hypotheses and the prior probabilities.
(b) Compute the prior and posterior predictive distributions, i.e. give the probabilities of
all possible outcomes.
1
18.05 class 12 problems, Spring 2022 2
(a) Solution: The hypotheses are 𝐶 , the chosen coin has probability 0.5 of landing
0.5
heads. Likewise for 𝐶 and 𝐶 .
0.6 0.9
(b) Solution: Let 𝐻 and 𝑇 stand for heads and tails. The prior predictive probability of
heads is
1 1 1
𝑃(𝐻) = 𝑃(𝐻|𝐶 )𝑃(𝐶 )+𝑃(𝐻|𝐶 )𝑃(𝐶 )+𝑃(𝐻|𝐶 )𝑃(𝐶 ) = 0.5⋅ +0.6⋅ +0.9⋅ = 2/3.
0.5 0.5 0.6 0.6 0.9 0.9 3 3 3
So, the prior predictive probability of tails is 𝑃(𝑇) = 1/3.
The data 𝒟 is ‘1 head and 4 tails’. We first make a Bayesian update table to find the
posterior probabilities (of hypotheses).
Bayes
hypothesis prior likelihood numerator posterior
ℋ 𝑃 (ℋ) 𝑃 (𝒟|ℋ) 𝑃 (𝒟|ℋ)𝑃 (ℋ) 𝑃 (ℋ|𝒟)
𝐶 1/3 (5)(0.5)5 0.0521 0.669
0.5 1
𝐶 1/3 (5)(0.6) ⋅ (0.4)4 0.0256 0.329
0.6 1
𝐶 1/3 (5)(0.9) ⋅ (0.1)4 0.00015 0.002
0.9 1
total 1 0.0778 1
Using the posterior probabilities (of hypotheses) we compute the posterior predictive prob-
abilities of heads and tails.
𝑃(𝐻|𝒟) = 0.669⋅0.5+0.329 ⋅0.6+0.002 ⋅0.9 = 0.53366
𝑃(𝑇|𝒟) = 1−𝑃(𝐻|𝒟) = 0.46634.
So, the posterior predictice probabilities (for all outcomes) are
𝑃 (heads|𝒟) = 0.669 ⋅ 0.5 + 0.329 ⋅ 0.6 + 0.002 ⋅ 0.9 = 0.53366
𝑃 (tails|𝒟) = 1−𝑃(heads|𝒟) = 0.46634.
Problem 2. Screening test odds
A disease is present in 0.005 of the population.
A screening test has a 0.05 false positive rate and a 0.02 false negative rate.
(a) Give the prior odds a patient has the disease
Assume the patient tests positive
(b) What is the Bayes factor for this data?
(c) What are the posterior odds they have the disease?
(d) Based on your answers to (a) and (b) would you say a positive test (the data) provides
strong or weak evidence for the presence of the disease.
Solution: Let ℋ = ‘has disease’ and ℋ = ‘doesn’t have disease’. Let 𝒯 = positive
+ − +
test
𝑃 (ℋ ) 0.005
(a) 𝑂(ℋ ) = + = = 0.00503
+ 𝑃 (ℋ ) 0.995
−
18.05 class 12 problems, Spring 2022 3
(b) The likelihoods are 𝑃 (𝒯 |ℋ ) = 0.98, 𝑃 (𝒯 |ℋ ) = 0.05.
+ + + −
𝑃 (𝒯 |ℋ ) 0.98
So the Bayes factor = likelihood ratio = + + = = 19.6
𝑃 (𝒯 |ℋ ) 0.05
+ −
(c) Posterior odds = Bayes factor × prior odds = 19.6 × 0.00504 = 0.0985
(d) Yes, a Bayes factor of 19.6 indicates a positive test is strong evidence the patient has
the disease. The posterior odds are still small because the prior odds are extremely small.
It would have been slower, but we could have computed the posterior odds by first computing
the posterior probabilities using a Bayesian update table.
Problem 3. CSI Blood Types
We need to weigh the evidence at a crime scene:
• Crime scene: the two perpetrators left blood: one of type O and one of type AB
• In population 60% are type O and 1% are type AB
(a) Suspect Oliver is tested and has type O blood.
Compute the Bayes factor and posterior odds that Oliver was one of the perpetrators.
Is the data evidence for or against the hypothesis that Oliver is guilty?
(b) Same question for suspect Alberto who has type AB blood.
Hopefully helpful hints:
For the question about Oliver we have
Hypotheses:
𝑆 = ‘Oliver and another unknown person were at the scene’
𝑆𝑐 = ‘two unknown people were at the scene’
Data: 𝐷 = ‘type ‘O’ and ‘AB’ blood were found; Oliver is type O’
Prior odds: These are unknown. We can just say 𝑂(𝑆).
*From ‘Information Theory, Inference, and Learning Algorithms’ by David J. C. Mackay.
(a) Solution: (Oliver)
The trickiest part of this is seeing that 𝑃(𝐷|𝑆𝑐) ≈ 2 ⋅0.6⋅0.01. We will show this below.
So,
𝑃(𝐷|𝑆) 0.01
Bayes factor = = = 0.83.
𝑃(𝐷|𝑆𝑐) 2⋅0.6⋅ 0.01
Therefore the posterior odds = 0.83 × prior odds. That is,
𝑂(𝑆|𝐷) = 0.83 ⋅ 𝑂(𝑆).
Since the odds of his presence decreased this is (weak) evidence of his innocence.
Computing 𝑃 (𝐷|𝑆𝑐): Let’s use the following notation:
𝑛 = number of people in the population of type O.
𝑂
𝑛 = number of people in the population of type AB.
𝐴𝐵
𝑛 = total population.
18.05 class 12 problems, Spring 2022 4
So 𝑛 /𝑛 = 0.6 and 𝑛 /𝑛 = 0.01.
𝑂 𝐴𝐵
𝑛 𝑛(𝑛 − 1)
The number of ways to choose two people from the population is ( ) = . The
2 2
number of ways to choose one person of type O who is not Oliver and one of type AB is
(𝑛 − 1) ⋅ 𝑛 . So
𝑂 𝐴𝐵
(𝑛 − 1)𝑛 𝑛 − 1 𝑛
𝑃(𝐷|𝑆𝑐) = 𝑂 𝐴𝐵 = 2⋅ 𝑂 ⋅ 𝐴𝐵 ≈ 2 ⋅0.6⋅0.01.
𝑛(𝑛−1)/2 𝑛 𝑛−1
Here we have assumed that 𝑛 and 𝑛 are large enough that subtracting 1 has a negligible
𝑂
effect, i.e.
𝑛 − 1 𝑛 𝑛 𝑛
𝑂 ≈ 0 = 0.6 and 𝐴𝐵 ≈ 𝐴𝐵 = 0.01.
𝑛 𝑛 𝑛−1 𝑛
(b) For Alberto, the hypotheses are
𝐴 = ‘Alberto and another unknown person were at the scene’
𝐴𝑐 = ‘two unknown people were at the scene’
𝑃 (𝐷|𝐴) 0.6
Bayes factor = = = 50.
𝑃 (𝐷|𝐴𝑐) 2 ⋅ 0.6 ⋅ 0.01
Therefore the posterior odds = 50 × prior odds. That is,
𝑂(𝐴|𝐷) = 50 ⋅ 𝑂(𝐴).
Since the odds of his presence increased this is (strong) evidence of his presence at the
scene.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
