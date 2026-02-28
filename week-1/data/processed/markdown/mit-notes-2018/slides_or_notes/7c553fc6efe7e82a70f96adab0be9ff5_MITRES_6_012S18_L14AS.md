# 7C553Fc6Efe7E82A70F96Adab0Be9Ff5 Mitres 6 012S18 L14As

---

LECTURE 14: Introduction to Bayesian inference
• The big picture
motivation, applications
problem types (hypothesis testing, estimation, etc.)
• The general framework
Bayes' rule , posterior
(4 versions)
point estimates (MAP, LMS)
performance measures)
(prob. of error; mean squared error)
examples
1
Inference: the big picture
redictions
Probability theory
Real world
(Analysis)
Decisions
Models
IS
In fere n ce tatist i cs
•
2
Inference then and now
• Then:
10 patients were treated: 3 died
10 patients were not treated: 5 died
Therefore ...
Now:
• Big data
• Big models
•
• Big computers
3
A sample of application domains
STATE COUNTS
17 SOLIDLY DEMOCRATIC 23 SOLIDLY RIPUBLICAN
11 TOSSUP
• Design and interpretation of experiments
ELECTORAL VOTE COUNTS
LIKELY DEMOCRATIC LIKELY REPUBLICAN
237 191
I IO TOSSUP
- polling •
Obama/Bden I Romne /Ryan
i
© Source unknown. All rights reserved. This content is excluded
from our Creative Commons license. For more information, see
https://ocw.mit.edu/help/faq-fair-use.
4
A sample of application domains
• marketing , advertising
• recommendation systems
- Netflix competition
•
•
t
5
A sample of application domains
S�P 500 INDEX (STANDARD & POOR'
as of 30-Mar2-007
1500
1450�-+--- - --+-- - - -+--- - --+-- - - t--- ---:""T"'rf"''rt-----l
• 1350
Finance
1300
12001---�.....,.,---,�
-
.,..+�� ��......,.,---,��.,-L�� ��'-,-:,
-
��,--,..,�----1
Ma 06 Jul06 Se 06 Nov06 Jan07 Mar07
6.0
·- 6 4. 0 l----+-- - ---+- - - +--- - -+--�- -+-- - -.+-- �----1
.o
0.0
::: 2
Cop�right 2007 Yahoo! Inc. http://financ�.�ahoo.co•/
•
© Source unknown. All rights reserved. This content is excluded
from our Creative Commons license. For more information, see
https://ocw.mit.edu/help/faq-fair-use.
6
A sample of application domains
systems biology
•
Life sciences
Chemotines.
Honnones
Swvival Fbetors
Tfansml11ers Grov.th Factors
genomics (e.g� I GFl) (e
s
.
er
g.
ot
, in
o
t
ni
e
n
r1
.
e
e
uki
tc.
n
)
s , (e.g., TGFo, EGF) ElClta
Ma
c
t
el
tix
U ar
I I I
I
...
"i""'
ldeoer-11"� tontia:!JlSI H$Un•i G:tl� GPCR
x,. x,. n n . . l » , ' '·. I�IT. - -r:- 1 o2-.e ol ,ml ), I • ... � -l " M 11 o ,· , . -3 "� $., M 2 n ? R1T- I I I RT� cdc42'i I Wm
it,2 )(fon :t,2 .: 1 .r: · �.. .;,: , :.I):! :s l:.m , '� l n ·l-. . · I / ' P� C ...____ G">2f0 S / / F'yr1Shc I
11 ...... ,.
x,.n.n "'.. •1 11'&1, .:.3I FAK O$hCVOlltd -
llo,1t491 ----- Pl I 3 K '\,_ ..-----rr-- G-Prote l n RRteis , Src i I
J(f,21,!
� ll't> ..!.2l l : J 1 H. .' 1 l irT_,m-n. ,. t,:ll • of , . , o - 't u f77'4 ,, , A i k t PK i C A cyc den l y a t s at e e M I E K GS I K -30
)l'.tll,I Akka
-"'l',l· " 1111 ll " ,, f ,. · , � l n ' O f" o l W. 'O : 4 " 1 I ,,s / NF-11.8 PK 4 A / I ......._" APC I
__1111111 ,.,,,.
111.ons.
-+--
JAKs
MEKK MAPK MKK P,.catenln
11,,m,1•
-..... STAT3..S
ll1
� ,17t:)2t
" M o· ·, • 'l'S •w � .:zt l
-
""·""'
11• • �,
� Cytoeh'ome C
e
1
_111w1. :::*ili Casp I a se9
llo, ltfl
-�•*·
C.SPM08 _::: ARF
.._ ....... , 1� 4, 11 ll" 110 o , ,· . , ) ,.. 2' 1 " 1 U 1 ,.,. 1 n S 0 'l FkO -1 I
mdm2
'- --+- - 8C l•2
J 'p53
11,.,011.t Sad � M1-
"'-11,'26. i:11:,:,:1&m:tl f:asR Ab S no e r n m SOf al i ly -Si .m
11,. . ,. llf,:!011�ia
�
, -tn': .;,:, 12 :s 59" ,n , . • llf,019�
11,,,,,...,.
I
•
neuroscience, etc., etc. Oeath tactors
(e.g. Fast., Tnf)
This image is in the public domain.
This image is in the public domain.
Source: Wikimedia.
Source: Wikimedia. 7
A sample of application domains
• Modeling and monitoring the oceans
• Modeling and monitoring global climate
• Modeling and monitoring pollution
• Interpreting data from physics experiments •
• Interpreting astronomy data
8
A sample of application domains
• Signal processing
communication systems (noisy ... )
speech processing and understanding
image processing and understanding
tracking of objects
positioning systems (e.g., GPS)
detection of abnormal events •
9
10
Hypothesis testing versus estimation
• Hypothesis testing:
unknown takes one of few possible values
aim at small probability of incorrect decision
Is it an airplane or a bird?
• Estimation:
numerical unknown(s)
aim at an estimate that is "close" to the true but unknown value
11
The Bayesian inference framework
e
• Unknown
• Where does the prior come fro m ?
- treated as a random va r iable
symmetry
Pe Ie
- prior distribution or
known range
earlier studies
• Observation X
subjective or arbitrary
x le I x le •
- observa tio n model P or
• Use appropriate version of the Bayes rule
= =
to find Pe lx(· 1 X x) or Ie lx(· 1 X x)
Pr •
lor Pe
x PSlx(· I X =x)
Observation Posterior
Process Calculation
Condi tional
PX IS
12
ELECTORAL VOTE DISTRIBUTION FOR OBAMA
ROMNEY 14.62% 84.59% OBAMA
The output of Bayesian inference
11 " Tlr
The complete answer is a posterior distribution:
6%
PMF PeixC· I x) or PDF feixC· I x) 5%
>-- 270
t:
....,- 4%
-< 3%
<O
0
cL 2%
"'-
1 %
0% ___________.....
NUMBER OF ELECTORAL VOTES
•
•
• •
© Source unknown. All rights reserved. This content is excluded
from our Creative Commons license. For more information, see
https://ocw.mit.edu/help/faq-fair-use.
.-------------,
Pe
X I
-
= x)
- X
. 1 1
•I
Pri or
- - I I
Observation Posterior Pe1x ( · I I Point Estimates
I
Error Analysis :
Process Calculation
etc.
:
Condi tional -- - ---- _._ - - -
13
PxJe
Point estimates in Bayesian inference
The complete answer is a posterior distribution :
I I
PMF PerxC- x) or PDF fe rxC- x)
estimate: (j = g(x)
(number)
e
I , I
I estimator: = g(X)
r I
=
(random va ri ab le)
• Maximum a posteriori probability (MAP):
I
Perx(O* x) = mrperx (8 1x )
I
I
fe rx(O* x) = mrfelx(81 x) ,
I xl
• ConditIonal expectation: E[e X = (LMS: L east Mean Squares)
14
Discrete 6. discrete X
• values of 6: alternative hypotheses
2>e(8') I e f
px(x) = PX le(x
)
0'
0 .6
0.3
• conditional prob of error:
0.1
0.11
=
P (fJ i=6 I X = x)
e smallest under the MAP rule
1
• overall probability of error:
2.
P(8 i=6 ) =2:P(8i=6 I X=x)px(x)
• MAP rule: fJ =
• I •
I x I
I
= 2:P(8 i= 6 6 = e)pe(e)
e
15
e,
Discrete continuous X
I
pe(e) fX le(x e)
pelx(e x) = fx(x)
I
• Standard example:
e
send signal E {l , 2, 3} I
fx(x) = LPe(e')fx le(x ef)
8'
x=e+w
w e
2
~ N(O , a ), indep. of
• conditional prob of error:
I
fX le(x e) = fw(x - e)
p(Bi=e l x=x)
0.6
smallest under the MAP rule
•
0.3
• overall probability of error:
0.1 ' - pee
e) e I
i= = f, P(e i= X = x )fx(x) dx
1
~
e
2 3
1
e
I
= LP(e i= e = e)pe(e)
e
• MAP rule:
16
Continuous 8, continuous X
fe(O) fX leCx ] 0)
fe lxCO ] x) = fx(x)
• linear normal models
J
fx(x) = fe(O')fx le(x ] 0') dO'
estimation of a noisy signal
8 and W: independent normals
multi-dimensional versions Cmany normal parameters, many observations)
- MAt
• estimating the parameter of a uniform
• 8 = g(X)
I.."?$
• interested in:
X: uniform[O, 8]
E[ce - 8)2 ] X x]
=
8: uniform [0 , 1]
E[ce - 8)2]
17
Inferring the unknown bias of a coin and the Beta distribution
• Standard example:
1 le(O) I
(0 1 k) = PK le(k 0)
leO
coin with bias 8; prior
e lK PK(k)
- fix n; K =number of heads J
PK(k) = le(O')PK le(k 0') dO'
1
leO
• Assume is uniform in [0, 1)
eIe ..
~ (1-19)
/1, • I )
- I<
PI' .
•
(k ~
- + +
1 Ok ( 1 _ 0) n - k
"Beta distribution , with parameters (k 1, n - k 1)"
d(n,k)
le(O) ~
• If prior is Beta: = 0"(1 - 0) 13
c
18
Inferring the unknown bias of a coin: point estimates
• Standard example:
{l " fJ _ ",1131
1 + +
e; 10 0 ( - 0) dO - ('" 13 1) 1
feU
- coin with bias prior
,
- fix n; K =number of heads
e
fe/K IJddB
I (0
feU E[e K = k) =
• Assume is uniform in [0, 1)
o
1 k ( )n k I
fe lK(O I k) = d(n, k) 0 1 - 0 - I I Ie + ) ... _I:
(I-e)
(J
of)
-:. -
• MAP estimate:
o
,
)
kin
=
BMAP
I
e e.,r
e
J)
[K
o€ 1
~ Ie)
("'l - (1- ~---
"'" Q)(
~I
l> fo-
•
....
~/e ("'-"=) e) =- 0
- Ie: t- I
-
1<1. ..
8
=
M AP ~ +-~
19
Summary
• Problem data: peO, pX leC I ·)
• Given the value x of X: find , e.g., pe lxC 1x )
("I
- using appropriate version of the Bayes rule Gf20 I'Ges)
-
e
• Estimator = g(X) Estimate Ii = g(x)
MAP : li = 9MAP(X) maximizes pe lx(e 1x )
MAP
1 xl
LMS : li = 9LMS(X) = E[e X =
LMS
•
20
MIT OpenCourseWare
https://ocw.mit.edu
Resource: Introduction to Probability
John Tsitsiklis and Patrick Jaillet
The following may not correspond to a particular course on MIT OpenCourseWare, but has been provided by the author as an individual learning resource.
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
