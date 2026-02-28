# Openintro Chapter Distributions

---

3.1. DEFINING PROBABILITY 91
GUIDEDPRACTICE3.23
Suppose 5 people are selected at random.18
(a) What is the probability that all are right-handed?
(b) What is the probability that all are left-handed?
(c) What is the probability that not all of the people are right-handed?
Suppose the variables handedness and sex are independent, i.e. knowing someone’s sex pro-
vides no useful information about their handedness and vice-versa. Then we can compute whether
a randomly selected person is right-handed and female19 using the Multiplication Rule:
P(right-handed and female)=P(right-handed)×P(female)
=0.91×0.50=0.455
GUIDEDPRACTICE3.24
Three people are selected at random.20
(a) What is the probability that the first person is male and right-handed?
(b) What is the probability that the first two people are male and right-handed?.
(c) What is the probability that the third person is female and left-handed?
(d) What is the probability that the first two people are male and right-handed and the third
person is female and left-handed?
Sometimeswewonderifoneoutcomeprovidesusefulinformationaboutanotheroutcome. The
question we are asking is, are the occurrences of the two events independent? We say that two
events A and B are independent if they satisfy P(A and B)=P(A)×P(B).
EXAMPLE3.25
If we shuffle up a deck of cards and draw one, is the event that the card is a heart independent of
the event that the card is an ace?
Theprobabilitythecardisaheartis1/4andtheprobabilitythatitisanaceis1/13. Theprobability
the card is the ace of hearts is 1/52. We check whether P(A and B)=P(A)×P(B) is satisfied:
1 1 1
P(♡)×P(ace)= × = =P(♡ and ace)
4 13 52
Because the equation holds, the event that the card is a heart and the event that the card is an ace
are independent events.
18(a)TheabbreviationsRHandLHareusedforright-handedandleft-handed,respectively. Sinceeachareindepen-
dent,weapplytheMultiplicationRuleforindependentprocesses:
P(allfiveareRH)=P(first=RH,second=RH,...,fifth=RH)
=P(first=RH)×P(second=RH)×···×P(fifth=RH)
=0.91×0.91×0.91×0.91×0.91=0.624
(b)Usingthesamereasoningasin(a),0.09×0.09×0.09×0.09×0.09=0.0000059
(c)Usethecomplement,P(allfiveareRH),toanswerthisquestion:
P(notallRH)=1−P(allRH)=1−0.624=0.376
19TheactualproportionoftheU.S.populationthatisfemaleisabout50%,andsoweuse0.5fortheprobability
ofsamplingawoman. However,thisprobabilitydoesdifferinothercountries.
20Briefanswersare provided. (a)This canbewrittenin probability notation asP(arandomly selectedpersonis
maleandright-handed)=0.455. (b)0.207. (c)0.045. (d)0.0093.
92 CHAPTER 3. PROBABILITY
Exercises
3.1 Trueorfalse. Determine if the statements below are true or false, and explain your reasoning.
(a) If afair coinistossed many timesandthe lasteight tossesare all heads, thenthe chancethat thenext
toss will be heads is somewhat less than 50%.
(b) Drawing a face card (jack, queen, or king) and drawing a red card from a full deck of playing cards are
mutually exclusive events.
(c) Drawingafacecardanddrawinganacefromafulldeckofplayingcardsaremutuallyexclusiveevents.
3.2 Roulettewheel. Thegameofrouletteinvolvesspinningawheelwith38slots: 18red,18black,and2
green. A ball is spun onto the wheel and will eventually land in a slot, where each slot has an equal chance
of capturing the ball.
(a) You watch a roulette wheel spin 3 consecutive times and the ball
lands on a red slot each time. What is the probability that the
ball will land on a red slot on the next spin?
(b) You watch a roulette wheel spin 300 consecutive times and the
ball lands on a red slot each time. What is the probability that
the ball will land on a red slot on the next spin?
(c) Are you equally confident of your answers to parts (a) and (b)?
PhotobyH˚akanDahlstr¨om
Why or why not? (http://flic.kr/p/93fEzp)
CCBY2.0license
3.3 Fourgames,onewinner. Below are four versions of the same game. Your archnemesis gets to pick
the version of the game, and then you get to choose how many times to flip a coin: 10 times or 100 times.
Identifyhowmanycoinflipsyoushouldchooseforeachversionofthegame. Itcosts$1toplayeachgame.
Explain your reasoning.
(a) If the proportion of heads is larger than 0.60, you win $1.
(b) If the proportion of heads is larger than 0.40, you win $1.
(c) If the proportion of heads is between 0.40 and 0.60, you win $1.
(d) If the proportion of heads is smaller than 0.30, you win $1.
3.4 Backgammon. Backgammon is a board game for two players in which the playing pieces are moved
accordingtotherolloftwodice. Playerswinbyremovingalloftheirpiecesfromtheboard,soitisusually
good to roll high numbers. You are playing backgammon with a friend and you roll two 6s in your first
roll and two 6s in your second roll. Your friend rolls two 3s in his first roll and again in his second row.
Your friend claims that you are cheating, because rolling double 6s twice in a row is very unlikely. Using
probability, show that your rolls were just as likely as his.
3.5 Coinflips. If you flip a fair coin 10 times, what is the probability of
(a) getting all tails?
(b) getting all heads?
(c) getting at least one tails?
3.6 Dicerolls. If you roll a pair of fair dice, what is the probability of
(a) getting a sum of 1?
(b) getting a sum of 5?
(c) getting a sum of 12?
3.1. DEFINING PROBABILITY 93
3.7 Swingvoters. A Pew Research survey asked 2,373 randomly sampled registered voters their political
affiliation (Republican, Democrat, or Independent) and whether or not they identify as swing voters. 35%
of respondents identified as Independent, 23% identified as swing voters, and 11% identified as both.21
(a) Are being Independent and being a swing voter disjoint, i.e. mutually exclusive?
(b) Draw a Venn diagram summarizing the variables and their associated probabilities.
(c) What percent of voters are Independent but not swing voters?
(d) What percent of voters are Independent or swing voters?
(e) What percent of voters are neither Independent nor swing voters?
(f) IstheeventthatsomeoneisaswingvoterindependentoftheeventthatsomeoneisapoliticalIndepen-
dent?
3.8 Poverty and language. The American Community Survey is an ongoing survey that provides data
every year to give communities the current information they need to plan investments and services. The
2010 American Community Survey estimates that 14.6% of Americans live below the poverty line, 20.7%
speak a language other than English (foreign language) at home, and 4.2% fall into both categories.22
(a) Are living below the poverty line and speaking a foreign language at home disjoint?
(b) Draw a Venn diagram summarizing the variables and their associated probabilities.
(c) What percent of Americans live below the poverty line and only speak English at home?
(d) What percent of Americans live below the poverty line or speak a foreign language at home?
(e) What percent of Americans live above the poverty line and only speak English at home?
(f) Is the event that someone lives below the poverty line independent of the event that the person speaks
a foreign language at home?
3.9 Disjointvs. independent. Inparts(a)and(b), identifywhethertheeventsaredisjoint, independent,
or neither (events cannot be both disjoint and independent).
(a) You and a randomly selected student from your class both earn A’s in this course.
(b) You and your class study partner both earn A’s in this course.
(c) If two events can occur at the same time, must they be dependent?
3.10 Guessing on an exam. In a multiple choice exam, there are 5 questions and 4 choices for each
question(a,b,c,d). Nancyhasnotstudiedfortheexamatallanddecidestorandomlyguesstheanswers.
What is the probability that:
(a) the first question she gets right is the 5th question?
(b) she gets all of the questions right?
(c) she gets at least one question right?
21Pew Research Center, With Voters Focused on Economy, Obama Lead Narrows, data collected between April
4-15,2012.
22U.S.CensusBureau,2010AmericanCommunitySurvey1-YearEstimates,CharacteristicsofPeoplebyLanguage
SpokenatHome.
94 CHAPTER 3. PROBABILITY
3.11 Educational attainment of couples. The table below shows the distribution of education level
attained by US residents by gender based on data collected in the 2010 American Community Survey.23
Gender
Male Female
Less than 9th grade 0.07 0.13
9th to 12th grade, no diploma 0.10 0.09
Highest HS graduate (or equivalent) 0.30 0.20
education Some college, no degree 0.22 0.24
attained Associate’s degree 0.06 0.08
Bachelor’s degree 0.16 0.17
Graduate or professional degree 0.09 0.09
Total 1.00 1.00
(a) What is the probability that a randomly chosen man has at least a Bachelor’s degree?
(b) What is the probability that a randomly chosen woman has at least a Bachelor’s degree?
(c) WhatistheprobabilitythatamanandawomangettingmarriedbothhaveatleastaBachelor’sdegree?
Note any assumptions you must make to answer this question.
(d) Ifyoumadeanassumptioninpart(c),doyouthinkitwasreasonable? Ifyoudidn’tmakeanassumption,
double check your earlier answer and then return to this part.
3.12 School absences. Data collected at elementary schools in DeKalb County, GA suggest that each
yearroughly25%ofstudentsmissexactlyonedayofschool,15%miss2days,and28%miss3ormoredays
due to sickness.24
(a) Whatistheprobabilitythatastudentchosenatrandomdoesn’tmissanydaysofschoolduetosickness
this year?
(b) What is the probability that a student chosen at random misses no more than one day?
(c) What is the probability that a student chosen at random misses at least one day?
(d) IfaparenthastwokidsataDeKalbCountyelementaryschool,whatistheprobabilitythatneitherkid
will miss any school? Note any assumption you must make to answer this question.
(e) If a parent has two kids at a DeKalb County elementary school, what is the probability that both kids
will miss some school, i.e. at least one day? Note any assumption you make.
(f) If you made an assumption in part (d) or (e), do you think it was reasonable? If you didn’t make any
assumptions, double check your earlier answers.
23U.S.CensusBureau,2010AmericanCommunitySurvey1-YearEstimates,EducationalAttainment.
24S.S.Mizanetal.“Absence,ExtendedAbsence,andRepeatTardinessRelatedtoAsthmaStatusamongElemen-
tarySchoolChildren”. In: Journal of Asthma 48.3(2011),pp.228–234.
3.2. CONDITIONAL PROBABILITY 95
3.2 Conditional probability
There can be rich relationships between two or more variables that are useful to understand.
For example a car insurance company will consider information about a person’s driving history to
assess the risk that they will be responsible for an accident. These types of relationships are the
realm of conditional probabilities.
3.2.1 Exploring probabilities with a contingency table
The photo classify data set represents a classifier a sample of 1822 photos from a photo
sharing website. Data scientists have been working to improve a classifier for whether the photo is
aboutfashionornot, andthese1822photosrepresentatestfortheirclassifier. Eachphotogetstwo
classifications: thefirstiscalledmach learnandgivesaclassificationfromamachinelearning(ML)
system of either pred fashion or pred not. Each of these 1822 photos have also been classified
carefully by a team of people, which we take to be the source of truth; this variable is called truth
and takes values fashion and not. Figure 3.11 summarizes the results.
truth
fashion not Total
pred fashion 197 22 219
mach learn
pred not 112 1491 1603
Total 309 1513 1822
Figure 3.11: Contingency table summarizing the photo classify data set.
Fashion Photos
0.06
0.01
0.11
ML Predicts Fashion
Neither: 0.82
Figure 3.12: A Venn diagram using boxes for the photo classify data set.
EXAMPLE3.26
If a photo is actually about fashion, what is the chance the ML classifier correctly identified the
photo as being about fashion?
We can estimate this probability using the data. Of the 309 fashion photos, the ML algorithm
correctly classified 197 of the photos:
197
P(mach learn is pred fashion given truth is fashion)= =0.638
309
96 CHAPTER 3. PROBABILITY
EXAMPLE3.27
We sample a photo from the data set and learn the ML algorithm predicted this photo was not
about fashion. What is the probability that it was incorrect and the photo is about fashion?
If the ML classifier suggests a photo is not about fashion, then it comes from the second row in the
data set. Of these 1603 photos, 112 were actually about fashion:
112
P(truth is fashion given mach learn is pred not)= =0.070
1603
3.2.2 Marginal and joint probabilities
Figure3.11includesrowandcolumntotalsforeachvariableseparatelyinthephoto classify
dataset. Thesetotalsrepresentmarginal probabilitiesforthesample,whicharetheprobabilities
based on a single variable without regard to any other variables. For instance, a probability based
solely on the mach learn variable is a marginal probability:
219
P(mach learn is pred fashion)= =0.12
1822
A probability of outcomes for two or more variables or processes is called a joint probability:
197
P(mach learn is pred fashion and truth is fashion)= =0.11
1822
It is common to substitute a comma for “and” in a joint probability, although using either the word
“and” or a comma is acceptable:
P(mach learn is pred fashion, truth is fashion)
means the same thing as
P(mach learn is pred fashion and truth is fashion)
MARGINALANDJOINTPROBABILITIES
If a probability is based on a single variable, it is a marginal probability. The probability of
outcomes for two or more variables or processes is called a joint probability.
We use table proportions to summarize joint probabilities for the photo classify sample.
These proportions are computed by dividing each count in Figure 3.11 by the table’s total, 1822,
to obtain the proportions in Figure 3.13. The joint probability distribution of the mach learn and
truth variables is shown in Figure 3.14.
truth: fashion truth: not Total
mach learn: pred fashion 0.1081 0.0121 0.1202
mach learn: pred not 0.0615 0.8183 0.8798
Total 0.1696 0.8304 1.00
Figure 3.13: Probability table summarizing the photo classify data set.
3.2. CONDITIONAL PROBABILITY 97
Joint outcome Probability
mach learn is pred fashion and truth is fashion 0.1081
mach learn is pred fashion and truth is not 0.0121
mach learn is pred not and truth is fashion 0.0615
mach learn is pred not and truth is not 0.8183
Total 1.0000
Figure 3.14: Joint probability distribution for the photo classify data set.
GUIDEDPRACTICE3.28
Verify Figure 3.14 represents a probability distribution: events are disjoint, all probabilities are
non-negative, and the probabilities sum to 1.25
We can compute marginal probabilities using joint probabilities in simple cases. For example,
the probability a randomly selected photo from the data set is about fashion is found by summing
the outcomes where truth takes value fashion:
P(truth is fashion)=P(mach learn is pred fashion and truth is fashion)
+P(mach learn is pred not and truth is fashion)
=0.1081+0.0615
=0.1696
3.2.3 Defining conditional probability
TheMLclassifierpredictswhetheraphotoisaboutfashion, evenifitisnotperfect. Wewould
like to better understand how to use information from a variable like mach learn to improve our
probability estimation of a second variable, which in this example is truth.
The probability that a random photo from the data set is about fashion is about 0.17. If we
knew the machine learning classifier predicted the photo was about fashion, could we get a better
estimate of the probability the photo is actually about fashion? Absolutely. To do so, we limit our
viewtoonlythose219caseswheretheMLclassifierpredictedthatthephotowasaboutfashionand
look at the fraction where the photo was actually about fashion:
197
P(truth is fashion given mach learn is pred fashion)= =0.900
219
We call this a conditional probability because we computed the probability under a condition:
the ML classifier prediction said the photo was about fashion.
Therearetwopartstoaconditionalprobability,theoutcome of interestandthecondition.
Itisusefultothinkoftheconditionasinformationweknowtobetrue,andthisinformationusually
canbedescribedasaknownoutcomeorevent. Wegenerallyseparatethetextinsideourprobability
notation into the outcome of interest and the condition with a vertical bar:
P(truth is fashion given mach learn is pred fashion)
197
=P(truth is fashion | mach learn is pred fashion)= =0.900
219
The vertical bar “|” is read as given.
25Eachofthefouroutcomecombinationaredisjoint,allprobabilitiesareindeednon-negative,andthesumofthe
probabilitiesis0.1081+0.0121+0.0615+0.8183=1.00.
98 CHAPTER 3. PROBABILITY
In the last equation, we computed the probability a photo was about fashion based on the
condition that the ML algorithm predicted it was about fashion as a fraction:
P(truth is fashion | mach learn is pred fashion)
# cases where truth is fashion and mach learn is pred fashion
=
# cases where mach learn is pred fashion
197
= =0.900
219
We considered only those cases that met the condition, mach learn is pred fashion, and then we
computed the ratio of those cases that satisfied our outcome of interest, photo was actually about
fashion.
Frequently, marginal and joint probabilities are provided instead of count data. For example,
disease rates are commonly listed in percentages rather than in a count format. We would like to
be able to compute conditional probabilities even when no counts are available, and we use the last
equation as a template to understand this technique.
We considered only those cases that satisfied the condition, where the ML algorithm predicted
fashion. Of these cases, the conditional probability was the fraction representing the outcome of
interest, that the photo was about fashion. Suppose we were provided only the information in Fig-
ure 3.13, i.e. only probability data. Then if we took a sample of 1000 photos, we would anticipate
about 12.0% or 0.120×1000 = 120 would be predicted to be about fashion (mach learn is pred
fashion). Similarly, we would expect about 10.8% or 0.108×1000 = 108 to meet both the in-
formation criteria and represent our outcome of interest. Then the conditional probability can be
computed as
P(truth is fashion | mach learn is pred fashion)
# (truth is fashion and mach learn is pred fashion)
=
# (mach learn is pred fashion)
108 0.108
= = =0.90
120 0.120
Hereweareexaminingexactlythefractionoftwoprobabilities,0.108and0.120,whichwecanwrite
as
P(truth is fashion and mach learn is pred fashion) and P(mach learn is pred fashion).
The fraction of these probabilities is an example of the general formula for conditional probability.
CONDITIONALPROBABILITY
The conditional probability of outcome A given condition B is computed as the following:
P(A and B)
P(A|B)=
P(B)
GUIDEDPRACTICE3.29
(a) Write out the following statement in conditional probability notation: “The probability that the
ML prediction was correct, if the photo was about fashion”. Here the condition is now based on the
photo’s truth status, not the ML algorithm.
(b) Determine the probability from part (a). Table 3.13 on page 96 may be helpful.26
26(a)IfthephotoisaboutfashionandtheMLalgorithmpredictionwascorrect,thentheMLalgorithmmyhave
avalueof pred fashion:
P(mach learnispred fashion|truthisfashion)
(b)Theequationforconditionalprobabilityindicatesweshouldfirstfind
P(mach learnispred fashionandtruthisfashion)=0.1081andP(truthisfashion)=0.1696.
Thentheratiorepresentstheconditionalprobability: 0.1081/0.1696=0.6374.
3.2. CONDITIONAL PROBABILITY 99
GUIDEDPRACTICE3.30
(a)Determinetheprobabilitythatthealgorithmisincorrectifitisknownthephotoisaboutfashion.
(b) Using the answers from part (a) and Guided Practice 3.29(b), compute
P(mach learn is pred fashion | truth is fashion)
+ P(mach learn is pred not | truth is fashion)
(c) Provide an intuitive argument to explain why the sum in (b) is 1.27
3.2.4 Smallpox in Boston, 1721
The smallpox data set provides a sample of 6,224 individuals from the year 1721 who were
exposed to smallpox in Boston. Doctors at the time believed that inoculation, which involves
exposing a person to the disease in a controlled form, could reduce the likelihood of death.
Each case represents one person with two variables: inoculated and result. The variable
inoculated takes two levels: yes or no, indicating whether the person was inoculated or not. The
variable result has outcomes lived or died. These data are summarized in Tables 3.15 and 3.16.
inoculated
yes no Total
lived 238 5136 5374
result
died 6 844 850
Total 244 5980 6224
Figure 3.15: Contingency table for the smallpox data set.
inoculated
yes no Total
lived 0.0382 0.8252 0.8634
result
died 0.0010 0.1356 0.1366
Total 0.0392 0.9608 1.0000
Figure 3.16: Table proportions for the smallpox data, computed by dividing each
count by the table total, 6224.
GUIDEDPRACTICE3.31
Write out, in formal notation, the probability a randomly selected person who was not inoculated
died from smallpox, and find this probability.28
GUIDEDPRACTICE3.32
Determine the probability that an inoculated person died from smallpox. How does this result
compare with the result of Guided Practice 3.31?29
27(a)Thisprobabilityis P(mach learnispred not,truthisfashion) = 0.0615 =0.3626. (b)Thetotalequals1. (c)Under
P(truthisfashion) 0.1696
the condition the photo is about fashion, the ML algorithm must have either predicted it was about fashion or
predicteditwasnotaboutfashion. Thecomplementstillworksforconditionalprobabilities,providedtheprobabilities
areconditionedonthesameinformation.
28P(result=died|inoculated=no)= P(result=diedandinoculated=no) = 0.1356 =0.1411.
P(inoculated=no) 0.9608
29P(result = died | inoculated = yes) = P(result=diedandinoculated=yes) = 0.0010 = 0.0255 (if we avoided
P(inoculated=yes) 0.0392
roundingerrors,we’dget6/244=0.0246). Thedeathrateforindividualswhowereinoculatedisonlyabout1in40
whilethedeathrateisabout1in7forthosewhowerenotinoculated.
100 CHAPTER 3. PROBABILITY
GUIDEDPRACTICE3.33
The people of Boston self-selected whether or not to be inoculated. (a) Is this study observational
or was this an experiment? (b) Can we infer any causal connection using these data? (c) What are
somepotential confoundingvariables thatmight influencewhethersomeone lived or died andalso
affect whether that person was inoculated?30
3.2.5 General multiplication rule
Section 3.1.7 introduced the Multiplication Rule for independent processes. Here we provide
the General Multiplication Rule for events that might not be independent.
GENERALMULTIPLICATIONRULE
If A and B represent two outcomes or events, then
P(A and B)=P(A|B)×P(B)
It is useful to think of A as the outcome of interest and B as the condition.
ThisGeneral MultiplicationRuleis simplyarearrangement oftheconditional probabilityequation.
EXAMPLE3.34
Consider the smallpox data set. Suppose we are given only two pieces of information: 96.08%
of residents were not inoculated, and 85.88% of the residents who were not inoculated ended up
surviving. How could we compute the probability that a resident was not inoculated and lived?
We will compute our answer using the General Multiplication Rule and then verify it using Fig-
ure 3.16. We want to determine
P(result = lived and inoculated = no)
and we are given that
P(result = lived | inoculated = no)=0.8588 P(inoculated = no)=0.9608
Among the 96.08% of people who were not inoculated, 85.88% survived:
P(result = lived and inoculated = no)=0.8588×0.9608=0.8251
ThisisequivalenttotheGeneralMultiplicationRule. WecanconfirmthisprobabilityinFigure3.16
at the intersection of no and lived (with a small rounding error).
GUIDEDPRACTICE3.35
Use P(inoculated = yes) = 0.0392 and P(result = lived | inoculated = yes) = 0.9754 to
determine the probability that a person was both inoculated and lived.31
GUIDEDPRACTICE3.36
If 97.54% of the inoculated people lived, what proportion of inoculated people must have died?32
30Brief answers: (a) Observational. (b) No, we cannot infer causation from this observational study. (c) Accessi-
bilitytothelatestandbestmedicalcare. Thereareothervalidanswersforpart(c).
31Theansweris0.0382,whichcanbeverifiedusingFigure3.16.
32Therewereonlytwopossibleoutcomes: livedordied. Thismeansthat100%-97.54%=2.46%ofthepeople
whowereinoculateddied.
3.2. CONDITIONAL PROBABILITY 101
SUMOFCONDITIONALPROBABILITIES
Let A , ..., A represent all the disjoint outcomes for a variable or process. Then if B is an
1 k
event, possibly for another variable or process, we have:
P(A |B)+···+P(A |B)=1
1 k
The rule for complements also holds when an event and its complement are conditioned on the
same information:
P(A|B)=1−P(Ac|B)
GUIDEDPRACTICE3.37
Based on the probabilities computed above, does it appear that inoculation is effective at reducing
the risk of death from smallpox?33
3.2.6 Independence considerations in conditional probability
Iftwoeventsareindependent, thenknowingtheoutcomeofoneshouldprovidenoinformation
about the other. We can show this is mathematically true using conditional probabilities.
GUIDEDPRACTICE3.38
Let X and Y represent the outcomes of rolling two dice.34
(a) What is the probability that the first die, X, is 1?
(b) What is the probability that both X and Y are 1?
(c) Use the formula for conditional probability to compute P(Y = 1 | X = 1).
(d) What is P(Y =1)? Is this different from the answer from part (c)? Explain.
We can show in Guided Practice 3.38(c) that the conditioning information has no influence by
using the Multiplication Rule for independence processes:
P(Y =1 and X =1)
P(Y =1 | X =1)=
P(X =1)
P(Y =1)×P(X =1)
=
P(X =1)
=P(Y =1)
GUIDEDPRACTICE3.39
Ron is watching a roulette table in a casino and notices that the last five outcomes were black. He
figures that the chances of getting black six times in a row is very small (about 1/64) and puts his
paycheck on red. What is wrong with his reasoning?35
33Thesamplesarelargerelativetothedifferenceindeathratesforthe“inoculated”and“notinoculated”groups,
so it seems there is an association between inoculated and outcome. However, as noted in the solution to Guided
Practice3.33,thisisanobservationalstudyandwecannotbesureifthereisacausalconnection. (Furtherresearch
hasshownthatinoculationiseffectiveatreducingdeathrates.)
34Brief solutions: (a) 1/6. (b) 1/36. (c) P(Y=1andX=1) = 1/36 = 1/6. (d) The probability is the same as in
P(X=1) 1/6
part(c): P(Y =1)=1/6. TheprobabilitythatY =1wasunchangedbyknowledgeaboutX,whichmakessenseas
X andY areindependent.
35Hehasforgottenthatthenextroulettespinisindependentofthepreviousspins. Casinosdoemploythispractice,
posting the last several outcomes of many betting games to trick unsuspecting gamblers into believing the odds are
intheirfavor. Thisiscalledthegambler’s fallacy.
102 CHAPTER 3. PROBABILITY
3.2.7 Tree diagrams
Tree diagrams are a tool to organize outcomes and probabilities around the structure of the
data. They are most useful when two or more processes occur in a sequence and each process is
conditioned on its predecessors.
The smallpox data fit this description. We see the population as split by inoculation: yes
and no. Following this split, survival rates were observed for each group. This structure is reflected
in the tree diagram shown in Figure 3.17. The first branch for inoculation is said to be the
primary branch while the other branches are secondary.
Inoculated Result
lived, 0.9754
0.0392*0.9754 = 0.03824
yes, 0.0392
died, 0.0246
0.0392*0.0246 = 0.00096
lived, 0.8589
0.9608*0.8589 = 0.82523
no, 0.9608
died, 0.1411
0.9608*0.1411 = 0.13557
Figure 3.17: A tree diagram of the smallpox data set.
Tree diagrams are annotated with marginal and conditional probabilities, as shown in Fig-
ure 3.17. This tree diagram splits the smallpox data by inoculation into the yes and no groups
with respective marginal probabilities 0.0392 and 0.9608. The secondary branches are conditioned
onthefirst, soweassignconditionalprobabilitiestothesebranches. Forexample, thetopbranchin
Figure3.17istheprobabilitythatresult=livedconditionedontheinformationthatinoculated
= yes. We may (and usually do) construct joint probabilities at the end of each branch in our tree
by multiplying the numbers we come across as we move from left to right. These joint probabilities
are computed using the General Multiplication Rule:
P(inoculated = yes and result = lived)
=P(inoculated = yes)×P(result = lived|inoculated = yes)
=0.0392×0.9754=0.0382
3.2. CONDITIONAL PROBABILITY 103
EXAMPLE3.40
Consider the midterm and final for a statistics class. Suppose 13% of students earned an A on the
midterm. Of those students who earned an A on the midterm, 47% received an A on the final, and
11% of the students who earned lower than an A on the midterm received an A on the final. You
randomly pick up a final exam and notice the student received an A. What is the probability that
this student earned an A on the midterm?
The end-goal is to find P(midterm = A|final = A). To calculate this conditional probability, we
need the following probabilities:
P(midterm = A and final = A) and P(final = A)
However, thisinformationisnotprovided, anditisnotobvioushowtocalculatetheseprobabilities.
Since we aren’t sure how to proceed, it is useful to organize the information into a tree diagram:
Midterm Final
A, 0.47
0.13*0.47 = 0.0611
A, 0.13
other, 0.53
0.13*0.53 = 0.0689
A, 0.11
0.87*0.11 = 0.0957
other, 0.87
other, 0.89
0.87*0.89 = 0.7743
When constructing a tree diagram, variables provided with marginal probabilities are often used to
create the tree’s primary branches; in this case, the marginal probabilities are provided for midterm
grades. The final grades, which correspond to the conditional probabilities provided, will be shown
on the secondary branches.
With the tree diagram constructed, we may compute the required probabilities:
P(midterm = A and final = A)=0.0611
P(final = A)
=P(midterm = other and final = A)+P(midterm = A and final = A)
=0.0957+0.0611=0.1568
The marginal probability, P(final = A), was calculated by adding up all the joint probabilities on
the right side of the tree that correspond to final = A. We may now finally take the ratio of the
two probabilities:
P(midterm = A and final = A)
P(midterm = A|final = A)=
P(final = A)
0.0611
= =0.3897
0.1568
The probability the student also earned an A on the midterm is about 0.39.
104 CHAPTER 3. PROBABILITY
GUIDEDPRACTICE3.41
After an introductory statistics course, 78% of students can successfully construct tree diagrams.
Of those who can construct tree diagrams, 97% passed, while only 57% of those students who could
not construct tree diagrams passed. (a) Organize this information into a tree diagram. (b) What is
the probability that a randomly selected student passed? (c) Compute the probability a student is
able to construct a tree diagram if it is known that she passed.36
3.2.8 Bayes’ Theorem
In many instances, we are given a conditional probability of the form
P(statement about variable 1 | statement about variable 2)
but we would really like to know the inverted conditional probability:
P(statement about variable 2 | statement about variable 1)
Treediagramscanbeusedtofindthesecondconditionalprobabilitywhengiventhefirst. However,
sometimes it is not possible to draw the scenario in a tree diagram. In these cases, we can apply a
very useful and general formula: Bayes’ Theorem.
We first take a critical look at an example of inverting conditional probabilities where we still
apply a tree diagram.
36(a)Thetreediagramisshowntotheright.
(b)Identifywhichtwojointprobabilitiesrepresentstudentswhopassed,andaddthem: P(passed)=0.7566+0.1254=
0.8820.
(c)P(constructtreediagram|passed)= 0.7566 =0.8578.
0.8820
Able to construct Pass class
tree diagrams
pass, 0.97
0.78*0.97 = 0.7566
yes, 0.78
fail, 0.03
0.78*0.03 = 0.0234
pass, 0.57
0.22*0.57 = 0.1254
no, 0.22
fail, 0.43
0.22*0.43 = 0.0946
3.2. CONDITIONAL PROBABILITY 105
EXAMPLE3.42
In Canada, about 0.35% of women over 40 will develop breast cancer in any given year. A common
screening test for cancer is the mammogram, but this test is not perfect. In about 11% of patients
with breast cancer, the test gives a false negative: it indicates a woman does not have breast
cancerwhenshedoeshavebreastcancer. Similarly,thetestgivesafalse positivein7%ofpatients
who do not have breast cancer: it indicates these patients have breast cancer when they actually do
not. Ifwetestedarandomwomanover40forbreastcancerusingamammogramandthetestcame
back positive – that is, the test suggested the patient has cancer – what is the probability that the
patient actually has breast cancer?
Noticethatwearegivensufficientinformationtoquicklycomputetheprobabilityoftestingpositive
if a woman has breast cancer (1.00−0.11 = 0.89). However, we seek the inverted probability of
cancer given a positive test result. (Watch out for the non-intuitive medical language: a positive
test result suggests the possible presence of cancer in a mammogram screening.) This inverted
probability may be broken into two pieces:
P(has BC and mammogram+)
P(has BC | mammogram+)=
P(mammogram+)
where“hasBC”isanabbreviationforthepatienthavingbreastcancerand“mammogram+”means
the mammogram screening was positive. We can construct a tree diagram for these probabilities:
Truth Mammogram
positive, 0.89
0.0035*0.89 = 0.00312
cancer, 0.0035
negative, 0.11
0.0035*0.11 = 0.00038
positive, 0.07
0.9965*0.07 = 0.06976
no cancer, 0.9965
negative, 0.93
0.9965*0.93 = 0.92675
The probability the patient has breast cancer and the mammogram is positive is
P(has BC and mammogram+)=P(mammogram+ | has BC)P(has BC)
=0.89×0.0035=0.00312
The probability of a positive test result is the sum of the two corresponding scenarios:
P(mammogram+)=P(mammogram+ and has BC)
+P(mammogram+ and no BC)
=P(has BC)P(mammogram+ | has BC)
+P(no BC)P(mammogram+ | no BC)
=0.0035×0.89+0.9965×0.07=0.07288
Then if the mammogram screening is positive for a patient, the probability the patient has breast
cancer is
P(has BC and mammogram+)
P(has BC | mammogram+)=
P(mammogram+)
0.00312
= ≈0.0428
0.07288
That is, even if a patient has a positive mammogram screening, there is still only a 4% chance that
she has breast cancer.
106 CHAPTER 3. PROBABILITY
Example 3.42 highlights why doctors often run more tests regardless of a first positive test
result. When a medical condition is rare, a single positive test isn’t generally definitive.
Consider again the last equation of Example 3.42. Using the tree diagram, we can see that the
numerator (the top of the fraction) is equal to the following product:
P(has BC and mammogram+)=P(mammogram+ | has BC)P(has BC)
The denominator – the probability the screening was positive – is equal to the sum of probabilities
for each positive screening scenario:
P(mammogram+)=P(mammogram+ and no BC)+P(mammogram+ and has BC)
In the example, each of the probabilities on the right side was broken down into a product of a
conditional probability and marginal probability using the tree diagram.
P(mammogram+)=P(mammogram+ and no BC)+P(mammogram+ and has BC)
=P(mammogram+ | no BC)P(no BC)
+P(mammogram+ | has BC)P(has BC)
We can see an application of Bayes’ Theorem by substituting the resulting probability expressions
into the numerator and denominator of the original conditional probability.
P(has BC | mammogram+)
P(mammogram+ | has BC)P(has BC)
=
P(mammogram+ | no BC)P(no BC)+P(mammogram+ | has BC)P(has BC)
BAYES’THEOREM:INVERTINGPROBABILITIES
Consider the following conditional probability for variable 1 and variable 2:
P(outcome A of variable 1 | outcome B of variable 2)
1
Bayes’ Theorem states that this conditional probability can be identified as the following frac-
tion:
P(B|A )P(A )
1 1
P(B|A )P(A )+P(B|A )P(A )+···+P(B|A )P(A )
1 1 2 2 k k
where A , A , ..., and A represent all other possible outcomes of the first variable.
2 3 k
Bayes’ Theorem is a generalization of what we have done using tree diagrams. The numerator
identifies the probability of getting both A and B. The denominator is the marginal probability of
1
getting B. This bottom component of the fraction appears long and complicated since we have to
add up probabilities from all of the different ways to get B. We always completed this step when
using tree diagrams. However, we usually did it in a separate step so it didn’t seem as complex.
To apply Bayes’ Theorem correctly, there are two preparatory steps:
(1) First identify the marginal probabilities of each possible outcome of the first variable: P(A ),
1
P(A ), ..., P(A ).
2 k
(2) Then identify the probability of the outcome B, conditioned on each possible scenario for the
first variable: P(B|A ), P(B|A ), ..., P(B|A ).
1 2 k
Once each of these probabilities are identified, they can be applied directly within the formula.
Bayes’ Theorem tends to be a good option when there are so many scenarios that drawing a tree
diagram would be complex.
3.2. CONDITIONAL PROBABILITY 107
GUIDEDPRACTICE3.43
Jose visits campus every Thursday evening. However, some days the parking garage is full, often
due to college events. There are academic events on 35% of evenings, sporting events on 20% of
evenings, and no events on 45% of evenings. When there is an academic event, the garage fills up
about 25% of the time, and it fills up 70% of evenings with sporting events. On evenings when
there are no events, it only fills up about 5% of the time. If Jose comes to campus and finds the
garage full, what is the probability that there is a sporting event? Use a tree diagram to solve this
problem.37
EXAMPLE3.44
Here we solve the same problem presented in Guided Practice 3.43, except this time we use Bayes’
Theorem.
The outcome of interest is whether there is a sporting event (call this A ), and the condition is that
1
the lot is full (B). Let A represent an academic event and A represent there being no event on
2 3
campus. Then the given probabilities can be written as
P(A )=0.2 P(A )=0.35 P(A )=0.45
1 2 3
P(B|A )=0.7 P(B|A )=0.25 P(B|A )=0.05
1 2 3
Bayes’Theoremcanbeusedtocomputetheprobabilityofasportingevent(A )underthecondition
1
that the parking lot is full (B):
P(B|A )P(A )
P(A |B)= 1 1
1 P(B|A )P(A )+P(B|A )P(A )+P(B|A )P(A )
1 1 2 2 3 3
(0.7)(0.2)
=
(0.7)(0.2)+(0.25)(0.35)+(0.05)(0.45)
=0.56
Based on the information that the garage is full, there is a 56% probability that a sporting event is
being held on campus that evening.
37The tree diagram, with three
Event Garage full
primary branches, is shown to
theright. Next,weidentifytwo
Full, 0.25
probabilities from the tree dia- 0.35*0.25 = 0.0875
Academic, 0.35
gram. (1) The probability that
Spaces Available, 0.75
there is a sporting event and 0.35*0.75 = 0.2625
thegarageisfull: 0.14. (2)The
Full, 0.7
probability the garage is full: 0.2*0.7 = 0.14
Sporting, 0.20
0.0875+0.14+0.0225 = 0.25.
Spaces Available, 0.3
Thenthesolutionistheratioof 0.2*0.3 = 0.06
t If he t s h e e p g ro a b ra a g b e ili i t s ie f s u : ll 0 0 , . . 1 2 t 4 5 he = re 0 i . s 56 a . None, 0.45 Full, 0.05 0.45*0.05 = 0.0225
56% probability that there is a Spaces Available, 0.95
sportingevent. 0.45*0.95 = 0.4275
108 CHAPTER 3. PROBABILITY
GUIDEDPRACTICE3.45
Use the information in the previous exercise and example to verify the probability that there is an
academic event conditioned on the parking lot being full is 0.35.38
GUIDEDPRACTICE3.46
In Guided Practice 3.43 and 3.45, you found that if the parking lot is full, the probability there is a
sportingeventis0.56andtheprobabilitythereisanacademiceventis0.35. Usingthisinformation,
compute P(no event | the lot is full).39
The last several exercises offered a way to update our belief about whether there is a sporting
event, academicevent, ornoeventgoingonattheschoolbasedontheinformationthattheparking
lot was full. This strategy of updating beliefs using Bayes’ Theorem is actually the foundation of an
entire section of statistics called Bayesian statistics. While Bayesian statistics is very important
and useful, we will not have time to cover much more of it in this book.
38Shortanswer:
P(A2|B)=
P(B|A2)P(A2)
P(B|A1)P(A1)+P(B|A2)P(A2)+P(B|A3)P(A3)
(0.25)(0.35)
=
(0.7)(0.2)+(0.25)(0.35)+(0.05)(0.45)
=0.35
39Eachprobabilityisconditionedonthesameinformationthatthegarageisfull,sothecomplementmaybeused:
1.00−0.56−0.35=0.09.
3.2. CONDITIONAL PROBABILITY 109
Exercises
3.13 Jointandconditionalprobabilities. P(A) = 0.3, P(B) = 0.7
(a) Can you compute P(A and B) if you only know P(A) and P(B)?
(b) Assuming that events A and B arise from independent random processes,
i. what is P(A and B)?
ii. what is P(A or B)?
iii. what is P(A|B)?
(c) IfwearegiventhatP(AandB)=0.1,aretherandomvariablesgivingrisetoeventsAandBindepen-
dent?
(d) If we are given that P(A and B) = 0.1, what is P(A|B)?
3.14 PB&J. Suppose 80% of people like peanut butter, 89% like jelly, and 78% like both. Given that a
randomly sampled person likes peanut butter, what’s the probability that he also likes jelly?
3.15 Globalwarming. A Pew Research poll asked 1,306 Americans “From what you’ve read and heard,
is there solid evidence that the average temperature on earth has been getting warmer over the past few
decades, or not?”. The table below shows the distribution of responses by party and ideology, where the
counts have been replaced with relative frequencies.40
Response
Earth is Not Don’t Know
warming warming Refuse Total
Conservative Republican 0.11 0.20 0.02 0.33
Party and Mod/Lib Republican 0.06 0.06 0.01 0.13
Ideology Mod/Cons Democrat 0.25 0.07 0.02 0.34
Liberal Democrat 0.18 0.01 0.01 0.20
Total 0.60 0.34 0.06 1.00
(a) Are believing that the earth is warming and being a liberal Democrat mutually exclusive?
(b) Whatistheprobabilitythatarandomlychosenrespondentbelievestheearthiswarmingorisaliberal
Democrat?
(c) Whatistheprobabilitythatarandomlychosenrespondentbelievestheearthiswarminggiventhathe
is a liberal Democrat?
(d) Whatistheprobabilitythatarandomlychosenrespondentbelievestheearthiswarminggiventhathe
is a conservative Republican?
(e) Does it appear that whether or not a respondent believes the earth is warming is independent of their
party and ideology? Explain your reasoning.
(f) Whatistheprobabilitythatarandomlychosenrespondentisamoderate/liberalRepublicangiventhat
he does not believe that the earth is warming?
40Pew Research Center, Majority of Republicans No Longer See Evidence of Global Warming, data collected on
October27,2010.
110 CHAPTER 3. PROBABILITY
3.16 Healthcoverage, relativefrequencies. The Behavioral Risk Factor Surveillance System (BRFSS)
is an annual telephone survey designed to identify risk factors in the adult population and report emerging
health trends. The following table displays the distribution of health status of respondents to this survey
(excellent, very good, good, fair, poor) and whether or not they have health insurance.
Health Status
Excellent Very good Good Fair Poor Total
Health No 0.0230 0.0364 0.0427 0.0192 0.0050 0.1262
Coverage Yes 0.2099 0.3123 0.2410 0.0817 0.0289 0.8738
Total 0.2329 0.3486 0.2838 0.1009 0.0338 1.0000
(a) Are being in excellent health and having health coverage mutually exclusive?
(b) What is the probability that a randomly chosen individual has excellent health?
(c) Whatistheprobabilitythatarandomlychosenindividualhasexcellenthealthgiventhathehashealth
coverage?
(d) What is the probability that a randomly chosen individual has excellent health given that he doesn’t
have health coverage?
(e) Do having excellent health and having health coverage appear to be independent?
3.17 Burger preferences. A 2010 SurveyUSA poll asked 500 Los Angeles residents, “What is the best
hamburger place in Southern California? Five Guys Burgers? In-N-Out Burger? Fat Burger? Tommy’s
Hamburgers? Umami Burger? Or somewhere else?” The distribution of responses by gender is shown
below.41
Gender
Male Female Total
Five Guys Burgers 5 6 11
In-N-Out Burger 162 181 343
Best Fat Burger 10 12 22
hamburger Tommy’s Hamburgers 27 27 54
place Umami Burger 5 1 6
Other 26 20 46
Not Sure 13 5 18
Total 248 252 500
(a) Are being female and liking Five Guys Burgers mutually exclusive?
(b) What is the probability that a randomly chosen male likes In-N-Out the best?
(c) What is the probability that a randomly chosen female likes In-N-Out the best?
(d) What is the probability that a man and a woman who are dating both like In-N-Out the best? Note
any assumption you make and evaluate whether you think that assumption is reasonable.
(e) What is the probability that a randomly chosen person likes Umami best or that person is female?
41SurveyUSA,ResultsofSurveyUSANewsPoll#17718,datacollectedonDecember2,2010.
3.2. CONDITIONAL PROBABILITY 111
3.18 Assortativemating. Assortativematingisanonrandommatingpatternwhereindividualswithsimi-
largenotypesand/orphenotypesmatewithoneanothermorefrequentlythanwhatwouldbeexpectedunder
a random mating pattern. Researchers studying this topic collected data on eye colors of 204 Scandinavian
men and their female partners. The table below summarizes the results.42
Partner (female)
Blue Brown Green Total
Blue 78 23 13 114
Brown 19 23 12 54
Self (male)
Green 11 9 16 36
Total 108 55 41 204
(a) What is the probability that a randomly chosen male respondent or his partner has blue eyes?
(b) Whatistheprobabilitythatarandomlychosenmalerespondentwithblueeyeshasapartnerwithblue
eyes?
(c) What is the probability that a randomly chosen male respondent with brown eyes has a partner with
blueeyes? Whatabouttheprobabilityofarandomlychosenmalerespondentwithgreeneyeshavinga
partner with blue eyes?
(d) Does it appear that the eye colors of male respondents and their partners are independent? Explain
your reasoning.
3.19 Drawingboxplots. Afteranintroductorystatisticscourse,80%ofstudentscansuccessfullyconstruct
box plots. Of those who can construct box plots, 86% passed, while only 65% of those students who could
not construct box plots passed.
(a) Construct a tree diagram of this scenario.
(b) Calculate the probability that a student is able to construct a box plot if it is known that he passed.
3.20 Predispositionforthrombosis. A genetic test is used to determine if people have a predisposition
for thrombosis, which is the formation of a blood clot inside a blood vessel that obstructs the flow of blood
through the circulatory system. It is believed that 3% of people actually have this predisposition. The
genetic test is 99% accurate if a person actually has the predisposition, meaning that the probability of a
positive test result when a person actually has the predisposition is 0.99. The test is 98% accurate if a
persondoesnothavethepredisposition. Whatistheprobabilitythatarandomlyselectedpersonwhotests
positive for the predisposition by the test actually has the predisposition?
3.21 It’s never lupus. Lupus is a medical phenomenon where antibodies that are supposed to attack
foreign cells to prevent infections instead see plasma proteins as foreign bodies, leading to a high risk of
blood clotting. It is believed that 2% of the population suffer from this disease. The test is 98% accurate
if a person actually has the disease. The test is 74% accurate if a person does not have the disease. There
is a line from the Fox television show House that is often used after a patient tests positive for lupus: “It’s
never lupus.” Do you think there is truth to this statement? Use appropriate probabilities to support your
answer.
3.22 Exit poll. Edison Research gathered exit poll results from several sources for the Wisconsin recall
electionofScottWalker. Theyfoundthat53%oftherespondentsvotedinfavorofScottWalker. Addition-
ally, they estimated that of those who did vote in favor for Scott Walker, 37% had a college degree, while
44%ofthosewhovotedagainstScottWalkerhadacollegedegree. Supposewerandomlysampledaperson
who participated in the exit poll and found that he had a college degree. What is the probability that he
voted in favor of Scott Walker?43
42B. Laeng et al. “Why do blue-eyed men prefer women with the same eye color?” In: Behavioral Ecology and
Sociobiology 61.3(2007),pp.371–384.
43NewYorkTimes,Wisconsinrecallexitpolls.
112 CHAPTER 3. PROBABILITY
3.3 Sampling from a small population
Whenwesampleobservationsfromapopulation,usuallywe’reonlysamplingasmallfractionofthe
possible individuals or cases. However, sometimes our sample size is large enough or the population
is small enough that we sample more than 10% of a population44 without replacement (meaning
we do not have a chance of sampling the same cases twice). Sampling such a notable fraction of a
population can be important for how we analyze the sample.
EXAMPLE3.47
Professors sometimes select a student at random to answer a question. If each student has an equal
chance of being selected and there are 15 people in your class, what is the chance that she will pick
you for the next question?
If there are 15 people to ask and none are skipping class, then the probability is 1/15, or about
0.067.
EXAMPLE3.48
If the professor asks 3 questions, what is the probability that you will not be selected? Assume that
she will not pick the same person twice in a given lecture.
For the first question, she will pick someone else with probability 14/15. When she asks the second
question, she only has 14 people who have not yet been asked. Thus, if you were not picked on the
first question, the probability you are again not picked is 13/14. Similarly, the probability you are
again not picked on the third question is 12/13, and the probability of not being picked for any of
the three questions is
P(not picked in 3 questions)
=P(Q1=not picked, Q2=not picked, Q3=not picked.)
14 13 12 12
= × × = =0.80
15 14 13 15
GUIDEDPRACTICE3.49
What rule permitted us to multiply the probabilities in Example 3.48?45
44The10%guidelineisaruleofthumbcutoffforwhentheseconsiderationsbecomemoreimportant.
45Thethreeprobabilitieswecomputedwereactuallyonemarginalprobability,P(Q1=not picked),andtwocondi-
tionalprobabilities:
P(Q2=not picked|Q1=not picked)
P(Q3=not picked|Q1=not picked,Q2=not picked)
UsingtheGeneralMultiplicationRule,theproductofthesethreeprobabilitiesistheprobabilityofnotbeingpicked
in3questions.
3.3. SAMPLING FROM A SMALL POPULATION 113
EXAMPLE3.50
Suppose the professor randomly picks without regard to who she already selected, i.e. students can
be picked more than once. What is the probability that you will not be picked for any of the three
questions?
Each pick is independent, and the probability of not being picked for any individual question is
14/15. Thus, we can use the Multiplication Rule for independent processes.
P(not picked in 3 questions)
=P(Q1=not picked, Q2=not picked, Q3=not picked.)
14 14 14
= × × =0.813
15 15 15
You have a slightly higher chance of not being picked compared to when she picked a new person
for each question. However, you now may be picked more than once.
GUIDEDPRACTICE3.51
Under the setup of Example 3.50, what is the probability of being picked to answer all three ques-
tions?46
Ifwesamplefromasmallpopulationwithout replacement, wenolongerhaveindependence
between our observations. In Example 3.48, the probability of not being picked for the second ques-
tion was conditioned on the event that you were not picked for the first question. In Example 3.50,
the professor sampled her students with replacement: she repeatedly sampled the entire class
without regard to who she already picked.
GUIDEDPRACTICE3.52
Your department is holding a raffle. They sell 30 tickets and offer seven prizes. (a) They place the
tickets in a hat and draw one for each prize. The tickets are sampled without replacement, i.e. the
selectedticketsarenotplacedbackinthehat. Whatistheprobabilityofwinningaprizeifyoubuy
one ticket? (b) What if the tickets are sampled with replacement?47
GUIDEDPRACTICE3.53
Compare your answers in Guided Practice 3.52. How much influence does the sampling method
have on your chances of winning a prize?48
Had we repeated Guided Practice 3.52 with 300 tickets instead of 30, we would have found
something interesting: the results would be nearly identical. The probability would be 0.0233
without replacement and 0.0231 with replacement. When the sample size is only a small fraction
of the population (under 10%), observations are nearly independent even when sampling without
replacement.
46P(beingpickedtoanswerallthreequestions)= (cid:0) 1 (cid:1)3 =0.00030.
15
47(a)Firstdeterminetheprobabilityofnotwinning. Theticketsaresampledwithoutreplacement, whichmeans
the probability you do not win on the first draw is 29/30, 28/29 for the second, ..., and 23/24 for the seventh. The
probabilityyouwinnoprizeistheproductoftheseseparateprobabilities: 23/30. Thatis,theprobabilityofwinning
aprizeis1−23/30=7/30=0.233. (b)Whentheticketsaresampledwithreplacement,therearesevenindependent
draws. Againwefirstfindtheprobabilityofnotwinningaprize: (29/30)7=0.789. Thus,theprobabilityofwinning
(atleast)oneprizewhendrawingwithreplacementis0.211.
48There is about a 10% larger chance of winning a prize when using sampling without replacement. However, at
mostoneprizemaybewonunderthissamplingprocedure.
114 CHAPTER 3. PROBABILITY
Exercises
3.23 Marblesinanurn. Imagine you have an urn containing 5 red, 3 blue, and 2 orange marbles in it.
(a) What is the probability that the first marble you draw is blue?
(b) Supposeyoudrewabluemarbleinthefirstdraw. Ifdrawingwithreplacement,whatistheprobability
of drawing a blue marble in the second draw?
(c) Supposeyouinsteaddrewanorangemarbleinthefirstdraw. Ifdrawingwithreplacement,whatisthe
probability of drawing a blue marble in the second draw?
(d) If drawing with replacement, what is the probability of drawing two blue marbles in a row?
(e) When drawing with replacement, are the draws independent? Explain.
3.24 Socksinadrawer. In your sock drawer you have 4 blue, 5 gray, and 3 black socks. Half asleep one
morning you grab 2 socks at random and put them on. Find the probability you end up wearing
(a) 2 blue socks
(b) no gray socks
(c) at least 1 black sock
(d) a green sock
(e) matching socks
3.25 Chipsinabag. Imagine you have a bag containing 5 red, 3 blue, and 2 orange chips.
(a) Suppose you draw a chip and it is blue. If drawing without replacement, what is the probability the
next is also blue?
(b) Supposeyoudrawachipanditisorange,andthenyoudrawasecondchipwithoutreplacement. What
is the probability this second chip is blue?
(c) If drawing without replacement, what is the probability of drawing two blue chips in a row?
(d) When drawing without replacement, are the draws independent? Explain.
3.26 Books on a bookshelf. The table below shows the distribution of books on a bookcase based on
whether they are nonfiction or fiction and hardcover or paperback.
Format
Hardcover Paperback Total
Fiction 13 59 72
Type
Nonfiction 15 8 23
Total 28 67 95
(a) Find the probability of drawing a hardcover book first then a paperback fiction book second when
drawing without replacement.
(b) Determine the probability of drawing a fiction book first and then a hardcover book second, when
drawing without replacement.
(c) Calculate the probability of the scenario in part (b), except this time complete the calculations under
the scenario where the first book is placed back on the bookcase before randomly drawing the second
book.
(d) The final answers to parts (b) and (c) are very similar. Explain why this is the case.
3.27 Studentoutfits. Inaclassroomwith24students,7studentsarewearingjeans,4arewearingshorts,8
arewearingskirts,andtherestarewearingleggings. Ifwerandomlyselect3studentswithoutreplacement,
what is the probability that one of the selected students is wearing leggings and the other two are wearing
jeans? Note that these are mutually exclusive clothing options.
3.28 Thebirthdayproblem. Supposewepickthreepeopleatrandom. Foreachofthefollowingquestions,
ignore the special case where someone might be born on February 29th, and assume that births are evenly
distributed throughout the year.
(a) What is the probability that the first two people share a birthday?
(b) What is the probability that at least two people share a birthday?
3.4. RANDOM VARIABLES 115
3.4 Random variables
It’softenusefultomodelaprocessusingwhat’scalledarandom variable. Suchamodelallowsus
toapplyamathematicalframeworkandstatisticalprinciplesforbetterunderstandingandpredicting
outcomes in the real world.
EXAMPLE3.54
Two books are assigned for a statistics class: a textbook and its corresponding study guide. The
university bookstore determined 20% of enrolled students do not buy either book, 55% buy the
textbook only, and 25% buy both books, and these percentages are relatively constant from one
term to another. If there are 100 students enrolled, how many books should the bookstore expect
to sell to this class?
Around 20 students will not buy either book (0 books total), about 55 will buy one book (55 books
total), and approximately 25 will buy two books (totaling 50 books for these 25 students). The
bookstore should expect to sell about 105 books for this class.
GUIDEDPRACTICE3.55
Would you be surprised if the bookstore sold slightly more or less than 105 books?49
EXAMPLE3.56
The textbook costs $137 and the study guide $33. How much revenue should the bookstore expect
from this class of 100 students?
About 55 students will just buy a textbook, providing revenue of
$137×55=$7,535
The roughly 25 students who buy both the textbook and the study guide would pay a total of
($137+$33)×25=$170×25=$4,250
Thus, the bookstore should expect to generate about $7,535+$4,250 = $11,785 from these 100
studentsforthisoneclass. However, theremightbesomesampling variability sotheactualamount
may differ by a little bit.
0.4
0.2
0.0
$0 $137 $170
Cost
ytilibaborP
Figure3.18: Probabilitydistributionforthebookstore’srevenuefromonestudent.
The triangle represents the average revenue per student.
49If they sell a little more or a little less, this should not be a surprise. Hopefully Chapter 1 helped make clear
that there is natural variability in observed data. For example, if we would flip a coin 100 times, it will not usually
comeupheadsexactlyhalfthetime,butitwillprobablybeclose.
116 CHAPTER 3. PROBABILITY
EXAMPLE3.57
What is the average revenue per student for this course?
The expected total revenue is $11,785, and there are 100 students. Therefore the expected revenue
per student is $11,785/100=$117.85.
3.4.1 Expectation
We call a variable or process with a numerical outcome a random variable, and we usually
represent this random variable with a capital letter such as X, Y, or Z. The amount of money a
single student will spend on her statistics books is a random variable, and we represent it by X.
RANDOMVARIABLE
A random process or variable with a numerical outcome.
ThepossibleoutcomesofX arelabeledwithacorrespondinglowercaseletterxandsubscripts.
Forexample,wewritex =$0,x =$137,andx =$170,whichoccurwithprobabilities0.20,0.55,
1 2 3
and 0.25. The distribution of X is summarized in Figure 3.18 and Figure 3.19.
i 1 2 3 Total
x $0 $137 $170 –
i
P(X =x ) 0.20 0.55 0.25 1.00
i
Figure 3.19: The probability distribution for the random variable X, representing
the bookstore’s revenue from a single student.
We computed the average outcome of X as $117.85 in Example 3.57. We call this average the
expected value of X, denoted by E(X). The expected value of a random variable is computed by
adding each outcome weighted by its probability:
E(X)=0×P(X =0)+137×P(X =137)+170×P(X =170)
=0×0.20+137×0.55+170×0.25=117.85
EXPECTEDVALUEOFADISCRETERANDOMVARIABLE
If X takes outcomes x , ..., x with probabilities P(X = x ), ..., P(X = x ), the expected
1 k 1 k
value of X is the sum of each outcome multiplied by its corresponding probability:
E(X)=x ×P(X =x )+···+x ×P(X =x )
1 1 k k
k
(cid:88)
= x P(X =x )
i i
i=1
The Greek letter µ may be used in place of the notation E(X).
3.4. RANDOM VARIABLES 117
0 137 170
117.85
Figure 3.20: A weight system representing the probability distribution for X. The
string holds the distribution at the mean to keep the system balanced.
m
Figure 3.21: A continuous distribution can also be balanced at its mean.
Theexpectedvalueforarandomvariablerepresentstheaverageoutcome. Forexample,E(X)=
117.85 represents the average amount the bookstore expects to make from a single student, which
we could also write as µ=117.85.
It is also possible to compute the expected value of a continuous random variable (see Sec-
tion 3.5). However, it requires a little calculus and we save it for a later class.50
In physics, the expectation holds the same meaning as the center of gravity. The distribution
can be represented by a series of weights at each outcome, and the mean represents the balancing
point. This is represented in Figures 3.18 and 3.20. The idea of a center of gravity also expands
to continuous probability distributions. Figure 3.21 shows a continuous probability distribution
balanced atop a wedge placed at the mean.
50µ= (cid:82) xf(x)dxwheref(x)representsafunctionforthedensitycurve.
118 CHAPTER 3. PROBABILITY
3.4.2 Variability in random variables
Suppose you ran the university bookstore. Besides how much revenue you expect to generate,
you might also want to know the volatility (variability) in your revenue.
Thevarianceandstandarddeviationcanbeusedtodescribethevariabilityofarandomvariable.
Section2.1.4introducedamethodforfindingthevarianceandstandarddeviationforadataset. We
first computed deviations from the mean (x −µ), squared those deviations, and took an average to
i
get the variance. In the case of a random variable, we again compute squared deviations. However,
wetaketheirsumweightedbytheircorrespondingprobabilities,justlikewedidfortheexpectation.
Thisweightedsumofsquareddeviationsequalsthevariance,andwecalculatethestandarddeviation
by taking the square root of the variance, just as we did in Section 2.1.4.
GENERALVARIANCEFORMULA
IfX takesoutcomesx ,...,x withprobabilitiesP(X =x ),...,P(X =x )andexpectedvalue
1 k 1 k
µ=E(X), then the variance of X, denoted by Var(X) or the symbol σ2, is
σ2 =(x −µ)2×P(X =x )+···
1 1
···+(x −µ)2×P(X =x )
k k
k
(cid:88)
= (x −µ)2P(X =x )
j j
j=1
The standard deviation of X, labeled σ, is the square root of the variance.
EXAMPLE3.58
Computetheexpectedvalue,variance,andstandarddeviationofX,therevenueofasinglestatistics
student for the bookstore.
It is useful to construct a table that holds computations for each outcome separately, then add up
the results.
i 1 2 3 Total
x $0 $137 $170
i
P(X =x ) 0.20 0.55 0.25
i
x ×P(X =x ) 0 75.35 42.50 117.85
i i
Thus,theexpectedvalueisµ=117.85,whichwecomputedearlier. Thevariancecanbeconstructed
by extending this table:
i 1 2 3 Total
x $0 $137 $170
i
P(X =x ) 0.20 0.55 0.25
i
x ×P(X =x ) 0 75.35 42.50 117.85
i i
x −µ -117.85 19.15 52.15
i
(x −µ)2 13888.62 366.72 2719.62
i
(x −µ)2×P(X =x ) 2777.7 201.7 679.9 3659.3
i i
√
The variance of X is σ2 =3659.3, which means the standard deviation is σ = 3659.3=$60.49.
3.4. RANDOM VARIABLES 119
GUIDEDPRACTICE3.59
The bookstore also offers a chemistry textbook for $159 and a book supplement for $41. From past
experience, they know about 25% of chemistry students just buy the textbook while 60% buy both
the textbook and supplement.51
(a) What proportion of students don’t buy either book? Assume no students buy the supplement
without the textbook.
(b) Let Y represent the revenue from a single student. Write out the probability distribution of
Y, i.e. a table for each outcome and its associated probability.
(c) Compute the expected revenue from a single chemistry student.
(d) Find the standard deviation to describe the variability associated with the revenue from a
single student.
3.4.3 Linear combinations of random variables
So far, we have thought of each variable as being a complete story in and of itself. Sometimes
it is more appropriate to use a combination of variables. For instance, the amount of time a person
spends commuting to work each week can be broken down into several daily commutes. Similarly,
the total gain or loss in a stock portfolio is the sum of the gains and losses in its components.
EXAMPLE3.60
Johntravelstoworkfivedaysaweek. WewilluseX torepresenthistraveltimeonMonday,X to
1 2
represent his travel time on Tuesday, and so on. Write an equation using X , ..., X that represents
1 5
his travel time for the week, denoted by W.
His total weekly travel time is the sum of the five daily values:
W =X +X +X +X +X
1 2 3 4 5
Breaking the weekly travel time W into pieces provides a framework for understanding each source
of randomness and is useful for modeling W.
51(a)100%-25%-60%=15%ofstudentsdonotbuyanybooksfortheclass. Part(b)isrepresentedbythefirst
twolinesinthetablebelow. Theexpectationforpart(c)isgivenasthetotalonthelineyi×P(Y =yi). Theresult
(cid:112)
ofpart(d)isthesquare-rootofthevariancelistedoninthetotalonthelastline: σ= Var(Y)=$69.28.
i(scenario) 1(noBook) 2(textbook) 3(both) Total
yi 0.00 159.00 200.00
P(Y =yi) 0.15 0.25 0.60
yi×P(Y =yi) 0.00 39.75 120.00 E(Y)=159.75
yi−E(Y) -159.75 -0.75 40.25
(yi−E(Y))2 25520.06 0.56 1620.06
(yi−E(Y))2×P(Y) 3828.0 0.1 972.0 Var(Y)≈4800
120 CHAPTER 3. PROBABILITY
EXAMPLE3.61
It takes John an average of 18 minutes each day to commute to work. What would you expect his
average commute time to be for the week?
We were told that the average (i.e. expected value) of the commute time is 18 minutes per day:
E(X ) = 18. To get the expected time for the sum of the five days, we can add up the expected
i
time for each individual day:
E(W)=E(X +X +X +X +X )
1 2 3 4 5
=E(X )+E(X )+E(X )+E(X )+E(X )
1 2 3 4 5
=18+18+18+18+18=90 minutes
The expectation of the total time is equal to the sum of the expected individual times. More
generally, the expectation of a sum of random variables is always the sum of the expectation for
each random variable.
GUIDEDPRACTICE3.62
Elena is selling a TV at a cash auction and also intends to buy a toaster oven in the auction. If
X represents the profit for selling the TV and Y represents the cost of the toaster oven, write an
equation that represents the net change in Elena’s cash.52
GUIDEDPRACTICE3.63
Based on past auctions, Elena figures she should expect to make about $175 on the TV and pay
about $23 for the toaster oven. In total, how much should she expect to make or spend?53
GUIDEDPRACTICE3.64
WouldyoubesurprisedifJohn’sweeklycommutewasn’texactly90minutesorifElenadidn’tmake
exactly $152? Explain.54
Two important concepts concerning combinations of random variables have so far been in-
troduced. First, a final value can sometimes be described as the sum of its parts in an equation.
Second, intuition suggests that putting the individual average values into this equation gives the
average value we would expect in total. This second point needs clarification – it is guaranteed to
be true in what are called linear combinations of random variables.
A linear combination of two random variables X and Y is a fancy phrase to describe a
combination
aX+bY
whereaandbaresomefixedandknownnumbers. ForJohn’scommutetime,therewerefiverandom
variables – one for each work day – and each random variable could be written as having a fixed
coefficient of 1:
1X +1X +1X +1X +1X
1 2 3 4 5
For Elena’s net gain or loss, the X random variable had a coefficient of +1 and the Y random
variable had a coefficient of -1.
52ShewillmakeX dollarsontheTVbutspendY dollarsonthetoasteroven: X−Y.
53E(X−Y)=E(X)−E(Y)=175−23=$152. Sheshouldexpecttomakeabout$152.
54No,sincethereisprobablysomevariability. Forexample,thetrafficwillvaryfromonedaytonext,andauction
priceswillvarydependingonthequalityofthemerchandiseandtheinterestoftheattendees.
3.4. RANDOM VARIABLES 121
When considering the average of a linear combination of random variables, it is safe to plug
in the mean of each random variable and then compute the final result. For a few examples of
nonlinearcombinationsofrandomvariables–caseswherewecannotsimplypluginthemeans–see
the footnote.55
LINEARCOMBINATIONSOFRANDOMVARIABLESANDTHEAVERAGERESULT
IfX andY arerandomvariables, thenalinearcombinationoftherandomvariablesisgivenby
aX+bY
where a and b are some fixed numbers. To compute the average value of a linear combination
of random variables, plug in the average of each individual random variable and compute the
result:
a×E(X)+b×E(Y)
Recall that the expected value is the same as the mean, e.g. E(X)=µ .
X
EXAMPLE3.65
Leonard has invested $6000 in Caterpillar Inc (stock ticker: CAT) and $2000 in Exxon Mobil Corp
(XOM). If X represents the change in Caterpillar’s stock next month and Y represents the change
inExxonMobil’sstocknextmonth,writeanequationthatdescribeshowmuchmoneywillbemade
or lost in Leonard’s stocks for the month.
For simplicity, we will suppose X and Y are not in percents but are in decimal form (e.g. if
Caterpillar’s stock increases 1%, then X = 0.01; or if it loses 1%, then X = −0.01). Then we can
write an equation for Leonard’s gain as
$6000×X+$2000×Y
If we plug in the change in the stock value for X and Y, this equation gives the change in value of
Leonard’s stock portfolio for the month. A positive value represents a gain, and a negative value
represents a loss.
GUIDEDPRACTICE3.66
Caterpillarstockhasrecentlybeenrisingat2.0%andExxonMobil’sat0.2%permonth,respectively.
Compute the expected change in Leonard’s stock portfolio for next month.56
GUIDEDPRACTICE3.67
You should have found that Leonard expects a positive gain in Guided Practice 3.66. However,
would you be surprised if he actually had a loss this month?57
55If X and Y are random variables, consider the following combinations: X1+Y, X×Y, X/Y. In such cases,
pluggingintheaveragevalueforeachrandomvariableandcomputingtheresultwillnotgenerallyleadtoanaccurate
averagevaluefortheendresult.
56E($6000×X+$2000×Y)=$6000×0.020+$2000×0.002=$124.
57No. Whilestockstendtoriseovertime,theyareoftenvolatileintheshortterm.
122 CHAPTER 3. PROBABILITY
3.4.4 Variability in linear combinations of random variables
Quantifying the average outcome from a linear combination of random variables is helpful, but
it is also important to have some sense of the uncertainty associated with the total outcome of that
combination of random variables. The expected net gain or loss of Leonard’s stock portfolio was
considered in Guided Practice 3.66. However, there was no quantitative discussion of the volatility
of this portfolio. For instance, while the average monthly gain might be about $124 according to
the data, that gain is not guaranteed. Figure 3.22 shows the monthly changes in a portfolio like
Leonard’s during a three year period. The gains and losses vary widely, and quantifying these
fluctuations is important when investing in stocks.
−1000 −500 0 500 1000
Monthly Returns Over 3 Years
Figure 3.22: The change in a portfolio like Leonard’s for 36 months, where $6000
is in Caterpillar’s stock and $2000 is in Exxon Mobil’s.
Just as we have done in many previous cases, we use the variance and standard deviation to
describe the uncertainty associated with Leonard’s monthly returns. To do so, the variances of each
stock’s monthly return will be useful, and these are shown in Figure 3.23. The stocks’ returns are
nearly independent.
Here we use an equation from probability theory to describe the uncertainty of Leonard’s
monthly returns; we leave the proof of this method to a dedicated probability course. The variance
of a linear combination of random variables can be computed by plugging in the variances of the
individual random variables and squaring the coefficients of the random variables:
Var(aX+bY)=a2×Var(X)+b2×Var(Y)
It is important to note that this equality assumes the random variables are independent; if inde-
pendence doesn’t hold, then a modification to this equation would be required that we leave as a
topic for a future course to cover. This equation can be used to compute the variance of Leonard’s
monthly return:
Var(6000×X+2000×Y)=60002×Var(X)+20002×Var(Y)
=36,000,000×0.0057+4,000,000×0.0021
≈213,600
√
Thestandarddeviationiscomputedasthesquarerootofthevariance: 213,600=$463. Whilean
average monthly return of $124 on an $8000 investment is nothing to scoff at, the monthly returns
are so volatile that Leonard should not expect this income to be very stable.
Mean (x¯) Standard deviation (s) Variance (s2)
CAT 0.0204 0.0757 0.0057
XOM 0.0025 0.0455 0.0021
Figure 3.23: The mean, standard deviation, and variance of the CAT and XOM
stocks. Thesestatisticswereestimatedfromhistoricalstockdata,sonotationused
for sample statistics has been used.
3.4. RANDOM VARIABLES 123
VARIABILITYOFLINEARCOMBINATIONSOFRANDOMVARIABLES
The variance of a linear combination of random variables may be computed by squaring the
constants, substituting in the variances for the random variables, and computing the result:
Var(aX+bY)=a2×Var(X)+b2×Var(Y)
This equation is valid as long as the random variables are independent of each other. The
standard deviation of the linear combination may be found by taking the square root of the
variance.
EXAMPLE3.68
Suppose John’s daily commute has a standard deviation of 4 minutes. What is the uncertainty in
his total commute time for the week?
The expression for John’s commute time was
X +X +X +X +X
1 2 3 4 5
Each coefficient is 1, and the variance of each day’s time is 42 =16. Thus, the variance of the total
weekly commute time is
variance =12×16+12×16+12×16+12×16+12×16=5×16=80
√ √
standard deviation = variance= 80=8.94
The standard deviation for John’s weekly work commute time is about 9 minutes.
GUIDEDPRACTICE3.69
The computation in Example 3.68 relied on an important assumption: the commute time for each
day is independent of the time on other days of that week. Do you think this is valid? Explain.58
GUIDEDPRACTICE3.70
Consider Elena’s two auctions from Guided Practice 3.62 on page 120. Suppose these auctions are
approximately independent and the variability in auction prices associated with the TV and toaster
oven can be described using standard deviations of $25 and $8. Compute the standard deviation of
Elena’s net gain.59
Consider again Guided Practice 3.70. The negative coefficient for Y in the linear combination
was eliminated when we squared the coefficients. This generally holds true: negatives in a linear
combination will have no impact on the variability computed for a linear combination, but they do
impact the expected value computations.
58Oneconcerniswhethertrafficpatternstendtohaveaweeklycycle(e.g. Fridaysmaybeworsethanotherdays).
Ifthatisthecase,andJohndrives,thentheassumptionisprobablynotreasonable. However,ifJohnwalkstowork,
thenhiscommuteisprobablynotaffectedbyanyweeklytrafficcycle.
59TheequationforElenacanbewrittenas
(1)×X+(−1)×Y
ThevariancesofX andY are625and64. Wesquarethecoefficientsandpluginthevariances:
(1)2×Var(X)+(−1)2×Var(Y)=1×625+1×64=689
Thevarianceofthelinearcombinationis689,andthestandarddeviationisthesquarerootof689: about$26.25.
124 CHAPTER 3. PROBABILITY
Exercises
3.29 Collegesmokers. At a university, 13% of students smoke.
(a) Calculate the expected number of smokers in a random sample of 100 students from this university.
(b) The university gym opens at 9 am on Saturday mornings. One Saturday morning at 8:55 am there are
27studentsoutsidethegymwaitingforittoopen. Shouldyouusethesameapproachfrompart(a)to
calculate the expected number of smokers among these 27 students?
3.30 Aceofclubswins. Consider the following card game with a well-shuffled deck of cards. If you draw
a red card, you win nothing. If you get a spade, you win $5. For any club, you win $10 plus an extra $20
for the ace of clubs.
(a) Create a probability model for the amount you win at this game. Also, find the expected winnings for
a single game and the standard deviation of the winnings.
(b) Whatisthemaximumamountyouwouldbewillingtopaytoplaythisgame? Explainyourreasoning.
3.31 Heartswin. In a new card game, you start with a well-shuffled full deck and draw 3 cards without
replacement. If you draw 3 hearts, you win $50. If you draw 3 black cards, you win $25. For any other
draws, you win nothing.
(a) Createa probabilitymodel fortheamountyouwinatthisgame, and findtheexpectedwinnings. Also
compute the standard deviation of this distribution.
(b) Ifthegamecosts$5toplay,whatwouldbetheexpectedvalueandstandarddeviationofthenetprofit
(or loss)? (Hint: profit = winnings − cost; X−5)
(c) If the game costs $5 to play, should you play this game? Explain.
3.32 Isitworthit? Andy is always looking for ways to make money fast. Lately, he has been trying to
makemoneybygambling. Hereisthegameheisconsideringplaying: Thegamecosts$2toplay. Hedraws
a card from a deck. If he gets a number card (2-10), he wins nothing. For any face card ( jack, queen or
king), he wins $3. For any ace, he wins $5, and he wins an extra $20 if he draws the ace of clubs.
(a) Create a probability model and find Andy’s expected profit per game.
(b) Would you recommend this game to Andy as a good way to make money? Explain.
3.33 Portfolio return. A portfolio’s value increases by 18% during a financial boom and by 9% during
normal times. It decreases by 12% duringa recession. What is the expected return on this portfolio if each
scenario is equally likely?
3.34 Baggagefees. An airline charges the following baggage fees: $25 for the first bag and $35 for the
second. Suppose 54% of passengers have no checked luggage, 34% have one piece of checked luggage and
12% have two pieces. We suppose a negligible portion of people check more than two bags.
(a) Buildaprobabilitymodel,computetheaveragerevenueperpassenger,andcomputethecorresponding
standard deviation.
(b) About how much revenue should the airline expect for a flight of 120 passengers? With what standard
deviation? Note any assumptions you make and if you think they are justified.
3.35 Americanroulette. The game of American roulette involves spinning a wheel with 38 slots: 18 red,
18 black, and 2 green. A ball is spun onto the wheel and will eventually land in a slot, where each slot has
an equal chance of capturing the ball. Gamblers can place bets on red or black. If the ball lands on their
color, they double their money. If it lands on another color, they lose their money. Suppose you bet $1 on
red. What’s the expected value and standard deviation of your winnings?
3.36 Europeanroulette. The game of European roulette involves spinning a wheel with 37 slots: 18 red,
18 black, and 1 green. A ball is spun onto the wheel and will eventually land in a slot, where each slot has
an equal chance of capturing the ball. Gamblers can place bets on red or black. If the ball lands on their
color, they double their money. If it lands on another color, they lose their money.
(a) Suppose you play roulette and bet $3 on a single round. What is the expected value and standard
deviation of your total winnings?
(b) Suppose you bet $1 in three different rounds. What is the expected value and standard deviation of
your total winnings?
(c) How do your answers to parts (a) and (b) compare? What does this say about the riskiness of the two
games?
3.5. CONTINUOUS DISTRIBUTIONS 125
3.5 Continuous distributions
So far in this chapter we’ve discussed cases where the outcome of a variable is discrete. In this
section, we consider a context where the outcome is a continuous numerical variable.
EXAMPLE3.71
Figure3.24showsafewdifferenthollowhistogramsfortheheightsofUSadults. Howdoeschanging
the number of bins allow you to make different interpretations of the data?
Addingmorebinsprovidesgreaterdetail. Thissampleisextremelylarge,whichiswhymuchsmaller
binsstillworkwell. Usuallywedonotusesomanybinswithsmallersamplesizessincesmallcounts
per bin mean the bin heights are very volatile.
140 160 180 200
height (cm) height (cm)
ycneuqerf
140 160 180 200
140 160 180 200
height (cm) height (cm)
ycneuqerf
140 160 180 200
Figure3.24: FourhollowhistogramsofUSadultsheightswithvaryingbinwidths.
EXAMPLE3.72
What proportion of the sample is between 180 cm and 185 cm tall (about 5’11” to 6’1”)?
We can add up the heights of the bins in the range 180 cm and 185 and divide by the sample size.
For instance, this can be done with the two shaded bins shown in Figure 3.25. The two bins in
this region have counts of 195,307 and 156,239 people, resulting in the following estimate of the
probability:
195307+156239
=0.1172
3,000,000
Thisfractionisthesameastheproportionofthehistogram’sareathatfallsintherange180to185
cm.
126 CHAPTER 3. PROBABILITY
140 160 180 200
height (cm)
Figure 3.25: A histogram with bin sizes of 2.5 cm. The shaded region represents
individuals with heights between 180 and 185 cm.
3.5.1 From histograms to continuous distributions
Examinethetransitionfromaboxyhollowhistograminthetop-leftofFigure3.24tothemuch
smoother plot in the lower-right. In this last plot, the bins are so slim that the hollow histogram is
startingtoresembleasmoothcurve. Thissuggeststhepopulationheightasacontinuous numerical
variable might best be explained by a curve that represents the outline of extremely slim bins.
This smooth curve represents a probability density function (also called a density or
distribution), and such a curve is shown in Figure 3.26 overlaid on a histogram of the sample. A
density has a special property: the total area under the density’s curve is 1.
140 160 180 200
height (cm)
Figure 3.26: The continuous probability distribution of heights for US adults.
3.5. CONTINUOUS DISTRIBUTIONS 127
3.5.2 Probabilities from continuous distributions
We computed the proportion of individuals with heights 180 to 185 cm in Example 3.72 as a
fraction:
number of people between 180 and 185
total sample size
We found the number of people with heights between 180 and 185 cm by determining the fraction
of the histogram’s area in this region. Similarly, we can use the area in the shaded region under the
curve to find a probability (with the help of a computer):
P(height between 180 and 185)=area between 180 and 185=0.1157
The probability that a randomly selected person is between 180 and 185 cm is 0.1157. This is very
close to the estimate from Example 3.72: 0.1172.
140 160 180 200
height (cm)
Figure 3.27: Density for heights in the US adult population with the area between
180 and 185 cm shaded. Compare this plot with Figure 3.25.
GUIDEDPRACTICE3.73
Three US adults are randomly selected. The probability a single adult is between 180 and 185 cm
is 0.1157.60
(a) What is the probability that all three are between 180 and 185 cm tall?
(b) What is the probability that none are between 180 and 185 cm?
EXAMPLE3.74
What is the probability that a randomly selected person is exactly 180 cm? Assume you can
measure perfectly.
This probability is zero. A person might be close to 180 cm, but not exactly 180 cm tall. This also
makes sense with the definition of probability as area; there is no area captured between 180 cm
and 180 cm.
GUIDEDPRACTICE3.75
Suppose a person’s height is rounded to the nearest centimeter. Is there a chance that a random
person’s measured height will be 180 cm?61
60Briefanswers: (a)0.1157×0.1157×0.1157=0.0015. (b)(1−0.1157)3=0.692
61Thishaspositiveprobability. Anyonebetween179.5cmand180.5cmwillhaveameasured heightof 180cm.
ThisisprobablyamorerealisticscenariotoencounterinpracticeversusExample3.74.
128 CHAPTER 3. PROBABILITY
Exercises
3.37 Catweights. The histogram shown below represents the weights (in kg) of 47 female and 97 male
cats.62
(a) Whatfractionofthesecatsweighlessthan2.5
kg?
(b) What fraction of these cats weigh between 2.5
and 2.75 kg?
(c) Whatfractionofthesecatsweighbetween2.75
and 3.5 kg?
Body weight
ycneuqerF
30
20
10
0
2.0 2.5 3.0 3.5 4.0
3.38 Income and gender. The relative frequency table below displays the distribution of annual total
personal income (in 2009 inflation-adjusted dollars) for a representative sample of 96,420,486 Americans.
These data come from the American Community Survey for 2005-2009. This sample is comprised of 59%
males and 41% females.63
(a) Describe the distribution of total personal income. Income Total
$1 to $9,999 or loss 2.2%
(b) WhatistheprobabilitythatarandomlychosenUSresident
makes less than $50,000 per year? $10,000 to $14,999 4.7%
$15,000 to $24,999 15.8%
(c) WhatistheprobabilitythatarandomlychosenUSresident $25,000 to $34,999 18.3%
makes less than $50,000 per year and is female? Note any $35,000 to $49,999 21.2%
assumptions you make. $50,000 to $64,999 13.9%
(d) The same data source indicates that 71.8% of females make $65,000 to $74,999 5.8%
less than $50,000 per year. Use this value to determine $75,000 to $99,999 8.4%
whetherornottheassumptionyoumadeinpart(c)isvalid. $100,000 or more 9.7%
62W. N. Venables and B. D. Ripley. Modern Applied Statistics with S. Fourth Edition.
www.stats.ox.ac.uk/pub/MASS4. NewYork: Springer,2002.
63U.S.CensusBureau,2005-2009AmericanCommunitySurvey.
3.5. CONTINUOUS DISTRIBUTIONS 129
Chapter exercises
3.39 Gradedistributions. Eachrowinthetablebelowisaproposedgradedistributionforaclass. Identify
each as a valid or invalid probability distribution, and explain your reasoning.
Grades
A B C D F
(a) 0.3 0.3 0.3 0.2 0.1
(b) 0 0 1 0 0
(c) 0.3 0.3 0.3 0 0
(d) 0.3 0.5 0.2 0.1 -0.1
(e) 0.2 0.4 0.2 0.1 0.1
(f) 0 -0.1 1.1 0 0
3.40 Health coverage, frequencies. The Behavioral Risk Factor Surveillance System (BRFSS) is an
annualtelephonesurveydesignedtoidentifyriskfactorsintheadultpopulationandreportemerginghealth
trends. Thefollowingtablesummarizestwovariablesfortherespondents: healthstatusandhealthcoverage,
which describes whether each respondent had health insurance.64
Health Status
Excellent Very good Good Fair Poor Total
Health No 459 727 854 385 99 2,524
Coverage Yes 4,198 6,245 4,821 1,634 578 17,476
Total 4,657 6,972 5,675 2,019 677 20,000
(a) If we draw one individual at random, what is the probability that the respondent has excellent health
and doesn’t have health coverage?
(b) If we draw one individual at random, what is the probability that the respondent has excellent health
or doesn’t have health coverage?
3.41 HIVinSwaziland. Swaziland has the highest HIV prevalence in the world: 25.9% of this country’s
population is infected with HIV.65 The ELISA test is one of the first and most accurate tests for HIV. For
thosewhocarryHIV,theELISAtestis99.7%accurate. ForthosewhodonotcarryHIV,thetestis92.6%
accurate. If an individual from Swaziland has tested positive, what is the probability that he carries HIV?
3.42 Twins. About 30% of human twins are identical, and the rest are fraternal. Identical twins are
necessarily the same sex – half are males and the other half are females. One-quarter of fraternal twins are
bothmale,one-quarterbothfemale,andone-halfaremixes: onemale,onefemale. Youhavejustbecomea
parent of twins and are told they are both girls. Given this information, what is the probability that they
are identical?
3.43 Costofbreakfast. Sally gets a cup of coffee and a muffin every day for breakfast from one of the
manycoffeeshopsinherneighborhood. Shepicksacoffeeshopeachmorningatrandomandindependently
of previous days. The average price of a cup of coffee is $1.40 with a standard deviation of 30¢ ($0.30), the
average price of a muffin is $2.50 with a standard deviation of 15¢, and the two prices are independent of
each other.
(a) What is the mean and standard deviation of the amount she spends on breakfast daily?
(b) What is the mean and standard deviation of the amount she spends on breakfast weekly (7 days)?
64OfficeofSurveillance,Epidemiology,andLaboratoryServicesBehavioralRiskFactorSurveillanceSystem,BRFSS
2010SurveyData.
65Source: CIAFactbook,CountryComparison: HIV/AIDS-AdultPrevalenceRate.
130 CHAPTER 3. PROBABILITY
3.44 Scoopingicecream. Ice cream usually comes in 1.5 quart boxes (48 fluid ounces), and ice cream
scoops hold about 2 ounces. However, there is some variability in the amount of ice cream in a box as well
as the amount of ice cream scooped out. We represent the amount of ice cream in the box as X and the
amount scooped out as Y. Suppose these random variables have the following means, standard deviations,
and variances:
mean SD variance
X 48 1 1
Y 2 0.25 0.0625
(a) An entire box of ice cream, plus 3 scoops from a second box is served at a party. How much ice cream
do you expect to have been served at this party? What is the standard deviation of the amount of ice
cream served?
(b) How much ice cream would you expect to be left in the box after scooping out one scoop of ice cream?
That is, find the expected value of X −Y. What is the standard deviation of the amount left in the
box?
(c) Usingthecontextofthisexercise,explainwhyweaddvarianceswhenwesubtractonerandomvariable
from another.
3.45 Varianceofamean,PartI.SupposewehaveindependentobservationsX andX fromadistribution
1 2
with mean µ and standard deviation σ. What is the variance of the mean of the two values: X1+X2?
2
3.46 Variance of a mean, Part II. Suppose we have 3 independent observations X , X , X from a dis-
1 2 3
tribution with mean µ and standard deviation σ. What is the variance of the mean of these 3 values:
X1+X2+X3?
3
3.47 Variance of a mean, Part III. Suppose we have n independent observations X , X , ..., X from a
1 2 n
distribution with mean µ and standard deviation σ. What is the variance of the mean of these n values:
X1+X2+···+Xn?
n
131
Chapter 4
Distributions of random
variables
4.1 Normal distribution
4.2 Geometric distribution
4.3 Binomial distribution
4.4 Negative binomial distribution
4.5 Poisson distribution
132
In this chapter, we discuss statistical distributions that frequently arise
in the context of data analysis or statistical inference. We start with
the normal distribution in the first section, which is used frequently in
later chapters of this book. The remaining sections will occasionally be
referenced but may be considered optional for the content in this book.
For videos, slides, and other resources, please visit
www.openintro.org/os
4.1. NORMAL DISTRIBUTION 133
4.1 Normal distribution
Among all the distributions we see in practice, one is overwhelmingly the most common. The
symmetric, unimodal, bell curve is ubiquitous throughout statistics. Indeed it is so common, that
peopleoftenknowitasthenormalcurveornormaldistribution,1 showninFigure4.1. Variables
such as SAT scores and heights of US adult males closely follow the normal distribution.
Figure 4.1: A normal curve.
NORMALDISTRIBUTIONFACTS
Many variables are nearly normal, but none are exactly normal. Thus the normal distribution,
while not perfect for any single problem, is very useful for a variety of problems. We will use it
in data exploration and to solve important problems in statistics.
4.1.1 Normal distribution model
The normal distribution always describes a symmetric, unimodal, bell-shaped curve. How-
ever, these curves can look different depending on the details of the model. Specifically, the normal
distribution model can be adjusted using two parameters: mean and standard deviation. As you
can probably guess, changing the mean shifts the bell curve to the left or right, while changing the
standard deviation stretches or constricts the curve. Figure 4.2 shows the normal distribution with
mean 0 and standard deviation 1 in the left panel and the normal distributions with mean 19 and
standard deviation 4 in the right panel. Figure 4.3 shows these distributions on the same axis.
−3 −2 −1 0 1 2 3
Y
7 11 15 19 23 27 31
Figure 4.2: Both curves represent the normal distribution. However, they differ in
their center and spread.
If a normal distribution has mean µ and standard deviation σ, we may write the distribution
as N(µ,σ). The two distributions in Figure 4.3 may be written as
N(µ=0,σ =1) and N(µ=19,σ =4)
Because the mean and standard deviation describe a normal distribution exactly, they are called
the distribution’s parameters. The normal distribution with mean µ = 0 and standard deviation
σ =1 is called the standard normal distribution.
1It is also introduced as the Gaussian distribution after Frederic Gauss, the first person to formalize its mathe-
maticalexpression.
134 CHAPTER 4. DISTRIBUTIONS OF RANDOM VARIABLES
0 10 20 30
Figure4.3: ThenormaldistributionsshowninFigure4.2butplottedtogetherand
on the same scale.
GUIDEDPRACTICE4.1
Write down the short-hand for a normal distribution with2
(a) mean 5 and standard deviation 3,
(b) mean -100 and standard deviation 10, and
(c) mean 2 and standard deviation 9.
4.1.2 Standardizing with Z-scores
Weoftenwanttoputdataontoastandardizedscale,whichcanmakecomparisonsmorereasonable.
EXAMPLE4.2
Table 4.4 shows the mean and standard deviation for total scores on the SAT and ACT. The
distribution of SAT and ACT scores are both nearly normal. Suppose Ann scored 1300 on her SAT
and Tom scored 24 on his ACT. Who performed better?
We use the standard deviation as a guide. Ann is 1 standard deviation above average on the SAT:
1100+200=1300. Tom is 0.5 standard deviations above the mean on the ACT: 21+0.5×6=24.
In Figure 4.5, we can see that Ann tends to do better with respect to everyone else than Tom did,
so her score was better.
SAT ACT
Mean 1100 21
SD 200 6
Figure 4.4: Mean and standard deviation for the SAT and ACT.
Example 4.2 used a standardization technique called a Z-score, a method most commonly
employed for nearly normal observations but that may be used with any distribution. The Z-score
of an observation is defined as the number of standard deviations it falls above or below the mean.
If the observation is one standard deviation above the mean, its Z-score is 1. If it is 1.5 standard
deviationsbelow themean,thenitsZ-scoreis-1.5. IfxisanobservationfromadistributionN(µ,σ),
we define the Z-score mathematically as
x−µ
Z =
σ
Using µ =1100, σ =200, and x =1300, we find Ann’s Z-score:
SAT SAT Ann
x −µ 1300−1100
Z = Ann SAT = =1
Ann σ 200
SAT
2(a)N(µ=5,σ=3). (b)N(µ=−100,σ=10). (c)N(µ=2,σ=9).
4.1. NORMAL DISTRIBUTION 135
Ann
700 900 1100 1300 1500
X
Tom
9 15 21 27 33
Figure4.5: Ann’sandTom’sscoresshownagainsttheSATandACTdistributions.
THEZ-SCORE
The Z-score of an observation is the number of standard deviations it falls above or below the
mean. We compute the Z-score for an observation x that follows a distribution with mean µ
and standard deviation σ using
x−µ
Z =
σ
GUIDEDPRACTICE4.3
Use Tom’s ACT score, 24, along with the ACT mean and standard deviation to find his Z-score.3
ObservationsabovethemeanalwayshavepositiveZ-scores,whilethosebelowthemeanalways
have negative Z-scores. If an observation is equal to the mean, such as an SAT score of 1100, then
the Z-score is 0.
GUIDEDPRACTICE4.4
Let X represent a random variable from N(µ=3,σ =2), and suppose we observe x=5.19.
(a) Find the Z-score of x.
(b) Use the Z-score to determine how many standard deviations above or below the mean x falls.4
GUIDEDPRACTICE4.5
Head lengths of brushtail possums follow a normal distribution with mean 92.6 mm and standard
deviation3.6mm. ComputetheZ-scoresforpossumswithheadlengthsof95.4mmand85.8mm.5
We can use Z-scores to roughly identify which observations are more unusual than others. An
observation x is said to be more unusual than another observation x if the absolute value of its Z-
1 2
scoreislargerthantheabsolutevalueoftheotherobservation’sZ-score: |Z |>|Z |. Thistechnique
1 2
is especially insightful when a distribution is symmetric.
GUIDEDPRACTICE4.6
Which of the observations in Guided Practice 4.5 is more unusual?6
3ZTom= xTom
σA
−
C
µ
T
ACT = 24−
6
21 =0.5
4(a) Its Z-score is given by Z = x−µ = 5.19−3 = 2.19/2 = 1.095. (b) The observation x is 1.095 standard
σ 2
deviationsabove themean. WeknowitmustbeabovethemeansinceZ ispositive.
5Forx1=95.4mm: Z1= x1
σ
−µ = 95.4
3
−
.6
92.6 =0.78. Forx2=85.8mm: Z2= 85.8
3
−
.6
92.6 =−1.89.
6Because the absolute value of Z-score for the second observation is larger than that of the first, the second
observationhasamoreunusualheadlength.
136 CHAPTER 4. DISTRIBUTIONS OF RANDOM VARIABLES
4.1.3 Finding tail areas
It’s very useful in statistics to be able to identify tail areas of distributions. For instance, what
fractionofpeoplehaveanSATscorebelowAnn’sscoreof1300? Thisisthesameasthepercentile
Ann is at, which is the percentage of cases that have lower scores than Ann. We can visualize such
a tail area like the curve and shading shown in Figure 4.6.
500 700 900 1100 1300 1500 1700
Figure 4.6: The area to the left of Z represents the fraction of people who scored
lower than Ann.
There are many techniques for doing this, and we’ll discuss three of the options.
1. The most common approach in practice is to use statistical software. For example, in the
program R, we could find the area shown in Figure 4.6 using the following command, which
takes in the Z-score and returns the lower tail area:
.....> pnorm(1)
.....[1] 0.8413447
According to this calculation, the region shaded that is below 1300 represents the proportion
0.841 (84.1%) of SAT test takers who had Z-scores below Z =1. More generally, we can also
specify the cutoff explicitly if we also note the mean and standard deviation:
.....> pnorm(1300, mean = 1100, sd = 200)
.....[1] 0.8413447
There are many other software options, such as Python or SAS; even spreadsheet programs
such as Excel and Google Sheets support these calculations.
2. Acommonstrategyinclassroomsistouseagraphingcalculator,suchasaTIorCasiocalcula-
tor. These calculators require a series of button presses that are less concisely described. You
can find instructions on using these calculators for finding tail areas of a normal distribution
in the OpenIntro video library:
www.openintro.org/videos
3. The last option for finding tail areas is to use what’s called a probability table; these are
occasionallyusedinclassroomsbutrarelyinpractice. AppendixC.1containssuchatableand
a guide for how to use it.
We will solve normal distribution problems in this section by always first finding the Z-score. The
reason is that we will encounter close parallels called test statistics beginning in Chapter 5; these
are, in many instances, an equivalent of a Z-score.
4.1. NORMAL DISTRIBUTION 137
4.1.4 Normal probability examples
Cumulative SAT scores are approximated well by a normal model, N(µ=1100,σ =200).
EXAMPLE4.7
Shannon is a randomly selected SAT taker, and nothing is known about Shannon’s SAT aptitude.
What is the probability Shannon scores at least 1190 on her SATs?
First, always draw and label a picture of the normal distribution. (Drawings need not be exact to
be useful.) We are interested in the chance she scores above 1190, so we shade this upper tail:
700 1100 1500
The picture shows the mean and the values at 2 standard deviations above and below the mean.
The simplest way to find the shaded area under the curve makes use of the Z-score of the cutoff
value. With µ=1100, σ =200, and the cutoff value x=1190, the Z-score is computed as
x−µ 1190−1100 90
Z = = = =0.45
σ 200 200
Using statistical software (or another preferred method), we can find the area left of Z = 0.45 as
0.6736. To find the area above Z =0.45, we compute one minus the area of the lower tail:
1.0000 0.6736 = 0.3264
The probability Shannon scores at least 1190 on the SAT is 0.3264.
ALWAYSDRAWAPICTUREFIRST,ANDFINDTHEZ-SCORESECOND
For any normal probability situation, always always always draw and label the normal curve
and shade the area of interest first. The picture will provide an estimate of the probability.
After drawing a figure to represent the situation, identify the Z-score for the value of interest.
GUIDEDPRACTICE4.8
If the probability of Shannon scoring at least 1190 is 0.3264, then what is the probability she scores
less than 1190? Draw the normal curve representing this exercise, shading the lower region instead
of the upper one.7
7WefoundthisprobabilityinExample4.7: 0.6736.
700 1100 1500
138 CHAPTER 4. DISTRIBUTIONS OF RANDOM VARIABLES
EXAMPLE4.9
Edward earned a 1030 on his SAT. What is his percentile?
First, a picture is needed. Edward’s percentile is the proportion of people who do not get as high
as a 1030. These are the scores to the left of 1030.
700 1100 1500
Identifying the mean µ = 1100, the standard deviation σ = 200, and the cutoff for the tail area
x=1030 makes it easy to compute the Z-score:
x−µ 1030−1100
Z = = =−0.35
σ 200
Using statistical software, we get a tail area of 0.3632. Edward is at the 36th percentile.
GUIDEDPRACTICE4.10
UsetheresultsofExample4.9tocomputetheproportionofSATtakerswhodidbetterthanEdward.
Also draw a new picture.8
FINDINGAREASTOTHERIGHT
Many software programs return the area to the left when given a Z-score. If you would like the
area to the right, first find the area to the left and then subtract this amount from one.
GUIDEDPRACTICE4.11
Stuart earned an SAT score of 1500. Draw a picture for each part.
(a) What is his percentile?
(b) What percent of SAT takers did better than Stuart?9
Basedonasampleof100men,theheightsofmaleadultsintheUSisnearlynormalwithmean
70.0” and standard deviation 3.3”.
GUIDEDPRACTICE4.12
Mike is 5’7” and Jose is 6’4”, and they both live in the US.
(a) What is Mike’s height percentile?
(b) What is Jose’s height percentile?
Also draw one picture for each part.10
8IfEdwarddidbetterthan36%ofSATtakers,thenabout64%musthavedonebetterthanhim.
700 1100 1500
9Weleavethedrawingstoyou. (a)Z= 1500−1100 =2→0.9772. (b)1−0.9772=0.0228.
200
10Firstputtheheightsintoinches: 67and76inches. Figuresareshownbelow.
(a)Z
Mike
= 67
3
−
.3
70 =−0.91 → 0.1814. (b)ZJose= 76
3
−
.3
70 =1.82 → 0.9656.
Mike Jose
67 70 70 76
4.1. NORMAL DISTRIBUTION 139
The last several problems have focused on finding the percentile (lower tail) or the upper tail
for a particular observation. What if you would like to know the observation corresponding to a
particular percentile?
EXAMPLE4.13
Erik’s height is at the 40th percentile. How tall is he?
As always, first draw the picture.
40%
(0.40)
63.4 70 76.6
Inthiscase,thelowertailprobabilityisknown(0.40),whichcanbeshadedonthediagram. Wewant
tofindtheobservationthatcorrespondstothisvalue. Asafirststepinthisdirection, wedetermine
the Z-score associated with the 40th percentile. Using software, we can obtain the corresponding
Z-score of about -0.25.
Knowing Z = −0.25 and the population parameters µ = 70 and σ = 3.3 inches, the Z-score
Erik
formula can be set up to determine Erik’s unknown height, labeled x :
Erik
x −µ x −70
−0.25=Z = Erik = Erik
Erik σ 3.3
Solving for x yields a height of 69.18 inches. That is, Erik is about 5’9”.
Erik
EXAMPLE4.14
What is the adult male height at the 82nd percentile?
Again, we draw the figure first.
18%
82% (0.18)
(0.82)
63.4 70 76.6
Next, we want to find the Z-score at the 82nd percentile, which will be a positive value and can be
found using software as Z =0.92. Finally, the height x is found using the Z-score formula with the
known mean µ, standard deviation σ, and Z-score Z =0.92:
x−µ x−70
0.92=Z = =
σ 3.3
This yields 73.04 inches or about 6’1” as the height at the 82nd percentile.
GUIDEDPRACTICE4.15
The SAT scores follow N(1100,200).11
(a) What is the 95th percentile for SAT scores?
(b) What is the 97.5th percentile for SAT scores?
11Shortanswers: (a)Z95=1.6449→1429SATscore. (b)Z97.5=1.96→1492SATscore.
140 CHAPTER 4. DISTRIBUTIONS OF RANDOM VARIABLES
GUIDEDPRACTICE4.16
Adult male heights follow N(70.0”,3.3”).12
(a) What is the probability that a randomly selected male adult is at least 6’2” (74 inches)?
(b) What is the probability that a male adult is shorter than 5’9” (69 inches)?
EXAMPLE4.17
What is the probability that a random adult male is between 5’9” and 6’2”?
These heights correspond to 69 inches and 74 inches. First, draw the figure. The area of interest is
no longer an upper or lower tail.
63.4 70.0 76.6
The total area under the curve is 1. If we find the area of the two tails that are not shaded (from
Guided Practice 4.16, these areas are 0.3821 and 0.1131), then we can find the middle area:
1.0000 0.3821 0.1131 = 0.5048
That is, the probability of being between 5’9” and 6’2” is 0.5048.
GUIDEDPRACTICE4.18
SAT scores follow N(1100,200). What percent of SAT takers get between 1100 and 1400?13
GUIDEDPRACTICE4.19
AdultmaleheightsfollowN(70.0”,3.3”). Whatpercentofadultmalesarebetween5’5”and5’7”?14
12Shortanswers: (a)Z=1.21→0.8869,thensubtractthisvaluefrom1toget0.1131. (b)Z=−0.30→0.3821.
13Thisis anabbreviated solution. (Besure todraw afigure!) First findthepercent whoget below1100and the
percentthatgetabove1400: Z1100=0.00→0.5000(areabelow),Z1400=1.5→0.0668(areaabove). Finalanswer:
1.0000−0.5000−0.0668=0.4332.
145’5”is65inches(Z=−1.52). 5’7”is67inches(Z=−0.91). Numericalsolution: 1.000−0.0643−0.8186=0.1171,
i.e. 11.71%.

---
