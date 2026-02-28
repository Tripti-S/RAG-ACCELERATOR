# Openintro Chapter Probability

---

OpenIntro Statistics
Fourth Edition
David Diez
Data Scientist
OpenIntro
Mine C¸etinkaya-Rundel
Associate Professor of the Practice, Duke University
Professional Educator, RStudio
Christopher D Barr
Investment Analyst
Varadero Capital
Copyright © 2019. Fourth Edition.
Updated: Dec 30th, 2024.
This book may be downloaded as a free PDF at openintro.org/book/os. This textbook is also
available under a Creative Commons license, with the source files hosted on Github.
3
Table of Contents
1 Introduction to data 7
1.1 Case study: using stents to prevent strokes . . . . . . . . . . . . . . . . . . . . . . . 9
1.2 Data basics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
1.3 Sampling principles and strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
1.4 Experiments. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
2 Summarizing data 39
2.1 Examining numerical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
2.2 Considering categorical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
2.3 Case study: malaria vaccine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
3 Probability 79
3.1 Defining probability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
3.2 Conditional probability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
3.3 Sampling from a small population . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
3.4 Random variables. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
3.5 Continuous distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
4 Distributions of random variables 131
4.1 Normal distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
4.2 Geometric distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 144
4.3 Binomial distribution. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 149
4.4 Negative binomial distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 158
4.5 Poisson distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 163
5 Foundations for inference 168
5.1 Point estimates and sampling variability . . . . . . . . . . . . . . . . . . . . . . . . . 170
5.2 Confidence intervals for a proportion . . . . . . . . . . . . . . . . . . . . . . . . . . . 181
5.3 Hypothesis testing for a proportion . . . . . . . . . . . . . . . . . . . . . . . . . . . . 189
6 Inference for categorical data 206
6.1 Inference for a single proportion. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 208
6.2 Difference of two proportions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 217
6.3 Testing for goodness of fit using chi-square. . . . . . . . . . . . . . . . . . . . . . . . 229
6.4 Testing for independence in two-way tables . . . . . . . . . . . . . . . . . . . . . . . 240
7 Inference for numerical data 249
7.1 One-sample means with the t-distribution . . . . . . . . . . . . . . . . . . . . . . . . 251
7.2 Paired data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 262
7.3 Difference of two means . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 267
7.4 Power calculations for a difference of means . . . . . . . . . . . . . . . . . . . . . . . 278
7.5 Comparing many means with ANOVA . . . . . . . . . . . . . . . . . . . . . . . . . . 285
4 TABLE OF CONTENTS
8 Introduction to linear regression 303
8.1 Fitting a line, residuals, and correlation . . . . . . . . . . . . . . . . . . . . . . . . . 305
8.2 Least squares regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 317
8.3 Types of outliers in linear regression . . . . . . . . . . . . . . . . . . . . . . . . . . . 328
8.4 Inference for linear regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 331
9 Multiple and logistic regression 341
9.1 Introduction to multiple regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . 343
9.2 Model selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 353
9.3 Checking model conditions using graphs . . . . . . . . . . . . . . . . . . . . . . . . . 358
9.4 Multiple regression case study: Mario Kart . . . . . . . . . . . . . . . . . . . . . . . 365
9.5 Introduction to logistic regression . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 371
A Exercise solutions 384
B Data sets within the text 403
C Distribution tables 408
5
Preface
OpenIntro Statistics covers a first course in statistics, providing a rigorous introduction to applied
statistics that is clear, concise, and accessible. This book was written with the undergraduate level
in mind, but it’s also popular in high schools and graduate courses.
We hope readers will take away three ideas from this book in addition to forming a foundation
of statistical thinking and methods.
• Statistics is an applied field with a wide range of practical applications.
• You don’t have to be a math guru to learn from real, interesting data.
• Data are messy, and statistical tools are imperfect. But, when you understand the strengths
and weaknesses of these tools, you can use them to learn about the world.
Textbook overview
The chapters of this book are as follows:
1. Introduction to data. Data structures, variables, and basic data collection techniques.
2. Summarizing data. Data summaries, graphics, and a teaser of inference using randomization.
3. Probability. Basic principles of probability.
4. Distributions of random variables. The normal model and other key distributions.
5. Foundations for inference. Generalideasforstatisticalinferenceinthecontextofestimating
the population proportion.
6. Inference for categorical data. Inference for proportions and tables using the normal and
chi-square distributions.
7. Inference for numerical data. Inferenceforoneortwosamplemeansusingthet-distribution,
statisticalpowerforcomparingtwogroups,andalsocomparisonsofmanymeansusingANOVA.
8. Introduction to linear regression. Regression for a numerical outcome with one predictor
variable. Most of this chapter could be covered after Chapter 1.
9. Multiple and logistic regression. Regression for numerical and categorical data using many
predictors.
OpenIntro Statistics supportsflexibilityinchoosingandorderingtopics. Ifthemaingoalistoreach
multiple regression (Chapter 9) as quickly as possible, then the following are the ideal prerequisites:
• Chapter 1, Sections 2.1, and Section 2.2 for a solid introduction to data structures and statis-
tical summaries that are used throughout the book.
• Section 4.1 for a solid understanding of the normal distribution.
• Chapter 5 to establish the core set of inference tools.
• Section 7.1 to give a foundation for the t-distribution
• Chapter 8 for establishing ideas and principles for single predictor regression.
6 TABLE OF CONTENTS
Examples and exercises
Examples are provided to establish an understanding of how to apply methods
EXAMPLE0.1
This is an example. When a question is asked here, where can the answer be found?
The answer can be found here, in the solution section of the example!
When we think the reader should be ready to try determining the solution to an example, we frame
it as Guided Practice.
GUIDEDPRACTICE0.2
The reader may check or learn the answer to any Guided Practice problem by reviewing the full
solution in a footnote.1
Exercises are also provided at the end of each section as well as review exercises at the end of each
chapter. Solutions are given for odd-numbered exercises in Appendix A.
Additional resources
Video overviews, slides, statistical software labs, data sets used in the textbook, and much more are
readily available at
openintro.org/os
We also have improved the ability to access data in this book through the addition of Appendix B,
whichprovidesadditionalinformationforeachofthedatasetsusedinthemaintextandisnewinthe
Fourth Edition. Online guides to each of these data sets are also provided at openintro.org/data
and through a companion R package.
We appreciate all feedback as well as reports of any typos through the website. A short-link to
report a new typo or review known typos is openintro.org/os/typos.
For those focused on statistics at the high school level, consider Advanced High School Statistics,
whichisaversionofOpenIntro Statistics thathasbeenheavilycustomizedbyLeahDorazioforhigh
school courses and AP® Statistics.
Acknowledgements
Thisprojectwouldnotbepossiblewithoutthepassionanddedicationofmanymorepeoplebeyond
those on the author list. The authors would like to thank the OpenIntro Staff for their involvement
and ongoing contributions. We are also very grateful to the hundreds of students and instructors
who have provided us with valuable feedback since we first started posting book content in 2009.
We also want to thank the many teachers who helped review this edition, including Laura Acion,
Matthew E. Aiello-Lammens, Jonathan Akin, Stacey C. Behrensmeyer, Juan Gomez, Jo Hardin,
Nicholas Horton, Danish Khan, Peter H.M. Klaren, Jesse Mostipak, Jon C. New, Mario Orsi, Steve
Phelps, and David Rockoff. We appreciate all of their feedback, which helped us tune the text in
significant ways and greatly improved this book.
1Guided Practice problems are intended to stretch your thinking, and you can check yourself by reviewing the
footnotesolutionforanyGuidedPractice.
7
Chapter 1
Introduction to data
1.1 Case study: using stents to prevent strokes
1.2 Data basics
1.3 Sampling principles and strategies
1.4 Experiments
8
Scientists seek to answer questions using rigorous methods and careful
observations. These observations – collected from the likes of field
notes, surveys, and experiments – form the backbone of a statistical
investigation and are called data. Statistics is the study of how best
to collect, analyze, and draw conclusions from data, and in this first
chapter, we focus on both the properties of data and on the collection
of data.
For videos, slides, and other resources, please visit
www.openintro.org/os
1.1. CASE STUDY: USING STENTS TO PREVENT STROKES 9
1.1 Case study: using stents to prevent strokes
Section 1.1 introduces a classic challenge in statistics: evaluating the efficacy of a medical
treatment. Terms in this section, and indeed much of this chapter, will all be revisited later in the
text. The plan for now is simply to get a sense of the role statistics can play in practice.
In this section we will consider an experiment that studies effectiveness of stents in treating
patients at risk of stroke. Stents are devices put inside blood vessels that assist in patient recovery
after cardiac events and reduce the risk of an additional heart attack or death. Many doctors have
hoped that there would be similar benefits for patients at risk of stroke. We start by writing the
principal question the researchers hope to answer:
Does the use of stents reduce the risk of stroke?
The researchers who asked this question conducted an experiment with 451 at-risk patients.
Each volunteer patient was randomly assigned to one of two groups:
Treatment group. Patients in the treatment group received a stent and medical manage-
ment. The medical management included medications, management of risk factors, and help
in lifestyle modification.
Control group. Patients in the control group received the same medical management as the
treatment group, but they did not receive stents.
Researchers randomly assigned 224 patients to the treatment group and 227 to the control group.
Inthisstudy,thecontrolgroupprovidesareferencepointagainstwhichwecanmeasurethemedical
impact of stents in the treatment group.
Researchersstudiedtheeffectofstentsattwotimepoints: 30daysafterenrollmentand365days
after enrollment. The results of 5 patients are summarized in Figure 1.1. Patient outcomes are
recorded as “stroke” or “no event”, representing whether or not the patient had a stroke at the end
of a time period.
Patient group 0-30 days 0-365 days
1 treatment no event no event
2 treatment stroke stroke
3 treatment no event no event
. . .
. . .
. . .
450 control no event no event
451 control no event no event
Figure 1.1: Results for five patients from the stent study.
Considering data from each patient individually would be a long, cumbersome path towards
answering the original research question. Instead, performing a statistical data analysis allows us to
consider all of the data at once. Figure 1.2 summarizes the raw data in a more helpful way. In this
table, we can quickly see what happened over the entire study. For instance, to identify the number
of patients in the treatment group who had a stroke within 30 days, we look on the left-side of the
table at the intersection of the treatment and stroke: 33.
0-30 days 0-365 days
stroke no event stroke no event
treatment 33 191 45 179
control 13 214 28 199
Total 46 405 73 378
Figure 1.2: Descriptive statistics for the stent study.
10 CHAPTER 1. INTRODUCTION TO DATA
GUIDEDPRACTICE1.1
Ofthe224patientsinthetreatmentgroup, 45hadastrokebytheendofthefirstyear. Usingthese
two numbers, compute the proportion of patients in the treatment group who had a stroke by the
end of their first year. (Please note: answers to all Guided Practice exercises are provided using
footnotes.)1
We can compute summary statistics from the table. A summary statistic is a single number
summarizing a large amount of data. For instance, the primary results of the study after 1 year
could be described by two summary statistics: the proportion of people who had a stroke in the
treatment and control groups.
Proportion who had a stroke in the treatment (stent) group: 45/224=0.20=20%.
Proportion who had a stroke in the control group: 28/227=0.12=12%.
These two summary statistics are useful in looking for differences in the groups, and we are in for
a surprise: an additional 8% of patients in the treatment group had a stroke! This is important
for two reasons. First, it is contrary to what doctors expected, which was that stents would reduce
the rate of strokes. Second, it leads to a statistical question: do the data show a “real” difference
between the groups?
This second question is subtle. Suppose you flip a coin 100 times. While the chance a coin
lands heads in any given coin flip is 50%, we probably won’t observe exactly 50 heads. This type of
fluctuationispartofalmostanytypeofdatageneratingprocess. Itispossiblethatthe8%difference
inthestentstudyisduetothisnaturalvariation. However, thelargerthedifferenceweobserve(for
a particular sample size), the less believable it is that the difference is due to chance. So what we
are really asking is the following: is the difference so large that we should reject the notion that it
was due to chance?
While we don’t yet have our statistical tools to fully address this question on our own, we can
comprehend the conclusions of the published analysis: there was compelling evidence of harm by
stents in this study of stroke patients.
Be careful: Do not generalize the results of this study to all patients and all stents. This
studylookedatpatientswithveryspecificcharacteristicswhovolunteeredtobeapartofthisstudy
andwhomaynotberepresentativeofallstrokepatients. Inaddition,therearemanytypesofstents
andthisstudyonlyconsideredtheself-expandingWingspanstent(BostonScientific). However,this
study does leave us with an important lesson: we should keep our eyes open for surprises.
1Theproportionofthe224patientswhohadastrokewithin365days: 45/224=0.20.
1.1. CASE STUDY: USING STENTS TO PREVENT STROKES 11
Exercises
1.1 Migraineandacupuncture,PartI.Amigraineisaparticularlypainfultypeofheadache,whichpatients
sometimes wish to treat with acupuncture. To determine whether acupuncture relieves migraine pain,
researchers conducted a randomized controlled study where 89 females diagnosed with migraine headaches
were randomly assigned to one of two groups: treatment or control. 43 patients in the treatment group
received acupuncture that is specifically designed to treat migraines. 46 patients in the control group
received placebo acupuncture (needle insertion at non-acupoint locations). 24 hours after patients received
S174 acupuncture,theywereaskediftheywerepNaeiunrolfSrceie(2.01R1)3e2s(uSulptpsl1a):rSe173s–uS1m75marizedinthecontingencytablebelow.2
identifiedontheantero-internalpartoftheantitragus,the Fig.1 The appropriate area
anteriorpartofthelobeandtheupperauricularconcha,on (M) versus the inappropriate
area(S)usedinthetreatment
thesamesideofpain.Themajorityofthesepointswere ofmigraineattacks Figure from the original pa-
effectiveveryrapidly(within1min),whiletheremaininPgain free
pointsproducedaslowerantalgicresponse,between2anYdes No Total per displaying the appropri-
5min.Theinsertionofasemi-permanentneedleinthese ate area (M) versus the in-
Treatment 10 33 43
zonesallowedstablecGonrtrooluopfthemigrainepain,which appropriate area (S) used in
occurredwithin30minandstillpersCistoendt2r4ohllater. 2 44 46
SincethemostactivesiteincontTroollitnaglmigrainepain12 77 89 thetreatmentofmigraineat-
wastheantero-internalpartoftheantitragus,theaimof tacks.
thisstudywastoverifythetherapeuticvalueofthiselec-
tivearea(appropriatepoint)andtocompareitwithanarea
oftheear(representingthesciaticnerve)whichisprobably
inappropriate in term(as)ofWgivhinagtaptheerracpeenutticoefffepctatonients in the treatment group were pain free 24 hours after receiving acupuncture?
migraineattacks,sinceithasnosomatotopiccorrelation In group B, the lower branch of the anthelix was
withheadpain. (b) What percent were painrefpreeaetedilny ttehsteedcwointhtrthoelaglgroomuepte?r for about 30s to
ensureitwasnotsensitive.OnboththeFrenchandChinese
(c) Inwhichgroupdidahigherpercentofpatientsbecomepainfree24hoursafterreceivingacupuncture?
auricularmaps,thisareacorrespondstotherepresentation
Materialsandmeth(odd)s Yourfindingssofarmighotfthseusgcgiaeticstnetrvhea(tFiga.c1u,parueanSc)taundreisisspeacinficaelfflyeucsetdivetreatmentformigrainesforallpeople
totreatsciaticpain.Fourneedleswereinsertedinthisarea,
who suffer from migraines. However, this is not the only possible conclusion that can be drawn based
The study enrolled 94 females, diagnosed as migraine twoforeachear.
withoutaurafollowingtheoInnteyrnoautiornafilnCdlaisnsigficsatsioonfoafr. WIhnaatllipsatioenntse, othteheearr apcuopsusnicbtulreeewxasplaalwnaaystipoenr- for the observed difference between the
HeadacheDisorders[5],whpoewrcereensutbasgeqeusenotlfyepxaamtiineendts tfhoramtedabryeapnaexinperfierneceed2a4cuphuonucturrsista.fTtheeranraelcyseisivoifng acupuncture in the two groups?
attheWomen’sHeadacheCentre,DepartmentofGynae- the diaries collecting VAS data was conducted by an
cologyandObstetricsofTurinUniversity.Theywereall impartialoperatorwhodidnotknowthegroupeachpatient
includedinthestudy1du.2ringaSmiingruaisneitaittsackapnrodvidaedntthiabtiotwicassi,n.Part I. Researchers studying the effect of antibiotic treatment for acute
it started no more tshiannu4sihtipsrecvioomuslpy.aAreccdortdoingsytomaptomTahteicavterraegaetvmalueenstosfrVaAnSdionmgrloyupaAssiagndneBdw1e6re6adultsdiagnosedwithacutesinusitisto
predeterminedcomputer-maderandomizationlist,theeli- calculatedatthedifferenttimesofthestudy,andastatis-
oneoftwogroups: treatmentorcontrol. Studyparticipantsreceivedeithera10-daycourseofamoxicillin(an
giblepatientswererandomlyandblindlyassignedtothe tical evaluation of the differences between the values
following two groupasn:tgirbouioptAic)(no=r4a6)p(alavecreagbeoagseimiolabtraininedainppT0e,aTr1a,nTc2e, Ta3nadndtaTs4tien.thTehtweopglraoucpesbo consisted of symptomatic treatments
35.93years,range15s–u6c0h),garosupaBce(nta=m48i)n(oavpehraegena,genasastluddieedcwonasgepesrtfoarnmtesd,uesitncg.anAtanatlhyseiseonfdvaorifantcehe 10-day period, patients were asked if
33.2years,range16– t 5 h 8 e ). y experienced improveme ( n A t NO in VA s ) ym for p r t e o pe m ate s d . m T e h as e ure d s is fo t l r lo i w b e u d ti b o y n m o ul f tip r l e e sponses is summarized below.3
Beforeenrollment,eachpatientwasaskedtogivean ttestofBonferronitoidentifythesourceofvariance.
informedconsenttoparticipationinthestudy. Moreover,toevaluatethedifferencebetweengroupB
Self-reported improvement
MigraineintensitywasmeasuredbymeansofaVAS andgroupA,attestforunpaireddatawasalwaysper-
beforeapplyingNCT(T0). formedforeachlevelofthevariable‘‘tiimne’’s.yInmthpetcoasmeosf
IngroupA,aspecificalgometerexertingamaximum proportions, a Chi square teYstewsas applied. All anNaloyses Total
pressureof250g(SEDATELEC,France)waschosento wereperformedusingtheStatisticalPackagefortheSocial
Treatment 66 19 85
identifythetenderpointswithPain–PressureTest(PPT).GroSucipences(SPSS)softwareprogram.Allvaluesgiveninthe
Everytenderpointlocatedwithintheidentifiedareabythe followingCteoxntatrreorleportedas6ar5ithmeticmean(±SE1M6). 81
pilotstudy(Fig.1,areaM)wastestedwithNCTfor10s Total 131 35 166
startingfromtheauricle,thatwasipsilateral,tothesideof
prevalentcephalic pain. If the test was positive and the Results
(a) What percent of patients in the treatment group experienced improvement in symptoms?
reduction was at least 25% in respect to basis, a semi-
permanent needle ((bAS)PWSEhDaAtTEpLeErCc,enFtranecxe)pewraisenceOdnlyim89ppartoievnetsmouetnoftthienenstyiremgprotuopmofs94in(43tihnegrocuopntrol group?
insertedafter1min.Onthecontrary,ifpaindidnotlessen A,46ingroupB)completedtheexperiment.Fourpatients
after1min,afurthe(rcte)ndIenrpwoinhtiwchasgchraolluenpgeddiindthaehigwhitehdrrepwerfrcoemntthaegsetudoyf,pbeactauiesentthseyexexppeerrieiencnecdeanimprovement in symptoms?
sameareaandsoon(.dW)heYnopautirenfitsnbdecianmgesawsoarefaoframn ighuntbesauragblgeeesxtacearbrateioanlodfpiffainerinetnheceperiinodepffreececdtinivgethneessofantibioticandplacebotreatments
initial decrease in the pain in all the zones of the head lastcontrolat24h(twofromgroupAandtwofromgroup
forimprovingsymptomsofsinusitis. However,thisisnottheonlypossibleconclusionthatcanbedrawn
affected,theywereinvitedtouseaspecificdiarycardto B)andwereexcludedfromthestatisticalanalysissince
scoretheintensityofthepabinawseitdhaoVnAySoatutrhefifonlldowininggssothfeayrr.eqWueshtedatthiesroemnoevaoltohfetrhepnoesesdliebs.leOenexppaltaienntationfortheobserveddifferencebetween
intervals: after 10min (Tth1)e, apfteerrc3e0nmtainge(Ts2o),fapftaertienfrtosmignrotuphAedaindtnoibtgiiovteihceracnondsenptltaoctheebimoptlarnetaoftmtheentgroupsthatexperienceimprovement
60min(T3),after120min(T4),andafter24h(T5). semi-permanentneedles.IngroupA,themeannumberof
in symptoms of sinusitis?
123
2G. Allais et al. “Ear acupuncture in the treatment of migraine attacks: a randomized trial on the efficacy of
appropriateversusinappropriateacupoints”. In: Neurological Sci.32.1(2011),pp.173–175.
3J.M. Garbutt et al. “Amoxicillin for Acute Rhinosinusitis: A Randomized Controlled Trial”. In: JAMA: The
Journal of the American Medical Association 307.7(2012),pp.685–692.
12 CHAPTER 1. INTRODUCTION TO DATA
1.2 Data basics
Effective organization and description of data is a first step in most analyses. This section
introduces the data matrix for organizing data as well as some terminology about different forms of
data that will be used throughout this book.
1.2.1 Observations, variables, and data matrices
Figure 1.3 displays rows 1, 2, 3, and 50 of a data set for 50 randomly sampled loans offered
throughLendingClub,whichisapeer-to-peerlendingcompany. Theseobservationswillbereferred
to as the loan50 data set.
Each row in the table represents a single loan. The formal name for a row is a case or
observational unit. Thecolumnsrepresentcharacteristics,calledvariables,foreachoftheloans.
For example, the first row represents a loan of $22,000 with an interest rate of 10.90%, where the
borrower is based in New Jersey (NJ) and has an income of $59,000.
GUIDEDPRACTICE1.2
What is the grade of the first loan in Figure 1.3? And what is the home ownership status of the
borrower for that first loan? For these Guided Practice questions, you can check your answer in the
footnote.4
Inpractice, itisespeciallyimportanttoaskclarifyingquestionstoensureimportantaspectsof
thedataareunderstood. Forinstance,itisalwaysimportanttobesureweknowwhateachvariable
means and the units of measurement. Descriptions of the loan50 variables are given in Figure 1.4.
loan amount interest rate term grade state total income homeownership
1 22000 10.90 60.00 B NJ 59000.00 rent
2 6000 9.92 36.00 B CA 60000.00 rent
3 25000 26.30 36.00 E SC 75000.00 mortgage
. . . . . . . .
. . . . . . . .
. . . . . . . .
50 15000 6.08 36.00 A TX 77500.00 mortgage
Figure 1.3: Four rows from the loan50 data matrix.
variable description
loan amount Amount of the loan received, in US dollars.
interest rate Interest rate on the loan, in an annual percentage.
term The length of the loan, which is always set as a whole number of months.
grade Loangrade,whichtakesvaluesAthroughGandrepresentsthequalityof
the loan and its likelihood of being repaid.
state US state where the borrower resides.
total income Borrower’s total income, including any second income, in US dollars.
homeownership Indicates whether the person owns, owns but has a mortgage, or rents.
Figure 1.4: Variables and their descriptions for the loan50 data set.
The data in Figure 1.3 represent a data matrix, which is a convenient and common way to
organize data, especially if collecting data in a spreadsheet. Each row of a data matrix corresponds
to a unique case (observational unit), and each column corresponds to a variable.
4Theloan’sgradeisB,andtheborrowerrentstheirresidence.
1.2. DATA BASICS 13
When recording data, use a data matrix unless you have a very good reason to use a different
structure. This structure allows new cases to be added as rows or new variables as new columns.
GUIDEDPRACTICE1.3
The grades for assignments, quizzes, and exams in a course are often recorded in a gradebook that
takes the form of a data matrix. How might you organize grade data using a data matrix?5
GUIDEDPRACTICE1.4
We consider data for 3,142 counties in the United States, which includes each county’s name, the
statewhereitresides,itspopulationin2017,howitspopulationchangedfrom2010to2017,poverty
rate, and six additional characteristics. How might these data be organized in a data matrix?6
The data described in Guided Practice 1.4 represents the county data set, which is shown as
a data matrix in Figure 1.5. The variables are summarized in Figure 1.6.
5Therearemultiplestrategiesthatcanbefollowed. Onecommonstrategyistohaveeachstudentrepresentedby
arow,andthenaddacolumnforeachassignment,quiz,orexam. Underthissetup,itiseasytoreviewasingleline
to understand a student’s grade history. There should also be columns to include student information, such as one
columntoliststudentnames.
6Eachcountymaybeviewedasacase,andthereareelevenpiecesofinformationrecordedforeachcase. Atable
with3,142rowsand11columnscouldholdthesedata,whereeachrowrepresentsacountyandeachcolumnrepresents
aparticularpieceofinformation.
14 CHAPTER 1. INTRODUCTION TO DATA
emocni
hh
naidem
ude
naidem
ortem
etar
pmenu
tinu
itlum
pihsrenwoemoh
ytrevop
egnahc
pop
pop
etats
eman
71355
egelloc
emos
sey
68.3
2.7
5.77
7.31
84.1
40555
amabalA
aguatuA
1
26525
egelloc
emos
sey
99.3
6.22
7.67
8.11
91.9
826212
amabalA
niwdlaB
2
86333
amolpid
sh
on
09.5
1.11
0.86
2.72
22.6-
07252
amabalA
ruobraB
3
40434
amolpid
sh
sey
93.4
6.6
9.28
2.51
37.0
86622
amabalA
bbiB
4
21474
amolpid
sh
sey
20.4
7.3
0.28
6.51
86.0
31085
amabalA
tnuolB
5
55692
amolpid
sh
on
39.4
9.9
9.67
5.82
82.2-
90301
amabalA
kcolluB
6
62363
amolpid
sh
on
94.5
7.31
0.96
4.42
96.2-
52891
amabalA
reltuB
7
68634
egelloc
emos
sey
39.4
3.41
7.07
6.81
15.1-
827411
amabalA
nuohlaC
8
24373
amolpid
sh
on
80.4
7.8
4.17
8.81
02.1-
31733
amabalA
srebmahC
9
14004
amolpid
sh
on
50.4
3.4
5.77
1.61
06.0-
75852
amabalA
eekorehC
01
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
50695
egelloc
emos
on
89.3
5.6
9.77
4.41
39.2-
7296
gnimoyW
notseW
2413
.tes
atad
ytnuoc
eht
morf
swor
nevelE
:5.1
erugiF
noitpircsed
elbairav
.eman
ytnuoC
eman
.aibmuloC
fo
tcirtsiD
eht
ro
,sediser
ytnuoc
eht
erehw
etatS
etats
.7102
ni
noitalupoP
pop
eulav
eht
,elpmaxe
roF
.7102
ot 0102
morf
noitalupop
eht
ni
egnahc
tnecreP
egnahc
pop
%84.1ybdesaercniytnuocsihtrofnoitalupopehtsnaemwortsrfiehtni84.1
.7102
ot
0102
morf
.ytrevop
ni
noitalupop
eht
fo
tnecreP
ytrevop
,renwoehthtiwsevilroemohnworiehtniseviltahtnoitalupopehtfotnecreP
pihsrenwoemoh
.emoh
eht
nwo
ohw
stnerap
htiw
gnivil
nerdlihc
.g.e
.stnemtrapa
.g.e
,serutcurts
tinu-itlum
ni
era
taht stinu
gnivil
fo
tnecreP
tinu
itlum
.tnecrep
a sa
etar
tnemyolpmenU
etar
pmenu
.aera
natiloportem
a
sniatnoc
ytnuoc
eht
rehtehW
ortem
,amolpid
sh,sh
wolebgnomaeulavaekatnachcihw,levelnoitacudenaideM
ude
naidem
.srolehcab
dna
,egelloc
emos
slauqe
emocni
s’dlohesuoh
a
erehw
,ytnuoc
eht
rof
emocni
dlohesuoh
naideM
emocni
hh
naidem
.redlo
ro
sraey
51
era
ohw
stnapucco
sti
fo
emocni
latot
eht
.tes
atad
ytnuoc
eht
rof
snoitpircsed
rieht
dna
selbairaV
:6.1
erugiF
1.2. DATA BASICS 15
1.2.2 Types of variables
Examine the unemp rate, pop, state, and median edu variables in the county data set. Each
of these variables is inherently different from the other three, yet some share certain characteristics.
First consider unemp rate, which is said to be a numerical variable since it can take a wide
rangeofnumericalvalues, anditissensibletoadd, subtract, ortakeaverageswiththosevalues. On
the other hand, we would not classify a variable reporting telephone area codes as numerical since
the average, sum, and difference of area codes doesn’t have any clear meaning.
The pop variable is also numerical, although it seems to be a little different than unemp rate.
Thisvariableofthepopulationcountcanonlytakewholenon-negativenumbers(0,1,2,...). Forthis
reason, the population variable is said to be discrete since it can only take numerical values with
jumps. On the other hand, the unemployment rate variable is said to be continuous.
The variable state can take up to 51 values after accounting for Washington, DC: AL, AK, ...,
andWY.Becausetheresponsesthemselvesarecategories,stateiscalledacategoricalvariable,and
the possible values are called the variable’s levels.
Finally,considerthemedian eduvariable,whichdescribesthemedianeducationlevelofcounty
residentsandtakesvaluesbelow hs,hs diploma,some college,orbachelorsineachcounty. This
variable seems to be a hybrid: it is a categorical variable but the levels have a natural ordering.
A variable with these properties is called an ordinal variable, while a regular categorical variable
withoutthistypeofspecialorderingiscalledanominalvariable. Tosimplifyanalyses, anyordinal
variable in this book will be treated as a nominal (unordered) categorical variable.
all variables
numerical categorical
continuous discrete nominal ordinal
(unordered categorical) (ordered categorical)
Figure 1.7: Breakdown of variables into their respective types.
EXAMPLE1.5
Data were collected about students in a statistics course. Three variables were recorded for each
student: numberofsiblings,studentheight,andwhetherthestudenthadpreviouslytakenastatistics
course. Classify each of the variables as continuous numerical, discrete numerical, or categorical.
The number of siblings and student height represent numerical variables. Because the number of
siblingsisacount, itisdiscrete. Heightvariescontinuously, soitisacontinuousnumericalvariable.
The last variable classifies students into two categories – those who have and those who have not
taken a statistics course – which makes this variable categorical.
GUIDEDPRACTICE1.6
An experiment is evaluating the effectiveness of a new drug in treating migraines. A group variable
isusedtoindicatetheexperimentgroupforeachpatient: treatmentorcontrol. Thenum migraines
variable represents the number of migraines the patient experienced during a 3-month period.
Classify each variable as either numerical or categorical.7
7The group variable can take just one of two group names, making it categorical. The num migraines variable
describesacountofthenumberofmigraines,whichisanoutcomewherebasicarithmeticissensible,whichmeansthis
isnumericaloutcome;morespecifically,sinceitrepresentsacount,num migrainesisadiscretenumericalvariable.
16 CHAPTER 1. INTRODUCTION TO DATA
1.2.3 Relationships between variables
Many analyses are motivated by a researcher looking for a relationship between two or more
variables. A social scientist may like to answer some of the following questions:
(1) Ifhomeownershipislowerthanthenationalaverageinonecounty,willthepercentofmulti-unit
structures in that county tend to be above or below the national average?
(2) Does a higher than average increase in county population tend to correspond to counties with
higher or lower median household incomes?
(3) How useful a predictor is median education level for the median household income for US
counties?
To answer these questions, data must be collected, such as the county data set shown in
Figure 1.5. Examining summary statistics could provide insights for each of the three questions
about counties. Additionally, graphs can be used to visually explore data.
Scatterplots are one type of graph used to study the relationship between two numerical vari-
ables. Figure 1.8 compares the variables homeownership and multi unit, which is the percent of
units in multi-unit structures (e.g. apartments, condos). Each point on the plot represents a single
county. For instance, the highlighted dot corresponds to County 413 in the county data set: Chat-
tahoochee County, Georgia, which has 39.4% of units in multi-unit structures and a homeownership
rate of 31.3%. The scatterplot suggests a relationship between the two variables: counties with
a higher rate of multi-units tend to have lower homeownership rates. We might brainstorm as to
why this relationship exists and investigate each idea to determine which are the most reasonable
explanations.
etaR
pihsrenwoemoH
80%
60%
40%
l
20%
0%
0% 20% 40% 60% 80% 100%
Percent of Units in Multi−Unit Structures
Figure 1.8: A scatterplot of homeownership versus the percent of units that are
in multi-unit structures for US counties. The highlighted dot represents Chatta-
hoochee County, Georgia, which has a multi-unit rate of 39.4% and a homeowner-
ship rate of 31.3%.
The multi-unit and homeownership rates are said to be associated because the plot shows a
discernible pattern. When two variables show some connection with one another, they are called
associated variables. Associated variables can also be called dependent variables and vice-versa.
1.2. DATA BASICS 17
20%
10%
0%
−10%
$0 $20k $40k $60k $80k $100k $120k
Median Household Income
egnahC
noitalupoP
sraeY
7
revo
l
Figure1.9: Ascatterplotshowingpop changeagainstmedian hh income. Owsley
County of Kentucky, is highlighted, which lost 3.63% of its population from 2010
to 2017 and had median household income of $22,736.
GUIDEDPRACTICE1.7
Examine the variables in the loan50 data set, which are described in Figure 1.4 on page 12. Create
two questions about possible relationships between variables in loan50 that are of interest to you.8
EXAMPLE1.8
This example examines the relationship between a county’s population change from 2010 to 2017
andmedianhouseholdincome,whichisvisualizedasascatterplotinFigure1.9. Arethesevariables
associated?
The larger the median household income for a county, the higher the population growth observed
for the county. While this trend isn’t true for every county, the trend in the plot is evident. Since
there is some relationship between the variables, they are associated.
Because there is a downward trend in Figure 1.8 – counties with more units in multi-unit
structures are associated with lower homeownership – these variables are said to be negatively
associated. A positive association is shown in the relationship between the median hh income
and pop change in Figure 1.9, where counties with higher median household income tend to have
higher rates of population growth.
If two variables are not associated, then they are said to be independent. That is, two
variables are independent if there is no evident relationship between the two.
ASSOCIATEDORINDEPENDENT,NOTBOTH
A pair of variables are either related in some way (associated) or not (independent). No pair of
variables is both associated and independent.
8Two example questions: (1) What is the relationship between loan amount and total income? (2) If someone’s
incomeisabovetheaverage,willtheirinterestratetendtobeaboveorbelowtheaverage?
18 CHAPTER 1. INTRODUCTION TO DATA
1.2.4 Explanatory and response variables
When we ask questions about the relationship between two variables, we sometimes also want
to determine if the change in one variable causes a change in the other. Consider the following
rephrasing of an earlier question about the county data set:
If there is an increase in the median household income in a county, does this drive an
increase in its population?
In this question, we are asking whether one variable affects another. If this is our underlying
belief, thenmedian household income istheexplanatory variableandthepopulation change isthe
response variable in the hypothesized relationship.9
EXPLANATORYANDRESPONSEVARIABLES
When we suspect one variable might causally affect another, we label the first variable the
explanatory variable and the second the response variable.
explanatory might affect response
variable variable
For many pairs of variables, there is no hypothesized relationship, and these labels would not
be applied to either variable in such cases.
Bear in mind that the act of labeling the variables in this way does nothing to guarantee that
a causal relationship exists. A formal evaluation to check whether one variable causes a change in
another requires an experiment.
1.2.5 Introducing observational studies and experiments
There are two primary types of data collection: observational studies and experiments.
Researchers perform an observational study when they collect data in a way that does not
directly interfere with how the data arise. For instance, researchers may collect information via
surveys, review medical or company records, or follow a cohort of many similar individuals to form
hypothesesaboutwhycertaindiseasesmightdevelop. Ineachofthesesituations,researchersmerely
observe the data that arise. In general, observational studies can provide evidence of a naturally
occurring association between variables, but they cannot by themselves show a causal connection.
When researchers want to investigate the possibility of a causal connection, they conduct an
experiment. Usually there will be both an explanatory and a response variable. For instance, we
may suspect administering a drug will reduce mortality in heart attack patients over the following
year. To check if there really is a causal connection between the explanatory variable and the
response,researcherswillcollectasampleofindividualsandsplitthemintogroups. Theindividuals
in each group are assigned a treatment. When individuals are randomly assigned to a group, the
experiment is called a randomized experiment. For example, each heart attack patient in the
drug trial could be randomly assigned, perhaps by flipping a coin, into one of two groups: the
first group receives a placebo (fake treatment) and the second group receives the drug. See the
case study in Section 1.1 for another example of an experiment, though that study did not employ
a placebo.
ASSOCIATION̸=CAUSATION
In general, association does not imply causation, and causation can only be inferred from a
randomized experiment.
9Sometimes the explanatory variable is called the independent variable and the response variable is called the
dependentvariable. However,thisbecomesconfusingsinceapair ofvariablesmightbeindependentordependent,
soweavoidthislanguage.
1.2. DATA BASICS 19
Exercises
1.3 Air pollution and birth outcomes, study components. Researchers collected data to examine the
relationshipbetweenairpollutantsandpretermbirthsinSouthernCalifornia. Duringthestudyairpollution
levelsweremeasuredbyairqualitymonitoringstations. Specifically,levelsofcarbonmonoxidewererecorded
inpartspermillion,nitrogendioxideandozoneinpartsperhundredmillion,andcoarseparticulatematter
(PM ) in µg/m3. Length of gestation data were collected on 143,196 births between the years 1989 and
10
1993,andairpollutionexposureduringgestationwascalculatedforeachbirth. Theanalysissuggestedthat
increased ambient PM and, to a lesser degree, CO concentrations may be associated with the occurrence
10
of preterm births.10
(a) Identify the main research question of the study.
(b) Who are the subjects in this study, and how many are included?
(c) What are the variables in the study? Identify each variable as numerical or categorical. If numerical,
statewhetherthevariableisdiscreteorcontinuous. Ifcategorical,statewhetherthevariableisordinal.
1.4 Buteykomethod,studycomponents. The Buteyko method is a shallow breathing technique devel-
oped by Konstantin Buteyko, a Russian doctor, in 1952. Anecdotal evidence suggests that the Buteyko
method can reduce asthma symptoms and improve quality of life. In a scientific study to determine the
effectivenessofthismethod,researchersrecruited600asthmapatientsaged18-69whoreliedonmedication
for asthma treatment. These patients were randomly split into two research groups: one practiced the
Buteyko method and the other did not. Patients were scored on quality of life, activity, asthma symptoms,
and medication reduction on a scale from 0 to 10. On average, the participants in the Buteyko group
experienced a significant reduction in asthma symptoms and an improvement in quality of life.11
(a) Identify the main research question of the study.
(b) Who are the subjects in this study, and how many are included?
(c) What are the variables in the study? Identify each variable as numerical or categorical. If numerical,
statewhetherthevariableisdiscreteorcontinuous. Ifcategorical,statewhetherthevariableisordinal.
1.5 Cheaters,studycomponents. Researchers studying the relationship between honesty, age and self-
control conducted an experiment on 160 children between the ages of 5 and 15. Participants reported their
age, sex, and whether they were an only child or not. The researchers asked each child to toss a fair coin
in private and to record the outcome (white or black) on a paper sheet, and said they would only reward
children who report white. The study’s findings can be summarized as follows: “Half the students were
explicitly told not to cheat and the others were not given any explicit instructions. In the no instruction
groupprobabilityofcheatingwasfoundtobeuniformacrossgroupsbasedonchild’scharacteristics. Inthe
group that was explicitly told to not cheat, girls were less likely to cheat, and while rate of cheating didn’t
vary by age for boys, it decreased with age for girls.”12
(a) Identify the main research question of the study.
(b) Who are the subjects in this study, and how many are included?
(c) How many variables were recorded for each subject in the study in order to conclude these findings?
State the variables and their types.
10B.Ritzetal.“EffectofairpollutiononpretermbirthamongchildrenborninSouthernCaliforniabetween1989
and1993”. In: Epidemiology 11.5(2000),pp.502–511.
11J.McGowan. “HealthEducation: DoestheButeykoInstituteMethodmakeadifference?” In: Thorax 58(2003).
12AlessandroBucciolandMarcoPiovesan. “Luckorcheating? Afieldexperimentonhonestywithchildren”. In:
Journal of Economic Psychology 32.1(2011),pp.73–78.
20 CHAPTER 1. INTRODUCTION TO DATA
1.6 Stealers,studycomponents. Inastudyoftherelationshipbetweensocio-economicclassandunethical
behavior, 129 University of California undergraduates at Berkeley were asked to identify themselves as
havingloworhighsocial-classbycomparingthemselvestootherswiththemost(least)money,most(least)
education, and most (least) respected jobs. They were also presented with a jar of individually wrapped
candies and informed that the candies were for children in a nearby laboratory, but that they could take
some if they wanted. After completing some unrelated tasks, participants reported the number of candies
they had taken.13
(a) Identify the main research question of the study.
(b) Who are the subjects in this study, and how many are included?
(c) The study found that students who were identified as upper-class took more candy than others. How
many variables were recorded for each subject in the study in order to conclude these findings? State
the variables and their types.
1.7 Migraine and acupuncture, Part II. Exercise 1.1 introduced a study exploring whether acupuncture
had any effect on migraines. Researchers conducted a randomized controlled study where patients were
randomly assigned to one of two groups: treatment or control. The patients in the treatment group re-
ceived acupuncture that was specifically designed to treat migraines. The patients in the control group
received placebo acupuncture (needle insertion at non-acupoint locations). 24 hours after patients received
acupuncture, they were asked if they were pain free. What are the explanatory and response variables in
this study?
1.8 Sinusitis and antibiotics, Part II. Exercise 1.2 introduced a study exploring the effect of antibiotic
treatment for acute sinusitis. Study participants either received either a 10-day course of an antibiotic
(treatment)oraplacebosimilarinappearanceandtaste(control). Attheendofthe10-dayperiod,patients
wereaskediftheyexperiencedimprovementinsymptoms. Whataretheexplanatoryandresponsevariables
in this study?
1.9 Fisher’s irises. Sir Ronald Aylmer Fisher was an English statistician, evolutionary biologist, and
geneticistwhoworkedonadatasetthatcontainedsepallengthandwidth,andpetallengthandwidthfrom
threespeciesofirisflowers(setosa,versicolor andvirginica). Therewere50flowersfromeachspeciesinthe
data set.14
(a) How many cases were included in the data?
(b) How many numerical variables are included in
the data? Indicate what they are, and if they Photo by Ryan Claussen
are continuous or discrete. (http://flic.kr/p/6QTcuX)
(c) How many categorical variables are included in CCBY-SA2.0license
the data, and what are they? List the corre-
sponding levels (categories).
1.10 Smoking habits of UK residents. A survey was conducted to study the smoking habits of UK
residents. Below is a data matrix displaying a portion of the data collected in this survey. Note that “£”
standsforBritishPoundsSterling,“cig”standsforcigarettes,and“N/A”referstoamissingcomponentof
the data.15
sex age marital grossIncome smoke amtWeekends amtWeekdays
1 Female 42 Single Under£2,600 Yes 12cig/day 12cig/day
2 Male 44 Single £10,400to£15,600 No N/A N/A
3 Male 53 Married Above£36,400 Yes 6cig/day 6cig/day
. . . . . . . .
. . . . . . . .
. . . . . . . .
1691 Male 40 Single £2,600to£5,200 Yes 8cig/day 8cig/day
(a) What does each row of the data matrix represent?
(b) How many participants were included in the survey?
(c) Indicatewhethereachvariableinthestudyisnumericalorcategorical. Ifnumerical,identifyascontin-
uous or discrete. If categorical, indicate if the variable is ordinal.
13P.K. Piff et al. “Higher social class predicts increased unethical behavior”. In: Proceedings of the National
Academy of Sciences (2012).
14R.A Fisher. “The Use of Multiple Measurements in Taxonomic Problems”. In: Annals of Eugenics 7 (1936),
pp.179–188.
15NationalSTEMCentre,LargeDatasetsfromstats4schools.
1.2. DATA BASICS 21
1.11 USAirports. Thevisualizationbelowshowsthegeographicaldistributionofairportsinthecontiguous
United States and Washington, DC. This visualization was constructed based on a dataset where each
observation is an airport.16
(a) List the variables used in creating this visualization.
(b) Indicatewhethereachvariableinthestudyisnumericalorcategorical. Ifnumerical,identifyascontin-
uous or discrete. If categorical, indicate if the variable is ordinal.
1.12 UNVotes. ThevisualizationbelowshowsvotingpatternsintheUnitedStates,Canada,andMexicoin
theUnitedNationsGeneralAssemblyonavarietyofissues. Specifically,foragivenyearbetween1946and
2015,itdisplaysthepercentageofrollcallsinwhichthecountryvotedyesforeachissue. Thisvisualization
was constructed based on a dataset where each observation is a country/year pair.17
(a) List the variables used in creating this visualization.
(b) Indicatewhethereachvariableinthestudyisnumericalorcategorical. Ifnumerical,identifyascontin-
uous or discrete. If categorical, indicate if the variable is ordinal.
16FederalAviationAdministration,www.faa.gov/airports/airport safety/airportdata 5010.
17DavidRobinson. unvotes: United Nations General Assembly Voting Data. Rpackageversion0.2.0. 2017. url:
https://CRAN.R-project.org/package=unvotes.
22 CHAPTER 1. INTRODUCTION TO DATA
1.3 Sampling principles and strategies
Thefirststepinconductingresearchistoidentifytopicsorquestionsthataretobeinvestigated.
Aclearlylaidoutresearchquestionishelpfulinidentifyingwhatsubjectsorcasesshouldbestudied
and what variables are important. It is also important to consider how data are collected so that
they are reliable and help achieve the research goals.
1.3.1 Populations and samples
Consider the following three research questions:
1. What is the average mercury content in swordfish in the Atlantic Ocean?
2. Over the last 5 years, what is the average time to complete a degree for Duke undergrads?
3. Does a new drug reduce the number of deaths in patients with severe heart disease?
Each research questionrefers to atarget population. Inthe first question, the target population is
all swordfish in the Atlantic ocean, and each fish represents a case. Often times, it is too expensive
to collect data for every case in a population. Instead, a sample is taken. A sample represents
a subset of the cases and is often a small fraction of the population. For instance, 60 swordfish
(or some other number) in the population might be selected, and this sample data may be used to
provide an estimate of the population average and answer the research question.
GUIDEDPRACTICE1.9
For the second and third questions above, identify the target population and what represents an
individual case.18
1.3.2 Anecdotal evidence
Consider the following possible responses to the three research questions:
1. A man on the news got mercury poisoning from eating swordfish, so the average mercury
concentration in swordfish must be dangerously high.
2. I met two students who took more than 7 years to graduate from Duke, so it must take longer
to graduate at Duke than at many other colleges.
3. My friend’s dad had a heart attack and died after they gave him a new heart disease drug,
so the drug must not work.
Each conclusion is based on data. However, there are two problems. First, the data only represent
one or two cases. Second, and more importantly, it is unclear whether these cases are actually
representative of the population. Data collected in this haphazard fashion are called anecdotal
evidence.
ANECDOTALEVIDENCE
Be careful of data collected in a haphazard fashion. Such evidence may be true and verifiable,
but it may only represent extraordinary cases.
18(2) The first question is only relevant to students who complete their degree; the average cannot be computed
using a student who never finished her degree. Thus, only Duke undergrads who graduated in the last five years
represent cases in the population under consideration. Each such student is an individual case. (3) A person with
severeheartdiseaserepresentsacase. Thepopulationincludesallpeoplewithsevereheartdisease.
1.3. SAMPLING PRINCIPLES AND STRATEGIES 23
Figure1.10: InFebruary2010,somemediapundits
citedonelargesnowstormasvalidevidenceagainst
globalwarming. AscomedianJonStewartpointed
out,“It’sonestorm,inoneregion,ofonecountry.”
Anecdotalevidencetypicallyiscomposedofunusualcasesthatwerecallbasedontheirstriking
characteristics. Forinstance,wearemorelikelytorememberthetwopeoplewemetwhotook7years
tograduatethanthesixotherswhograduatedinfouryears. Insteadoflookingatthemostunusual
cases, we should examine a sample of many cases that represent the population.
1.3.3 Sampling from a population
We might try to estimate the time to graduation for Duke undergraduates in the last 5 years
by collecting a sample of students. All graduates in the last 5 years represent the population, and
graduateswhoareselectedforreviewarecollectivelycalledthesample. Ingeneral,wealwaysseekto
randomly select a sample from a population. The most basic type of random selection is equivalent
to how raffles are conducted. For example, in selecting graduates, we could write each graduate’s
name on a raffle ticket and draw 100 tickets. The selected names would represent a random sample
of 100 graduates. We pick samples randomly to reduce the chance we introduce biases.
all graduates
sample
Figure 1.11: In this graphic, five graduates are randomly selected from the popu-
lation to be included in the sample.
EXAMPLE1.10
Suppose we ask a student who happens to be majoring in nutrition to select several graduates for
the study. What kind of students do you think she might collect? Do you think her sample would
be representative of all graduates?
Perhaps she would pick a disproportionate number of graduates from health-related fields. Or per-
haps her selection would be a good representation of the population. When selecting samples by
hand, we run the risk of picking a biased sample, even if their bias isn’t intended.
24 CHAPTER 1. INTRODUCTION TO DATA
all graduates
sample
graduates from
health−related fields
Figure 1.12: Asked to pick a sample of graduates, a nutrition major might inad-
vertentlypickadisproportionatenumberofgraduatesfromhealth-relatedmajors.
If someone was permitted to pick and choose exactly which graduates were included in the
sample, it is entirely possible that the sample could be skewed to that person’s interests, which may
be entirely unintentional. This introduces bias into a sample. Sampling randomly helps resolve
this problem. The most basic random sample is called a simple random sample, and which is
equivalenttousingaraffletoselectcases. Thismeansthateachcaseinthepopulationhasanequal
chance of being included and there is no implied connection between the cases in the sample.
The act of taking a simple random sample helps minimize bias. However, bias can crop up in
other ways. Even when people are picked at random, e.g. for surveys, caution must be exercised
if the non-response rate is high. For instance, if only 30% of the people randomly sampled for
a survey actually respond, then it is unclear whether the results are representative of the entire
population. This non-response bias can skew results.
population of interest
sample
population actually
sampled
Figure1.13: Duetothepossibilityofnon-response,surveysstudiesmayonlyreach
a certain group within the population. It is difficult, and often times impossible,
to completely fix this problem.
Another common downfall is a convenience sample, where individuals who are easily ac-
cessible are more likely to be included in the sample. For instance, if a political survey is done
by stopping people walking in the Bronx, this will not represent all of New York City. It is often
difficult to discern what sub-population a convenience sample represents.
GUIDEDPRACTICE1.11
We can easily access ratings for products, sellers, and companies through websites. These ratings
are based only on those people who go out of their way to provide a rating. If 50% of online reviews
for a product are negative, do you think this means that 50% of buyers are dissatisfied with the
product?19
19Answers will vary. From our own anecdotal experiences, we believe people tend to rant more about products
that fell below expectations than rave about those that perform as expected. For this reason, we suspect there is a
negativebiasinproductratingsonsiteslikeAmazon. However,sinceourexperiencesmaynotberepresentative,we
alsokeepanopenmind.
1.3. SAMPLING PRINCIPLES AND STRATEGIES 25
1.3.4 Observational studies
Datawherenotreatmenthasbeenexplicitlyapplied(orexplicitlywithheld)iscalledobserva-
tionaldata. Forinstance,theloandataandcountydatadescribedinSection1.2arebothexamples
of observational data. Making causal conclusions based on experiments is often reasonable. How-
ever, making the same causalconclusions basedon observationaldata canbe treacherousand isnot
recommended. Thus, observationalstudiesaregenerallyonlysufficienttoshowassociationsorform
hypotheses that we later check using experiments.
GUIDEDPRACTICE1.12
Suppose an observational study tracked sunscreen use and skin cancer, and it was found that the
more sunscreen someone used, the more likely the person was to have skin cancer. Does this mean
sunscreen causes skin cancer?20
Somepreviousresearchtellsusthatusingsunscreenactuallyreducesskincancerrisk,somaybe
thereisanothervariablethatcanexplainthishypotheticalassociationbetweensunscreenusageand
skin cancer. One important piece of information that is absent is sun exposure. If someone is out
in the sun all day, she is more likely to use sunscreen and more likely to get skin cancer. Exposure
to the sun is unaccounted for in the simple investigation.
sun exposure
?
use sunscreen skin cancer
Sunexposureiswhatiscalledaconfounding variable,21 whichisavariablethatiscorrelated
with both the explanatory and response variables. While one method to justify making causal
conclusionsfromobservationalstudiesistoexhaustthesearchforconfoundingvariables,thereisno
guarantee that all confounding variables can be examined or measured.
GUIDEDPRACTICE1.13
Figure1.8showsanegativeassociationbetweenthehomeownershiprateandthepercentageofmulti-
unitstructuresinacounty. However,itisunreasonabletoconcludethatthereisacausalrelationship
between the two variables. Suggest a variable that might explain the negative relationship.22
Observational studies come in two forms: prospective and retrospective studies. A prospec-
tive study identifies individuals and collects information as events unfold. For instance, medical
researchers may identify and follow a group of patients over many years to assess the possible influ-
ences of behavior on cancer risk. One example of such a study is The Nurses’ Health Study, started
in 1976 and expanded in 1989. This prospective study recruits registered nurses and then collects
data from them using questionnaires. Retrospective studies collect data after events have taken
place, e.g. researchers may review past events in medical records. Some data sets may contain both
prospectively- and retrospectively-collected variables.
1.3.5 Four sampling methods
Almost all statistical methods are based on the notion of implied randomness. If observational
data are not collected in a random framework from a population, these statistical methods – the
estimates and errors associated with the estimates – are not reliable. Here we consider four random
sampling techniques: simple, stratified, cluster, and multistage sampling. Figures 1.14 and 1.15
provide graphical representations of these techniques.
20No. Seetheparagraphfollowingtheexerciseforanexplanation.
21Alsocalledalurking variable,confounding factor,oraconfounder.
22Answers will vary. Population density may be important. If a county is very dense, then this may require a
largerfractionofresidentstoliveinmulti-unitstructures. Additionally,thehighdensitymaycontributetoincreases
inpropertyvalue,makinghomeownershipinfeasibleformanyresidents.
26 CHAPTER 1. INTRODUCTION TO DATA
l lll
lll
l
l l
l lll
l
l
lll l l l l
l
l l
l l
l l l lll l
l
lll
l l
l l l lll l
l
l
l l
l l l
l l l l
l l l l l l l l l l l l l l l lll l l l l
l l l l l l
l l l l l l l l lll l lll l lll
lll l
l
l
l
l l lll l l lll l l
lll lll
l lll l l l lll l
l l
Stratum 2
Stratum 4
Stratum 6
Index
l
l
l
lll
l
l
l Stratum 3 l
l
lll
l
l l
ll
l
ll
l ll
l
l ll l l l ll
lll l l l l ll l
l
lll l
l
l l
l
l l
ll
l
lll
l
l
ll l l
l
l lll
ll
l
l l l l l
lll l l l l ll l
l
l l l l ll l l
Stratum 1 l l l l l
l l l l l l l l l ll l lll l l l
l
lll
l
l
l
lll
ll
l
lll l ll
lll l
lll
l
l l
l l
l
llll
llll
l
l l
l
l
l l
l l Stratum 5
Figure1.14: Examplesofsimplerandomandstratifiedsampling. Inthetoppanel,
simple random sampling was used to randomly select the 18 cases. In the bottom
panel, stratified sampling was used: cases were grouped into strata, then simple
random sampling was employed within each stratum.
1.3. SAMPLING PRINCIPLES AND STRATEGIES 27
Simple random samplingisprobablythemostintuitiveformofrandomsampling. Consider
the salaries of Major League Baseball (MLB) players, where each player is a member of one of the
league’s 30 teams. To take a simple random sample of 120 baseball players and their salaries, we
could write the names of that season’s several hundreds of players onto slips of paper, drop the slips
into a bucket, shake the bucket around until we are sure the names are all mixed up, then draw out
slipsuntilwehavethesampleof120players. Ingeneral, asampleisreferredtoas“simplerandom”
ifeachcaseinthepopulationhasanequalchanceofbeingincludedinthefinalsampleand knowing
that a case is included in a sample does not provide useful information about which other cases are
included.
Stratified sampling is a divide-and-conquer sampling strategy. The population is divided
into groups called strata. The strata are chosen so that similar cases are grouped together, then a
second sampling method, usually simple random sampling, is employed within each stratum. In the
baseball salary example, the teams could represent the strata, since some teams have a lot more
money (up to 4 times as much!). Then we might randomly sample 4 players from each team for a
total of 120 players.
Stratified sampling is especially useful when the cases in each stratum are very similar with
respect to the outcome of interest. The downside is that analyzing data from a stratified sample
is a more complex task than analyzing data from a simple random sample. The analysis methods
introducedinthisbookwouldneedtobeextendedtoanalyzedatacollectedusingstratifiedsampling.
EXAMPLE1.14
Why would it be good for cases within each stratum to be very similar?
Wemightgetamorestableestimateforthesubpopulationinastratumifthecasesareverysimilar,
leadingtomorepreciseestimateswithineachgroup. Whenwecombinetheseestimatesintoasingle
estimate for the full population, that population estimate will tend to be more precise since each
individual group estimate is itself more precise.
In a cluster sample, we break up the population into many groups, called clusters. Then
we sample a fixed number of clusters and include all observations from each of those clusters in the
sample. A multistage sample is like a cluster sample, but rather than keeping all observations in
each cluster, we collect a random sample within each selected cluster.
Sometimesclusterormultistagesamplingcanbemoreeconomicalthanthealternativesampling
techniques. Also,unlikestratifiedsampling,theseapproachesaremosthelpfulwhenthereisalotof
case-to-casevariabilitywithinaclusterbuttheclustersthemselvesdon’tlookverydifferentfromone
another. For example, if neighborhoods represented clusters, then cluster or multistage sampling
work best when the neighborhoods are very diverse. A downside of these methods is that more
advanced techniques are typically required to analyze the data, though the methods in this book
can be extended to handle such data.
EXAMPLE1.15
Suppose we are interested in estimating the malaria rate in a densely tropical portion of rural
Indonesia. We learn that there are 30 villages in that part of the Indonesian jungle, each more or
less similar to the next. Our goal is to test 150 individuals for malaria. What sampling method
should be employed?
A simple random sample would likely draw individuals from all 30 villages, which could make data
collection extremely expensive. Stratified sampling would be a challenge since it is unclear how we
would build strata of similar individuals. However, cluster sampling or multistage sampling seem
like very good ideas. If we decided to use multistage sampling, we might randomly select half of the
villages, then randomly select 10 people from each. This would probably reduce our data collection
costs substantially in comparison to a simple random sample, and the cluster sample would still
give us reliable information, even if we would need to analyze the data with slightly more advanced
methods than we discuss in this book.
28 CHAPTER 1. INTRODUCTION TO DATA
Cluster 9
Cluster 2 Cluster 5
Cluster 7 l
l l l
l l l l
l l l l l l l l Cluster 3 l l l l l ll l l l l l l l ll l l ll l l
l l l lll lll
lll
llllll
l
l
ll
l l l l
l ll
l
l l l Cluster 8
l l l l l l ll l l
l
l l l ll l l lll lll llllll lll lll lll lll C lll l
l
u
l l lll
l l s l l l l l ll
lll
ter llll 4 ll lll lll ll ll C l ll l l l u l s l t l er l 6 l l l l l ll ll
l
l l
l
l l
l
l l l l l l l l l ll lll lll ll l l l ll ll lll lll
Cluster 1
Cluster 9
Cluster 2 Cluster 5
Index
Cluster 7 l
l ll l l l l l l l l l l
l l l l l l Cluster 3 l l l l l l l l l l l ll l l l l l l
l lll llll lll l l l l l l l l l l l l l l ll l Cluster 8
l lll l lll Cluster 4 ll l ll l
l l l lll l l l l l l l lll
lll
l l l ll l l l
l
l l lll llllll l l ll l l
l
lll l
l
l
ll
ll l l
l
lll
l
l
l
l l
l
llllll l
l
ll
l
Cluster 6 lll
Cluster 1
Figure1.15: Examplesofclusterandmultistagesampling. Inthetoppanel,cluster
sampling was used: data were binned into nine clusters, three of these clusters
were sampled, and all observations within these three cluster were included in the
sample. In the bottom panel, multistage sampling was used, which differs from
cluster sampling only in that we randomly select a subset of each cluster to be
included in the sample rather than measuring every case in each sampled cluster.
1.3. SAMPLING PRINCIPLES AND STRATEGIES 29
Exercises
1.13 Air pollution and birth outcomes, scope of inference. Exercise 1.3 introduces a study where
researcherscollecteddatatoexaminetherelationshipbetweenairpollutantsandpretermbirthsinSouthern
California. Duringthestudyairpollutionlevelsweremeasuredbyairqualitymonitoringstations. Lengthof
gestationdatawerecollectedon143,196birthsbetweentheyears1989and1993,andairpollutionexposure
during gestation was calculated for each birth.
(a) Identify the population of interest and the sample in this study.
(b) Comment on whether or not the results of the study can be generalized to the population, and if the
findings of the study can be used to establish causal relationships.
1.14 Cheaters,scopeofinference. Exercise 1.5 introduces a study where researchers studying the rela-
tionship between honesty, age, and self-control conducted an experiment on 160 children between the ages
of5and15. Theresearchersaskedeachchildtotossafaircoininprivateandtorecordtheoutcome(white
or black) on a paper sheet, and said they would only reward children who report white. Half the students
were explicitly told not to cheat and the others were not given any explicit instructions. Differences were
observedinthecheatingratesintheinstructionandnoinstructiongroups,aswellassomedifferencesacross
children’s characteristics within each group.
(a) Identify the population of interest and the sample in this study.
(b) Comment on whether or not the results of the study can be generalized to the population, and if the
findings of the study can be used to establish causal relationships.
1.15 Buteykomethod,scopeofinference. Exercise1.4introducesastudyonusingtheButeykoshallow
breathing technique to reduce asthma symptoms and improve quality of life. As part of this study 600
asthma patients aged 18-69 who relied on medication for asthma treatment were recruited and randomly
assigned to two groups: one practiced the Buteyko method and the other did not. Those in the Buteyko
group experienced, on average, a significant reduction in asthma symptoms and an improvement in quality
of life.
(a) Identify the population of interest and the sample in this study.
(b) Comment on whether or not the results of the study can be generalized to the population, and if the
findings of the study can be used to establish causal relationships.
1.16 Stealers, scope of inference. Exercise 1.6 introduces a study on the relationship between socio-
economic class and unethical behavior. As part of this study 129 University of California Berkeley under-
graduates were asked to identify themselves as having low or high social-class by comparing themselves to
otherswiththemost(least)money,most(least)education,andmost(least)respectedjobs. Theywerealso
presented with a jar of individually wrapped candies and informed that the candies were for children in a
nearby laboratory, but that they could take some if they wanted. After completing some unrelated tasks,
participantsreportedthenumberofcandiestheyhadtaken. Itwasfoundthatthosewhowereidentifiedas
upper-class took more candy than others.
(a) Identify the population of interest and the sample in this study.
(b) Comment on whether or not the results of the study can be generalized to the population, and if the
findings of the study can be used to establish causal relationships.
1.17 Relaxing after work. The General Social Survey asked the question, “After an average work day,
abouthowmanyhoursdoyouhavetorelaxorpursueactivitiesthatyouenjoy?”toarandomsampleof1,155
Americans. The average relaxing time was found to be 1.65 hours. Determine which of the following is an
observation, a variable, a sample statistic (value calculated based on the observed sample), or a population
parameter.
(a) An American in the sample.
(b) Number of hours spent relaxing after an average work day.
(c) 1.65.
(d) Average number of hours all Americans spend relaxing after an average work day.
30 CHAPTER 1. INTRODUCTION TO DATA
1.18 CatsonYouTube. Suppose you want to estimate the percentage of videos on YouTube that are cat
videos. It is impossible for you to watch all videos on YouTube so you use a random video picker to select
1000videosforyou. Youfindthat2%ofthesevideosarecatvideos. Determinewhichofthefollowingisan
observation, a variable, a sample statistic (value calculated based on the observed sample), or a population
parameter.
(a) Percentage of all videos on YouTube that are cat videos.
(b) 2%.
(c) A video in your sample.
(d) Whether or not a video is a cat video.
1.19 Course satisfaction across sections. A large college class has 160 students. All 160 students
attendthelecturestogether,butthestudentsaredividedinto4groups,eachof40students,forlabsections
administered by different teaching assistants. The professor wants to conduct a survey about how satisfied
thestudentsarewiththecourse,andhebelievesthatthelabsectionastudentisinmightaffectthestudent’s
overall satisfaction with the course.
(a) What type of study is this?
(b) Suggest a sampling strategy for carrying out this study.
1.20 Housingproposalacrossdorms. Onalargecollegecampusfirst-yearstudentsandsophomoreslive
in dorms located on the eastern part of the campus and juniors and seniors live in dorms located on the
western part of the campus. Suppose you want to collect student opinions on a new housing structure the
collegeadministrationisproposingandyouwanttomakesureyoursurveyequallyrepresentsopinionsfrom
students from all years.
(a) What type of study is this?
(b) Suggest a sampling strategy for carrying out this study.
1.21 Internetuseandlifeexpectancy. Thefollowingscatterplotwascreatedaspartofastudyevaluating
therelationshipbetweenestimatedlifeexpectancyatbirth(asof2014)andpercentageofinternetusers(as
of 2009) in 208 countries for which such data were available.23
(a) Describe the relationship between life ex-
pectancy and percentage of internet users.
(b) What type of study is this?
(c) State a possible confounding variable that
mightexplainthisrelationshipanddescribe
its potential effect.
Percent Internet Users
htriB
ta
ycnatcepxE
efiL
90
80
70
60
50
0% 20% 40% 60% 80% 100%
1.22 Stressedout,PartI.Astudythatsurveyedarandomsampleofotherwisehealthyhighschoolstudents
found that they are more likely to get muscle cramps when they are stressed. The study also noted that
students drink more coffee and sleep less when they are stressed.
(a) What type of study is this?
(b) Can this study be used to conclude a causal relationship between increased stress and muscle cramps?
(c) State possible confounding variables that might explain the observed relationship between increased
stress and muscle cramps.
1.23 Evaluate sampling methods. A university wants to determine what fraction of its undergraduate
studentbodysupportanew$25annualfeetoimprovethestudentunion. Foreachproposedmethodbelow,
indicate whether the method is reasonable or not.
(a) Survey a simple random sample of 500 students.
(b) Stratify students by their field of study, then sample 10% of students from each stratum.
(c) Cluster students by their ages (e.g. 18 years old in one cluster, 19 years old in one cluster, etc.), then
randomly sample three clusters and survey all students in those clusters.
23CIAFactbook,CountryComparisons,2014.
1.3. SAMPLING PRINCIPLES AND STRATEGIES 31
1.24 Randomdigitdialing. The Gallup Poll uses a procedure called random digit dialing, which creates
phone numbers based on a list of all area codes in America in conjunction with the associated number of
residentialhouseholdsineachareacode. GiveapossiblereasontheGallupPollchoosestouserandomdigit
dialing instead of picking phone numbers from the phone book.
1.25 Haters are gonna hate, study confirms. A study published in the Journal of Personality and
Social Psychology asked a group of 200 randomly sampled men and women to evaluate how they felt about
various subjects, such as camping, health care, architecture, taxidermy, crossword puzzles, and Japan in
order to measure their attitude towards mostly independent stimuli. Then, they presented the participants
with information about a new product: a microwave oven. This microwave oven does not exist, but the
participants didn’t know this, and were given three positive and three negative fake reviews. People who
reacted positively to the subjects on the dispositional attitude measurement also tended to react positively
to the microwave oven, and those who reacted negatively tended to react negatively to it. Researchers
concludedthat“somepeopletendtolikethings,whereasotherstendtodislikethings,andamorethorough
understandingofthistendencywillleadtoamorethoroughunderstandingofthepsychologyofattitudes.”24
(a) What are the cases?
(b) What is (are) the response variable(s) in this study?
(c) What is (are) the explanatory variable(s) in this study?
(d) Does the study employ random sampling?
(e) Is this an observational study or an experiment? Explain your reasoning.
(f) Can we establish a causal link between the explanatory and response variables?
(g) Can the results of the study be generalized to the population at large?
1.26 Familysize. Suppose we want to estimate household size, where a “household” is defined as people
living together in the same dwelling, and sharing living accommodations. If we select students at random
at an elementary school and ask them what their family size is, will this be a good measure of household
size? Or will our average be biased? If so, will it overestimate or underestimate the true value?
1.27 Samplingstrategies. Astatisticsstudentwhoiscuriousabouttherelationshipbetweentheamount
of time students spend on social networking sites and their performance at school decides to conduct a
survey. Various research strategies for collecting data are described below. In each, name the sampling
method proposed and any bias you might expect.
(a) He randomly samples 40 students from the study’s population, gives them the survey, asks them to fill
it out and bring it back the next day.
(b) He gives out the survey only to his friends, making sure each one of them fills out the survey.
(c) He posts a link to an online survey on Facebook and asks his friends to fill out the survey.
(d) He randomly samples 5 classes and asks a random sample of students from those classes to fill out the
survey.
1.28 Readingthepaper. Below are excerpts from two articles published in the NY Times:
(a) An article titled Risks: Smokers Found More Prone to Dementia states the following:25
“Researchers analyzed data from 23,123 health plan members who participated in a voluntary exam and
health behavior survey from 1978 to 1985, when they were 50-60 years old. 23 years later, about 25% of
the group had dementia, including 1,136 with Alzheimer’s disease and 416 with vascular dementia. After
adjusting for other factors, the researchers concluded that pack-a-day smokers were 37% more likely than
nonsmokers todevelopdementia, andtherisks wentup withincreasedsmoking; 44%for onetotwo packs
aday;andtwicetheriskformorethantwopacks.”
Basedonthisstudy,canweconcludethatsmokingcausesdementialaterinlife? Explainyourreasoning.
(b) Another article titled The School Bully Is Sleepy states the following:26
“The University of Michigan study, collected survey data from parents on each child’s sleep habits and
askedbothparentsandteacherstoassessbehavioralconcerns. Aboutathirdofthestudentsstudiedwere
identified by parents or teachers as having problems with disruptive behavior or bullying. The researchers
foundthatchildrenwhohadbehavioralissuesandthosewhowereidentifiedasbulliesweretwiceaslikely
tohaveshownsymptomsofsleepdisorders.”
A friend of yours who read the article says, “The study shows that sleep disorders lead to bullying in
school children.” Is this statement justified? If not, how best can you describe the conclusion that can
be drawn from this study?
24Justin Hepler and Dolores Albarrac´ın. “Attitudes without objects - Evidence for a dispositional attitude, its
measurement,anditsconsequences”. In: Journal of personality and social psychology 104.6(2013),p.1060.
25R.C.Rabin. “Risks: SmokersFoundMorePronetoDementia”. In: New York Times (2010).
26T.Parker-Pope. “TheSchoolBullyIsSleepy”. In: New York Times (2011).
32 CHAPTER 1. INTRODUCTION TO DATA
1.4 Experiments
Studies where the researchers assign treatments to cases are called experiments. When this
assignmentincludesrandomization,e.g.usingacoinfliptodecidewhichtreatmentapatientreceives,
it is called a randomized experiment. Randomized experiments are fundamentally important
when trying to show a causal connection between two variables.
1.4.1 Principles of experimental design
Randomized experiments are generally built on four principles.
Controlling. Researchers assign treatments to cases, and they do their best to control any other
differencesinthegroups.27 Forexample,whenpatientstakeadruginpillform,somepatients
takethepillwithonlyasipofwaterwhileothersmayhaveitwithanentireglassofwater. To
control for the effect of water consumption, a doctor may ask all patients to drink a 12 ounce
glass of water with the pill.
Randomization. Researchers randomize patients into treatment groups to account for variables
that cannot be controlled. For example, some patients may be more susceptible to a disease
than others due to their dietary habits. Randomizing patients into the treatment or control
group helps even out such differences, and it also prevents accidental bias from entering the
study.
Replication. The more cases researchers observe, the more accurately they can estimate the effect
of the explanatory variable on the response. In a single study, we replicate by collecting a
sufficiently large sample. Additionally, a group of scientists may replicate an entire study to
verify an earlier finding.
Blocking. Researchers sometimes know or suspect that variables, other than the treatment, influ-
ence the response. Under these circumstances, they may first group individuals based on this
variableintoblocksandthenrandomizecaseswithineachblocktothetreatmentgroups. This
strategyisoftenreferredtoasblocking. Forinstance,ifwearelookingattheeffectofadrug
on heart attacks, we might first split patients in the study into low-risk and high-risk blocks,
thenrandomlyassignhalfthepatientsfromeachblocktothecontrolgroupandtheotherhalf
to the treatment group, as shown in Figure 1.16. This strategy ensures each treatment group
has an equal number of low-risk and high-risk patients.
Itisimportanttoincorporatethefirstthreeexperimentaldesignprinciplesintoanystudy, and
this book describes applicable methods for analyzing data from such experiments. Blocking is a
slightly more advanced technique, and statistical methods in this book may be extended to analyze
data collected using blocking.
1.4.2 Reducing bias in human experiments
Randomized experiments are the gold standard for data collection, but they do not ensure an
unbiased perspective into the cause and effect relationship in all cases. Human studies are perfect
examples where bias can unintentionally arise. Here we reconsider a study where a new drug was
used to treat heart attack patients. In particular, researchers wanted to know if the drug reduced
deaths in patients.
These researchers designed a randomized experiment because they wanted to draw causal con-
clusions about the drug’s effect. Study volunteers28 were randomly placed into two study groups.
One group, the treatment group, received the drug. The other group, called the control group,
did not receive any drug treatment.
27Thisisadifferentconceptthanacontrol group,whichwediscussinthesecondprincipleandinSection1.4.2.
28Humansubjectsareoftencalledpatients,volunteers,orstudy participants.
1.4. EXPERIMENTS 33
Numbered patients
1 7 13 19 25 31 37 43 49
l l l l l l l l l
2 8 14 20 26 32 38 44 50
l l l l l l l l l
3 9 15 21 27 33 39 45 51
l l l l l l l l l
4 10 16 22 28 34 40 46 52
l l l l l l l l l
5 11 17 23 29 35 41 47 53
l l l l l l l l l
6 12 18 24 30 36 42 48 54
l l l l l l l l l
create
blocks
Low−risk patients High−risk patients
l 2 l 17 l 36 l 47 l 1 1 l 2 2 l 4 3 l 2 4 l 8
l 5 l 21 l 37 l 50 l 3 1 l 4 2 l 5 3 l 5 4 l 9
4 15 26 38 51
l 6 l 23 l 39 l 53 l l l l l
7 18 27 40 52
8 29 41 54 l l l l l
l l l l
9 19 28 42
l l l l
13 33 45
l l l
10 20 30 43
l l l l
16 34 46
l l l 11 22 31 44
l l l l
randomly randomly
split in half split in half
Control
6 29 47 1 12 25 42
l l l l l l l
13 33 50 9 14 30 44
l l l l l l l
17 34 53 10 15 31 51
l l l l l l l
21 39 11 19 35 52
l l l l l l
Treatment
2 23 45 3 20 27 40
l l l l l l l
5 36 46 4 22 28 43
l l l l l l l
8 37 54 7 24 32 48
l l l l l l l
16 41 18 26 38 49
l l l l l l
Figure 1.16: Blocking using a variable depicting patient risk. Patients are first
divided into low-risk and high-risk blocks, then each block is evenly separated
into the treatment groups using randomization. This strategy ensures an equal
representation of patients in each treatment group from both the low-risk and
high-risk categories.
34 CHAPTER 1. INTRODUCTION TO DATA
Put yourself in the place of a person in the study. If you are in the treatment group, you
are given a fancy new drug that you anticipate will help you. On the other hand, a person in the
other group doesn’t receive the drug and sits idly, hoping her participation doesn’t increase her
risk of death. These perspectives suggest there are actually two effects: the one of interest is the
effectiveness of the drug, and the second is an emotional effect that is difficult to quantify.
Researchers aren’t usually interested in the emotional effect, which might bias the study. To
circumvent this problem, researchers do not want patients to know which group they are in. When
researchers keep the patients uninformed about their treatment, the study is said to be blind. But
there is one problem: if a patient doesn’t receive a treatment, she will know she is in the control
group. The solution to this problem is to give fake treatments to patients in the control group.
A fake treatment is called a placebo, and an effective placebo is the key to making a study truly
blind. A classic example of a placebo is a sugar pill that is made to look like the actual treatment
pill. Oftentimes,aplaceboresultsinaslightbutrealimprovementinpatients. Thiseffecthasbeen
dubbed the placebo effect.
The patients are not the only ones who should be blinded: doctors and researchers can ac-
cidentally bias a study. When a doctor knows a patient has been given the real treatment, she
might inadvertently give that patient more attention or care than a patient that she knows is on
the placebo. To guard against this bias, which again has been found to have a measurable effect
in some instances, most modern studies employ a double-blind setup where doctors or researchers
who interact with patients are, just like the patients, unaware of who is or is not receiving the
treatment.29
GUIDEDPRACTICE1.16
Look back to the study in Section 1.1 where researchers were testing whether stents were effective
at reducing strokes in at-risk patients. Is this an experiment? Was the study blinded? Was it
double-blinded?30
GUIDEDPRACTICE1.17
For the study in Section 1.1, could the researchers have employed a placebo? If so, what would that
placebo have looked like?31
You may have many questions about the ethics of sham surgeries to create a placebo after
reading Guided Practice 1.17. These questions may have even arisen in your mind when in the
general experiment context, where a possibly helpful treatment was withheld from individuals in
the control group; the main difference is that a sham surgery tends to create additional risk, while
withholding a treatment only maintains a person’s risk.
There are always multiple viewpoints of experiments and placebos, and rarely is it obvious
whichisethically“correct”. Forinstance,isitethicaltouseashamsurgerywhenitcreatesariskto
thepatient? However, ifwedon’tuseshamsurgeries, wemaypromotetheuseofacostlytreatment
that has no real effect; if this happens, money and other resources will be diverted away from other
treatments that are known to be helpful. Ultimately, this is a difficult situation where we cannot
perfectly protect both the patients who have volunteered for the study and the patients who may
benefit (or not) from the treatment in the future.
29Therearealwayssomeresearchersinvolvedinthestudywhodoknowwhichpatientsarereceivingwhichtreat-
ment. However, they do not interact with the study’s patients and do not tell the blinded health care professionals
whoisreceivingwhichtreatment.
30The researchers assigned the patients into their treatment groups, so this study was an experiment. However,
the patients could distinguish what treatment they received, so this study was not blind. The study could not be
double-blindsinceitwasnotblind.
31Ultimately,canwemakepatientsthinktheygottreatedfromasurgery? Infact,wecan,andsomeexperiments
use what’s called a sham surgery. In a sham surgery, the patient does undergo surgery, but the patient does not
receivethefulltreatment,thoughtheywillstillgetaplaceboeffect.
1.4. EXPERIMENTS 35
Exercises
1.29 Lightandexamperformance. Astudyisdesignedtotesttheeffectoflightlevelonexamperformance
of students. The researcher believes that light levels might have different effects on males and females, so
wantstomakesurebothareequallyrepresentedineachtreatment. Thetreatmentsarefluorescentoverhead
lighting, yellow overhead lighting, no overhead lighting (only desk lamps).
(a) What is the response variable?
(b) What is the explanatory variable? What are its levels?
(c) What is the blocking variable? What are its levels?
1.30 Vitamin supplements. To assess the effectiveness of taking large doses of vitamin C in reducing
the duration of the common cold, researchers recruited 400 healthy volunteers from staff and students at a
university. A quarter of the patients were assigned a placebo, and the rest were evenly divided between 1g
VitaminC,3gVitaminC,or3gVitaminCplusadditivestobetakenatonsetofacoldforthefollowingtwo
days. All tablets had identical appearance and packaging. The nurses who handed the prescribed pills to
the patients knew which patient received which treatment, but the researchers assessing the patients when
they were sick did not. No significant differences were observed in any measure of cold duration or severity
between the four groups, and the placebo group had the shortest duration of symptoms.32
(a) Was this an experiment or an observational study? Why?
(b) What are the explanatory and response variables in this study?
(c) Were the patients blinded to their treatment?
(d) Was this study double-blind?
(e) Participantsareultimatelyabletochoosewhetherornottousethepillsprescribedtothem. Wemight
expect that not all of them will adhere and take their pills. Does this introduce a confounding variable
to the study? Explain your reasoning.
1.31 Light,noise,andexamperformance. A study is designed to test the effect of light level and noise
levelonexamperformanceofstudents. Theresearcherbelievesthatlightandnoiselevelsmighthavedifferent
effects on males and females, so wants to make sure both are equally represented in each treatment. The
lighttreatmentsconsideredarefluorescentoverheadlighting,yellowoverheadlighting,nooverheadlighting
(only desk lamps). The noise treatments considered are no noise, construction noise, and human chatter
noise.
(a) What type of study is this?
(b) How many factors are considered in this study? Identify them, and describe their levels.
(c) What is the role of the sex variable in this study?
1.32 Musicandlearning. Youwouldliketoconductanexperimentinclasstoseeifstudentslearnbetter
iftheystudywithoutanymusic,withmusicthathasnolyrics(instrumental),orwithmusicthathaslyrics.
Briefly outline a design for this study.
1.33 Sodapreference. You would like to conduct an experiment in class to see if your classmates prefer
the taste of regular Coke or Diet Coke. Briefly outline a design for this study.
1.34 Exercise and mental health. A researcher is interested in the effects of exercise on mental health
and he proposes the following study: Use stratified random sampling to ensure representative proportions
of18-30,31-40and41-55yearoldsfromthepopulation. Next,randomlyassignhalfthesubjectsfromeach
age group to exercise twice a week, and instruct the rest not to exercise. Conduct a mental health exam at
the beginning and at the end of the study, and compare the results.
(a) What type of study is this?
(b) What are the treatment and control groups in this study?
(c) Does this study make use of blocking? If so, what is the blocking variable?
(d) Does this study make use of blinding?
(e) Comment on whether or not the results of the study can be used to establish a causal relationship
between exercise and mental health, and indicate whether or not the conclusions can be generalized to
the population at large.
(f) Suppose you are given the task of determining if this proposed study should get funding. Would you
have any reservations about the study proposal?
32C. Audera et al. “Mega-dose vitamin C in treatment of the common cold: a randomised controlled trial”. In:
Medical Journal of Australia 175.7(2001),pp.359–362.
36 CHAPTER 1. INTRODUCTION TO DATA
Chapter exercises
1.35 Petnames. ThecityofSeattle,WAhasanopendataportalthatincludespetsregisteredinthecity.
For each registered pet, we have information on the pet’s name and species. The following visualization
plots the proportion of dogs with a given name versus the proportion of cats with the same name. The 20
most common cat and dog names are displayed. The diagonal line on the plot is the x=y line; if a name
appeared on this line, the name’s popularity would be exactly the same for dogs and cats.
(a) Are these data collected as part of an
experiment or an observational study?
(b) What is the most common dog name?
What is the most common cat name?
(c) What names are more common for
cats than dogs?
(d) Is the relationship between the two
variables positive or negative? What
does this mean in context of the data?
1.36 Stressedout,PartII. In a study evaluating the relationship between stress and muscle cramps, half
the subjects are randomly assigned to be exposed to increased stress by being placed into an elevator that
falls rapidly and stops abruptly and the other half are left at no or baseline stress.
(a) What type of study is this?
(b) Can this study be used to conclude a causal relationship between increased stress and muscle cramps?
1.37 Chiaseedsandweightloss. Chia Pets – those terra-cotta figurines that sprout fuzzy green hair –
madethechiaplantahouseholdname. Butchiahasgainedanentirelynewreputationasadietsupplement.
In one 2009 study, a team of researchers recruited 38 men and divided them randomly into two groups:
treatment or control. They also recruited 38 women, and they randomly placed half of these participants
into the treatment group and the other half into the control group. One group was given 25 grams of chia
seeds twice a day, and the other was given a placebo. The subjects volunteered to be a part of the study.
After12weeks,thescientistsfoundnosignificantdifferencebetweenthegroupsinappetiteorweightloss.33
(a) What type of study is this?
(b) What are the experimental and control treatments in this study?
(c) Has blocking been used in this study? If so, what is the blocking variable?
(d) Has blinding been used in this study?
(e) Comment on whether or not we can make a causal statement, and indicate whether or not we can
generalize the conclusion to the population at large.
1.38 Citycouncilsurvey. A city council has requested a household survey be conducted in a suburban
area of their city. The area is broken into many distinct and unique neighborhoods, some including large
homes,somewithonlyapartments,andothersadiversemixtureofhousingstructures. Foreachpartbelow,
identify the sampling methods described, and describe the statistical pros and cons of the method in the
city’s context.
(a) Randomly sample 200 households from the city.
(b) Divide the city into 20 neighborhoods, and sample 10 households from each neighborhood.
(c) Dividethecityinto20neighborhoods,randomlysample3neighborhoods,andthensampleallhouseholds
from those 3 neighborhoods.
(d) Divide the city into 20 neighborhoods, randomly sample 8 neighborhoods, and then randomly sample
50 households from those neighborhoods.
(e) Sample the 200 households closest to the city council offices.
33D.C. Nieman et al. “Chia seed does not promote weight loss or alter disease risk factors in overweight adults”.
In: Nutrition Research 29.6(2009),pp.414–418.
1.4. EXPERIMENTS 37
1.39 Flawed reasoning. Identify the flaw(s) in reasoning in the following scenarios. Explain what the
individuals in the study should have done differently if they wanted to make such strong conclusions.
(a) Students at an elementary school are given a questionnaire that they are asked to return after their
parents have completed it. One of the questions asked is, “Do you find that your work schedule makes
it difficult for you to spend time with your kids after school?” Of the parents who replied, 85% said
“no”. Based on these results, the school officials conclude that a great majority of the parents have no
difficulty spending time with their kids after school.
(b) Asurveyisconductedonasimplerandomsampleof1,000womenwhorecentlygavebirth,askingthem
about whether or not they smoked during pregnancy. A follow-up survey asking if the children have
respiratory problems is conducted 3 years later. However, only 567 of these women are reached at the
same address. The researcher reports that these 567 women are representative of all mothers.
(c) An orthopedist administers a questionnaire to 30 of his patients who do not have any joint problems
and finds that 20 of them regularly go running. He concludes that running decreases the risk of joint
problems.
1.40 IncomeandeducationinUScounties. The scatterplot below shows the relationship between per
capitaincome(inthousandsofdollars)andpercentofpopulationwithabachelor’sdegreein3,143counties
in the US in 2010.
$60k
(a) What are the explanatory and response
variables?
(b) Describe the relationship between the two
$40k
variables. Makesuretodiscussunusualob-
servations, if any.
(c) Can we conclude that having a bachelor’s $20k
degree increases one’s income?
$0
0% 20% 40% 60% 80%
Percent with Bachelor's Degree
emocnI
atipaC
reP
1.41 Eatbetter,feelbetter? Inapublichealthstudyontheeffectsofconsumptionoffruitsandvegetables
on psychological well-being in young adults, participants were randomly assigned to three groups: (1) diet-
as-usual,(2)anecologicalmomentaryinterventioninvolvingtextmessagereminderstoincreasetheirfruits
and vegetable consumption plus a voucher to purchase them, or (3) a fruit and vegetable intervention in
whichparticipantsweregiventwoadditionaldailyservingsoffreshfruitsandvegetablestoconsumeontop
of their normal diet. Participants were asked to take a nightly survey on their smartphones. Participants
were student volunteers at the University of Otago, New Zealand. At the end of the 14-day study, only
participants in the third group showed improvements to their psychological well-being across the 14-days
relative to the other groups.34
(a) What type of study is this?
(b) Identify the explanatory and response variables.
(c) Comment on whether the results of the study can be generalized to the population.
(d) Comment on whether the results of the study can be used to establish causal relationships.
(e) A newspaper article reporting on the study states, “The results of this study provide proof that giving
young adults fresh fruits and vegetables to eat can have psychological benefits, even over a brief period
of time.” How would you suggest revising this statement so that it can be supported by the study?
34Tamlin S Conner et al. “Let them eat fruit! The effect of fruit and vegetable consumption on psychological
well-beinginyoungadults: Arandomizedcontrolledtrial”. In: PloS one 12.2(2017),e0171206.
38 CHAPTER 1. INTRODUCTION TO DATA
1.42 Screens,teens,andpsychologicalwell-being. In a study of three nationally representative large-
scale data sets from Ireland, the United States, and the United Kingdom (n = 17,247), teenagers between
the ages of 12 to 15 were asked to keep a diary of their screen time and answer questions about how they
felt or acted. The answers to these questions were then used to compute a psychological well-being score.
Additional data were collected and included in the analysis, such as each child’s sex and age, and on the
mother’s education, ethnicity, psychological distress, and employment. The study concluded that there is
little clear-cut evidence that screen time decreases adolescent well-being.35
(a) What type of study is this?
(b) Identify the explanatory variables.
(c) Identify the response variable.
(d) Comment on whether the results of the study can be generalized to the population, and why.
(e) Comment on whether the results of the study can be used to establish causal relationships.
1.43 StanfordOpenPolicing. TheStanfordOpenPolicingprojectgathers,analyzes,andreleasesrecords
from traffic stops by law enforcement agencies across the United States. Their goal is to help researchers,
journalists, and policymakers investigate and improve interactions between police and the public.36 The
following is an excerpt from a summary table created based off of the data collected as part of this project.
Driver’s No. of stops % of stopped
County State race per year cars searched drivers arrested
Apaice County Arizona Black 266 0.08 0.02
Apaice County Arizona Hispanic 1008 0.05 0.02
Apaice County Arizona White 6322 0.02 0.01
Cochise County Arizona Black 1169 0.05 0.01
Cochise County Arizona Hispanic 9453 0.04 0.01
Cochise County Arizona White 10826 0.02 0.01
··· ··· ··· ··· ··· ···
Wood County Wisconsin Black 16 0.24 0.10
Wood County Wisconsin Hispanic 27 0.04 0.03
Wood County Wisconsin White 1157 0.03 0.03
(a) What variables were collected on each individual traffic stop in order to create to the summary table
above?
(b) State whether each variable is numerical or categorical. If numerical, state whether it is continuous or
discrete. If categorical, state whether it is ordinal or not.
(c) Supposewewantedtoevaluatewhethervehiclesearchratesaredifferentfordriversofdifferentraces. In
thisanalysis,whichvariablewouldbetheresponsevariableandwhichvariablewouldbetheexplanatory
variable?
1.44 Spacelaunches. ThefollowingsummarytableshowsthenumberofspacelaunchesintheUSbythe
type of launching agency and the outcome of the launch (success or failure).37
1957 - 1999 2000 - 2018
Failure Success Failure Success
Private 13 295 10 562
State 281 3751 33 711
Startup - - 5 65
(a) What variables were collected on each launch in order to create to the summary table above?
(b) State whether each variable is numerical or categorical. If numerical, state whether it is continuous or
discrete. If categorical, state whether it is ordinal or not.
(c) Supposewewantedtostudyhowthesuccessrateoflaunchesvarybetweenlaunchingagenciesandover
time. In this analysis, which variable would be the response variable and which variable would be the
explanatory variable?
35Amy Orben and AK Baukney-Przybylski. “Screens, Teens and Psychological Well-Being: Evidence from three
time-usediarystudies”. In: Psychological Science (2018).
36Emma Pierson et al. “A large-scale analysis of racial disparities in police stops across the United States”. In:
arXiv preprint arXiv:1706.05678 (2017).
37JSRLaunchVehicleDatabase,Acomprehensivelistofsuborbitalspacelaunches,2019Feb10Edition.
39
Chapter 2
Summarizing data
2.1 Examining numerical data
2.2 Considering categorical data
2.3 Case study: malaria vaccine
40
This chapter focuses on the mechanics and construction of summary
statistics and graphs. We use statistical software for generating the
summaries and graphs presented in this chapter and book. However,
since this might be your first exposure to these concepts, we take our
time in this chapter to detail how to create them. Mastery of the
content presented in this chapter will be crucial for understanding the
methods and techniques introduced in rest of the book.
For videos, slides, and other resources, please visit
www.openintro.org/os

---
