# Mit18 05 S22 Pset02 Sol

---

18.05 Problem Set 2, Spring 2022 Solutions
Problem 1. (20: 10,10 pts.) (‘Binary’ paradox)
For this problem assume that puppies are equally probable to be male or female. Likewise
for kittens.
Be sure to carefully justify your answers.
(a) Our dog Layla had two puppies. The older puppy is female. What is the probability that
both puppies are female?
Solution: Listing the sex of older puppy first, our sample space is {𝑀𝑀, 𝑀𝐹 , 𝐹 𝑀, 𝐹 𝐹 } .
The event “the older puppy is female” is {𝐹 𝑀, 𝐹 𝐹 } and the event “both puppies are female”
is {𝐹 𝐹 } . Thus the probability that both puppies are females given the older is female is
𝑃(𝐹𝐹) 1/4 1
𝑃(𝐹𝐹|{𝐹𝑀, 𝐹𝐹}) = = = .
𝑃({𝐹𝑀, 𝐹𝐹}) 1/2 2
(b) Our cat Ariel had two kittens. At least one of them is male. What is the probability
that both kittens are males?
Solution: The event “at least one kitten is male” is {𝑀𝑀, 𝑀𝐹 , 𝐹 𝑀} so the probability
that both kittens are male is
𝑃(𝑀𝑀) 1/4 1
𝑃(𝑀𝑀|{𝑀𝑀, 𝑀𝐹, 𝐹𝑀}) = = = .
𝑃({𝑀𝑀, 𝑀𝐹, 𝐹𝑀}) 3/4 3
Problem 2. (15 pts.) (The blue taxi)
In a city with one hundred taxis, 1 is blue and 99 are green. A witness observes a hit-and-run
by a taxi at night and recalls that the taxi was blue, so the police arrest the blue taxi driver
who was on duty that night. The driver proclaims their innocence and hires you to defend
them in court. You hire a scientist to test the witness’ ability to distinguish blue and green
taxis under conditions similar to the night of accident. The data suggests that the witness
sees blue cars as blue 99% of the time and green cars as blue 2% of the time.
Write a speech for the jury to give them reasonable doubt about your client’s guilt. Your
speech need not be longer than the statement of this question. Keep in mind that most jurors
have not taken this course, so an illustrative table may be easier for them to understand
than fancy formulas.
Solution: The defense will try to make the case that this is likely to be a case of random
mis-identification. So we look for the probability a random taxi the witness sees as blue is
actually blue.
This is a question of ‘inverting’ conditional probability. We know
𝑃 (the witness sees blue|the car is blue)
but we’d like to know
𝑃 (the car is blue|the witness sees blue).
Our first job is to translate this to symbols.
1
18.05 Problem Set 2, Spring 2022 Solutions 2
Let 𝑊 = ‘witness sees a blue taxi’ and let 𝑊 = ‘witness sees a green car’. Further, let 𝑇
𝑏 𝑔 𝑏
= ‘taxi is blue’ and let 𝑇 = ‘taxi is green’. With this notation we want to find 𝑃 (𝑇 |𝑊 ).
𝑔 𝑏 𝑏
We will compute this using Bayes’ formula
𝑃 (𝑊 |𝑇 ) ⋅ 𝑃 (𝑇 )
𝑃 (𝑇 |𝑊 ) = 𝑏 𝑏 𝑏 .
𝑏 𝑏 𝑃 (𝑊 )
𝑏
All the pieces are represented in the following diagram.
0.01 0.99
Random taxi 𝑇 𝑇
𝐵 𝐺
0.99 0.01 0.02 0.98
Witness sees
𝑊 𝑊 𝑊 𝑊
𝐵 𝐺 𝐵 𝐺
We can determine each factor in the right side of Bayes’ formula:
We are given 𝑃 (𝑇 ) = 0.01 (so 𝑃 (𝑇 ) = 0.99).
𝑏 𝑔
We are given, 𝑃 (𝑊 |𝑇 ) = 0.99 and 𝑃(𝑊 |𝑇 ) = 0.02.
𝑏 𝑏 𝑏 𝑔
We compute 𝑃 (𝑊 ) using the law of total probability:
𝑏
𝑃(𝑊 ) = 𝑃(𝑊 |𝑇 )𝑃(𝑇 )+𝑃(𝑊 |𝑇 )𝑃(𝑇 ) = 0.99×0.01+0.02×0.99 = 0.99×0.03.
𝑏 𝑏 𝑏 𝑏 𝑏 𝑔 𝑔
Putting all this in Bayes’ formula we get
0.99 × 0.01 1
𝑃 (𝑇 |𝑊 ) = =
𝑏 𝑏 0.99 × 0.03 3
Our speech:
Ladies and gentlemen of the jury. The prosecutor tells you that the witness is nearly flawless
in their ability to distinguish whether a taxi is green or blue. They claims that this implies
that beyond a reasonable doubt the taxi involved in the hit and run was blue. However
probability theory shows without any doubt that a random taxi which the witness sees as
blue is actually blue only 1/3 of the time. This is considerably more than a reasonable
doubt. In fact it is more probable than not that the taxi involved in the accident was green.
If the probability doesn’t fit you must acquit!
Note: Confusing of 𝑃 (testimony|guilty) for 𝑃 (guilty|testimony) is known as the prosecutor’s
fallacy
Problem 3. (20 pts.) (Trees of cards) There are 8 cards in a hat:
{1♡, 1♠, 1♢, 1♣, 2♡, 2♠, 2♢, 2♣}
You draw one card at random. If its rank is 1 you draw one more card; if its rank is two
you draw two more cards. Let 𝑋 be the sum of the ranks on the 2 or 3 cards drawn. Find
𝐸[𝑋]. (Note: all the draws are done without replacement.)
Solution: The following tree shows all the possible ways we can draw cards. The first draw
is the top row of nodes. The value of the draw is given in the circle. The probability of
that draw is given along the edge. Likewise for the second and third draws. At the end of
each path we give the value of 𝑋 resulting from those draws.
18.05 Problem Set 2, Spring 2022 Solutions 3
4/8 4/8
1 2
3/7 4/7 4/7 3/7
1 2 1 2
𝑋 = 2 𝑋 = 3
3/6 3/6 4/6 2/6
1 2 1 2
𝑋 = 4 𝑋 = 5 𝑋 = 5 𝑋 = 6
This gives us the probability distribution of 𝑋:
value 𝑥 2 3 4 5 6
pmf 𝑝(𝑥) 3/14 2/7 1/7 2/7 1/14
So,
3 2 1 2 1 26
𝐸[𝑋] = 2⋅ +3 ⋅ +4 ⋅ +5 ⋅ +6 ⋅ = ≈ 3.7143.
14 7 7 7 14 7
Problem 4. (25: 5,10,5,5 pts.) (Dice) There are four dice in a drawer: one D4 (4 sides),
one D6 (6-sides), and two D8 (8 sides). As usual, the sides of a die are numbered 1 to 𝑛,
where 𝑛 is the number of sides.
Your friend secretly grabs one of the four dice at random. Let 𝑆 be the number of sides on
the chosen die.
(a) What is the pmf of S?
Solution: Here is the pmf:
value 𝑠 4 6 8
pmf 𝑝(𝑠) 1/4 1/4 1/2
(b) Now, without showing it to you, your friend rolls the chosen die and tells you the result.
Let 𝑅 be the result of the roll.
Use Bayes’ rule to find 𝑃(𝑆 = 𝑠|𝑅 = 3) for 𝑠 = 4,6,8. Which die is most likely if 𝑅 = 3?
Terminology: You are computing the pmf of ‘𝑆 given 𝑅 = 3’.
Solution: Bayes’ rule says
𝑃(𝑅 = 3|𝑆 = 𝑠)𝑃(𝑆 = 𝑠)
𝑃(𝑆 = 𝑠|𝑅 = 3) = .
𝑃(𝑅 = 3)
We summarize what we know in a tree. In the tree the notation 𝐷 means the 4-sided die
4
(𝑆 = 4), likewise 𝑅 means a 3 was rolled (𝑅 = 3). Because we only care about the case
3
𝑅 = 3 the tree does not include other possible rolls.
1/4 1/4 1/2
Chosen die 𝐷 𝐷 𝐷
4 6 8
1/4 1/6 1/8
Roll result
𝑅 𝑅 𝑅
3 3 3
18.05 Problem Set 2, Spring 2022 Solutions 4
We have the following probabilities (you should identify them in the tree):
𝑃(𝑅 = 3|𝑆 = 4) = 1/4, 𝑃(𝑅 = 3|𝑆 = 6) = 1/6, 𝑃(𝑅 = 3|𝑆 = 8) = 1/8.
The law of total probability gives (again, see how the tree tells us this):
𝑃(𝑅 = 3) = 𝑃(𝑅 = 3|𝑆 = 4)𝑃(𝑆 = 4)+𝑃(𝑅 = 3|𝑆 = 6)𝑃(𝑆 = 6)+𝑃(𝑅 = 3|𝑆 = 8)𝑃(𝑆 = 8)
1 1 1 1 1 1
= ⋅ + ⋅ + ⋅
4 4 6 4 8 2
1
= .
6
Hence,
𝑃(𝑅 = 3|𝑆 = 4)⋅𝑃(𝑆 = 4) (1/4)⋅(1/4) 3
𝑃(𝑆 = 4|𝑅 = 3) = = =
𝑃(𝑅 = 3) 1/6 8
𝑃(𝑅 = 3|𝑆 = 6)⋅𝑃(𝑆 = 6) (1/6)⋅(1/4) 1
𝑃(𝑆 = 6|𝑅 = 3) = = =
𝑃(𝑅 = 3) 1/6 4
𝑃(𝑅 = 3|𝑆 = 8)⋅𝑃(𝑆 = 8) (1/8)⋅(1/2) 3
𝑃(𝑆 = 8|𝑅 = 3) = = = .
𝑃(𝑅 = 3) 1/6 8
We see that the 4 and 8 sided dice are equally most likely given 𝑅 = 3.
(c) Which die is most likely if 𝑅 = 6? Hint: You can either repeat the computation in (b),
or you can reason based on your result in (b).
Solution: In a similar vein, we have
𝑃(𝑅 = 6|𝑆 = 4) = 0, 𝑃(𝑅 = 6|𝑆 = 6) = 1/6, 𝑃(𝑅 = 6|𝑆 = 8) = 1/8.
and
1 1 1 1 1 5
𝑃(𝑅 = 6) = 0⋅ + ⋅ + ⋅ = .
4 6 4 8 2 48
So,
1/24 2 1/16 3
𝑃(𝑆 = 4|𝑅 = 6) = 0, 𝑃(𝑆 = 6|𝑅 = 6) = = , 𝑃(𝑆 = 8|𝑅 = 6) = = .
5/48 5 5/48 5
The eight-sided die is more likely. Note, the denominator is the same in each probability,
i.e. the total probability 𝑃(𝑅 = 6), so all we really had to check was the numerator.
(d) Which die is most likely if 𝑅 = 7? No computations are needed!
Solution: The only way to get 𝑅 = 7 is if we picked an 8-sided die D8.
Problem 5. (10 pts.) (Seating arrangement and relative height) A total of 𝑛 people
randomly take their seats around a circular table with 𝑛 chairs. No two people have the same
height. What is the expected number of people who are shorter than both of their immediate
neighbors?
Solution: Label the seats 1 to 𝑛 going clockwise around the table. Let 𝑋 be the Bernoulli
𝑖
random variable with value 1 if the person in seat 𝑖 is shorter than their neighbors. Then
18.05 Problem Set 2, Spring 2022 Solutions 5
𝑛
𝑋 = ∑ 𝑋 represents the total number of people who are shorter than both of their
𝑖=1 𝑖
neighbors, and, by linearity of expected value,
𝑛 𝑛
𝐸[𝑋] = 𝐸[∑𝑋 ] = ∑𝐸[𝑋 ]
𝑖 𝑖
𝑖=1 𝑖=1
Recall that this property of expected values holds even when the 𝑋 are dependent, as is
𝑖
the case here!
Among 3 random people the probability that the middle one is the shortest is 1/3. Therefore
𝑋 ∼ Bernoulli(1/3), which implies 𝐸[𝑋 ] = 1/3. Therefore the expected number of people
𝑖 𝑖
shorter than both their neighbors is
𝑛 𝑛
𝐸[𝑋] = ∑𝐸[𝑋 ] = .
𝑖 3
𝑖=1
Problem 6. (20: 3,2,10,5 pts.)
In this problem we will use R to simulate flipping a fair coin 50 times. We’ll use the
simulation to explore ‘runs’. That is, sequences of all 1’s or 0’s.
(a) Make up a sequence of length 50 consisting of ones and zeros. Try to make the sequence
look like it was randomly generated by flipping a coin.
Solution: Any sequence of 50 zeros and ones is valid.
(b) A run is a sequence of all 1s or all 0s. How long is the longest run in your answer to
part (a)?
Solution: Answers will vary because we can’t know the sequence you chose. However,
most people, when trying to be random, do not put in any long runs. Parts (c) and (d)
show these actually happen frequently.
(c) Now we will use R to simulate 50 tosses of a fair coin and estimate the average length
of the longest run. The code below simulates one trial. You will need to use a ‘for loop’ to
run 10000 trials. On our MITx site you can find tutorials on both for loops and the rle()
function used in the code. (As usual, choose the Course info tab and click on the R code
link under course handouts).
Sample code illustrating the use of rle().
# R code to simulate 50 flips of a fair coin and find the longest run
# rle stands for `run length encoding'.
# rle(trial)$lengths is a vector of the lengths of all the different runs
# in trial.
nflips = 50
trial = rbinom(nflips, 1, 0.5) # Note: binomial(1, 0.5) = bernoulli(0.5)
max_run = max(rle(trial)$lengths)
Sample code illustrating ‘for loops’. (These may be useful in the code for this problem.)
# R code demonstrating `for' loops.
for (j in 1:5) {
print(j^2)
18.05 Problem Set 2, Spring 2022 Solutions 6
}
(Should produce: 1, 4, 9, 16, 25.)
sum = 0
for (j in 1:5) {
sum = sum + j
}
print(sum)
(Should produce: 15.)
Use R to simulate the average length of the longest run in 50 flips of a fair coin. Do this
three times with 10000 trials each time and report the three results.
Solution: Here is my code with comments
nflips = 50
ntrials = 10000
total = 0 # We'll keep a running total of all the trials' longest runs
for (j in 1:ntrials) {
# One trial consists of 50 flips
trial = rbinom(nflips, 1, 0.5) # binomial(1, 0.5) = bernoulli(0.5)
# rle() finds the lengths of all the runs in trials. We add the max to total
total = total + max(rle(trial)$lengths)
}
# The average maximum run is the total/ntrials
ave_max = total/ntrials
print(ave_max)
My three runs of this code produced ave_max = 5.9863, 5.9696, 5.9804
(d) A small modification of your code will let you estimate the probability of a run of 8 or
more in 50 flips. Do this three times with 10000 trials each time. Report the three results.
Solution: Instead of keeping a total we keep a count of the number of trials with a run of
8 or more
nflips = 50
ntrials = 10000
# We'll keep count of all the trials with a run of 8 or more
count = 0
for (j in 1:ntrials) {
trial = rbinom(nflips, 1, 0.5) # binomial(1, 0.5) = bernoulli(0.5)
count = count + (max(rle(trial)$lengths) >= 8)
}
# The probability of a run of 8 or more is count/ntrials
prob8 = count/ntrials
print(prob8)
My run of this code produced prob8 = 0.1596, 0.1637, 0.1632
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
