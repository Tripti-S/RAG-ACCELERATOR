# Mit18 05 S22 Statistics

---

Introduction to Statistics
Class 10, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Know the three overlapping “phases” of statistical practice.
2. Know what is meant by the term statistic.
2 Introduction to statistics
Statistics deals with data. Generally speaking, the goal of statistics is to make inferences
based on data. We can divide this the process into three phases: collecting data, describing
data and analyzing data. This fits into the paradigm of the scientific method. We make
hypotheses about what’s true, collect data in experiments, describe the results, and then
infer from the results the strength of the evidence concerning our hypotheses.
2.1 Experimental design
The design of an experiment is crucial to making sure the collected data is useful. The
adage ‘garbage in, garbage out’ applies here. A poorly designed experiment will produce
poor quality data, from which it may be impossible to draw useful, valid inferences. To
quote R.A. Fisher one of the founders of modern statistics,
To consult a statistician after an experiment is finished is often merely to ask
him to conduct a post-mortem examination. He can perhaps say what the
experiment died of.
2.2 Descriptive statistics
Raw data often takes the form of a massive list, array, or database of labels and numbers.
To make sense of the data, we can calculate summary statistics like the mean, median, and
interquartile range. We can also visualize the data using graphical devices like histograms,
scatterplots, and the empirical cdf. These methods are useful for both communicating and
exploring the data to gain insight into its structure, such as whether it might follow a
familiar probability distribution.
2.3 Inferential statistics
Ultimately we want to draw inferences about the world. Often this takes the form of
specifyingastatisticalmodelfortherandomprocessbywhichthedataarises. Forexample,
suppose the data takes the form of a series of measurements whose error we believe follows
a normal distribution. (Note this is always an approximation since we know the error must
1
18.05 Class 10, Introduction to Statistics, Spring 2022 2
have some bound while a normal distribution has range (−∞,∞).) We might then use the
data to provide evidence for or against this hypothesis. Our focus in 18.05 will be on how
to use data to draw inferences about model parameters. For example, assuming gestational
length follows a 𝑁(𝜇,𝜎) distribution, we’ll use the data of the gestational lengths of, say,
500 pregnancies to draw inferences about the values of the parameters 𝜇 and 𝜎. Similarly,
we may model the result of a two-candidate election by a Bernoulli(𝑝) distribution, and use
poll data to draw inferences about the value of 𝑝.
We can rarely make definitive statements about such parameters because the data itself
comesfromarandomprocess(suchaschoosingwhotopoll). Rather,ourstatisticalevidence
will always involve probability statements. Unfortunately, the media and public at large
are wont to misunderstand the probabilistic meaning of statistical statements. In fact,
researchers themselves often commit the same errors. In this course, we will emphasize the
meaning of statistical statements alongside the methods which produce them.
Example 1. To study the effectiveness of new treatment for cancer, patients are recruited
and then divided into an experimental group and a control group. The experimental group
is given the new treatment and the control group receives the current standard of care.
Data collected from the patients might include demographic information, medical history,
initial state of cancer, progression of the cancer over time, treatment cost, and the effect of
the treatment on tumor size, remission rates, longevity, and quality of life. The data will
be used to make inferences about the effectiveness of the new treatment compared to the
current standard of care.
Notice that this study will go through all three phases described above. The experimental
design must specify the size of the study, who will be eligible to join, how the experimental
and control groups will be chosen, how the treatments will be administered, whether or
not the subjects or doctors know who is getting which treatment, and precisely what data
will be collected, among other things. Once the data is collected it must be described and
analyzed to determine whether it supports the hypothesis that the new treatment is more
(or less) effective than the current one(s), and by how much. These statistical conclusions
will be framed as precise statements involving probabilities.
As noted above, misinterpreting the exact meaning of statistical statements is a common
source of error which has led to tragedy on more than one occasion.
Example 2. In 1999 in Great Britain, Sally Clark was convicted of murdering her two
children after each child died weeks after birth (the first in 1996, the second in 1998). Her
conviction was largely based on a faulty use of statistics to rule out sudden infant death
syndrome. Thoughherconvictionwasoverturnedin2003, shedevelopedseriouspsychiatric
problems during and after her imprisonment and died of alcohol poisoning in 2007. See
https://en.wikipedia.org/wiki/Sally_Clark
ThisTEDtalkdiscussestheSallyClarkcaseandotherinstancesofpoorstatisticalintuition:
https://www.youtube.com/watch?v=kLmzxmRcUTo
2.4 What is a statistic?
We give a simple definition whose meaning is best elucidated by examples.
Definition. A statistic is anything that can be computed from the collected data.
18.05 Class 10, Introduction to Statistics, Spring 2022 3
Example 3. Consider the data of 1000 rolls of a die. All of the following are statistics:
the average of the 1000 rolls; the number of times a 6 was rolled; the sum of the squares of
the rolls minus the number of even rolls. It’s hard to imagine how we would use the last
example, but it is a statistic. On the other hand, the probability of rolling a 6 is not a
statistic, whether or not the die is truly fair. Rather this probability is a property of the die
(and the way we roll it) which we can estimate using the data. Such an estimate is given
by the statistic ‘proportion of the rolls that were 6’.
Example 4. Suppose we treat a group of cancer patients with a new procedure and collect
data on how long they survive post-treatment. From the data we can compute the average
survival time of patients in the group. We might employ this statistic as an estimate of the
averagesurvivaltimeforfuturecancerpatientsfollowingthenewprocedure. The“expected
survival time” for the new procedure (if that even has a meaning) is not a statistic.
Example 5. Suppose we ask 1000 residents whether or not they support the proposal to
legalize marijuana in Massachusetts. The proportion of the 1000 who support the proposal
is a statistic. The proportion of all Massachusetts residents who support the proposal is
not a statistic since we have not queried every single one (note the word “collected” in the
definition). Rather,wehopetodrawastatisticalconclusionaboutthestate-wideproportion
based on the data of our random sample.
The following are two general types of statistics we will use in 18.05.
1. Point statistics: a single value computed from data, such as the sample average 𝑥 or
𝑛
the sample standard deviation 𝑠 .
𝑛
2. Interval statistics: an interval [𝑎,𝑏] computed from the data. This is really just a pair of
point statistics, and will often be presented in the form 𝑥±𝑠.
3 Review of Bayes’ theorem
WecannotstressstronglyenoughhowimportantBayes’theoremistoourviewofinferential
statistics. Recall that Bayes’ theorem allows us to ‘invert’ conditional probabilities. That
is, if 𝐻 and 𝐷 are events, then Bayes’ theorem says
𝑃(𝐷|𝐻)𝑃(𝐻)
𝑃(𝐻|𝐷) = .
𝑃(𝐷)
In scientific experiments we start with a hypothesis and collect data to test the hypothesis.
We will often let 𝐻 represent the event ‘our hypothesis is true’ and let 𝐷 be the collected
data. In these words Bayes’ theorem says
𝑃(data |hypothesis is true)⋅𝑃(hypothesis is true)
𝑃(hypothesis is true | data) =
𝑃(data)
The left-hand term is the probability our hypothesis is true given the data we collected.
This is precisely what we’d like to know. When all the probabilities on the right are known
exactly, we can compute the probability on the left exactly. This will be our focus next
week. Unfortunately, in practice we rarely know the exact values of all the terms on the
18.05 Class 10, Introduction to Statistics, Spring 2022 4
right. Statisticians have developed a number of ways to cope with this lack of knowledge
and still make useful inferences. We will be exploring these methods for the rest of the
course.
Example 6. Screening for a disease redux
Suppose a screening test for a disease has a 1% false positive rate and a 1% false negative
rate. Suppose also that the rate of the disease in the population is 0.002. Finally suppose
a randomly selected person tests positive. In the language of hypothesis and data we have:
Hypothesis: 𝐻 = ‘the person has the disease’
Data: 𝐷 = ‘the test was positive.’
What we want to know: 𝑃(𝐻|𝐷) = 𝑃(the person has the disease | a positive test)
In this example all the probabilities on the right are known so we can use Bayes’ theorem
to compute what we want to know.
𝑃(hypothesis | data) = 𝑃(the person has the disease | a positive test)
= 𝑃(𝐻|𝐷)
𝑃(𝐷|𝐻)𝑃(𝐻)
=
𝑃(𝐷)
0.99⋅0.002
=
0.99⋅0.002+0.01⋅0.998
= 0.166
Before the test we would have said the probability the person had the disease was 0.002.
After the test we see the probability is 0.166. That is, the positive test provides some
evidence that the person has the disease.
Maximum Likelihood Estimates
Class 10, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to define the likelihood function for a parametric model given data.
2. Be able to compute the maximum likelihood estimate of unknown parameter(s).
2 Introduction
Suppose we know we have data consisting of values 𝑥 ,…,𝑥 drawn from an exponential
1 𝑛
distribution. The question remains: which exponential distribution?!
We have casually referred to the exponential distribution or the binomial distribution or the
normal distribution. In fact the exponential distribution exp(𝜆) is not a single distribution
butratheraone-parameterfamilyofdistributions. Eachvalueof𝜆definesadifferentdistri-
bution in the family, with pdf 𝑓 (𝑥) = 𝜆𝑒−𝜆𝑥 on [0,∞). Similarly, a binomial distribution
𝜆
bin(𝑛,𝑝) is determined by the two parameters 𝑛 and 𝑝, and a normal distribution 𝑁(𝜇,𝜎2)
is determined by the two parameters 𝜇 and 𝜎2 (or equivalently, 𝜇 and 𝜎). Parameterized
families of distributions are often called parametric distributions or parametric models.
We are often faced with the situation of having random data which we know (or believe)
is drawn from a parametric model, whose parameters we do not know. For example, in
an election between two candidates, polling data constitutes draws from a Bernoulli(𝑝)
distribution with unknown parameter 𝑝. In this case we would like to use the data to
estimate the value of the parameter 𝑝, as the latter predicts the result of the election.
Similarly, assuming gestational length follows a normal distribution, we would like to use
the data of the gestational lengths from a random sample of pregnancies to draw inferences
about the values of the parameters 𝜇 and 𝜎2.
Our focus so far has been on computing the probability of data arising from a parametric
model with known parameters. Statistical inference flips this on its head: we will estimate
the probability of parameters given a parametric model and observed data drawn from it.
In the coming weeks we will see how parameter values are naturally viewed as hypotheses,
so we are in fact estimating the probability of various hypotheses given the data.
3 Maximum Likelihood Estimates
There are many methods for estimating unknown parameters from data. We will first
consider the maximum likelihood estimate (MLE), which answers the question:
For which parameter value does the observed data have the biggest probability?
The MLE is an example of a point estimate because it gives a single value for the unknown
parameter (later our estimates will involve intervals and probabilities). Two advantages of
1
18.05 Class 10, Maximum Likelihood Estimates , Spring 2022 2
the MLE are that it is often easy to compute and that it agrees with our intuition in simple
examples. We will explain the MLE through a series of examples.
Example 1. Acoinisflipped100times. Giventhattherewere55heads,findthemaximum
likelihood estimate for the probability 𝑝 of heads on a single toss.
Before actually solving the problem, let’s establish some notation and terms.
We can think of counting the number of heads in 100 tosses as an experiment. For a given
value of 𝑝, the probability of getting 55 heads in this experiment is the binomial probability
100
𝑃(55 heads) = ( )𝑝55(1−𝑝)45.
55
The probability of getting 55 heads depends on the value of 𝑝, so let’s include 𝑝 in by using
the notation of conditional probability:
100
𝑃(55 heads|𝑝) = ( )𝑝55(1−𝑝)45.
55
You should read 𝑃(55 heads|𝑝) as:
‘the probability of 55 heads given 𝑝,’
or more precisely as
‘the probability of 55 heads given that the probability of heads on a single toss is 𝑝.’
Here are some standard terms we will use as we do statistics.
• Experiment: Flip the coin 100 times and count the number of heads.
• Data: The data is the result of the experiment. In this case it is ‘55 heads’.
• Parameter(s) of interest: We are interested in the value of the unknown parameter 𝑝.
• Likelihood, or likelihood function: this is 𝑃(data|𝑝). Note it is a function of both the
data and the parameter 𝑝. In this case the likelihood is
100
𝑃(55 heads|𝑝) = ( )𝑝55(1−𝑝)45.
55
Notes: 1. The likelihood 𝑃(data |𝑝) changes as the parameter of interest 𝑝 changes.
2. Look carefully at the definition. One typical source of confusion is to mistake the likeli-
hood 𝑃(data |𝑝) for 𝑃(𝑝|data). We know from our earlier work with Bayes’ theorem that
𝑃(data|𝑝) and 𝑃(𝑝|data) are usually very different.
Definition: Given data the maximum likelihood estimate (MLE) for the parameter 𝑝 is
the value of 𝑝 that maximizes the likelihood 𝑃(data |𝑝). That is, the MLE is the value of
𝑝 for which the data is most likely.
Solution: For the problem at hand, we saw above that the likelihood
100
𝑃(55 heads|𝑝) = ( )𝑝55(1−𝑝)45.
55
18.05 Class 10, Maximum Likelihood Estimates , Spring 2022 3
We’ll use the notation 𝑝̂ for the MLE. We use calculus to find it by taking the derivative of
the likelihood function and setting it to 0.
𝑑 100
𝑃(data |𝑝) = ( )(55𝑝54(1−𝑝)45−45𝑝55(1−𝑝)44) = 0.
𝑑𝑝 55
Solving this for 𝑝 we get
55𝑝54(1−𝑝)45 = 45𝑝55(1−𝑝)44
55(1−𝑝) = 45𝑝
55 = 100𝑝
the MLE is 𝑝̂ = 0.55
Note: 1. The MLE for 𝑝 turned out to be exactly the fraction of heads we saw in our data.
2. The MLE is computed from the data. That is, it is a statistic.
3. Oﬀicially we need to check that this critical point is actually the maximum. We could
use the second derivative test. Another way is to notice that we are interested only in
0 ≤ 𝑝 ≤ 1; that the probability is bigger than zero for 0 < 𝑝 < 1; and that the probability
is equal to zero for 𝑝 = 0 and for 𝑝 = 1. From these facts it follows that the critical point
must be the unique maximum.
3.1 Log likelihood
If is often easier to work with the natural log of the likelihood function. For short this is
simply called the log likelihood. Since ln(𝑥) is an increasing function, the maxima of the
likelihood and log likelihood coincide.
Example 2. Redo the previous example using log likelihood.
Solution: We had the likelihood 𝑃(55 heads |𝑝) = (100)𝑝55(1 − 𝑝)45. Therefore the log
55
likelihood is
100
ln(𝑃(55 heads |𝑝) = ln(( ))+55ln(𝑝)+45ln(1−𝑝).
55
Maximizing likelihood is the same as maximizing log likelihood. We check that calculus
gives us the same answer as before:
𝑑 𝑑 100
(log likelihood) = [ln(( ))+55ln(𝑝)+45ln(1−𝑝)]
𝑑𝑝 𝑑𝑝 55
55 45
= − = 0
𝑝 1−𝑝
⇒ 55(1−𝑝) = 45𝑝
⇒ 𝑝̂ = 0.55
18.05 Class 10, Maximum Likelihood Estimates , Spring 2022 4
3.2 Maximum likelihood for continuous distributions
Forcontinuousdistributions,weusetheprobabilitydensityfunctiontodefinethelikelihood.
We show this in a few examples. In the next section we explain how this is analogous to
what we did in the discrete case.
Example 3. Light bulbs
Suppose that the lifetime of Badger brand light bulbs is modeled by an exponential distri-
bution with (unknown) parameter 𝜆. We test 5 bulbs and find they have lifetimes of 2, 3,
1, 3, and 4 years, respectively. What is the MLE for 𝜆?
Solution: We need to be careful with our notation. With five different values it is best to
use subscripts. Let 𝑋 be the lifetime of the 𝑖th bulb and let 𝑥 be the value 𝑋 takes. Then
𝑖 𝑖 𝑖
each 𝑋 has pdf 𝑓 (𝑥 ) = 𝜆e−𝜆𝑥 𝑖. We assume the lifetimes of the bulbs are independent,
𝑖 𝑋 𝑖
𝑖
so the joint pdf is the product of the individual densities:
𝑓(𝑥 ,𝑥 ,𝑥 ,𝑥 ,𝑥 |𝜆) = (𝜆e−𝜆𝑥 1)(𝜆e−𝜆𝑥 2)(𝜆e−𝜆𝑥 3)(𝜆e−𝜆𝑥 4)(𝜆e−𝜆𝑥 5) = 𝜆5e−𝜆(𝑥 1 +𝑥 2 +𝑥 3 +𝑥 4 +𝑥 5 ).
1 2 3 4 5
Note that we write this as a conditional density, since it depends on 𝜆. Viewing the data
as fixed and 𝜆 as variable, this density is the likelihood function. Our data had values
𝑥 = 2, 𝑥 = 3, 𝑥 = 1, 𝑥 = 3, 𝑥 = 4.
1 2 3 4 5
So the likelihood and log likelihood functions with this data are
𝑓(2,3,1,3,4|𝜆) = 𝜆5e−13𝜆, ln(𝑓(2,3,1,3,4|𝜆) = 5ln(𝜆)−13𝜆
Finally we use calculus to find the MLE:
𝑑 5 5
(log likelihood) = −13 = 0 ⇒ 𝜆̂ = .
𝑑𝜆 𝜆 13
Note: 1. In this example we used an uppercase letter for a random variable and the
corresponding lowercase letter for the value it takes. This will be our usual practice.
2. The MLE for 𝜆 turned out to be the reciprocal of the sample mean 𝑥,̄ so 𝑋 ∼ exp(𝜆̂)
satisfies 𝐸[𝑋] = 𝑥.̄
The following example illustrates how we can use the method of maximum likelihood to
estimate multiple parameters at once.
Example 4. Normal distributions
Suppose the data 𝑥 ,𝑥 ,…,𝑥 is drawn from a N(𝜇,𝜎2) distribution, where 𝜇 and 𝜎 are
1 2 𝑛
unknown. Find the maximum likelihood estimate for the pair (𝜇,𝜎2).
Solution: Let’s be precise and phrase this in terms of random variables and densities. Let
uppercase 𝑋 ,…,𝑋 be i.i.d. N(𝜇,𝜎2) random variables, and let lowercase 𝑥 be the value
1 𝑛 𝑖
𝑋 takes. The density for each 𝑋 is
𝑖 𝑖
𝑓 𝑋 (𝑥 𝑖 ) = √
1 e−(𝑥
2
𝑖−
𝜎
𝜇
2
)2
.
𝑖 2𝜋𝜎
Since the 𝑋 are independent their joint pdf is the product of the individual pdf’s:
𝑖
𝑛
𝑓(𝑥 1 ,…,𝑥 𝑛 |𝜇,𝜎) = (√
1
)
e−∑𝑛
𝑖=1
(𝑥
2
𝑖−
𝜎
𝜇
2
)2
.
2𝜋𝜎
18.05 Class 10, Maximum Likelihood Estimates , Spring 2022 5
For the fixed data 𝑥 ,…,𝑥 , the likelihood and log likelihood are
1 𝑛
𝑓(𝑥 1 ,…,𝑥 𝑛 |𝜇,𝜎) = (√ 2 1 𝜋𝜎 ) 𝑛 e−∑𝑛 𝑖=1 (𝑥 2 𝑖− 𝜎 𝜇 2 )2 , ln(𝑓(𝑥 1 ,…,𝑥 𝑛 |𝜇,𝜎)) = −𝑛ln( √ 2𝜋)−𝑛ln(𝜎)−∑ 𝑛 (𝑥 𝑖 2 − 𝜎2 𝜇)2 .
𝑖=1
Since ln(𝑓(𝑥 ,…,𝑥 |𝜇,𝜎)) is a function of the two variables 𝜇, 𝜎 we use partial derivatives
1 𝑛
to find the MLE. The easy value to find is 𝜇:̂
𝜕𝑓(𝑥 ,…,𝑥 |𝜇,𝜎) 𝑛 (𝑥 −𝜇) 𝑛 ∑ 𝑛 𝑥
1 𝑛 = ∑ 𝑖 = 0 ⇒ ∑𝑥 = 𝑛𝜇 ⇒ 𝜇̂= 𝑖=1 𝑖 = 𝑥.
𝜕𝜇 𝜎2 𝑖 𝑛
𝑖=1 𝑖=1
To find 𝜎̂ we differentiate and solve for 𝜎:
𝜕𝑓(𝑥 ,…,𝑥 |𝜇,𝜎) 𝑛 𝑛 (𝑥 −𝜇)2 ∑ 𝑛 (𝑥 −𝜇)2
1 𝑛 = − +∑ 𝑖 = 0 ⇒ 𝜎̂2 = 𝑖=1 𝑖 .
𝜕𝜎 𝜎 𝜎3 𝑛
𝑖=1
We already know 𝜇̂= 𝑥, so we use that as the value for 𝜇 in the formula for 𝜎̂. We get the
maximum likelihood estimates
𝜇̂ = 𝑥 = the mean of the data
𝑛 1 𝑛 1
𝜎̂2 = ∑ (𝑥 −𝜇)̂ 2 = ∑ (𝑥 −𝑥)2 = the unadjusted variance of the data.
𝑛 𝑖 𝑛 𝑖
𝑖=1 𝑖=1
∑ 𝑛 (𝑥 −𝜇)̂ 2
(Later we will learn that the sample variance is 𝑖=1 𝑖 .)
𝑛−1
Example 5. Uniform distributions
Suppose our data 𝑥 ,…𝑥 are independently drawn from a uniform distribution 𝑈(𝑎,𝑏).
1 𝑛
Find the MLE for 𝑎 and 𝑏.
Solution: This example is different from the previous ones in that we won’t use calculus
to find the MLE. The density for 𝑈(𝑎,𝑏) is 1 on [𝑎,𝑏]. Therefore our likelihood function
𝑏−𝑎
is
𝑛
( 1 ) if all 𝑥 are in the interval [𝑎,𝑏]
𝑓(𝑥 ,…,𝑥 |𝑎,𝑏) = { 𝑏−𝑎 𝑖
1 𝑛
0 otherwise.
This is maximized by making 𝑏−𝑎 as small as possible. The only restriction is that the
interval [𝑎,𝑏] must include all the data. Thus the MLE for the pair (𝑎,𝑏) is
𝑎̂= min(𝑥 ,…,𝑥 ) 𝑏̂ = max(𝑥 ,…,𝑥 ).
1 𝑛 1 𝑛
Example 6. Capture/recapture method
The capture/recapture method is a way to estimate the size of a population in the wild.
The method assumes that each animal in the population is equally likely to be captured by
a trap.
Suppose 10 animals are captured, tagged and released. A few months later, 20 animals are
captured, examined, and released. 4 of these 20 are found to be tagged. Estimate the size
of the wild population using the MLE for the probability that a wild animal is tagged.
18.05 Class 10, Maximum Likelihood Estimates , Spring 2022 6
Solution: Our unknown parameter 𝑛 is the number of animals in the wild. Our data is
that 4 out of 20 recaptured animals were tagged (and that there are 10 tagged animals).
The likelihood function is
(𝑛−10)(10)
𝑃(data |𝑛 animals) = 16 4
(𝑛)
20
(Thenumeratoristhenumberofwaystochoose16animalsfromamongthe𝑛−10untagged
ones times the number of was to choose 4 out of the 10 tagged animals. The denominator
is the number of ways to choose 20 animals from the entire population of 𝑛.) We can use
R to compute that the likelihood function is maximized when 𝑛 = 50. This should make
some sense. It says our best estimate is that the fraction of all animals that are tagged is
10/50 which equals the fraction of recaptured animals which are tagged.
Example 7. Hardy-Weinberg. Suppose that a particular gene occurs as one of two
alleles (𝐴 and 𝑎), where allele 𝐴 has frequency 𝜃 in the population. That is, a random copy
of the gene is 𝐴 with probability 𝜃 and 𝑎 with probability 1−𝜃. Since a diploid genotype
consists of two genes, the probability of each genotype is given by:
genotype AA Aa aa
probability 𝜃2 2𝜃(1−𝜃) (1−𝜃)2
Suppose we test a random sample of people and find that 𝑘 are 𝐴𝐴, 𝑘 are 𝐴𝑎, and 𝑘 are
1 2 3
𝑎𝑎. Find the MLE of 𝜃.
Solution: The likelihood function is given by
𝑘 +𝑘 +𝑘 𝑘 +𝑘 𝑘
𝑃(𝑘 ,𝑘 ,𝑘 |𝜃) = ( 1 2 3)( 2 3)( 3)𝜃2𝑘 1(2𝜃(1−𝜃))𝑘 2(1−𝜃)2𝑘 3.
1 2 3 𝑘 𝑘 𝑘
1 2 3
So the log likelihood is given by
constant+2𝑘 ln(𝜃)+𝑘 ln(𝜃)+𝑘 ln(1−𝜃)+2𝑘 ln(1−𝜃)
1 2 2 3
We set the derivative equal to zero:
2𝑘 +𝑘 𝑘 +2𝑘
1 2 − 2 3 = 0
𝜃 1−𝜃
Solving for 𝜃, we find the MLE is
2𝑘 +𝑘
𝜃̂= 1 2 ,
2𝑘 +2𝑘 +2𝑘
1 2 3
which is simply the fraction of 𝐴 alleles among all the genes in the sampled population.
4 Why we use the density to find the MLE for continuous
distributions
The idea for the maximum likelihood estimate is to find the value of the parameter(s) for
which the data has the highest probability. In this section we ’ll see that we’re doing this
18.05 Class 10, Maximum Likelihood Estimates , Spring 2022 7
is really what we are doing with the densities. We will do this by considering a smaller
version of the light bulb example.
Example 8. Suppose we have two light bulbs whose lifetimes follow an exponential(𝜆)
distribution. Suppose also that we independently measure their lifetimes and get data
𝑥 = 2 years and 𝑥 = 3 years. Find the value of 𝜆 that maximizes the probability of this
1 2
data.
Solution: The main paradox to deal with is that for a continuous distribution the proba-
bility of a single value, say 𝑥 = 2, is zero. We resolve this paradox by remembering that a
1
single measurement really means a range of values, e.g. in this example we might check the
light bulb once a day. So the data 𝑥 = 2 years really means 𝑥 is somewhere in a range of
1 1
1 day around 2 years.
If the range is small we call it 𝑑𝑥 . The probability that 𝑋 is in the range is approximated
1 1
by 𝑓 (𝑥 |𝜆)𝑑𝑥 . This is illustrated in the figure below. The data value 𝑥 is treated in
𝑋 1 1 2
1
exactly the same way.
density𝑓 (𝑥 |𝜆) density𝑓 (𝑥 |𝜆)
𝑋1 1 𝑋2 2
𝜆 𝜆
probability≈𝑓 (𝑥 |𝜆)𝑑𝑥
𝑋1 1 1 probability≈𝑓
𝑋2
(𝑥
2
|𝜆)𝑑𝑥
2
𝑑𝑥
1 𝑑𝑥
2
𝑥 𝑥
𝑥 𝑥
1 2
The usual relationship between density and probability for small ranges.
Sincethedataiscollectedindependentlythejointprobabilityistheproductoftheindividual
probabilities. Stated carefully
𝑃(𝑋 in range, 𝑋 in range|𝜆) ≈ 𝑓 (𝑥 |𝜆)𝑑𝑥 ⋅𝑓 (𝑥 |𝜆)𝑑𝑥
1 2 𝑋 1 1 𝑋 2 2
1 2
Finally, using the values 𝑥 = 2 and 𝑥 = 3 and the formula for an exponential pdf we have
1 2
𝑃(𝑋 in range, 𝑋 in range|𝜆) ≈ 𝜆e−2𝜆𝑑𝑥 ⋅𝜆e−3𝜆𝑑𝑥 = 𝜆2e−5𝜆𝑑𝑥 𝑑𝑥 .
1 2 1 2 1 2
Now that we have a genuine probability we can look for the value of 𝜆 that maximizes it.
Looking at the formula above we see that the factor 𝑑𝑥 𝑑𝑥 will play no role in finding the
1 2
maximum. So for the MLE we drop it and simply call the density the likelihood:
likelihood = 𝑓(𝑥 ,𝑥 |𝜆) = 𝜆2e−5𝜆.
1 2
The value of 𝜆 that maximizes this is found just like in the example above. It is 𝜆̂ = 2/5.
5 Appendix: Properties of the MLE
Fortheinterestedreader,wenoteseveralnicefeaturesoftheMLE.Thesearequitetechnical
and will not be on any exams.
18.05 Class 10, Maximum Likelihood Estimates , Spring 2022 8
The MLE behaves well under transformations. That is, if 𝑝̂ is the MLE for 𝑝 and 𝑔 is a
one-to-one function, then 𝑔(𝑝̂) is the MLE for 𝑔(𝑝). For example, if 𝜎̂ is the MLE for the
standard deviation 𝜎 then (𝜎̂)2 is the MLE for the variance 𝜎2.
Furthermore, under some technical smoothness assumptions, the MLE is asymptotically
unbiased and has asymptotically minimal variance. To explain these notions, note that
the MLE is itself a random variable since the data is random and the MLE is computed
from the data. Let 𝑥 ,𝑥 ,… be an infinite sequence of samples from a distribution with
1 2
parameter 𝑝. Let 𝑝̂ be the MLE for 𝑝 based on the data 𝑥 ,…,𝑥 .
𝑛 1 𝑛
Asymptotically unbiased means that as the amount of data grows, the mean of the MLE
converges to 𝑝. In symbols: 𝐸[𝑝̂ ] → 𝑝 as 𝑛 → ∞. Of course, we would like the MLE to be
𝑛
close to 𝑝 with high probability, not just on average, so the smaller the variance of the MLE
the better. Asymptotically minimal variance means that as the amount of data grows, the
MLE has the minimal variance among all unbiased estimators of 𝑝. In symbols: for any
unbiased estimator 𝑝̃ and 𝜖 > 0 we have that Var(𝑝̃ )+𝜖 > Var(𝑝̂ ) as 𝑛 → ∞.
𝑛 𝑛 𝑛
Bayesian Updating with Discrete Priors
Class 11, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to apply Bayes’ theorem to compute probabilities.
2. Be able to define and to identify the roles of prior probability, likelihood (Bayes term),
posterior probability, data and hypothesis in the application of Bayes’ Theorem.
3. Be able to use a Bayesian update table to compute posterior probabilities.
2 Review of Bayes’ theorem
Recall that Bayes’ theorem allows us to ‘invert’ conditional probabilities. If ℋ and 𝒟 are
events, then:
𝑃(𝒟|ℋ)𝑃(ℋ)
𝑃(ℋ|𝒟) =
𝑃(𝒟)
Our view is that Bayes’ theorem forms the foundation for inferential statistics. We will
begin to justify this view today.
2.1 The base rate fallacy
When we first learned Bayes’ theorem we worked an example about screening tests showing
that 𝑃(𝒟|ℋ) can be very different from 𝑃(ℋ|𝒟). In the appendix we work a similar
example. If you are not comfortable with Bayes’ theorem you should read the example in
the appendix now.
3 Terminology and Bayes’ theorem in tabular form
WenowuseacointossingproblemtointroduceterminologyandatabularformatforBayes’
theorem. This will provide a simple, uncluttered example that shows our main points.
Example 1. There are three types of coins which have different probabilities of landing
heads when tossed.
• Type 𝐴 coins are fair, with probability 0.5 of heads
• Type 𝐵 coins are bent and have probability 0.6 of heads
• Type 𝐶 coins are bent and have probability 0.9 of heads
Suppose I have a drawer containing 5 coins: 2 of type 𝐴, 2 of type 𝐵, and 1 of type 𝐶. I
reach into the drawer and pick a coin at random. Without showing you the coin I flip it
once and get heads. What is the probability it is type 𝐴? Type 𝐵? Type 𝐶?
1
18.05 Class 11, Bayesian Updating with Discrete Priors, Spring 2022 2
Solution: Let 𝐴, 𝐵, and 𝐶 be the event that the chosen coin was type 𝐴, type 𝐵, and
type 𝐶. Let 𝒟 be the event that the toss is heads. The problem asks us to find
𝑃(𝐴|𝒟), 𝑃(𝐵|𝒟), 𝑃(𝐶|𝒟).
Before applying Bayes’ theorem, let’s introduce some terminology.
• Experiment: pick a coin from the drawer at random, flip it, and record the result.
• Data: the result of our experiment. In this case the event 𝒟 = ‘heads’. We think of
𝒟 as data that provides evidence for or against each hypothesis.
• Hypotheses: we are testing three hypotheses: the coin is type 𝐴, 𝐵 or 𝐶.
• Prior probability: the probability of each hypothesis prior to tossing the coin (collect-
ing data). Since the drawer has 2 coins of type 𝐴, 2 of type 𝐵 and 1 of type 𝐶 we
have
𝑃(𝐴) = 0.4, 𝑃(𝐵) = 0.4, 𝑃(𝐶) = 0.2.
• Likelihood: (ThisisthesamelikelihoodweusedfortheMLE.)Thelikelihoodfunction
is𝑃(𝒟|ℋ),i.e.,theprobabilityofthedataassumingthatthehypothesisistrue. Most
often we will consider the data as fixed and let the hypothesis vary. For example,
𝑃(𝒟|𝐴) = probability of heads if the coin is type 𝐴. In our case the likelihoods are
𝑃(𝒟|𝐴) = 0.5, 𝑃(𝒟|𝐵) = 0.6, 𝑃(𝒟|𝐶) = 0.9.
The name likelihood is so well established in the literature that we have to teach
it to you. However in colloquial language likelihood and probability are synonyms.
This leads to the likelihood function often being confused with the probability of a
hypothesis. Because of this we’d prefer to use the name Bayes’ term. However since
we are stuck with ‘likelihood’ we will try to use it very carefully and in a way that
minimizes any confusion.
• Posterior probability: the probability (posterior to) of each hypothesis given the data
from tossing the coin.
𝑃(𝐴|𝒟), 𝑃(𝐵|𝒟), 𝑃(𝐶|𝒟).
These posterior probabilities are what the problem asks us to find.
We now use Bayes’ theorem to compute each of the posterior probabilities. We are going
to write this out in complete detail so we can pick out each of the parts (Remember that
the data 𝒟 is that the toss was heads.)
First we organize the probabilities into a tree:
0.4 0.4 0.2
𝐴 𝐵 𝐶
0.5 0.5 0.6 0.4 0.9 0.1
𝐻 𝑇 𝐻 𝑇 𝐻 𝑇
Probability tree for choosing and tossing a coin.
18.05 Class 11, Bayesian Updating with Discrete Priors, Spring 2022 3
𝑃(𝒟|𝐴)𝑃(𝐴)
Bayes’ theorem says, e.g. 𝑃(𝐴|𝒟) = . The denominator 𝑃(𝒟) is computed
𝑃(𝒟)
using the law of total probability:
𝑃(𝒟) = 𝑃(𝒟|𝐴)𝑃(𝐴)+𝑃(𝒟|𝐵)𝑃(𝐵)+𝑃(𝒟|𝐶)𝑃(𝐶) = 0.5⋅0.4+0.6⋅0.4+0.9⋅0.2 = 0.62.
Now each of the three posterior probabilities can be computed:
𝑃(𝒟|𝐴)𝑃(𝐴) 0.5⋅0.4 0.2
𝑃(𝐴|𝒟) = = =
𝑃(𝒟) 0.62 0.62
𝑃(𝒟|𝐵)𝑃(𝐵) 0.6⋅0.4 0.24
𝑃(𝐵|𝒟) = = =
𝑃(𝒟) 0.62 0.62
𝑃(𝒟|𝐶)𝑃(𝐶) 0.9⋅0.2 0.18
𝑃(𝐶|𝒟) = = =
𝑃(𝒟) 0.62 0.62
Notice that the total probability 𝑃(𝒟) is the same in each of the denominators and that it
is the sum of the three numerators. We can organize all of this very neatly in a Bayesian
update table:
hypothesis prior likelihood Bayes numerator posterior
(numerator/𝑃(𝒟))
ℋ 𝑃(ℋ) 𝑃(𝒟|ℋ) 𝑃(𝒟|ℋ)𝑃(ℋ) 𝑃(ℋ|𝒟)
𝐴 0.4 0.5 0.2 0.3226
𝐵 0.4 0.6 0.24 0.3871
𝐶 0.2 0.9 0.18 0.2903
total 1 NO SUM 𝑃(𝒟) = 0.62 1
The Bayes numerator is the product of the prior and the likelihood. We see in each of the
Bayes’ formula computations above that the posterior probability is obtained by dividing
the Bayes numerator by 𝑃(𝒟) = 0.62. We also see that the law of law of total probability
says that 𝑃(𝒟) is the sum of the entries in the Bayes numerator column.
Bayesian updating: The process of going from the prior probability 𝑃(ℋ) to the pos-
terior 𝑃(ℋ|𝒟) is called Bayesian updating. Bayesian updating uses the data to alter our
understanding of the probability of each of the possible hypotheses.
3.1 Important things to notice
1. There are two types of probabilities: Type one is the standard probability of data, e.g.
the probability of heads is 𝑝 = 0.9. Type two is the probability of the hypotheses, e.g.
the probability the chosen coin is type 𝐴, 𝐵 or 𝐶. This second type has prior (before
the data) and posterior (after the data) values.
2. The posterior (after the data) probabilities for each hypothesis are in the last column.
We see that coin 𝐵 is now the most probable, though its probability has decreased from
a prior probability of 0.4 to a posterior probability of 0.39. Meanwhile, the probability
of type 𝐶 has increased from 0.2 to 0.29.
3. The Bayes numerator column determines the posterior probability column. To compute
thelatter,wesimplydividedeachnumeratorby𝑃(𝒟),i.e. rescaledtheBayesnumerators
so that they sum to 1.
18.05 Class 11, Bayesian Updating with Discrete Priors, Spring 2022 4
4. If all we care about is finding the most likely hypothesis, the Bayes numerator works as
well as the normalized posterior.
5. The likelihood column does not sum to 1. The likelihood function is not a probability
function.
6. Theposteriorprobabilityrepresentstheoutcomeofa‘tug-of-war’betweenthelikelihood
and the prior. When calculating the posterior, a large prior may be deflated by a small
likelihood, and a small prior may be inflated by a large likelihood.
7. The maximum likelihood estimate (MLE) for Example 1 is hypothesis 𝐶, with a likeli-
hood 𝑃(𝒟|𝐶) = 0.9. The MLE is useful, but you can see in this example that it is not
the entire story, since type 𝐵 has the greatest posterior probability.
Terminology in hand, we can express Bayes’ theorem in various ways:
𝑃(𝒟|ℋ)𝑃(ℋ)
𝑃(ℋ|𝒟) =
𝑃(𝒟)
𝑃(data|hypothesis)𝑃(hypothesis)
𝑃(hypothesis|data) =
𝑃(data)
With the data fixed, the denominator 𝑃(𝒟) just serves to normalize the total posterior
probability to 1. So we can also express Bayes’ theorem as a statement about the propor-
tionality of two functions of ℋ (i.e, of the last two columns of the table).
𝑃(hypothesis|data) ∝ 𝑃(data|hypothesis)𝑃(hypothesis)
This leads to the most elegant form of Bayes’ theorem in the context of Bayesian updating:
posterior ∝ likelihood×prior
3.2 Prior and posterior probability mass functions
Earlier in the course we saw that it is convenient to use random variables and probability
mass functions. To do this we had to assign values to events (head is 1 and tails is 0). We
will do the same thing in the context of Bayesian updating.
Our standard notations will be:
• 𝜃 is the value of the hypothesis.
• 𝑝(𝜃) is the prior probability mass function of the hypothesis.
• 𝑝(𝜃|𝒟) is the posterior probability mass function of the hypothesis given the data.
• 𝑝(𝒟|𝜃) is the likelihood function. (This is not a pmf!)
In Example 1 we can represent the three hypotheses 𝐴, 𝐵, and 𝐶 by 𝜃 = 0.5, 0.6, 0.9. For
the data we’ll let 𝑥 = 1 mean heads and 𝑥 = 0 mean tails. Then the prior and posterior
probabilities in the table define the prior and posterior probability mass functions.
18.05 Class 11, Bayesian Updating with Discrete Priors, Spring 2022 5
Hypothesis 𝜃 prior pmf 𝑝(𝜃) posterior pmf 𝑝(𝜃|𝑥 = 1)
𝐴 0.5 𝑃(𝐴) = 𝑝(0.5) = 0.4 𝑃(𝐴|𝒟) = 𝑝(0.5|𝑥 = 1) = 0.3226
𝐵 0.6 𝑃(𝐵) = 𝑝(0.6) = 0.4 𝑃(𝐵|𝒟) = 𝑝(0.6|𝑥 = 1) = 0.3871
𝐶 0.9 𝑃(𝐶) = 𝑝(0.9) = 0.2 𝑃(𝐶|𝒟) = 𝑝(0.9|𝑥 = 1) = 0.2903
Here are plots of the prior and posterior pmf’s from the example.
𝑝(𝜃) 𝑝(𝜃|𝑥=1)
.4 .4
.2 .2
𝜃 𝜃
.5 .6 .9 .5 .6 .9
Prior pmf 𝑝(𝜃) and posterior pmf 𝑝(𝜃|𝑥 = 1) for Example 1
If the data was different then the likelihood column in the Bayesian update table would be
different. We can plan for different data by building the entire likelihood table ahead of
time. In the coin example there are two possibilities for the data: the toss is heads or the
toss is tails. So the full likelihood table has two likelihood columns:
hypothesis likelihood 𝑝(𝑥|𝜃)
𝜃 𝑝(𝑥 = 0|𝜃) 𝑝(𝑥 = 1|𝜃)
0.5 0.5 0.5
0.6 0.4 0.6
0.9 0.1 0.9
Important convention. Notice that in the above table we used the value of 𝜃 as the
hypothesis. Ofcourse, hypothesizing‘𝜃 = 0.5’isexactlythesameashypothesizing‘thecoin
is type A’. It is also useful in settings where we haven’t named all the possible hypotheses.
Example 2. Using the notation 𝑝(𝜃), etc., redo Example 1 assuming the flip was tails.
Solution: Since the data has changed, the likelihood column in the Bayesian update table
is now for 𝑥 = 0. That is, we must take the 𝑝(𝑥 = 0|𝜃) column from the likelihood table.
Bayes
hypothesis prior likelihood numerator posterior
𝜃 𝑝(𝜃) 𝑝(𝑥 = 0|𝜃) 𝑝(𝑥 = 0|𝜃)𝑝(𝜃) 𝑝(𝜃|𝑥 = 0)
0.5 0.4 0.5 0.2 0.5263
0.6 0.4 0.4 0.16 0.4211
0.9 0.2 0.1 0.02 0.0526
total 1 NO SUM 0.38 1
Now the probability that 𝜃 = 0.5, i.e. the coin is type A, has increased from 0.4 to 0.5263,
while the probability that 𝜃 = 0.9, i.e the coin is type C, has decreased from 0.2 to only
0.0526. Here are the corresponding plots:
18.05 Class 11, Bayesian Updating with Discrete Priors, Spring 2022 6
𝑝(𝜃) 𝑝(𝜃|𝑥=0)
.4 .4
.2 .2
𝜃 𝜃
.5 .6 .9 .5 .6 .9
Prior pmf 𝑝(𝜃) and posterior pmf 𝑝(𝜃|𝑥 = 0)
3.3 Food for thought.
Suppose that in Example 1 you didn’t know how many coins of each type were in the
drawer. You picked one at random and got heads. How would you go about deciding which
hypothesis (coin type) if any was most supported by the data?
4 Updating again and again
In life we are continually updating our beliefs with each new experience of the world. In
Bayesian inference, after updating the prior to the posterior, we can take more data and
update again! For the second update, the posterior from the first data becomes the prior
for the second data.
Example 3. Suppose you have picked a coin as in Example 1. You flip it once and get
heads. Then you flip the same coin and get heads again. What is the probability that the
coin was type A? Type B? Type C?
Solution: As we update several times the table gets big, so we use a smaller font to fit it
in:
Bayes Bayes
hypothesis prior likelihood 1 numerator 1 likelihood 2 numerator 2 posterior 2
𝜃 𝑝(𝜃) 𝑝(𝑥 =1|𝜃) 𝑝(𝑥 =1|𝜃)𝑝(𝜃) 𝑝(𝑥 =1|𝜃) 𝑝(𝑥 =1|𝜃)𝑝(𝑥 =1|𝜃)𝑝(𝜃) 𝑝(𝜃|𝑥 =1,𝑥 =1)
1 1 2 2 1 1 2
0.5 0.4 0.5 0.2 0.5 0.1 0.2463
0.6 0.4 0.6 0.24 0.6 0.144 0.3547
0.9 0.2 0.9 0.18 0.9 0.162 0.3990
total 1 NO SUM NO SUM 0.406 1
NotethatthesecondBayesnumeratoriscomputedbymultiplyingthefirstBayesnumerator
and the second likelihood; since we are only interested in the final posterior, there is no
need to normalize until the last step. As shown in the last column and plot, after two heads
the type C hypothesis has finally taken the lead!
18.05 Class 11, Bayesian Updating with Discrete Priors, Spring 2022 7
𝑝(𝜃) 𝑝(𝜃|𝑥=1) 𝑝(𝜃|𝑥 =1,𝑥 =1)
1 2
.4 .4 .4
.2 .2 .2
𝜃 𝜃 𝜃
.5.6 .9 .5.6 .9 .5.6 .9
prior𝑝(𝜃), firstposterior𝑝(𝜃|𝑥 = 1), secondposterior𝑝(𝜃|𝑥 = 1,𝑥 = 1)
1 1 2
5 Appendix: the base rate fallacy
Example 4. A screening test for a disease is both sensitive and specific. By that we mean
it is usually positive when testing a person with the disease and usually negative when
testing someone without the disease. Let’s assume the true positive rate is 99% and the
false positive rate is 2%. Suppose the prevalence of the disease in the general population is
0.5%. If a random person tests positive, what is the probability that they have the disease?
Solution: As a review we first do the computation using trees. Next we will redo the
computation using tables.
Let’s use notation established above for hypotheses and data: let ℋ be the hypothesis
+
(event)thatthepersonhasthediseaseandletℋ bethehypothesistheydonot. Likewise,
−
let 𝒯 and 𝒯 represent the data of a positive and negative screening test respectively. We
+ −
are asked to compute 𝑃(ℋ |𝒯 ).
+ +
We are given
𝑃(𝒯 |ℋ ) = 0.99, 𝑃(𝒯 |ℋ ) = 0.02, 𝑃(ℋ ) = 0.005.
+ + + − +
From these we can compute the false negative and true negative rates:
𝑃(𝒯 |ℋ ) = 0.01, 𝑃(𝒯 |ℋ ) = 0.98
− + − −
All of these probabilities can be displayed quite nicely in a tree.
0.005 0.995
ℋ ℋ
+ −
0.99 0.01 0.02 0.98
𝒯 𝒯 𝒯 𝒯
+ − + −
Bayes’ theorem yields
𝑃(𝒯 |ℋ )𝑃(ℋ ) 0.99⋅0.005
𝑃(ℋ |𝒯 ) = + + + = = 0.19920 ≈ 20%
+ + 𝑃(𝒯 ) 0.99⋅0.005+0.02⋅0.995
+
Now we redo this calculation using a Bayesian update table:
18.05 Class 11, Bayesian Updating with Discrete Priors, Spring 2022 8
Bayes
hypothesis prior likelihood numerator posterior
ℋ 𝑃(ℋ) 𝑃(𝒯 |ℋ) 𝑃(𝒯 |ℋ)𝑃(ℋ) 𝑃(ℋ|𝒯 )
+ + +
ℋ 0.005 0.99 0.00495 0.19920
+
ℋ 0.995 0.02 0.01990 0.80080
−
total 1 NO SUM 𝑃(𝒯 ) = 0.02485 1
+
The table shows that the posterior probability 𝑃(ℋ |𝒯 ) that a person with a positive
+ +
test has the disease is about 20%. This is far less than the sensitivity of the test (99%) but
much higher than the prevalence of the disease in the general population (0.5%).
Bayesian Updating: Probabilistic Prediction
Class 12, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to use the law of total probability to compute prior and posterior predictive
probabilities.
2 Introduction
In the previous class we looked at updating the probability of hypotheses based on data.
We can also use the data to update the probability of each possible outcome of a future
experiment. In this class we will look at how this is done.
2.1 Probabilistic prediciton; words of estimative probability (WEP)
There are many ways to word predictions:
• Prediction: “It will rain tomorrow.”
• Prediction using words of estimative probability (WEP): “It is likely to rain tomor-
row.”
• Probabilistic prediction: “Tomorrow it will rain with probability 60% (and not rain
with probability 40%).”
Each type of wording is appropriate at different times.
In this class we are going to focus on probabilistic prediction and precise quantitative state-
ments. Youcanseehttps://en.wikipedia.org/wiki/Words_of_Estimative_Probability
for an interesting discussion about the appropriate use of words of estimative probability.
The article also contains a list of weasel words such as ‘might’, ‘cannot rule out’, ‘it’s
conceivable’ that should be avoided as almost certain to cause confusion.
There are many places where we want to make a probabilistic prediction. Examples are
• Medical treatment outcomes
• Weather forecasting
• Climate change
• Sports betting
• Elections
• …
1
18.05 Class 12, Bayesian Updating: Probabilistic Prediction, Spring 2022 2
These are all situations where there is uncertainty about the outcome and we would like as
precise a description of what could happen as possible.
3 Predictive Probabilities
Probabilistic prediction simply means assigning a probability to each possible outcomes of
an experiment.
Recall the coin example from the previous class notes: there are three types of coins which
are indistinguishable apart from their probability of landing heads when tossed.
• Type 𝐴 coins are fair, with probability 0.5 of heads
• Type 𝐵 coins have probability 0.6 of heads
• Type 𝐶 coins have probability 0.9 of heads
You have a drawer containing 4 coins: 2 of type 𝐴, 1 of type 𝐵, and 1 of type 𝐶. You reach
into the drawer and pick a coin at random. We let 𝐴 stand for the event ‘the chosen coin
is of type 𝐴’. Likewise for 𝐵 and 𝐶.
3.1 Prior predictive probabilities
Before taking data we can compute the probability that our chosen coin will land heads (or
tails) if flipped. Let 𝐷 be the event it lands heads and let 𝐷 the event it lands tails. We
𝐻 𝑇
can use the law of total probability to determine the probabilities of these events. Either
by drawing a tree or directly proceeding to the algebra, we get:
0.5 0.25 0.25
𝐴 𝐵 𝐶 Coin type
0.5 0.5 0.6 0.4 0.9 0.1
Flip result
𝐷 𝐷 𝐷 𝐷 𝐷 𝐷
𝐻 𝑇 𝐻 𝑇 𝐻 𝑇
𝑃(𝐷 ) = 𝑃(𝐷 |𝐴)𝑃(𝐴)+𝑃(𝐷 |𝐵)𝑃(𝐵)+𝑃(𝐷 |𝐶)𝑃(𝐶)
𝐻 𝐻 𝐻 𝐻
= 0.5⋅0.5+0.6⋅0.25+0.9⋅0.25 = 0.625
𝑃(𝐷 ) = 𝑃(𝐷 |𝐴)𝑃(𝐴)+𝑃(𝐷 |𝐵)𝑃(𝐵)+𝑃(𝐷 |𝐶)𝑃(𝐶)
𝑇 𝑇 𝑇 𝑇
= 0.5⋅0.5+0.4⋅0.25+0.1⋅0.25 = 0.375
Definition: These probabilities give a (probabilistic) prediction of what will happen if the
coin is tossed. Because they are computed before we collect any data they are called prior
predictive probabilities.
3.2 Posterior predictive probabilities
Suppose we flip the coin once and it lands heads. We now have data 𝐷, which we can use
to update the prior probabilities of our hypotheses to posterior probabilities. Last class we
learned to use a Bayes table to facilitate this computation:
18.05 Class 12, Bayesian Updating: Probabilistic Prediction, Spring 2022 3
Bayes
hypothesis prior likelihood numerator posterior
𝐻 𝑃(𝐻) 𝑃(𝐷|𝐻) 𝑃(𝐷|𝐻)𝑃(𝐻) 𝑃(𝐻|𝐷)
𝐴 0.5 0.5 0.25 0.4
𝐵 0.25 0.6 0.15 0.24
𝐶 0.25 0.9 0.225 0.36
total 1 NO SUM 0.625 1
Having flipped the coin once and gotten heads, we can compute the probability that our
chosencoinwilllandheads(ortails)ifflippedasecondtime. Weproceedjustasbefore, but
usingtheposteriorprobabilities𝑃(𝐴|𝐷),𝑃(𝐵|𝐷),𝑃(𝐶|𝐷)inplaceofthepriorprobabilities
𝑃(𝐴), 𝑃(𝐵), 𝑃(𝐶).
0.4 0.24 0.36
𝐴 𝐵 𝐶 Coin type
0.5 0.5 0.6 0.4 0.9 0.1
Flip result
𝐷 𝐷 𝐷 𝐷 𝐷 𝐷
𝐻 𝑇 𝐻 𝑇 𝐻 𝑇
𝑃(𝐷 |𝐷) = 𝑃(𝐷 |𝐴)𝑃(𝐴|𝐷)+𝑃(𝐷 |𝐵)𝑃(𝐵|𝐷)+𝑃(𝐷 |𝐶)𝑃(𝐶|𝐷)
𝐻 𝐻 𝐻 𝐻
= 0.5⋅0.4+0.6⋅0.24+0.9⋅0.36 = 0.668
𝑃(𝐷 |𝐷) = 𝑃(𝐷 |𝐴)𝑃(𝐴|𝐷)+𝑃(𝐷 |𝐵)𝑃(𝐵|𝐷)+𝑃(𝐷 |𝐶)𝑃(𝐶|𝐷)
𝑇 𝑇 𝑇 𝑇
= 0.5⋅0.4+0.4⋅0.24+0.1⋅0.36 = 0.332
Definition: These probabilities give a (probabilistic) prediction of what will happen if the
coin is tossed again. Because they are computed after collecting data and updating the
prior to the posterior, they are called posterior predictive probabilities.
Note that heads on the first toss increases the probability of heads on the second toss.
3.3 Review
Here’s a succinct description of the preceding sections that may be helpful:
Each hypothesis gives a different probability of heads, so the total probability of heads is
a weighted average. For the prior predictive probability of heads, the weights are given by
the prior probabilities of the hypotheses. For the posterior predictive probability of heads,
the weights are given by the posterior probabilities of the hypotheses.
Remember: Prior and posterior probabilities are for hypotheses. Prior predictive and
posterior predictive probabilities are for outcomes. To keep this straight, remember that
the predictive probabilities are used to predict future outcomes, i.e. data.
Bayesian Updating: Odds
Class 12, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to convert between odds and probability.
2. Be able to update prior odds to posterior odds using Bayes factors.
3. Understand how Bayes factors measure the extent to which data provides evidence for
or against a hypothesis.
2 Odds
When comparing two events, it common to phrase probability statements in terms of odds.
DefinitionTheoddsofevent𝐸 versusevent𝐸′aretheratiooftheirprobabilities𝑃(𝐸)/𝑃(𝐸′).
If unspecified, the second event is assumed to be the complement 𝐸𝑐. So the odds of 𝐸 are:
𝑃(𝐸)
𝑂(𝐸) = .
𝑃(𝐸𝑐)
For example, 𝑂(rain) = 2 means that the probability of rain is twice the probability of no
rain (2/3 versus 1/3). We might say ‘the odds of rain are 2 to 1.’
1/2
Example. For a fair coin, 𝑂(heads) = = 1. We might say the odds of heads are 1 to
1/2
1 or fifty-fifty.
1/6 1
Example. For a standard die, the odds of rolling a 4 are = . We might say the odds
5/6 5
are ‘1 to 5 for’ or ‘5 to 1 against’ rolling a 4.
Example. The probability of a pair in a five card poker hand is 0.42257. So the odds of a
pair are 0.42257/(1-0.42257) = 0.73181.
We can go back and forth between probability and odds as follows.
𝑝 𝑞
Conversion formulas: if𝑃(𝐸) = 𝑝 then𝑂(𝐸) = . If𝑂(𝐸) = 𝑞 then𝑃(𝐸) = .
1−𝑝 1+𝑞
Notes:
1. The second formula simply solves 𝑞 = 𝑝/(1−𝑝) for 𝑝.
2. Probabilities are between 0 and 1, while odds are between 0 to ∞.
3. The property 𝑃(𝐸𝑐) = 1−𝑃(𝐸) becomes 𝑂(𝐸𝑐) = 1/𝑂(𝐸).
Example. Let 𝐹 be the event that a five card poker hand is a full house. Then 𝑃(𝐹) =
0.00145214 so 𝑂(𝐹) = 0.0014521/(1−0.0014521) = 0.0014542.
The odds not having a full house are 𝑂(𝐹𝑐) = (1−0.0014521)/0.0014521 = 687 = 1/𝑂(𝐹).
1
18.05 Class 12, Bayesian Updating: Odds, Spring 2022 2
4. If 𝑃(𝐸) or 𝑂(𝐸) is small then 𝑂(𝐸) ≈ 𝑃(𝐸). This follows from the conversion formulas.
Example. In the poker example where 𝐹 = ‘full house’ we saw that 𝑃(𝐹) and 𝑂(𝐹) differ
only in the fourth significant digit.
3 Updating odds
3.1 Introduction
In Bayesian updating, we used the likelihood of data to update prior probabilities of hy-
potheses to posterior probabilities. In the language of odds, we will update prior odds to
posterior odds. One of our key points will be that the data can provide evidence supporting
or negating a hypothesis depending on whether its posterior odds are greater or less than
its prior odds.
We’ll begin by returning to our familiar example of a screening test for a disease.
Example 1. Briefly, a screening test for a disease is both sensitive and specific. Assume
the true positive rate is 99% and the false positiverate is 2%. Suppose the prevalenceof the
disease in the general population is 0.5%. For a randomly chosen person, what are the prior
odds that they have the disease? Suppose they test positive, now what are the posterior
odds that they have the disease? By what factor have the odds changed as a result of the
test?
Solution: We’ll use our, by now, standard notation:
ℋ = have disease, ℋ = do not have disease, 𝒯 = test positive, 𝒯 = test negative.
+ − + −
To start with the prior odds that they have the disease are
𝑃(ℋ ) 0.005
𝑂(ℋ ) = + = ≈ 0.005
+ 𝑃(ℋ ) 0.995
−
For the posterior odds, we’ll do the computation with trees and then repeat it with tables.
Here is the tree describing the scenario.
0.005 0.995
ℋ ℋ
+ −
0.99 0.01 0.02 0.98
𝒯 𝒯 𝒯 𝒯
+ − + −
Bayes’ theorem yields
𝑃(ℋ |𝒯 ) 𝑃(𝒯 |ℋ )𝑃(ℋ )/𝑃(𝒯 ) 𝑃(𝒯 |ℋ )𝑃(ℋ )
𝑂(ℋ |𝒯 ) = + + = + + + + = + + +
+ + 𝑃(ℋ |𝒯 ) 𝑃(𝒯 |ℋ )𝑃(ℋ )/𝑃(𝒯 ) 𝑃(𝒯 |ℋ )𝑃(ℋ )
− + + − − + + − −
This is great! For the odds, the total probability 𝑃(𝒯 ) cancels and does not need to be
+
computed. Putting in numbers we see the posterior odds are
0.99⋅0.005
𝑂(ℋ |𝒯 ) = ≈ 50⋅0.005 = 1/4.
+ + 0.02⋅0.995
18.05 Class 12, Bayesian Updating: Odds, Spring 2022 3
We’ve structured the presentation so you can easily see that the posterior odds are only one
in four. However, the posterior odds are about a factor of 50 greater than the prior odds.
Redoing this calculation using a Bayesian update table:
Bayes
hypothesis prior likelihood numerator posterior
ℋ 𝑃(ℋ) 𝑃(𝒯 |ℋ) 𝑃(𝒯 |ℋ)𝑃(ℋ) 𝑃(ℋ|𝒯 )
+ + +
ℋ 0.005 0.99 0.00495 0.19920
+
ℋ 0.995 0.02 0.01990 0.80080
−
total 1 NO SUM 𝑃(𝒯 ) = 0.02485 1
+
The prior odds are computed using the prior column of the table. As above, they are
𝑃(ℋ ) 0.005
+ = .
𝑃(ℋ ) 0.995
−
The posterior odds are computed using either the posterior or Bayes numerator columns of
the table. We can use either column, because, they only differ by the normalazing factor of
𝑃(𝒯 ) in the denominator of the posteriors. We get the same answer as above:
+
0.00495 5
𝑂(ℋ |𝒯 ) = ≈ .
+ + 0.01990 20
You should see that these odds come by multiplying the prior odds by the ratio of the
likelihoods.
3.2 Example: Marfan syndrome
Marfan syndrome is a genetic disease of connective tissue that occurs in 1 of every 15000
people. The main ocular features of Marfan syndrome include bilateral ectopia lentis (lens
dislocation), myopia and retinal detachment. About 70% of people with Marfan syndrome
have a least one of these ocular features; only 7% of people without Marfan syndrome do.
(We don’t guarantee the accuracy of these numbers, but they will work perfectly well for
our example.)
If a person has at least one of these ocular features, what are the odds that they have
Marfan syndrome?
Solution: This is a standard Bayesian updating problem. Our hypotheses are:
𝑀 = ‘the person has Marfan syndrome’ 𝑀𝑐 = ‘the person does not have Marfan
syndrome’
The data is:
𝐹 = ‘the person has at least one ocular feature’.
We are given the prior probability of 𝑀 and the likelihoods of 𝐹 given 𝑀 or 𝑀𝑐:
𝑃(𝑀) = 1/15000, 𝑃(𝐹|𝑀) = 0.7, 𝑃(𝐹|𝑀𝑐) = 0.07.
As before, we can compute the posterior probabilities using a table:
18.05 Class 12, Bayesian Updating: Odds, Spring 2022 4
Bayes
hypothesis prior likelihood numerator posterior
𝐻 𝑃(𝐻) 𝑃(𝐹|𝐻) 𝑃(𝐹|𝐻)𝑃(𝐻) 𝑃(𝐻|𝐹)
𝑀 0.000067 0.7 0.0000467 0.00066
𝑀𝑐 0.999933 0.07 0.069995 0.99933
total 1 no sum 𝑃(𝐹) = 0.07004 1
First we find the prior odds:
𝑃(𝑀) 1/15000 1
𝑂(𝑀) = = = ≈ 0.000067.
𝑃(𝑀𝑐) 14999/15000 14999
The posterior odds are given by the ratio of the posterior probabilities or the Bayes numer-
ators, since the normalizing factor will be the same in both numerator and denominator.
𝑃(𝑀|𝐹) 𝑃(𝐹|𝑀)𝑃(𝑀)
𝑂(𝑀|𝐹) = = = 0.000667.
𝑃(𝑀𝑐|𝐹) 𝑃(𝐹|𝑀𝑐)𝑃(𝑀𝑐)
The posterior odds are a factor of 10 larger than the prior odds. In that sense, having an
ocular feature is strong evidence in favor of the hypothesis 𝑀. However, because the prior
odds are so small, it is still highly unlikely the person has Marfan syndrome.
4 Bayes factors and strength of evidence
The factor of 10 in the previous example is called a Bayes factor or a likelihood ratio. The
exact definition is the following.
Definition: Forahypothesis𝐻 anddata𝐷, theBayesfactoristheratioofthelikelihoods:
𝑃(𝐷|𝐻)
Bayes factor = .
𝑃(𝐷|𝐻𝑐)
This is also called the likelihood ratio.
Let’s see exactly where the Bayes factor arises in updating odds. We have
𝑃(𝐻|𝐷)
𝑂(𝐻|𝐷) =
𝑃(𝐻𝑐|𝐷)
𝑃(𝐷|𝐻)𝑃(𝐻)
=
𝑃(𝐷|𝐻𝑐)𝑃(𝐻𝑐)
𝑃(𝐷|𝐻) 𝑃(𝐻)
= ⋅
𝑃(𝐷|𝐻𝑐) 𝑃(𝐻𝑐)
𝑃(𝐷|𝐻)
= ⋅ 𝑂(𝐻)
𝑃(𝐷|𝐻𝑐)
posterior odds = Bayes factor × prior odds
From this formula, we see that the Bayes’ factor (𝐵𝐹) tells us whether the data provides
evidence for or against the hypothesis.
18.05 Class 12, Bayesian Updating: Odds, Spring 2022 5
• If 𝐵𝐹 > 1 then the posterior odds are greater than the prior odds. So the data
provides evidence for the hypothesis.
• If 𝐵𝐹 < 1 then the posterior odds are less than the prior odds. So the data provides
evidence against the hypothesis.
• If 𝐵𝐹 = 1 then the prior and posterior odds are equal. So the data provides no
evidence either way.
The following example is taken from the textbook Information Theory, Inference, and
Learning Algorithms by David J. C. Mackay, who has this to say regarding trial evidence.
In my view, a jury’s task should generally be to multiply together carefully
evaluated likelihood ratios from each independent piece of admissible evidence
withanequallycarefullyreasonedpriorprobability. Thisviewissharedbymany
statisticians but learned British appeal judges recently disagreed and actually
overturnedtheverdictofatrialbecausethejurorshad beentaughttouseBayes’
theorem to handle complicated DNA evidence.
Example 2. Two people have left traces of their own blood at the scene of a crime. A
suspect , Oliver, is tested and found to have type ‘O’ blood. The blood groups of the two
traces are found to be of type ‘O’ (a common type in the local population, having frequency
60%) and type ‘AB’ (a rare type, with frequency 1%). Does this data (type ‘O’ and ‘AB’
blood were found at the scene) give evidence in favor of the proposition that Oliver was one
of the two people present at the scene of the crime?”
Solution: There are two hypotheses:
𝑆 = ‘Oliver and another unknown person were at the scene of the crime
𝑆𝑐 = ‘two unknown people were at the scene of the crime’
The data is:
𝐷 = ‘type ‘O’ and ‘AB’ blood were found’
𝑃(𝐷|𝑆)
The Bayes factor for Oliver’s presence is 𝐵𝐹 = . We compute the numerator
Oliver 𝑃(𝐷|𝑆𝑐)
and denominator of this separately.
The data says that both type O and type AB blood were found. If Oliver was at the scene
then ‘type O’ blood would be there. So 𝑃(𝐷|𝑆) is the probability that the other person
had type AB blood. We are told this is 0.01, so 𝑃(𝐷|𝑆) = 0.01.
If Oliver was not at the scene then there were two random people one with type O and
one with type AB blood. The probability of this is 2⋅0.6⋅0.01.* Thus the Bayes factor for
Oliver’s presence is
𝑃(𝐷|𝑆) 0.01
𝐵𝐹 = = = 0.83.
Oliver 𝑃(𝐷|𝑆𝑐) 2⋅0.6⋅0.01
Since 𝐵𝐹 < 1, the data provides (weak) evidence against Oliver being at the scene.
Oliver
*Thefactorof2is,perhapssurprising. Thefollowingcarefulcountingwillexplainit. Supposethere
are 𝑁 people in the population, 𝑁 have type O blood and 𝑁 have type AB. So 𝑁 /𝑁 = 0.6
𝑂 𝐴𝐵 𝑂
18.05 Class 12, Bayesian Updating: Odds, Spring 2022 6
and𝑁 /𝑁 =0.01. Wewantthe probabilitythat arandom choiceof2 peoplewill pickoneof type
𝐴𝐵
O and one of type AB. This is clearly
(𝑁 𝑂)(𝑁 𝐴𝐵) 𝑁 𝑁 𝑁 𝑁
1 1 = 𝑂 𝐴𝐵 =2⋅ 𝑂 ⋅ 𝐴𝐵 ≈2⋅0.6⋅0.01.
(𝑁) 𝑁(𝑁 −1)/2 𝑁 𝑁 −1
2
In the last approximation, we assumed that 𝑁 is large enough the 𝑁 /(𝑁 −1)≈𝑁 /𝑁.
𝐴𝐵 𝐴𝐵
Example 3. Another suspect Alberto is found to have type ‘AB’ blood. Do the same data
give evidence in favor of the proposition that Alberto was one of the two people present at
the crime?
Solution: Reusing the above notation with Alberto in place of Oliver we have:
𝑃(𝐷|𝑆) 0.6
𝐵𝐹 = = = 50.
Alberto 𝑃(𝐷|𝑆𝑐) 2⋅0.6⋅0.01
Since 𝐵𝐹 ≫ 1, the data provides strong evidence in favor of Alberto being at the
Alberto
scene.
Notes:
1. In both examples, we have only computed the Bayes factor, not the posterior odds. To
compute the latter, we would need to know the prior odds that Oliver (or Alberto) was at
the scene based on other evidence.
2. Note that if 50% of the population had type O blood instead of 60%, then the Oliver’s
Bayes factor would be 1 (neither for nor against). More generally, the break-even point
for blood type evidence is when the proportion of the suspect’s blood type in the general
population equals the proportion of the suspect’s blood type among those who left blood
at the scene.
4.1 Updating again and again
Suppose we collect data in two stages, first 𝐷 , then 𝐷 . We have seen in our dice and coin
1 2
examples that the final posterior can be computed all at once or in two stages where we
first update the prior using the likelihoods for 𝐷 and then update the resulting posterior
1
using the likelihoods for 𝐷 . The latter approach works whenever likelihoods multiply:
2
𝑃(𝐷 ,𝐷 |𝐻) = 𝑃(𝐷 |𝐻)𝑃(𝐷 |𝐻).
1 2 1 2
Since likelihoods are conditioned on hypotheses, we say that 𝐷 and 𝐷 are conditionally
1 2
independent if the above equation holds for every hypothesis 𝐻.
Example. There are five dice in a drawer, with 4, 6, 8, 12, and 20 sides (these are the
hypotheses). I pick a die at random and roll it twice. The first roll gives 7. The second roll
gives 11. Are these results conditionally independent? Are they independent?
Solution: These results are conditionally independent. For example, for the hypothesis of
the 8-sided die we have:
𝑃(7 on roll 1|8-sided die) = 1/8
𝑃(11 on roll 2|8-sided die) = 0
𝑃(7 on roll 1, 11 on roll 2|8-sided die) = 0
18.05 Class 12, Bayesian Updating: Odds, Spring 2022 7
For the hypothesis of the 20-sided die we have:
𝑃(7 on roll 1|20-sided die) = 1/20
𝑃(11 on roll 2|20-sided die) = 1/20
𝑃(7 on roll 1, 11 on roll 2|20-sided die) = (1/20)2
However, the results of the rolls are not independent. That is:
𝑃(7 on roll 1, 11 on roll 2) ≠ 𝑃(7 on roll 1)𝑃(11 on roll 2).
Intuitively, this is because a 7 on the roll 1 allows us to rule out the 4- and 6-sided dice,
making an 11 on roll 2 more likely. Let’s check this intuition by computing both sides
precisely. On the righthand side we have:
1 1 1 1 1 1 31
𝑃(7 on roll 1) = ⋅ + ⋅ + ⋅ =
5 8 5 12 5 20 600
1 1 1 1 2
𝑃(11 on roll 2) = ⋅ + ⋅ =
5 12 5 20 75
On the lefthand side we have:
𝑃(7 on roll 1, 11 on roll 2) = 𝑃(11 on roll 2|7 on roll 1)𝑃(7 on roll 1)
30 1 6 1 31
= ( ⋅ + ⋅ )⋅
93 12 31 20 600
17 31 17
= ⋅ =
465 600 9000
Here 30 and 6 are the posterior probabilities of the 12- and 20-sided dice given a 7 on roll
93 31
1. We conclude that, without conditioning on hypotheses, the rolls are not independent.
Returning the to general setup, if 𝐷 and 𝐷 are conditionally independent for 𝐻 and 𝐻𝑐
1 2
then it makes sense to consider each Bayes factor independently:
𝑃(𝐷 |𝐻)
𝐵𝐹 = 𝑖 .
𝑖 𝑃(𝐷 |𝐻𝑐)
𝑖
The prior odds of 𝐻 are 𝑂(𝐻). The posterior odds after 𝐷 are
1
𝑂(𝐻|𝐷 ) = 𝐵𝐹 ⋅𝑂(𝐻).
1 1
And the posterior odds after 𝐷 and 𝐷 are
1 2
𝑂(𝐻|𝐷 ,𝐷 ) = 𝐵𝐹 ⋅𝑂(𝐻|𝐷 )
1 2 2 1
= 𝐵𝐹 ⋅𝐵𝐹 ⋅𝑂(𝐻)
2 1
We have the beautifully simple notion that updating with new data just amounts to mul-
tiplying the current posterior odds by the Bayes factor of the new data.
Example 4. Other symptoms of Marfan Syndrome
Recall from the earlier example that the Bayes factor for a least one ocular feature (𝐹) is
𝑃(𝐹|𝑀) 0.7
𝐵𝐹 = = = 10.
𝐹 𝑃(𝐹|𝑀𝑐) 0.07
18.05 Class 12, Bayesian Updating: Odds, Spring 2022 8
The wrist sign (𝑊) is the ability to wrap one hand around your other wrist to cover your
pinky nail with your thumb. Assume 10% of the population have the wrist sign, while 90%
of people with Marfan’s have it. Therefore the Bayes factor for the wrist sign is
𝑃(𝑊|𝑀) 0.9
𝐵𝐹 = = = 9.
𝑊 𝑃(𝑊|𝑀𝑐) 0.1
We will assume that 𝐹 and 𝑊 are conditionally independent symptoms. That is, among
people with Marfan syndrome, ocular features and the wrist sign are independent, and
amongpeoplewithoutMarfansyndrome,ocularfeaturesandthewristsignareindependent.
Given this assumption, the posterior odds of Marfan syndrome for someone with both an
ocular feature and the wrist sign are
1 6
𝑂(𝑀|𝐹,𝑊) = 𝐵𝐹 ⋅𝐵𝐹 ⋅𝑂(𝑀) = 9⋅10⋅ ≈ .
𝑊 𝐹 14999 1000
We can convert the posterior odds back to probability, but since the odds are so small the
result is nearly the same:
6
𝑃(𝑀|𝐹,𝑊) ≈ ≈ 0.596%.
1000+6
So ocular features and the wrist sign are both strong evidence in favor of the hypothesis
𝑀, and taken together they are very strong evidence. Again, because the prior odds are so
small, it is still unlikely that the person has Marfan syndrome, but at this point it might be
worth undergoing further testing given potentially fatal consequences of the disease (such
as aortic aneurysm or dissection).
Note also that if a person has exactly one of the two symptoms, then the product of the
Bayes factors is near 1 (either 9/10 or 10/9). So the two pieces of data essentially cancel
each other out with regard to the evidence they provide for Marfan’s syndrome.
5 Log odds
In practice, people often find it convenient to work with the natural log of the odds in place
of odds. Naturally enough these are called the log odds. The Bayesian update formula
𝑂(𝐻|𝐷 ,𝐷 ) = 𝐵𝐹 ⋅𝐵𝐹 ⋅𝑂(𝐻)
1 2 2 1
becomes
ln(𝑂(𝐻|𝐷 ,𝐷 )) = ln(𝐵𝐹 )+ln(𝐵𝐹 )+ln(𝑂(𝐻)).
1 2 2 1
We can interpret the above formula for the posterior log odds as the sum of the prior log
odds and all the evidence ln(𝐵𝐹 ) provided by the data. Note that by taking logs, evidence
𝑖
in favor (𝐵𝐹 > 1) is positive and evidence against (𝐵𝐹 < 1) is negative.
𝑖 𝑖
Toavoidlengthiercomputations, wewillworkwithoddsratherthanlogoddsinthiscourse.
Logoddsarenicebecausesumsareoftenmoreintuitivethenproducts. Logoddsalsoplaya
centralrole in logistic regression, an importantstatistical model related to linear regression.
Bayesian Updating with Continuous Priors
Class 13, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Understand a parameterized family of distributions as representing a continuous range
of hypotheses for the observed data.
2. Be able to state Bayes’ theorem and the law of total probability for continous densities.
3. Be able to apply Bayes’ theorem to update a prior probability density function to a
posterior pdf given data and a likelihood function.
4. Be able to interpret and compute posterior predictive probabilities.
2 Introduction
UptonowwehaveonlydoneBayesianupdatingwhenwehadafinitenumberofhypothesis,
e.g. our dice example had five hypotheses (4, 6, 8, 12 or 20 sides). Now we will study
Bayesian updating when there is a continuous range of hypotheses. The Bayesian update
process will be essentially the same as in the discrete case. As usual when moving from
discretetocontinuouswewill needtoreplacetheprobabilitymassfunctionbya probability
density function, and sums by integrals.
The first few sections of this note are devoted to working with pdfs. In particular we will
cover the law of total probability and Bayes’ theorem. We encourage you to focus on how
these are essentially identical to the discrete versions. After that, we will apply Bayes’
theorem and the law of total probability to Bayesian updating.
3 Examples with continuous ranges of hypotheses
Here are three standard examples with continuous ranges of hypotheses.
Example 1. Suppose you have a system that can succeed or fail with probability 𝑝. Then
we can hypothesize that 𝑝 is anywhere in the range [0,1]. That is, we have a continuous
range of hypotheses. We will often model this example with a ‘bent’ coin with unknown
probability 𝑝 of heads.
Example 2. The lifetime of a certain isotope is modeled by an exponential distribution
exp(𝜆). In principle, the mean lifetime 1/𝜆 can be any real number in (0,∞).
Example 3. We are not restricted to a single parameter. In principle, the parameters 𝜇
and𝜎ofanormaldistributioncanbeanyrealnumbersin(−∞,∞)and(0,∞),respectively.
If we model gestational length for single births by a normal distribution, then from millions
of data points we know that 𝜇 is about 40 weeks and 𝜎 is about one week.
1
18.05 Class 13, Bayesian Updating with Continuous Priors, Spring 2022 2
In all of these examples we modeled the random process giving rise to the data by a distri-
bution with parameters –called a parametrized distribution. Every possible choice of the
parameter(s) is a hypothesis, e.g. we can hypothesize that the probability of succcess in
Example 1 is 𝑝 = 0.7313. We have a continuous set of hypotheses because we could take
any value between 0 and 1.
4 Notational conventions
4.1 Parametrized models
As in the examples above our hypotheses often take the form a certain parameter has value
𝜃. We will often use the letter 𝜃 to stand for an arbitrary hypothesis. This will leave
symbols like 𝑝, 𝑓, and 𝑥 to take there usual meanings as pmf, pdf, and data. Also, rather
than saying ‘the hypothesis that the parameter of interest has value 𝜃’ we will simply say
the hypothesis 𝜃.
4.2 Big and little letters
We have two parallel notations for outcomes and probability:
1. (Big letters) Event 𝐴, probability function 𝑃(𝐴).
2. (Little letters) Value 𝑥, pmf 𝑝(𝑥) or pdf 𝑓(𝑥).
These notations are related by 𝑃(𝑋 = 𝑥) = 𝑝(𝑥), where 𝑥 is a value the discrete random
variable 𝑋 and ‘𝑋 = 𝑥’ is the corresponding event.
We carry these notations over to the probabilities used in Bayesian updating.
1. (Bigletters)Fromhypothesesℋanddata𝒟wecomputeseveralassociatedprobabilities
𝑃(ℋ), 𝑃(𝒟), 𝑃(ℋ|𝒟), 𝑃(𝒟|ℋ).
In the coin example we might have ℋ = ‘the chosen coin has probability 0.6 of heads’,
0.6
𝒟 = ‘3 flips landed HHT’, so 𝑃(𝒟|ℋ ) = (0.6)2(0.4)
0.6
2. (Small letters) Hypothesis values 𝜃 and data values 𝑥 both have probabilities or proba-
bility densities:
𝑝(𝜃) 𝑝(𝑥) 𝑝(𝜃|𝑥) 𝑝(𝑥|𝜃)
𝑓(𝜃) 𝑓(𝑥) 𝑓(𝜃|𝑥) 𝑓(𝑥|𝜃)
In the coin example we might have 𝜃 = 0.6 and 𝑥 is the sequence 1,1,0. So, 𝑝(𝑥|𝜃) =
(0.6)2(0.4). We might also write 𝑝(𝑥 = 1,1,0|𝜃 = 0.6) to emphasize the values of 𝑥 and 𝜃.
Although we will still use both types of notation, from now on we will mostly use the small
letter notation involving pmfs and pdfs. Hypotheses will usually be parameters represented
by Greek letters (𝜃,𝜆,𝜇,𝜎,…) while data values will usually be represented by English
letters (𝑥,𝑥 ,𝑦,…).
𝑖
18.05 Class 13, Bayesian Updating with Continuous Priors, Spring 2022 3
5 Quick review of pdf and probability
Suppose 𝑋 is a random variable with pdf 𝑓(𝑥). Recall 𝑓(𝑥) is a density; its units are
probability/(units of 𝑥).
𝑓(𝑥) 𝑓(𝑥)
probability𝑓(𝑥)𝑑𝑥
𝑃(𝑐≤𝑋≤𝑑)
𝑐 𝑑 𝑥 𝑑 𝑥 𝑥 𝑥
The probability that the value of 𝑋 is in [𝑐,𝑑] is given by
𝑑
∫ 𝑓(𝑥)𝑑𝑥.
𝑐
The probability that 𝑋 is in an infinitesimal range 𝑑𝑥 around 𝑥 is 𝑓(𝑥)𝑑𝑥. In fact, the
integral formula is just the ‘sum’ of these infinitesimal probabilities. We can visualize these
probabilities by viewing the integral as area under the graph of 𝑓(𝑥).
In order to manipulate probabilities instead of densities in what follows, we will make
frequent use of the notion that 𝑓(𝑥)𝑑𝑥 is the probability that 𝑋 is in an infinitesimal range
around 𝑥 of width 𝑑𝑥. Please make sure that you fully understand this notion.
6 Continuous priors, discrete likelihoods
In the Bayesian framework we have probabilities of hypotheses –called prior and posterior
probabilities– and probabilities of data given a hypothesis –called likelihoods. In earlier
classes both the hypotheses and the data had discrete ranges of values. We saw in the
introduction that we might have a continuous range of hypotheses. The same is true for
the data, but for today we will assume that our data can only take a discrete set of values.
In this case, the likelihood of data 𝑥 given hypothesis 𝜃 is written using a pmf: 𝑝(𝑥|𝜃).
We will use the following coin example to explain these notions. We will carry this example
through in each of the succeeding sections.
Example 4. Suppose we have a bent coin with unknown probability 𝜃 of heads. In this
case, we’ll say the coin is of ’type 𝜃’ and we’ll label the hypothesis that a random coin is
of type 𝜃 by ℋ . The value of 𝜃 is random and could be anywhere between 0 and 1. For
𝜃
this and the examples that follow we’ll suppose that the value of 𝜃 follows a distribution
with continuous prior probability density 𝑓(𝜃) = 2𝜃. We have a discrete likelihood because
tossing a coin has only two outcomes, 𝑥 = 1 for heads and 𝑥 = 0 for tails.
𝑝(𝑥 = 1|ℋ ) = 𝜃, 𝑝(𝑥 = 0|ℋ ) = 1−𝜃.
𝜃 𝜃
As we stated earlier, we will often write 𝜃 for the hypothesis ℋ . So the above probabilities
𝜃
become
𝑝(𝑥 = 1|𝜃) = 𝜃, 𝑝(𝑥 = 0|𝜃) = 1−𝜃.
18.05 Class 13, Bayesian Updating with Continuous Priors, Spring 2022 4
Think: This can be tricky to wrap your mind around. We have a continuous range of
types of coins –we identify the type by the value of the parameter 𝜃. We are able to choose
a coin at random and the type chosen has a probability density 𝑓(𝜃).
It may help to see that the discrete examples we did in previous classes are similar. In one
example, we had three types of coin with probability of heads 0.5, 0.6, or 0.9. So, we called
our hypotheses 𝐻 , 𝐻 , 𝐻 and these had prior probabilities 𝑃(𝐻 ) etc. In other
0.5 0.6 0.9 0.5
words, we had a type of coin with an unknown probability of heads, we had hypotheses
about that probability and each of these hypotheses had a prior probability.
7 The law of total probability
The law of total probability for continuous probability distributions is essentially the same
as for discrete distributions. We replace the prior pmf by a prior pdf and the sum by an
integral. We start by reviewing the law for the discrete case.
Recall that for a discrete set of hypotheses ℋ ,ℋ ,…ℋ the law of total probability says
1 2 𝑛
𝑛
𝑃(𝒟) = ∑𝑃(𝒟|ℋ )𝑃(ℋ ). (1)
𝑖 𝑖
𝑖=1
This is the total prior probability of 𝒟 because we used the prior probabilities 𝑃(ℋ )
𝑖
In the little letter notation with 𝜃 ,𝜃 ,…,𝜃 for hypotheses and 𝑥 for data the law of total
1 2 𝑛
probability is written
𝑛
𝑝(𝑥) = ∑𝑝(𝑥|𝜃 )𝑝(𝜃 ). (2)
𝑖 𝑖
𝑖=1
We also called this the prior predictive probability of the outcome 𝑥 to distinguish it from
the prior probability of the hypothesis 𝜃.
Likewise, there is a law of total probability for continuous pdfs. We state it as a theorem
using little letter notation.
Theorem. Law of total probability. Suppose we have a continuous parameter 𝜃 in the
range [𝑎,𝑏], and discrete random data 𝑥. Assume 𝜃 is itself random with density 𝑓(𝜃) and
that 𝑥 and 𝜃 have likelihood 𝑝(𝑥|𝜃). In this case, the total probability of 𝑥 is given by the
formula.
𝑏
𝑝(𝑥) = ∫ 𝑝(𝑥|𝜃)𝑓(𝜃)𝑑𝜃 (3)
𝑎
Proof. Ourproofwillbebyanalogytothediscreteversion: Theprobabilityterm𝑝(𝑥|𝜃)𝑓(𝜃)𝑑𝜃
is perfectly analogous to the term 𝑝(𝑥|𝜃 )𝑝(𝜃 ) in Equation 2 (or the term 𝑃(𝒟|ℋ )𝑃(ℋ )
𝑖 𝑖 𝑖 𝑖
in Equation 1). Continuing the analogy: the sum in Equation 2 becomes the integral in
Equation 3
As in the discrete case, when we think of 𝜃 as a hypothesis explaining the probability of the
data we call 𝑝(𝑥) the prior predictive probability for 𝑥.
Example 5. (Law of total probability.) Continuing with Example 4. We have a bent coin
with probability 𝜃 of heads. The value of 𝜃 is random with prior pdf 𝑓(𝜃) = 2𝜃 on [0,1].
18.05 Class 13, Bayesian Updating with Continuous Priors, Spring 2022 5
Suppose I am about to flip the coin. What is the total probability of heads, i.e what is the
prior predictive probability of heads?
Solution: In Example 4 we noted that the likelihoods are 𝑝(𝑥 = 1|𝜃) = 𝜃 and 𝑝(𝑥 = 0|𝜃) =
1−𝜃. So the total probability of 𝑥 = 1 is
1 1 1 2
𝑝(𝑥 = 1) = ∫ 𝑝(𝑥 = 1|𝜃)𝑓(𝜃)𝑑𝜃 = ∫ 𝜃⋅2𝜃𝑑𝜃 = ∫ 2𝜃2𝑑𝜃 = .
3
0 0 0
Since the prior is weighted towards higher probabilities of heads, so is the total probability
of heads.
8 Bayes’ theorem for continuous probability densities
ThestatementofBayes’theoremforcontinuouspdfsisessentiallyidenticaltothestatement
for pmfs. We state it including 𝑑𝜃 so we have genuine probabilities:
Theorem. Bayes’ Theorem. Use the same assumptions as in the law of total probability,
i.e. 𝜃 is a continuous parameter with pdf 𝑓(𝜃) and range [𝑎,𝑏]; 𝑥 is random discrete data;
together they have likelihood 𝑝(𝑥|𝜃). With these assumptions:
𝑝(𝑥|𝜃)𝑓(𝜃)𝑑𝜃 𝑝(𝑥|𝜃)𝑓(𝜃)𝑑𝜃
𝑓(𝜃|𝑥)𝑑𝜃 = = . (4)
𝑝(𝑥) 𝑏
∫ 𝑝(𝑥|𝜃)𝑓(𝜃)𝑑𝜃
𝑎
Proof. Since this is a statement about probabilities it is just the usual statement of Bayes’
theorem. We hope this is clear.
It is important enough to spell out somewhat formally: Let Θ be the random variable that
produces the value 𝜃. Consider the events
ℋ = ‘Θ is in an interval of width 𝑑𝜃 around the value 𝜃’
and
𝒟 = ‘the value of the data is 𝑥’.
Then 𝑃(ℋ) = 𝑓(𝜃)𝑑𝜃, 𝑃(𝒟) = 𝑝(𝑥), and 𝑃(𝒟|ℋ) = 𝑝(𝑥|𝜃). Now our usual form of
Bayes’ theorem becomes
𝑃(𝒟|ℋ)𝑃(ℋ) 𝑝(𝑥|𝜃)𝑓(𝜃)𝑑𝜃
𝑓(𝜃|𝑥)𝑑𝜃 = 𝑃(ℋ|𝒟) = =
𝑃(𝒟) 𝑝(𝑥)
Looking at the first and last terms in this equation we see the new form of Bayes’ theorem.
Finally, we firmly believe that it is more conducive to careful thinking about probability
to keep the factor of 𝑑𝜃 in the statement of Bayes’ theorem. But because it appears in the
numerator on both sides of Equation 4 many people drop the 𝑑𝜃 and write Bayes’ theorem
in terms of densities as
𝑝(𝑥|𝜃)𝑓(𝜃) 𝑝(𝑥|𝜃)𝑓(𝜃)
𝑓(𝜃|𝑥) = = .
𝑝(𝑥) 𝑏
∫ 𝑝(𝑥|𝜃)𝑓(𝜃)𝑑𝜃
𝑎
18.05 Class 13, Bayesian Updating with Continuous Priors, Spring 2022 6
9 Bayesian updating with continuous priors
Now that we have Bayes’ theorem and the law of total probability we can finally get to
Bayesian updating. Before continuing with Example 4, we point out two features of the
Bayesian updating table that appears in the next example:
1. The table for continuous priors is very simple: since we cannot have a row for each of
an infinite number of hypotheses we’ll have just one row which uses a variable to stand for
all hypotheses ℋ .
𝜃
2. Byincluding𝑑𝜃, alltheentriesinthetableareprobabilitiesandallourusualprobability
rules apply.
Example 6. (Bayesian updating.) Continuing Examples 4 and 5. We have a bent coin
with unknown probability 𝜃 of heads. The value of 𝜃 is random with prior pdf 𝑓(𝜃) = 2𝜃.
Suppose we flip the coin three times and get the sequence 𝐻𝑇𝑇. Compute the posterior
pdf for 𝜃.
Solution: We make the usual update table, with an added column giving the range of
values that 𝜃 can take. We make the first row an abstract version of Bayesian updating and
the second row is Bayesian updating for this particular example. In later examples we will
skip that abstract version.
hypothesis range prior likelihood Bayes posterior
numerator
ℋ 𝜃 range 𝑓(𝜃)𝑑𝜃 𝑝(𝑥 = 1,1,0|𝜃) 𝑝(𝑥 = 1,1,0|𝜃)𝑓(𝜃)𝑑𝜃 𝑓(𝜃|𝑥 = 1,1,0)𝑑𝜃
𝜃
ℋ [0,1] 2𝜃𝑑𝜃 𝜃2(1−𝜃) 2𝜃3(1−𝜃)𝑑𝜃 20𝜃3(1−𝜃)𝑑𝜃
𝜃
𝑝(𝑥 = 1,1,0)
𝑏
total [0,1] ∫ 𝑓(𝜃)𝑑𝜃 = 1 no sum 1
𝑎 = ∫ 1 2𝜃3(1−𝜃)𝑑𝜃 = 1/10
0
Therefore the posterior pdf (after seeing HHT) is 𝑓(𝜃|𝑥) = 20𝜃3(1−𝜃) .
We have a number of comments:
1. Since we used the prior probability 𝑓(𝜃)𝑑𝜃, the hypothesis should have been:
’the unknown paremeter is in an interval of width 𝑑𝜃 around 𝜃’.
Even for us that is too much to write, so you will have to think it everytime we write that
the hypothesis is 𝜃 or ℋ .
𝜃
2. The posterior pdf for 𝜃 is found by removing the 𝑑𝜃 from the posterior probability in
the table.
𝑓(𝜃|𝑥) = 20𝜃3(1−𝜃).
3. (i) As always 𝑝(𝑥) is the total probability. Since we have a continuous distribution
instead of a sum we compute an integral.
(ii) Notice that by including 𝑑𝜃 in the table, it is clear what integral we need to compute
to find the total probability 𝑝(𝑥).
4. The table organizes the continuous version of Bayes’ theorem. Namely, the posterior pdf
18.05 Class 13, Bayesian Updating with Continuous Priors, Spring 2022 7
is related to the prior pdf and likelihood function via:
𝑝(𝑥|𝜃)𝑓(𝜃)𝑑𝜃 𝑝(𝑥|𝜃)𝑓(𝜃)
𝑓(𝜃|𝑥)𝑑𝜃 = = 𝑑𝜃
𝑏 𝑝(𝑥)
∫ 𝑝(𝑥|𝜃)𝑓(𝜃)𝑑𝜃
𝑎
Removingthe𝑑𝜃 inthenumeratorofbothsideswehavethestatementintermsofdensities.
5. Regarding both sides as functions of 𝜃, we can again express Bayes’ theorem in the form:
𝑓(𝜃|𝑥) ∝ 𝑝(𝑥|𝜃)⋅𝑓(𝜃)
posterior ∝ likelihood × prior.
9.1 Flat priors
One important prior is called a flat or uniform prior. A flat prior assumes that every
hypothesis is equally probable. For example, if 𝜃 has range [0,1] then 𝑓(𝜃) = 1 is a flat
prior.
Example 7. (Flat priors.) We have a bent coin with unknown probability 𝜃 of heads.
Supposewetossitonceandgetheads. Assumeaflatpriorandfindtheposteriorprobability
for 𝜃.
Solution: This is similar Example 6 with a different prior and data.
hypothesis range prior likelihood Bayes numerator posterior
𝜃 𝜃 𝑓(𝜃)𝑑𝜃 𝑝(𝑥 = 1|𝜃) 𝑓(𝜃|𝑥 = 1)𝑑𝜃
𝜃 [0,1] 1⋅𝑑𝜃 𝜃 𝜃𝑑𝜃 2𝜃𝑑𝜃
1
𝑏
total [0,1] ∫ 𝑓(𝜃)𝑑𝜃 = 1 no sum 𝑝(𝑥 = 1) = ∫ 𝜃𝑑𝜃 = 1/2 1
𝑎
0
9.2 Using the posterior pdf
Example 8. In the previous example the prior probability was flat. First show that this
means that a priori the coin is equally like to be biased towards heads or tails. Then, after
observing one heads, what is the (posterior) probability that the coin is biased towards
heads?
Solution: Sincetheparameter𝜃 istheprobabilitythecoinlandsheads, thefirstpartofthe
problem asks us to show 𝑃(𝜃 > 0.5) = 0.5 and the second part asks for 𝑃(𝜃 > 0.5|𝑥 = 1).
These are easily computed from the prior and posterior pdfs respectively.
The prior probability that the coin is biased towards heads is
1 1 1
1
𝑃(𝜃 > 0.5) = ∫ 𝑓(𝜃)𝑑𝜃 = ∫ 1⋅𝑑𝜃 = 𝜃| = .
0.5 2
0.5 0.5
The probability of 1/2 means the coin is equally likely to be biased toward heads or tails.
The posterior probabilitiy that it’s biased towards heads is
1 1 1 3
𝑃(𝜃 > 0.5|𝑥 = 1) = ∫ 𝑓(𝜃|𝑥 = 1)𝑑𝜃 = ∫ 2𝜃𝑑𝜃 = 𝜃2∣ = .
0.5 4
0.5 0.5
18.05 Class 13, Bayesian Updating with Continuous Priors, Spring 2022 8
Weseethatobservingoneheadshasincreasedtheprobabilitythatthecoinisbiasedtowards
heads from 1/2 to 3/4.
10 Predictive probabilities
Just as in the discrete case we are also interested in using the posterior probabilities of the
hypotheses to make predictions for what will happen next.
Example 9. (Prior and posterior prediction.) Continuing Examples 4, 5, 6: we have a
coin with unknown probability 𝜃 of heads and the value of 𝜃 has prior pdf 𝑓(𝜃) = 2𝜃. Find
the prior predictive probability of heads. Then suppose the first flip was heads and find the
posterior predictive probabilities of both heads and tails on the second flip.
Solution: For notation let 𝑥 be the result of the first flip and let 𝑥 be the result of the
1 2
second flip. The prior predictive probability is exactly the total probability computed in
Examples 5 and 6.
1 1 2
𝑝(𝑥 = 1) = ∫ 𝑝(𝑥 = 1|𝜃)𝑓(𝜃)𝑑𝜃 = ∫ 2𝜃2𝑑𝜃 = .
1 1 3
0 0
The posterior predictive probabilities are the total probabilities computed using the poste-
rior pdf. From Example 6 we know the posterior pdf is 𝑓(𝜃|𝑥 = 1) = 3𝜃2. So the posterior
1
predictive probabilities are
1 1
𝑝(𝑥 = 1|𝑥 = 1) = ∫ 𝑝(𝑥 = 1|𝜃,𝑥 = 1)𝑓(𝜃|𝑥 = 1)𝑑𝜃 = ∫ 𝜃⋅3𝜃2𝑑𝜃 = 3/4
2 1 2 1 1
0 0
1 1
𝑝(𝑥 = 0|𝑥 = 1) = ∫ 𝑝(𝑥 = 0|𝜃,𝑥 = 1)𝑓(𝜃|𝑥 = 1)𝑑𝜃 = ∫ (1−𝜃)⋅3𝜃2𝑑𝜃 = 1/4
2 1 2 1 1
0 0
(More simply, we could have computed 𝑝(𝑥 = 0|𝑥 = 1) = 1−𝑝(𝑥 = 1|𝑥 = 1) = 1/4.)
2 1 2 1
11 (Optional) From discrete to continuous Bayesian updat-
ing
Thissectionisoptional. Initwewilltrytodevelopintuitionforthetransitionfromdiscrete
to continuous Bayesian updating. We’ll walk a familiar road from calculus. Namely we will:
(i) divide the continuous range of hypotheses into a finite number of short intervals.
(ii) create the discrete updating table for the finite number of hypotheses.
(iii) consider how the table changes as the number of hypotheses goes to infinity.
In this way, we’ll see the prior and posterior pmfs converge to the prior and posterior pdfs.
Example 10. To keep things concrete, we will work with the same prior and data as in
Example 7. We have a ‘bent’ coin with a flat prior 𝑓(𝜃) = 1. Our data is we tossed the coin
once and got heads.
Our goal is to go from discrete to continuous by increasing the number of hypotheses.
18.05 Class 13, Bayesian Updating with Continuous Priors, Spring 2022 9
4 hypotheses. Suppose we have four types of coins that have probability of heads 1/8,
3/8, 5/8 and 7/8 respectively. If one coin is chosen at random, our hypotheses for its type
are
ℋ ∶ 𝜃 = 1/8, ℋ ∶ 𝜃 = 3/8, ℋ ∶ 𝜃 = 5/8, ℋ ∶ 𝜃 = 7/8.
1 2 3 4
To get this, we divided [0,1] into 4 equal intervals: [0,1/4], [1/4,1/2], [1/2,3/4], [3/4,1].
Each interval has width Δ𝜃 = 1/4. We put our the value of 𝜃 for our coin types at the
centers of the four intervals.
(Just as with forming Riemann sums in calculus, it’s not important where in each interval
we choose 𝜃. The center is one easy choice.)
Let’s name each of these values 𝜃 = 𝑗/8, where 𝑗 = 1,3,5,7.
𝑗
The flat prior gives each hypothesis a probability of 1/4 = 1⋅Δ𝜃. We have the table:
hypothesis prior likelihood Bayesnum. posterior
𝜃=𝜃 = 1 1 1 1 ⋅ 1 0.0625
1 8 4 8 4 8
𝜃=𝜃 = 3 1 3 1 ⋅ 3 0.1875
2 8 4 8 4 8
𝜃=𝜃 = 5 1 5 1 ⋅ 5 0.3125
3 8 4 8 4 8
𝜃=𝜃 = 7 1 7 1 ⋅ 7 0.4375
4 8 4 8 4 8
𝑛
Total 1 – ∑𝜃 Δ𝜃 1
𝑖
𝑖=1
Here are the density histograms of the prior and posterior pmf. The prior and posterior
pdfs from Example 7 are superimposed on the histograms in red.
2 density 2 density
1.5 1.5
1 1
.5 .5
𝑥 𝑥
1/8 3/8 5/8 7/8 1/8 3/8 5/8 7/8
8 hypotheses. Next we slice [0,1] into 8 intervals each of width Δ𝜃 = 1/8 and use the
center of each slice for our 8 hypotheses 𝜃 .
𝑖
𝜃 : ’𝜃 = 1/16’, 𝜃 : ’𝜃 = 3/16’, 𝜃 : ’𝜃 = 5/16’, 𝜃 : ’𝜃 = 7/16’
1 2 3 4
𝜃 : ’𝜃 = 9/16’, 𝜃 : ’𝜃 = 11/16’, 𝜃 : ’𝜃 = 13/16’, 𝜃 : ’𝜃 = 15/16’
5 6 7 8
The flat prior gives each hypothesis the probablility 1/8 = 1⋅Δ𝜃. Here are the table and
density histograms.
18.05 Class 13, Bayesian Updating with Continuous Priors, Spring 2022 10
hypothesis prior likelihood Bayesnum. posterior
𝜃=𝜃 = 1 1 1 1 ⋅ 1 0.0156
1 16 8 16 8 16
𝜃=𝜃 = 3 1 3 1 ⋅ 3 0.0469
2 16 8 16 8 16
𝜃=𝜃 = 5 1 5 1 ⋅ 5 0.0781
3 16 8 16 8 16
𝜃=𝜃 = 7 1 7 1 ⋅ 7 0.1094
4 16 8 16 8 16
𝜃=𝜃 = 9 1 9 1 ⋅ 9 0.1406
5 16 8 16 8 16
𝜃=𝜃 = 11 1 11 1 ⋅ 11 0.1719
6 16 8 16 8 16
𝜃=𝜃 = 13 1 13 1 ⋅ 13 0.2031
7 16 8 16 8 16
𝜃=𝜃 = 15 1 15 1 ⋅ 15 0.2344
8 16 8 16 8 16
𝑛
Total 1 – ∑𝜃 Δ𝜃 1
𝑖
𝑖=1
2 density 2 density
1.5 1.5
1 1
.5 .5
𝑥 𝑥
1/16 3/16 5/16 7/16 9/16 11/16 13/16 15/16 1/16 3/16 5/16 7/16 9/16 11/16 13/16 15/16
20 hypotheses. Finally we slice [0,1] into 20 pieces. This is essentially identical to the
previous two cases. Let’s skip right to the density histograms.
2 density 2 density
1.5 1.5
1 1
.5 .5
𝑥 𝑥
3/7 3/7
Looking at the sequence of plots we see how the prior and posterior density histograms
converge to the prior and posterior probability density functions.
Notational conventions
Class 13, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to work with the various notations and terms we use to describe probabilities
and likelihood.
2 Introduction
We’ve introduced a number of different notations for probability, hypotheses and data. We
collect them here, to have them in one place.
3 Notation and terminology for data and hypotheses
The problem of labeling data and hypotheses is a tricky one. When we started the course
we talked about outcomes, e.g. heads or tails. Then when we introduced random variables
we gave outcomes numerical values, e.g. 1 for heads and 0 for tails. This allowed us to do
things like compute means and variances. We need to do something similar now. Recall
our notational conventions:
• Events are labeled with capital letters, e.g. 𝐴, 𝐵, 𝐶.
• A random variable is capital 𝑋 and takes values small 𝑥.
• The connection between values and events: ‘𝑋 = 𝑥’ is the event that 𝑋 takes the
value 𝑥.
• The probability of an event is capital 𝑃(𝐴).
• Adiscreterandomvariablehasaprobabilitymassfunctionsmall𝑝(𝑥)Theconnection
between 𝑃 and 𝑝 is that 𝑃(𝑋 = 𝑥) = 𝑝(𝑥).
• A continuous random variable has a probability density function 𝑓(𝑥) The connection
𝑏
between 𝑃 and 𝑓 is that 𝑃(𝑎 ≤ 𝑋 ≤ 𝑏) = ∫ 𝑓(𝑥)𝑑𝑥.
𝑎
• For a continuous random variable 𝑋 the probability that 𝑋 is in an infinitesimal
interval of width 𝑑𝑥 around 𝑥 is 𝑓(𝑥)𝑑𝑥.
In the context of Bayesian updating we have similar conventions.
• We use capital letters, especially ℋ, to indicate a hypothesis, e.g. ℋ = ’the coin is
fair’.
1
18.05 Class 13, Notational conventions, Spring 2022 2
• We use lower case letters, especially 𝜃, to indicate the hypothesized value of a model
parameter, e.g. the probability the coin lands heads is 𝜃 = 0.5.
• We use upper case letters, especially 𝒟, when talking about data as events. For
example, 𝒟 = ‘the sequence of tosses was HTH.
• We use lower case letters, especially 𝑥, when talking about data as values. For exam-
ple, the sequence of data was 𝑥 ,𝑥 ,𝑥 = 1,0,1.
1 2 3
• When the set of hypotheses is discrete we can use the probability of individual hy-
potheses, e.g. 𝑝(𝜃). When the set is continuous we need to use the probability for an
infinitesimal range of hypotheses, e.g. 𝑓(𝜃)𝑑𝜃.
The following table summarizes this for discrete 𝜃 and continuous 𝜃. In both cases we
are assuming a discrete set of possible outcomes (data) 𝑥. Tomorrow we will deal with a
continuous set of outcomes.
Bayes
hypothesis prior likelihood numerator posterior
ℋ 𝑃(ℋ) 𝑃(𝒟|ℋ) 𝑃(𝒟|ℋ)𝑃(ℋ) 𝑃(ℋ|𝒟)
Discrete 𝜃: 𝜃 𝑝(𝜃) 𝑝(𝑥|𝜃) 𝑝(𝑥|𝜃)𝑝(𝜃) 𝑝(𝜃|𝑥)
Continuous 𝜃: 𝜃 𝑓(𝜃)𝑑𝜃 𝑝(𝑥|𝜃) 𝑝(𝑥|𝜃)𝑓(𝜃)𝑑𝜃 𝑓(𝜃|𝑥)𝑑𝜃
Remember the continuous hypothesis 𝜃 is really a shorthand for ‘the parameter 𝜃 is in an
interval of width 𝑑𝜃 around 𝜃’.
Continuous Data with Continuous Priors
Class 14, 18.05
Jeremy Orloff and Jonathan Bloom
This reading is not assigned. It goes into a little more detail on Bayesian updating where
both hypotheses and data are continuous.
1 Learning Goals
1. Be able to construct a Bayesian update table for continuous hypotheses and continuous
data.
2. Beabletorecognizethepdfofanormaldistributionanddetermineitsmeanandvariance.
2 Introduction
We are now ready to do Bayesian updating when both the hypotheses and the data take
continuous values. The pattern is the same as what we’ve done before, so let’s first review
the previous two cases.
3 Previous cases
1. Discrete hypotheses, discrete data
Notation
• Hypotheses ℋ
• Data 𝑥
• Prior 𝑃(ℋ)
• Likelihood 𝑝(𝑥|ℋ)
• Posterior 𝑃(ℋ|𝑥).
Example 1. Suppose we have data 𝑥 and three possible explanations (hypotheses) for the
data that we’ll call 𝐴, 𝐵, 𝐶. Suppose also that the data can take two possible values, -1
and 1.
In order to use the data to help estimate the probabilities of the different hypotheses we
need a prior pmf and a likelihood table. Assume the prior and likelihoods are given in
the following table. (For this example we are only concerned with the formal process of
Bayesian updating. So we just made up the prior and likelihoods.)
1
18.05 Class 14, Continuous Data with Continuous Priors, Spring 2022 2
hypothesis prior hypothesis likelihood 𝑝(𝑥|ℋ)
ℋ 𝑃(ℋ) ℋ 𝑥 = −1 𝑥 = 1
A 0.1 A 0.2 0.8
B 0.3 B 0.5 0.5
C 0.6 C 0.7 0.3
Prior probabilities Likelihoods
Naturally, each entry in the likelihood table is a likelihood 𝑝(𝑥|ℋ). For instance the 0.2
row 𝐴 and column 𝑥 = −1 is the likelihood 𝑝(𝑥 = −1|𝐴).
Question: Suppose we run one trial and obtain the data 𝑥 = 1. Use this to find the
1
posterior probabilities for the hypotheses.
Solution: The data picks out one column from the likelihood table which we then use in
our Bayesian update table.
Bayes
hypothesis prior likelihood numerator posterior
𝑝(𝑥|ℋ)𝑃(ℋ)
ℋ 𝑃(ℋ) 𝑝(𝑥 = 1|ℋ) 𝑝(𝑥|ℋ)𝑃(ℋ) 𝑃(ℋ|𝑥) =
𝑝(𝑥)
𝐴 0.1 0.8 0.08 0.195
𝐵 0.3 0.5 0.15 0.366
𝐶 0.6 0.3 0.18 0.439
total 1 no sum 𝑝(𝑥) = 0.41 1
To summarize: the prior probabilities of hypotheses and the likelihoods of data given hy-
pothesis were given; the Bayes numerator is the product of the prior and likelihood; the
total probability 𝑝(𝑥) is the sum of the probabilities in the Bayes numerator column; and
we divide by 𝑝(𝑥) to normalize the Bayes numerator.
Note: As usual, the term ‘no sum’ in the likelihood column is not literally true. What it
means is that the sum is not meaningful to us. In particular, we don’t expect the likelihood
column to sum to 1.
2. Continuous hypotheses, discrete data
Now suppose that we have data 𝑥 that can take a discrete set of values and a continuous
parameter 𝜃 that determines the distribution the data is drawn from.
Notation
• Hypotheses 𝜃
• Data 𝑥
• Prior 𝑓(𝜃)𝑑𝜃
• Likelihood 𝑝(𝑥|𝜃)
• Posterior 𝑓(𝜃|𝑥)𝑑𝜃.
18.05 Class 14, Continuous Data with Continuous Priors, Spring 2022 3
Note: Here we multiplied by 𝑑𝜃 to express the prior and posterior as probabilities. As
densities, we have the prior pdf 𝑓(𝜃) and the posterior pdf 𝑓(𝜃|𝑥).
Example 2. Assume that 𝑥 ∼ Binomial(5,𝜃). So 𝜃 is in the range [0,1] and the data 𝑥
can take six possible values, 0, 1, …, 5.
Since there is a continuous range of values we use a pdf to describe the prior on 𝜃. Let’s
suppose the prior is 𝑓(𝜃) = 2𝜃. We can still make a likelihood table, though it only has one
row representing an arbitrary hypothesis 𝜃.
hypothesis likelihood 𝑝(𝑥|𝜃)
𝑥 = 0 𝑥 = 1 𝑥 = 2 𝑥 = 3 𝑥 = 4 𝑥 = 5
𝜃 (5)(1−𝜃)5 (5)𝜃(1−𝜃)4 (5)𝜃2(1−𝜃)3 (5)𝜃3(1−𝜃)2 (5)𝜃4(1−𝜃) (5)𝜃5
0 1 2 3 4 5
Likelihoods
Question: Suppose we run one trial and obtain the data 𝑥 = 2. Use this to find the
posterior pdf for the parameter (hypotheses) 𝜃.
Solution: As before, the data picks out one column from the likelihood table which we
can use in our Bayesian update table. Since we want to work with probabilities we write
𝑓(𝜃)𝑑𝜃 and 𝑓(𝜃|𝑥)𝑑𝜃 for the pdfs.
hypothesis prior likelihood Bayes posterior
(for 𝑥 = 2) numerator
𝑝(𝑥|𝜃)𝑓(𝜃)𝑑𝜃
𝜃 𝑓(𝜃)𝑑𝜃 𝑝(𝑥|𝜃) 𝑝(𝑥|𝜃)𝑓(𝜃)𝑑𝜃 𝑓(𝜃|𝑥)𝑑𝜃 =
𝑝(𝑥)
7!
𝜃 2𝜃𝑑𝜃 (5)𝜃2(1−𝜃)3 2(5)𝜃3(1−𝜃)3𝑑𝜃 𝑓(𝜃|𝑥)𝑑𝜃 = 𝜃3(1−𝜃)3𝑑𝜃
2 2 3!3!
𝑝(𝑥) = ∫ 1 2(5)𝜃3(1−𝜃)3𝑑𝜃
total 1 no sum 0 2 1
= 2(5)3!3!
2 7!
To summarize: the prior probabilities of hypotheses and the likelihoods of data given hy-
pothesis were given; the Bayes numerator is the product of the prior and likelihood; the
total probability 𝑝(𝑥) is the integral of the probabilities in the Bayes numerator column;
and we divide by 𝑝(𝑥) to normalize the Bayes numerator.
4 Continuous hypotheses and continuous data
When both data and hypotheses are continuous, the only change to the previous example is
that the likelihood function uses a pdf 𝜙(𝑥|𝜃) instead of a pmf 𝑝(𝑥|𝜃). The general shape
of the Bayesian update table is the same.
Notation
18.05 Class 14, Continuous Data with Continuous Priors, Spring 2022 4
• Hypotheses 𝜃. For continuous hypotheses, this really means that we hypothesize that
the parameter is in a small interval of size 𝑑𝜃 around 𝜃.
• Data 𝑥. For continuous data, this really means that the data is in a small interval of
size 𝑑𝑥 around 𝑥.
• Prior 𝑓(𝜃)𝑑𝜃. This is our initial belief about the probability that the parameter is in
a small interval of size 𝑑𝜃 around 𝜃.
• Likelihood 𝜙(𝑥|𝜃)𝑑𝑥. This is the (calculated) probability that the data is in a small
interval of size 𝑑𝑥 around 𝑥, ASSUMING the hypothesis 𝜃.
• Posterior 𝑓(𝜃|𝑥)𝑑𝜃. This is the (calculated) probability that the parameter is in a
small interval of size 𝑑𝜃 around 𝜃, GIVEN the data 𝑥.
Simplifying the notation. Inthepreviouscasesweincluded𝑑𝜃 sothatwewereworking
with probabilities instead of densities. When both data and hypotheses are continuous
we will need both 𝑑𝜃 and 𝑑𝑥. This makes things conceptually simpler, but notationally
cumbersome. To simplify the notation we will sometimes allow ourselves to drop 𝑑𝑥 in our
tables. This is fine because the data 𝑥 is fixed in each calculation. We keep the 𝑑𝜃 because
the hypothesis 𝜃 is allowed to vary.
For comparison, we first show the general table in simplified notation followed immediately
afterward by the table showing both infinitesimals.
Bayes
hypoth. prior likelihood numerator posterior
𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃
𝜃 𝑓(𝜃)𝑑𝜃 𝜙(𝑥|𝜃) 𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃 𝑓(𝜃|𝑥)𝑑𝜃 =
𝜙(𝑥)
total 1 no sum 𝜙(𝑥) = ∫𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃 1
(integrate over 𝜃) = prior prob. density for data 𝑥
Bayesian update table without 𝑑𝑥
Bayes
hypoth. prior likelihood numerator posterior
𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃𝑑𝑥
𝑓(𝜃|𝑥)𝑑𝜃 =
𝜙(𝑥)𝑑𝑥
𝜃 𝑓(𝜃)𝑑𝜃 𝜙(𝑥|𝜃)𝑑𝑥 𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃𝑑𝑥
= 𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃
𝜙(𝑥)
total 1 no sum 𝜙(𝑥)𝑑𝑥 = (∫𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃) 𝑑𝑥 1
Bayesian update table with 𝑑𝜃 and 𝑑𝑥
To summarize: the prior probabilities of hypotheses and the likelihoods of data given hy-
pothesis were given; the Bayes numerator is the product of the prior and likelihood; the
18.05 Class 14, Continuous Data with Continuous Priors, Spring 2022 5
total probability 𝜙(𝑥)𝑑𝑥 is the integral of the probabilities in the Bayes numerator column;
we divide by 𝜙(𝑥)𝑑𝑥 to normalize the Bayes numerator.
5 A digression on notational messes
We have chosen to use the notation 𝜙(𝑥), 𝜙(𝑥|𝜃) for the pdfs of data and 𝑓(𝜃), 𝑓(𝜃|𝑥) for
the pdfs of hypotheses. This is nice because 𝜙 is a Greek 𝑓, but the different symbols help
us distinguish the two types of pdfs. Many, perhaps most, writers use the same letter 𝑓 for
both. This forces the reader to look at the arguments to the function to understand what
is meant. That is, 𝑓(𝑥|𝜃) is the probability of data given an hypothesis, i.e. the likelihood
and 𝑓(𝜃|𝑥) is the probability of an hypothesis given the data, i.e. the posterior pdf.
As mathematicians this makes us pull our hair out. But, to be fair, there is a philosoph-
ical underpinning to this notation. We can think of 𝑓 as a universal probability density
which gives the probability of absolutely any combination of things. Thus 𝑓(𝑥,𝑦) is the
joint probability density for the quantities denoted by 𝑥 and 𝑦. If we just write 𝑓(𝑥) the
implication is that this means the marginal density for 𝑥, i.e. the density for 𝑥 when 𝑦 is
allowed to take any value. Similarly we can write 𝑓(𝑥,𝑦|𝑧) for the conditional density of 𝑥
and 𝑦 given 𝑧.
6 Normal hypothesis, normal data
A standard example of continuous hypotheses and continuous data assumes that both the
dataandpriorfollownormaldistributions. Thefollowingexampleassumesthatthevariance
of the data is known.
Example 3. Suppose we have data 𝑥 = 5 which was drawn from a normal distribution
with unknown mean 𝜃 and standard deviation 1.
𝑥 ∼ N(𝜃,1)
Suppose further, that our prior distribution for the unknown parameter 𝜃 is 𝜃 ∼ N(2,1).
Let 𝑥 represent an arbitrary data value.
(a) Make a Bayesian table with prior, likelihood, and Bayes numerator.
(b) Show that the posterior distribution for 𝜃 is normal as well.
(c) Find the mean and variance of the posterior distribution.
Solution: Aswedidwiththetablesabove,agoodcompromiseonthenotationistoinclude
𝑑𝜃 but not 𝑑𝑥. The reason for this is that the total probability is computed by integrating
over 𝜃 and the 𝑑𝜃 reminds of us that.
Our prior pdf is
1
𝑓(𝜃) = √ e−(𝜃−2)2/2.
2𝜋
The likelihood function is
1
𝜙(𝑥 = 5|𝜃) = √ e−(5−𝜃)2/2.
2𝜋
18.05 Class 14, Continuous Data with Continuous Priors, Spring 2022 6
We know we are going to multiply the prior and the likelihood, so we carry out that algebra
first. In the very last step we give the complicated constant factor the name 𝑐 .
1
1 1
prior ⋅ likelihood = √ e−(𝜃−2)2/2⋅ √ e−(5−𝜃)2/2
2𝜋 2𝜋
1
= e−(2𝜃2−14𝜃+29)/2
2𝜋
1
= e−(𝜃2−7𝜃+29/2) (complete the square)
2𝜋
1
= e−((𝜃−7/2)2+9/4)
2𝜋
e−9/4
= e−(𝜃−7/2)2)
2𝜋
= 𝑐 e−(𝜃−7/2)2
1
In the last step we named the complicated constant factor 𝑐 .
1
Bayes posterior
hypothesis prior likelihood numerator 𝑓(𝜃|𝑥 = 5)𝑑𝜃
𝜙(𝑥 = 5|𝜃)𝑓(𝜃)𝑑𝜃
𝜃 𝑓(𝜃)𝑑𝜃 𝜙(𝑥 = 5|𝜃) 𝜙(𝑥 = 5|𝜃)𝑓(𝜃)𝑑𝜃
𝜙(𝑥 = 5)
𝜃 √1 e−(𝜃−2)2/2𝑑𝜃 √1 e−(5−𝜃)2/2 𝑐 e−(𝜃−7/2)2 𝑐 e−(𝜃−7/2)2
2𝜋 2𝜋 1 2
total 1 no sum 𝜙(𝑥 = 5) = ∫𝜙(𝑥 = 5|𝜃)𝑓(𝜃)𝑑𝜃 1
We can see by the form of the posterior pdf that it is a normal distribution. Because the
exponential for a normal distribution is e−(𝜃−𝜇)2/2𝜎2 we have mean 𝜇 = 7/2 and 2𝜎2 = 1, so
variance 𝜎2 = 1/2.
We don’t need to bother computing the total probability; it is just used for normalization
1
and we already know the normalization constant √ for a normal distribution. To
𝜎 2𝜋
summarize,
The posterior pdf follows a N(7/2,1/2) distribution.
Here is the graph of the prior and the posterior pdfs for this example. Note how the data
‘pulls’ the prior (the wider bell on the left) towards the data. The posterior is the narrower
bell on the right. After collecting data, we have a new opinion about the mean, and we are
more sure of this new opinion.
18.05 Class 14, Continuous Data with Continuous Priors, Spring 2022 7
0 1 2 3 4 5 6 7
5.0
4.0
3.0
2.0
1.0
0.0
prior = orange; posterior = blue; data = red line
Now we’ll repeat the previous example for general 𝑥. When reading this if you mentally
substitute 5 for 𝑥 you will understand the algebra.
Example 4. Suppose our data 𝑥 is drawn from a normal distribution with unknown mean
𝜃 and standard deviation 1.
𝑥 ∼ N(𝜃,1)
Suppose further, that our prior distribution for the unknown parameter 𝜃 is 𝜃 ∼ N(2,1).
Solution: As before, we show the algebra used to simplify the Bayes numerator: The prior
pdf and likelihood function are
1 1
𝑓(𝜃) = √ e−(𝜃−2)2/2 𝑓(𝑥|𝜃) = √ e−(𝑥−𝜃)2/2.
2𝜋 2𝜋
The Bayes numerator is the product of the prior and the likelihood:
1 1
prior ⋅ likelihood = √ e−(𝜃−2)2/2⋅ √ e−(𝑥−𝜃)2/2
2𝜋 2𝜋
1
= e−(2𝜃2−(4+2𝑥)𝜃+4+𝑥2)/2
2𝜋
1
= e−(𝜃2−(2+𝑥)𝜃+(4+𝑥2)/2) (complete the square)
2𝜋
1
= e−((𝜃−(1+𝑥/2))2−(1+𝑥/2)2+(4+𝑥2)/2)
2𝜋
= 𝑐 e−(𝜃−(1+𝑥/2))2
1
Just as in the previous example, in the last step we replaced all the constants, including
the exponentials that just involve 𝑥, by by the simple constant 𝑐 .
1
Now the Bayesian update table becomes
18.05 Class 14, Continuous Data with Continuous Priors, Spring 2022 8
Bayes posterior
hypothesis prior likelihood numerator 𝑓(𝜃|𝑥)𝑑𝜃
𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃
𝜃 𝑓(𝜃)𝑑𝜃 𝜙(𝑥|𝜃) 𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃
𝜙(𝑥)
𝜃 √1 e−(𝜃−2)2/2𝑑𝜃 √1 e−(𝑥−𝜃)2/2 𝑐 e−(𝜃−(1+𝑥/2))2 𝑐 e−(𝜃−(1+𝑥/2))2
2𝜋 2𝜋 1 2
𝜃 𝜃 ∼ N(2,1) 𝑥 ∼ N(𝜃,1) 𝜃 ∼ N(1+𝑥/2,1/2)
total 1 no sum 𝜙(𝑥) = ∫𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃 1
As in the previous example we can see by the form of the posterior that it must be a normal
distribution with mean 1+𝑥/2 and variance 1/2. That is,
The posterior pdf follows a N(1+𝑥/2,1/2) distribution.
You should compare this with the case 𝑥 = 5 in the previous example.
7 Predictive probabilities
Sincethedata𝑥iscontinuousithaspriorandposteriorpredictivepdfs. Thepriorpredictive
pdfisthetotalprobabilitydensitycomputedatthebottomoftheBayesnumeratorcolumn:
𝜙(𝑥) = ∫𝑓(𝑥|𝜃)𝑓(𝜃)𝑑𝜃,
where the integral is computed over the entire range of 𝜃.
The posterior predictive pdf has the same form as the prior predictive pdf, except it uses
the posterior probabilities for 𝜃:
𝜙(𝑥 |𝑥 ) = ∫𝜙(𝑥 |𝜃,𝑥 )𝑓(𝜃|𝑥 )𝑑𝜃,
2 1 2 1 1
We usually assume that 𝑥 and 𝑥 are conditionally independent. That is,
1 2
𝜙(𝑥 |𝜃,𝑥 ) = 𝜙(𝑥 |𝜃).
2 1 2
In this case the formula for the posterior predictive pdf is a little simpler:
𝜙(𝑥 |𝑥 ) = ∫𝜙(𝑥 |𝜃)𝑓(𝜃|𝑥 )𝑑𝜃.
2 1 2 1
Conjugate priors: Beta and normal
Class 15, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be familiar with the 2-parameter family of beta distributions and its normalization.
2. Understand the benefits of conjugate priors.
3. Be able to update a beta prior given a Bernoulli, binomial, or geometric likelihood.
4. Understand and be able to use the formula for updating a normal prior given a normal
likelihood with known variance.
2 Introduction
Our main goal here is to introduce the idea of conjugate priors and look at some specific
conjugate pairs. These simplify the job of Bayesian updating to simple arithmetic. We’ll
start by introducing the beta distribution and using it as a conjugate prior with a binomial
likelihood. After that we’ll look at other conjugate pairs.
3 Beta distribution
The beta distribution Beta(𝑎,𝑏) is a two-parameter distribution with range [0,1] and pdf
(𝑎+𝑏−1)!
𝑓(𝜃) = 𝜃𝑎−1(1−𝜃)𝑏−1
(𝑎−1)!(𝑏−1)!
We have made an applet so you can explore the shape of the beta distribution as you vary
the parameters:
https://mathlets.org/mathlets/beta-distribution/.
As you can see in the applet, the beta distribution may be defined for any real numbers
𝑎 > 0 and 𝑏 > 0. In 18.05 we will stick to integers 𝑎 and 𝑏, but you can get the full story
here: https://en.wikipedia.org/wiki/Beta_distribution
InthecontextofBayesianupdating, 𝑎and𝑏areoftencalledhyperparameterstodistinguish
them from the unknown parameter 𝜃 representing our hypotheses. In a sense, 𝑎 and 𝑏 are
‘one level up’ from 𝜃 since they parameterize its pdf.
3.1 A simple but important observation!
If a pdf 𝑓(𝜃) with range [0,1] has the form 𝑐𝜃𝑎−1(1−𝜃)𝑏−1 then 𝑓(𝜃) is a Beta(𝑎,𝑏) distri-
bution and the normalizing constant must be
(𝑎+𝑏−1)!
𝑐 = .
(𝑎−1)!(𝑏−1)!
1
18.05 Class 15, Conjugate priors: Beta and normal, Spring 2022 2
This follows because the constant 𝑐 must normalize the pdf to have total probability 1.
There is only one such constant and it is given in the formula for the beta distribution.
A similar observation holds for normal distributions, exponential distributions, and so on.
3.2 Beta priors and posteriors for binomial random variables
Example 1. Suppose we have a bent coin with unknown probability 𝜃 of heads. We toss
it 12 times and get 8 heads and 4 tails. Starting with a flat prior, show that the posterior
pdf is a Beta(9,5) distribution.
Solution: This is nearly identical to examples from the previous class. We’ll call the data
from all 12 tosses 𝑥 . In the following table we call the leading constant factor in the
1
posterior column 𝑐 . Our simple observation will tell us that it has to be the constant
2
factor from the beta pdf.
The data is 8 heads and 4 tails. Since this comes from a binomial(12, 𝜃) distribution, the
12
likelihood 𝑝(𝑥 |𝜃) = ( )𝜃8(1−𝜃)4. Thus the Bayesian update table is
1 8
Bayes
hypothesis prior likelihood numerator posterior
𝜃 1⋅ 𝑑𝜃 (12)𝜃8(1−𝜃)4 (12)𝜃8(1−𝜃)4𝑑𝜃 𝑐 𝜃8(1−𝜃)4𝑑𝜃
8 8 2
12 1
total 1 𝑇 = ( )∫ 𝜃8(1−𝜃)4𝑑𝜃 1
8
0
For the posterior pdf, our simple observation holds with 𝑎 = 9 and 𝑏 = 5. Therefore the
posterior pdf follows a Beta(9,5) distribution and we have
13!
𝑓(𝜃|𝑥 ) = 𝑐 𝜃8(1−𝜃)4, where 𝑐 = .
1 2 2 8!4!
Note: We explicitly included the binomial coeﬀicient (12) in the likelihood. We could just
8
as easily have given it a name, say 𝑐 and not bothered making its value explicit.
1
Example 2. Now suppose we toss the same coin again, getting 𝑛 heads and 𝑚 tails. Using
the posterior pdf of the previous example as our new prior pdf, show that the new posterior
pdf is that of a Beta(9+𝑛,5+𝑚) distribution.
Solution: It’s all in the table. We’ll call the data of these 𝑛+𝑚 additional tosses 𝑥 . This
2
time we won’t make the binomial coeﬀicient explicit. Instead we’ll just call it 𝑐 . Whenever
3
we need a new label we will simply use 𝑐 with a new subscript.
Bayes
hyp. prior likelihood numerator posterior
𝜃 𝑐 𝜃8(1−𝜃)4𝑑𝜃 𝑐 𝜃𝑛(1−𝜃)𝑚 𝑐 𝑐 𝜃𝑛+8(1−𝜃)𝑚+4𝑑𝜃 𝑐 𝜃𝑛+8(1−𝜃)𝑚+4𝑑𝜃
2 3 2 3 4
1
total 1 𝑇 = ∫ 𝑐 𝑐 𝜃𝑛+8(1−𝜃)𝑚+4𝑑𝜃 1
2 3
0
Again our simple observation holds and therefore the posterior pdf
𝑓(𝜃|𝑥 ,𝑥 ) = 𝑐 𝜃𝑛+8(1−𝜃)𝑚+4
1 2 4
18.05 Class 15, Conjugate priors: Beta and normal, Spring 2022 3
follows a Beta(𝑛+9,𝑚+5) distribution.
Note: Flat beta. The Beta(1,1) distribution is the same as the uniform distribution on
[0,1], which we have also called the flat prior on 𝜃. This follows by plugging 𝑎 = 1 and
𝑏 = 1 into the definition of the beta distribution, giving 𝑓(𝜃) = 1.
Summary: If the probability of heads is 𝜃, the number of heads in 𝑛+𝑚 tosses follows a
binomial(𝑛+𝑚,𝜃) distribution. We have seen that if the prior on 𝜃 is a beta distribution
then so is the posterior; only the parameters 𝑎, 𝑏 of the beta distribution change! We
summarize precisely how they change in a table. We assume the data is 𝑛 heads and 𝑚
tails in 𝑛+𝑚 tosses.
hypothesis data prior likelihood posterior
𝜃 𝑥 = 𝑛, 𝑚 Beta(𝑎,𝑏) binomial(𝑛+𝑚,𝜃) Beta(𝑎+𝑛,𝑏+𝑚)
𝜃 𝑥 = 𝑛, 𝑚 𝑐 𝜃𝑎−1(1−𝜃)𝑏−1𝑑𝜃 𝑐 𝜃𝑛(1−𝜃)𝑚 𝑐 𝜃𝑎+𝑛−1(1−𝜃)𝑏+𝑚−1𝑑𝜃
1 2 3
4 Conjugate priors
The beta distribution is called a conjugate prior for the binomial distribution. This means
that if the likelihood function is binomial, then a beta prior gives a beta posterior –this is
what we saw in the previous examples. In fact, the beta distribution is a conjugate prior
for the Bernoulli and geometric distributions as well.
We will soon see another important example: the normal distribution is its own conjugate
prior. In particular, if the likelihood function is normal with known variance, then a normal
prior gives a normal posterior.
ConjugatepriorsareusefulbecausetheyreduceBayesianupdatingtomodifyingtheparam-
eters of the prior distribution (so-called hyperparameters) rather than computing integrals.
We saw this for the beta distribution in the last table. For many more examples see:
https://en.wikipedia.org/wiki/Conjugate_prior_distribution
We now give a definition of conjugate prior. It is best understood through the examples in
the subsequent sections.
Definition. Suppose we have data with likelihood function 𝜙(𝑥|𝜃) depending on a hy-
pothesized parameter 𝜃. Also suppose the prior distribution for 𝜃 is one of a family of
parametrized distributions. If the posterior distribution for 𝜃 is in this family then we say
the the family of priors are conjugate priors for the likelihood.
This definition will be illustrated with specific examples in the sections below.
5 Beta priors
In this section, we will show that the beta distribution is a conjugate prior for binomial,
Bernoulli, and geometric likelihoods.
18.05 Class 15, Conjugate priors: Beta and normal, Spring 2022 4
5.1 Binomial likelihood
We saw above that the beta distribution is a conjugate prior for the binomial distribution.
Thismeansthatifthelikelihoodfunctionisbinomialandthepriordistributionisbetathen
the posterior is also beta.
More specifically, suppose that the likelihood follows a binomial(𝑁,𝜃) distribution where 𝑁
is known and 𝜃 is the (unknown) parameter of interest. We also have that the data 𝑥 from
one trial is an integer between 0 and 𝑁. Then for a beta prior we have the following table:
hypoth. data prior likelihood posterior
Beta(𝑎,𝑏) binomial(𝑁,𝜃) Beta(𝑎+𝑥,𝑏+𝑁 −𝑥)
𝜃 𝑥
𝑓(𝜃) = 𝑐 𝜃𝑎−1(1−𝜃)𝑏−1 𝑝(𝑥|𝜃) = 𝑐 𝜃𝑥(1−𝜃)𝑁−𝑥 𝑓(𝜃|𝑥) = 𝑐 𝜃𝑎+𝑥−1(1−𝜃)𝑏+𝑁−𝑥−1
1 2 3
The table is simplified by writing the normalizing coeﬀicients as 𝑐 , 𝑐 and 𝑐 respectively.
1 2 3
If needed, we can recover the values of the 𝑐 and 𝑐 by recalling (or looking up) the
1 2
normalizations of the beta and binomial distributions.
(𝑎+𝑏−1)! 𝑁 𝑁! (𝑎+𝑏+𝑁 −1)!
𝑐 = 𝑐 = ( ) = 𝑐 =
1 (𝑎−1)!(𝑏−1)! 2 𝑥 𝑥!(𝑁 −𝑥)! 3 (𝑎+𝑥−1)!(𝑏+𝑁 −𝑥−1)!
5.2 Bernoulli likelihood
The beta distribution is a conjugate prior for the Bernoulli distribution. This is actually
a special case of the binomial distribution, since Bernoulli(𝜃) is the same as binomial(1,
𝜃). We do it separately because it is slightly simpler and of special importance. In the
table below, we show the updates corresponding to success (𝑥 = 1) and failure (𝑥 = 0) on
separate rows.
hypothesis data prior likelihood posterior
𝜃 𝑥 Beta(𝑎,𝑏) Bernoulli(𝜃) Beta(𝑎+1,𝑏) or Beta(𝑎,𝑏+1)
𝜃 𝑥 = 1 𝑓(𝜃) = 𝑐 𝜃𝑎−1(1−𝜃)𝑏−1 𝑝(𝑥|𝜃) = 𝜃 Beta(𝑎+1,𝑏): 𝑓(𝜃|𝑥) = 𝑐 𝜃𝑎(1−𝜃)𝑏−1
1 3
𝜃 𝑥 = 0 𝑓(𝜃) = 𝑐 𝜃𝑎−1(1−𝜃)𝑏−1 𝑝(𝑥|𝜃) = 1−𝜃 Beta(𝑎,𝑏+1): 𝑓(𝜃|𝑥) = 𝑐 𝜃𝑎−1(1−𝜃)𝑏
1 4
The constants 𝑐 , 𝑐 and 𝑐 have the same formulas as in the previous (binomial likelihood
1 3 4
case) with 𝑁 = 1.
5.3 Geometric likelihood
Recall that the geometric(𝜃) distribution describes the probability of 𝑥 successes before
the first failure, where the probability of success on any single independent trial is 𝜃. The
corresponding pmf is given by 𝑝(𝑥) = 𝜃𝑥(1−𝜃).
Now suppose that we have a data point 𝑥, and our hypothesis 𝜃 is that 𝑥 is drawn from a
geometric(𝜃) distribution. From the table we see that the beta distribution is a conjugate
prior for a geometric likelihood as well:
hypothesis data prior likelihood posterior
Beta(𝑎,𝑏) geometric(𝜃) Beta(𝑎+𝑥,𝑏+1)
𝜃 𝑥
= 𝑓(𝜃) = 𝑐 𝜃𝑎−1(1−𝜃)𝑏−1 = 𝑝(𝑥|𝜃) = 𝜃𝑥(1−𝜃) 𝑓(𝜃|𝑥) = 𝑐 𝜃𝑎+𝑥−1(1−𝜃)𝑏
1 3
18.05 Class 15, Conjugate priors: Beta and normal, Spring 2022 5
At first it may seem strange that the beta distribution is a conjugate prior for both the
binomial and geometric distributions. The key reason is that the geometric likelihood is
proportional to a binomial likelihood as a function of 𝜃. Let’s illustrate this in a concrete
example.
Example 3. While traveling through the Mushroom Kingdom, Mario and Luigi find some
ratherunusualcoins. Theyagreeonapriorof𝑓(𝜃) ∼Beta(5,5)fortheprobabilityofheads,
though they disagree on what experiment to run to investigate 𝜃 further.
(a) Mario decides to flip a coin 5 times. He gets four heads in five flips.
(b) Luigi decides to flip a coin until the first tails. He gets four heads before the first tail.
ShowthatMarioandLuigiwillarriveatthesameposterioron𝜃,andcalculatethisposterior.
Solution: WewillshowthatbothMarioandLuigifindtheposteriorpdffor𝜃isaBeta(9,6)
distribution.
Mario’s table
hypothesis data prior likelihood posterior
Beta(5,5) binomial(5,𝜃) ???
𝜃 𝑥 = 4
= 𝑐 𝜃4(1−𝜃)4 = (5)𝜃4(1−𝜃) = 𝑐 𝜃8(1−𝜃)5
1 4 3
Luigi’s table
hypothesis data prior likelihood posterior
Beta(5,5) geometric(𝜃) ???
𝜃 𝑥 = 4
= 𝑐 𝜃4(1−𝜃)4 = 𝜃4(1−𝜃) = 𝑐 𝜃8(1−𝜃)5
1 3
Since both Mario and Luigi’s posteriors have the form of a Beta(9,6) distribution that’s
what they both must be. The normalizing factor must be the same in both cases because
it’s determined by requiring the total probability to be 1.
6 Bayesian updating with continuous hypotheses and contin-
uous data
The idea here is essentially identical to the Bayesian updating we’ve already done. The
only change is, with a continuous likelihood, we have to compute the total probability of
the data (i.e. sum of the Bayes numerator column, i.e. normalizing factor) as an integral
instead of a sum. We will cover this briefly. For those who are interested, a bit more detail
is given in an optional note.
Notation
• Hypotheses 𝜃. For continuous hypotheses, this really means that we hypothesize that
the parameter is in a small interval of size 𝑑𝜃 around 𝜃.
• Data 𝑥. For continuous data, this really means that the data is in a small interval of
size 𝑑𝑥 around 𝑥.
• Prior 𝑓(𝜃)𝑑𝜃. This is our initial belief about the probability that the parameter is in
a small interval of size 𝑑𝜃 around 𝜃.
18.05 Class 15, Conjugate priors: Beta and normal, Spring 2022 6
• Likelihood 𝜙(𝑥|𝜃). So the probability that the data is in a small interval of size 𝑑𝑥
around 𝑥, ASSUMING the hypothesis 𝜃 is 𝜙(𝑥|𝜃)𝑑𝑥
• Posterior 𝑓(𝜃|𝑥)𝑑𝜃. This is the (calculated) probability that the parameter is in a
small interval of size 𝑑𝜃 around 𝜃, GIVEN the data 𝑥.
Bayes
hypoth. prior likelihood numerator posterior
𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃
𝜃 𝑓(𝜃)𝑑𝜃 𝜙(𝑥|𝜃) 𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃 𝑓(𝜃|𝑥)𝑑𝜃 =
𝜙(𝑥)
total 1 no sum 𝜙(𝑥) = ∫𝜙(𝑥|𝜃)𝑓(𝜃)𝑑𝜃 1
(integrate over 𝜃) = prior prob. density for data 𝑥
Continuous-continuous Bayesian update table
To summarize: the prior probabilities of hypotheses and the likelihoods of data given hy-
pothesis were given; the Bayes numerator is the product of the prior and likelihood; the
total likelihood 𝜙(𝑥) is the integral of the probabilities in the Bayes numerator column; we
divide by 𝜙(𝑥) to normalize the Bayes numerator.
7 Normal begets normal
We now turn to an important example of coninuous-continuous updating: the normal dis-
tribution is its own conjugate prior. In particular, if the likelihood function is normal with
known variance, then a normal prior gives a normal posterior. Now both the hypotheses
and the data are continuous.
Suppose we have a measurement 𝑥 ∼ 𝑁(𝜃,𝜎2) where the variance 𝜎2 is known. That is, the
mean 𝜃 is our unknown parameter of interest and we are given that the likelihood comes
from a normal distribution with variance 𝜎2. If we choose a normal prior pdf
𝑓(𝜃) ∼ N(𝜇 ,𝜎2 )
prior prior
then the posterior pdf is also normal: 𝑓(𝜃|𝑥) ∼ N(𝜇 ,𝜎2 ) where
post post
𝜇 𝜇 𝑥 1 1 1
post prior
= + , = + (1)
𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2
post prior post prior
The following form of these formulas is easier to read and shows that 𝜇 is a weighted
post
average between 𝜇 and the data 𝑥.
prior
1 1 𝑎𝜇 +𝑏𝑥 1
𝑎 = 𝑏 = , 𝜇 = prior , 𝜎2 = . (2)
𝜎2 𝜎2 post 𝑎+𝑏 post 𝑎+𝑏
prior
With these formulas in mind, we can express the update via the table:
18.05 Class 15, Conjugate priors: Beta and normal, Spring 2022 7
hypothesis data prior likelihood posterior
𝑓(𝜃) ∼ N(𝜇 ,𝜎2 ) 𝜙(𝑥|𝜃) ∼ N(𝜃,𝜎2) 𝑓(𝜃|𝑥) ∼ N(𝜇 ,𝜎2 )
prior prior post post
𝜃 𝑥
= 𝑐 exp(
−(𝜃−𝜇
prior
)2
) = 𝑐
exp(−(𝑥−𝜃)2
) = 𝑐 exp(
−(𝜃−𝜇
post
)2
)
1 2𝜎2 2 2𝜎2 3 2𝜎2
prior post
We leave the proof of the general formulas to the problem set. It is an involved algebraic
manipulation which is essentially the same as the following numerical example.
Example 4. Suppose we have prior 𝜃 ∼ N(4,8), and likelihood function likelihood 𝑥 ∼
N(𝜃,5). Supposealsothatwehaveonemeasurement𝑥 = 3. Showtheposteriordistribution
1
is normal.
Solution: We will show this by grinding through the algebra which involves completing
the square.
prior: 𝑓(𝜃) = 𝑐 e−(𝜃−4)2/16; likelihood: 𝜙(𝑥 |𝜃) = 𝑐 e−(𝑥 1 −𝜃)2/10 = 𝑐 e−(3−𝜃)2/10
1 1 2 2
We multiply the prior and likelihood to get the posterior:
𝑓(𝜃|𝑥 ) = 𝑐 e−(𝜃−4)2/16e−(3−𝜃)2/10
1 3
(𝜃−4)2 (3−𝜃)2
= 𝑐 exp(− − )
3 16 10
We complete the square in the exponent
(𝜃−4)2 (3−𝜃)2 5(𝜃−4)2+8(3−𝜃)2
− − = −
16 10 80
13𝜃2−88𝜃+152
= −
80
𝜃2− 88𝜃+ 152
= − 13 13
80/13
(𝜃−44/13)2+152/13−(44/13)2
= − .
80/13
Therefore the posterior is
𝑓(𝜃|𝑥 ) = 𝑐
e−(𝜃−44/13)2+
8
1
0
5
/
2
1
/
3
13−(44/13)2
= 𝑐
e−(𝜃−
8
4
0
4
/
/
1
1
3
3)2
.
1 3 4
This has the form of the pdf for N(44/13,40/13). QED
For practice we check this against the formulas (2).
1 1
𝜇 = 4, 𝜎2 = 8, 𝜎2 = 5 ⇒ 𝑎 = , 𝑏 = .
prior prior 8 5
Therefore
𝑎𝜇 +𝑏𝑥 44
prior
𝜇 = = = 3.38
post 𝑎+𝑏 13
1 40
𝜎2 = = = 3.08.
post 𝑎+𝑏 13
18.05 Class 15, Conjugate priors: Beta and normal, Spring 2022 8
7.1 A word on weighted averages
The updating formula 2 gives 𝜇 as a weighted average of the 𝜇 and the data. The
post prior
weight on 𝜇 is 𝑎/(𝑎+𝑏), and the weight on the data is 𝑏/(𝑎+𝑏). These weights are
prior
always positive numbers summing to 1. If 𝑏 is very large (that is, if the data has a tiny
variance) then most of the weight is on the data. If 𝑎 is very large (that is, 𝜎2 is small,
prior
i.e. if you are very confident in your prior) then most of the weight is on the prior.
In the above example the variance on the prior was bigger than the variance on the data,
so 𝑎 was smaller than 𝑏; so the weight was mostly on the data. The posterior 3.38 for the
mean was closer to the data 3 than to the prior 4 for the mean.
7.2 Examples of normal-normal updating
Example 5. Suppose that we know the data 𝑥 ∼ N(𝜃,4/9) and we have prior N(0,1). We
get one data value 𝑥 = 6.5. Describe the changes to the pdf for 𝜃 in updating from the
prior to the posterior.
Solution: 𝜇 = 0, 𝜎2 = 1, 𝜎2 = 4/9. So, using the updating formulas 2 we have
prior prior
1 9 𝑎𝜇 +𝑏𝑥 1 4
𝑎 = 1, 𝑏 = = , 𝜇 = prior = 4.5, 𝜎2 = = .
4/9 4 post 𝑎+𝑏 post 𝑎+𝑏 13
Here is a graph of the prior and posterior pdfs with the data point marked by a red line.
−2 0 2 4 6 8 10
6.0
4.0
2.0
0.0
Prior in blue, posterior in orange, data = red line
We see that the posterior mean is closer to the data point than the prior mean We also see
that the posterior distribution is taller and narrower than the prior, i.e. it has a smaller
variance. The smaller variance says that we are now more certain about where the value of
𝜃 lies.
Example 6. Use the formulas 2 to show that for normal-normal Bayesian updating we
have:
1. The posterior mean is always between the data point and the prior mean.
2. The posterior variance is smaller than both the prior variance and 𝜎. That is, our
18.05 Class 15, Conjugate priors: Beta and normal, Spring 2022 9
posterior uncetainty is smaller than both our prior uncertainty and the uncertainty in the
data.
Solution: Usingtheupdateformulas2,wehaveTheposteriormeanistheweightedaverage
of the prior mean and the data, so it must lie between the prior mean and the data.
Also, the posterior variance is
1 1
𝜎2 = < = 𝜎2
post 𝑎+𝑏 𝑎 prior
That is the posterior has smaller variance than the prior, i.e. data makes us more certain
about where in its range 𝜃 lies.
1 1
Likewise 𝜎2 = < = 𝜎2. So, the posterior variance is smaller than 𝜎2.
post 𝑎+𝑏 𝑏
7.3 More than one data point
Example 7. Suppose we have data 𝑥 , 𝑥 , 𝑥 . Use the formulas (1) to update sequentially.
1 2 3
Solution: Let’s label the prior mean and variance as 𝜇 and 𝜎2. The updated means and
0 0
variances will be 𝜇 and 𝜎2. In sequence we have
𝑖 𝑖
1 1 1 𝜇 𝜇 𝑥
= + ; 1 = 0 + 1
𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2
1 0 1 0
1 1 1 1 2 𝜇 𝜇 𝑥 𝜇 𝑥 +𝑥
= + = + ; 2 = 1 + 2 = 0 + 1 2
𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2
2 1 0 2 1 0
1 1 1 1 3 𝜇 𝜇 𝑥 𝜇 𝑥 +𝑥 +𝑥
= + = + ; 3 = 2 + 3 = 0 + 1 2 3
𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2
3 2 0 3 2 0
The example generalizes to 𝑛 data values 𝑥 ,…,𝑥 :
1 𝑛
Normal-normal update formulas for 𝑛 data points
𝜇 𝜇 𝑛𝑥̄ 1 1 𝑛 𝑥 +…+𝑥
post = prior + , = + , 𝑥̄= 1 𝑛. (3)
𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝜎2 𝑛
post prior post prior
Again we give the easier to read form, showing 𝜇 is a weighted average of 𝜇 and the
post prior
sample average 𝑥:̄
1 𝑛 𝑎𝜇 +𝑏𝑥̄ 1
𝑎 = 𝑏 = , 𝜇 = prior , 𝜎2 = . (4)
𝜎2 𝜎2 post 𝑎+𝑏 post 𝑎+𝑏
prior
Interpretation: 𝜇 is a weighted average of 𝜇 and 𝑥.̄ If the number of data points is
post prior
large then the weight 𝑏 is large and 𝑥̄ will have a strong influence on the posterior. If 𝜎2
prior
is small then the weight 𝑎 is large and 𝜇 will have a strong influence on the posterior.
prior
To summarize:
1. Lots of data has a big influence on the posterior.
2. High certainty (low variance) in the prior has a big influence on the posterior.
The actual posterior is a balance of these two influences.
Choosing priors
Class 16, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Learn that the choice of prior affects the posterior.
2. See that too rigid a prior can make it diﬀicult to learn from the data.
3. See that more data lessens the dependence of the posterior on the prior.
4. Be able to make a reasonable choice of prior, based on prior understanding of the system
under consideration.
2 Introduction
Up to now we have always been handed a prior pdf. In this case, statistical inference from
data is essentially an application of Bayes’ theorem. When the prior is known there is no
controversy on how to proceed. The art of statistics starts when the prior is not known
with certainty. There are two main schools on how to proceed in this case: Bayesian and
frequentist. For now we are following the Bayesian approach. Starting next week we will
learn the frequentist approach.
Recall that given data 𝐷 and a hypothesis 𝐻 we used Bayes’ theorem to write
𝑃(𝐷|𝐻)⋅𝑃(𝐻)
𝑃(𝐻|𝐷) =
𝑃(𝐷)
posterior ∝ likelihood⋅prior.
Bayesian: Bayesians make inferences using the posterior 𝑃(𝐻|𝐷), and therefore always
need a prior 𝑃(𝐻). If a prior is not known with certainty the Bayesian must try to make
a reasonable choice. There are many ways to do this and reasonable people might make
different choices. In general it is good practice to justify your choices and to explore a range
of priors to see if they all point to the same conclusion.
Frequentist: Very briefly, frequentists do not try to create a prior. Instead, they make
inferences using the likelihood 𝑃(𝐷|𝐻).
We will compare the two approaches in detail once we have more experience with each. For
now we simply list two benefits of the Bayesian approach.
1. Theposteriorprobability𝑃(𝐻|𝐷)forthehypothesisgiventheevidenceisusuallyexactly
what we’d like to know. The Bayesian can say something like ‘the parameter of interest has
probability 0.95 of being between 0.49 and 0.51.’
2. The assumptions that go into choosing the prior can be clearly spelled out.
More good data: It is always the case that more and better data allows for stronger
conclusions and lessens the influence of the prior. The emphasis should be as much on
better data (quality) as on more data (quantity).
1
18.05 Class 16, Choosing priors, Spring 2022 2
3 Example: Dice
Suppose we have a drawer full of dice, each of which has either 4, 6, 8, 12, or 20 sides. This
time, we do not know how many of each type are in the drawer. A die is picked at random
from the drawer and rolled 5 times. The results in order are 4, 2, 4, 7, and 5.
3.1 Uniform prior
Suppose we have no idea what the distribution of dice in the drawer might be. In this case
it’s reasonable to use a flat prior. Here is the update table for the posterior probabilities
that result from updating after each roll. In order to fit all the columns, we leave out the
Bayes numerators.
hyp. prior lik post lik post lik post lik post lik post
1 1 2 2 3 3 4 4 5 5
𝐻 1/5 1/4 0.370 1/4 0.542 1/4 0.682 0 0.000 0 0.000
4
𝐻 1/5 1/6 0.247 1/6 0.241 1/6 0.202 0 0.000 1/6 0.000
6
𝐻 1/5 1/8 0.185 1/8 0.135 1/8 0.085 1/8 0.818 1/8 0.876
8
𝐻 1/5 1/12 0.123 1/12 0.060 1/12 0.025 1/12 0.161 1/12 0.115
12
𝐻 1/5 1/20 0.074 1/20 0.022 1/20 0.005 1/20 0.021 1/20 0.009
20
This should look familiar. Given the data the final posterior is heavily weighted towards
hypthesis 𝐻 that the 8-sided die was picked.
8
3.2 Other priors
To see how much the above posterior depended on our choice of prior, let’s try some other
priors. Suppose we have reason to believe that there are ten times as many 20-sided dice
in the drawer as there are each of the other types. The table becomes:
hyp. prior lik post lik post lik post lik post lik post
1 1 2 2 3 3 4 4 5 5
𝐻 0.071 1/4 0.222 1/4 0.453 1/4 0.650 0 0.000 0 0.000
4
𝐻 0.071 1/6 0.148 1/6 0.202 1/6 0.193 0 0.000 1/6 0.000
6
𝐻 0.071 1/8 0.111 1/8 0.113 1/8 0.081 1/8 0.688 1/8 0.810
8
𝐻 0.071 1/12 0.074 1/12 0.050 1/12 0.024 1/12 0.136 1/12 0.107
12
𝐻 0.714 1/20 0.444 1/20 0.181 1/20 0.052 1/20 0.176 1/20 0.083
20
Even here the final posterior is heavily weighted to the hypothesis 𝐻 .
8
What if the 20-sided die is 100 times more likely than each of the others?
hyp. prior lik post lik post lik post lik post lik post
1 1 2 2 3 3 4 4 5 5
𝐻 0.0096 1/4 0.044 1/4 0.172 1/4 0.443 0 0.000 0 0.000
4
𝐻 0.0096 1/6 0.030 1/6 0.077 1/6 0.131 0 0.000 1/6 0.000
6
𝐻 0.0096 1/8 0.022 1/8 0.043 1/8 0.055 1/8 0.266 1/8 0.464
8
𝐻 0.0096 1/12 0.015 1/12 0.019 1/12 0.016 1/12 0.053 1/12 0.061
12
𝐻 0.9615 1/20 0.889 1/20 0.689 1/20 0.354 1/20 0.681 1/20 0.475
20
With such a strong prior belief in the 20-sided die, the final posterior gives a lot of weight
to the theory that the data arose from a 20-sided die, even though it extremely unlikely the
18.05 Class 16, Choosing priors, Spring 2022 3
20-sided die would produce a maximum of 7 in 5 roles. The posterior now gives roughly
even odds that an 8-sided die versus a 20-sided die was picked.
3.3 Rigid priors
Mild cognitive dissonance. Too rigid a prior belief can overwhelm any amount of data.
Suppose I’ve got it in my head that the die has to be 20-sided. So I set my prior to
𝑃(𝐻 ) = 1 with the other 4 hypotheses having probability 0. Look what happens in the
20
update table.
hyp. prior lik post lik post lik post lik post lik post
1 1 2 2 3 3 4 4 5 5
𝐻 0 1/4 0 1/4 0 1/4 0 0 0 0 0
4
𝐻 0 1/6 0 1/6 0 1/6 0 0 0 1/6 0
6
𝐻 0 1/8 0 1/8 0 1/8 0 1/8 0 1/8 0
8
𝐻 0 1/12 0 1/12 0 1/12 0 1/12 0 1/12 0
12
𝐻 1 1/20 1 1/20 1 1/20 1 1/20 1 1/20 1
20
Nomatterwhatthedata, ahypothesiswithpriorprobability0willhaveposteriorprobabil-
ity 0. In this case I’ll never get away from the hypothesis 𝐻 , although I might experience
20
some mild cognitive dissonance.
Severe cognitive dissonance. Rigid priors can also lead to absurdities. Suppose I now
have it in my head that the die must be 4-sided. So I set 𝑃(𝐻 ) = 1 and the other prior
4
probabilities to 0. With the given data on the fourth roll I reach an impasse. A roll of 7
can’t possibly come from a 4-sided die. Yet this is the only hypothesis I’ll allow. My Bayes
numerator is a column of all zeros which cannot be normalized.
hyp. prior lik post lik post lik post lik Bayes numer post
1 1 2 2 3 3 4 4 4
𝐻 1 1/4 1 1/4 1 1/4 1 0 0 ???
4
𝐻 0 1/6 0 1/6 0 1/6 0 0 0 ???
6
𝐻 0 1/8 0 1/8 0 1/8 0 1/8 0 ???
8
𝐻 0 1/12 0 1/12 0 1/12 0 1/12 0 ???
12
𝐻 0 1/20 0 1/20 0 1/20 0 1/20 0 ???
20
I must adjust my belief about what is possible or, more likely, I’ll suspect you of accidently
or deliberately messing up the data.
4 Example: Malaria
Here is a real example adapted from Statistics, A Bayesian Perspective by Donald Berry:
By the 1950s scientists had begun to formulate the hypothesis that carriers of the sickle-cell
gene were more resistant to malaria than noncarriers. There was a fair amount of circum-
stantial evidence for this hypothesis. It also helped explain the persistance of an otherwise
deleterious gene in the population. In one experiment scientists injected 30 African volun-
teers with malaria. Fifteen of the volunteers carried one copy of the sickle-cell gene and the
other 15 were noncarriers. Fourteen out of 15 noncarriers developed malaria while only 2
18.05 Class 16, Choosing priors, Spring 2022 4
out of 15 carriers did. Does this small sample support the hypothesis that the sickle-cell
gene protects against malaria?
Let 𝑆 represent a carrier of the sickle-cell gene and 𝑁 represent a non-carrier. Let 𝐷+
indicate developing malaria and 𝐷− indicate not developing malaria. The data can be put
in a table.
𝐷+ 𝐷−
𝑆 2 13 15
𝑁 14 1 15
16 14 30
Beforeanalysingthedataweshouldsayafewwordsabouttheexperimentandexperimental
design. First, it is clearly unethical: to gain some information they infected 16 people with
malaria. We also need to worry about bias. How did they choose the test subjects? Is
it possible the noncarriers were weaker and thus more susceptible to malaria than the
carriers? Berry points out that it is reasonable to assume that an injection is similar to
a mosquito bite, but it is not guaranteed. This last point means that if the experiment
shows a relation between sickle-cell and protection against injected malaria, we need to
consider the hypothesis that the protection from mosquito transmitted malaria is weaker or
non-existent. Finally, we will frame our hypothesis as ’sickle-cell protects against malaria’,
but really all we can hope to say from a study like this is that ’sickle-cell is correlated with
protection against malaria’.
Model. For our model let 𝜃 be the probability that an injected carrier 𝑆 develops malaria
𝑆
and likewise let 𝜃 be the probability that an injected noncarrier 𝑁 develops malaria. We
𝑁
assumeindependencebetweenalltheexperimentalsubjects. Withthismodel,thelikelihood
is a function of both 𝜃 and 𝜃 :
𝑆 𝑁
𝑃(data|𝜃 ,𝜃 ) = 𝑐𝜃2(1−𝜃 )13𝜃14(1−𝜃 ).
𝑆 𝑁 𝑆 𝑆 𝑁 𝑁
As usual we leave the constant factor 𝑐 as a letter. (It is a product of two binomial
coeﬀicients: 𝑐 = (15)(15).)
2 14
Hypotheses. Each hypothesis consists of a pair (𝜃 ,𝜃 ). To keep things simple we will
𝑁 𝑆
only consider a finite number of values for these probabilities. We could easily consider
many more values or even a continuous range of hypotheses. Assume 𝜃 and 𝜃 are each
𝑆 𝑁
one of 0, 0.2, 0.4, 0.6, 0.8, 1. This leads to two-dimensional tables.
First is a table of hypotheses. The color coding indicates the following:
1. Light blue squares along the diagonal are where 𝜃 = 𝜃 , i.e. sickle-cell makes no
𝑆 𝑁
difference one way or the other.
2. Orange and darker blue squares above the diagonal are where 𝜃 > 𝜃 , i.e. sickle-cell
𝑁 𝑆
provides some protection against malaria.
3. In the orange squares 𝜃 −𝜃 ≥ 0.6, i.e. sickle-cell provides a lot of protection.
𝑁 𝑆
4. White squares below diagonal are where 𝜃 > 𝜃 , i.e. sickle-cell actually increases the
𝑆 𝑁
probability of developing malaria.
18.05 Class 16, Choosing priors, Spring 2022 5
𝜃 \𝜃 0 0.2 0.4 0.6 0.8 1
𝑁 𝑆
1 (0,1) (.2,1) (.4,1) (.6,1) (.8,1) (1,1)
0.8 (0,.8) (.2,.8) (.4,.8) (.6,.8) (.8,.8) (1,.8)
0.6 (0,.6) (.2,.6) (.4,.6) (.6,.6) (.8,.6) (1,.6)
0.4 (0,.4) (.2,.4) (.4,.4) (.6,.4) (.8,.4) (1,.4)
0.2 (0,.2) (.2,.2) (.4,.2) (.6,.2) (.8,.2) (1,.2)
0 (0,0) (.2,0) (.4,0) (.6,0) (.8,0) (1,0)
Hypotheses on level of protection due to 𝑆:
orange = strong; darker blue = some; light blue = none; white = negative.
Next is the table of likelihoods. (Actually we’ve taken advantage of our indifference to scale
andscaledallthelikelihoodsby100000/𝑐 tomakethetablemorepresentable.) Noticethat,
to the precision of the table, many of the likelihoods are 0. The color coding is the same as
in the hypothesis table. We’ve highlighted the biggest likelihoods with a thick black border.
𝜃 \𝜃 0 0.2 0.4 0.6 0.8 1
𝑁 𝑆
1 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000
0.8 0.00000 1.93428 0.18381 0.00213 0.00000 0.00000
0.6 0.00000 0.06893 0.00655 0.00008 0.00000 0.00000
0.4 0.00000 0.00035 0.00003 0.00000 0.00000 0.00000
0.2 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000
0 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000
Likelihoods 𝑝(data|𝜃 ,𝜃 ) scaled by 100000/𝑐
𝑆 𝑁
4.1 Flat prior
Suppose we have no opinion whatsoever on whether and to what degree sickle-cell protects
againstmalaria. Inthiscaseitisreasonabletouseaflatprior. Sincethereare36hypotheses
each one gets a prior probability of 1/36. This is given in the table below. Remember each
square in the table represents one hypothesis. Because it is a probability table we include
the marginal pmfs.
𝜃 \𝜃 0 0.2 0.4 0.6 0.8 1 𝑝(𝜃 )
𝑁 𝑆 𝑁
1 1/36 1/36 1/36 1/36 1/36 1/36 1/6
0.8 1/36 1/36 1/36 1/36 1/36 1/36 1/6
0.6 1/36 1/36 1/36 1/36 1/36 1/36 1/6
0.4 1/36 1/36 1/36 1/36 1/36 1/36 1/6
0.2 1/36 1/36 1/36 1/36 1/36 1/36 1/6
0 1/36 1/36 1/36 1/36 1/36 1/36 1/6
𝑝(𝜃 ) 1/6 1/6 1/6 1/6 1/6 1/6 1
𝑆
Flat prior 𝑝(𝜃 ,𝜃 ): every hypothesis (square) has equal probability
𝑆 𝑁
To compute the posterior we simply multiply the likelihood table by the prior table and
18.05 Class 16, Choosing priors, Spring 2022 6
normalize. Normalization means making sure the entire table sums to 1.
𝜃 \𝜃 0 0.2 0.4 0.6 0.8 1 𝑝(𝜃 |data)
𝑁 𝑆 𝑁
1 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000
0.8 0.00000 0.88075 0.08370 0.00097 0.00000 0.00000 0.96542
0.6 0.00000 0.03139 0.00298 0.00003 0.00000 0.00000 0.03440
0.4 0.00000 0.00016 0.00002 0.00000 0.00000 0.00000 0.00018
0.2 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000
0 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000
𝑝(𝜃 |data) 0.00000 0.91230 0.08670 0.00100 0.00000 0.00000 1.00000
𝑆
Posterior to flat prior: 𝑝(𝜃 ,𝜃 |data)
𝑆 𝑁
To decide whether 𝑆 confers protection against malaria, we compute the posterior proba-
bilities of ‘some protection’ and of ‘strong protection’. These are computed by summing the
corresponding squares in the posterior table.
Some protection: 𝑃(𝜃 > 𝜃 ) = sum of orange and darker blue = 0.99995
𝑁 𝑆
Strong protection: 𝑃(𝜃 −𝜃 > 0.6) = sum of orange = 0.88075
𝑁 𝑆
Working from the flat prior, it is effectively certain that sickle-cell provides some protection
and very probable that it provides strong protection.
4.2 Informed prior
The experiment was not run without prior information. There was a lot of circumstantial
evidence that the sickle-cell gene offered some protection against malaria. For example it
was reported that a greater percentage of carriers survived to adulthood.
Here’s one way to build an informed prior. We’ll reserve a reasonable amount of probability
for the hypotheses that 𝑆 gives no protection. Let’s say 24% split evenly among the 6 (light
blue) cells where 𝜃 = 𝜃 . We know we shouldn’t set any prior probabilities to 0, so let’s
𝑁 𝑆
spread 6% of the probability evenly among the 15 white cells below the diagonal. That
leaves 70% of the probability for the 15 orange and darker blue squares above the diagonal.
𝜃 \𝜃 0 0.2 0.4 0.6 0.8 1 𝑝(𝜃 )
𝑁 𝑆 𝑁
1 0.04667 0.04667 0.04667 0.04667 0.04667 0.04000 0.27333
0.8 0.04667 0.04667 0.04667 0.04667 0.04000 0.00400 0.23067
0.6 0.04667 0.04667 0.04667 0.04000 0.00400 0.00400 0.18800
0.4 0.04667 0.04667 0.04000 0.00400 0.00400 0.00400 0.14533
0.2 0.04667 0.04000 0.00400 0.00400 0.00400 0.00400 0.10267
0 0.04000 0.00400 0.00400 0.00400 0.00400 0.00400 0.06000
𝑝(𝜃 ) 0.27333 0.23067 0.18800 0.14533 0.10267 0.06000 1.0
𝑆
Informed prior 𝑝(𝜃 ,𝜃 ): makes use of prior information that sickle-cell is protective.
𝑆 𝑁
We then compute the posterior pmf.
18.05 Class 16, Choosing priors, Spring 2022 7
𝜃 \𝜃 0 0.2 0.4 0.6 0.8 1 𝑝(𝜃 |data)
𝑁 𝑆 𝑁
1 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000
0.8 0.00000 0.88076 0.08370 0.00097 0.00000 0.00000 0.96543
0.6 0.00000 0.03139 0.00298 0.00003 0.00000 0.00000 0.03440
0.4 0.00000 0.00016 0.00001 0.00000 0.00000 0.00000 0.00017
0.2 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000
0 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000 0.00000
𝑝(𝜃 |data) 0.00000 0.91231 0.08669 0.00100 0.00000 0.00000 1.00000
𝑆
Posterior to informed prior: 𝑝(𝜃 ,𝜃 |data)
𝑆 𝑁
We again compute the posterior probabilities of ‘some protection’ and ‘strong protection’.
Some protection: 𝑃(𝜃 > 𝜃 ) = sum of orange and darker blue = 0.99996
𝑁 𝑆
Strong protection: 𝑃(𝜃 −𝜃 > 0.6) = sum of orange = 0.88076
𝑁 𝑆
Note that the informed posterior is nearly identical to the flat posterior.
4.3 PDALX
The following plot is based on the flat prior. For each 𝑥, it gives the probability that
𝜃 −𝜃 ≥ 𝑥. To make it smooth we used many more hypotheses.
𝑁 𝑆
0.0 0.2 0.4 0.6 0.8 1.0
0.1
8.0
6.0
4.0
2.0
0.0
x
x
tsael
ta
.ffid
.borP
Probability the difference 𝜃 −𝜃 is at least 𝑥 (PDALX).
𝑁 𝑆
Notice that it is almost certain that the difference is at least 0.4.
Probability intervals
Class 16, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to find probability intervals given a pmf or pdf.
2. Understand how probability intervals summarize belief in Bayesian updating.
3. Be able to use subjective probability intervals to construct reasonable priors.
4. Be able to construct subjective probability intervals by systematically estimating quan-
tiles.
2 Probability intervals
Supposewehaveapmf𝑝(𝜃)orpdf𝑓(𝜃)describingourbeliefaboutthevalueofanunknown
parameter of interest 𝜃.
Definition: A 𝑝-probability interval for 𝜃 is an interval [𝑎,𝑏] with 𝑃(𝑎 ≤ 𝜃 ≤ 𝑏) = 𝑝.
Notes.
1. In the discrete case with pmf 𝑝(𝜃), this means ∑ 𝑝(𝜃 ) = 𝑝.
𝑎≤𝜃 ≤𝑏 𝑖
𝑖
𝑏
2. In the continuous case with pdf 𝑓(𝜃), this means ∫ 𝑓(𝜃)𝑑𝜃 = 𝑝.
𝑎
3. We may say 90%-probability interval to mean 0.9-probability interval. Probability
intervals are also called credible intervals to contrast them with confidence intervals, which
we will introduce in the frequentist unit.
Example 1. Between the 0.05 and 0.55 quantiles is a 0.5 probability interval. There are
many 50% probability intervals, e.g. the interval from the 0.25 to the 0.75 quantiles.
In particular, notice that the 𝑝-probability interval for 𝜃 is not unique.
Q-notation. We can phrase probability intervals in terms of quantiles. Recall that the
𝑠-quantile for 𝜃 is the value 𝑞 with 𝑃(𝜃 ≤ 𝑞 ) = 𝑠. So for 𝑠 ≤ 𝑡, the amount of probability
𝑠 𝑠
between the 𝑠-quantile and the 𝑡-quantile is just 𝑡 − 𝑠. In these terms, a 𝑝-probability
interval is any interval [𝑞 ,𝑞 ] with 𝑡−𝑠 = 𝑝.
𝑠 𝑡
Example 2. We have 0.5 probability intervals [𝑞 ,𝑞 ] and [𝑞 ,𝑞 ].
0.25 0.75 0.05 0.55
Symmetric probability intervals.
Theinterval[𝑞 ,𝑞 ]issymmetricbecausetheamountofprobabilityremainingoneither
0.25 0.75
side of the interval is the same, namely 0.25. If the pdf is not too skewed, the symmetric
interval is usually a good default choice.
More notes.
1
18.05 Class 16, Probability intervals, Spring 2022 2
1. Different 𝑝-probability intervals for 𝜃 may have different widths. We can make the width
smaller by centering the interval under the highest part of the pdf. Such an interval is
usually a good choice since it contains the most likely values. See the examples below for
normal and beta distributions.
2. Since the width can vary for fixed 𝑝, a larger 𝑝 does not always mean a larger width.
Here’swhatistrue: ifa𝑝 -probabilityintervalisfullycontainedina𝑝 -probabilityinterval,
1 2
then 𝑝 is smaller than 𝑝 .
1 2
Probability intervals for a normal distribution. The figure shows a number of prob-
ability intervals for the standard normal.
1. All of the blue bars span a 0.68-probability interval. Notice that the smallest blue bar
runs between -1 and 1. This runs from the 16th percentile to the 84th percentile so it is a
symmetric interval.
2. All the green bars span a 0.9-probability interval. They are longer than the blue bars
becausetheyincludemoreprobability. Noteagainthattheshortestgreenbarissymmetric.
−3 −2 −1 0 1 2 3
4.0
3.0
2.0
1.0
0.0
1.0−
N(0, 1)
orange = 0.5, blue = 0.68, green = 0.9
Probabilitiy intervals for a beta distribution. The following figure shows probability
intervals for a beta distribution. Notice how the two blue bars have very different lengths
yet cover the same probability 𝑝 = 0.68.
0.0 0.2 0.4 0.6 0.8 1.0
3
2
1
0
beta(10, 4)
orange = 0.5, blue = 0.68, green = 0.9
18.05 Class 16, Probability intervals, Spring 2022 3
3 Uses of probability intervals
3.1 Summarizing and communicating your beliefs
Probabilityintervalsareanintuitiveandeffectivewaytosummarizeandcommunicateyour
beliefs. It’shardtodescribeanentirefunction𝑓(𝜃)toafriendinwords. Ifthefunctionisn’t
from a parameterized family then it’s especially hard. Even with a beta distribution, it’s
easier to interpret “I think 𝜃 is between 0.45 and 0.65 with 50% probability” than “I think 𝜃
follows a beta(8,6) distribution”. An exception to this rule of communication might be the
normal distribution, but only if the recipient is also comfortable with standard deviation.
Of course, what we gain in clarity we lose in precision, since the function contains more
information than the probability interval.
Probability intervals also play well with Bayesian updating. If we update from the prior
𝑓(𝜃) to the posterior 𝑓(𝜃|𝑥), then the 𝑝-probability interval for the posterior will tend to be
shorter than than the 𝑝-probability interval for the prior. In this sense, the data has made
us more certain. See for example the election example below.
4 Constructing a prior using subjective probability intervals
Probability intervals are also useful when we do not have a pmf or pdf at hand. In this
case, subjective probability intervals give us a method for constructing a reasonable prior
for 𝜃 “from scratch”. The thought process is to ask yourself a series of questions, e.g., ‘what
is my expected value for 𝜃?’; ‘my 0.5-probability interval?’; ‘my 0.9-probability interval?’
Then build a prior that is consistent with these intervals.
4.1 Estimating the intervals directly
Example 3. Building priors
In 2013 there was a special election for a congressional seat in a district in South Carolina.
The election pitted Republican Mark Sanford against Democrat Elizabeth Colbert Busch.
Let 𝜃 be the fraction of the population who favored Sanford. Our goal in this example is
to build a subjective prior for 𝜃. We’ll use the following prior evidence.
• Sanford is a former S. Carolina Congressman and Governor
• In 2009, while Governor, he had to resign after he was discovered to be having an
affair in Argentina while he claimed to be hiking the Appalachian trail.
• In 2013 Sanford won the Republican primary over 15 primary opponents.
• In the district in the 2012 presidential election the Republican Romney beat the
Democrat Obama 58% to 40%.
• The Colbert bump: Elizabeth Colbert Busch is the sister of well-known comedian
Stephen Colbert.
18.05 Class 16, Probability intervals, Spring 2022 4
Our strategy will be to use our intuition to construct some probability intervals and then
find a beta distribution that approximately matches these intervals. This is subjective so
someone else might give a different answer.
Step 1. Use the evidence to construct 0.5 and 0.9 probability intervals for 𝜃.
We’ll start by thinking about the 90% interval. The single strongest prior evidence is the
58% to 40% of Romney over Obama. Given the negatives for Sanford we don’t expect he’ll
win much more than 58% of the vote. So we’ll put the top of the 0.9 interval at 0.65. With
all of Sanford’s negatives he could lose big. So we’ll put the bottom at 0.3.
0.9 interval: [0.3, 0.65]
For the 0.5 interval we’ll pull these endpoints in. It really seems unlikely Sanford will get
more votes than Romney, so we can leave 0.25 probability that he’ll get above 57%. The
lower limit seems harder to predict. So we’ll leave 0.25 probability that he’ll get under 42%.
0.5 interval: [0.42, 0.57]
Step 2. Use our 0.5 and 0.9 probability intervals to pick a beta distribution that approx-
imats these intervals. We used the R function pbeta and a little trial and error to choose
beta(11,12). Here is our R code.
a = 11
b = 12
pbeta(0.65, a, b) - pbeta(0.3, a, b)
pbeta(0.57, a, b) - pbeta(0.42, a, b)
Thiscomputed𝑃([0.3,0.65]) = 0.91and𝑃([0.42,0.57]) = 0.52. Soourintervalsareactually
0.91 and 0.52-probability intervals. This is pretty close to what we wanted!
The plot below shows the density of beta(11,12). The horizontal orange line shows our
interval [0.42, 0.57] and the blue line shows our interval [0.3, 0.65].
0.0 0.2 0.4 0.6 0.8 1.0
3
2
1
0
PDF for beta(11,12)
[0.42, 0.57] = 0.91 interval
[0.3, 0.65] = 0.52 interval
q
beta(11,12) fitting 0.5 and 0.9 probability intervals
4.2 Constructing a prior by estimating quantiles
The method in Example 3 gives a good feel for building priors from probability intervals.
Here we illustrate a slightly different way of building a prior by estimating quantiles. The
18.05 Class 16, Probability intervals, Spring 2022 5
basic strategy is to first estimate the median, then divide and conquer to estimate the first
and third quantiles. Finally you choose a prior distribution that fits these estimates.
Example 4. Redo the Sanford vs. Colbert-Busch election example using quantiles.
Solution: We start by estimating the median. Just as before the single strongest evidence
is the 58% to 40% victory of Romney over Obama. However, given Sanford’s negatives and
Busch’s Colbert bump we’ll estimate the median at 0.47.
In a district that went 58 to 40 for the Republican Romney it’s hard to imagine Sanford’s
vote going a lot below 40%. So we’ll estimate Sanford 25th percentile as 0.40. Likewise,
given his negatives it’s hard to imagine him going above 58%, so we’ll estimate his 75th
percentile as 0.55.
We used R to search through values of 𝑎 and 𝑏 for the beta distribution that matches these
quartiles the best. Since the beta distribution does not require 𝑎 and 𝑏 to be integers we
looked for the best fit to 1 decimal place. We found beta(9.9, 11.0). Above is a plot of
beta(9.9,11.0) with its actual quartiles shown. These match the desired quartiles pretty
well.
0.0 0.2 0.4 0.6 0.8 1.0
3
2
1
0
PDF for beta(9.9,11.0)
q0.25 =0.399
q0.5 =0.472
q0.75 =0.547
q
beta(9.9, 11.0) matching desired quartiles
Historic note. In the election Sanford won 54% of the vote and Busch won 45.2%. (Source:
https://elections.huffingtonpost.com/2013/mark-sanford-vs-elizabeth-colbert-busch-sc1
The Frequentist School of Statistics
Class 17, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to explain the difference between the frequentist and Bayesian approaches to
statistics.
2. Know our working definition of a statistic and be able to distinguish a statistic from a
non-statistic.
2 Introduction
After much foreshadowing, the time has finally come to switch from Bayesian statistics to
frequentist statistics. For much of the twentieth century, frequentist statistics has been the
dominant school. If you’ve ever encountered confidence intervals, 𝑝-values, 𝑡-tests, or 𝜒2-
tests,you’veseenfrequentiststatistics. Withtheriseofhigh-speedcomputingandbigdata,
Bayesian methods are becoming more common. After we’ve studied frequentist methods
we will compare the strengths and weaknesses of the two approaches.
2.1 The fork in the road
Both schools of statistics start with probability. In particular both know and love Bayes’
theorem:
𝑃(𝐷|𝐻)𝑃(𝐻)
𝑃(𝐻|𝐷) = .
𝑃(𝐷)
When the prior is known exactly, all statisticians will use Bayes’ formula. For Bayesian
inference we take 𝐻 to be a hypothesis and 𝐷 some data. Over the last few weeks we
have seen that, given a prior and a likelihood model, Bayes’ theorem is a complete recipe
for updating our beliefs in the face of new data. This works perfectly when the prior was
known perfectly. We saw this in our dice examples. We also saw examples of a disease with
a known frequency in the general population and a screening test of known accuracy.
In practice we saw that there is usually no universally accepted prior – different people
will have different a priori beliefs – but we would still like to make useful inferences from
data. Bayesians and frequentists take fundamentally different approaches to this challenge,
as summarized in the figure below.
1
18.05 Class 17, The Frequentist School of Statistics, Spring 2022 2
Everyone uses Bayes’
𝑃(𝐷|𝐻)𝑃(𝐻)
Probability 𝑃(𝐻|𝐷)= formula when the prior
𝑃(𝐷)
(mathematics) 𝑃(𝐻) is known.
Bayesian path Frequentist path
Statistics
(art)
𝑃(𝐷|𝐻)𝑃 (𝐻)
𝑃 (𝐻|𝐷)= prior Likelihood 𝐿(𝐻;𝐷)=𝑃(𝐷|𝐻)
Posterior 𝑃(𝐷)
Bayesians require a prior, so Without a known prior, frequen-
they develop one from the best tists draw inferences from just
information they have. the likelihood function.
The reasons for this split are both practical (ease of implementation and computation) and
philosophical (subjectivity versus objectivity and the nature of probability).
2.2 What is probability?
Themainphilosophicaldifferenceconcernsthemeaningofprobability. Thetermfrequentist
refers to the idea that probabilities represent long term frequencies of repeatable random
experiments. For example, ‘a coin has probability 1/2 of heads’ means that the relative
frequency of heads (number of heads out of number of flips) goes to 1/2 as the number of
flips goes to infinity. This means the frequentist finds it nonsensical to specify a probability
distributionforaparameterwithafixedvalue. WhileBayesiansarehappytouseprobability
to describe their incomplete knowledge of a fixed parameter, frequentists reject the use of
probability to quantify degree of belief in hypotheses.
Example 1. Suppose I have a bent coin with unknown probability 𝜃 of heads. The value
of 𝜃 may be unknown, but it is a fixed value. Thus, to the frequentist there can be no prior
pdf 𝑓(𝜃). By comparison the Bayesian may agree that 𝜃 has a fixed value, but interprets
𝑓(𝜃) as representing uncertainty about that value. Both the Bayesian and the frequentist
are perfectly happy with 𝑝(heads|𝜃) = 𝜃, since the longterm frequency of heads given 𝜃 is
𝜃.
Inshort,Bayesiansputprobabilitydistributionsoneverything(hypothesesanddata),while
frequentists put probability distributions on (random, repeatable, experimental) data given
a hypothesis. For the frequentist when dealing with data from an unknown distribution
only the likelihood has meaning. The prior and posterior do not.
3 Working definition of a statistic
Our view of statistics is that it is the art of drawing conclusions (making inferences) from
data. With that in mind we can make a simple working definition of a statistic. There is a
more formal definition, but we don’t need to introduce it at this point.
18.05 Class 17, The Frequentist School of Statistics, Spring 2022 3
Statistic. Astatisticisanythingthatcanbecomputedfromdataandknownvalues. Some-
times to be more precise we’ll say a statistic is a rule for computing something from data
and the value of the statistic is what is computed. This can include computing likelihoods
where we hypothesize values of the model parameters. But it does not include anything
that requires we know the true value of a model parameter with unknown value.
Examples. 1. The mean of data is a statistic. It is a rule that says given data 𝑥 ,…,𝑥
1 𝑛
compute 𝑥 1 +…+𝑥 𝑛.
𝑛
2. The maximum of data is a statistic. It is a rule that says to pick the maximum value of
the data 𝑥 ,…,𝑥 .
1 𝑛
3. Suppose 𝑥 ∼ N(𝜇,32) where 𝜇 is unknown. Then the likelihood
𝜙(𝑥|𝜇 = 7) = √
1 e−(𝑥−7)2
18
3 2𝜋
is a statistic. However, the distance of 𝑥 from the true mean 𝜇 is not a statistic since we
cannot compute it without knowing 𝜇
𝑥−5
4. If our data 𝑥 ,…,𝑥 is drawn from N(𝜇,32), where 𝜇 is unknown, then 𝑧 = √ is a
1 𝑛 3/ 𝑛
statistic, since it is computed from the data and known values. More generally, if 𝜇 is a
0
𝑥−𝜇 𝑥−𝜇
known value then 𝑧 = √ 0 is a statistic. However, since 𝜇 is not known, 𝑧 = √ is
3/ 𝑛 3/ 𝑛
not a statistic.
Note. WewillusuallystickwithourBayesianpracticeofusingthesymbol𝜙forcontinuous
likelihoods. This will help remind us that Frequentists don’t have prior and posterior
probabilities for hypotheses.
Point statistic. A point statistic is a single value computed from data. For example, the
mean and the maximum are both point statistics. The maximum likelihood estimate is also
a point statistic since it is computed directly from the data based on a likelihood model.
Interval statistic. An interval statistic is an interval computed from data. For example,
the range from the minimum to maximum of 𝑥 ,…,𝑥 is an interval statistic, e.g. the data
1 𝑛
0.5, 1.0, 0.2, 3.0, 5.0 has range [0.2, 5.0].
Set statistic. A set statistic is a set computed from data.
Example. Suppose we have five dice: 4, 6, 8, 12 and 20-sided. We pick one at random and
roll it once. The value of the roll is the data. The set of dice for which this roll is possible
is a set statistic. For example, if the roll is a 10 then the value of this set statistic is {12,
20}. If the roll is a 7 then this set statistic has value {8, 12, 20}.
It’s important to remember that a statistic is itself a random variable since it is computed
from random data. For example, if data is drawn from N(𝜇,𝜎2) then the mean of 𝑛 data
points follows the distribution N(𝜇,𝜎2/𝑛)).
Sampling distribution. The probability distribution of a statistic is called its sampling
distribution.
Point estimate. We can use statistics to make a point estimate of a parameter 𝜃. For
example, if our data is drawn from a normal distribution with unknown mean 𝜃. Then the
data mean 𝑥̄ is a point estimate of 𝜃.
Null Hypothesis Significance Testing I
Class 17, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Know the definitions of the significance testing terms: null hypothesis, alternative hy-
pothesis, NHST, simple hypothesis, composite hypothesis, significance level, power.
2. Be able to design and run a significance test for Bernoulli or binomial data.
3. Be able to compute a 𝑝-value for a normal hypothesis and use it in a significance test.
2 Introduction
Frequentiststatisticsisoftenappliedintheframeworkofnullhypothesissignificancetesting
(NHST). We will look at the Neyman-Pearson paradigm which focuses on one hypothesis
called the null hypothesis. There are other paradigms for hypothesis testing, but Neyman-
Pearson is the most common. Stated simply, this method asks if the data is well outside
the region where we would expect to see it under the null hypothesis. If so, then we reject
the null hypothesis in favor of a second hypothesis called the alternative hypothesis. The
reasoning is that such extreme data is very unlikely in a world where the null hypothesis is
true.
We have said before that statistics is an art. We will see that this statement is certainly
valid when we discuss choosing null and alternative hypotheses.
The computations done here all involve the likelihood function. There are two main differ-
ences between what we’ll do here and what we did in Bayesian updating.
1. The evidence of the data will be considered purely through the likelihood function: it
will not be weighted by our prior beliefs.
2. We will need a notion of extreme data, e.g. 95 out of 100 heads in a coin toss or a mayfly
that lives for a month.
2.1 A suggestion of how to learn this material
There are seemingly a lot of terms with similar definitions. If you pay careful attention
to the figures and how they are shaded and labeled we think you will find that is not so
complicated.
2.2 Motivating examples
Example 1. Suppose you want to decide whether a coin is fair. If you toss it 100 times
and get 85 heads, wouldyouthink the coin is likelyto be unfair? What about 60 heads? Or
52 heads? Most people would guess that 85 heads is strong evidence that the coin is unfair,
1
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 2
whereas 52 heads is no evidence at all. Sixtyheads is less clear. Null hypothesis significance
testing (NHST) is a frequentist approach to thinking quantitatively about these questions.
Example 2. Suppose you want to compare a new medical treatment to a placebo or
to the current standard of care. What sort of evidence would convince you that the new
treatmentisbetterthantheplaceboorthecurrentstandard? Again,NHSTisaquantitative
framework for answering these questions.
3 Significance testing
We’ll start by listing the ingredients for NHST. Formally they are pretty simple. There is
an art to choosing good ingredients. We will explore the art in examples. If you have never
seen NHST before just scan this list now and come back to it after reading through the
examples and explanations given below.
3.1 Ingredients
• 𝐻 : the null hypothesis. This is the default assumption for the model generating the
0
data.
• 𝐻 : the alternative hypothesis. If we reject the null hypothesis we accept this alter-
𝐴
native as the best explanation for the data.
• 𝑋: theteststatistic. Wecomputethisfromthedata. Itisarandomvariable, because
it is computed from random data.
• Null distribution: the probability distribution of 𝑋 assuming 𝐻 .
0
• Rejection region: if 𝑋 is in the rejection region we reject 𝐻 in favor of 𝐻 .
0 𝐴
• Non-rejection region: the complement to the rejection region. If 𝑋 is in this region
we do not reject 𝐻 . Note that we say ‘do not reject’ rather than ‘accept’ because
0
usually the best we can say is that the data does not support rejecting 𝐻 .
0
The null hypothesis 𝐻 and the alternative hypothesis 𝐻 play different roles. Typically
0 𝐴
we choose 𝐻 to be either a simple hypothesis or the default which we’ll only reject if we
0
have enough evidence against it. The examples below will clarify this.
4 NHST Terminology
In this section we will use one extended example to introduce and explore the terminology
used in null hypothesis significance testing (NHST).
Example 3. To test whether a coin is fair we flip it 10 times. If we get an unexpectedly
large or small number of heads we’ll suspect the coin is unfair. To make this precise in the
language of NHST we set up the ingredients as follows. Let 𝜃 be the probability that the
coin lands heads when flipped.
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 3
1. Null hypothesis: 𝐻 = ‘the coin is fair’, i.e. 𝜃 = 0.5.
0
2. Alternative hypothesis: 𝐻 = ‘the coin is not fair’, i.e. 𝜃 ≠ 0.5
𝐴
3. Test statistic: 𝑋 = number of heads in 10 flips
4. Null distribution: This is the probability function based on the null hypothesis
𝑝(𝑥|𝜃 = 0.5) ∼ binomial(10,0.5).
Here is the probability table for the null distribution.
𝑥 0 1 2 3 4 5 6 7 8 9 10
𝑝(𝑥|𝐻 ) .001 .010 .044 .117 .205 .246 .205 .117 .044 .010 .001
0
5. Rejection region: under the null hypothesis we expect to get about 5 heads in 10 tosses.
Whereas, under the alternate hypothesis we expect the number of heads to be biased either
above or below 5. So, we’ll reject 𝐻 in favor of 𝐻 if the number of heads is much fewer
0 𝐴
or greater than 5. Let’s set the rejection region as {0,1,2,8,9,10}. That is, if the number
of heads in 10 tosses is in this region we will reject the hypothesis that the coin is fair in
favor of the hypothesis that it is not.
We can summarize all this in the graph and probability table below. The rejection region
consists of those values of 𝑥 in orange, i.e. 0, 1, 2, 8, 9, 10. The probabilities corresponding
to it are shaded in orange. We also show the null distribution as a stem plot with the
rejection values of 𝑥 in orange.
𝑥 0 1 2 3 4 5 6 7 8 9 10
𝑝(𝑥|𝐻 ) 0.001 0.010 0.044 0.117 0.205 0.246 0.205 0.117 0.044 0.010 0.001
0
Rejection region and null probabilities as a table for Example 3.
𝑝(𝑥|𝐻 )
0
.25
.15
.05
𝑥
0 1 2 3 4 5 6 7 8 9 10
Rejection region and null probabilities as a stem plot for Example 3.
Notes for Example 3:
1. The null hypothesis is the cautious default: we won’t claim the coin is unfair unless we
have compelling evidence.
2. The rejection region consists of data that is extreme under the null hypothesis and more
likely under the alternative hypothesis. That is, it consists of the outcomes that are in the
tail of the null distribution away from the high probability center. As we’ll discuss soon,
how far away depends on the significance level 𝛼 of the test.
3. If we get 3 heads in 10 tosses, then the test statistic is in the non-rejection region. The
usual scientific language would be to say that the data ‘does not support rejecting the null
hypothesis’. Even if we got 5 heads, we would not claim that the data proves the null
hypothesis is true.
Question: If we have a fair coin what is the probability that we will decide incorrectly it
is unfair?
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 4
Solution: The null hypothesis is that the coin is fair. The question asks for the probability
the data from a fair coin will be in the rejection region. That is, the probability that we
will get 0, 1, 2, 8, 9 or 10 heads in 10 tosses. This is the sum of the probabilities in the
table in shaded orange boxes. That is,
𝑃(rejecting 𝐻 |𝐻 is true) = 0.11
0 0
Below we will continue with Example 3, define more terms used in NHST and see how to
quantify properties of the significance test.
4.1 Simple and composite hypotheses
Definition: simple hypothesis: A simple hypothesis is one for which we can specify its
distribution completely. A typical simple hypothesis is that a parameter of interest takes a
specific value.
Definition: composite hypotheses: If its distribution cannot be fully specified, we say
that the hypothesis is composite. A typical composite hypothesis is that a parameter of
interest lies in a range of values.
InExample3thenullhypothesisisthat𝜃 = 0.5,sothenulldistributionisbinomial(10,0.5).
Since the null distribution is fully specified, 𝐻 is simple. The alternative hypothesis is that
0
𝜃 ≠ 0.5. This is really many hypotheses in one: 𝜃 could be 0.51, 0.7, 0.99, etc. Since the
alternative distribution binomial(10,𝜃) is not fully specified, 𝐻 is composite.
𝐴
Example 4. Suppose we have data 𝑥 , …, 𝑥 . Suppose also that our hypotheses are
1 𝑛
𝐻 : the data is drawn from 𝑁(0,1)
0
𝐻 : the data is drawn from 𝑁(1,1).
𝐴
These are both simple hypotheses – each hypothesis completely specifies a distribution.
Example 5. (Composite hypotheses.) Now suppose that our hypotheses are
𝐻 : the data is drawn from a Poisson distribution of unknown parameter.
0
𝐻 : the data is not drawn from a Poisson distribution.
𝐴
These are both composite hypotheses, as they don’t fully specify the distribution.
Example 6. In an ESP experiment a subject is asked to identify the suits of 100 cards
drawn (with replacement) from a deck of cards. Let 𝑇 be the number of successes. The
(simple) null hypothesis that the subject does not have ESP is given by
𝐻 : 𝑇 ∼ binomial(100,0.25)
0
The (composite) alternative hypothesis that the subject has ESP is given by
𝐻 : 𝑇 ∼ binomial(100,𝑝) with 𝑝 > 0.25
𝐴
Another(composite) alternativehypothesisthat something besides purechanceis going on,
i.e. the subject has ESP or anti-ESP. This is given by
𝐻 : 𝑇 ∼ binomial(100,𝑝), with 𝑝 ≠ 0.25
𝐴
Values of 𝑝 < 0.25 represent hypotheses that the subject has a kind of anti-esp.
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 5
4.2 Types of error
There are two types of errors we can make. We can incorrectly reject the null hypothesis
when it is true or we can incorrectly fail to reject it when it is false. These are unimagina-
tively labeled type I and type II errors. We summarize this in the following table.
True state of nature
𝐻 𝐻
0 𝐴
Our Reject 𝐻 Type I error correct decision
0
decision ‘Don’t reject’ 𝐻 correct decision Type II error
0
Type I: false rejection of 𝐻
0
Type II: false non-rejection (‘acceptance’) of 𝐻
0
4.3 Significance level and power
Significance level and power are used to quantify the quality of the significance test. Ideally
a significance test would not make errors. That is, it would not reject 𝐻 when 𝐻 was true
0 0
and would reject 𝐻 in favor of 𝐻 when 𝐻 was true. Altogether there are 4 important
0 𝐴 𝐴
probabilities corresponding to the 2×2 table just above.
𝑃(reject 𝐻 |𝐻 ) 𝑃(reject 𝐻 |𝐻 )
0 0 0 𝐴
𝑃(do not reject 𝐻 |𝐻 ) 𝑃(do not reject 𝐻 |𝐻 )
0 0 0 𝐴
The two probabilities we focus on are:
Significance level = 𝑃(reject 𝐻 |𝐻 )
0 0
= probability we incorrectly reject 𝐻
0
= 𝑃(type I error).
Power = probability we correctly reject 𝐻
0
= 𝑃(reject 𝐻 |𝐻 )
0 𝐴
= 1−𝑃(type II error).
Ideally, a hypothesis test should have a small significance level (near 0) and a large power
(near 1). Here are two analogies to help you remember the meanings of significance and
power.
Some analogies
1. Think of 𝐻 as the hypothesis ‘nothing noteworthy is going on’, i.e. ‘the coin is fair’,
0
‘the treatment is no better than placebo’ etc. And think of 𝐻 as the opposite: ‘something
𝐴
interesting is happening’. Then power is the probability of detecting something interesting
when it’s present and significance level is the probability of mistakenly claiming something
interesting has occured.
2. In the U.S. criminal defendents are presumed innocent until proven guilty beyond a
reasonable doubt. We can phrase this in NHST terms as
𝐻 : the defendent is innocent (the default)
0
𝐻 : the defendent is guilty.
𝐴
Significance level is the probability of finding an innocent person guilty. Power is the
probability of correctly finding a guilty party guilty. ‘Beyond a reasonable doubt’ means
we should demand the significance level be very small.
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 6
Composite hypotheses
𝐻 is composite in Example 3, so the power is different for different values of 𝜃. We expand
𝐴
the previous probability table to include some alternate values of 𝜃. We do the same with
the stem plots. As always in the NHST game, we look at likelihoods: the probability of the
data given a hypothesis.
The rejection range consists of the extreme values of 𝑥. The non-rejection range (3-7) is a
set of center values of 𝑥.
𝑥 0 1 2 3 4 5 6 7 8 9 10
𝐻 ∶ 𝑝(𝑥|𝜃=0.5) 0.001 0.010 0.044 0.117 0.205 0.246 0.205 0.117 0.044 0.010 .001
0
𝐻 ∶ 𝑝(𝑥|𝜃=0.6) 0.000 0.002 0.011 0.042 0.111 0.201 0.251 0.215 0.121 0.040 0.006
𝐴
𝐻 ∶ 𝑝(𝑥|𝜃=0.7) 0.000 0.000 0.001 0.009 0.037 0.103 0.200 0.267 0.233 0.121 0.028
𝐴
𝑝(𝑥|𝐻 ) 𝑝(𝑥|𝜃=.6) 𝑝(𝑥|𝜃=.7)
0
.25 .25 .25
.15 .15 .15
.05 .05 .05
𝑥
0 1 2 3 4 5 6 7 8 9 10 0 1 2 3 4 5 6 7 8 9 10 0 1 2 3 4 5 6 7 8 9 10
Rejection region and null and alternative probabilities for example 3
We use the probability table to compute the significance level and power of this test.
Significance level = probability we reject 𝐻 when it is true
0
= probability the test statistic is in the rejection region when 𝐻 is true
0
= probability the test stat. is in the rejection region of the 𝐻 row of the table
0
= sum of shaded orange boxes in the 𝜃 = 0.5 row
= 0.11
Power when 𝜃 = 0.6 = probability we reject 𝐻 when 𝜃 = 0.6
0
= probability the test statistic is in the rejection region when 𝜃 = 0.6
= probability the test stat. is in the rejection region of the 𝜃 = 0.6 row of the table
= sum of blue boxes in the 𝜃 = 0.6 row
= 0.180
Power when 𝜃 = 0.7 = probability we reject 𝐻 when 𝜃 = 0.7
0
= probability the test statistic is in the rejection region when 𝜃 = 0.7
= probability the test stat. is in the rejection region of the 𝜃 = 0.7 row of the table
= sum of blue boxes in the 𝜃 = 0.7 row
= 0.384
We see that the power is greater for 𝜃 = 0.7 than for 𝜃 = 0.6. This isn’t surprising since we
expect it to be easier to recognize that a 0.7 coin is unfair than is is to recognize 0.6 coin
is unfair. Typically, we get higher power when the alternate hypothesis is farther from the
null hypothesis. In Example 3, it would be quite hard to distinguish a fair coin from one
with 𝜃 = 0.51.
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 7
4.4 Conceptual sketches
We illustrate the notions of null hypothesis, rejection region and power with some sketches
of the pdfs for the null and alternative hypotheses.
4.4.1 Null distribution: rejection and non-rejection regions
The first diagram below illustrates a null distribution with rejection and non-rejection re-
gions. Also shown are two possible test statistics: 𝑥 and 𝑥 .
1 2
𝜙(𝑥|𝐻 )
0
𝑥
𝑥 2 -3 0 𝑥 1 3
reject 𝐻 don’t reject 𝐻 reject 𝐻
0 0 0
Theteststatistic𝑥 isinthenon-rejectionregion. So, ifourdataproducedtheteststatistic
1
𝑥 then we would not reject the null hypothesis 𝐻 . On the other hand the test statistic 𝑥
1 0 2
isintherejectionregion,soifourdataproduced𝑥 thenwewouldrejectthenullhypothesis
2
in favor of the alternative hypothesis.
There are several things to note in this picture.
1. The rejection region consists of values far from the center of the null distribution.
2. Therejectionregionistwo-sided. Wewillalsoseeexamplesofone-sidedrejectionregions
as well.
3. The probability of rejection (significance) is the shaded area under the curve, i.e. the
probability of data being in the rejection region assuming 𝐻 is true.
0
4. The alternative hypothesis is not mentioned. We reject or don’t reject 𝐻 based only
0
on the likelihood 𝜙(𝑥|𝐻 ), i.e. the probability of the test statistic conditioned on 𝐻 . As
0 0
we will see, the alternative hypothesis 𝐻 should be considered when choosing a rejection
𝐴
region, but formally it does not play a role in rejecting or not rejecting 𝐻 .
0
5. Sometimes we rather lazily call the non-rejection region the acceptance region. This is
technically incorrect because we never truly accept the null hypothesis. We either reject or
say the data does not support rejecting 𝐻 . This is often summarized by the statement:
0
you can never prove the null hypothesis.
4.4.2 High and low power tests
The next two figures show high and low power tests. In both tests the null distributions
are standard normal. Likewise, the alternative distributions are both normal with variance
1, but different means: -4.0 in the top figure and -0.4 in the bottom one.
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 8
Since the alternative distribution is to the left of the null distribution we use a one-sided
rejection region. It is the same for both tests. The shaded area under 𝜙(𝑥|𝐻 ) represents
0
the significance level – it is the same for both tests. Remember the significance level can be
described two ways:
• The probability of falsely rejecting the null hypothesis when it is true.
• The probabilitiy the test statistic falls in the rejection region even though 𝐻 is true.
0
Likewise, the shaded area under 𝜙(𝑥|𝐻 ) represents the power, i.e. the probability that
𝐴
the test statistic is in the rejection (of 𝐻 ) region when 𝐻 is true. Both tests have the
0 𝐴
same significance level, but different powers. When 𝜙(𝑥|𝐻 ) has considerable overlap with
𝐴
𝜙(𝑥|𝐻 ) the power will tend to be low (bottom figure) and when they are well separated it
0
tends to be high (top figure). It is well worth your while to thoroughly understand these
graphical representations of significance testing.
𝜙(𝑥|𝐻 ) 𝜙(𝑥|𝐻 )
𝐴 0
𝑥
𝑥 1 -4 𝑥 2 0 𝑥 3
reject𝐻 region . non-reject𝐻 region
0 0
Highpowertest
𝜙(𝑥|𝐻 ) 𝜙(𝑥|𝐻 )
𝐴 0
𝑥
𝑥 1 𝑥 2 -0.4 0 𝑥 3
reject𝐻 region . non-reject𝐻 region
0 0
Lowpowertest
In the top figure we see that the means of the null and alternative distributions are 4
standard deviations apart. Since the areas under the densities have very little overlap the
test has high power. That is, if 𝐻 was true, then seeing the data 𝑥 would be rare and
𝐴 3
surprising and similarly for any point in the non-rejection region. That is, if 𝐻 is the
𝐴
true distribution we are extremely likely to correctly reject the null hypothesis, i.e. we are
unlikely to make a type II error.
In the bottom figure we see that the means of the null and alternative distributions are just
0.4 standard deviations apart. Since the areas under the densities have a lot of overlap the
test has low power. That is, if the data 𝑥 is drawn from 𝐻 it is highly likely to be in the
𝐴
non-rejection region. For example 𝑥 would be not be a very surprising outcome for the 𝐻
3 𝐴
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 9
distribution. That is, if 𝐻 is the true distribution, we are highly likely to make a type II
𝐴
error.
Typically we can increase the power of a test by increasing the amount of data and thereby
decreasing the variance of the null and alternative distributions. In experimental design it
is important to determine ahead of time the number of trials or subjects needed to achieve
a desired power.
Example 7. Suppose a drug for a disease is being compared to a placebo. We choose our
null and alternative hypotheses as
𝐻 = the drug does not work better than the placebo
0
𝐻 = the drug works better than the placebo
𝐴
The power of the hypothesis test is the probability that the test will conclude that the drug
is better, if it is indeed truly better. The significance level is the probability that the test
will conclude that the drug works better, when in fact it does not. We will look at this in
more detail below.
5 Designing a hypothesis test
Formally all a hypothesis test requires is 𝐻 , 𝐻 , a test statistic and a rejection region. In
0 𝐴
practice the design is often done using the following steps.
1. Pick the null hypothesis 𝐻 .
0
The choice of 𝐻 and 𝐻 is not mathematics. It’s art and custom. We often choose 𝐻 to
0 𝐴 0
be simple. Or we often choose 𝐻 to be the simplest or most cautious explanation, i.e. no
0
effect of drug, no ESP, no bias in the coin.
2. Decide if 𝐻 is one-sided or two-sided.
𝐴
In Example 3 we wanted to know if the coin was unfair. An unfair coin could be biased for
or against heads, so 𝐻 ∶ 𝜃 ≠ 0.5 is a two-sided hypothesis. If we only care whether or not
𝐴
the coin is biased for heads we could use the one-sided hypothesis 𝐻 ∶ 𝜃 > 0.5.
𝐴
3. Pick a test statistic.
Forexample,thesamplemean,sampletotal,orsamplevariance. Oftenthechoiceisobvious.
Some standard statistics that we will encounter are 𝑧, 𝑡, and 𝜒2. We will learn to use these
statistics as we work examples over the next few classes. One thing we will say repeatedly
is that the distributions that go with these statistics are always conditioned on the null
hypothesis. That is, we will compute likelihoods such as 𝜙(𝑧|𝐻 ).
0
4. Pick a significance level and determine the rejection region.
We will usually use 𝛼 to denote the significance level. The Neyman-Pearson paradigm is to
pick 𝛼 in advance. Typical values are 0.1, 0.05, 0.01. Recall that the significance level is
the probability of a type I error, i.e. of incorrectly rejecting the null hypothesis when it is
true. The value we choose will depend on the consequences of a type I error.
Once the significance level is chosen we can determine the rejection region in the tail(s) of
the null distribution. In Example 3, 𝐻 is two sided so the rejection region is split between
𝐴
the two tails of the null distribution. This distribution is given in the following table:
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 10
𝑥 0 1 2 3 4 5 6 7 8 9 10
𝑝(𝑥|𝐻 ) 0.001 0.010 0.044 0.117 0.205 0.246 0.205 0.117 0.044 0.010 0.001
0
If we set 𝛼 = 0.05 then the rejection region must contain at most 0.05 probability. For a
two-sided rejection region this is split between the two tails, so we get
{0, 1, 9, 10}.
If we set 𝛼 = 0.01 the rejection region is
{0, 10}.
We show these in tables with the rejection region (values of 𝑥) inside the orange rectangle
and the corresponding null likelihoods in the shaded orange boxes.
𝑥 0 1 2 3 4 5 6 7 8 9 10
𝑝(𝑥|𝐻 ) 0.001 0.010 0.044 0.117 0.205 0.246 0.205 0.117 0.044 0.010 0.001
0
𝑥 0 1 2 3 4 5 6 7 8 9 10
𝑝(𝑥|𝐻 ) 0.001 0.010 0.044 0.117 0.205 0.246 0.205 0.117 0.044 0.010 0.001
0
Tables with shaded rejection regions for 𝛼 = 0.05 (top) and 𝛼 = 0.01 (bottom)
Suppose we change 𝐻 to ‘the coin is biased in favor of heads’. We now have a one-sided
𝐴
hypothesis 𝜃 > 0.5. Our rejection region will now be in the right-hand tail since we don’t
want to reject 𝐻 in favor of 𝐻 if we get a small number of heads. Now if 𝛼 = 0.05 the
0 𝐴
rejection region is the one-sided range
{9, 10}.
If we set 𝛼 = 0.01 then the rejection region is
{10}.
As above we show the one sided rejection regions in tables.
𝑥 0 1 2 3 4 5 6 7 8 9 10
𝑝(𝑥|𝐻 ) 0.001 0.010 0.044 0.117 0.205 0.246 0.205 0.117 0.044 0.010 0.001
0
𝑥 0 1 2 3 4 5 6 7 8 9 10
𝑝(𝑥|𝐻 ) 0.001 0.010 0.044 0.117 0.205 0.246 0.205 0.117 0.044 0.010 0.001
0
Tables with shaded one-sided rejection regions for 𝛼 = 0.05 (top) and 𝛼 = 0.01 (bottom)
5. Determine the power(s).
As we saw in Example 3, once the rejection region is set we can determine the power of the
test at various values of the alternate hypothesis.
Example 8. (Consequences of significance) If 𝛼 = 0.1 then we’d expect a 10% type
I error rate. That is, we expect to reject the null hypothesis in 10% of those experiments
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 11
where the null hypothesis is true. Whether 0.1 is a reasonable signficance level depends on
the decisions that will be made using it.
For example, if you were running an experiment to determine if your chocolate is more than
72% cocoa then a 10% error type I error rate is probably okay. That is, falsely believing
some 72% chocalate is greater that 72%, is probably acceptable. On the other hand, if your
forensic lab is identifying fingerprints for a murder trial then a 10% type I error rate, i.e.
mistakenly claiming that fingerprints found at the crime scene belonged to someone who
was truly innocent, is definitely not acceptable.
Significanceforacompositenullhypothesis. If𝐻 iscompositethenP(typeIerror)depends
0
onwhichmemberof𝐻 istrue. Inthiscasethesignificancelevelisdefinedasthemaximum
0
of these probabilities.
6 Critical values
Criticalvaluesarelikequantilesexcepttheyrefertotheprobabilitytotherightofthevalue
instead of the left.
Example 9. Use R to find the 0.05 critical value for the standard normal distribution.
Solution: Welabelthiscriticalvalue𝑧 . Thecriticalvalue𝑧 isjustthe0.95quantile,
0.05 0.05
i.e. ithas5%probabilitytoitsrightandtherefore95%probabilitytoitsleft. Wecomputed
it with the R function qnorm: qnorm(0.95, 0, 1), which returns 1.64.
In a typical significance test the rejection region consists of one or both tails of the null
distribution. The value of the test statistic that marks the start of the rejection region is a
critical value. We show this and the notation used in some examples.
Example 10. Critical values and rejection regions. Suppose our test statistic 𝑥 has null
distribution N(100,152), i.e. 𝜙(𝑥|𝐻 ) ∼ N(100,152). Suppose also that our rejection region
0
is right-sided and we have a significance level of 0.05. Find the critical value and sketch the
null distribution and rejection region.
Solution: The notation used for the critical value with right tail containing probability
0.05 is 𝑥 . The critical value 𝑥 is just the 0.95 quantile, i.e. it has 5% probability
0.05 0.05
to its right and therefore 95% probability to its left. We computed it with the R function
qnorm: qnorm(0.95, 100, 15), which returned 124.7. This is shown in the figure below.
𝜙(𝑥|𝐻 )∼N(100,152)
0
𝑥 =124.7
0.05
𝛼 = shaded area
= 0.05
𝑥
𝑥
100 0.05
non-reject 𝐻 reject 𝐻
0 0
Example 11. Critical values and rejection regions. Repeat the previous example for a
left-sided rejection region with significance level 0.05.
Solution: In this case the critical value has 0.05 probability to its left and therefore 0.95
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 12
probability to its right. So we label it 𝑥 . Since it is the 0.05 quantile compute it with
0.95
the R function: qnorm(0.05, 100, 15), which returned 75.3.
𝜙(𝑥|𝐻 )∼N(100,152)
0
𝑥 =75.3
0.95
𝛼 = shaded area
= 0.05
𝑥
𝑥
0.95 100
reject 𝐻 non-reject 𝐻
0 0
Example 12. Criticalvalues. Repeatthepreviousexampleforatwo-sidedrejectionregion.
Put half the significance in each tail.
Solution: To have a total significance of 0.05 we put 0.025 in each tail. That is, the left
tail starts at 𝑥 = 𝑞 and the right tail starts at 𝑥 = 𝑞 . We compute these
0.975 0.025 0.025 0.975
values with qnorm(0.025, 100, 15) and qnorm(0.975, 100, 15). The values are shown
in the figure below.
𝑥 =129.4 𝜙(𝑥|𝐻 )∼N(100,152)
0.025 0
𝑥 =70.6
0.975
𝛼 = shaded area
= 0.05
𝑥
𝑥 𝑥
0.975 100 0.025
reject 𝐻 non-reject 𝐻 reject 𝐻
0 0 0
7 𝑝-values
In practice people often specify the significance level and do the significance test using what
are called 𝑝-values. We will first define 𝑝-value and then state the 𝑝-test. After that, we
will illustrate it with figures and examples.
Definition. The 𝑝-value is the probability, assuming the null hypothesis, of seeing data at
least as extreme as the experimental data. What ‘at least as extreme’ means depends on
the experimental design.
P-test. If the 𝑝-value is less than the significance level 𝛼 then we reject 𝐻 . Otherwise we
0
do not reject 𝐻 .
0
We first illustrate 𝑝-values graphically and then we will work a simple one-sided example.
We will look at two-sided examples in later classes.
Suppose we have a right-sided alternate hypothesis, so our rejection region is in the right
tail of the range of possible outcomes. This is illustrated in the following figure.
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 13
𝜙(𝑥|𝐻 ) = null pdf
0
𝑥 = critical point
𝑞
𝛼 = shaded area
𝑥
𝑥
𝑞
non-reject 𝐻 reject 𝐻
0 0
Right-sided rejection region
Suppose we get data 𝑥 which is in the rejection region. This is shown in the figure below.
1
𝜙(𝑥|𝐻 ) = null pdf
0
𝑥 = critical point
𝑞
𝛼 = shaded area
𝑝 = striped area
𝑥
𝑥 𝑥
𝑞 1
non-reject 𝐻 reject 𝐻
0 0
𝑝-value = probability of data ‘more extreme’ than 𝑥 : 𝑝 < 𝛼
1
Since the rejection region is right-sided, the phrase ‘at least as extreme’ means all values to
the right of 𝑥 . So, the 𝑝-value is the area of the striped region.
1
Here is the key to connecting the 𝑝-test, rejection and signifcance:
Since 𝑥 is in the rejection region, the striped area 𝑝 is less than the shaded area 𝛼. That
1
is, 𝑝 < 𝛼. In other words, we reject the null hypothesis when 𝑝 < 𝛼.
For completeness we show a figure where 𝑥 is not in the rejection region, so 𝑝 > 𝛼. That
1
is, we do not reject 𝐻 when 𝑝 > 𝛼.
0
𝜙(𝑥|𝐻 ) = null pdf
0
𝑥 = critical point
𝑞
𝛼 = shaded area
𝑝 = striped area
𝑥
𝑥 𝑥
1 𝑞
non-reject 𝐻 reject 𝐻
0 0
𝑝-value = probability of data ‘more extreme’ than 𝑥 : 𝑝 > 𝛼
1
7.1 Example: 𝑧-tests
When our test statistic is standard normal we will call it 𝑧, and the corresponding test for
significance will be called a 𝑧-test.
Example 13. The 𝑧-test for normal hypotheses
IQ is normally distributed in the population according to a N(100,152) distribution. We
suspect that most MIT students have above average IQ so we frame the following hypothe-
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 14
ses.
𝐻 = MIT student IQs are distributed identically to the general population
0
= MIT IQ’s follow a N(100,152) distribution.
𝐻 = MIT student IQs tend to be higher than those of the general population
𝐴
= the average MIT student IQ is greater than 100.
Notice that 𝐻 is one-sided.
𝐴
Suppose we test 9 students and find they have an average IQ of 𝑥 = 112. Can we reject 𝐻
0
at a significance level 𝛼 = 0.05?
Solution: To compute 𝑝 we first standardize the data: Under the null hypothesis 𝑥̄ ∼
N(100,152/9) and therefore
𝑥̄−100 36
𝑧 = √ = = 2.4 ∼ N(0,1).
15/ 9 15
That is, the null distribution for 𝑧 is standard normal. We call 𝑧 a 𝑧-statistic, we will use
it as our test statistic.
For a right-sided alternative hypothesis the phrase ‘data at least as extreme’ is a one-sided
tail to the right of 𝑧. The 𝑝-value is then
𝑝 = 𝑃(𝑍 ≥ 2.4) = 1- pnorm(2.4,0,1) = 0.0081975.
Since 𝑝 ≤ 𝛼 we reject the null hypothesis. The reason this works is explained below. We
phrase our conclusion as
WerejectthenullhypothesisinfavorofthealternativehypothesisthatMIT
students have higher IQs on average. We have done this at significance level
0.05 with a 𝑝-value of 0.008.
Notes: 1. The average 𝑥 = 112 is random: if we ran the experiment again we could get a
different value for 𝑥.
2. We could use the statistic 𝑥 directly. Standardizing is fairly standard because, with
practice, we will have a good feel for the meaning of different 𝑧-values.
The justification for rejecting 𝐻 when 𝑝 ≤ 𝛼 is given in the following figure.
0
𝜙(𝑧|𝐻 )∼N(0,1)
0
𝑧 =1.645
0.05
𝛼 = shaded area = 0.05
𝑝 = striped area = 0.008
𝑥
-1 0 1 𝑧 0.05 2.4
non-reject 𝐻 reject 𝐻
0 0
In this example 𝛼 = 0.05, 𝑧 = 1.64 and the rejection region is the range to the right
0.05
of 𝑧 . Also, 𝑧 = 2.4 and the 𝑝-value is the probability to the right of 𝑧. The picture
0.05
illustrates that
• 𝑧 = 2.64 is in the rejection region
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 15
• is the same as 𝑧 is to the right of 𝑧
0.05
• is the same as the probability to the right of 𝑧 is less than 0.05
• which means 𝑝 < 0.05.
8 More examples
Hypothesistestingiswidelyusedininferentialstatistics. Wedon’texpectthatthefollowing
examples will make perfect sense at this time. Read them quickly just to get a sense of how
hypothesis testing is used. We will explore the details of these examples in class.
Example 14. The chi-square statistic and goodness of fit. (Rice, example B, p.313)
To test the level of bacterial contamination, milk was spread over a grid with 400 squares.
The amount of bacteria in each square was measured. We summarize in the table below.
The bottom row of the table is the number of different squares that had a given amount of
bacteria.
Amount of bacteria 0 1 2 3 4 5 6 7 8 9 10 19
Number of squares 56 104 80 62 42 27 9 9 5 3 2 1
We compute that the average amount of bacteria per square is 2.44. Since the Poisson(𝜆)
distribution is used to model counts of relatively rare events and the parameter 𝜆 is the
expected value of the distribution. we decide to see if these counts could come from a
Poisson distribution. To do this we first graphically compare the observed frequencies with
those expected from Poisson(2.44).
l
l l
l
l
l
l l l l l l l l l l l l l
5 10 15
08
06
04
02
0
Number of bacteria in square
serauqs
fo
rebmuN
l
l Poisson(2.44)
l
l Observed
l
l
l
l
l l
l l l l
The picture is suggestive, so we do a hypothesis test with
𝐻 ∶ the samples come from a Poisson(2.44) distribution.
0
𝐻 ∶ the samples come from a different distribution.
𝐴
18.05 Class 17, Null Hypothesis Significance Testing I, Spring 2022 16
We use a chi-square statistic, so called because it (approximately) follows a chi-square
distribution. To compute 𝑋2 we first combine the last few cells in the table so that the
minimum expected count is around 5 (a general rule-of-thumb in this game.)
The expected number of squares with a certain amount of bacteria comes from considering
400 trials from a Poisson(2.44) distribution, e.g., with = 2.44 the expected number of
3
squares with 3 bacteria is 400×e− = 84.4.
3!
(𝑂 −𝐸 )2
The chi-square statistic is ∑ 𝑖 𝑖 , where 𝑂 is the observed number and 𝐸 is the
𝐸 𝑖 𝑖
𝑖
expected number.
Number per square 0 1 2 3 4 5 6 > 6
Observed 56 104 80 62 42 27 9 20
Expected 34.9 85.1 103.8 84.4 51.5 25.1 10.2 5.0
Component of 𝑋2 12.8 4.2 5.5 6.0 1.7 0.14 0.15 44.5
Summing up we get 𝑋2 = 74.9.
Since the mean (2.44) and the total number of trials (400) are fixed, the 8 cells only have
6 degrees of freedom. So, assuming 𝐻 , our chi-square statistic follows (approximately) a
0
𝜒2 distribution. Using this distribution, 𝑃(𝑋2 > 74.59) = 0 (to at least 6 decimal places).
6
Thus we decisively reject the null hpothesis in favor of the alternate hypothesis that the
distribution is not Poisson(2.44).
To analyze further, look at the individual components of 𝑋2. There are large contributions
in the tail of the distribution, so that is where the fit goes awry.
Example 15. Student’s 𝑡 test.
Suppose we want to compare a medical treatment for increasing life expectancy with a
placebo. We give 𝑛 people the treatment and 𝑚 people the placebo. Let 𝑋 ,…,𝑋 be the
1 𝑛
number of years people live after receiving the treatment. Likewise, let 𝑌 ,…,𝑌 be the
1 𝑚
number of years people live after receiving the placebo. Let 𝑋̄ and 𝑌̄ be the sample means.
We want to know if the difference between 𝑋̄ and 𝑌̄ is statistically significant. We frame
this as a hypothesis test. Let 𝜇 and 𝜇 be the (unknown) means.
𝑋 𝑌
𝐻 ∶ 𝜇 = 𝜇 , 𝐻 ∶ 𝜇 ≠ 𝜇 .
0 𝑋 𝑌 𝐴 𝑋 𝑌
With certain assumptions and a proper formula for the pooled standard error 𝑠 the test
𝑝
𝑋̄ −𝑌̄
statistic 𝑡 = follow a 𝑡 distribution with 𝑛 + 𝑚 − 2 degrees of freedom. So our
𝑠
𝑝
rejection region is determined by a threshold 𝑡 with 𝑃(𝑡 > 𝑡 ) = 𝛼.
0 0
Null Hypothesis Significance Testing II
Class 18, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to list the steps common to all null hypothesis significance tests.
2. Be able to define and compute the probability of Type I and Type II errors.
3. Be able to look up and apply one- and two-sample 𝑡-tests.
2 Introduction
We continue our study of significance tests. In these notes we will introduce two new tests:
one-sample 𝑡-tests and two-sample 𝑡-tests. You should pay careful attention to the fact that
every test makes some assumptions about the data – often that is drawn from a normal
distribution. You should also notice that all the tests follow the same pattern. It is just the
computation of the test statistic and the type of the null distribution that changes.
3 Review
3.1 Setting up and running a significance test
There is a fairly standard set of steps one takes to set up and run a null hypothesis signifi-
cance test.
1. Design an experiment to collect data and choose a test statistic 𝑥 to be computed
from the data. The key requirement here is to know the null distribution 𝜙(𝑥|𝐻 ).
0
To compute power, one must also know the alternative distribution 𝜙(𝑥|𝐻 ).
𝐴
2. Decideifthetestisoneortwo-sidedbasedon𝐻 andtheformofthenulldistribution.
𝐴
3. Choose a significance level 𝛼 for rejecting the null hypothesis.
4. Decide how much data you need to collect to achieve the desired power for the test.
5. Run the experiment to collect data 𝑥 ,𝑥 ,…,𝑥 .
1 2 𝑛
6. Compute the test statistic 𝑥.
7. Compute the 𝑝-value corresponding to 𝑥 using the null distribution.
8. If 𝑝 < 𝛼, reject the null hypothesis in favor of the alternative hypothesis.
1
18.05 Class 18, Null Hypothesis Significance Testing II, Spring 2022 2
Notes.
1. Rather than choosing a significance level, you could instead choose a rejection region
and reject 𝐻 if 𝑥 falls in this region. The corresponding significance level is then the
0
probability, assuming 𝐻 , that 𝑥 falls in the rejection region.
0
2. The null hypothesis is often the ‘cautious hypothesis’. The lower we set the significance
level, the more “evidence” we will require before rejecting our cautious hypothesis in favor
of a more sensational alternative. It is standard practice to publish the 𝑝 value itself so that
others may draw their own conclusions.
3. A key point of confusion: A significance level of 0.05 does not mean the test only
makes mistakes 5% of the time. It means that if the null hypothesis is true, then the
probability the test will mistakenly reject it is 5%. The power of the test measures the
accuracy of the test when the alternative hypothesis is true. Namely, the power of the
test is the probability of rejecting the null hypothesis if the alternative hypothesis is true.
Thereforetheprobabilityoffalselyfailingtorejectthenullhypothesisis1minusthepower.
4. Another key point of confusion: We use 𝑝-values, but conceptually the 𝑝-value is
just a computational trick. After choosing a test statistic, the conceptual order is: first
pick a significance level, then use this to define the rejection region. We reject the null
hypothesis if the test statistic is in the rejection region. All the 𝑝-value does is tell us in
one computation whether or not the test stastic is in the rejection region.
Errors. We can summarize these two types of errors and their probabilities as follows:
Type I error = rejecting 𝐻 when 𝐻 is true.
0 0
Type II error = failing to reject 𝐻 when 𝐻 is true.
0 𝐴
P(type I error) = probability of falsely rejecting 𝐻
0
= P(test statistic is in the rejection region |𝐻 )
0
= significance level of the test
P(type II error) = probability of falsely not rejecting 𝐻
0
= P(test statistic is in the acceptance region |𝐻 )
𝐴
= 1 - power.
Helpful analogies.
In terms of medical testing for a disease: a Type I error is a false positive and a Type II
error is a false negative.
In a jury trial, a Type I error is convicting an innocent defendant and a Type II error is
acquitting a guilty defendant.
3.2 Power
We discussed power in the Class 17 notes. Power is the probabilitiy of correctly rejecting
the null hypothesis. It depends on the alternative hypothesis 𝐻 being considered.
𝐴
Theidealtesthaspowerequalto1.0andsignificanceequalto0.0. Ofcourse,ingeneral,this
is impossible. And we want to find some compromise where power is high and signficance
is low.
In symbols: power = 𝑃(data is in the rejection region |𝐻 ).
𝐴
18.05 Class 18, Null Hypothesis Significance Testing II, Spring 2022 3
Compare this with: signficance = 𝑃(data is in the rejection region |𝐻 ).
0
4 Understanding a significance test
Questions to ask:
1. How did they collect data? What is the experimental setup?
2. What are the null and alternative hypotheses?
3. What type of significance test was used?
Does the data match the criteria needed to use this type of test?
How robust is the test to deviations from these criteria?
4. For example, some tests comparing two groups of data assume that the groups are
drawnfromdistributionsthathavethesamevariance. Thisneedstobeverifiedbefore
applying the test. Often the check is done using another significance test designed to
compare the variances of two groups of data.
5. How is the 𝑝-value computed?
A significance test comes with a test statistic and a null distribution. In most tests
the 𝑝-value is
𝑝 = 𝑃(data at least as extreme as what we got|𝐻 )
0
What does ‘data at least as extreme as the data we saw’ mean? For example, is the
test one or two-sided?
6. What is the significance level 𝛼 for this test? If 𝑝 < 𝛼 then the experimenter will
reject 𝐻 in favor of 𝐻 .
0 𝐴
7. What is the power of the test?
5 𝑡 tests
Many significance tests assume that the data are drawn from a normal distribution, so
before using such a test you should examine the data to see if the normality assumption is
reasonable. We will describe how to do this in more detail later, but plotting a histogram
is a good start. Like the 𝑧-test, the one-sample and two-sample 𝑡-tests that we consider
below start from this normality assumption.
We don’t expect you to memorize all the computational details of these tests and those to
follow. In real life, you have access to textbooks, google, and wikipedia; on the exam, you’ll
have your notecard. Instead, you should be able to identify when a 𝑡-test is appropriate
and apply this test after looking up the details and using a table or software like R.
18.05 Class 18, Null Hypothesis Significance Testing II, Spring 2022 4
5.1 𝑧-test
Let’s first review the 𝑧-test.
• Data: we assume 𝑥 ,𝑥 ,…,𝑥 ∼ 𝑁(𝜇,𝜎2), where 𝜇 is unknown and 𝜎 is known.
1 2 𝑛
• Null hypothesis: 𝜇 = 𝜇 for some specific value 𝜇
0 0
𝑥−𝜇
• Test statistic: 𝑧 = √ 0 = standardized mean
𝜎/ 𝑛
• Null distribution: 𝜙(𝑧|𝐻 ) is the pdf of 𝑍 ∼ 𝑁(0,1)
0
• One-sided 𝑝-value (right side): 𝑝 = 𝑃(𝑍 ≥ 𝑧|𝐻 )
0
One-sided 𝑝-value (left side): 𝑝 = 𝑃(𝑍 ≤ 𝑧|𝐻 )
0
2𝑃(𝑍 ≥ 𝑧) if 𝑧 > 0
Two-sided 𝑝-value: 𝑝 = { .
2𝑃(𝑍 ≤ 𝑧) if 𝑧 < 0.
Because of the symmetry of the distribution around 0, we can also write this as
𝑝 = 𝑃(|𝑍| ≥ |𝑧|).
See Example 1b for the rationale for this.
Example 1. Suppose that we have data that follows a normal distribution of unknown
mean𝜇andknownvariance4. Letthenullhypothesis𝐻 bethat𝜇 = 2. Letthealternative
0
hypothesis 𝐻 be that 𝜇 > 2. Suppose we collect the following data:
𝐴
3, 2, 5, 7, 1
At a significance level of 𝛼 = 0.05, should we reject the null hypothesis?
Solution: There are 5 data points with average 𝑥 = 3.6. Because we have normal data
with a known variance we should use a 𝑧 test. Our 𝑧 statistic is
𝑥−𝜇 3.6−2
𝑧 = √ 0 = √ = 1.79
𝜎/ 𝑛 2/ 5
Our test is one-sided because the alternative hypothesis is one-sided. So (using R) our
𝑝-value is
𝑝 = 𝑃(𝑍 > 𝑧) = 𝑃(𝑍 > 1.79) = 0.037
Since 𝑝 < 𝛼 = 0.05, we reject the null hypothesis in favor of the alternative hypothesis that
𝜇 > 2.
We can visualize the test as follows:
18.05 Class 18, Null Hypothesis Significance Testing II, Spring 2022 5
Rejection region = shaded orange
𝜙(𝑧|𝐻 )∼N(0,1)
0 (starts at 𝑞 =𝑧 =1.64)
0.95 0.05
𝛼 = shaded orange area = 0.05
𝑧 = statistic = black dot = 1.79
𝑝 = blue stripe area = 0.037
𝑥
1.64 1.79
-1 0 1
non-reject 𝐻 reject 𝐻
0 0
Example 1b. Repeat Example 1 as a two-sided test, i.e. with 𝐻 being 𝜇 ≠ 2.
𝐴
Solution: Let’s do the test and then we’ll explain the rationale behind the computation of
the 𝑝-value.
Since 𝑧 > 0, 𝑝 = 2𝑃(𝑍 > 𝑧) = 0.074. Since, 𝑝 > 𝛼 = 0.05, the data does not support
rejecting the null hypothesis in favor of 𝐻 .
𝐴
Reason for the factor of 2 in the computation of 𝑝
The reason is essentially arithmetic. Remember, the purpose of the 𝑝-value is that 𝑝 ≤ 𝛼
indicates that the test statistic is in the rejection region.
The picture below illustrates the following. For a two-sided test, each side of the rejection
region has probability 𝛼/2. So, if the test statistic is on the right, then it is in the rejection
region if 𝑃(𝑍 > 𝑧) ≤ 𝛼/2, i.e. if 𝑝 = 2𝑃(𝑍 > 𝑧) ≤ 𝛼
Left rejection region = shaded orange Right rejection region = shaded orange
𝜙(𝑧|𝐻 )∼N(0,1)
(starts at 𝑞 =𝑧 =−1.96) 0 (starts at 𝑞 =𝑧 =1.96)
0.025 0.925 0.975 0.025
𝛼/2 = left shaded orange area = 0.025 𝛼/2 = right shaded orange area = 0.025
−𝑧 = black dot = 1.79 𝑧 = statistic = black dot = 1.79
𝑝/2 = left blue stripe area = 0.037 𝑝/2 = right blue stripe area = 0.037
𝑥
−1.79 1.79
−1.96 -1 0 1 1.96
reject 𝐻 non-reject 𝐻 reject 𝐻
0 0 0
5.2 The Student 𝑡 distribution
‘Student’ is the pseudonym used by the William Gosset who first described this test and
distribution. See https://en.wikipedia.org/wiki/Student's_t-test
The 𝑡-distribution is symmetric and bell-shaped like the normal distribution. It has a
parameter 𝑑𝑓 which stands for degrees of freedom. For 𝑑𝑓 small the 𝑡-distribution has
more probability in its tails than the standard normal distribution. As 𝑑𝑓 increases 𝑡(𝑑𝑓)
becomes more and more like the standard normal distribution.
18.05 Class 18, Null Hypothesis Significance Testing II, Spring 2022 6
Hereisasimpleappletthatshows𝑡(𝑑𝑓)andcomparesittothestandardnormaldistribution:
https://mathlets.org/mathlets/t-distribution/
−4 −2 0 2 4
4.0
2.0
0.0
N(0,1)
m=8
m=4
m=2
t densities for m degrees of freedom
As degrees of freedom increases the t-distribution becomes normal
5.3 R
AsusualinR,thefunctionspt, dt, qt, rtcorrespondtocdf, pdf, quantiles, andrandom
sampling for a 𝑡 distribution. Remember that you can type ?dt in RStudio to view the help
file specifying the parameters of dt. For example, pt(1.65,3) computes the probability
that 𝑥 is less than or equal 1.65 given that 𝑥 is sampled from the 𝑡 distribution with 3
degrees of freedom, i.e. 𝑃(𝑥 ≤ 1.65) given that 𝑥 ∼ 𝑡(3)).
5.4 One sample 𝑡-test
For the 𝑧-test, we assumed that the variance of the underlying distribution of the data was
known. However, it is often the case that we don’t know 𝜎 and therefore we must estimate
it from the data. In these cases, we use a one sample 𝑡-test instead of a 𝑧-test and the
studentized mean in place of the standardized mean
• Data: we assume 𝑥 ,𝑥 ,…,𝑥 ∼ 𝑁(𝜇,𝜎2), where both 𝜇 and 𝜎 are unknown.
1 2 𝑛
• Null hypothesis: 𝜇 = 𝜇 for some specific value 𝜇
0 0
• Test statistic:
𝑥−𝜇
𝑡 = √ 0
𝑠/ 𝑛
where
1 𝑛
𝑠2 = ∑(𝑥 −𝑥)2.
𝑛−1 𝑖
𝑖=1
Here 𝑡 is called the Studentized mean and 𝑠2 is called the sample variance. The latter
is an estimate of the true variance 𝜎2.
• Null distribution: 𝜙(𝑡|𝐻 ) is the pdf of 𝑇 ∼ 𝑡(𝑛−1), the 𝑡 distribution with 𝑛−1
0
degrees of freedom.*
18.05 Class 18, Null Hypothesis Significance Testing II, Spring 2022 7
• One-sided 𝑝-value (right side): 𝑝 = 𝑃(𝑇 ≥ 𝑡|𝐻 )
0
One-sided 𝑝-value (left side): 𝑝 = 𝑃(𝑇 ≤ 𝑡|𝐻 )
0
2𝑃(𝑇 ≥ 𝑡) if 𝑡 > 0
Two-sided 𝑝-value: 𝑝 = {
2𝑃(𝑇 ≤ 𝑡) if 𝑡 < 0.
Because of the symmetry of the distribution around 0, we can also write this as
𝑝 = 𝑃(|𝑇| ≥ |𝑡|).
*Important note. This is a good example of how we will work with significance tests.
Once we know the distribution of the test statistic, all the tests have the same basic form.
In this case, we make use of a theorem that says, for normal data the Studentized mean
follows a 𝑡-distribution. We will not prove this in 18.05, but you can look up the proof if
you want: https://en.wikipedia.org/wiki/Student's_t-distribution#Derivation
Example 2. Now suppose that in Example 1 the variance is unknown. That is, we have
data that follows a normal distribution of unknown mean 𝜇 and and unknown variance 𝜎.
Suppose we collect the same data as before:
1, 2, 3, 6, −1
As above, let the null hypothesis 𝐻 be that 𝜇 = 0 and the alternative hypothesis 𝐻 be
0 𝐴
that 𝜇 > 0. At a significance level of 𝛼 = 0.05, should we reject the null hypothesis?
Solution: There are 5 data points with average 𝑥 = 2.2. Because we have normal data
with unknown mean and unknown variance we should use a one-sample 𝑡 test. Computing
the sample variance we get
1
𝑠2 = ((1−2.2)2+(2−2.2)2+(3−2.2)2+(6−2.2)2+(−1−2.2)2) = 6.7
4
Our 𝑡-statistic is the Studentized mean:
𝑥−𝜇 2.2−0
𝑡 = √ 0 = √ √ = 1.901
𝑠/ 𝑛 6.7/ 5
Our test is one-sided because the alternative hypothesis is one-sided. So (using R) the
𝑝-value is
𝑝 = 𝑃(𝑇 > 𝑡) = 𝑃(𝑇 > 1.901) = 1-pt(1.901,4) = 0.065
Since 𝑝 > 0.05, we do not reject the null hypothesis.
We can visualize the test as follows:
𝜙(𝑦|𝐻 0 )∼𝑡(4) Rejectionregion=shadedorange
(startsat𝑞 =𝑡 =2.13)
0.95 0.05
𝛼=shadedorangearea=0.05
𝑡=statistic=blackdot=1.90
𝑝=bluestripearea=0.065
𝑥
1.9 2.13
-1 0 1
non-reject𝐻 reject𝐻
0 0
18.05 Class 18, Null Hypothesis Significance Testing II, Spring 2022 8
5.5 Two-sample 𝑡-test with equal variances
We next consider the case of comparing the means of two samples. For example, we might
be interested in comparing the mean eﬀicacies of two medical treatments.
• Data: We assume we have two sets of data drawn from normal distributions
𝑥 ,𝑥 ,…,𝑥 ∼ 𝑁(𝜇 ,𝜎2)
1 2 𝑛 1
𝑦 ,𝑦 ,…,𝑦 ∼ 𝑁(𝜇 ,𝜎2)
1 2 𝑚 2
where the means 𝜇 and 𝜇 and the variance 𝜎2 are all unknown. Notice the assump-
1 2
tion that the two distributions have the same variance. Also notice that there are 𝑛
samples in the first group and 𝑚 samples in the second.
• Null hypothesis: 𝜇 = 𝜇 (the values of 𝜇 and 𝜇 are not specified)
1 2 1 2
• Test statistic:
𝑥−𝑦
𝑡 = ,
𝑠
𝑝
where 𝑠2 is the pooled variance
𝑝
(𝑛−1)𝑠2 +(𝑚−1)𝑠2 1 1
𝑠2 = 𝑥 𝑦 ( + )
𝑝 𝑛+𝑚−2 𝑛 𝑚
Here 𝑠2 and 𝑠2 are the sample variances of the 𝑥 and 𝑦 respectively. The expression
𝑥 𝑦 𝑖 𝑗
for 𝑡 is somewhat complicated, but the basic idea remains the same and it still results
in a known null distribution.
• Null distribution: 𝜙(𝑡|𝐻 ) is the pdf of 𝑇 ∼ 𝑡(𝑛+𝑚−2).
0
• One-sided 𝑝-value (right side): 𝑝 = 𝑃(𝑇 > 𝑡|𝐻 )
0
One-sided 𝑝-value (left side): 𝑝 = 𝑃(𝑇 < 𝑡|𝐻 )
0
Two-sided 𝑝-value: 𝑝 = 𝑃(|𝑇| > |𝑡|).
Note 1: Some authors use a different notation. They define the pooled variance as
(𝑛−1)𝑠2 +(𝑚−1)𝑠2
𝑠2 = 𝑥 𝑦
𝑝-other-authors 𝑛+𝑚−2
and what we called the pooled variance they point out is the estimated variance of 𝑥−𝑦.
That is,
𝑠2 = 𝑠 ×(1/𝑛+1/𝑚) ≈ 𝑠2
𝑝 𝑝-other-authors 𝑥−𝑦̄
Note 2: There is a version of the two-sample 𝑡-test that allows the two groups to have
different variances. In this case the test statistic is a little more complicated but R will
handle it with equal ease.
Note 3: We reiterate our ‘important note’ from above: It can be proved that under the
assumptions on the data (independent samples, normal data, equal variances), the null
distribution is a 𝑡-distribution. We won’t prove this in 18.05. But knowing it, we can
18.05 Class 18, Null Hypothesis Significance Testing II, Spring 2022 9
work with and understand the gist of the two-sample 𝑡-test in exactly the same way we can
understand other significance tests.
Example 3. The following data comes from a real study in which 1408 women were
admittedtoamaternityhospitalfor(i)medicalreasonsorthrough(ii)unbookedemergency
admission. The duration of pregnancy is measured in complete weeks from the beginning
of the last menstrual period. We can summarize the data as follows:
Medical: 775 observations with 𝑥̄ = 39.08 and 𝑠2 = 7.77.
𝑀 𝑀
Emergency: 633 observations with 𝑥̄ = 39.60 and 𝑠2 = 4.95
𝐸 𝐸
Set up and run a two-sample 𝑡-test to investigate whether the mean duration differs for the
two groups.
What assumptions did you make?
Solution: The pooled variance for this data is
774(7.77)+632(4.95) 1 1
𝑠2 = ( + ) = 0.0187
𝑝 1406 775 633
The 𝑡 statistic for the null distribution is
𝑥 ̄ −𝑦 ̄
𝑀 𝐸 = −3.8064
𝑠
𝑝
We have 1406 degrees of freedom. Using R to compute the two-sided 𝑝-value we get
𝑝 = 𝑃(|𝑇| > |𝑡|) = 2*pt(-3.8064, 1406) = 0.00015
𝑝 is very small, much smaller than 𝛼 = 0.05 or 𝛼 = 0.01. Therefore we reject the null
hypothesis in favor of the alternative that there is a difference in the mean durations.
Rather than compute the two-sided 𝑝-value exactly using a 𝑡-distribution we could have
noted that with 1406 degrees of freedom the 𝑡 distribution is essentially standard normal
and 3.8064 is almost 4 standard deviations. So
𝑃(|𝑡| ≥ 3.8064) ≈ 𝑃(|𝑧| ≥ 3.8064) < 0.001
We assumed the data was normal and that the two groups had equal variances. Given the
large difference between the sample variances this assumption may not be warranted.
Infact, thereareothersignificanceteststhattestwhetherthedataisapproximatelynormal
and whether the two groups have the same variance. In practice one might apply these first
to determine whether a 𝑡 test is appropriate in the first place. We don’t have time to go
into normality tests here, but we will see the 𝐹 distribution used for equality of variances
next week.
https://en.wikipedia.org/wiki/Normality_test
https://en.wikipedia.org/wiki/F-test_of_equality_of_variances
Null Hypothesis Significance Testing III
Class 19, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Given hypotheses and data, be able to identify an appropriate significance test from
a list of common ones.
2. Givenhypotheses, data, andasuggestedsignificancetest, knowhowtolookupdetails
and apply the significance test.
2 Introduction
In these notes we will collect together some of the most common significance tests, though
by necessity we will leave out many other useful ones. Still, all significance tests follow the
same basic pattern in their design and implementation, so by learning the ones we include
you should be able to apply other ones as needed.
Designing a null hypothesis significance test (NHST):
• Specify null and alternative hypotheses.
• Choose a test statistic whose null distribution and alternative distribution(s) are
known.
• Specifyarejectionregion. Veryoftenthisisdoneimplicitlybyspecifyingasignificance
level𝛼andamethodforcomputing𝑝-valuesbasedonthetailsofthenulldistribution.
• Compute power using the alternative distribution(s).
Running a NHST:
• Collect data and compute the test statistic.
• Check if the test statistic is in the rejection region. Most often this is done implicitly
by checking if 𝑝 < 𝛼. If so, we ‘reject the null hypothesis in favor of the alternative
hypothesis’. Otherwise we conclude ‘the data does not support rejecting the null
hypothesis’.
Note the careful phrasing: when we fail to reject 𝐻 , we do not conclude that 𝐻 is true.
0 0
The failure to reject may have other causes. For example, we might not have enough data
to clearly distinguish 𝐻 and 𝐻 , whereas more data might indicate that we should reject
0 𝐴
𝐻 .
0
1
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 2
3 Population parameters and sample statistics
Example 1. If we randomly select 10 men from a population and measure their heights we
say that we have sampled the heights from the population. In this case the sample mean,
say 𝑥, is the mean of the sampled heights. It is a statistic and we know its value explicitly.
On the other hand, the true average height of the population, say 𝜇, is unknown and we
can only estimate its value. We call 𝜇 a population parameter.
Themainpurposeofsignificancetestingistousesamplestatisticstodrawconlusionsabout
population parameters. For example, we might test if the average height of men in a given
population is greater than 70 inches.
4 A gallery of common significance tests related to the nor-
mal distribution
We will show a number of tests that all assume normal data. For completeness we will
include the 𝑧 and 𝑡 tests we’ve already explored.
You shouldn’t try to memorize these tests. It is a hopeless task to memorize the tests given
here and even more hopeless to memorize all the tests we’ve left out. Rather, your goal
should be to be able to find the correct test when you need it. Pay attention to the types
of hypotheses the tests are designed to distinguish and the assumptions about the data
needed for the test to be valid. We will work through the details of these tests in class and
on homework.
The null distributions for all of these tests are all related to the normal distribution by
explicit formulas. We will not go into the details of these distributions or the arguments
showing how they arise as the null distributions in our significance tests. However, the
arguments are accessible to anyone who knows calculus and is interested in understanding
them. Given the name of any distribution, you can easily look up the details of its con-
struction and properties online. You can also use R to explore the distribution numerically
and graphically.
When analyzing data with any of these tests one thing of key importance is to verify that
the assumptions are true or at least approximately true. For example, you shouldn’t use a
test that assumes the data is normal unless you’ve checked that the data is approximately
normal.
The script class19.r contains examples of using R to run some of these tests. It is posted in
our usual place for R code.
4.1 𝑧-test
• Use: Test if the population mean equals a hypothesized mean.
• Data: 𝑥 ,𝑥 ,…,𝑥 .
1 2 𝑛
• Assumptions: The data are independent normal samples:
𝑥 ∼ 𝑁(𝜇,𝜎2) where 𝜇 is unknown, but 𝜎 is known.
𝑖
• 𝐻 : For a specified 𝜇 , 𝜇 = 𝜇 .
0 0 0
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 3
• 𝐻 :
𝐴
Two-sided: 𝜇 ≠ 𝜇
0
one-sided-greater: 𝜇 > 𝜇
0
one-sided-less: 𝜇 < 𝜇
0
𝑥−𝜇
• Test statistic: 𝑧 = √ 0
𝜎/ 𝑛
• Null distribution: 𝜙(𝑧|𝐻 ) is the pdf of 𝑍 ∼ 𝑁(0,1).
0
• 𝑝-value:
Two-sided: 𝑝 = 𝑃(|𝑍| > 𝑧) = 2*(1-pnorm(abs(z), 0, 1))
one-sided-greater: 𝑝 = 𝑃(𝑍 > 𝑧) = 1 - pnorm(z, 0, 1)
one-sided-less: 𝑝 = 𝑃(𝑍 < 𝑧) = pnorm(z, 0, 1)
• R code: There does not seem to be a single R function in the base R packages that
runs a 𝑧-test. There are other packages you can install that have a z.test function.
Of course, it is easy enough to get R to compute the 𝑧 score and 𝑝-value. There is an
example of this in class19.r.
Example 2. We quickly reprise our example from the class 17 notes.
IQ is normally distributed in the population according to a N(100,152) distribution. We
suspect that most MIT students have above average IQ so we frame the following hypothe-
ses.
𝐻 = MIT student IQs are distributed identically to the general population
0
= MIT IQ’s follow a N(100,152) distribution.
𝐻 = MIT student IQs tend to be higher than those of the general population
𝐴
= the average MIT student IQ is greater than 100.
Notice that 𝐻 is one-sided.
𝐴
Suppose we test 9 students and find they have an average IQ of 𝑥̄= 112. Can we reject 𝐻
0
at a significance level 𝛼 = 0.05?
Solution: Our test statistic is
𝑥̄−100 36
𝑧 = √ = = 2.4.
15/ 9 15
The right-sided 𝑝-value is therefore
𝑝 = 𝑃(𝑍 ≥ 2.4) = 1- pnorm(2.4,0,1) = 0.0081975.
Since 𝑝 ≤ 𝛼 we reject the null hypothesis in favor of the alternative hypothesis that MIT
students have higher IQs on average.
4.2 One-sample 𝑡-test of the mean
• Use: Test if the population mean equals a hypothesized mean.
• Data: 𝑥 ,𝑥 ,…,𝑥 .
1 2 𝑛
• Assumptions: The data are independent normal samples:
𝑥 ∼ 𝑁(𝜇,𝜎2) where both 𝜇 and 𝜎 are unknown.
𝑖
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 4
• 𝐻 : For a specified 𝜇 , 𝜇 = 𝜇
0 0 0
• 𝐻 :
𝐴
Two-sided: 𝜇 ≠ 𝜇
0
one-sided-greater: 𝜇 > 𝜇
0
one-sided-less: 𝜇 < 𝜇
0
𝑥−𝜇
• Test statistic: 𝑡 = √ 0,
𝑠/ 𝑛
1 𝑛
where 𝑠2 is the sample variance: 𝑠2 = ∑(𝑥 −𝑥)2
𝑛−1 𝑖
𝑖=1
• Null distribution: 𝜙(𝑡|𝐻 ) is the pdf of 𝑇 ∼ 𝑡(𝑛−1).
0
(Student 𝑡-distribution with 𝑛−1 degrees of freedom)
• 𝑝-value:
Two-sided: 𝑝 = 𝑃(|𝑇| > 𝑡) = 2*(1-pt(abs(t), n-1))
one-sided-greater: 𝑝 = 𝑃(𝑇 > 𝑡) = 1 - pt(t, n-1)
one-sided-less: 𝑝 = 𝑃(𝑇 < 𝑡) = pt(t, n-1)
• R code example: For data 𝑥 = 1, 3,5,7,2 we can run a one-sample 𝑡-test with 𝐻 :
0
𝜇 = 2.5 using the R command:
0
t.test(x, mu = 2.5, alternative=t́wo.sided)́
This will return a several pieces of information including the mean of the data, 𝑡-value
and the two-sided 𝑝-value. See the help for this function for other argument settings.
Example 3. Look in the class 18 notes or slides for an example of this test. The class 19
example R code also gives an example.
4.3 Two-sample 𝑡-test for comparing means
4.3.1 The case of equal variances
We start by describing the test assuming equal variances.
• Use: Test if the population means from two populations differ by a hypothesized
amount.
• Data: 𝑥 ,𝑥 ,…,𝑥 and 𝑦 ,𝑦 ,…,𝑦 .
1 2 𝑛 1 2 𝑚
• Assumptions: Both groups of data are independent normal samples:
𝑥 ∼ 𝑁(𝜇 ,𝜎2)
𝑖 𝑥
𝑦 ∼ 𝑁(𝜇 ,𝜎2)
𝑗 𝑦
where both 𝜇 and 𝜇 are unknown and possibly different. The variance 𝜎2 is un-
𝑥 𝑦
known, but the same for both groups.
• 𝐻 : For a specified Δ𝜇 the difference of means 𝜇 −𝜇 = Δ𝜇
0 𝑥 𝑦
• 𝐻 :
𝐴
Two-sided: 𝜇 −𝜇 ≠ Δ𝜇
𝑥 𝑦
one-sided-greater: 𝜇 −𝜇 > Δ𝜇
𝑥 𝑦
one-sided-less: 𝜇 −𝜇 < Δ𝜇
𝑥 𝑦
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 5
𝑥−𝑦̄−Δ𝜇
• Test statistic: 𝑡 = ,
𝑠
𝑃
where 𝑠2 and 𝑠2 are the sample variances of the 𝑥 and 𝑦 data respectively, and 𝑠2
𝑥 𝑦 𝑃
is (sometimes called) the pooled sample variance:
(𝑛−1)𝑠2 +(𝑚−1)𝑠2 1 1
𝑠2 = 𝑥 𝑦 ( + ) and 𝑑𝑓 = 𝑛+𝑚−2
𝑝 𝑛+𝑚−2 𝑛 𝑚
• Null distribution: 𝜙(𝑡|𝐻 ) is the pdf of 𝑇 ∼ 𝑡(𝑑𝑓), the 𝑡-distribution with 𝑑𝑓 =
0
𝑛+𝑚−2 degrees of freedom.
• 𝑝-value:
Two-sided: 𝑝 = 𝑃(|𝑇| > 𝑡) = 2*(1-pt(abs(t), df))
one-sided-greater: 𝑝 = 𝑃(𝑇 > 𝑡) = 1 - pt(t, df)
one-sided-less: 𝑝 = 𝑃(𝑇 < 𝑡) = pt(t, df)
• R code: The R function t.test will run a two-sample 𝑡-test. See the example code
in class19.r. In t.test the argument mu is used for what we have called Δ𝜇.
Notes: 1. Most often the test is done with Δ𝜇 = 0. That is, the null hypothesis is the the
means are equal, i.e. 𝜇 −𝜇 = 0.
𝑥 𝑦
2. If the 𝑥 and 𝑦 data have the same length 𝑛 = 𝑚, then the formula for 𝑠2 becomes
𝑝
simpler:
𝑠2 +𝑠2
𝑠2 = 𝑥 𝑦
𝑝 𝑛
Example 4. Look in the class 18 notes or slides for an example of the two-sample 𝑡-test.
4.3.2 The case of unequal variances
There is a form of the 𝑡-test for when the variances are not assumed equal. It is sometimes
called Welch’s 𝑡-test.
Thislooksexactlythesameasthecaseofequalexceptforasmallchangeintheassumptions
and the formula for the pooled variance:
• Use: Test if the population means from two populations differ by a hypothesized
amount.
• Data: 𝑥 ,𝑥 ,…,𝑥 and 𝑦 ,𝑦 ,…,𝑦 .
1 2 𝑛 1 2 𝑚
• Assumptions: Both groups of data are independent normal samples:
𝑥 ∼ 𝑁(𝜇 ,𝜎2)
𝑖 𝑥 𝑥
𝑦 ∼ 𝑁(𝜇 ,𝜎2)
𝑗 𝑦 𝑦
where both 𝜇 and 𝜇 are unknown and possibly different. The variances 𝜎2 and 𝜎2
𝑥 𝑦 𝑥 𝑦
are unknown and not assumed to be equal.
• 𝐻 , 𝐻 : Exactly the same as the case of equal variances.
0 𝐴
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 6
𝑥−𝑦̄−Δ𝜇
• Test statistic: 𝑡 = ,
𝑠
𝑃
where 𝑠2 and 𝑠2 are the sample variances of the 𝑥 and 𝑦 data respectively, and 𝑠2
𝑥 𝑦 𝑃
is (sometimes called) the pooled sample variance:
𝑠2 𝑠2 (𝑠2/𝑛+𝑠2/𝑚)2
𝑠2 = 𝑥 + 𝑦 and 𝑑𝑓 = 𝑥 𝑦
𝑝 𝑛 𝑚 (𝑠2/𝑛)2/(𝑛−1)+(𝑠2/𝑚)2/(𝑚−1)
𝑥 𝑦
• Null distribution: 𝜙(𝑡|𝐻 ) is the pdf of 𝑇 ∼ 𝑡(𝑑𝑓), the 𝑡 distribution with 𝑑𝑓
0
degrees of freedom.
• 𝑝-value: Exactly the same as the case of equal variances.
• Rcode: Thefunctiont.testalsohandlesthiscaseifyousettheargumentvar.equal=FALSE.
Notes. 1. In truth, the null distribution given above only approximates the exact null
distribution.
2. Notice that the degrees of freedom are unlikely to be a whole number.
3. Some people recommend always using Welch’s t-test, even if the variances are believed
to be equal. This avoids making the assumption that the variances are equal and has very
little downside if they are equal.
4.3.3 The paired two-sample 𝑡-test
When the data naturally comes in pairs (𝑥 ,𝑦 ), we can use the paired two-sample 𝑡-test.
𝑖 𝑖
(After checking the assumptions are valid!)
Example 5. To measure the effectiveness of a cholesterol lowering medication we might
test each subject before and after treatment with the drug. So for each subject we have a
pair of measurements:
𝑥 = cholesterol level before treatment
𝑖
𝑦 = cholesterol level after treatment.
𝑖
Example 6. To measure the effectiveness of a cancer treatment we might pair each subject
who received the treatment with one who did not. In this case we would want to pair
subjects who are similar in terms of stage of the disease, age, sex, etc.
• Use: Test if the average difference between paired values in a population equals a
hypothesized value.
• Data: 𝑥 ,𝑥 ,…,𝑥 and 𝑦 ,𝑦 ,…,𝑦 must have the same length.
1 2 𝑛 1 2 𝑛
• Assumptions: Thedifferences𝑤 = 𝑥 −𝑦 betweenthepairedsamplesareindependent
𝑖 𝑖 𝑖
draws from a normal distribution N(𝜇,𝜎2), where 𝜇 and 𝜎 are unknown.
• 𝐻 : For a specified 𝜇 , 𝜇 = 𝜇 .
0 0 0
• 𝐻 :
𝐴
Two-sided: 𝜇 ≠ 𝜇
0
one-sided-greater: 𝜇 > 𝜇
0
one-sided-less: 𝜇 < 𝜇
0
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 7
𝑤−𝜇
• Test statistic: 𝑡 = √ 0,
𝑠/ 𝑛
1 𝑛
where 𝑠2 is the sample variance: 𝑠2 = ∑(𝑤 −𝑤)2
𝑛−1 𝑖
𝑖=1
• Null distribution: 𝜙(𝑡|𝐻 ) is the pdf of 𝑇 ∼ 𝑡(𝑛−1).
0
(Student 𝑡-distribution with 𝑛−1 degrees of freedom)
• 𝑝-value:
Two-sided: 𝑝 = 𝑃(|𝑇| > 𝑡) = 2*(1-pt(abs(t), n-1))
one-sided-greater: 𝑝 = 𝑃(𝑇 > 𝑡) = 1 - pt(t, n-1)
one-sided-less: 𝑝 = 𝑃(𝑇 < 𝑡) = pt(t, n-1)
• R code: The R function t.test will do a paired two-sample test if you set the argu-
mentpaired=TRUE.Youcanalsorunaone-sample𝑡-teston𝑥−𝑦. Thereareexamples
of both of these in class19.r
Notes. 1. This is just a one-sample 𝑡-test using 𝑤 .
𝑖
2. Another way to write the assumption is that we assume a relation between 𝑥 and 𝑦 of
𝑖 𝑖
the form 𝑦 = 𝑥 +𝜇+𝑒. Here 𝜇 is some (unknown) constant, and 𝑒 is random error (noise)
𝑖 𝑖
of mean 0 and (unknown) variance 𝜎2.
Example 7. The following example is taken from Rice 1
To study the effect of cigarette smoking on platelet aggregation Levine (1973) drew blood
samples from 11 subjects before and after they smoked a cigarette and measured the extent
to which platelets aggregated. Here is the data:
Before 25 25 27 44 30 67 53 53 52 60 28
After 27 29 37 56 46 82 57 80 61 59 43
Difference 2 4 10 12 16 15 4 27 9 -1 15
The null hypothesis is that smoking had no effect on platelet aggregation, i.e. that the
difference between before and after should have mean 𝜇 = 0. We ran a paired two-sample
0
𝑡-test to test this hypothesis. Here is the R code: (It’s also in class19.r.)
before.cig = c(25,25,27,44,30,67,53,53,52,60,28)
after.cig = c(27,29,37,56,46,82,57,80,61,59,43)
mu0 = 0
result = t.test(after.cig, before.cig, alternative="two.sided", mu=mu0, paired=TRUE)
print(result)
Here is the output:
Paired t-test
data: after.cig and before.cig
t = 4.2716, df = 10, p-value = 0.001633
alternative hypothesis: true difference in means is not equal to 0
mean of the differences: 10.27273
We got the same results with the one-sample 𝑡-test:
t.test(after.cig - before.cig, mu=0)
1JohnRice,MathematicalStatisticsandDataAnalysis,2ndedition,p. 412. ThisexamplereferencesP.H
Levine (1973) An acute effect of cigarette smoking on platelet function. Circulation, 48, 619-623.
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 8
4.4 One-way ANOVA (𝐹-test for equal means)
• Use: Test if the population means from 𝑛 groups are all the same.
• Data: (𝑛 groups, 𝑚 samples from each group)
𝑥 , 𝑥 , …, 𝑥
1,1 1,2 1,𝑚
𝑥 , 𝑥 , …, 𝑥
2,1 2,2 2,𝑚
…
𝑥 , 𝑥 , …, 𝑥
𝑛,1 𝑛,2 𝑛,𝑚
• Assumptions: Data for each group is an independent normal sample drawn from
distributions with (possibly) different means but the same variance:
𝑥 ∼ 𝑁(𝜇 ,𝜎2)
1,𝑗 1
𝑥 ∼ 𝑁(𝜇 ,𝜎2)
2,𝑗 2
…
𝑥 ∼ 𝑁(𝜇 ,𝜎2)
𝑛,𝑗 𝑛
The group means 𝜇 are unknown and possibly different. The variance 𝜎 is unknown,
𝑖
but the same for all groups.
• 𝐻 : All the means are identical 𝜇 = 𝜇 = … = 𝜇 .
0 1 2 𝑛
• 𝐻 : Not all the means are the same.
𝐴
• Test statistic: 𝑓 = MS 𝐵, where
MS
𝑊
𝑥̄ = mean of group 𝑖
𝑖
𝑥 +𝑥 +…+𝑥
𝑖,1 𝑖,2 𝑖,𝑚
= .
𝑚
𝑥 = grand mean of all the data.
𝑠2 = sample variance of group 𝑖
𝑖
1 𝑚
= ∑(𝑥 −𝑥̄ )2.
𝑚−1 𝑖,𝑗 𝑖
𝑗=1
MS = between group variance
𝐵
= 𝑚 × sample variance of group means
𝑚 𝑛
= ∑(𝑥̄ −𝑥)2.
𝑛−1 𝑖
𝑖=1
MS = average within group variance
𝑊
= sample mean of 𝑠2,…,𝑠2
1 𝑛
𝑠2+𝑠2+…+𝑠2
= 1 2 𝑛
𝑛
• Idea: If the 𝜇 are all equal, test statistic 𝑓, which is a ratio, should be near 1. If they
𝑖
are not equal then MS should be larger while MS should remain about the same,
𝐵 𝑊
so 𝑓 should be larger. We won’t give a proof of this.
• Null distribution: 𝜙(𝑓|𝐻 ) is the pdf of 𝐹 ∼ 𝐹(𝑛−1,𝑛(𝑚−1)).
0
This is the 𝐹-distribution with (𝑛 − 1) and 𝑛(𝑚 − 1) degrees of freedom. Several
𝐹-distributions are plotted below.
• 𝑝-value: 𝑝 = 𝑃(𝐹 > 𝑓) = 1- pf(f, n-1, n*(m-1)))
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 9
0 2 4 6 8 10
0.1
8.0
6.0
4.0
2.0
0.0
F(3,4)
F(10,15)
F(30,15)
x
Notes: 1. ANOVA tests whether all the means are the same. It does not test whether
some subset of the means are the same.
2. There is a test where the variances are not assumed equal.
3. There is a test where the groups don’t all have the same number of samples.
4. R has a function aov() to run ANOVA tests.
5. See: https://en.wikipedia.org/wiki/F-test
Example 8. The table shows patients’ perceived level of pain (on a scale of 1 to 6) after
3 different medical procedures.
𝑇 𝑇 𝑇
1 2 3
2 3 2
4 4 1
1 6 3
5 1 3
3 4 5
(1) Set up and run an F-test comparing the means of these 3 treatments.
(2) Based on the test, what might you conclude about the treatments?
Solution: Using the code below, the 𝐹 statistic is 0.325 and the 𝑝-value is 0.729 At any
reasonable significance level we will fail to reject the null hypothesis that the average pain
level is the same for all three treatments..
Note, it is not reasonable to conclude the the null hypothesis is true. With just 5 data
points per procedure we might simply lack the power to distinguish different means.
R code to perform the test
# DATA ----
T1 = c(2,4,1,5,3)
T2 = c(3,4,6,1,4)
T3 = c(2,1,3,3,5)
procedure = c(rep('T1',length(T1)),rep('T2',length(T2)),rep('T3',length(T3)))
pain = c(T1,T2,T3)
data.pain = data.frame(procedure,pain)
aov.data = aov(pain∼procedure,data=data.pain) # do the analysis of variance
print(summary(aov.data)) # show the summary table
# class19.r also shows code to compute the ANOVA by hand.
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 10
The summary shows a 𝑝-value (shown as Pr(>F)) of 0.729. Therefore we do not reject the
null hypothesis that all three group population means are the same.
4.5 Chi-square test for goodness of fit
This is a test of how well a hypothesized probability distribution fits a set of data. The test
statistic is called a chi-square statistic and the null distribution associated to the chi-square
statistic is the chi-square distribution. It is denoted by 𝜒2(𝑑𝑓) where the parameter 𝑑𝑓 is
called the degrees of freedom.
Suppose we have an unknown probability mass function given by the following table.
Outcomes 𝜔 𝜔 … 𝜔
1 2 𝑛
Probabilities 𝑝 𝑝 … 𝑝
1 2 𝑛
In the chi-square test for goodness of fit we hypothesize a set of values for the probabilities.
Typicallywewillhypothesizethattheprobabilitiesfollowaknowndistributionwithcertain
parameters, e.g. binomial, Poisson, multinomial. The test then tries to determine if this
set of probabilities could reasonably have generated the data we collected.
• Use: Test whether discrete data fits a specific finite probability mass function.
• Data: An observed count 𝑂 for each possible outcome 𝜔 .
𝑖 𝑖
• Assumptions: None
• 𝐻 : The data was drawn from a specific discrete distribution.
0
• 𝐻 : The data was drawn from a different distribution.
𝐴
• Test statistic: The data consists of observed counts 𝑂 for each 𝜔 . From the null hy-
𝑖 𝑖
pothesis probability table we get a set of expected counts 𝐸 . There are two statistics
𝑖
that we can use:
𝑂
Likelihood ratio statistic 𝐺 = 2∗∑𝑂 ln( 𝑖)
𝑖 𝐸
𝑖
(𝑂 −𝐸 )2
Pearson’s chi-square statistic 𝑋2 = ∑ 𝑖 𝑖 .
𝐸
𝑖
It is a theorem that under the null hypothesis 𝑋2 ≈ 𝐺 and both are approximately
chi-square. Before computers, 𝑋2 was used because it was easier to compute. Now,
it is better to use 𝐺 although you will still see 𝑋2 used quite often.
• Degrees of freedom 𝑑𝑓: For chi-square tests the number of degrees of freedom can be
a bit tricky. In this case 𝑑𝑓 = 𝑛−1. It is computed as the number of cell counts
that can be freely set under 𝐻 consistent with the statistics needed to compute the
𝐴
expected cell counts assuming 𝐻 .
0
• Null distribution: Assuming 𝐻 , both statistics (approximately) follow a chi-square
0
distribution with 𝑑𝑓 degrees of freedom. That is both 𝜙(𝐺|𝐻 ) and 𝜙(𝑋2|𝐻 ) have
0 0
(approximately) the same pdf as 𝑌 ∼ 𝜒2(𝑑𝑓).
• 𝑝-value: Extreme data means large values of 𝑋2, i.e. large differences between the
observed and expected counts. So,
𝑝 = 𝑃(𝑌 > 𝐺) = 1 - pchisq(G, df)
𝑝 = 𝑃(𝑌 > 𝑋2) = 1 - pchisq(𝑋2, df)
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 11
• R code: The R function chisq.test can be used to do the computations for a chi-
square test use 𝑋2. For 𝐺 you either have to do it by hand or find a package that has
a function. (It will probably be called likelihood.test or G.test.
Notes. 1. When the likelihood ratio statistic 𝐺 is used the test is also called a 𝐺-test or
a likelihood ratio test.
Example 9. First chi-square example. Suppose we have an experiment that produces
numerical data. For this experiment the possible outcomes are 0, 1, 2, 3, 4, 5 or more. We
run 51 trials and count the frequency of each outcome, getting the following data:
Outcomes 0 1 2 3 4 ≥ 5
Observed counts 3 10 15 13 7 3
Suppose our null hypothesis 𝐻 is that the data is drawn from 51 trials of a binomial(8,
0
0.5) distribution and our alternative hypothesis 𝐻 is that the data is drawn from some
𝐴
other distribution. Do all of the following:
1. Make a table of the observed and expected counts.
2. Compute both the likelihood ratio statistic 𝐺 and Pearson’s chi-square statistic 𝑋2.
3. Compute the degrees of freedom of the null distribution.
4. Compute the 𝑝-values corresponding to 𝐺 and 𝑋2.
Solution: All of the R code used for this example is in class19.r.
1. Assuming 𝐻 the data truly comes from a binomial(8, 0.5) distribution. We have 51
0
total observations, so the expected count for each outcome is just 51 times its probability.
We computed the binomial(8, 0.5) probabilities and expected counts in R:
Outcomes 0 1 2 3 4 ≥ 5
Observed counts 3 10 15 13 7 3
𝐻 probabilities 0.0039 0.0313 0.1094 0.2188 0.2734 0.3633
0
Expected counts 0.20 1.59 5.58 11.16 13.95 18.53
2. Using the formulas above we compute that 𝑋2 = 116.41 and 𝐺 = 66.08
3. The only statistic used in computing the expected counts was the total number of
observations 51. So, the degrees of freedom is 5, i.e we can set 5 of the cell counts freely
and the last is determined by requiring that the total number is 51.
4. The 𝑝-values are 𝑝𝐺 =1 - pchisq(G, 5) and 𝑝𝑋2 = 1 - pchisq(𝑋2, 5). Both 𝑝-
values are effectively 0. For almost any significance level we would reject 𝐻 in favor of
0
𝐻 .
𝐴
4.5.1 Degrees of freedom in chi-square tests
We alreay gave a quick definition of degrees of freedom for a chi-square test. Here we will
try to go a little slower in showing how to compute degrees of freedom.
To start, recall that in a chi-square test, our table has 𝑛 observed counts. Then, we use
observed counts and the null hypothesis to compute 𝑛 expected counts. This is typically
done by computing some statistics and using them estimate the parameters needed to
compute the expected counts. For example, in the previous example the statistic computed
was the total number of counts.
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 12
Now, imagine that we are allowed to fabricate the 𝑛 observed counts, but we demand that
our made up observations produce the same statistics as the true observed counts. That is,
our imaginary observed counts need to produce the same expected counts as the true data.
The degrees of freedom is the number of fake observed counts we can freely choose. The
rest will be determined by our constraint that they produce the same statistics.
Example 10. (Degrees of freedom.) Suppose we have the following observed counts
Outcomes 0 1 2 3 4 5
Observed counts 6 9 13 12 7 3
Suppose our null hypothesis 𝐻 is that the data producing these counts was drawn from
0
50 trials of a binomial(5, 𝜃) distribution. Our alternative hypothesis 𝐻 is that the data
𝐴
is drawn from some other distribution. Run a chi-square test of these hypotheses with
significance 0.05.
Solution: To compute expected counts we need a value of 𝜃. Since it is not known, we
have to use the data to estimate it.
The total number of observations is 50. So, the mean of the data is
6⋅0+9⋅1+13⋅2+12⋅3+7⋅4+3⋅5
𝑚 = = 2.28.
50
The expected value of a binom(5,𝜃) distribution, is 5𝜃. The maximum likelihood estimate
for 𝜃 is 𝜃̂= 𝑚/5 = 0.456.
Now, just like in the previous example, we can compute expected counts for each possible
outcome. The expected count of outcome 𝑘 is 50⋅𝑝(𝑘). In R this is 50*dbinom(k, 50,
𝜃) ̂ . We have the following table
Outcomes 0 1 2 3 4 5
Observed counts 6 9 13 12 7 3
Expected counts 2.38 9.98 16.74 14.03 5.88 0.99
To determine the degrees of freedom:
(i) We have 6 observed counts.
(ii) To compute the expected counts we need the total number of counts = 50 and our
estimate of 𝜃̂ = 𝑚/5 That is, we have two constraints: the total number of counts is 50,
and mean 𝑚 = 2.28.
So, to get the same expected counts, we could choose 4 of the observed counts freely and
then set last two counts so the constraints are met. Thus, there are 4 degrees of freedom.
More briefly: 6 observed counts - 2 constraints = 4 degrees of freedom.
Using R we can compute 𝐺 = 8.01, with 𝑝-value 0.09. Thus, at significance level 0.05 we
would not reject the null hypothesis.
Note, the 𝑋2 statistic is 11.05 with 𝑝-value 0.026. Clearly this example is a borderline case,
since we reject 𝐻 when using 𝑋2 and we don’t when using 𝐺.
0
It bears repeating, for reasons like this, we never say 𝐻 is false. The most we can say is
0
that the data does not support rejecting 𝐻 .
0
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 13
4.5.2 More examples
Example 11. Mendel’s genetic experiments (Adapted from Rice Mathematical Statis-
tics and Data Analysis, 2nd ed., example C, p.314)
In one of his experiments on peas Mendel looked at 2 genetic trait pairs: smooth/wrinkled
and yellow/green. Symbolically we label a smooth gene 𝑆 and a wrinkled gene 𝑠. Likewise
we use 𝑌 and 𝑦 for yellow and green respectively.
Mendel started by selecting a parent generation of homozygous plants. They were either
smooth/yellow(genes𝑆𝑆𝑌𝑌)andwrinkled/green(genes𝑠𝑠𝑦𝑦). Hecrossedthesmooth/yellow
withthewrinkled/greenpeascreatingthe, socalled, 𝐹 generationconsistingofplantswith
1
genes 𝑆𝑠𝑌𝑦. Since smooth (𝑆) and yellow 𝑌 are both dominant traits, all these plants were
smooth/yellow.
Hethencrossed556pairsofthe𝐹 generationtocreatethe𝐹 generation. Wewouldexpect
1 2
1/4ofthe𝐹 generationtohavetwosmoothgenes(𝑆𝑆),1/4tohavetwowrinkledgenes(𝑠𝑠),
2
and the remaining 1/2 to be heterozygous (𝑆𝑠). We also expect these fractions for yellow
(𝑌) and green (𝑦) genes. If the color and smoothness genes are inherited independently
and smooth and yellow are both dominant we’d expect the following table of frequencies
for phenotypes.
Yellow Green
Smooth 9/16 3/16 3/4
Wrinkled 3/16 1/16 1/4
3/4 1/4 1
Probability table for the null hypothesis
So from the 556 crosses the expected number of smooth yellow peas is 556×9/16 = 312.75.
Likewise for the other possibilities. Here is a table giving the observed and expected counts
from Mendel’s experiments.
Observed count Expected count
Smooth yellow 315 312.75
Smooth green 108 104.25
Wrinkled yellow 102 104.25
Wrinkled green 31 34.75
The null hypothesis is that the observed counts are random samples distributed according
to the frequency table given above. We use the counts to compute our statistics
The likelihood ratio statistic is
𝑂
𝐺 = 2∗∑𝑂 ln( 𝑖)
𝑖 𝐸
𝑖
315 108 102 31
= 2∗(315 ln( )+108 ln( )+102 ln( )+31 ln( ))
412.75 104.25 104.25 34.75
= 0.618
Pearson’s chi-square statistic is
(𝑂 −𝐸 )2 2.752 3.752 2.252 3.752
𝑋2 = ∑ 𝑖 𝑖 = + + + = 0.604
𝐸 312.75 104.25 104.25 34.75
𝑖
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 14
You can see that the two statistics are very close. This is usually the case. In general the
likelihood ratio statistic is more robust and should be preferred.
Thedegreesoffreedomis3,becausethereare4observedquantitiesandonerelationbetween
them, i.e. they sum to 556. So, under the null hypothesis 𝐺 follows a 𝜒2(3) distribution.
Using R to compute the 𝑝-value we get
𝑝 = 1- pchisq(0.618, 3) = 0.8923
Assuming the null hypothesis we would see data at least this extreme almost 90% of the
time. We would not reject the null hypothesis for any reasonable significance level.
The 𝑝-value using Pearson’s statistic is 0.8955 –nearly identical.
The script class19.r shows these calculations and also how to use chisq.test to run a
chi-square test directly.
4.6 Chi-square test for homogeneity
This is a test to see if several independent sets of random data are all drawn from the same
distribution. (The meaning of homogeneity in this case is that all the distributions are the
same.)
• Use: Test whether 𝑚 different independent sets of discrete data are drawn from the
same distribution.
• Outcomes: 𝜔 , 𝜔 , …, 𝜔 are the possible outcomes. These are the same for each set
1 2 𝑛
of data.
• Data: We assume 𝑚 independent sets of data giving counts for each of the possible
outcomes. That is, for data set 𝑖 we have an observed count 𝑂 for each possible
𝑖,𝑗
outcome 𝜔 .
𝑗
• Assumptions: None
• 𝐻 : Each data set is drawn from the same distribution. (We don’t specify what this
0
distribution is.)
• 𝐻 : The data sets are not all drawn from the same distribution.
𝐴
• Test statistic: See the example below. There are 𝑚𝑛 cells containing counts for each
outcomeforeachdataset. Usingthenulldistributionwecanestimateexpectedcounts
for each of the data sets. The statistics 𝑋2 and 𝐺 are computed exactly as above.
• Degrees of freedom 𝑑𝑓: (𝑚−1)(𝑛−1). (See the example below.)
• The null distribution 𝜒2(𝑑𝑓). The 𝑝-values are computed just as in the chi-square test
for goodness of fit.
• R code: The R function chisq.test can be used to do the computations for a chi-
square test use 𝑋2. For 𝐺 you either have to do it by hand or find a package that has
a function. (It will probably be called likelihood.test or G.test.
Example 12. Someone claims to have found a long lost work by William Shakespeare.
They ask you to test whether or not the play was actually written by Shakespeare .
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 15
You go to https://www.opensourceshakespeare.org and pick a random 12 pages from
King Lear and count the use of common words. You do the same thing for the ‘long lost
work’. You get the following table of counts.
Word a an this that
King Lear 150 30 30 90
Long lost work 90 20 10 80
Using this data, set up and evaluate a significance test of the claim that the long lost book
is by William Shakespeare. Use a significance level of 0.1.
Solution: The null hypothesis 𝐻 : For the 4 words counted the long lost book has the
0
same relative frequencies as the counts taken from King Lear.
Thetotalwordcountofbothbookscombinedis500,sothethemaximumlikelihoodestimate
of the relative frequencies assuming 𝐻 is simply the total count for each word divided by
0
the total word count.
Word a an this that Total count
King Lear 150 30 30 90 300
Long lost work 90 20 10 80 200
totals 240 50 40 170 500
rel. frequencies under 𝐻 240/500 50/500 40/500 170/500 500/500
0
Now the expected counts for each book under 𝐻 are the total count for that book times
0
the relative frequencies in the above table. The following table gives the counts: (observed,
expected) for each book.
Word a an this that Totals
King Lear (150, 144) (30, 30) (30, 24) (90, 102) (300, 300)
Long lost work (90, 96) (20, 20) (10, 16) (80, 68) (200, 200)
Totals (249, 240) (50, 50) (40, 40) (170, 170) (500, 500)
The chi-square statistic is
(𝑂 −𝐸 )2
𝑋2 = ∑ 𝑖 𝑖
𝐸
𝑖
62 02 62 122 62 02 62 122
= + + + + + + +
144 30 24 102 96 20 16 68
≈ 7.9
Thereare8cellsandallthemarginalcountsarefixedbecausetheywereneededtodetermine
the expected counts. To be consistent with these statistics we could freely set the values
in 3 cells in the table, e.g. the 3 blue cells, then the rest of the cells are determined
in order to make the marginal totals correct. Thus 𝑑𝑓 = 3. (Or we could recall that
𝑑𝑓 = (𝑚−1)(𝑛−1) = (3)(1) = 3, where 𝑚 is the number of columns and 𝑛 is the number
of rows.)
Using R we find p = 1-pchisq(7.9,3) = 0.048. Since this is less than our significance
level of 0.1 we reject the null hypothesis that the relative frequencies of the words are the
same in both books.
If we make the further assumption that all of Shakespeare’s plays have similar word fre-
quencies (which is something we could check) we conclude that the book is probably not
18.05 Class 19, Null Hypothesis Significance Testing III, Spring 2022 16
by Shakespeare.
4.7 Other tests
There are far too many other tests to even make a dent. We will see some of them in
class and on psets. Again, we urge you to master the paradigm of NHST and recognize the
importance of choosing a test statistic with a known null distribution.
Comparison of frequentist and Bayesian inference.
Class 20, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to explain the difference between the 𝑝-value and a posterior probability to a
doctor.
2 Introduction
We have now learned about two schools of statistical inference: Bayesian and frequentist.
Bothapproachesallowonetoevaluateevidenceaboutcompetinghypotheses. Inthesenotes
we will review and compare the two approaches, starting from Bayes’ formula.
3 Bayes’ formula as touchstone
In our first unit (probability) we learned Bayes’ formula, a perfectly abstract statement
about conditional probabilities of events:
𝑃(𝐵|𝐴)𝑃(𝐴)
𝑃(𝐴|𝐵) = .
𝑃(𝐵)
We began our second unit (Bayesian inference) by reinterpreting the events in Bayes’ for-
mula:
𝑃(𝒟|ℋ)𝑃(ℋ)
𝑃(ℋ|𝒟) = .
𝑃(𝒟)
Now ℋ is a hypothesis and 𝒟 is data which may give evidence for or against ℋ. Each
term in Bayes’ formula has a name and a role.
• The prior 𝑃(ℋ) is the probability that ℋ is true before the data is considered.
• The posterior 𝑃(ℋ|𝒟) is the probability that ℋ is true after the data is considered.
• The likelihood 𝑃(𝒟|ℋ) is the evidence about ℋ provided by the data 𝒟.
• 𝑃(𝒟) is the total probability of the data taking into account all possible hypotheses.
If the prior and likelihood are known for all hypotheses, then Bayes’ formula computes the
posterior exactly. Such was the case when we rolled a die randomly selected from a cup
whosecontentsyouknew. Wecallthisthedeductivelogicofprobabilitytheory, anditgives
a direct way to compare hypotheses, draw conclusions, and make decisions.
In most experiments, the prior probabilities on hypotheses are not known. In this case, our
recourse is the art of statistical inference: we either make up a prior (Bayesian) or do our
best using only the likelihood (frequentist).
1
18.05 Class 20, Comparison of frequentist and Bayesian inference., Spring 2022 2
The Bayesian school models uncertainty by a probability distribution over hypotheses.
One’s ability to make inferences depends on one’s degree of confidence in the chosen prior,
and the robustness of the findings to alternate prior distributions may be relevant and
important.
The frequentist school only uses conditional distributions of data given specific hypotheses.
Thepresumptionisthatsomehypothesis(parameterspecifyingtheconditionaldistribution
of the data) is true and that the observed data is sampled from that distribution. In
particular, the frequentist approach does not depend on a subjective prior that may vary
from one investigator to another.
These two schools may be further contrasted as follows:
Bayesian inference
• uses probabilities for both hypotheses and data.
• depends on the prior and likelihood of observed data.
• requires one to know or construct a ‘subjective prior’.
• dominated statistical practice before the 20th century.
• may be computationally intensive due to integration over many parameters.
Frequentist inference (NHST)
• never uses or gives the probability of a hypothesis (no prior or posterior).
• depends on the likelihood 𝑃(𝒟|ℋ)) for both observed and unobserved data.
• does not require a prior.
• dominated statistical practice during the 20th century.
• tends to be less computationally intensive.
Frequentist measures like 𝑝-values and confidence intervals continue to dominate research,
especially in the life sciences. However, in the current era of powerful computers and
big data, Bayesian methods have undergone an enormous renaissance in fields like ma-
chine learning and genetics. There are now a number of large, ongoing clinical trials using
Bayesian protocols, something that would have been hard to imagine a generation ago.
While professional divisions remain, the consensus forming among top statisticians is that
the most effective approaches to complex problems often draw on the best insights from
both schools working in concert.
4 Critiques and defenses
4.1 Critique of Bayesian inference
1. The main critique of Bayesian inference is that a subjective prior is, well, subjective.
There is no single method for choosing a prior, so different people will produce different
priors and may therefore arrive at different posteriors and conclusions.
18.05 Class 20, Comparison of frequentist and Bayesian inference., Spring 2022 3
2. Furthermore, there are philosophical objections to assigning probabilities to hypotheses,
as hypotheses do not constitute outcomes of repeatable experiments in which one can mea-
sure long-term frequency. Rather, a hypothesis is either true or false, regardless of whether
one knows which is the case. A coin is either fair or unfair; treatment 1 is either better or
worse than treatment 2; the sun will or will not come up tomorrow.
4.2 Defense of Bayesian inference
1. The probability of hypotheses is exactly what we need to make decisions. When the
doctor tells me a screening test came back positive I want to know what is the probability
this means I’m sick. That is, I want to know the probability of the hypothesis “I’m sick”.
2. Using Bayes’ theorem is logically rigorous. Once we have a prior all our calculations
have the certainty of deductive logic.
3. By trying different priors we can see how sensitive our results are to the choice of prior.
4. It is easy to communicate a result framed in terms of probabilities of hypotheses.
5. Even though the prior may be subjective, one can specify the assumptions used to arrive
at it, which allows other people to challenge it or try other priors.
6. The evidence derived from the data is independent of notions about ‘data more extreme’
that depend on the exact experimental setup (see the “Stopping rules” section below).
7. Data can be used as it comes in. There is no requirement that every contingency be
planned for ahead of time.
4.3 Critique of frequentist inference
1. It is ad-hoc and does not carry the force of deductive logic. Notions like ‘data more
extreme’ are not well defined. The 𝑝-value depends on the exact experimental setup (see
the “Stopping rules” section below).
2. Experiments must be fully specified ahead of time. This can lead to paradoxical seeming
results. See the ‘voltmeter story’ in:
https://en.wikipedia.org/wiki/Likelihood_principle
3. The 𝑝-value and significance level are notoriously prone to misinterpretation. Careful
statisticians know that a significance level of 0.05 means the probability of a type I error
is 5%. That is, if the null hypothesis is true then 5% of the time it will be rejected due to
randomness. Many (most) other people erroneously think a 𝑝-value of 0.05 means that the
probability of the null hypothesis is 5%.
Strictly speaking you could argue that this is not a critique of frequentist inference but,
rather, a critique of popular ignorance. Still, the subtlety of the ideas certainly contributes
to the problem. (see “Mind your 𝑝’s” below).
4.4 Defense of frequentist inference
1. It is objective: all statisticians will agree on the 𝑝-value. Any individual can then decide
if the 𝑝-value warrants rejecting the null hypothesis.
18.05 Class 20, Comparison of frequentist and Bayesian inference., Spring 2022 4
2. Hypothesis testing using frequentist significance testing is applied in the statistical anal-
ysis of scientific investigations, evaluating the strength of evidence against a null hypothesis
with data. The interpretation of the results is left to the user of the tests. Different users
may apply different significance levels for determining statistical significance. Frequen-
tist statistics does not pretend to provide a way to choose the significance level; rather it
explicitly describes the trade-off between type I and type II errors.
3. Frequentist experimental design demands a careful description of the experiment and
methods of analysis before starting. This helps control for experimenter bias.
4. The frequentist approach has been used for over 100 years and we have seen tremendous
scientific progress. Although the frequentist themself would not put a probability on the
belief that frequentist methods are valuable, shouldn’t this history give the Bayesian a
strong prior belief in the utility of frequentist methods?
5 Mind your 𝑝’s.
We run a two-sample 𝑡-test for equal means, with 𝛼 = 0.05, and obtain a 𝑝-value of 0.04.
What are the odds that the two samples are drawn from distributions with the same mean?
(a) 19/1 (b) 1/19 (c) 1/20 (d) 1/24 (e) unknown
Solution: (e) unknown. Frequentist methods only give probabilities of statistics condi-
tioned on hypotheses. They do not give probabilities of hypotheses.
6 Stopping rules
When running a series of trials we need a rule on when to stop. Two common rules are:
1. Run exactly 𝑛 trials and stop.
2. Run trials until you see a certain result and then stop.
In this example we’ll consider two coin tossing experiments.
Experiment 1: Toss the coin exactly 6 times and report the number of heads.
Experiment 2: Toss the coin until the first tails and report the number of heads.
Jon is worried that his coin is biased towards heads, so before using it in class he tests it
for fairness. He runs an experiment and reports to Jerry that his sequence of tosses was
𝐻𝐻𝐻𝐻𝐻𝑇. But Jerry is only half-listening, and he forgets which experiment Jon ran to
produce the data.
Frequentist approach.
Since he’s forgotten which experiment Jon ran, Jerry the frequentist decides to compute
the 𝑝-values for both experiments given Jon’s data.
Let 𝜃 be the probability of heads. We have the null and one-sided alternative hypotheses
𝐻 ∶ 𝜃 = 0.5, 𝐻 ∶ 𝜃 > 0.5.
0 𝐴
Experiment 1: The null distribution is binomial(6, 0.5) so, the one sided 𝑝-value is the
probability of 5 or 6 heads in 6 tosses. Using R we get
𝑝 = 1 - pbinom(4, 6, 0.5) = 0.1094.
18.05 Class 20, Comparison of frequentist and Bayesian inference., Spring 2022 5
Experiment 2: The null distribution is geometric(0.5) so, the one sided 𝑝-value is the prob-
ability of 5 or more heads before the first tails. Using R we get
𝑝 = 1 - pgeom(4, 0.5) = 0.0313.
Using the typical significance level of 0.05, the same data leads to opposite conclusions! We
would reject 𝐻 in experiment 2, but not in experiment 1.
0
The frequentist is fine with this. The set of possible outcomes is different for the different
experiments so the notion of extreme data, and therefore 𝑝-value, is different. For example,
in experiment 1 we would consider 𝑇𝐻𝐻𝐻𝐻𝐻 to be as extreme as 𝐻𝐻𝐻𝐻𝐻𝑇. In ex-
periment 2 we would never see 𝑇𝐻𝐻𝐻𝐻𝐻 since the experiment would end after the first
tails.
Bayesian approach.
Jerry the Bayesian knows it doesn’t matter which of the two experiments Jon ran, since
the binomial and geometric likelihood functions (columns) for the data 𝐻𝐻𝐻𝐻𝐻𝑇 are
proportional. In either case, he must make up a prior, and he chooses Beta(3,3). This is a
relatively flat prior concentrated over the interval 0.25 ≤ 𝜃 ≤ 0.75.
See https://mathlets.org/mathlets/beta-distribution/
Sincethebetaandbinomial(orgeometric)distributionsformaconjugatepairtheBayesian
update is simple. Data of 5 heads and 1 tails gives a posterior distribution Beta(8,4). Here
is a graph of the prior and the posterior. The blue lines at the bottom are 50% and 90%
probability intervals for the posterior.
0.3
0.2
0.1
0.0
Prior Beta(3,3)
Posterior Beta(8,4)
0 .25 .50 .75 1.0
q
Prior and posterior distributions with 0.5 and 0.9 probability intervals
Here are the relevant computations in R:
Posterior 50% probability interval: qbeta(c(0.25, 0.75), 8, 4) = [0.58 0.76]
Posterior 90% probability interval: qbeta(c(0.05, 0.95), 8, 4) = [0.44 0.86]
𝑃(𝜃 > 0.50|data) = 1- pbeta(0.5, posterior.a, posterior.b) = 0.89
Starting from the prior Beta(3,3), the posterior probability that the coin is biased toward
heads is 0.89.
18.05 Class 20, Comparison of frequentist and Bayesian inference., Spring 2022 6
7 Making decisions
Quite often the goal of statistical inference is to help with making a decision, e.g. whether
or not to undergo surgery, how much to invest in a stock, whether or not to go to graduate
school, etc.
In statistical decision theory, consequences of taking actions are measured by a utility
function. The utility function assigns a weight to each possible outcome; in the language of
probability, it is simply a random variable.
For example, in my investments I could assign a utility of 𝑑 to the outcome of a gain of
𝑑 dollars per share of a stock (if 𝑑 < 0 my utility is negative). On the other hand, if my
tolerance for risk is low, I will assign a more negative utility to losses than to gains (say,
−𝑑2 if 𝑑 < 0 and 𝑑 if 𝑑 ≥ 0).
A decision rule combines the expected utility with evidence for each hypothesis given by
the data (e.g., 𝑝-values or posterior distributions) into a formal statistical framework for
making decisions.
In this setting, the frequentist will consider the expected utility given a hypothesis
𝐸[𝑈|ℋ]
where 𝑈 is the random variable representing utility. There are frequentist methods for
combining the expected utility with 𝑝-values of hypotheses to guide decisions.
The Bayesian can combine 𝐸[𝑈|ℋ] with the posterior (or prior if it’s before data is col-
lected) to create a Bayesian decision rule.
In either framework, two people considering the same investment may have different utility
functions and make different decisions. For example, a riskier stock (with higher potential
upside and downside) will be more appealing with respect to the first utility function above
than with respect to the second (loss-averse) one.
A significant theoretical result is that for any decision rule there is a Bayesian decision rule
which is, in a precise sense, at least as good a rule.
8 The likelihood principle
We briefly mention the likelihood principle. It can be stated succinctly as
‘All of the evidence from data is contained in its likelihood function’
• Controversial
• Consistent with Bayesian updating.
It only uses the column in the likelihood table that is for the data we actually saw.
• Inconsistent with NHST.
Computing significance and 𝑝-values uses the entire likelihood table. That is, it relies
on the probabilities of both observed and unobserved data (the full experimental
design).
18.05 Class 20, Comparison of frequentist and Bayesian inference., Spring 2022 7
• See https://en.wikipedia.org/wiki/Likelihood_principle
Confidence intervals based on normal data
Class 22, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to determine whether an expression defines a valid interval statistic.
2. Be able to compute 𝑧 and 𝑡 confidence intervals for the mean given normal data.
3. Be able to compute the 𝜒2 confidence interval for the variance given normal data.
4. Be able to define the confidence level of a confidence interval.
5. Be able to explain the relationship between the 𝑧 confidence interval (and confidence
level) and the 𝑧 non-rejection region (and significance level) in NHST.
2 Introduction
We continue to survey the tools of frequentist statistics. Suppose we have a model (proba-
bilitydistribution)forobserveddatawithanunknownparameter. WehaveseenhowNHST
uses data to test the hypothesis that the unknown parameter has a particular value.
We have also seen how point estimates like the MLE use data to provide an estimate of the
unknown parameter. On its own, a point estimate like 𝑥̄= 2.2 carries no information about
its accuracy; it’s just a single number, regardless of whether its based on ten data points or
one million data points.
For this reason, statisticians augment point estimates with confidence intervals. For exam-
ple, to estimate an unknown mean 𝜇 we might be able to say that our best estimate of
the mean is 𝑥 = 2.2 with a 95% confidence interval [1.2,3.2]. Another way to describe the
interval is: 𝑥±1.
We will leave to later the explanation of exactly what the 95% confidence level means.
For now, we’ll note that taken together the width of the interval and the confidence level
provide a measure on the strength of the evidence supporting the hypothesis that the 𝜇 is
close to our estimate 𝑥. You should think of the confidence level of an interval as analogous
to the significance level of a NHST. As explained below, it is no accident that we often see
significance level 𝛼 = 0.05 and confidence level 0.95 = 1−𝛼.
We will first explore confidence intervals in situations where you will easily be able to com-
pute by hand: 𝑧 and 𝑡 confidence intervals for the mean and 𝜒2 confidence intervals for the
variance. We will use R to handle all the computations in more complicated cases. Indeed,
the challenge with confidence intervals is not their computation, but rather interpreting
them correctly and knowing how to use them in practice.
1
18.05 Class 22, Confidence intervals based on normal data, Spring 2022 2
3 Interval statistics
Recall that our definition of a statistic is anything that can be computed from data. In
particular, the formula for a statistic cannot include unknown quantities.
Example 1. Suppose 𝑥 ,…,𝑥 is drawn from N(𝜇,𝜎2) where 𝜇 and 𝜎 are unknown.
1 𝑛
(i) 𝑥 and 𝑥−5 are statistics.
(ii) 𝑥−𝜇 is not a statistic since 𝜇 is unknown.
(iii) If 𝜇 a known value, then 𝑥−𝜇 is a statistic. This case arises when we consider the
0 0
null hypothesis 𝜇 = 𝜇 . For example, if the null hypothesis is 𝜇 = 5, then the statistic
0
𝑥−𝜇 is just 𝑥−5 from (i).
0
We can play the same game with intervals to define interval statistics
Example 2. Suppose 𝑥 ,…,𝑥 is drawn from N(𝜇,𝜎2) where 𝜇 is unknown.
1 𝑛
(i) The interval [𝑥−2.2, 𝑥+2.2] = 𝑥±2.2 is an interval statistic.
2𝜎 2𝜎
(ii) If 𝜎 is known, then [𝑥− √ , 𝑥+ √ ] is an interval statistic.
𝑛 𝑛
2𝜎 2𝜎
(iii)Ontheotherhand,if𝜎 isunknownthen[𝑥− √ , 𝑥+ √ ]isnotanintervalstatistic.
𝑛 𝑛
2𝑠 2𝑠
(iv) If 𝑠2 is the sample variance, then [𝑥− √ , 𝑥+ √ ] is an interval statistic because 𝑠2
𝑛 𝑛
is computed from the data.
We will return to (ii) and (iv), as these are respectively the 𝑧 and 𝑡 confidence intervals for
estimating 𝜇.
Technically an interval statistic is nothing more than a pair of point statistics giving the
lower and upper bounds of the interval. Our reason for emphasizing that the interval is a
statistic is to highlight the following:
1. The interval is random – new random data will produce a new interval.
2. Asfrequentists, weareperfectlyhappyusingitbecauseitdoesn’tdependonthevalue
of an unknown parameter or hypothesis.
3. As usual with frequentist statistics we have to assume a certain hypothesis, e.g. value
of 𝜇, before we can compute probabilities about the interval.
Example 3. Supposewedraw𝑛samples𝑥 ,…,𝑥 fromaN(𝜇,1)distribution, where
1 𝑛
𝜇 is unknown. Suppose we wish to know the probability that 0 is in the interval
[𝑥−2,𝑥+2]. Without knowing the value of 𝜇 this is impossible. However, we can
compute this probability for any given (hypothesized) value of 𝜇.
4. A warning which will be repeated: Be careful in your thinking about these probabili-
ties. Confidence intervals are a frequentist notion. Since frequentists do not compute
probabilities of hypotheses, the confidence level is never a probability that the
unknown parameter is in the specific confidence interval computed from
the given data.
18.05 Class 22, Confidence intervals based on normal data, Spring 2022 3
4 𝑧 confidence intervals for the mean
Throughout this section we will assume that we have normally distributed data:
𝑥 , 𝑥 , …, 𝑥 ∼ N(𝜇,𝜎2).
1 2 𝑛
As we often do, we will introduce the main ideas through examples, building on what
we know about rejection and non-rejection regions in NHST until we have constructed a
confidence interval.
4.1 Definition of 𝑧 confidence intervals for the mean
We start with 𝑧 confidence intervals for the mean. First we’ll give the formula. Then we’ll
walk through the derivation in one entirely numerical example. This will give us the basic
idea. Then we’ll repeat this example, replacing the explicit numbers by symbols. Finally
we’ll work through a computational example.
Definition: Suppose the data 𝑥 ,…,𝑥 ∼ N(𝜇,𝜎2), with unknown mean 𝜇 and known
1 𝑛
variance 𝜎2. The (1−𝛼) confidence interval for 𝜇 is
𝑧 ⋅𝜎 𝑧 ⋅𝜎
𝛼/2 𝛼/2
[𝑥 − √ , 𝑥 + √ ], (1)
𝑛 𝑛
where 𝑧 is the right critical value 𝑃(𝑍 > 𝑧 ) = 𝛼/2.
𝛼/2 𝛼/2
For example, if 𝛼 = 0.05 then 𝑧 = 1.96 so the 0.95 (or 95%) confidence interval is
𝛼/2
1.96𝜎 1.96𝜎
[𝑥− √ , 𝑥+ √ ].
𝑛 𝑛
We’ve created an applet that generates normal data and displays the corresponding 𝑧 con-
fidence interval for the mean. It also shows the 𝑡-confidence interval, as discussed in the
next section. Play around to get a sense for random intervals!
https://mathlets.org/mathlets/confidence-intervals/
Example 4. Suppose we collect 100 data points from a N(𝜇,32) distribution and the
sample mean is 𝑥 = 12. Give the 95 % confidence interval for 𝜇.
Solution: Using formula 1, this is trivial to compute: the 95% confidence interval for 𝜇 is
1.96𝜎 1.96𝜎 1.96⋅3 1.96⋅3
[𝑥− √ , 𝑥+ √ ] = [12− ,12+ ]
𝑛 𝑛 10 10
4.2 Explaining the definition part 1: non-rejection regions
Our next goal is to explain the definition 1 starting from our knowledge of rejection/non-
rejection regions. The phrase ‘non-rejection region’ is not pretty, but we will discipline
ourselves to use it instead of the inacurate phrase ‘acceptance region’.
18.05 Class 22, Confidence intervals based on normal data, Spring 2022 4
Example 5. Supposethat𝑛 = 12datapointsaredrawnfromN(𝜇,52)where𝜇isunknown.
As usual, call the average of the data 𝑥. Set up a two-sided 𝑧-test of 𝐻 ∶ 𝜇 = 2.71 at
0
significance level 𝛼 = 0.05. Describe the rejection and non-rejection regions.
Solution: Under the null hypothesis (𝜇 = 2.71) we have
𝑥−2.71
𝑧 = √ ∼ N(0,1)
5/ 12
We know that, for 𝛼 = 0.05, the non-rejection region for 𝑧 is
[−1.96,1.96].
That is, we do not reject if, assuming 𝐻 , 𝑧 is within two standard deviations of the
0
standardized mean. By definition, this means
𝑃(−1.96 ≤ 𝑧 ≤ 1.96|𝜇 = 2.71) = 0.95.
And, the rejection region is
(−∞,−1.96)∪(1.96,∞).
For confidence intervals, we will want to unwind the definition of 𝑧 and write the regions in
terms of 𝑥. This allows us to directly use the natural statistic 𝑥.
Example 6. Redo the previous example using 𝑥 as the test statistic.
Solution: Under the null hypothesis (𝜇 = 2.71) we have 𝑥 ∼ N(2.71,52) and thus
𝑖
𝑥 ∼ N(2.71,52/12)
where 52/12 is the variance 𝑥. We know that for normal data, significance 𝛼 = 0.05
corresponds to a rejection region starting 1.96 standard deviations from the hypothesized
mean. That is,
Non-rejection region: We do not reject 𝐻 if 𝑥 is in the interval
0
1.96⋅5 1.96⋅5
[2.71 − √ , 2.71 + √ ] = [−0.12, 5.54].
12 12
That is, we do not reject if, assuming 𝐻 , 𝑥 is within two standard deviations of the
0
hypothesized mean. By definition, this means
𝑃(−0.12 ≤ 𝑥 ≤ 5.54|𝜇 = 2.71) = 0.95.
Rejection region:
1.96⋅5 1.96⋅5
(−∞, 2.71 − √ ] ∪ [2.71 + √ , ∞) = (−∞, −0.12] ∪ [5.54, ∞).
12 12
The following figure shows the rejection and non-rejection regions for 𝑥. The regions repre-
sent ranges of 𝑥 so they are represented by the colored bars on the 𝑥 axis. The area of the
shaded region in the tails is the significance level.
18.05 Class 22, Confidence intervals based on normal data, Spring 2022 5
𝑁(2.71,52/12)
𝑥
−0.12 2.71 5.54
The rejection (orange) and non-rejection (blue) regions for 𝑥.
Now, what about different data or null hypotheses. This is straight-forward, let’s redo the
previous example using symbols for all quantities.
Example 7. Suppose that 𝑛 data points are drawn from N(𝜇,𝜎2) where 𝜇 is unknown and
𝜎 is known. Set up a two-sided significance test of 𝐻 ∶ 𝜇 = 𝜇 using the statistic 𝑥 at
0 0
significance level 𝛼. Describe the rejection and non-rejection regions.
Solution: Under the null hypothesis 𝜇 = 𝜇 we have 𝑥 ∼ N(𝜇 ,𝜎2) and thus
0 𝑖 0
𝑥 ∼ N(𝜇 ,𝜎2/𝑛),
0
where 𝜎2/𝑛 is the variance (𝜎 )2 of 𝑥 and 𝜇 , 𝜎 and 𝑛 are all known values.
𝑥 0
Let 𝑧 be the critical value: 𝑃(𝑍 > 𝑧 ) = 𝛼/2. Then the non-rejection and rejection
𝛼/2 𝛼/2
regions are separated by the values of 𝑥 that are 𝑧 ⋅ 𝜎 from the hypothesized mean.
𝛼/2 𝑥
𝜎
Since 𝜎 = √ we have
𝑥 𝑛
Non-rejection region: we do not reject 𝐻 if 𝑥 is in the interval
0
𝑧 ⋅𝜎 𝑧 ⋅𝜎
𝛼/2 𝛼/2
[𝜇 − √ , 𝜇 + √ ] (2)
0 𝑛 0 𝑛
Rejection region:
𝑧 ⋅𝜎 𝑧 ⋅𝜎
𝛼/2 𝛼/2
(−∞, 𝜇 − √ ] ∪ [𝜇 + √ , ∞).
0 𝑛 0 𝑛
We get the same figure as above, with the explicit numbers replaced by symbolic values.
𝑁(𝜇 ,𝜎2/𝑛)
0
𝑥
𝑧 ⋅𝜎 𝜇 𝑧 ⋅𝜎
𝜇 − 𝛼√/2 0 𝜇 + 𝛼√/2
0 𝑛 0 𝑛
The rejection (orange) and non-rejection (blue) regions for 𝑥.
4.3 Manipulating intervals: algebraic pivoting
We need to get comfortable manipulating intervals. In general, we will make use of the
type of ‘obvious’ statements that can be hard to get across. First is the notion of pivoting.
Stripping away the statistical terms, pivoting is the following algebraic maneuver.
18.05 Class 22, Confidence intervals based on normal data, Spring 2022 6
Example 8. Algebraic pivoting. Suppose we have two variables 𝑎 and 𝑏. Suppose also
that 𝑎 is in the interval [𝑏−4,𝑏+6]. Show that 𝑏 is in the interval [𝑎−6,𝑎+4].
Solution: We are given, 𝑏−4 ≤ 𝑎 ≤ 𝑏+6. Therefore,
−4 ≤ 𝑎−𝑏 ≤ 6 ⇒ 4 ≥ 𝑏−𝑎 ≥ −6 ⇒ 𝑎+4 ≥ 𝑏 ≥ 𝑎−6. QED
This is called pivoting because the roles of 𝑎 and 𝑏 are reversed along with the direction of
the inequalities.
In the example above, the ranges on either side of 𝑏 are different. Quite often they will be
the same. Here are some simple numerical examples of pivoting for symmetric intervals.
Example9. (i)1.5isintheinterval[0−2.3,0+2.3],so0isintheinterval[1.5−2.3,1.5+2.3]
(ii)Likewise1.5isnotintheinterval[0−1,0+1], so 0isnotintheinterval[1.5−1,1.5+1].
4.4 Pivoting non-rejection intervals to confidence intervals
For normal data, the non-rejection region for 𝑥 is an interval centered on 𝜇 . By pivoting,
0
we get the confidence interval for 𝜇 centered on 𝑥.
Example 10. Suppose we have 𝑛 data points with a sample mean 𝑥 and hypothesized
mean 𝜇 = 2.71. Suppose also that the null distribution is 𝑥 ∼ N(𝜇 ,32). Then with a
0 𝑖 0
significance level of 0.05 we have:
(1a) The non-rejection region is centered on 𝜇 = 2.71. That is, we don’t reject 𝐻 if 𝑥 is
0 0
in the interval
1.96𝜎 1.96𝜎
[𝜇 − √ , 𝜇 + √ ]
0 𝑛 0 𝑛
(1b) Assuming the null hypothesis we have
𝑃(𝑥 is in the non-rejection region|𝐻 ) = 1−𝛼 = 0.95.
0
That is,
1.96𝜎 1.96𝜎
𝑃 (𝜇 − √ ≤ 𝑥 ≤ 𝜇 + √ |𝐻 ) = 0.95
0 𝑛 0 𝑛 0
(2a) Pivoting (1a) gives: we don’t reject 𝐻 if 𝜇 is in the interval
0 0
1.96𝜎 1.96𝜎
[𝑥− √ , 𝑥+ √ ]
𝑛 𝑛
(2b) Pivoting (1b) gives: assuming the null hypothesis we have
1.96𝜎 1.96𝜎
𝑃 (𝑥− √ ≤ 𝜇 ≤ 𝑥+ √ |𝐻 ) = 0.95
𝑛 0 𝑛 0
The interval in (2a) is called the 0.95 confidence interval for 𝜇. It is centered on 𝑥, it has
the same width as the non-rejection region.
18.05 Class 22, Confidence intervals based on normal data, Spring 2022 7
Again, notice the symmetry: the statement ‘𝑥 is in the non-rejection interval around 𝜇 ’ is
0
equivalent to ‘𝜇 is in the confidence interval [𝑥−1.96𝜎,𝑥+1.96𝜎] around 𝑥’.
0
Here is a visualization of pivoting from intervals around 𝜇 to intervals around 𝑥. In the
0
figures, 𝜇 = 1 and 𝑥 = 1.5. The first pair of intervals have width 2 and the second pair
0
have width 4.6.
−2 −1 0 1 2 3 4
𝜇 0 𝑥
𝜇 ±1 interval centered on 𝜇 does not contain 𝑥
0 0
𝑥±1 interval centered on 𝑥 does not contain 𝜇
0
𝜇 ±2.3 interval centered on 𝜇 contains 𝑥
0 0
𝑥±2.3 interval centered on 𝑥 contains 𝜇
0
The first pair of intervals shows the interval 𝜇 ±1 pivoted to the interval 𝑥±1. Since 𝑥
0
is not in the first interval, 𝜇 is not in the pivoted interval. In the second pair of intervals,
0
since 𝑥 is in the interval 𝜇 ±2.3, we see 𝜇 is in the pivoted interval 𝑥±2.3.
0 0
4.5 Summary of normal confidence intervals: definition and properties
Suppose 𝑥 , 𝑥 ,…, 𝑥 are independent data from a N(𝜇,𝜎2) distribution. We assume 𝜇 is
1 2 𝑛
unknown, but 𝜎 is known.
• Definition. The 1−𝛼 confidence interval for 𝜇 is
𝑧 𝜎 𝑧 𝜎
𝛼/2 𝛼/2
[𝑥− √ , 𝑥+ √ ],
𝑛 𝑛
where 𝑧 is standard normal 𝛼/2 critical value.
𝛼/2
• The confidence interval only depends on 𝑥 and known values, so it is a statistic.
• The confidence interval is random: different data generate different intervals.
• If the null hypothesis is 𝜇 = 𝜇 , then the confidence interval is found by pivoting the
0
non-rejection region. If 𝜇 is in the 1−𝛼 confidence interval, then we do not reject
0
𝐻 at significance level 𝛼. Likewise, we do reject 𝐻 at significance level 𝛼 if 𝜇 is not
0 0 0
in the 1−𝛼 confidence interval.
• Assuming 𝐻 , then in 95% of random trials the 95% confidence interval will contain
0
𝜇 .
0
The following figure illustrates how we don’t reject 𝐻 if the confidence interval around 𝑥
0
contains 𝜇 and we reject 𝐻 if the confidence interval doesn’t contain 𝜇 . There is a lot in
0 0 0
the figure so we will list carefully what you are seeing:
1. WestartedwiththefigurefromExample6whichshowsthenulldistributionfor𝜇 = 2.71
0
and the rejection and non-rejection regions.
2. We added two possible values of the statistic 𝑥, i.e. 𝑥 and 𝑥 , and their confidence
1 2
intervals. Note that the width of each interval is exactly the same as the width of the
1.96⋅5
non-rejection region since both use ± √ .
12
18.05 Class 22, Confidence intervals based on normal data, Spring 2022 8
Thefirstvalue, 𝑥 , isinthenon-rejectionregionanditsintervalincludesthenullhypothesis
1
𝜇 = 2.71. This illustrates that not rejecting 𝐻 corresponds to the confidence interval
0 0
containing 𝜇 .
0
The second value, 𝑥 , is in the rejection region and its interval does not contain 𝜇 . This
2 0
illustrates that rejecting 𝐻 corresponds to the confidence interval not containing 𝜇 .
0 0
𝑁(2.71,52/12)
𝑥
𝑥 −.12 2.71 𝑥 5.54
2 1
The non-rejection region (blue) and two confidence intervals (light blue).
We can still wring one more essential observation out of this example. Our choice of null
hypothesis 𝜇 = 2.71 was completely arbitrary. If we replace 𝜇 = 2.71 by any other hy-
pothesis 𝜇 = 𝜇 then the confidence interval is the same, i.e. it does not depend on any
0
hypothesis.
4.6 Explaining the definition part 3: translating a general non-rejection
region to a confidence interval
Note that the specific values of 𝜎 and 𝑛 in the preceding example were of no particular
consequence, so they can be replaced by their symbols. In this way we can take Example 7
quickly through the same steps as Example6.
In words, Equation 2 and the corresponding figure say that we don’t reject if
𝑧 𝜎
𝛼/2
𝑥 is in the interval 𝜇 ± √ .
0 𝑛
This is exactly equivalent to saying that we don’t reject if
𝑧 𝜎
𝛼/2
𝜇 is in the interval 𝑥 ± √ . (3)
0 𝑛
We can rewrite equation 3 as: at significance level 𝛼 we don’t reject if
𝑧 ⋅𝜎 𝑧 ⋅𝜎
𝛼/2 𝛼/2
the interval [𝑥− √ , 𝑥+ √ ] contains 𝜇 . (4)
𝑛 𝑛 0
We call the interval 4 a (1−𝛼) confidence interval because, assuming 𝜇 = 𝜇 , on average
0
it will contain 𝜇 in the fraction (1−𝛼) of random trials.
0
The following figure illustrates the point that 𝜇 is in the (1−𝛼) confidence interval around
0
𝑥 is equivalent to 𝑥 is in the non-rejection region (at significance level 𝛼) for 𝐻 ∶ 𝜇 = 𝜇.
0 0
The figure shows 𝑥 is in the non-rejection region for 𝜇 , so the confidence interval around
1 0
𝑥 contains 𝜇 .
1 0
Similarly, 𝑥 is not in the non-rejection region for 𝜇 , so the confidence interval around 𝑥
2 0 2
does not contain 𝜇 .
0
18.05 Class 22, Confidence intervals based on normal data, Spring 2022 9
Note, that the confidence intervals and the non-rejection region all have the same width!
𝑁(𝜇 ,𝜎2/𝑛)
0
𝑥
𝜇 −𝑧 ⋅ √𝜎 𝜇 +𝑧 ⋅ √𝜎
𝑥 2 0 𝛼/2 𝑛 𝜇 0 𝑥 1 0 𝛼/2 𝑛
4.7 Computational example
Example 11. Supposethedata 2.5, 5.5, 8.5, 11.5 wasdrawnfromaN(𝜇,102)distribution
with unknown mean 𝜇.
(a)Computethepointestimate𝑥for𝜇andthecorresponding50%,80%and95%confidence
intervals.
(b) Consider the null hypothesis 𝜇 = 1. Would you reject 𝐻 at 𝛼 = 0.05? 𝛼 = 0.20?
0
𝛼 = 0.50? Do these two ways: first by checking if the hypothesized value of 𝜇 is in the
relevant confidence interval and second by constructing a rejection region.
Solution: (a) We compute that 𝑥 = 7.0. The critical points are
𝑧 = qnorm(0.975) = 1.96, 𝑧 = qnorm(0.9) = 1.28, 𝑧 = qnorm(0.75) =
0.025 0.1 0.25
0.67.
Since 𝑛 = 4 we have 𝑥 ∼ N(𝜇,102/4), i.e. 𝜎 = 5. So we have:
𝑥
95% conf. interval = [𝑥−𝑧 𝜎 , 𝑥+𝑧 𝜎 ] = [7−1.96⋅5, 7+1.96⋅5] = [−2.8, 16.8]
0.025 𝑥 0.025 𝑥
80% conf. interval = [𝑥−𝑧 𝜎 , 𝑥+𝑧 𝜎 ] = [7−1.28⋅5, 7+1.28⋅5] = [ 0.6, 13.4]
0.1 𝑥 0.1 𝑥
50% conf. interval = [𝑥−𝑧 𝜎 , 𝑥+𝑧 𝜎 ] = [7−0.67⋅5, 7+0.67⋅5] = [3.65, 10.35]
0.75 𝑥 0.75 𝑥
Each of these intervals is a range estimate of 𝜇. Notice that the higher the confidence level,
the wider the interval needs to be.
(b) Since 𝜇 = 1 is in the 95% and 80% confidence intervals, we would not reject the null
hypothesis at the 𝛼 = 0.05 or 𝛼 = 0.20 levels. Since 𝜇 = 1 is not in the 50% confidence
interval, we would reject 𝐻 at the 𝛼 = 0.5 level.
0
We construct the rejection regions using the same critical values as in part (a). The differ-
ence is that rejection regions are intervals centered on the hypothesized value for 𝜇: 𝜇 = 1
0
and confidence intervals are centered on 𝑥. Here are the rejection regions.
𝛼 = 0.05 ⇒ (−∞,𝜇 −𝑧 𝜎 ] ∪ [𝜇 +𝑧 𝜎 ,∞) = (−∞,−8.8] ∪ [10.8,∞)
0 0.025 𝑥 0 0.025 𝑥
𝛼 = 0.20 ⇒ (−∞,𝜇 −𝑧 𝜎 ] ∪ [𝜇 +𝑧 𝜎 ,∞) = (−∞,−5.4] ∪ [7.4,∞)
0 0.1 𝑥 0 0.1 𝑥
𝛼 = 0.25 ⇒ (−∞,𝜇 −𝑧 𝜎 ] ∪ [𝜇 +𝑧 𝜎 ,∞) = (−∞,−2.35] ∪ [4.35,∞)
0 0.25 𝑥 0 0.25 𝑥
To to do the NHST we must check whether or not 𝑥 = 7 is in the rejection region.
18.05 Class 22, Confidence intervals based on normal data, Spring 2022 10
𝛼 = 0.05: 7 < 10.8 is not in the rejection region.
We do not reject the hypothesis that 𝜇 = 1 at a significance level of 0.05.
𝛼 = 0.2: 7 < 7.4 is not in the rejection region.
We do not reject the hypothesis that 𝜇 = 1 at a significance level of 0.2.
𝛼 = 0.5: 7 > 4.35 is in the rejection region.
We reject the hypothesis that 𝜇 = 1 at a significance level 0.5.
We get the same answers using either method.
5 𝑡-confidence intervals for the mean
This will be nearly identical to normal confidence intervals. In this setting 𝜎 is not known,
so we have to make the following replacements.
𝑠 𝜎
1. Use 𝑠 = √ instead of 𝜎 = √ . Here 𝑠 is the sample variance we used before in
𝑥 𝑛 𝑥 𝑛
𝑡-tests
2. Use 𝑡-critical values instead of 𝑧-critical values.
5.1 Definition of t-confidence intervals for the mean
Definition: Suppose that 𝑥 ,…,𝑥 ∼ N(𝜇,𝜎2), where the values of the mean 𝜇 and the
1 𝑛
standard deviation 𝜎 are both unknown. . The (1−𝛼) confidence interval for 𝜇 is
𝑡 ⋅𝑠 𝑡 ⋅𝑠
𝛼/2 𝛼/2
[𝑥 − √ , 𝑥 + √ ], (5)
𝑛 𝑛
here 𝑡 is the right critical value 𝑃(𝑇 > 𝑡 ) = 𝛼/2 for 𝑇 ∼ 𝑡(𝑛−1) and 𝑠2 is the sample
𝛼/2 𝛼/2
variance of the data.
5.2 Construction of 𝑡 confidence intervals
For 𝑡 confidence intervals we repeat the construction of normal confidence intervals with 𝜎
replaced by its estimate 𝑠.
Suppose that 𝑛 data points are drawn from N(𝜇,𝜎2) where 𝜇 and 𝜎 are unknown. We’ll
derive the 𝑡 confidence interval following the same pattern as for the 𝑧 confidence interval.
Under the null hypothesis 𝜇 = 𝜇 , we have 𝑥 ∼ N(𝜇 ,𝜎2). So the studentized mean follows
0 𝑖 0
a Student 𝑡 distribution with 𝑛−1 degrees of freedom:
𝑥−𝜇
𝑡 = √ 0 ∼ 𝑡(𝑛−1).
𝑠/ 𝑛
Let 𝑡 be the critical value: 𝑃(𝑇 > 𝑡 ) = 𝛼/2, where 𝑇 ∼ 𝑡(𝑛 − 1). We know from
𝛼/2 𝛼/2
running one-sample 𝑡-tests that the non-rejection region is given by
|𝑡| ≤ 𝑡
𝛼/2
18.05 Class 22, Confidence intervals based on normal data, Spring 2022 11
Using the definition of the 𝑡-statistic to write the rejection region in terms of 𝑥 we get: at
significance level 𝛼 we don’t reject if
|𝑥−𝜇 | 𝑠
√ 0 ≤ 𝑡 ⇔ |𝑥−𝜇 | ≤ 𝑡 ⋅ √ .
𝑠/ 𝑛 𝛼/2 0 𝛼/2 𝑛
Geometrically, the right hand side says that we don’t reject if
𝑠
𝜇 is within 𝑡 ⋅ √ of 𝑥.
0 𝛼/2 𝑛
This is exactly equivalent to saying that we don’t reject if
𝑡 ⋅𝑠 𝑡 ⋅𝑠
𝛼/2 𝛼/2
the interval [𝑥 − √ , 𝑥 + √ ] contains 𝜇 .
𝑛 𝑛 0
This interval is the confidence interval defined in 5.
Example 12. Suppose the data 2.5, 5.5, 8.5, 11.5 was drawn from a N(𝜇,𝜎2) distribution
with 𝜇 and 𝜎 both unknown.
Give interval estimates for 𝜇 by finding the 95%, 80% and 50% confidence intervals.
Solution: By direct computation we have 𝑥 = 7 and 𝑠2 = 15. The critical points are
𝑡 = qt(0.975) = 3.18, 𝑡 = qt(0.9) = 1.64, and 𝑡 = qt(0.75) = 0.76.
0.025 0.1 0.25
𝑠 𝑠
95% conf. interval = [𝑥−𝑡 ⋅ √ , 𝑥+𝑡 ⋅ √ ] = [0.84, 13.16]
0.025 𝑛 0.025 𝑛
𝑠 𝑠
80% conf. interval = [𝑥−𝑡 ⋅ √ , 𝑥+𝑡 ⋅ √ ] = [3.82, 10.18]
0.1 𝑛 0.1 𝑛
𝑠 𝑠
50% conf. interval = [𝑥−𝑡 ⋅ √ , 𝑥+𝑡 ⋅ √ ] = [5.53, 8.47]
0.25 𝑛 0.25 𝑛
All of these confidence intervals give interval estimates for the value of 𝜇. Again, notice
that the higher the confidence level, the wider the corresponding interval.
6 Chi-square confidence intervals for the variance
We now turn to an interval estimate for the unknown variance.
Definition: Suppose the data 𝑥 ,…,𝑥 is drawn from N(𝜇,𝜎2) with mean 𝜇 and standard
1 𝑛
deviation 𝜎 both unknown. The (1−𝛼) confidence interval for the variance 𝜎2 is
(𝑛−1)𝑠2 (𝑛−1)𝑠2
[ , ]. (6)
𝑐 𝑐
𝛼/2 1−𝛼/2
Here 𝑐 is the right critical value 𝑃(𝑋2 > 𝑐 ) = 𝛼/2 for 𝑋2 ∼ 𝜒2(𝑛−1) and 𝑠2 is the
𝛼/2 𝛼/2
sample variance of the data.
The derivation of this interval is nearly identical to that of the previous derivations, now
startingfromthechi-squaretestforvariance. Thebasicfactweneedisthat, fordatadrawn
from N(𝜇,𝜎2), the statistic
(𝑛−1)𝑠2
𝜎2
18.05 Class 22, Confidence intervals based on normal data, Spring 2022 12
follows a chi-square distribution with 𝑛−1 degrees of freedom. So given the null hypothesis
𝐻 ∶ 𝜎 = 𝜎 , the test statistic is (𝑛−1)𝑠2/𝜎2 and the non-rejection region at significance
0 0 0
level 𝛼 is
(𝑛−1)𝑠2
𝑐 < < 𝑐 .
1−𝛼/2 𝜎2 𝛼/2
0
Pivoting algebra converts this to
(𝑛−1)𝑠2 (𝑛−1)𝑠2
> 𝜎2 > .
𝑐 0 𝑐
1−𝛼/2 𝛼/2
This says we don’t reject if
(𝑛−1)𝑠2 (𝑛−1)𝑠2
the interval [ , ] contains 𝜎2
𝑐 𝑐 0
𝛼/2 1−𝛼/2
This is our (1−𝛼) confidence interval.
A difference from the 𝑧 and 𝑡 confidence intervals is that this chi-square confidence intervals
are not exactly symmetric around the estimator 𝑠2. The reason is that the chi-square
distribution (with 𝑛−1 degrees of freedom) is not symmetric around its mean 𝑛−1.
We will continue our exploration of confidence intervals next class. In the meantime, truly
the best way is to internalize the meaning of the confidence level is to experiment with the
confidence interval applet:
https://mathlets.org/mathlets/confidence-intervals/
Confidence Intervals: Three Views
Class 23, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to find 𝑧, 𝑡 and 𝜒2 confidence intervals using the corresponding standardized
statistics.
2. Beabletouseahypothesistesttofindaconfidenceintervalforanunknownparameter.
3. Refuse to answer questions that ask, in essence, ‘given a confidence interval what is
the probability or odds that it contains the true value of the unknown parameter?’
2 Introduction
Our approach to confidence intervals in the previous reading was a combination of stan-
dardizedstatisticsandhypothesistesting. Todaywewillconsidereachoftheseperspectives
separately, as well as introduce a third formal viewpoint. Each provides its own insight.
1. Standardized statistic. Most confidence intervals are based on standardized statistics
with known distributions like 𝑧, 𝑡 or 𝜒2. This provides a straightforward way to construct
and interpret confidence intervals as a point estimate plus or minus some error.
2. Hypothesis testing. Confidence intervals may also be constructed from hypothesis
tests. In cases where we don’t have a standardized statistic this method will still work. It
agrees with the standardized statistic approach in cases where they both apply.
This view connects the notions of significance level 𝛼 for hypothesis testing and confidence
level 1−𝛼 for confidence intervals; we will see that in both cases 𝛼 is the probability of
making a ‘type 1’ error. This gives some insight into the use of the word confidence. This
view also helps to emphasize the frequentist nature of confidence intervals.
3. Formal. The formal definition of confidence intervals is perfectly precise and general.
In a mathematical sense it gives insight into the inner workings of confidence intervals.
However, because it is so general it sometimes leads to confidence intervals without useful
properties. We will not dwell on this approach. We offer it mainly for those who are
interested.
3 Confidence intervals via standardized statistics
The strategy here is essentially the same as in the previous reading. Assuming normal data
we have what we called standardized statistics like the standardized mean, Studentized
mean, and standardized variance. These statistics have well known distributions which
depend on hypothesized values of 𝜇 and 𝜎. We then use algebra to produce confidence
intervals for 𝜇 or 𝜎.
1
18.05 Class 23, Confidence Intervals: Three Views, Spring 2022 2
Don’t let the algebraic details distract you from the essentially simple idea underlying
confidence intervals: we start with a standardized statistic (e.g., 𝑧, 𝑡 or 𝜒2) and use some
algebra to get an interval that depends only on the data and known parameters.
3.1 z-confidence intervals for the mean: normal data with known stan-
dard deviation
𝑧-confidence intervals for the mean of normal data are based on the standardized mean, i.e.
the 𝑧-statistic. We start with 𝑛 independent normal samples
𝑥 ,𝑥 ,…,𝑥 ∼ N(𝜇,𝜎2).
1 2 𝑛
We assume that 𝜇 is the unknown parameter of interest and 𝜎 is known. Notationally, let’s
write the (unknown) true value of 𝜇 as 𝜇
0
We know that the standardized mean is standard normal:
𝑥−𝜇
𝑧 = √ 0 ∼ N(0,1).
𝜎/ 𝑛
For the standard normal critical value 𝑧 we have: 𝑃(−𝑧 < 𝑍 < 𝑧 ) = 1−𝛼. Thus,
𝛼/2 𝛼/2 𝛼/2
𝑥−𝜇
𝑃 (−𝑧 < √ < 𝑧 | 𝜇 = 𝜇 ) = 1−𝛼
𝛼/2 𝜎/ 𝑛 𝛼/2 0
A little bit of algebra puts this in the form of an interval around 𝜇:
𝜎 𝜎
𝑃 (𝑥−𝑧 ⋅ √ < 𝜇 < 𝑥+𝑧 ⋅ √ | 𝜇 = 𝜇 ) = 1−𝛼
𝛼/2 𝑛 𝛼/2 𝑛 0
We can emphasize that the interval depends only on the statistic 𝑥 and the known value 𝜎
by writing this as
𝜎 𝜎
𝑃 ([𝑥−𝑧 ⋅ √ , 𝑥+𝑧 ⋅ √ ] contains 𝜇 | 𝜇 = 𝜇 ) = 1−𝛼.
𝛼/2 𝑛 𝛼/2 𝑛 0
This is the (1−𝛼) 𝑧-confidence interval for 𝜇. We often write it using the shorthand
𝜎
𝑥±𝑧 ⋅ √
𝛼/2 𝑛
Think of it as 𝑥± error.
Make sure you notice that the probabilities are conditioned on 𝜇 = 𝜇 . As with all frequen-
0
tist statistics, we have to fix hypothesized values of the parameters in order to compute
probabilities.
3.2 t-confidence intervals for the mean: normal data with unknown mean
and standard deviation
𝑡-confidence intervals for the mean of normal data are based on the Studentized mean, i.e.
the 𝑡-statistic.
18.05 Class 23, Confidence Intervals: Three Views, Spring 2022 3
Again we have 𝑥 ,𝑥 ,…,𝑥 ∼ N(𝜇,𝜎2), but now we assume both 𝜇 and 𝜎 are unknown. As
1 2 𝑛
wedidabove,let’swritethe(unknown)truevalueof𝜇as𝜇 . WeknowthattheStudentized
0
mean follows a Student 𝑡 distribution with 𝑛−1 degrees of freedom. That is,
𝑥−𝜇
𝑡 = √ 0 ∼ 𝑡(𝑛−1),
𝑠/ 𝑛
where 𝑠2 is the sample variance.
Now all we have to do is replace the standardized mean by the Studentized mean and the
same logic we used for 𝑧 gives us the 𝑡-confidence interval: start with
𝑥−𝜇
𝑃 (−𝑡 < √ < 𝑡 | 𝜇 = 𝜇 ) = 1−𝛼.
𝛼/2 𝑠/ 𝑛 𝛼/2 0
A little bit of algebra isolates 𝜇 in the middle of an interval:
𝑠 𝑠
𝑃 (𝑥−𝑡 ⋅ √ < 𝜇 < 𝑥+𝑡 ⋅ √ | 𝜇 = 𝜇 ) = 1−𝛼
𝛼/2 𝑛 𝛼/2 𝑛 0
We can emphasize that the interval depends only on the statistics 𝑥 and 𝑠 by writing this
as
𝑠 𝑠
𝑃 ([𝑥−𝑡 ⋅ √ , 𝑥+𝑡 ⋅ √ ] contains 𝜇 | 𝜇 = 𝜇 ) = 1−𝛼.
𝛼/2 𝑛 𝛼/2 𝑛 0
This is the (1−𝛼) 𝑡-confidence interval for 𝜇. We often write it using the shorthand
𝑠
𝑥±𝑡 ⋅ √
𝛼/2 𝑛
Think of it as 𝑥± error.
3.3 Chi-square confidence intervals for variance: normal data with un-
known mean and standard deviation
You guessed it: 𝜒2-confidence intervals for the variance of normal data are based on the
standardized variance, i.e. the 𝜒2-statistic.
We follow the same logic as above to get a 𝜒2-confidence interval for 𝜎2. Because this is
the third time through it we’ll move a little more quickly.
We assume we have 𝑛 independent normal samples: 𝑥 ,𝑥 ,…,𝑥 ∼ N(𝜇,𝜎2). We assume
1 2 𝑛
that 𝜇 and 𝜎 are both unknown and write the (unknown) true value of 𝜎 as 𝜎 . The
0
standardized variance is
(𝑛−1)𝑠2
𝑋2 = ∼ 𝜒2(𝑛−1).
𝜎2
0
We know that the 𝑋2 statistic follows a 𝜒2 distribution with 𝑛−1 degrees of freedom.
For 𝑍 and 𝑡 we used, without comment, the symmetry of the distributions to replace 𝑧
1−𝛼/2
by −𝑧 and 𝑡 by −𝑡 . Because the 𝜒2 distribution is not symmetric we need to be
𝛼/2 1−𝛼/2 𝛼/2
explicit about the critical values on both the left and the right. That is,
𝑃(𝑐 < 𝑋2 < 𝑐 ) = 1−𝛼,
1−𝛼/2 𝛼/2
18.05 Class 23, Confidence Intervals: Three Views, Spring 2022 4
where 𝑐 and 𝑐 are right tail critical values. Thus,
𝛼/2 1−𝛼/2
(𝑛−1)𝑠2
𝑃 (𝑐 < < 𝑐 | 𝜎 = 𝜎 ) = 1−𝛼
1−𝛼/2 𝜎2 𝛼/2 0
A little bit of algebra puts this in the form of an interval around 𝜎2:
(𝑛−1)𝑠2 (𝑛−1)𝑠2
𝑃 ( < 𝜎2 < | 𝜎 = 𝜎 ) = 1−𝛼
𝑐 𝑐 0
𝛼/2 1−𝛼/2
We can emphasize that the interval depends only on the statistic 𝑠2 by writing this as
(𝑛−1)𝑠2 (𝑛−1)𝑠2
𝑃 ([ , ] contains 𝜎2 | 𝜎 = 𝜎 ) = 1−𝛼.
𝑐 𝑐 0
𝛼/2 1−𝛼/2
This is the (1−𝛼) 𝜒2-confidence interval for 𝜎2.
4 Confidence intervals via hypothesis testing
Supposewehavedatadrawnfromadistributionwithaparameter𝜃whosevalueisunknown.
A significance test for the value 𝜃 has the following short description.
1. Set the null hypothesis 𝐻 ∶ 𝜃 = 𝜃 for some special value 𝜃 , e.g. we often have 𝐻 ∶
0 0 0 0
𝜃 = 0.
2. Use the data to compute the value of a test statistic, call it 𝑥.
3. If 𝑥 is far enough into the tail of the null distribution (the distribution assuming the null
hypothesis) then we reject 𝐻 .
0
In the case where there is no special value to test we may still want to estimate 𝜃. This is
the reverse of significance testing; rather than seeing if we should reject a specific value of
𝜃 because it doesn’t fit the data we want to find the range of values of 𝜃 that do, in some
sense, fit the data. This gives us the following definitions.
Definition. Given a value 𝑥 of the test statistic, the (1−𝛼) confidence interval contains all
values 𝜃 which are not rejected (at significance level 𝛼) when they are the null hypothesis.
0
Definition. A type 1 CI error occurs when the confidence interval does not contain the
true value of 𝜃.
For a (1−𝛼) confidence interval the type 1 CI error rate is 𝛼.
Example 1. Hereisanexamplerelatingconfidenceintervalsandhypothesistests. Suppose
data𝑥isdrawnfromabinomial(12, 𝜃)distributionwith𝜃 unknown. Let𝛼 = 0.1andcreate
the (1−𝛼) = 90% confidence interval for each possible value of 𝑥.
Solution: Our strategy is to look at one possible value of 𝜃 at a time and choose rejection
regions for a significance test with 𝛼 = 0.1. Once this is done, we will know, for each value
of 𝑥, which values of 𝜃 are not rejected, i.e. the confidence interval associated with 𝑥.
To start we set up a likelihood table for binomial(12, 𝜃) in Table 1. Each row shows the
probabilities 𝑝(𝑥|𝜃) for one value of 𝜃. To keep the size manageable we only show 𝜃 in
increments of 0.1.
18.05 Class 23, Confidence Intervals: Three Views, Spring 2022 5
𝜃\𝑥 0 1 2 3 4 5 6 7 8 9 10 11 12
1.0 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00
0.9 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.02 0.09 0.23 0.38 0.28
0.8 0.00 0.00 0.00 0.00 0.00 0.00 0.02 0.05 0.13 0.24 0.28 0.21 0.07
0.7 0.00 0.00 0.00 0.00 0.01 0.03 0.08 0.16 0.23 0.24 0.17 0.07 0.01
0.6 0.00 0.00 0.00 0.01 0.04 0.10 0.18 0.23 0.21 0.14 0.06 0.02 0.00
0.5 0.00 0.00 0.02 0.05 0.12 0.19 0.23 0.19 0.12 0.05 0.02 0.00 0.00
0.4 0.00 0.02 0.06 0.14 0.21 0.23 0.18 0.10 0.04 0.01 0.00 0.00 0.00
0.3 0.01 0.07 0.17 0.24 0.23 0.16 0.08 0.03 0.01 0.00 0.00 0.00 0.00
0.2 0.07 0.21 0.28 0.24 0.13 0.05 0.02 0.00 0.00 0.00 0.00 0.00 0.00
0.1 0.28 0.38 0.23 0.09 0.02 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
0.0 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Table 1. Likelihood table for Binomial(12, 𝜃)
Tables 2-4 below show the rejection region (in orange) and non-rejection region (in blue)
for the various values of 𝜃. To emphasize the row-by-row nature of the process the Table 2
just shows these regions for 𝜃 = 1.0, then Table 3 adds in regions for 𝜃 = 0.9 and Table 4
shows them for all the values of 𝜃.
Immediately following the tables we give a detailed explanation of how the rejection/non-
rejection regions were chosen.
𝜃\𝑥 0 1 2 3 4 5 6 7 8 9 10 11 12 significance
1.0 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.000
0.9 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.02 0.09 0.23 0.38 0.28
0.8 0.00 0.00 0.00 0.00 0.00 0.00 0.02 0.05 0.13 0.24 0.28 0.21 0.07
0.7 0.00 0.00 0.00 0.00 0.01 0.03 0.08 0.16 0.23 0.24 0.17 0.07 0.01
0.6 0.00 0.00 0.00 0.01 0.04 0.10 0.18 0.23 0.21 0.14 0.06 0.02 0.00
0.5 0.00 0.00 0.02 0.05 0.12 0.19 0.23 0.19 0.12 0.05 0.02 0.00 0.00
0.4 0.00 0.02 0.06 0.14 0.21 0.23 0.18 0.10 0.04 0.01 0.00 0.00 0.00
0.3 0.01 0.07 0.17 0.24 0.23 0.16 0.08 0.03 0.01 0.00 0.00 0.00 0.00
0.2 0.07 0.21 0.28 0.24 0.13 0.05 0.02 0.00 0.00 0.00 0.00 0.00 0.00
0.1 0.28 0.38 0.23 0.09 0.02 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
0.0 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Table 2. Likelihood table for binomial(12, 𝜃) with rejection (orange)/non-rejection (blue)
regions for 𝜃 = 1.0
𝜃\𝑥 0 1 2 3 4 5 6 7 8 9 10 11 12 significance
1.0 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.000
0.9 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.02 0.09 0.23 0.38 0.28 0.026
0.8 0.00 0.00 0.00 0.00 0.00 0.00 0.02 0.05 0.13 0.24 0.28 0.21 0.07
0.7 0.00 0.00 0.00 0.00 0.01 0.03 0.08 0.16 0.23 0.24 0.17 0.07 0.01
0.6 0.00 0.00 0.00 0.01 0.04 0.10 0.18 0.23 0.21 0.14 0.06 0.02 0.00
0.5 0.00 0.00 0.02 0.05 0.12 0.19 0.23 0.19 0.12 0.05 0.02 0.00 0.00
0.4 0.00 0.02 0.06 0.14 0.21 0.23 0.18 0.10 0.04 0.01 0.00 0.00 0.00
0.3 0.01 0.07 0.17 0.24 0.23 0.16 0.08 0.03 0.01 0.00 0.00 0.00 0.00
0.2 0.07 0.21 0.28 0.24 0.13 0.05 0.02 0.00 0.00 0.00 0.00 0.00 0.00
0.1 0.28 0.38 0.23 0.09 0.02 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
0.0 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
Table 3. Likelihood table: rejection (orange)/non-rejection (blue) regions for 𝜃 = 1.0 and
0.9
18.05 Class 23, Confidence Intervals: Three Views, Spring 2022 6
𝜃\𝑥 0 1 2 3 4 5 6 7 8 9 10 11 12 significance
1.0 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 1.00 0.000
0.9 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.02 0.09 0.23 0.38 0.28 0.026
0.8 0.00 0.00 0.00 0.00 0.00 0.00 0.02 0.05 0.13 0.24 0.28 0.21 0.07 0.073
0.7 0.00 0.00 0.00 0.00 0.01 0.03 0.08 0.16 0.23 0.24 0.17 0.07 0.01 0.052
0.6 0.00 0.00 0.00 0.01 0.04 0.10 0.18 0.23 0.21 0.14 0.06 0.02 0.00 0.077
0.5 0.00 0.00 0.02 0.05 0.12 0.19 0.23 0.19 0.12 0.05 0.02 0.00 0.00 0.092
0.4 0.00 0.02 0.06 0.14 0.21 0.23 0.18 0.10 0.04 0.01 0.00 0.00 0.00 0.077
0.3 0.01 0.07 0.17 0.24 0.23 0.16 0.08 0.03 0.01 0.00 0.00 0.00 0.00 0.052
0.2 0.07 0.21 0.28 0.24 0.13 0.05 0.02 0.00 0.00 0.00 0.00 0.00 0.00 0.073
0.1 0.28 0.38 0.23 0.09 0.02 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.026
0.0 1.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.000
Table 4. Likelihood table: rejection (orange)/non-rejection (blue) regions for 𝜃 = 0.0 to
1.0
Choosing the rejection and non-rejection regions in the tables
The first problem we confront is how exactly to choose the rejection region. We used two
rules:
1. The total probabilitiy of the rejection region, i.e. the significance, should be less than or
equal to 0.1. (Since we have a discrete distribution it is impossible to make the significance
exactly 0.1.)
2. We build the rejection region by choosing values of 𝑥 one at a time, always picking the
unused value with the smallest probability. We stop when the next value would make the
significance more that 0.1.
There are other ways to choose the rejection region which would result in slight differences.
Our method is one reasonable way.
Table 2 shows the rejection (orange) and non-rejection (blue) regions for 𝜃 = 1.0. This is
a special case because most of the probabilities in this row are 0.0. We’ll move right on to
the next table and step through the process for that.
In Table 3, let’s walk through the steps used to find these regions for 𝜃 = 0.9.
• The smallest probability is when 𝑥 = 0, so 𝑥 = 0 is in the rejection region.
• The next smallest is when 𝑥 = 1, so 𝑥 = 1 is in the rejection region.
• We continue with 𝑥 = 2,…,8. At this point the total probability in the rejection
region is 0.026.
• The next smallest probability is when 𝑥 = 9. Adding this probability (0.09) to 0.026
would put the total probability over 0.1. So we leave 𝑥 = 9 out of the rejection region
and stop the process.
Note three things for the 𝜃 = 0.9 row:
1. None of the probabilities in this row are truly zero, though some are small enough that
they equal 0 to 2 decimal places.
2. We show the significance for this value of 𝜃 in the right hand margin. More precisely, we
show the significance level of the NHST with null hypothesis 𝜃 = 0.9 and the given rejection
region.
18.05 Class 23, Confidence Intervals: Three Views, Spring 2022 7
3. The rejection region consists of values of 𝑥. When we say the rejection region is shown
in orange we really mean the rejection region contains the values of 𝑥 corresponding to the
probabilities highlighted in orange.
Think: Look back at the 𝜃 = 1.0 row and make sure you understand why the rejection
region is 𝑥 = 0,…,11 and the significance is 0.000.
Example 2. Using Table 4 determine the 0.90 confidence interval when 𝑥 = 8.
Solution: The 90% confidence interval consists of all those 𝜃 that would not be rejected
by an 𝛼 = 0.1 hypothesis test when 𝑥 = 8. Looking at the table, the blue (non-rejected)
entries in the column 𝑥 = 8 correspond to 0.5 ≤ 𝜃 ≤ 0.8: the confidence interval is [0.5,0.8].
Remark: The point of this example is to show how confidence intervals and hypothesis
tests are related. Since Table 4 has only finitely many values of 𝜃, our answer is close but
not exact. Using a computer we could look at many more values of 𝜃. For this problem we
used R to find that, correct to 2 decimal places, the confidence interval is [0.42,0.85].
Example 3. Explain why the expected type one CI error rate will be at most 0.092,
provided that the true value of 𝜃 is in the table.
Solution: The short answer is that this is the maximum significance for any 𝜃 in Table 4.
Expanding on that slightly: we make a type one CI error if the confidence interval does not
contain the true value of 𝜃, call it 𝜃 . This happens exactly when the data 𝑥 is in the
true
rejection region for 𝜃 . The probability of this happening is the significance for 𝜃 and
true true
this is at most 0.092.
Remark: The point of this example is to show how confidence level, type one CI error rate
and significance for each hypothesis are related. As in the previous example, we can use R
to compute the significance for many more values of 𝜃. When we do this we find that the
maximum significance for any 𝜃 is 0.1 ocurring when 𝜃 ≈ 0.0452.
Summary notes:
1. We start with a test statistic 𝑥. The confidence interval is random because it depends
on 𝑥.
2. For each hypothesized value of 𝜃 we make a significance test with significance level 𝛼 by
choosing rejection regions.
3. For a specific value of 𝑥 the associated confidence interval for 𝜃 consists of all 𝜃 that
aren’t rejected for that value, i.e. all 𝜃 that have 𝑥 in their non-rejection regions.
4. Because the distribution is discrete we can’t always achieve the exact significance level,
so our confidence interval is really an ‘at least 90% confidence interval’.
Example4. Opentheapplethttps://mathlets.org/mathlets/confidence-intervals/.
We want you to play with the applet to understand the random nature of confidence inter-
vals and the meaning of confidence as (1 - type I CI error rate).
(a) Read the help. It is short and will help orient you in the applet. Play with different
settings of the parameters to see how they affect the size of the confidence intervals.
(b) Set the number of trials to 𝑁 = 1. Click the ‘Run N trials’ button repeatedly and see
that each time data is generated the confidence intervals jump around.
(c) Now set the confidence level to 𝑐 = 0.5. As you click the ‘Run N trials’ button you
18.05 Class 23, Confidence Intervals: Three Views, Spring 2022 8
should see that about 50% of the confidence intervals include the true value of 𝜇. The ‘Z
correct’ and ‘t correct’ values should change accordingly.
(d) Now set the number of trials to 𝑁 = 100. With 𝑐 = 0.8. The ‘Run N trials’ button will
now run 100 trials at a time. Only the last confidence interval will be shown in the graph,
but the trials all run and the ‘percent correct’ statistics will be updated based on all 100
trials.
Click the run trials button repeatedly. Watch the correct rates start to converge to the
confidence level. To converge even faster, set 𝑁 = 1000.
5 Formal view of confidence intervals
Recall: An interval statistic is an interval 𝐼 computed from data 𝑥. An interval is deter-
𝑥
mined by its lower and upper bounds, and these are random because 𝑥 is random.
We suppose that 𝑥 is drawn from a distribution with pdf 𝑓(𝑥|𝜃) where the parameter 𝜃 is
unknown.
Definition: A (1−𝛼) confidence interval for 𝜃 is an interval statistic 𝐼 such that
𝑥
𝑃(𝐼 contains 𝜃 | 𝜃 = 𝜃 ) = 1−𝛼
𝑥 0 0
for all possible values of 𝜃 .
0
We wish this was simpler, but a definition is a definition and this definition is one way to
weigh the evidence provided by the data 𝑥. Let’s unpack it a bit.
The confidence level of an interval statistic is a probability concerning a random interval
and a hypothesized value 𝜃 for the unknown parameter. Precisely, it is the probability
0
that the random interval 𝐼 (computed from random data 𝑥) contains the value 𝜃 , given
𝑥 0
that the model parameter truly is 𝜃 . Since the true value of 𝜃 is unknown, the frequentist
0
statistician defines 95% confidence intervals so that the 0.95 probability is valid no matter
which hypothesized value of the parameter is actually true.
6 Comparison with Bayesian probability intervals
Confidenceintervalsareafrequentistnotion,andaswe’verepeatedmanytimes,frequentists
don’tassignprobabilitiestohypotheses,e.g.,tothevalueofanunknownparameter. Rather
they compute likelihoods; that is, probabilities about data or associated statistics given a
hypothesis (note the condition 𝜃 = 𝜃 in the formal view of confidence intervals). Note that
0
the construction of confidence intervals proceeds entirely from the full likelihood table.
In contrast Bayesian posterior probability intervals are truly the probability that the value
of the unknown parameter lies in the reported range. We add the usual caveat that this
depends on the specific choice of a (possibly subjective) Bayesian prior.
This distinction between the two is subtle because Bayesian posterior probability intervals
and frequentist confidence intervals share the following properties:
1. They start from a model 𝑓(𝑥|𝜃) for observed data 𝑥 with unknown parameter 𝜃.
18.05 Class 23, Confidence Intervals: Three Views, Spring 2022 9
2. Given data 𝑥, they give an interval 𝐼(𝑥) specifying a range of values for 𝜃.
3. They come with a number (say 0.95) that is the probability of something.
In practice, many people misinterpret confidence intervals as Bayesian probability inter-
vals, forgetting that frequentists never place probabilities on hypotheses (this is analogous
to mistaking the 𝑝-value in NHST for the probability that 𝐻 is false). The next section
0
explores this mistake in some detail. The harm of this misinterpretation is somewhat miti-
gated by that fact that, given enough data and a reasonable prior, Bayesian and frequentist
intervals often work out to be quite similar.
For an amusing example illustrating how they can be quite different, see the first answer
in the link just below (involving chocolate chip cookies!). This example uses the formal
definitions and is really about confidence sets instead of confidence intervals.
https://stats.stackexchange.com/questions/2272/whats-the-difference-between-a-confidence-interval-and-a-credible-interval
7 Misinterpreting confidence intervals
It is very tempting to think that given a 95% confidence interval for, say, the mean, the
probability that the true mean is in the confidence interval is 95%.
We know this can’t be true because the value of the mean can only be hypothesized and
Frequentists don’t assign probabilities to hypotheses. To be more concrete, if the mean is
𝜃 and the confidence interval is [45,55] then the statement 45 ≤ 𝜃 ≤ 55 is a hypothesis, so
asking for the probability that 45 ≤ 𝜃 ≤ 55, is asking for the probability of a hypothesis.
The mistake is subtle and hard to wrap your mind around. It boils down to a question of
what is being randomly sampled. Here is an attempt to explain the issue.
First, consider a test for a disease. Assume a person is given the test. Let 𝑇+ be a
positive test and 𝐷+ be that they have the disease. Assume the test is 95% accurate, i.e.
𝑃(𝑇+|𝐷+) = 0.95. We know (base rate fallacy) that this does not imply that 𝑃(𝐷+|𝑇+) =
0.95.
Let’s look at this from a different angle: Implicit in 𝑃(𝑇+|𝐷+) = 0.95 is the following
experiment: Draw a random person from the set of all people with the disease and give
them the test. Then 95% will test positive. That is, the population sampled is all people
with the disease and the event considered is that the chosen person in that population tests
positive.
For 𝑃(𝐷+|𝑇+), the experiment is to draw a random person from the set of all people who
testedpositive. Theprobabilityisthefractionwhohavethedisease. Thatis,thepopulation
sampled is all people who test positive and the event considered is that the chosen person
in that population has the disease.
We can’t expect 𝑃(𝑇+|𝐷+) and 𝑃(𝐷+|𝑇+) to be the same, since we’re sampling from
different populations and looking at different events. The probability 𝑃(𝐷+|𝑇+) can be
computed using Bayes’ theorem from the (prior) probability 𝑃(𝐷+) and the likelihoods
𝑃(𝑇+|𝐷+), 𝑃(𝑇+|𝐷−).
Confidence intervals are a little more abstract, but the analysis is similar. Just as in testing
for a disease, the populations sampled will be different. One source of diﬀiculty is that the
18.05 Class 23, Confidence Intervals: Three Views, Spring 2022 10
events are essentially the same in both cases.
Let’s assume we have a distribution with unknown mean 𝜃 . We generate some data and
0
computea95%confidenceintervalforthemean. Thevalueof95%comesfromthefollowing
implied experiment: imagine having run many trials and created a confidence interval for
each one. Then, 95% of confidence intervals contain the true mean. In notation,
𝑃(random interval contains 𝜃 ) = 0.95.
0
That is, the random sample is drawn from the set of all confidence intervals generated by
our trials. The event in question is that the chosen interval contains the true mean.
What if we run one experiment and generate the 95% confidence interval, call it 𝐼. To a
Frequentist,thetruemeanisnotrandomandwehaveafixedinterval. So,totheFrequentist,
it makes no sense to ask about the probability 𝜃 is in 𝐼.
0
To a Bayesian, it is fine to consider 𝜃 as randomly drawn from a probability distribution
0
–they often interpret it as a description of the uncertainty of our knowledge. So, they can
ask for the probability
𝑃(random 𝜃 is in a given 𝐼).
0
So, here, the random sample is drawn from the set of possible means and the event consid-
ered is that the chosen mean is contained in the given interval.
As in the disease testing example, what population is being randomly sampled is different
in the two cases, i.e in the first we have a random interval, in the second we have a random
value for the true mean. As noted above, in both cases the event is that the true mean is
in the interval.
We finish by noting that 𝑃(random 𝜃 is in 𝐼) can be computed using Bayes’ theorem and
0
depends on the prior distribution for the true mean and the likelihoods that each mean will
generate the given confidence interval. The formula is a little unwieldy. Here it is.
• Call the interval 𝐼 and the true mean 𝜃 .
0
• Call the data 𝐼. This is a shorthand for the data that the interval 𝐼 is based on.
• Let 𝑝(𝜃) be the prior probability that 𝜃 = 𝜃.
0
• Thelikelihood𝑓(𝐼|𝜃)istheprobability(ordensity)thattheexperimentwouldproduce
the interval 𝐼 given 𝜃 = 𝜃.
0
• Let 𝑝(𝜃|𝐼) be the posterior probability that 𝜃 = 𝜃. This is the updated probability
0
found using the Bayes’ theorem.
Bayes’ theorem gives us
𝑓(𝐼|𝜃)𝑝(𝜃)
𝑝(𝜃|𝐼) = , where 𝑓(𝐼) = ∑𝑓(𝐼|𝜃)𝑝(𝜃).
𝑓(𝐼)
𝜃
So we have, 𝑃(𝜃 ∈ 𝐼|𝐼) = ∑ 𝑝(𝜃|𝐼). (As usual, if 𝜃 has a continuous range of values,
0
𝜃in𝐼
then the sums will be replaced by integrals.)
Confidence Intervals for the Mean of Non-normal Data
Class 23, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to derive the formula for conservative normal confidence intervals for the
proportion 𝜃 in Bernoulli data.
2. Be able to find rule-of-thumb 95% confidence intervals for the proportion 𝜃 of a
Bernoulli distribution.
3. Beabletofindlargesampleconfidenceintervalsforthemeanofageneraldistribution.
2 Introduction
So far, we have focused on constructing confidence intervals for data drawn from a normal
distribution. We’llnowswitchgearsandlearnaboutconfidenceintervalsforthemeanwhen
the data is not necessarily normal.
Wewill first look carefully at estimating the probability𝜃 of success when the data is drawn
fromaBernoulli(𝜃)distribution–recallthat𝜃isalsothemeanoftheBernoullidistribution.
Then we will consider the case of a large sample from an unknown distribution. In this case
we can appeal to the central limit theorem to justify the use 𝑧-confidence intervals.
3 Bernoulli data and polling
One common use of confidence intervals is for estimating the proportion 𝜃 in a Bernoulli(𝜃)
distribution. Forexample,supposewewanttouseapoliticalpolltoestimatetheproportion
of the population that supports candidate A, or equivalent the probability 𝜃 that a random
person supports candidate A. In this case we have a simple rule-of-thumb that allows us to
quickly compute a confidence interval.
3.1 Conservative normal confidence intervals
Suppose we have i.i.d. data 𝑥 ,𝑥 ,…,𝑥 all drawn from a Bernoulli(𝜃) distribution. then
1 2 𝑛
a conservative normal (1−𝛼) confidence interval for 𝜃 is given by
1
𝑥 ± 𝑧 ⋅ √ . (1)
𝛼/2 2 𝑛
Theproofgivenbelowusesthecentrallimittheoremandtheobservationthat𝜎 = √𝜃(1−𝜃) ≤
1/2.
You will also see in the derivation below that this formula is conservative, providing an ‘at
least (1−𝛼)’ confidence interval.
1
18.05 Class 23, Confidence Intervals for the Mean of Non-normal Data , Spring 2022 2
Example 1. A pollster asks 196 people if they prefer candidate A to candidate B and finds
that 120 prefer 𝐴 and 76 prefer 𝐵. Find the 95% conservative normal confidence interval
for 𝜃, the proportion of the population that prefers 𝐴.
Solution: We have 𝑥 = 120/196 = 0.612, 𝛼 = 0.05 and 𝑧 = 1.96. The formula says a
0.025
95% confidence interval is
1.96
𝐼 ≈ 0.612 ± = 0.612±0.007.
2⋅14
3.2 Proof of Formula 1
The proof of Formula 1 will rely on the following fact.
Fact. The standard deviation of a Bernoulli(𝜃) distribution is at most 0.5.
Proof of fact: Let’s denote this standard deviation by 𝜎 to emphasize its dependence on
𝜃
𝜃. The variance is then 𝜎2 = 𝜃(1−𝜃). It’s easy to see using calculus or by graphing this
𝜃
parabola that the maximum occurs when 𝜃 = 1/2. Therefore the maximum variance is 1/4,
which implies that the standard deviation 𝜎 is less the √1/4 = 1/2.
𝑝
Proof of formula (1). The proof relies on the central limit theorem which says that (for
large 𝑛) the distribution of 𝑥 is approximately normal with mean 𝜃 and standard deviation
√
𝜎 / 𝑛. For normal data we have the (1−𝛼) 𝑧-confidence interval
𝜃
𝜎
𝑥 ± 𝑧 ⋅ √𝜃
𝛼/2 𝑛
The trick now is to replace 𝜎 by 1: since 𝜎 ≤ 1 the resulting interval around 𝑥
𝜃 2 𝜃 2
1
𝑥 ± 𝑧 ⋅ √
𝛼/2 2 𝑛
√
is always at least as wide as the interval using ±𝜎 / 𝑛. A wider interval is more likely to
𝜃
contain the true value of 𝜃 so we have a ‘conservative’ (1−𝛼) confidence interval for 𝜃.
Again, we call this conservative because √1 overestimates the standard deviation of 𝑥,̄
2 𝑛
resulting in a wider interval than is necessary to achieve a (1−𝛼) confidence level.
3.3 How political polls are reported
Political polls are often reported as a value with a margin-of-error. For example you might
hear
52% favor candidate A with a margin-of-error of ±5%.
The actual precise meaning of this is
if 𝜃 is the proportion of the population that supports A then the point
estimate for 𝜃 is 52% and the 95% confidence interval is 52%±5%.
Notice that reporters of polls in the news do not mention the 95% confidence. You just
have to know that that’s what pollsters do.
18.05 Class 23, Confidence Intervals for the Mean of Non-normal Data , Spring 2022 3
The 95% rule-of-thumb confidence interval.
Recall that the (1−𝛼) conservative normal confidence interval is
1
𝑥 ± 𝑧 ⋅ √ .
𝛼/2 2 𝑛
If we use the standard approximation 𝑧 = 2 (instead of 1.96) we get the rule-of thumb
0.025
95% confidence interval for 𝜃:
1
𝑥 ± √ .
𝑛
Example 2. Polling. Suppose there will soon be a local election between candidate 𝐴 and
candidate 𝐵. Suppose that the fraction of the voting population that supports 𝐴 is 𝜃.
Two polling organizations ask voters who they prefer.
1. The firm of Fast and First polls 40 random voters and finds 22 support 𝐴.
2. The firm of Quick but Cautious polls 400 random voters and finds 190 support 𝐴.
Find the point estimates and 95% rule-of-thumb confidence intervals for each poll. Explain
how the statistics reflect the intuition that the poll of 400 voters is more accurate.
Solution: For poll 1 we have
Point estimate: 𝑥 = 22/40 = 0.55
1 1
Confidence interval: 𝑥 ± √ = 0.55 ± √ = 0.55 ± 0.16 = 55% ± 16%.
𝑛 40
For poll 2 we have
Point estimate: 𝑥 = 190/400 = 0.475
1 1
Confidence interval: 𝑥 ± √ = 0.475 ± √ = 0.475 ± 0.05 = 47.5% ± 5%.
𝑛 400
The greater accuracy of the poll of 400 voters is reflected in the smaller margin of error, i.e.
5% for the poll of 400 voters vs. 16% for the poll of 40 voters.
Other binomial proportion confidence intervals
Therearemanymethodsofproducingconfidenceintervalsfortheproportion𝑝ofabinomial(𝑛,
𝑝) distribution. For a number of other common approaches, see:
https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval
4 Large sample confidence intervals
Onetypicalgoalinstatisticsistoestimatethemeanofadistribution. Whenthedatafollows
a normal distribution we could use confidence intervals based on standardized statistics to
estimate the mean.
But suppose the data 𝑥 ,𝑥 ,…,𝑥 is drawn from a distribution with pmf or pdf 𝑓(𝑥) that
1 2 𝑛
may not be normal or even parametric. If the distribution has finite mean and variance
and if 𝑛 is suﬀiciently large, then the following version of the central limit theorem shows
we can still use a standardized statistic.
Central Limit Theorem: For large 𝑛, the sampling distribution of the studentized mean
𝑥̄−𝜇
is approximately standard normal: √ ≈ N(0,1).
𝑠/ 𝑛
18.05 Class 23, Confidence Intervals for the Mean of Non-normal Data , Spring 2022 4
So for large 𝑛 the (1−𝛼) confidence interval for 𝜇 is approximately
𝑠 𝑠
[𝑥̄− √ ⋅𝑧 , 𝑥̄+ √ ⋅𝑧 ]
𝑛 𝛼/2 𝑛 𝛼/2
where 𝑧 is the 𝛼/2 critical value for N(0,1). This is called the large sample confidence
𝛼/2
interval.
Example 3. How large must 𝑛 be?
Recall that a type 1 CI error occurs when the confidence interval does not contain the true
value of the parameter, in this case the mean. Let’s call the value (1 − 𝛼) the nominal
confidence level. We say nominal because unless 𝑛 is large we shouldn’t expect the true
type 1 CI error rate to be 𝛼.
We can run numerical simulations to approximate of the true confidence level. We expect
that as 𝑛 gets larger the true confidence level of the large sample confidence interval will
converge to the nominal value.
We ran such simulations for 𝑥 drawn from the exponential distribution exp(1) (which is far
from normal). For several values of 𝑛 and nominal confidence level 𝑐 we ran 100,000 trials.
Each trial consisted of the following steps:
1. draw 𝑛 samples from exp(1).
2. compute the sample mean 𝑥̄ and sample standard deviation 𝑠.
𝑠
3. construct the large sample 𝑐 confidence interval: 𝑥±𝑧 ⋅ √ .
𝛼/2 𝑛
4. check for a type 1 CI error, i.e. see if the true mean 𝜇 = 1 is not in the interval.
With100,000trials, theempiricalconfidencelevelshouldcloselyapproximatethetruelevel.
For comparison we ran the same tests on data drawn from a standard normal distribution.
Here are the results.
nominal conf. nominal conf.
𝑛 1−𝛼 simulated conf. 𝑛 1−𝛼 simulated conf.
20 0.95 0.905 20 0.95 0.936
20 0.90 0.856 20 0.90 0.885
20 0.80 0.762 20 0.80 0.785
50 0.95 0.930 50 0.95 0.944
50 0.90 0.879 50 0.90 0.894
50 0.80 0.784 50 0.80 0.796
100 0.95 0.938 100 0.95 0.947
100 0.90 0.889 100 0.900 0.896
100 0.80 0.792 100 0.800 0.797
400 0.95 0.947 400 0.950 0.949
400 0.90 0.897 400 0.900 0.898
400 0.80 0.798 400 0.800 0.798
Simulations for exp(1) Simulations for N(0,1).
For the exp(1) distribution we see that for 𝑛 = 20 the simulated confidence of the large
sample confidence interval is less than the nominal confidence 1−𝛼. But for 𝑛 = 100 the
simulated confidence and nominal confidence are quite close. So for exp(1), 𝑛 somewhere
between 50 and 100 is large enough for most purposes.
18.05 Class 23, Confidence Intervals for the Mean of Non-normal Data , Spring 2022 5
Think: For 𝑛 = 20 why is the simulated confidence for the N(0,1) distribution is smaller
than the nominal confidence?
Thisisbecauseweused𝑧 insteadof𝑡 . Forlarge𝑛thesearequiteclose, butfor𝑛 = 20
𝛼/2 𝛼/2
there is a noticable difference, e.g. 𝑧 = 1.96 and 𝑡 = 2.09.
0.025 0.025
Bootstrap confidence intervals
Class 24, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to construct and sample from the empirical distribution of data.
2. Be able to explain the bootstrap principle.
3. Be able to design and run an empirical percentile or basic bootstrap to compute
confidence intervals.
4. Be able to design and run a parametric bootstrap to compute confidence intervals.
2 Introduction
The empirical bootstrap is a statistical technique popularized by Bradley Efron in 1979.
Though remarkably simple to implement, the bootstrap would not be feasible without
modern computing power. The key idea is to perform computations on the data itself
to estimate the variation of statistics that are themselves computed from the same data.
That is, the data is ‘pulling itself up by its own bootstrap.’ (A google search of ‘by ones
own bootstraps’ will give you the etymology of this metaphor.) Such techniques existed
before 1979, but Efron widened their applicability and demonstrated how to implement the
bootstrap effectively using computers. He also coined the term ‘bootstrap’ 1.
The empircal bootstrap is also known as the nonparametric bootstrap.
Our main application of the bootstrap will be to estimate the variation of point estimates;
that is, to estimate confidence intervals. An example will make our goal clear.
Example 1. Suppose we have data
𝑥 ,𝑥 ,…,𝑥
1 2 𝑛
IfweknewthedatawasdrawnfromN(𝜇,𝜎2)withtheunknownmean𝜇andknownvariance
𝜎2 then we have seen that
𝜎 𝜎
[𝑥−1.96√ , 𝑥+1.96√ ]
𝑛 𝑛
is a 95% confidence interval for 𝜇.
Now suppose the data is drawn from some completely unknown distribution. To have a
name we’ll call this distribution 𝐹 and its (unknown) mean 𝜇. We can still use the sample
mean 𝑥 as a point estimate of 𝜇. But how can we find a confidence interval for 𝜇 around
𝑥? Our answer will be to use the bootstrap!
1Paraphrased from Dekking et al. A Modern Introduction to Probabilty and Statistics, Springer, 2005,
page 275.
1
18.05 Class 24, Bootstrap confidence intervals, Spring 2022 2
In fact, we’ll see that the bootstrap handles other statistics as easily as it handles the mean.
For example: the median, other percentiles or the trimmed mean. These are statistics
where, even for normal distributions, it can be diﬀicult to compute a confidence interval
from theory alone.
3 Sampling
In statistics to sample from a set is to choose elements from that set. In a random sample
the elements are chosen randomly. There are two common methods for random sampling.
Sampling without replacement
Suppose we draw 10 cards at random from a deck of 52 cards without putting any of the
cards back into the deck between draws. This is called sampling without replacement or
simple random sampling. With this method of sampling our 10 card sample will have no
duplicate cards.
Sampling with replacement
Now suppose we draw 10 cards at random from the deck, but after each draw we put the
card back in the deck and shuffle the cards. This is called sampling with replacement. With
this method, the 10 card sample might have duplicates. It’s even possible that we would
draw the 6 of hearts all 10 times.
Think: What’s the probability of drawing the 6 of hearts 10 times in a row?
Example 2. We can view rolling an 8-sided die repeatedly as sampling with replacement
from the set {1,2,3,4,5,6,7,8}. Since each number is equally likely, we say we are sampling
uniformly from the data.
Note. In practice if we take a small sample from a very large set then it doesn’t matter
whether we sample with or without replacement. For example, if we randomly sample 400
out of 300 million people in the U.S., then it is so unlikely that the same person will be
picked twice that there is no real difference between sampling with or without replacement.
4 The empirical distribution of data
The empirical distribution of data is simply the distribution that you see in the data. Let’s
illustrate this with an example.
Example 3. Suppose we roll an 8-sided die 10 times and get the following data, written
in increasing order:
1, 1, 2, 3, 3, 3, 3, 4, 7, 7.
Imagine writing these values on 10 slips of paper, putting them in a hat and drawing one
at random. Then, for example, the probability of drawing a 3 is 4/10 and the probability
of drawing a 4 is 1/10. The full empirical distribution can be put in a probability table
value 𝑥 1 2 3 4 7
𝑝(𝑥) 2/10 1/10 4/10 1/10 2/10
Notation. If we label the true distribution the data is drawn from as 𝐹, then we’ll label
18.05 Class 24, Bootstrap confidence intervals, Spring 2022 3
the empirical distribution of the data as 𝐹∗. If we have enough data then the law of large
numbers tells us that 𝐹∗ should be a good approximation of 𝐹.
Example 4. In the dice example just above, the true and empirical distributions are:
value 𝑥 1 2 3 4 5 6 7 8
true 𝑝(𝑥) 1/8 1/8 1/8 1/8 1/8 1/8 1/8 1/8
empirical 𝑝(𝑥) 2/10 1/10 4/10 1/10 0 0 2/10 0
The true distribution 𝐹 and the empirical distribution 𝐹∗ of the 8-sided die.
Because 𝐹∗ is derived strictly from data we call it the empirical distribution of the data.
We will also call it the resampling distribution. Notice that we always know 𝐹∗ explicitly.
In particular the expected value of 𝐹∗ is just the sample mean 𝑥.
5 Resampling
The empirical (or nonparametric) bootstrap proceeds by resampling from the data. We
continue the dice example above.
Example 5. Suppose we have 10 data points, given in increasing order:
1, 1, 2, 3, 3, 3, 3, 4, 7, 7
Weviewthisasasampletakenfromsomeunderlyingdistribution. Toresampleistosample
with replacement from the empirical distribution, e.g. put these 10 numbers in a hat and
draw one at random. Then put the number back in the hat and draw again. You draw as
many numbers as the desired size of the resample.
Togetusalittleclosertoimplementingthisonacomputerwerephrasethisinthefollowing
way. Label the 10 data points 𝑥 , 𝑥 ,…, 𝑥 . To resample is to draw a number 𝑗 from the
1 2 10
uniform distribution on {1,2,…,10} and take 𝑥 as our resampled value. In this case we
𝑗
could do so by rolling a 10-sided die. For example, if we roll a 6 then our resampled value
is 𝑥 = 3, the 6th element in our list.
6
If we want a resampled data set of size 5, then we roll the 10-sided die 5 times and choose
the corresponding elements from the list of data. If the 5 rolls are
5, 3, 6, 6, 1
then the resample is
3, 2, 3, 3, 1.
Notes: 1. Because we are sampling with replacement, the same data point can appear
multiple times when we resample.
2. Also because we are sampling with replacement, we can have a resample data set of any
size we want, e.g. we could resample 1000 times.
Of course, in practice one uses a software package like R to do the resampling.
18.05 Class 24, Bootstrap confidence intervals, Spring 2022 4
5.1 Star notation
If we have sample data of size 𝑛
𝑥 ,𝑥 ,…,𝑥
1 2 𝑛
then we denote a resample of size 𝑚 by adding a star to the symbols
𝑥∗,𝑥∗,…,𝑥∗
1 2 𝑚
Similarly,justas𝑥isthemeanoftheoriginaldata,wewrite𝑥∗ forthemeanoftheresampled
data.
6 The empirical bootstrap
Suppose we have 𝑛 data points
𝑥 ,𝑥 ,…,𝑥
1 2 𝑛
drawn from a distribution 𝐹. An empirical bootstrap sample (or nonparametric bootstrap
sample) is a resample of the same size 𝑛:
𝑥∗,𝑥∗,…,𝑥∗.
1 2 𝑛
You should think of the latter as a sample of size 𝑛 drawn from the empirical distribution
𝐹∗. For any statistic 𝑣 computed from the original sample data, we can define a bootstrap
statistic 𝑣∗. They both use the same formula but 𝑣∗ is computed using the resampled data.
With this notation we can state the bootstrap principle.
6.1 The bootstrap principle
The bootstrap setup is as follows:
1. 𝑥 ,𝑥 ,…,𝑥 is a data sample drawn from a distribution 𝐹.
1 2 𝑛
2. 𝑢 is a statistic computed from the sample.
3. 𝐹∗ is the empirical distribution of the data (the resampling distribution).
4. 𝑥∗,𝑥∗,…,𝑥∗ is a resample of the data of the same size as the original sample
1 2 𝑛
5. 𝑢∗ is the statistic computed from the resample.
Then the bootstrap principle says that
1. 𝐹∗ is approximately equal to 𝐹.
2. The statistic 𝑢 is approximated by 𝑢∗.
3. The variation of 𝑢 is approximated by the variation of 𝑢∗.
Our real interest is in point 3: we can approximate the variation of 𝑢 by that of 𝑢∗. It turns
out that, in practice, the bootstrap gives a reasonable approximation of the variation. We
will exploit this to estimate the size of confidence intervals.
6.2 Why the resample is the same size as the original sample
Thisisstraightforward: thevariationofthestatistic𝑢willdependonthesizeofthesample.
If we want to approximate this variation we need to use resamples of the same size.
18.05 Class 24, Bootstrap confidence intervals, Spring 2022 5
7 The empirical bootstrap confidence interval
Herewewillshowtwomethodsofcomputinganempiricalconfidenceinterval: thepercentile
bootstrap confidence interval in part (c) below and the basic bootstrap confidence interval
in part (d).
A search of the internet credits these names to Efron. Below, we will briefly discuss the
merits of each. The basic confidence interval is also called the reverse percentile confidence
interval.
We will illustrate both methods with a ‘toy’ example using the same data.
Example 6. Toy example. We start with a made-up set of data that is small enough to
show each step explicitly. The sample data is
30, 37, 36, 43, 42, 43, 43, 46, 41, 42
(a) Use the data to give a point estimate of the mean of the underlying distribution.
(b) Resample this to get 20 bootstrap samples.
(c) Use the bootstrap samples to find the 80% bootstrap percentile confidence interval for
the mean.
(d) Use the bootstrap samples to find the 80% bootstrap basic confidence interval for the
mean.
Note: R code for this example is shown in the section ’R annotated scripts’ below. The
code is also implemented in the R script, class24-empiricalbootstrap.r which is posted
with our other R code.
Solution: (a) The sample mean is 𝑥 = 40.3, this is our point estimate.
(b) Our original sample contains 10 points. We used R to generate 20 bootstrap samples,
each of size 10. Each of the 20 columns in the following array is one bootstrap sample. The
values under the line are the means of the columns
36 36 42 42 41 42 42 43 42 36 43 42 42 43 43 43 36 43 36 46
43 37 36 43 43 41 36 41 46 30 43 46 42 30 43 43 41 41 37 43
43 43 43 42 46 42 42 43 43 43 36 43 42 30 36 43 42 41 41 37
42 43 37 37 43 36 43 43 43 41 42 42 37 43 36 42 46 43 43 42
36 46 36 41 43 30 43 42 46 46 43 37 46 42 46 43 41 43 41 36
41 42 43 43 46 30 36 41 36 46 36 30 42 43 42 37 42 41 37 43
42 46 30 46 30 43 42 41 46 42 37 46 43 43 37 43 30 43 46 37
43 42 43 37 42 43 46 43 37 42 42 37 36 43 46 30 43 46 46 41
43 43 41 46 46 43 30 46 36 41 42 42 36 42 37 36 46 43 42 43
30 46 43 42 43 42 41 42 37 43 43 43 43 43 41 36 43 42 43 46
39.9 42.4 39.4 41.9 42.3 39.2 40.1 42.5 41.2 41.0 40.7 40.8 40.9 40.2 40.7 39.6 41.0 42.6 41.2 41.4
(c) For the percentile method, we first compute 𝑥∗ from each of our bootstrap samples.
Here they are, sorted in increasing order.
39.2 39.4 39.6 39.9 40.1 40.2 40.7 40.7 40.8 40.9 41.0 41.0 41.2 41.2 41.4 41.9
42.3 42.4 42.5 42.6
The percentile method says to use the distribution of 𝑥∗ as an approximation to the dis-
tribution of 𝑥. The 80% confidence interval stretches from the 10th to the 90th percentile.
18.05 Class 24, Bootstrap confidence intervals, Spring 2022 6
Since we have 20 bootstrap means, these are given by the 2nd and 18th elements in our list.
Therefore the boostrap 80% percentile confidence interval is [39.4, 42.4].
To make the example readable, we only computed 20 bootstrap means. The beautiful key
to the bootstrap is, that since 𝑥∗ is computed by resampling the original data, we can have
a computer simulate 𝑥∗ as many times as we’d like. Hence, by the law of large numbers, we
can estimate the distribution of 𝑥∗ with high precision.
Note: In our R code we use the quantile function to find the percentile values. This is easier
than figuring out the index. It also is a little more sophisticated in finding the quantiles for
a discrete set of values.
(d) The basic method is quite similar to the percentile method. The difference is that uses
an alegebraic ‘pivot’ analogous to the pivot used in finding 𝑧 or 𝑡 confidence intervals. As
in Example 1, to make the confidence interval we want to know how much the distribution
of 𝑥 varies around 𝜇. That is, we’d like to know the distribution of
𝛿 = 𝑥−𝜇.
Ifweknewthisdistribution, thenwecouldusethesamealgebrawesawwhenpivotingfrom
non-rejection regions to confidence intervals. That is, we could find 𝛿 and 𝛿 , the 0.1
0.1 0.9
and 0.9 critical values of 𝛿. Then we would have
𝑃(𝛿 ≤ 𝑥−𝜇 ≤ 𝛿 |𝜇) = 0.8 ⇔ 𝑃(𝑥−𝛿 ≥ 𝜇 ≥ 𝑥−𝛿 |𝜇) = 0.8
0.9 0.1 0.9 0.1
which gives an 80% confidence interval of
[𝑥−𝛿 , 𝑥−𝛿 ].
0.1 0.9
(Asalwayswithconfidenceintervals,wehastentopointoutthattheprobabilitiescomputed
above are probabilities concerning the statistic 𝑥 given that the true mean is 𝜇.)
The bootstrap principle offers a practical approach to estimating the distribution of 𝛿 =
𝑥−𝜇. It says that we can approximate it by the distribution of
𝛿∗ = 𝑥∗−𝑥
where 𝑥∗ is the mean of an empirical bootstrap sample.
Here is the beautiful key: since 𝛿∗ is computed by resampling the original data, we can have
a computer simulate 𝛿∗ as many times as we’d like. Hence, by the law of large numbers, we
can estimate the distribution of 𝛿∗ with high precision.
Next we compute 𝛿∗ = 𝑥∗ −𝑥 for each bootstrap sample (i.e. each column) and sort them
from smallest to biggest:
-1.1 -0.9 -0.7 -0.4 -0.2 -0.1 0.4 0.4 0.5 0.6 0.7 0.7 0.9 0.9 1.1 1.6 2.0 2.1 2.2 2.3
We will approximate the critical values 𝛿 and 𝛿 by 𝛿∗ and 𝛿∗ . Since 𝛿∗ is at the
0.1 0.9 0.1 0.9 0.1
90th percentile we choose the 18th element in the list, i.e. 2.1. Likewise, since 𝛿∗ is at the
0.9
10th percentile we choose the 2nd element in the list, i.e. -0.9.
Therefore our bootstrap 80% basic confidence interval for 𝜇 is
[𝑥−𝛿∗ , 𝑥−𝛿∗ ] = [40.3−2.1, 40.3+0.9] = [38.2, 41.2]
0.1 0.9
In this example we only generated 20 bootstrap samples so they would fit on the page.
Using R, we would generate 10000 or more bootstrap samples in order to obtain a very
accurate estimate of 𝛿∗ and 𝛿∗ .
0.1 0.9
18.05 Class 24, Bootstrap confidence intervals, Spring 2022 7
8 Justification for the bootstrap principle
The bootstrap is remarkable because resampling gives us a decent estimate on how the
point estimate might vary. We can only give you a ‘hand-waving’ explanation of this, but
it’s worth a try. The bootstrap is based roughly on the law of large numbers, which says,
in short, that with enough data the empirical distribution will be a good approximation of
the true distribution. Visually it says that the histogram of the data should approximate
the density of the true distribution.
First let’s note what resampling cannot do for us: it cannot improve our point estimate.
For example, if we estimate the mean 𝜇 by 𝑥 then in the bootstrap we would compute 𝑥∗
for many resamples of the data. If we took the average of all the 𝑥∗ we would expect it to
be very close to 𝑥. This wouldn’t tell us anything new about the true value of 𝜇.
Even with a fair amount of data the match between the true and empirical distributions is
not perfect, so there will be error in our estimates for the mean (or any other value). But
the amount of variation in the estimates is much less sensitive to differences between the
truedensityandthe data histogram: as long asthey arereasonably close, the empirical and
true distributions will exhibit the similar amounts of variation. So, in general the bootstrap
principle is more robust when approximating the distribution of relative variation than
when approximating absolute distributions.
What we have in mind is the scenario of our examples. The distribution (over different sets
𝑥 of experimental data) of 𝑥 is ‘centered’ at 𝜇 and the distribution (over different bootstrap
samples 𝑥∗ of 𝑥) of 𝑥∗ is centered at 𝑥. If there is a significant separation between 𝑥 and 𝜇
then these two distributions will also differ significantly. On the other hand the distribution
of 𝛿 = 𝑥 − 𝜇 describes the variation of 𝑥 about its center. Likewise the distribution of
𝛿∗ = 𝑥∗ −𝑥 describes the variation of 𝑥∗ about its center. So even if the centers are quite
different the two variations about the centers can be approximately equal.
The figure below illustrates how the empirical distribution approximates the true distribu-
tion. To make the figure we generate 100 random values from a chi-square distribution with
3 degrees of freedom. The figure shows the pdf of the true distribution as a blue line and a
histogram of the empirical distribution in orange.
0 5 10 15
02.0
01.0
00.0
The true and empirical distributions are approximately equal.
18.05 Class 24, Bootstrap confidence intervals, Spring 2022 8
9 Other statistics
So far in this class we’ve avoided confidence intervals for the median and other statistics
because their sample distributions are hard to describe theoretically. The bootstrap has no
such problem. In fact, to handle the median all we have to do is change ‘mean’ to ‘median’
in the R code from Example 6.
Example 7. Old Faithful: confidence intervals for the median
Old Faithful is a geyser in Yellowstone National Park in Wyoming:
https://en.wikipedia.org/wiki/Old_Faithful
Thereisapubliclyavailabledatasetwhichgivesthedurationsof272consecutiveeruptions.
Here is a histogram of the data.
Question: Estimate the median length of an eruption and give a 90% percentile bootstrap
confidence interval for the median.
Solution: The full answer to this question is in the R file oldfaithful.r and the Old
Faithful data set. Both are posted on the class R code page. (Look under ‘Other R code’
for the old faithful script and data.)
Note: the code in oldfaithful.r assumes that the data oldfaithful-data.txt is in the
current working directory.
Let’s walk through a summary of the steps needed to answer the question.
1. Data: 𝑥 ,…,𝑥
1 272
2. Data median: 𝑥 = 240
median
3. Find the median 𝑥∗ of a bootstrap sample 𝑥∗,…,𝑥∗ . Repeat 1000 times.
median 1 272
Put these 1000 values in order and pick out the 0.05 and 0.95 quantiles , i.e. the 50th and
950th biggest values. (In R we do this using the quantile() function) Call these 𝑚∗ and
0.05
𝑚∗ .
0.95
5. The 90% percentile confidence interval for the medium is [𝑚∗ , 𝑚∗ ].
0.05 0.95
Thebootstrap90%CIwefoundfortheOldFaithfuldatawas[230,246]. Sinceweused1000
bootstrap samples a new simulation starting from the same sample data should produce a
similar interval. If in Step 3 we increase the number of bootstrap samples to 10000, then
18.05 Class 24, Bootstrap confidence intervals, Spring 2022 9
the intervals produced by simulation would tend to be even more similar to each other.
One common strategy is to increase the number of bootstrap samples until the resulting
simulations produce intervals that vary less than some acceptable level.
Example 8. Using the Old Faithful data, estimate 𝑃(|𝑥−𝜇| > 5|𝜇).
Solution: We proceed exactly as in the previous example in finding a basic bootstrap
confidence interval, except we use the mean instead of the median.
1. Data: 𝑥 ,…,𝑥
1 272
2. Data mean: 𝑥 = 209.27
3. Find the mean 𝑥∗ of 1000 empirical bootstrap samples: 𝑥∗,…,𝑥∗ .
1 272
4. Compute the bootstrap differences
𝛿∗ = 𝑥∗−𝑥
5. The bootstrap principle says that we can use the distribution of 𝛿∗ as an approximation
for the distribution 𝛿 = 𝑥−𝜇. Thus,
𝑃(|𝑥−𝜇| > 5|𝜇) = 𝑃(|𝛿| > 5|𝜇) ≈ 𝑃(|𝛿∗| > 5)
One bootstrap simulation for the Old Faithful data gave 0.230 for this probability.
10 Parametric bootstrap
Before getting started, we note that we only show the simplest algorithm for parametric
bootstrap confidence intervals. In practice, more sophisticated algorithms are used. Since
the bootsrap principle is the same in all cases, we feel it is worth encountering the simple
algorithm in 18.05.
The examples in the previous sections all used the empirical bootstrap, which makes no as-
sumptions at all about the underlying distribution and draws bootstrap samples by resam-
plingthedata. Inthissectionwewilllookattheparametricbootstrap. Themaindifference
between the parametric and empirical bootstrap is the source of the bootstrap sample. For
the parametric bootstrap, we generate the bootstrap sample from a parametrized distribu-
tion.
Another difference, is that, for the parametric bootstrap, we will use basic bootstrap con-
fidence intervals. It’s hard to find a definitive answer on whether the percentile or basic
interval is better in this case. As we noted above, the real answer seems to be that, in
practice, parametric bootstrap confidence intervals are computed with more sophisticated
algorithms.
Here are the elements of using the parametric bootstrap to estimate a confidence interval
for a parameter.
0. Data: 𝑥 ,…,𝑥 drawn from a distribution 𝐹(𝜃) with unknown parameter 𝜃.
1 𝑛
1. A statistic 𝜃̂that estimates 𝜃.
2. Our bootstrap samples are drawn from 𝐹(𝜃)̂ .
18.05 Class 24, Bootstrap confidence intervals, Spring 2022 10
3. For each bootstrap sample
𝑥∗,…,𝑥∗
1 𝑛
we compute 𝜃∗̂ and the bootstrap difference 𝛿∗ = 𝜃∗̂ −𝜃.̂
4. The bootstrap principle says that the distribution of 𝛿∗ approximates the distribution of
𝛿 = 𝜃̂−𝜃.
5. Use the bootstrap differences to make a bootstrap confidence interval for 𝜃.
Example 9. Suppose the data 𝑥 ,…,𝑥 is drawn from an exp(𝜆) distribution. Assume
1 300
also that the data mean 𝑥 = 2. Estimate 𝜆 and give a 95% parametric bootstrap confidence
interval for 𝜆.
Solution: This is implemented in the R script class24-parametricbootstrap.r which is
posted with our other R code.
It’s will be easiest to explain the solution using commented code.
# Parametric bootstrap
# Given 300 data points with mean 2.
# Assume the data is exp(lambda)
# PROBLEM: Compute a 95% parametric bootstrap confidence interval for lambda
# We are given the number of data points and mean
n = 300
xbar = 2
# The MLE for lambda is 1/xbar
lambda_hat = 1.0/xbar
# Generate the bootstrap samples
# Each column is one bootstrap sample (of 300 resampled values)
n_boot = 1000
# Here's the key difference with the empirical bootstrap:
# We draw the bootstrap sample from Exponential(lambda_hat).
x = rexp(n*n_boot, lambda_hat)
bootstrap_sample = matrix(x, nrow=n, ncol=n_boot)
# Compute the bootstrap lambda_star
lambda_star = 1.0/colMeans(bootstrap_sample)
# Compute the differences
delta_star = lambda_star - lambda_hat
# Find the 0.05 and 0.95 quantile for delta_star
d = quantile(delta_star, c(0.05,0.95))
# Calculate the 95% confidence interval for lambda.
ci = lambda_hat - c(d[2], d[1])
# This line of code is just one way to format the output text.
# sprintf is an old C function for doing this. R has many other
# ways to do the same thing.
s = sprintf("Confidence interval for lambda: [%.3f, %.3f]", ci[1], ci[2])
18.05 Class 24, Bootstrap confidence intervals, Spring 2022 11
cat(s)
11 Building a better bootstrap
The first thing to say, is that we have just scratched the surface of bootstrap techniques.
There are more sophisticated methods that correct for bias in the original sample or for
skewness in the underlying distribution. There are also methods for when the original
sample size is small.
For the nonparametric bootstrap, there are different opinions about which of the basic and
percentile methods gives the most accurate results. What is clear is that, if the empirical
distribution is symmetric, then the basic and percentile confidence intervals are equivalent.
If the distribution is skewed then the two intervals are skewed in opposite directions.
Hesterbergin(https://www.tandfonline.com/doi/full/10.1080/00031305.2015.1089789)
is fairly convincing that the percentile method performs better on skewed distributions.
On the other hand, Rice says of the percentile method, “Although this direct equation of
quantiles of the bootstrap sampling distribution with confidence limits may seem initially
appealing, it’s rationale is somewhat obscure.” 2
We’ll give Hesterberg the final word. He contributed several excellent responses to a dis-
cussion group. Unfortunately the link is no longer active, but here is one of his posts.
Skewness is a fact of life. So what do you do when there is skewness? A
bootstrap percentile interval is usually a good choice – much better than a
symmetric interval like 𝑡, that pretends there is no skewness. It is fine for a
beginning stats student, and for most applications in practice. Someone more
advanced (or using easy-to-use software) can use a BCa or bootstrap-t interval,
for better accuracy.
Bootstrapping the median is a different issue – for small samples the median
is quite sensitive to whether the population being sampled from is continuous
or discrete. So if the population is continuous, but you use the nonparametric
bootstrap that draws from a discrete distribution (the data), the bootstrap dis-
tribution won’t look like the true sampling distribution. Even so, the bootstrap
percentile interval is not bad in this case, close to the exact confidence interval
for the median (typically the same or one order statistic different).
12 R annotated transcripts
12.1 Using R to generate a empirical bootstrap confidence intervals
This code only generates 20 bootstrap samples. In real practice we would generate many
more bootstrap samples. It is making a bootstrap confidence interval for the mean. This
code is implemented in the R script class24-empiricalbootstrap.r which is posted with
our other R code.
2John Rice, Mathematical Statistics and Data Analysis, 2nd edition, p. 272.
18.05 Class 24, Bootstrap confidence intervals, Spring 2022 12
# Data for the example 6
x = c(30,37,36,43,42,43,43,46,41,42)
n = length(x)
# sample mean
xbar = mean(x)
n_boot = 20
# Generate 20 bootstrap samples, i.e. an n x 20 array of
# random resamples from x
tmp_data = sample(x, n*n_boot, replace=TRUE)
bootstrap_sample = matrix(tmp_data, nrow=n, ncol=n_boot)
# Compute the means 𝑥∗
xbar_star = colMeans(bootstrap_sample)
# Calculate the bounds for the 80% percentile confidence interval.
percentile_ci = quantile(xbar_star, c(0.1, 0.9))
cat('80% percentile confidence interval: ',percentile_ci, '\n')
# Compute 𝛿∗ for each bootstrap sample
delta_star = xbar_star - xbar
# Find the 0.1 and 0.9 quantiles for delta_star
d = quantile(delta_star, c(0.1, 0.9))
# Calculate the bounds for the 80% basic confidence interval.
# Note how pivoting reverses the order of d[1] and d[2]
basic_ci = xbar - c(d[2], d[1])
cat('80% basic confidence interval: ',basic_ci, '\n')
# ALTERNATIVE: the quantile() function is sophisticated about
# choosing a quantile between two data points. A less sophisticated
# approach is to pick the quantiles by sorting xbar_start and delta_star and
# choosing the index that corresponds to the desired quantiles.
# This is what we did in the text above. We show the code using this for the
percentile method below.
# Sort the results
sorted_xbar_star = sort(xbar_star)
# Find the 0.1 and 0.9 quantiles values of xbar_star
q1_alt = sorted_xbar_star[2]
q9_alt = sorted_xbar_star[18]
# Find and print the 80% percentile confidence interval for the mean
ci_alt = c(q1_alt, q9_alt)
cat('Alternative confidence interval: ',ci_alt, '\n')
Linear regression
Class 26, 18.05
Jeremy Orloff and Jonathan Bloom
1 Learning Goals
1. Be able to use the method of least squares to fit a line to bivariate data.
2. Be able to give a formula for the total squared error when fitting any type of curve to
data.
3. Be able to say the words homoscedasticity and heteroscedasticity.
2 Introduction
Suppose we have collected bivariate data (𝑥 ,𝑦 ), 𝑖 = 1,…,𝑛. The goal of linear regression
𝑖 𝑖
is to model the relationship between 𝑥 and 𝑦 by finding a function 𝑦 = 𝑓(𝑥) that is a close
fit to the data. The modeling assumptions we will use are that 𝑥 is not random and that
𝑖
𝑦 is a function of 𝑥 plus some random noise. With these assumptions 𝑥 is called the
𝑖 𝑖
independent or predictor variable and 𝑦 is called the dependent or response variable.
Here is a series of examples showing the results of linear regression. We will discuss the
details of how to do linear regression in the next section.
Example 1. The cost of a first class stamp in cents over time is given in the following list.
0.05 (1963) 0.06 (1968) 0.08 (1971) 0.10 (1974) 0.13 (1975) 0.15 (1978) 0.20 (1981)
0.22 (1985) 0.25 (1988) 0.29 (1991) 0.32 (1995) 0.33 (1999) 0.34 (2001) 0.37 (2002)
0.39 (2006) 0.41 (2007) 0.42 (2008) 0.44 (2009) 0.45 (2012) 0.46 (2013) 0.49 (2015)
0.49 (2017) 0.50 (2018) 0.55 (2019)
Using the R function lm we found the ‘least squares fit’ for a line to this data is
𝑦 = −0.21390+0.88203𝑥,
where 𝑥 is the number of years since 1960 and 𝑦 is in cents.
Using this result we ‘predict’ that in 2021 (𝑥 = 61) the cost of a stamp will be 53.6 cents
(since −0.21390+0.88203⋅61 = 53.6).
1
18.05 Class 26, Linear regression, Spring 2022 2
0 10 20 30 40 50 60
05
04
03
02
01
x
y
Stamp cost (cents) vs. time (years since 1960). Orange dot is predicted cost in 2021.
Note that none of the data points actually lie on the line. Rather this line has the ‘best fit’
with respect to all the data, with a small error for each data point.
(Note, the actual cost of a stamp dropped in January 2021 was 55 cents. See https:
//en.wikipedia.org/wiki/History_of_United_States_postage_rates)
Example 2. Suppose we have 𝑛 pairs of fathers and adult sons. Let 𝑥 and 𝑦 be the
𝑖 𝑖
heights of the 𝑖th father and son, respectively. The least squares line for this data could be
used to predict the adult height of a young boy from that of his father.
Example 3. We are not limited to best fit lines. For all positive 𝑑, the method of least
squares may be used to find a polynomial of degree 𝑑 with the ‘best fit’ to the data. Here’s
a figure showing the least squares fit of a parabola (𝑑 = 2).
Fitting a parabola, 𝑎𝑥2+𝑏𝑥+𝑐, to data
Example 4. In fact, we can use linear regression to fit many other types of curves to
bivariate data.
18.05 Class 26, Linear regression, Spring 2022 3
3 Fitting a line using least squares
Suppose we have data (𝑥 ,𝑦 ) as above. Our first goal is to find the line
𝑖 𝑖
𝑦 = 𝑎𝑥+𝑏
that ‘best fits’ the data. Our model says that each 𝑦 is predicted by 𝑥 up to some error 𝜖 :
𝑖 𝑖 𝑖
𝑦 = 𝑎𝑥 +𝑏+𝜖 .
𝑖 𝑖 𝑖
So
𝜖 = 𝑦 −𝑎𝑥 −𝑏.
𝑖 𝑖 𝑖
The method of least squares finds the values 𝑎̂ and 𝑏̂ of 𝑎 and 𝑏 that minimize the sum of
the squared errors:
𝑆(𝑎,𝑏) = ∑𝜖2 = ∑(𝑦 −𝑎𝑥 −𝑏)2.
𝑖 𝑖 𝑖
𝑖
Using calculus or linear algebra (details in the appendix), we find
𝑠
𝑎̂= 𝑥𝑦 𝑏̂ = 𝑦̄−𝑎̂𝑥̄ (1)
𝑠
𝑥𝑥
where
1 1 1 1
𝑥̄= ∑𝑥 , 𝑦̄= ∑𝑦 , 𝑠 = ∑(𝑥 −𝑥)̄ 2, 𝑠 = ∑(𝑥 −𝑥)̄ (𝑦 −𝑦)̄ .
𝑛 𝑖 𝑛 𝑖 𝑥𝑥 (𝑛−1) 𝑖 𝑥𝑦 (𝑛−1) 𝑖 𝑖
Here 𝑥̄ is the sample mean of 𝑥, 𝑦̄is the sample mean of 𝑦, 𝑠 is the sample variance of 𝑥,
𝑥𝑥
and 𝑠 is the sample covariance of 𝑥 and 𝑦.
𝑥𝑦
Example 5. Use least squares to fit a line to the following data: (0,1), (2,1), (3,4).
Solution: In our case, (𝑥 ,𝑦 ) = (0,1), (𝑥 ,𝑦 ) = (2,1) and (𝑥 ,𝑦 ) = (3,4). So
1 1 2 2 3 3
5 7
𝑥̄= , 𝑦̄= 2, 𝑠 = , 𝑠 = 2
3 𝑥𝑥 3 𝑥𝑦
Using the above formulas we get
6 4
𝑎̂= , 𝑏̂ = .
7 7
6 4
So the least squares line has equation 𝑦 = 𝑥+ . This is shown as the orange line in the
7 7
following figure. We will discuss the blue parabola soon.
𝑦
4
1
𝑥
1 2 3
Least squares fit of a line (orange) and a parabola (blue)
18.05 Class 26, Linear regression, Spring 2022 4
Simple linear regression: It’s a little confusing, but the word linear in ‘linear regression’
does not refer to fitting a line. We will explain its meaning below. However, the most
common curve to fit is a line. When we fit a line to bivariate data it is called simple linear
regression.
3.1 Residuals
For a line the model is
𝑦 = 𝑎𝑥̂ +𝑏̂+𝜖 .
𝑖 𝑖
Wethinkof𝑎𝑥̂ +𝑏̂aspredictingorexplaining𝑦 . Theleft-overterm𝜖 iscalledtheresidual,
𝑖 𝑖 𝑖
whichwethink of as random noise or measurementerror. A useful visual check of the linear
regression model is to plot the residuals. The data points should hover near the regression
line. The residuals should look about the same across the range of 𝑥.
l
l l
l ll l
ll ll l l ll l l l ll lllll llll l l ll l l l l l lll l l l l l l l ll l l lll l l l l ll l l l l ll ll l l l l l lll l l ll l
l
ll
lll
l
l ll
l
l
l
l
l
ll l
l
0 2 4 6 8 10
02
51
01 5
0
x
y
l
l
l l
l l l l l l l l ll l l l l ll l l l l l l l l l l l l lll l l l lll l l l ll ll ll l l ll l l ll l l l l l ll l ll l l l l l ll l l l l l l l l l l l l l l l lll l ll l
l l l l
0 2 4 6 8 10
4
3
2 1 0 1− 2−
3−
x
e
Data with regression line (left) and residuals (right). Note the homoscedasticity.
3.2 Homoscedasticity
An important assumption of the linear regression model is that the residuals 𝜖 have the
𝑖
same variance for all 𝑖. This is called homoscedasticity. You can see this is the case for
both figures above. The data hovers in the band of fixed width around the regression line
and at every 𝑥 the residuals have about the same vertical spread.
Below is a figure showing heteroscedastic data. The vertical spread of the data increases as
𝑥 increases. Before using least squares on this data we would need to transform the data
to be homoscedastic.
18.05 Class 26, Linear regression, Spring 2022 5
l
l
ll
l
l l
l
l l l l l l l l ll l l ll l ll l l l l l l ll ll ll ll l l l l ll l l l l l l l l l l l l l l l l l l ll l l ll l l l l ll l ll l l ll lll
l l l ll lll ll l lllllll
ll l lll lll ll ll l l l l l ll ll l l l ll lll l l l l l l ll l l
0 2 4 6 8 10
02
51 01
5
0
x
y
Heteroscedastic Data
4 Linear regression for fitting polynomials
When we fit a line to data it is called simple linear regression. We can also use linear
regression to fit polynomials to data. The use of the word linear in both cases may seem
confusing. This is because the word ‘linear’ in linear regression does not refer to fitting a
line. Rather it refers to the linear algebraic equations for the unknown parameters.
Example 6. Take the same data as in Example 5 and use least squares to find the best
fitting parabola to the data.
Solution: A parabola has the formula 𝑦 = 𝑎𝑥2+𝑏𝑥+𝑐. The squared error is
𝑆(𝑎,𝑏,𝑐) = ∑(𝑦 −(𝑎𝑥2+𝑏𝑥 +𝑐))2.
𝑖 𝑖 𝑖
After substituting the given values for each 𝑥 and 𝑦 , we can use calculus to find the triple
𝑖 𝑖
(𝑎,𝑏,𝑐) that minimizes 𝑆. With this data, we find that the least squares parabola has
equation
𝑦 = 𝑥2−2𝑥+1.
Note that for 3 points the quadratic fit is perfect.
𝑦
4
1
𝑥
1 2 3
Least squares fit of a line (orange) and a parabola (blue)
Example 7. The pairs (𝑥 ,𝑦 ) may give the age and vocabulary size of a 𝑛 children. Since
𝑖 𝑖
we expect that young children acquire new words at an accelerating pace, we might guess
that a higher order polynomial would best fit the data.
18.05 Class 26, Linear regression, Spring 2022 6
Example 8. (Transforming the data) Sometimes it is necessary to transform the data
before using linear regression. For example, let’s suppose the relationship is exponential,
i.e. 𝑦 = 𝑐𝑒𝑎𝑥. Then
ln(𝑦) = 𝑎𝑥+ln(𝑐).
So we can use simple linear regression on the data (𝑥 , ln(𝑦 )) to obtain a model
𝑖 𝑖
ln(𝑦) = 𝑎𝑥̂ +𝑏̂
and then exponentiate to obtain the exponential model
𝑦 = 𝑒𝑏̂ 𝑒𝑎̂𝑥.
4.1 Overfitting
Youcanalwaysachieveabetterfitbyusingahigherorderpolynomial. Forinstance,given6
datapoints(withdistinct𝑥 )onecanalwaysfindafifthorderpolynomialthatgoesthrough
𝑖
all of them. This can result in what’s called overfitting. That is, fitting the noise as well
as the true relationship between 𝑥 and 𝑦. An overfit model will fit the original data better
but perform less well on predicting 𝑦 for new values of 𝑥. Indeed, a primary challenge of
statistical modeling is balancing model fit against model complexity.
Example 9. In the plot below, we fit polynomials of degree 1, 2, and 9 to bivariate data
consisting of 10 data points. The degree 2 model (maroon) gives a significantly better fit
than the degree 1 model (blue). The degree 10 model (orange) gives fits the data exactly,
but at a glance we would guess it is overfit. That is, we don’t expect it to do a good job
fitting the next data point we see.
In fact, we generated this data using a quadratic model, so the degree 2 model will tend to
perform best fitting new data points.
0 2 4 6 8 10
01
5
0
x
y
4.2 R function lm
As you would expect we don’t actually do linear regression by hand. Computationally,
linear regression reduces to solving simultaneous equations, i.e. to matrix calculations. The
R function lm can be used to fit any order polynomial to data. (lm stands for linear model).
We will explore this in the next studio class. In fact lm can fit many types of functions
besides polynomials, as you can explore using R help or google.
18.05 Class 26, Linear regression, Spring 2022 7
5 Multiple linear regression
Dataisnotalwaysbivariate. Itcanbetrivariateorevenofsomehigherdimension. Suppose
we have data in the form of tuples
(𝑦 , 𝑥 , 𝑥 , … 𝑥 )
𝑖 1,𝑖 2,𝑖 𝑚,𝑖
We can analyze this in a manner very similar to linear regression on bivariate data. That
is, we can use least squares to fit the model
𝑦 = 𝛽 +𝛽 𝑥 +𝛽 𝑥 +…+𝛽 𝑥 .
0 1 1 2 2 𝑚 𝑚
Here each 𝑥 is a predictor variable and 𝑦 is the response variable. For example, we might
𝑗
be interested in how a fish population varies with measured levels of several pollutants, or
we might want to predict the adult height of a son based on the height of the mother and
the height of the father.
We don’t have time in 18.05 to study multiple linear regression, but we wanted you to see
the name.
6 Least squares as a statistical model
The linear regression model for fitting a line says that the value 𝑦 in the pair (𝑥 ,𝑦 ) is
𝑖 𝑖 𝑖
drawn from a random variable
𝑌 = 𝑎𝑥 +𝑏+𝜀
𝑖 𝑖 𝑖
where the ‘error’ terms 𝜀 are independent random variables with mean 0 and standard
𝑖
deviation 𝜎. The standard assumption is that the 𝜀 are i.i.d. with distribution 𝑁(0,𝜎2).
𝑖
So, the mean of 𝑌 is given by:
𝑖
𝐸[𝑌 ] = 𝑎𝑥 +𝑏+𝐸[𝜀 ] = 𝑎𝑥 +𝑏.
𝑖 𝑖 𝑖 𝑖
Fromthisperspective,theleastsquaresmethodchoosesthevaluesof𝑎and𝑏whichminimize
the sample variance about the line.
In fact, under the assumption that 𝜀 ∼ 𝑁(0,𝜎2), the least square estimate (𝑎,̂ 𝑏̂) coincides
𝑖
with the maximum likelihood estimate for the parameters (𝑎,𝑏); that is, among all possible
coeﬀicients, (𝑎,̂ 𝑏̂) are the ones that make the observed data most probable.
7 Regression to the mean
The reason for the term ‘regression’ is that the predicted response variable 𝑦 will tend to
be ‘closer’ to (i.e., regress to) its mean than the predictor variable 𝑥 is to its mean. Here
closer is in quotes because we have to control for the scale (i.e. standard deviation) of each
variable. The way we control for scale is to first standardize each variable.
𝑥 −𝑥̄ 𝑦 −𝑦̄
𝑢 = √ 𝑖 , 𝑣 = √ 𝑖 .
𝑖 𝑠 𝑖 𝑠
𝑥𝑥 𝑦𝑦
18.05 Class 26, Linear regression, Spring 2022 8
Standardization changes the mean to 0 and variance to 1:
𝑢̄ = 𝑣̄= 0, 𝑠 = 𝑠 = 1.
𝑢𝑢 𝑣𝑣
The algebraic properties of covariance show
𝑠
𝑥𝑦
𝑠 = √ = 𝜌,
𝑢𝑣 𝑠 𝑠
𝑥𝑥 𝑦𝑦
the correlation coeﬀicient. Thus the least squares fit to 𝑣 = 𝑎𝑢+𝑏 has
𝑠
𝑎̂= 𝑢𝑣 = 𝜌 and 𝑏̂ = 𝑣̄−𝑎𝑢̂ ̄ = 0.
𝑠
𝑢𝑢
So the least squares line is 𝑣 = 𝜌𝑢. Since 𝜌 is the correlation coeﬀicient, it is between -1 and
1. Let’s assume it is positive and less than 1 (i.e., 𝑥 and 𝑦 are positively but not perfectly
correlated). Then the formula 𝑣 = 𝜌𝑢 means that if 𝑢 is positive then the predicted value
of 𝑣 is less than 𝑢. That is, 𝑣 is closer to 0 than 𝑢. Equivalently,
𝑦−𝑦̄ 𝑥−𝑥̄
√ < √
𝑠 𝑠
𝑦𝑦 𝑥𝑥
i.e., 𝑦 regresses to 𝑦.̄ Notice how the standardization takes care of controlling the scale.
Consider the extreme case of 0 correlation between 𝑥 and 𝑦. Then, no matter what the 𝑥
value, the predicted value of 𝑦 is always 𝑦.̄ That is, 𝑦 has regressed all the way to its mean.
Note also that the regression line always goes through the point (𝑥,̄ 𝑦)̄ .
Example 10. Regression to the mean is important in longitudinal studies. Rice (Math-
ematical Statistics and Data Analysis) gives the following example. Suppose children are
given an IQ test at age 4 and another at age 5 we expect the results will be positively
correlated. The above analysis says that, on average, those kids who do poorly on the first
test will tend to show improvement (i.e. regress to the mean) on the second test. Thus, a
useless intervention might be misinterpreted as useful since it seems to improve scores.
Example 11. Another example with practical consequences is reward and punishment.
Imagine a school where high performance on an exam is rewarded and low performance is
punished. Regression to the mean tells us that (on average) the high performing students
will do slightly worse on the next exam and the low performing students will do slightly
better. An unsophisticated view of the data will make it seem that punishment improved
performance and reward actually hurt performance. There are real consequences if those in
authority act on this idea.
8 Appendix
We collect in this appendix a few things you might find interesting. You will not be asked
to know these things for exams.
18.05 Class 26, Linear regression, Spring 2022 9
8.1 Proof of the formula for least square fit of a line
The most straightforward proof is to use calculus. The sum of the squared errors is
𝑛
𝑆(𝑏,𝑎) = ∑(𝑦 −𝑎𝑥 −𝑏)2.
𝑖 𝑖
𝑖=1
Taking partial derivatives (and remembering that 𝑥 and 𝑦 are the data, hence constant)
𝑖 𝑖
𝜕𝑆 𝑛
= ∑−2(𝑦 −𝑎𝑥 −𝑏) = 0
𝜕𝑏 𝑖 𝑖
𝑖=1
𝜕𝑆 𝑛
= ∑−2𝑥 (𝑦 −𝑎𝑥 −𝑏) = 0
𝜕𝑎 𝑖 𝑖 𝑖
𝑖=1
Summing this up we get two linear equations in the unknowns 𝑏 and 𝑎:
(∑𝑥 )𝑎+𝑛𝑏 = ∑𝑦
𝑖 𝑖
(∑𝑥2)𝑎+(∑𝑥 )𝑏 = ∑𝑥 𝑦
𝑖 𝑖 𝑖 𝑖
Solving for 𝑎 and 𝑏 gives the formulas in Equation (1).
A sneakier approach which avoids calculus is to standardize the data, find the best fit line,
and then unstandardize. We omit the details.
For a slew of applications across disciplines see:
https://en.wikipedia.org/wiki/Linear_regression#Applications_of_linear_regression
8.2 Measuring the fit
Once one computes the regression coeﬀicients, it is important to check how well the regres-
sion model fits the data (i.e., how closely the best fit line tracks the data). A common but
crude ‘goodness of fit’ measure is the coeﬀicient of determination, denoted 𝑅2. We’ll need
some notation to define it. The total sum of squares is given by:
TSS = ∑(𝑦 −𝑦)̄ 2.
𝑖
The residual sum of squares is given by the sum of the squares of the residuals. When
fitting a line, this is:
RSS = ∑(𝑦 −𝑎̂𝑥 −𝑏̂)2.
𝑖 𝑖
The RSS is the “unexplained” portion of the total sum of squares, i.e. unexplained by the
regression equation. The difference TSS−RSS is the “explained” portion of the total sum
of squares. The coeﬀicient of determination 𝑅2 is the ratio of the “explained” portion to
the total sum of squares:
TSS−RSS
𝑅2 = .
TSS
In other words, 𝑅2 measures the proportion of the variability of the data that is accounted
for by the regression model. A value close to 1 indicates a good fit, while a value close to 0
18.05 Class 26, Linear regression, Spring 2022 10
indicates a poor fit. In the case of simple linear regression, 𝑅2 is simply the square of the
correlation coeﬀicient between the observed values 𝑦 and the predicted values 𝑎𝑥 +𝑏.
𝑖 𝑖
Example 12. In the overfitting example (9), the values of 𝑅2 are:
degree 𝑅2
1 0.3968
2 0.9455
9 1.0000
Notice the goodness of fit measure increases as 𝑛 increases. The fit is better, but the
model also becomes more complex, since it takes more coeﬀicients to describe higher order
polynomials.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
