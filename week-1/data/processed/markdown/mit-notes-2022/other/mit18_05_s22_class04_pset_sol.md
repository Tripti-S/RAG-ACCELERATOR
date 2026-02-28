# Mit18 05 S22 Class04 Pset Sol

---

Class 4 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1.
Suppose 𝑋 a random variable with the CDF shown.
values of 𝑋: 1 3 5 7
cdf 𝐹 (𝑎): 0.5 0.75 0.9 1
What is 𝑃(𝑋 ≤ 3)?
(a) 0.15 (b) 0.25 (c) 0.5 (d) 0.75
Solution: (d) 0.75. 𝑃(𝑋 ≤ 3) = 𝐹(3) = 0.75.
What is 𝑃(𝑋 = 3)? Same distribution as above
(a) 0.15 (b) 0.25 (c) 0.5 (d) 0.75
Solution: (b) 𝑃(𝑋 = 3) = 𝐹(3)−𝐹(1) = 0.75−0.5 = 0.25.
Board questions
Problem 1. Computing expectation
Suppose 𝑋 is a random variable with the following pmf.
𝑋: 1 2 3
pmf: 1/4 1/2 1/4
Find 𝐸[𝑋] and 𝐸[1/𝑋].
Solution:
1 1 1
𝐸[𝑋] = 1⋅ +2 ⋅ +3 ⋅ = 2
4 2 2
1 1 1 1 1 7
𝐸[1/𝑋] = 1⋅ + ⋅ + ⋅ = .
4 2 2 3 4 12
Problem 2. Interpreting expectation
(a) Would you accept a gamble that offers a 10% chance to win $95 and a 90% chance of
losing $5?
(b) Would you pay $5 to participate in a lottery that offers a 10% percent chance to win
$100 and a 90% chance to win nothing?
Hint: find the expected value of your winnings in each case.
Solution: (a) Here is the table for this random variable.
Values: 95 -5
PMF: 0.1 0.9
So, the expected value is $95⋅0.1−$5 ⋅0.9 = $5
1
18.05 class 4 problems, Spring 2022 2
(b) Has the same table, e.g. if you pay $5 and win $100, your net gain is $95. So, it has
the same expected value. If you play enough times, you will average winning $5 for every
game played.
Discussion
Framing bias / cost versus loss. The two situations are identical, with an expected value
of gaining $5. In a study, 132 undergrads were given these questions (in different orders)
separated by a short filler problem. 55 gave different preferences to the two events. Of
these, 42 rejected (a) but accepted (b). One interpretation is that we are far more willing
to pay a cost up front than risk a loss. (See Judgment under uncertainty: heuristics and
biases by Tversky and Kahneman.)
Loss aversion and cost versus loss sustain the insurance industry: people pay more in
premiums than they get back in claims on average (otherwise the industry wouldn’t be sus-
tainable), but they buy insurance anyway to protect themselves against substantial losses.
Think of it as paying $1 each year to protect yourself against a 1 in 1000 chance of losing
$100 that year. By buying insurance, the expected value of the change in your assets in
one year (ignoring other income and spending) goes from negative 10 cents to negative 1
dollar. But whereas without insurance you might lose $100, with insurance you always lose
exactly $1.
Problem 3. Musical chairs or linearity of expectation
Suppose that there are 𝑛 people at your table and everyone got up, ran around the room,
and sat back down randomly (i.e., all seating arrangements are equally likely).
What is the expected value of the number of people sitting in their original seat?
Solution: Number the people from 1 to 𝑛. Let 𝑋 be the Bernoulli random variable with
𝑖
value 1 if person 𝑖 returns to their original seat and value 0 otherwise. Since person 𝑖 is
equally likely to sit back down in any of the 𝑛 seats, the probability that person 𝑖 returns
to their original seat is 1/𝑛. Therefore 𝑋 ∼ 𝐵𝑒𝑟𝑛𝑜𝑢𝑙𝑙𝑖(1/𝑛) and 𝐸[𝑋 ] = 1/𝑛.
𝑖 𝑖
Now, let 𝑋 be the number of people sitting in their original seat following the rearrangement.
Then
𝑋 = 𝑋 +𝑋 +⋯+𝑋 .
1 2 𝑛
By linearity of expected values, we have
𝑛 𝑛
𝐸[𝑋] = ∑𝐸[𝑋 ] = ∑1/𝑛 = 1.
𝑖
𝑖=1 𝑖=1
Extra discussion of derangements (Not required – for fun only.)
• It’s neat that the expected value is 1 for any 𝑛.
• If 𝑛 = 2, then both people either retain their seats or exchange seats. So 𝑃(𝑋 = 0) = 1/2
and 𝑃(𝑋 = 2) = 1/2. In this case, 𝑋 never equals 𝐸[𝑋].
• The 𝑋 are not independent (e.g. for 𝑛 = 2, 𝑋 = 1 implies 𝑋 = 1).
𝑖 1 2
• Expectation behaves linearly even when the variables are dependent.
Neat fact: A permutation of 𝑛 people in which nobody returns to their original seat is
called a derangement. The number of derangements turns out to be the nearest integer to
18.05 class 4 problems, Spring 2022 3
𝑛!/𝑒. Since there are 𝑛! total permutations, we have:
𝑛!/𝑒
𝑃 (everyone in a different seat) ≈ = 1/𝑒 ≈ 0.3679.
𝑛!
It’s surprising that the probability is about 37% regardless of 𝑛, and that it converges to
1/𝑒 as 𝑛 goes to infinity.
https://en.wikipedia.org/wiki/Derangement
Problem 4. Bernoulli
(a) Suppose 𝑋 ∼ Bernoulli(𝑝). Find 𝐸[𝑋].
(This is important! Remember it!)
(b) Suppose 𝑌 = 𝑋 +𝑋 +…+𝑋 , where each 𝑋 ∼ Bernoulli(0.25). Find 𝐸[𝑌 ].
1 2 12 𝑖
Solution: (a) Here’s the probability table for a Bernoulli random variable.
𝑋: 0 1
pmf: 1−𝑝 𝑝
So,
𝐸[𝑋] = (1−𝑝) ⋅0+𝑝 ⋅1 = 𝑝
(b) By the linearity of expectation
𝐸[𝑋] = 𝐸[𝑋 ]+𝐸[𝑋 ]+…𝐸[𝑋 ] = 12⋅(0.25) = 3
1 2 12
(Remember, if 𝑋 , … , 𝑋 are independent, we say 𝑋 ∼ Binomial(12, 0.25).)
1 12
In general, if 𝑋 ∼ Binomial(𝑛, 𝑝) then 𝐸[𝑋] = 𝑛𝑝.
Problem 5. Don’t let one failure stop you
Let 𝑋 = # of successes before the second failure of a sequence of independent Bernoulli(𝑝)
trials. Find the pmf of 𝑋.
Hint: this requires a small amount of counting.
Solution: 𝑋 takes values 0, 1, 2, …. We will show the pmf is 𝑝(𝑛) = (𝑛 + 1)𝑝𝑛(1 − 𝑝)2.
For concreteness, we’ll derive this formula for 𝑛 = 3. Let’s list the outcomes with three
successes before the second failure. If 𝑛 = 3, then we had 3 successes and 2 failures and the
fifth trial was a failure. So each such outcome must have the form
__ __ __ __ 𝐹
with three 𝑆 and one 𝐹 in the first four slots. So we just have to choose which of these four
slots contains the 𝐹 . We can list all the possibilities
{𝐹 𝑆𝑆𝑆𝐹 , 𝑆𝐹 𝑆𝑆𝐹 , 𝑆𝑆𝐹 𝑆𝐹 , 𝑆𝑆𝑆𝐹 𝐹 }
In other words, there are (4) = 4 such outcomes. Each of these outcomes has three 𝑆 and
1
two 𝐹 , so each outcome has probability 𝑝3(1 − 𝑝)2. The probability that 𝑛 = 3 is therefore
𝑝(3) = 𝑃 (𝑋 = 3) = 4𝑝3(1 − 𝑝)2.
The same reasoning works for general 𝑛:
𝑛 + 1
𝑝(𝑛) = ( )𝑝𝑛(1 − 𝑝)2 = (𝑛 + 1)𝑝𝑛(1 − 𝑝)2.
1
18.05 class 4 problems, Spring 2022 4
In class examples and discussion
Gambler’s fallacy. [roulette]
Fallacy: If black comes up several times in a row then the next spin is more likely to be
red.
Truth: P(red) remains the same. The roulette wheel spins are independent.
Discussion: “On August 18, 1913, at the casino in Monte Carlo, black came up a record
twenty-six times in succession [in roulette]. [There] was a near-panicky rush to bet on red,
beginning about the time black had come up a phenomenal fifteen times. In application
of the maturity [of the chances] doctrine, players doubled and tripled their stakes, this
doctrine leading them to believe after black came up the twentieth time that there was not
a chance in a million of another repeat. In the end the unusual run enriched the Casino by
some millions of francs.” (I’ve lost the source for this. Wikipedia has a good article on the
Gambler’s Fallacy.)
Hot hand
Theory: NBA players get ‘hot’.
Data: The data show that player who has made 5 shots in a row is no more likely than
usual to make the next shot.
Discussion: See The Hot Hand in Basketball: On the Misperception of Random Sequences
by Gilovish, Vallone and Tversky. (A link that worked when these slides were written is
https://doi.org/10.1016/0010-0285(85)90010-6)
There is still some controversy about this. Some statisticians feel that the authors of the
above paper erred in their analysis of the data and the data do support the notion of a hot
hand in basketball.
Discussion: This reverses the Gambler’s Fallacy, but is less obviously false, since we cannot
model player psychology as well as we can model the Roulette wheel. The paper by Gilovish
et al uses NBA and college game data to conclude that the hot hand is hot air.
Extra problems
Extra 1. Suppose 𝑋 ∼ Binomial(𝑛, 𝑝), i.e. the number of successes in 𝑛, independent
Bernoulli(𝑝) trials. Explain why 𝑋 is the sum of 𝑛 Bernoulli(𝑝) random variables.
Solution: Let 𝑋 , 𝑋 , … , 𝑋 be the 𝑛 Bernoulli trials. 𝑋 is 1 if it’s a success and 0 if it’s
1 2 𝑛 𝑖
a failure. If there are 𝑘 successes, then 𝑘 of the 𝑋 are 1 and 𝑛 − 𝑘 are 0. If you sum, 𝑘
𝑖
ones and 𝑛 − 𝑘 zeros you get 𝑘. That is, the sum of the 𝑛 Bernoulli variables is the number
of successes. In symbols
𝑛
∑ 𝑋 = number of successes = 𝑋.
𝑖
𝑖=1
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
