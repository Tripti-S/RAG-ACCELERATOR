# 7F4Bafaeaf3Fc2B5E4F88Afb273F7D3D Irkum3Nnxje

---

MITOCW | MITRES6_012S18_L19-02_300k
In this segment, we will first discuss and compare different views of the sum of independent identically distributed
random variables.
And then, we will conclude with a statement of the central limit theorem.
So let X1 up to Xn be independent identically distributed random variables that have a certain finite mean and
finite variance that we'll denote by mu and sigma squared.
In order to have a concrete example in our hands, let us assume that this random variable has a distribution, let's
say, a PDF, that ranges from minus 1 to plus 1 and has a mean of 0.
Let us look at the sum of these random variables.
The sum has a variance of n times sigma squared, which goes to infinity.
And correspondingly, the standard deviation of this random variable also grows to infinity.
This random variable takes values between minus n and plus n.
And because the variance and the standard deviation increase, this means that for larger and larger n, the width
of this distribution is going to be larger and larger.
We can obtain a different view of this sum if we divided by n in, which case, we obtain the sample mean.
In this case, the variance goes to 0 as n goes to infinity.
And as a consequence, the distribution is highly concentrated around 0.
This is also what the weak law of large numbers tells us.
The bulk of the distribution is concentrated in an arbitrarily small interval around 0.
So this width becomes smaller and smaller as n goes to infinity.
So in this case, we obtain a limiting distribution.
But this limiting distribution is trivial.
It's degenerate.
It's all concentrated on a single point.
How can we make it so that we obtain a limiting distribution that is more interesting?
The key is to divide not by n, but to divide by the square root of n.
This has the following effect.
The variance of this ratio is calculated as follows.
We take the variance of the numerator, which is n times sigma squared.
And then we divide by the square of this number, which is n.
And therefore, the variance is equal to sigma squared.
What's important here is that the variance stays constant.
No matter what n is, the width of this distribution is going to be more or less the same.
The distribution itself might change as n changes.
But the distribution-- at least in this case, where we assume 0 mean, the distribution stays in place.
It doesn't move to the right or to the left.
And its width stays the same.
So one can wonder, in the limit, as n goes to infinity, does this shape start to approach a certain limiting shape?
And if it does, what is the limiting shape that it approaches?
The central limit theorem will give us the answers to these questions.
The setting for the central limit theorem will be pretty much the setting that we were just discussing.
So we will be looking into the case where we divide the sum of the random variables by square root of n, except
for a few additional twists.
Since this ratio has a variance of sigma squared, it would help to divide by a further factor of sigma here so that
the variance is going to become 1.
And there's another issue.
If the mean of the X's is non-zero, then the distribution is centered at a quantity that keeps changing with n.
So the distribution will be drifting away from 0.
It's not staying in place.
And so it wouldn't have any hope of converging to something.
For this reason, instead of looking at this ratio in particular, what we do is we first subtract the mean of the sum,
which is n times the mean.
And then we divide by a further factor of sigma.
This random variable that we obtain here has nice properties.
The mean of this random variable is equal to 0, because we did subtract the mean of the X's.
And the variance of this random variable is going to be equal to 1.
The reason is that the variance is the variance of the numerator, which is n times sigma squared, divided by the
square of the denominator, which is also n times sigma squared.
So as n changes, the distribution of the random variable Zn stays in place.
It has a mean of 0.
And its width, more or less, stays the same, because we have a constant variance.
We will compare this random variable with a standard normal random variable that has 0 mean and unit variance.
The central limit theorem states the amazing fact that as n goes to infinity, the distribution of this random variable
converges to the standard normal distribution in the following sense-- that this probability here converges to that
probability for any choice of little z.
Now, what we have here is just the CDF of this random variable, Zn.
So it tells us that the CDF of the random variable Zn converges to the CDF of a standard normal.
And fortunately, for the standard normal, the CDF is available in tables.
So if we needed to calculate the numerical value here, we can just look up the normal tables.
And this suggests an approximation to this probability for the case where n is finite but large.
When n is large, we can approximate this probability by this probability on the right, which we can find from the
normal tables.
The central limit theorem is a very important result.
For this reason, we will spend some time discussing how to interpret it, what it means, how we use it, and we will
go through a few examples to see how we actually apply it.

---
