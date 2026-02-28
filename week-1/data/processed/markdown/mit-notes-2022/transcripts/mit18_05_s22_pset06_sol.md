# Mit18 05 S22 Pset06 Sol

---

18.05 Problem Set 6, Spring 2022 Solutions
Problem 1. (10 pts.) Continuous MLE
Suppose we have a distribution with the following pdf (called a gamma distribution)
𝑎5
𝑓(𝑥|𝑎) = 𝑥4e−𝑎𝑥.
(4)!
Suppose we have independent data 𝑥 , 𝑥 , … , 𝑥 drawn from this distribution. Find the
1 2 𝑚
maximum likelihood estimate (MLE) for 𝑎.
Suggestion: The likelihood can be compactly written in terms of the sum S and the product
P of the data.
𝑎5
Solution: The likelihood for 𝑥
𝑖
is 𝑓(𝑥
𝑖
|𝑎) =
4!
𝑥4
𝑖
e−𝑎𝑥 𝑖 . So, the likelihood of the data is
𝑚 𝑎5𝑚
𝑓(data|𝑎) = ∏𝑓(𝑥 |𝑎) = 𝑃4e−𝑎𝑆,
𝑖 (4!)𝑚
𝑖=1
where 𝑃 = ∏𝑥 (product of data) and 𝑆 = ∑𝑥 (sum of data).
𝑖 𝑖
So, the log likelihood is
𝑙(𝑎) = 5𝑚 ln(𝑎) + 4 ln(𝑃)−𝑎𝑆 −𝑚 ln(4!).
Taking the derivative and setting it to 0, we get
5𝑚 5𝑚
𝑙′(𝑎) = −𝑆 = 0 ⇒ The MLE 𝑎̂= .
𝑎 𝑆
Note: It turns out, the distribution mean is 5/𝑎 and 𝑎̂ = 5/(𝑆/𝑚) = 5/𝑥, where 𝑥 is the
data mean.
Problem 2. (25: 5,10,10 pts.) Least squares
In this problem we will use maximum likelihood estimates to develop Gauss’ method of least
squares for fitting lines to data.
Bivariate data means data of the form
(𝑥 , 𝑦 ), (𝑥 , 𝑦 ), … , (𝑥 , 𝑦 ).
1 1 2 2 𝑛 𝑛
For bivariate data the simple linear regression model assumes that, for some values of the
parameters 𝑎 and 𝑏, we have
𝑦 = 𝑎𝑥 + 𝑏 + random measurement error.
𝑖 𝑖
The model assumes the measurement errors are independent and identically distributed and
follow a N(0, 𝜎2) distribution. (The values 𝑥 may or may not be random.)
𝑖
In general terms, we can say that the value of 𝑥 ‘explains’ the value of 𝑦 except for some
random noise. Graphically, the model says to make a scatter plot and find the line that best
fits the data. This is called a simple linear regression model.
1
18.05 Problem Set 6, Spring 2022 Solutions 2
It turns out that, under some assumptions about random variation of measurement error,
one way to find a “best” line is by solving a maximum likelihood problem.
The goal is to find the values of the model parameters 𝑎 and 𝑏 that give the MLE for this
model. To guide you, we note that the model says that
𝑦 ∼ N(𝑎𝑥 + 𝑏, 𝜎2).
𝑖 𝑖
Also remember that you know the density function for this distribution.
(a) For a general datum (𝑥 , 𝑦 ) give the likelihood and log likelihood functions (these will
1 1
be functions of 𝑦 , 𝑥 , 𝑎, 𝑏, and 𝜎.)
1 1
Solution: Since 𝑦 ∼ N(𝑎𝑥 + 𝑏, 𝜎2) the likelihood with data (𝑥 , 𝑦 ) is
𝑖 𝑖 1 1
1
𝑓(𝑥 ,𝑦 |𝑎,𝑏,𝜎) = √ e−(𝑦 1 −𝑎𝑥 1 −𝑏)2/(2𝜎2).
1 1
2𝜋 𝜎
The log likelihood is
√ (𝑦 − 𝑎𝑥 − 𝑏)2
ln(𝑓(𝑥 ,𝑦 |𝑎,𝑏,𝜎)) = − ln( 2𝜋 𝜎) − 1 1 .
1 1 2𝜎2
(b) Consider the data (1, 8), (3, 2), (5, 1). Assume that 𝜎 = 3 is a known constant and find
the maximum likelihood estimate for 𝑎 and 𝑏.
Note: since there are two variables 𝑎 and 𝑏, in order to find a critical point you will have
to take partial derivatives and set them equal to 0. This part of the problem takes a fair
amount of tedius algebra –sorry.
Note: We gave you a specific value of 𝜎, to avoid the distraction of one more symbol. If
you look at your calculations, you should see that the value of 𝜎 plays no role in finding the
MLE for 𝑎 and 𝑏. We get the same answer no matter what the value.
Solution: The likelihood for all the data is the product of the individual likelihoods. So,
3
1
𝑓((1,8), (3,2), (5,1) |𝑎,𝑏,𝜎) = ( √ ) e−((8−𝑎−𝑏)2+(2−3𝑎−𝑏)2+(1−5𝑎−𝑏)2)/(2𝜎2)
2𝜋 𝜎
Taking the natural log (and replacing the list of data by the word ‘data’) we get
√ (8−𝑎−𝑏)2+(2−3𝑎−𝑏)2+(1−5𝑎−𝑏)2
ln(𝑓(data | 𝑎, 𝑏, 𝜎)) = −3 ln( 2𝜋𝜎)−
2𝜎2
Since we want to find 𝑎 and 𝑏 that maximize the likelihood we take the partial derivatives
and set them to 0.
𝜕 ln(𝑓(data) | 𝑎, 𝑏, 𝜎) 2
= ((8−𝑎−𝑏)+3(2−3𝑎−𝑏)+5(1−5𝑎−𝑏)) = 0
𝜕𝑎 2𝜎2
𝜕 ln(𝑓(data) | 𝑎, 𝑏, 𝜎) 2
= ((8−𝑎−𝑏)+(2−3𝑎−𝑏)+(1−5𝑎−𝑏)) = 0
𝜕𝑏 2𝜎2
These are two equations in the unknowns 𝑎 and 𝑏. We simplify and solve:
35𝑎 + 9𝑏 = 19
which gives 𝑎 = −7/4 = −1.75; 𝑏 = 107/12 ≈ 8.917.
9𝑎 + 3𝑏 = 11
18.05 Problem Set 6, Spring 2022 Solutions 3
The linear regression fit of a line to the data is 𝑦 = 𝑎𝑥 + 𝑏 = −7𝑥/4 + 107/12.
(c) Use R to plot the data and the regression line you found in part (ii) The commands
plot(x,y, pch=19) and abline() will come in handy. For abline be careful: the param-
eter a is the intercept and b is the slope – exactly the opposite of our usage. Print the plot
and turn it in.
Solution: Here is the code for this plot:
x = c(1,3,5)
y = c(8,2,1)
a = -7/4
b = 107/12
plot(x, y, pch=19, col='blue')
#Perversely, in abline a is the intercept and b is the slope.
abline(a=b, b=a, col='orange', lwd=2)
1 2 3 4 5
8
7
6
5
4
3
2
1
x
y
Problem 3. (15: 10,5 pts.) Estimating uniform parameters
(a) Suppose we have data 1.2, 2.1, 1.3, 10.5, 5 which we know is drawn indepenedently
from a uniform(𝑎, 𝑏) distribution. Give the maximum likelihood estimate for the parameters
𝑎 and 𝑏.
Hint: in this case you should not try to find the MLE by differentiating the likelihood
function.
Solution: The pdf for uniform(𝑎, 𝑏) distribution takes two values
1/(𝑏 − 𝑎) if 𝑥 is in [𝑎, 𝑏]
𝑓(𝑥 | 𝑎, 𝑏) = {
0 otherwise
Since the likelihood is the product of the likelihoods of each data point, the likelihood
function is
1/(𝑏 − 𝑎)5 if all data is in [𝑎, 𝑏]
𝑓(data | 𝑎, 𝑏) = {
0 if not
This is maximized when (𝑏 − 𝑎) is as small as possible. Since all the data has to be in the
interval [𝑎, 𝑏] we minimize (𝑏 − 𝑎) by taking 𝑎 = minimum of data and 𝑏 = maximum of
data.
Answer: 𝑎 = 1.2, 𝑏 = 10.5 .
18.05 Problem Set 6, Spring 2022 Solutions 4
(b) Suppose we have data 𝑥 , 𝑥 , … , 𝑥 which we know is drawn indepenedently from a
1 2 𝑛
uniform(𝑎, 𝑏) distribution. Give the maximum likelihood estimate for the parameters 𝑎 and
𝑏.
Solution: The same logic as in part (a) shows 𝑎 = min(𝑥 , … , 𝑥 ) and 𝑏 = max(𝑥 , … , 𝑥 ) .
1 𝑛 1 𝑛
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
