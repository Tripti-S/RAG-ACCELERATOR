# 8701Cff8B5Ca00C9B6218Ec5B13B8Bd4 3Vmztgudtvw

---

MITOCW | MITRES6_012S18_S23-02_300k
In this video, we're going to establish a nice property of the Poisson process.
Here is our setting.
We have a Poisson process with arrival rate, lambda, and so arrivals keep coming.
And we watch this process until a certain random time, T.
So T is this time here.
Now, T is an exponential random variable with some parameter, and T is independent from the Poisson arrival
process.
What we're interested in is the number of arrivals that happened during this time.
How can we answer this question?
There are two ways.
One is using mathematical manipulations.
The other is using intuition.
Let's see what it would take if we wanted to solve the problem using formulas.
So let's call N-T, with capital T, the number of arrivals until time T in our Poisson process.
And we wish to find the distribution of N-T. So we want to calculate, for example, the probability that N-T is equal
to a specific number, k.
Now, we do not know very much about this random variable, but we do know the probability of the random
variable, N-T, If we have a deterministic time.
So perhaps we can condition by fixing the value of the random variable, capital T-- that is, to condition on that
random variable, taking on a specific value.
What happens in this case?
Well, if I tell you that capital T is equal to little t, this probability is going to be the same as the probability that N
with little t is equal to k, where N with little t is the number of arrivals until time, little t.
But the number of arrivals, until a certain time, is a Poisson random variable.
So we do know what this probability is.
It is lambda to the k, e to the [minus] lambda t, divided by k factorial.
Now, if we have this conditional probability, how can we get the unconditional probability?
This is done by using the total probability theorem.
We consider all possible values of little t, which are all the numbers from 0 to infinity.
We weigh each possible value of little t according to the corresponding PDF of the random variable, T.
And we have this equality.
We know what this term is.
It is this expression.
And the density of capital T, since it is an exponential variable, the density takes this form.
And so, in order to find the distribution of the random variable, N capital T, all that we need to do is to calculate
this integral.
But this is a rather messy integral.
So let us try to see if we can find a shortcut to this problem.
So here is what we have.
We have a Poisson process.
Let's call it the first Poisson process, that has a certain rate, lambda.
And this Poisson process has arrivals at various times.
And then we have a random variable, capital T, which is exponential.
How should we think about an exponential random variable?
We can think of an exponential random variable as being the first arrival in some Poisson process.
So let us put down a second Poisson process with rate mu.
Since we have assumed that capital T is independent from the red Poisson process, we can just assume that this
blue Poisson process is independent from the first.
Now, let us merge the two processes.
And we're going to form a merged process that records an arrival at those times at which either of the two
processes have an arrival.
This is the time of interest.
And the random variable that we're interested in is the number of red arrivals until that time.
That random variable we call N capital T. The discussion will be a little simpler if we define another random
variable, K, which is N capital T plus 1.
So K is the number of arrivals in the merged process until this time.
That is, we take those arrivals of the red process, and we also include that arrival here.
So if the number of arrivals that we got here was N capital T, here we have arrivals 1, 2, and so on.
And this is arrival number K. So K is a random variable, and we want to find what it is.
So what are we asking?
What is K?
K is the number of arrivals in the merged process until you get an arrival in the merged process which is coming
from the blue process.
And now, here is how we can think of this situation.
Think of each arrival in the merged process as a trial.
Each one of these arrivals is coming either from the red process or from the blue process.
Let us call it a success if it comes from the blue process.
So in that case, K is the number of trials until we have a success.
K is the number of arrivals in the merged process until we have a successful arrival, meaning one that came out of
the blue process.
So what do we know about those trials?
What are their statistical properties?
First, what is the probability of success?
The probability of success is the probability that when you get an arrival in the merged process, it is coming from
the blue process.
And as we have seen, given an arrival in the merged process, there is probability that it's coming from this
particular process that's proportional to the arrival rate of that particular process.
And it is equal, as we have discussed before, it is equal to this.
In addition, we have discussed that when you look at the merged process, and you ask, what was the origin of
that arrival, and you ask, what was the origin of that arrival, the answers to these two questions are independent
of each other.
In other words, the origin of this arrival is statistically independent from the origin of that arrival.
So this means that these trials are independent.
So what we're looking at is a random variable, which is the number of trials until the first success, in a sequence of
independent trials, where each trial has a success probability equal to that value.
And we know what that distribution is.
It is a geometric with this particular parameter.
This gives us the probability distribution of the random variable, K, and once you have the PMF of K, you just shift
it by 1 to the left in order to get the probability distribution, the PMF, of the random variable, N capital T.
And so this is the answer to this problem.
The number of arrivals during an exponentially distributed time interval [has] a geometric distribution that's shifted
by 1 to the left.

---
