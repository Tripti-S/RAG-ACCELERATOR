# B343Ddecdd393Da2822Aecd2608Eb5F0 Mitres 6 012S18 L13As

---

LECTURE 13: Conditional expectation and variance revisited;
Application: Sum of a random number of independent r.v.'s
• A more abstract version of the conditional expectation
view it as a random variable
the law of iterated expectations
• A more abstract version of the conditional variance
view it as a random variable
the law of total variance
• Sum of a random number
of independent r.v.'s
mean
variance
1
as a
Conditional expectation random variable
• Function h • Random variable X; what is heX)?
~x2
e.g., hex) = x 2 , for all x • heX) is the r.v. that takes the value x 2 ,
if X happens to take the value x
2:
• g(y) = E[X Y = y] = xpx lY (x y)
I I
-==
(integral in contimfous case)
<)('1)
I
• g(Y) : is the r.v. that takes the value E[X Y = y],
if Y happens to take the value y
• Remarks:
Definition: E [X IY] = g(Y)
It is a function of Y •
It is a random variable
Ha s a distribution, mean, variance, etc.
2
I
The mean of E[X Y]: Law of iterated expectations
• g(y) = E[X Y = y]
I
I
E [E[X YJ] = E[X]
If]
[[x I ~ ~ (y )
E[I'('OJ
E [~[X I ~]l ::
Z
P'f (/)
~ rr(i)
/
[xl
" ~ f '1'= / ] P'( (1)
teA
R
'/ . to fJ
e?<
f[-Y]
=
3
Stick-breaking example
fy(y)
e
• Stick example: stick of length
break at uniformly chosen point Y
e
break what is left at uniformly chosen point X
y
1--­
I
fxl>'(x y)
I Y/2
• E[X y = y ) =
Y!i
I
=
• E[X Y)
•
y x
4
Forecast revisions
• Suppose forecasts are made by calculating expected value,
I~:::'----+~::::::::::=;~
• X: February sales ..,
E[X}
• Forecast in the beginning of the year:
• End of January: will get new information, value y of Y
E[X/Y:Y]
Revised forecast:
• Law of iterated expectations:
5
The conditional variance as a random variable
var(X) = E [( X - E[X])2 ]
Y]
var(X I Y = y) = E [(X - E[X I Y = y])21 Y =
7 •
- -
I I
var(X Y) is the r.v. that takes the value var(X Y = y), when Y = y
"/1
!
YJ 2­
• Example: X uniform on [0, var(X Y = y) =
I
'ill
Y
Q
var(X Y) = /' ""
I
I + I YJ)
Law of total variance: var(X ) = E [var(X Y) ] var(E[X
6
Derivation of the law of total variance
1
I + I • var(X) = E[X2] - (E[X])2
var( x~ = E [var(X Y) var (E[X Y] )
r­
y] - ( f [ J
X'-j
I x)
var(X Y) = [ [ y
}'(])1
£[x - [ ( ""
~ ~var(X ~]
E Y) =
I
'-::-:-_...../
-+
-
I
var(E[X Y]
7
n ]
A simple example I + I
var( X ) -; E [Var(X var (E [X Y] ) .,. :P­
ya
-:: "11.'1
9/1,
t-
! 7
I 1/12­
xl var(X Y = 1) =
Ix(
I
var(X Y) = ' - .22; ..,
I I' = i2
I
/ ' ";:- var(X Y = 2) = /12
II' '--,
~ '---
'--- ' -
'-----
'­
' 1 ' - 1 ) ­
I
q; .
=
1 3 x E [var(X I Y) ] = 12- + ~ • L ~ t '-t
Y= 1 Y=2
,
"i"
'Ii
I
E[X Y = 1] = 5"")2­
i '
I 2I ' -
=/ YJ)
I
E[X I Y] var(E [X = --'1
1
~I
E[X Y = 2] =
I
Ii
:2.
I I I ,- '1 16
'"i ...
r[x]
E [E[X I YJ] = ~ It. • ~ ="Zj:
8
Section means and variances
• Two sections of a class: y = 1 (10 students); y = 2 (20 students)
x;: score of student i
• Experiment: pick a student at random (uniformly)
random va ri ab les: X and Y
1 10 1 30
L: L:
• Data : Y = 1 : Xi = 90 Y = 2 : Xi = 60
10 20
i =1 i = l1
10
L'X.
I
~ ~(~tl.JO+bO·tO)=:t-o
• E[X) = ~
90
'3
(~I
'30 E[X Y) =
E[X Y = 1) = I
I
il3 60
= =
I b
E[X Y 2) 0
:l 6 =
I f-
-. ': !)o". •• 0 0
I
• E [E[X Y )] = 3
~.
9
Section means and variances (ctd.)
w.p. 1/ 3 E [E(X I Y] ] = 70 = E(X]
E(X Y] = 90,
I
60, W.p. 2 / 3
~t f 2­
= ~(,?O-tO) ('0-1-0) ~:tOO
var(E(XIY])
1 10 1 30
L L
• More data: c-:c (Xi - 90)2 = 10 (Xi - 60)2 = 20
10 =1 20 i=l1
i
-/3 _
10
10
var(X I Y = 1) = var(X I Y) = •
:20
2/3
20
var(X I Y = 2) =
f .
lOt; .
:4
E [var(X I Y) ] = 0 ==
i->
+;to
var (X ) = E [var(X I Y) ] + var (E(X I Y] ) -:: 5'0 0
var(X) = (average variability within sections)+ (variability between sections)
•
10
J
Sum of a random number of independent r.v.'s
( E[Y] = E[N ] . E[X]
• N: number of stores visited
• X i : money spent in store i
eN
is a nonnegative integer r.v.)
- X i independent, identically distributed
+ .. . +
• L et Y = Xl X
N - independent of N
/N='>1.J; !I11='"'-]
f[X,+" ..
t-X,••.
[[X" .. dX
" E[Y N = n] =
I
Iv
1
::£[X,-1- •• E[,<j
o+'x... = 'n
(£['(}N] :: N[['>r]
• Total expectation theorem:
Ddf[X]
[x]
L -= .,- 'VL.f -=.f
I
E[Y] = pN(n) E[Y N = n] 0 ( .... )
.... 111/
n I '
• L aw of iterated expectations:
11
Variance of sum of a random number of independent r. v.'s
+
var( Y) = E [var(Y I N)] var(E [Y I N] )
o
+
va r(Y) = E [N] var (X ) (E[X])2 var (N )
• E[Y N] = N E[X]
I
• var E[Y IN] =
lIa" (?(",~ 000+'1"", /N=''''')::::VOJ' (x,-I- o -I-X",)
• var(Y IN=n) =
, .
uar(x)
=1l1.
( (x)
var(Y IN) = /VVQ.f'
=E[N ErN]
00.(' (X)] ::. Vel.'" (,,)
E [var(Y IN)]
12
MIT OpenCourseWare
https://ocw.mit.edu
Resource: Introduction to Probability
John Tsitsiklis and Patrick Jaillet
The following may not correspond to a particular course on MIT OpenCourseWare, but has been provided by the author as an individual learning resource.
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
