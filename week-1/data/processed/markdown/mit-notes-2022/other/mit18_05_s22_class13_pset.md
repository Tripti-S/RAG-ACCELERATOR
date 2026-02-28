# Mit18 05 S22 Class13 Pset

---

Class 13 in-class problems, 18.05, Spring 2022
In class examples and discussion
Class example 1.
• Three types of coins with probabilities 0.25, 0.5, 0.75 of heads.
• Assume the numbers of each type are in the ratio 1 to 2 to 1.
• Assume we pick a coin at random, toss it twice and get 𝑇 𝑇 .
Compute the posterior probability the coin has probability 0.25 of heads.
Concept questions
Concept question 1. Discrete or continuous?
Suppose 𝑋 ∼ Bernoulli(𝜃) where the value of 𝜃 is unknown. If we use Bayesian methods to
make probabilistic statements about 𝜃 then which one of the following is true?
1. The random variable is discrete, the space of hypotheses is discrete.
2. The random variable is discrete, the space of hypotheses is continuous.
3. The random variable is continuous, the space of hypotheses is discrete.
4. The random variable is continuous, the space of hypotheses is continuous.
Board questions
Problem 1. Total probability
(a) A coin has unknown probability of heads 𝜃 with prior pdf, for the value of 𝜃, 𝑓(𝜃) = 3𝜃2.
Find the probability of throwing tails on the first toss.
(b) Describe an experiment with success and failure that this models. Include the reason
for the prior in your description.
Problem 2. Bent coin 1
We have a ‘bent’ coin with an unknown probability 𝜃 of heads. Assume the following:
• Prior for the value of 𝜃: 𝑓(𝜃) = 2𝜃 on [0, 1].
• Data: toss once and get heads.
(a) Find the posterior pdf to this data.
(b) Suppose you toss again and get tails. Update your posterior from part (a) using this
data.
(c) On one set of axes graph the prior and the posteriors from parts (a) and (b).
1
18.05 class 13 problems, Spring 2022 2
Problem 2. Bent coin 2
Same scenario: bent coin ∼ Bernoulli(𝜃).
Flat prior: 𝑓(𝜃) = 1 on [0, 1]
Data: toss 27 times and get 15 heads and 12 tails.
Use this data to find the posterior pdf.
Write an integral formula for the normalizing factor (total probability of the data), but do
not compute it. Call its value 𝑇 and give the posterior pdf in terms of 𝑇 .
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
