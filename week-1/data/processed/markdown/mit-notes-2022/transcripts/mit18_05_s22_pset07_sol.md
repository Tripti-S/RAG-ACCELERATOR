# Mit18 05 S22 Pset07 Sol

---

18.05 Problem Set 7, Spring 2022 Solutions
Problem 1. (30: 10,10,10 pts.) (Monty Hall: Sober and drunk)
Recall the Monty Hall problem: Monty hosts a game show. There are three doors: one hides
a car and two hide goats. The contestant Shelby picks a door, which is not opened. Monty
then opens another door which has a goat behind it. Finally, Shelby must decide whether to
stay with her original choice or switch to the other unopened door. The problem asks which
is the better strategy: staying or switching?
To be precise, let’s label the door that Shelby picks by 𝐴, and the other two doors by 𝐵 and
𝐶. Hypothesis 𝐻 is that the car is behind door 𝐴, and similarly for hypotheses 𝐻 and
𝐴 𝐵
𝐻 .
𝐶
(a) In the usual formulation, Monty is sober and knows the locations of the car and goats.
So if the contestant picks a door with a goat, Monty always opens the other door with a
goat. And if the contestant picks the door with a car, Monty opens one of the other two
doors at random. Suppose that sober Monty Hall opens door 𝐵, revealing a goat. So the
data is: ‘Monty showed a goat behind 𝐵’. Our hypotheses are ‘the car is behind door A’,
etc. Make a Bayes table with prior, likelihood and posterior. Use the posterior probabilities
to determine the best strategy.
Solution: In all three parts to this problem we have 3 hypotheses:
𝐻 = ‘the car is behind door 𝐴’
𝐴
𝐻 = ‘the car is behind door 𝐵’
𝐵
𝐻 = ‘the car is behind door 𝐶’.
𝐶
In all three parts the data is 𝐷 = ‘Monty opens door 𝐵 and reveals a goat’.
The key to our Bayesian update table is the likelihoods: For part (a), since Monty is sober
he always reveals a goat.
𝑃 (𝐷|𝐻 ): 𝐻 says the car is behind 𝐴. So, assuming 𝐻 is true, Monty is equally likely
𝐴 𝐴 𝐴
to pick 𝐵 or 𝐶 and reveal a goat. Thus 𝑃 (𝐷|𝐻 ) = 1/2.
𝐴
𝑃 (𝐷|𝐻 ): If 𝐻 is true, the car is behind 𝐵 and sober Monty will never choose 𝐵 (and if
𝐵 𝐵
he did it would not reveal a goat). So 𝑃 (𝐷|𝐻 ) = 0.
𝐵
𝑃 (𝐷|𝐻 ): If 𝐻 is true, the car is behind 𝐶. Since sober Monty doesn’t make mistakes he
𝐶 𝑐
will open door 𝐵 and reveal a goat. So 𝑃(𝐷|𝐻 ) = 1.
𝐶
Here is the table for this situation.
Hyp. Prior Likelihood Bayes numerator Posterior
𝐻 𝑃 (𝐻) 𝑃 (data|𝐻) 𝑃 (𝐻)𝑃 (data|𝐻) 𝑃 (𝐻|data)
𝐻 1/3 1/2 1/6 1/3
𝐴
𝐻 1/3 0 0 0
𝐵
𝐻 1/3 1 1/3 2/3
𝐶
Total: 1 – 1/2 1
Therefore, Shelby should switch to door 𝐶, since the posterior probability 𝐻 is true is
𝐶
twice that of 𝐻 .
𝐴
(b) Now suppose that Monty is drunk, i.e. he has completely forgotten where the car is and
is only aware enough to randomly open one of the two doors not chosen by the contestant.
It’s entirely possible he might accidentally reveal the car, ruining the show.
1
18.05 Problem Set 7, Spring 2022 Solutions 2
Suppose that drunk Monty Hall opens door 𝐵, revealing a goat. Make a Bayes table with
prior, likelihood and posterior. Use the posterior probabilities to determine the best strategy.
(Hint: the data is the same but the likelihood function is not.)
Solution: Some of the likelihoods change in this setting.
𝑃 (𝐷|𝐻 ): If 𝐻 is true, then the car is behind 𝐴. So Monty is equally likely to show 𝐵
𝐴 𝐴
or 𝐶 and reveal a goat. Thus 𝑃 (𝐷|𝐻 ) = 1/2. (Remember, 𝐷 is the event ’Monty opens
𝐴
door 𝐵 and reveals a goat’.)
𝑃 (𝐷|𝐻 ): If 𝐻 is true, then the car is behind 𝐵, drunk Monty might show 𝐵, but if he
𝐵 𝐵
does we won’t reveal a goat. (He will ruin the game.) So 𝑃 (𝐷|𝐻 ) = 0.
𝐵
𝑃 (𝐷|𝐻 ): 𝐻 says the car is behind 𝐶. Drunk Monty is equally likely to show 𝐵 or 𝐶. If
𝐶 𝑐
he chooses 𝐵 he’ll reveal a goat. So 𝑃(𝐷|𝐻 ) = 1/2.
𝐶
Our table is now:
Hyp. Prior Likelihood Bayes numerator Posterior
𝐻 𝑃 (𝐻) 𝑃 (data|𝐻) 𝑃 (𝐻)𝑃 (data|𝐻) 𝑃 (𝐻|data)
𝐻 1/3 1/2 1/6 1/2
𝐴
𝐻 1/3 0 0 0
𝐵
𝐻 1/3 1/2 1/6 1/2
𝐶
Total: 1 – 1/3 1
So, in this case, switching is just as good (or as bad) as staying with the original choice.
The main lesson here is that, in the Bayesian framework, probability represents the uncer-
tainty of our knowledge. Sober Monty gave us information about the door he opened (it
hid a goat). But, since he would avoid the other door if the car was behind it, not picking
the other door gives us additional information. Since drunk Monty was choosing a door at
random, he gave us information about the door he opened, but, since he wasn’t avoiding the
other door, there was no information in the fact that he didn’t choose it. (Imagine there are
100 doors. If you choose 1 and sober Monty opens 98 with goats, then the door he avoided
almost certainly hides a car. On the other hand, drunk Monty is virtually guaranteed to
spoil the show if he randomly opens 98 doors.)
(c) Based on Monty’s pre-show behavior, Shelby thinks that Monty is sober with probability
0.7 and drunk with probability 0.3. Repeat the analysis from parts (a) and (b) in this
situation.
Solution: We have to recompute the likelihoods. Remember the data is that Monty chooses
door 𝐵 and reveals a goat.
𝑃 (𝐷|𝐻 ): If the car is behind 𝐴 then sober or drunk Monty is equally likely to choose door
𝐴
𝐵 and reveal a goat. Thus 𝑃 (𝐷|𝐻 ) = 1/2.
𝐴
𝑃 (𝐷|𝐻 ): If the car is behind door 𝐵, then if he chooses it he will reveal a car, not a goat.
𝐵
So the probability of the data given 𝐻 is 0, i.e., 𝑃 (𝐷|𝐻 ) = 0.
𝐵 𝐵
𝑃 (𝐷|𝐻 ): Let 𝑆 be the event that Monty is sober and 𝑆𝑐 the event he is drunk. From
𝐶
the table in (a), we see that 𝑃(𝐷|𝐻 ,𝑆) = 1 and from the table in (b), we see that
𝐶
𝑃(𝐷|𝐻 ,𝑆𝑐) = 1/2. Thus, by the law of total probability
𝐶
1 17
𝑃(𝐷|𝐻 ) = 𝑃(𝐷|𝐻 ,𝑆)𝑃(𝑆)+𝑃(𝐷|𝐻 ,𝑆𝑐)𝑃(𝑆𝑐) = 0.7+ (0.3) = 0.85 = .
𝐶 𝐶 𝐶 2 20
18.05 Problem Set 7, Spring 2022 Solutions 3
Hyp. Prior Likelihood Bayes numerator Posterior
𝐻 𝑃 (𝐻) 𝑃 (data|𝐻) 𝑃 (𝐻)𝑃 (data|𝐻) 𝑃 (𝐻|data)
𝐻 1/3 1/2 1/6 10/27
𝐴
𝐻 1/3 0 0 0
𝐵
𝐻 1/3 17/20 17/60 17/27
𝐶
Total: 1 – 9/20 1
Thus, switching gives a probability of 17/27 of winning. So switching is still the best strategy.
The intuitive feel for this is that even a little bit sober, Monty is giving some information
by picking 𝐵, or, more precisely, avoiding 𝐶.
Problem 2. (40: 10,10,10,5,5 pts.) Prediction
We are going to explore the dice problem from class further. I have five dice (4, 6, 8, 12, or
20 sides) and pick one at random (uniform probability). I then roll this die 𝑛 times and tell
you that, miraculously, every roll resulted in the value 7. As I am in a position of authority,
assume that I am telling the truth!
(a) First, consider just the first roll. Find the prior predictive probability that the first roll
will be a 7 and the posterior (after the first roll) predictive probability that the second roll
will be a 7. Also find the posterior (after the first roll) probabilities for the chosen die.
Solution: We start by making a Bayesian update table. Let 𝐷 , 𝐷 , 𝐷 , 𝐷 , and 𝐷 are
4 6 8 12 20
the hypotheses that we have selected the 4, 6, 8, 12, or 20 sided die respectively.
Hyp. Prior Likelihood Bayes numerator Posterior
𝐻 𝑃 (𝐻) 𝑃 (data|𝐻) 𝑃 (𝐻)𝑃 (data|𝐻) 𝑃 (𝐻|data)
𝐷 1/5 0 0 0
4
𝐷 1/5 0 0 0
6
𝐷 1/5 1/8 1 1 ≈ 0.4839
8 40 40𝑇
𝐷 1/5 1/12 1 1 ≈ 0.3226
12 60 60𝑇
𝐷 1/5 1/20 1 1 ≈ 0.1935
20 100 100𝑇
Total: 1 – 𝑇 = 31 ≈ 0.0517 1
600
Let 𝑅 be the event ‘the first roll is a 7’. The prior predictive probability 𝑃(𝑅 ) = 𝑇 ≈
1 1
0.0157, i.e. the total probability in the Bayes numerator column of the table.
The posterior probabilities 𝑃 (𝐷 |𝑅 ), 𝑃 (𝐷 |𝑅 ), 𝑃 (𝐷 |𝑅 ), 𝑃 (𝐷 |𝑅 ), 𝑃 (𝐷 |𝑅 ) are
4 1 6 1 8 1 12 1 20 1
given in the last column of the above table.
Let 𝑅 be the event ‘the second roll is a 7’. The posterior predictive probability 𝑃 (𝑅 |𝑅 )
2 2 1
is also computed using the law of total probability, where we must use the posterier prob-
abilities for each of the dice.
𝑃 (𝑅 |𝑅 ) = 𝑃 (𝑅 |𝐷 )𝑃 (𝐷 |𝑅 ) + 𝑃 (𝑅 |𝐷 )𝑃 (𝐷 |𝑅 ) + 𝑃 (𝑅 |𝐷 )𝑃 (𝐷 |𝑅 )
2 1 2 4 4 1 2 6 6 1 2 8 8 1
+ 𝑃 (𝑅 |𝐷 )𝑃 (𝐷 |𝑅 ) + 𝑃 (𝑅 |𝐷 )𝑃 (𝐷 |𝑅 )
2 12 12 1 2 20 20 1
1 1 1
≈ 0 ⋅0+0 ⋅0+ ⋅0.4839+ ⋅0.3226+ ⋅0.1935
8 12 20
≈ 0.0970
(b) Find the posterior probability 𝑃 (𝐻|data) for each die given the data of all 𝑛 rolls (your
18.05 Problem Set 7, Spring 2022 Solutions 4
answers should involve 𝑛). What is the limit of each of these probabilities as 𝑛 grows to
infinity? Explain why this makes sense.
Solution: We make the Bayesian update table. This is similar to the table in part (a).
The main difference is that the likelihood column needs to account for all 𝑛 rolls.
Hyp. Prior Likelihood Bayes numer. Posterior
𝐻 𝑃 (𝐻) 𝑃 (data|𝐻) 𝑃 (𝐻)𝑃 (data|𝐻) 𝑃 (𝐻|data)
𝐷 1/5 0 0 0
4
𝐷 1/5 0 0 0
6
𝐷 1/5 (1/8)𝑛 1 ⋅ (1/8)𝑛 1 (1/8)𝑛
8 5 5𝑇
𝐷 1/5 (1/12)𝑛 1 ⋅ (1/12)𝑛 1 (1/12)𝑛
12 5 5𝑇
𝐷 1/5 (1/20)𝑛 1 ⋅ (1/20)𝑛 1 (1/20)𝑛
20 5 5𝑇
Total: 1 – 𝑇 = 1 ⋅ ((1/8)𝑛 + (1/12)𝑛 + (1/20)𝑛) 1
5
The posterior probabilities are given in the table. To find what happens as 𝑛 grows large,
we rewrite the posterior probabilities by multiplying numerator and denominator by 8𝑛:
1
𝑃 (𝐷 |data) =
8 1+(2) 𝑛 +(2 ) 𝑛
3 5
(2)
𝑛
𝑃 (𝐷 |data) = 3
12 1+(2) 𝑛 +(2 ) 𝑛
3 5
(2)
𝑛
𝑃 (𝐷 |data) = 5
20 1+(2) 𝑛 +(2 ) 𝑛
3 5
As 𝑛 → ∞, we know that (2)
𝑛
→ 0 and (2)
𝑛
→ 0. Thus, as 𝑛 grows to infinity, 𝑃 (𝐷 |data)
3 5 8
approaches 1 and the posterior probability of all the other hypotheses goes to 0.
This makes sense because, as unlikely as it is, rolling 𝑛 sevens is vastly more probable with
the 8-sided die is vastly than with the bigger ones.
(c) Given that my first 10 rolls resulted in 7 (i.e., 𝑛 = 10), rank the possible values for my
next roll from most likely to least likely. Note any ties in rank and explain your reasoning
carefully. You need not do any computations to solve this problem.
Solution: Having observed 𝑛 7’s already, we know that we could not have selected the
4-sided or the 6-sided die. We have three different groups of numbers: we can roll 1 to 8
with all three remaining dice; 9 to 12 with the 12 and 20-sided dice; and 13 to 20 with only
the 20-sided die. Thus, rolling 1 to 8 are all equally likely, likewise 9 to 12 and 13 to 20.
Since we can get 1 to 8 from all three dice each of these values is in the most likely group.
The next most likely values are 9 to 12 which can happen on two dice. Least likely values
are 13 to 20.
(d) Let 𝑥 is the result of the 𝑖th roll.
𝑖
Find the posterior predictive pmf for the (𝑛 + 1)st roll given the data. That is, find
𝑃 (𝑥 |𝑥 = 7, ⋯ , 𝑥 = 7) for 𝑥 = 1,…,20. (Hint: use part (b) and the law of to-
𝑛+1 1 𝑛 𝑛+1
tal probability. Many values of the pmf coincide, so you do not need to do 20 separate
computations. You should check that your answer is consistent with your ranking in part
(c) for 𝑛 = 10).
18.05 Problem Set 7, Spring 2022 Solutions 5
Solution: Let 𝑇 be the total probability in the table from part (b). By the law of total
probability, for 𝑥 = 1,2,…,8, we have
𝑛+1
1 1 𝑛 1 1 1 𝑛 1 1 1 𝑛 1
𝑃 (𝑥 |data) = ⋅( ) ⋅ + ⋅( ) ⋅ + ⋅( ) ⋅ .
𝑛+1 5𝑇 8 8 5𝑇 12 12 5𝑇 20 20
For 𝑥 = 9, 10, 11, 12, we have
𝑛+1
1 1 𝑛 1 1 1 𝑛 1
𝑃 (𝑥 |data) = ⋅( ) ⋅ + ⋅( ) ⋅ .
𝑛+1 5𝑇 12 12 5𝑇 20 20
Finally, for 𝑥 = 13, 14, … , 20, we have
𝑛+1
1 1 𝑛 1
𝑃 (𝑥 |data) = ⋅( ) ⋅ .
𝑛+1 5𝑇 20 20
(e) What function does the pmf in part (d) converge to as 𝑛 grows to infinity? Explain why
this makes sense.
Solution: As 𝑛 → ∞, we see that 𝑃 (𝐷 = 𝑥|data = all sevens) → 1/8 for 𝑥 = 1,2,…,8,
𝑛+1
and 0 for 9 ≤ 𝑥 ≤ 20. This makes sense because, in the limit, all sevens makes the
probability the die is 8-sided equal to 1.
Problem 3. (30: 10,10,5,5 pts.) (Odds)
You have a drawer that contains 50 coins. 10 coins have probability 𝑝 = 0.3 of heads, 30
coins have probability 𝑝 = 0.5 and 10 coins have probability 𝑝 = 0.7. You pick one coin at
random from the drawer and flip it.
(a) What are the (prior) odds you chose a 0.3 coin? A 0.7 coin?
Solution: Odds of 𝐴 are 𝑃 (𝐴)/𝑃 (𝐴𝑐). So both types of coin have odds 0.2/0.8 = 1/4.
(b) What are the (prior predictive) odds of flipping a heads?
Solution: To answer parts b-d we make a likelihood table and a Bayesian update table. We
label our hypothesis 𝐶 , 𝐶 and 𝐶 meaning that the chosen coin has that probability
0.3 0.5 0.7
of heads. Our data from the first flip, 𝐷 , is the event ‘heads on the first flip’.
1
Likelihood table
Hypothesis outcomes
Type of coin Heads Tails
𝐶 0.3 0.7
0.3
𝐶 0.5 0.5
0.5
𝐶 0.7 0.3
0.7
Bayesian update table
Hypoth. Prior likelihood Bayes numer. posterior
𝐻 𝑃 (𝐻) 𝑃 (𝐷 |𝐻) 𝑃 (𝐻)𝑃 (𝐷 |𝐻) 𝑃 (𝐻|𝐷 )
1 1 1
𝐶 0.2 0.3 0.06 0.12
0.3
𝐶 0.6 0.5 0.30 0.60
0.5
𝐶 0.2 0.7 0.14 0.28
0.7
Total: 1 – 0.50 1
The prior probability of heads is the total in the Bayes numerator column: 𝑃 (heads) = 0.50
18.05 Problem Set 7, Spring 2022 Solutions 6
So the prior probability of tails is 1 − 𝑃(heads) = 0.50
So the prior odds of heads are 𝑂(heads) = 1, i.e. 50-50 odds.
(c) Suppose the flip lands heads.
(i) What are the posterior odds the coin is a 0.3 coin?
(ii) What are the posterior odds the coin is a 0.7 coin?
Solution: (i) From the table we see the posterior probability the coin is the 0.3 coin is 0.12
0.12 12
so the posterior odds are = = 0.136 .
0.88 88
0.28 28
(ii) Likewise the posterior odds it’s the 0.7 coin are = = 0.389 .
0.72 72
(d) What are the posterior predictive odds of heads on the next (second) flip?
Solution: The posterior predictive probability of heads is found by summing the product
of the posterior column in the Bayesian update table and the heads column in the likelihood
table. We get 𝑃 (heads|𝐷 ) = 0.12 ⋅ 0.3 + 0.60 ⋅ 0.5 + 0.28 ⋅ 0.7 = 0.532.
1
The posterior predictive probability of tails 𝑃 (tails|𝐷 ) = 1−0.532 = 0.468. So the posterior
1
0.532
predictive odds of heads are 𝑂(heads|𝐷 ) = = 1.1368 .
1 0.468
Problem 4. (20: 10,10 pts.) (Courtroom fallacies)
(a) Mrs S is found stabbed in her family garden. Mr S behaves strangely after her death
and is considered as a suspect. On investigation of police and social records it is found that
Mr S had beaten up his wife on at least nine previous occasions. The prosecution advances
this data as evidence in favor of the hypothesis that Mr S is guilty of the murder. ‘Ah no,’
says Mr S’s highly paid lawyer, ‘statistically, only one in a thousand wife-beaters actually
goes on to murder his wife. So the wife-beating is not strong evidence at all. In fact, given
the wife beating evidence alone, it’s extremely unlikely that he would be the murderer of his
wife – only a 1/1000 chance. You should therefore find him innocent.’
Is the lawyer right to imply that the history of wife-beating does not point to Mr S’s being
the murderer? Or is this a legal trick? If the latter, what is wrong with his argument?
Use the following scaffolding to reason precisely:
Hypothesis: M = ‘Mr S murdered Mrs S’
Data: K = ‘Mrs S was killed’, B = ‘Mr S had a history of beating Mrs S’
How is the above probability 1/1000 expressed in these terms? How is the (posterior)
probability of guilt expressed in these terms? How are these two probabilities related? Hint:
Bayes’ theorem, conditioning on 𝐵 throughout.
Solution: This problem is taken from [Mackay, Information Theory, Inference, and Learn-
ing Algorithms].
The lawyer may correctly state that 𝑃(𝑀|𝐵) = 1/1000, but the lawyer then conflates this
with the probability of guilt given all the relevant data, which is really 𝑃 (𝑀|𝐵, 𝐾). The
short counterargument is that while only one in a thousand abused wives are murdered, the
vast majority of those that are murdered, are killed by their abusers.
One way to format the solution is with a Bayes table. Alternatively we could use Bayes’
18.05 Problem Set 7, Spring 2022 Solutions 7
theorem written out long hand. Of course, they are equivalent.
Let’s condition throughout on the a priori known fact 𝐵 that Mr S beat Mrs S. A priori,
that is before Mrs S was murdered, there are three hypotheses. They are
𝑀: Mr S will murder Mrs S
𝐸: Someone else will murder Mrs S
𝐴: Mrs S will not be murdered.
(It’s important to specify all three so the prior probabilities sum to 1.)
We’ll take the lawyer’s value of 𝑃(𝑀|𝐵) = 1/1000. Our Bayes update table is then
Hyp. prior likelihood Bayes numer. posterior
𝐻 𝑃 (𝐻|𝐵) 𝑃 (𝐾|𝐻, 𝐵) 𝑃 (𝐻|𝐾, 𝐵)
0.001
𝑀 1/1000 1 0.001
𝑝 + 0.001
𝑝
𝐸 𝑝 1 p
𝑝 + 0.001
𝐴 𝑞 0 0 0
Total: 1 – 𝑝 + 0.001 1
Here we have used 𝑃(𝐾|𝑀,𝐵) = 1, i.e. given she was murdered by her husband the
probability she was killed is 1. Likewise 𝑃(𝐾|𝐸,𝐵) = 1 and 𝑃(𝐾|𝐴,𝐵) = 0.
We now see that the posterior odds that Mr S is the murderer are
0.001
𝑂(𝑀|𝐾,𝐵) = .
𝑝
Thus, the odds depend on the value of 𝑝. Now, in most countries, 𝑃 (𝑀|𝐵) is much greater
than 𝑝 = 𝑃(𝐸|𝐵), which tells us the odds overwhelmingly favor the hypothesis that Mr S
is the murderer.
In fact, let’s make one more assumption: 𝑝 = 𝑃(𝐸|𝐵) = 𝑃(𝐸), i.e. that Mrs S being
murdered by someone else is independent of the fact that her husband beat her. (We
should acknowledge that this assumption might not be warranted without further study.)
Now, our formula for the odds that Mr S is the murderer is
𝑃 (𝑀|𝐵)
𝑂(𝑀|𝐾,𝐵) =
𝑃 (𝐸)
Let’s accept the lawyer’s statistic that 𝑃(𝑀|𝐵) = 1/1000. A quick Wikipedia search gives
that the murder rate in the US in 2020 was about 6.5/100000.* A further google search
shows that the murder rate of women in the US in 2010 was about 1/100000** If Mr and
Mrs S lived in the US that would put the odds at greater than 100 to 1 that he is the
murderer. I would say the lawyer’s argument is not credible.
*The murder rate seems to be a hard statistic to pin down. Different sources give slightly different
rates. Other countries have much lower murder rates. In 2017*, the worldwide average was about
6.1/100000. The highest murder rates by country in 2021* was about 1/2000. This data was taken
from the following Wikipedia article
https://en.wikipedia.org/w/index.php?title=List_of_countries_by_intentional_homicide_
rate&oldid=1143421050
**https://en.wikipedia.org/w/index.php?title=Homicide_statistics_by_gender&oldid=1139890572
18.05 Problem Set 7, Spring 2022 Solutions 8
(b) [True story] In 1999 in Great Britain, Sally Clark was convicted of murdering her two
sons after each child died weeks after birth (the first in 1996, the second in 1998). Her
conviction was largely based on the testimony of the pediatrician Professor Sir Roy Meadow.
He claimed that, for an affluent non-smoking family like the Clarks, the probability of a
single cot death (SIDS) was 1 in 8543, so the probability of two cot deaths in the same
family was around “1 in 73 million.” Given that there are around 700,000 live births in
Britain each year, Meadow argued that a double cot death would be expected to occur once
every hundred years. Finally, he reasoned that given this vanishingly small rate, the far
more likely scenario is that Sally Clark murdered her children.
Carefully explain at least two errors in Meadow’s argument.
Solution: Here are four errors in the argument
1. The prosecutor arrived at “1 in 73 million” as follows: The probability that 1 child
from an affluent non-smoking family dies of SIDS is 1/8543, so the probability that
2 children die is (1/8543)2. However, this assumes that the SIDS death among sib-
lings are independent. Due to genetic or environmental factors, we suspect that this
assumption is invalid.
2. The use of the figure “700,000 live births in Britain each year.” The prosecutor had
restricted attention only to affluent non-smoking families when (erroneously) comput-
ing the probability of two SIDS deaths. However, he does not similarly restrict his
attention when considering the number of births.
3. The rate “once every hundred years” is not valid: The prosecutor arrived at this by
multiplying the number of live births by the probability that two children die from
SIDS. The result is a non-sensical rate.
4. While double SIDS is very unlikely, double infanticide may be even more unlikely. It
is the odds of one explanation relative to the other given the deaths that matters, and
not just how unlikely one possibility is.
The Sally Clark case is an example of the “Prosecutor’s Fallacy.” You can read about it at
https://en.wikipedia.org/w/index.php?title=Sally_Clark&oldid=629645024
There is also a video that discusses legal fallacies at
https://www.ted.com/talks/peter_donnelly_shows_how_stats_fool_juries
Problem 5. (15 pts.) (Bayes at the movies)
A local theater employs two ticket collectors, Oscar and Emmy, although only one of them
works on any given day. The number of tickets 𝑋 that a ticket collector can collect in an
hour is modeled by a distribution which has mean 𝜆, and probability mass function
𝜆𝑘
𝑃 (𝑋 = 𝑘) = 𝑒−𝜆
𝑘!
for 𝑘 = 0,1,2,…. (This distribution is called a Poisson distribution. It is an important
discrete distribution in biology and physics.)
Suppose that Oscar collects, on average, 10 tickets an hour and Emmy collects, on average,
15 tickets an hour. One day the manager stays home sick. They know Emmy is supposed
18.05 Problem Set 7, Spring 2022 Solutions 9
to work that day, but thinks there are 1 to 10 odds that Oscar is filling in for Emmy (based
on Emmy’s prior history of taking advantage of Oscar’s generous nature when the manager
is away). The suspicious manager monitors ticket sales online and observes that over the
span of 5 hours there are 12, 10, 11, 4, and 11 tickets collected. What are the manager’s
posterior odds that Oscar is filling in for Emmy?
Solution: Since we are computing odds, we will only give the hypothesis and likelihood
columns of the update table. Our hypotheses are Oscar, i.e. Oscar is working and Emmy,
i.e. Emmy is working. Denoting our data as 𝐷, we have the table
likelihood
hypothesis 𝑃 (𝐷|hypothesis)
1012+10+11+4+11𝑒−50
Oscar 𝑃 (𝐷|Oscar) =
12!10!11!4!11!
1512+10+11+4+11𝑒−75
Emmy 𝑃 (𝐷|Emmy) =
12!10!11!4!11!
𝑃 (𝐷|Oscar)
Thus the Bayes factor (likelihood ratio) is ≈ 254.09.
𝑃 (𝐷|E mmy)
We are given the prior odds that Oscar is working, 𝑂(Oscar) = 1 . Thus, our posterior
10
odds are
𝑂(Oscar|𝐷) = prior odds × Bayes factor ≈ 25.409
Problem 6. (30: 10,10,10 pts.) (Normal is the new normal)
Your friend transmits an unknown value 𝜃 to you over a noisy channel. The noise is
normally distributed with mean 0 and a known variance 4, so the value 𝑥 that you receive is
modeled by 𝑥 ∼ 𝑁(𝜃,22). Based on previous communications, your prior on 𝜃 is 𝑁(6, 32).
(a) Suppose your friend transmits a value to you that you receive as 𝑥 = 5. Use the formulas
for normal-normal updating (given in the reading), to find the posterior pdf for 𝜃.
Solution: For the normal-normal updating formulas given in the reading we have
𝑛 = 1 (number of data values) , 𝑥 = 𝑥 = 5, 𝜇 = 6, 𝜎2 = 9, 𝜎2 = 4
prior prior
So, using the normal-normal update formulas:
1 1 𝑛 1 𝑎𝜇 + 𝑏𝑥 69 1 36
𝑎 = = , 𝑏 = = , ⇒ 𝜇 = prior = , 𝜎2 = = .
𝜎2 9 𝜎2 4 post 𝑎+𝑏 13 post 𝑎+𝑏 13
prior
Thus, the posterior 𝑓(𝜃 |𝑥) ∼ 𝑁(69 , 36) ≈ 𝑁(5.31, 1.662).
13 13
(b) Suppose your friend transmits the same value 𝜃 to you 8 times. You receive these signals
plus noise as 𝑥 , … , 𝑥 with sample mean 𝑥̄ = 5. Using the same prior and know variance
1 8
𝜎2 as in part (a), show that the posterior on 𝜃 is 𝑁(5.05, 0.47). Plot the prior and posterior
on the same graph. Describe how the data changes your belief about the true value of 𝜃.
Solution: We have
𝑛 = 8, 𝑥 = 𝑥 = 5, 𝜇 = 6, 𝜎2 = 9, 𝜎2 = 4
prior prior
18.05 Problem Set 7, Spring 2022 Solutions 10
Using the update formulas we have
1 1 𝑛 𝑎𝜇 +𝑏𝑥 96 1 9
𝑎 = = , 𝑏 = = 2, ⇒ 𝜇 = prior = ≈ 5.05, 𝜎2 = = ≈ 0.47.
𝜎2 9 𝜎2 post 𝑎+𝑏 19 post 𝑎+𝑏 19
prior
−5 0 5 10 15
6.0
5.0
4.0
3.0
2.0
1.0
0.0
Prior N(6,9)
Posterior N(5.05,0.47)
q
After observing 𝑥 , … , 𝑥 , we see that the posterior mean is close to 𝑥 and the posterior
1 4
variance is much smaller than the prior variance. The data has made us more certain about
the location of 𝜃.
(c) IQ in the general population follows a 𝑁(100, 152) distribution. An IQ test is unbiased
with a known normal variance of 102; that is, if the same person is tested multiple times,
their measured IQ will differ from their true IQ according to a normal distribution with
mean 0 and variance 100.
(i) Randall Vard scored an 80 on the test. What is the posterior expected value of their true
IQ?
(ii) Mary I. Taft scored a 150 on the test. What is the posterior expected value of their true
IQ?
Solution: With no data we assume the prior mean for 𝜃 is the population average of 100,
i.e. our prior is 𝑓(𝜃) ∼ N(100, 152). For data 𝑥 = score on the IQ test we have the likelihood
𝑓(𝑥|𝜃) ∼ N(𝜃, 102). Using the update formulas we have
𝑛 = 1, 𝜇 = 100, 𝜎2 = 152, 𝜎2 = 102.
prior prior
So 𝑎 = 1/225, 𝑏 = 1/100.
𝑎 ⋅ 100 + 𝑏 ⋅ 80
(i) Randall, 𝑥 = 80: 𝜇 = = 86.15. (This is the posterior expected value.)
post 𝑎 + 𝑏
𝑎⋅100+𝑏 ⋅150
(ii) Mary, 𝑥 = 150: 𝜇 = = 134.62 (This is the posterior expected value.)
post 𝑎 + 𝑏
Both their posterior expected values are closer to the population mean than their scores.
This is the Bayesian version of regression towards the mean!
18.05 Problem Set 7, Spring 2022 Solutions 11
Problem 7. (15: 10,5 pts.) (Censored data)
Sometimes data is not reported in full. This can mean only reporting values in a certain
range or not reporting exact values. We call such data censored.
We have a 4-sided die and a 6-sided die. One of them is chosen at random and rolled 5
times. Instead of reporting the number of spots on a roll we censor the data and just report
1 if the roll is a 1; 0 if the roll is not a 1.
(a) Suppose the data for the five rolls is 1, 0, 1, 1, 1. Starting from a flat prior on the
choice of die, update in sequence and report, after each roll, the posterior odds that the
chosen die is the 4-sided die.
Solution: First note that we assume that, given a particular die, the rolls are independent.
Let 𝑥 be the censored value on one roll. The Bayes factor for 𝑥 is
𝑝(𝑥|4-sided) 3/4 = 9/10 if 𝑥 = 0
Bayes factor = = { 5/6
𝑝(𝑥|6-sided) 1/4 = 3/2 if 𝑥 = 1
1/6
Starting from the prior odds of 1, we multiply by the appropriate Bayes factor and get the
posterior odds after rolls 1–5 are
Prior odds: 1
3
Posterior odds after roll 1 = 1⋅ = 1.5
2
3 9 27
Posterior odds after roll 2 = ⋅ = = 1.35
2 10 20
27 3 81
Posterior odds after roll 3 = ⋅ = = 2.025
20 2 40
81 3 243
Posterior odds after roll 4 = ⋅ = = 3.0375
40 2 80
243 3 729
Posterior odds after roll 5 = ⋅ = = 4.55625
80 2 160
(b) A censored value of 1 is evidence in favor of which die? What about 0? How is this
reflected in the posterior odds in part (a)?
Solution: In part (a) we saw the Bayes factor when 𝑥 = 1 is 3/2. Since this is more than
1 it is evidence in favor of the 4-sided die. When 𝑥 = 0 the Bayes factor is 9/10, which is
evidence in favor of the 6-sided die.
We saw this in part (a) because after every value of 1 the odds for the 4-sided die went up
and after the value of 0 the odds went down.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
