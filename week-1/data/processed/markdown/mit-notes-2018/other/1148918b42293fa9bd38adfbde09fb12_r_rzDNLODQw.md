# 1148918B42293Fa9Bd38Adfbde09Fb12 R Rzdnlodqw

---

MITOCW | MITRES6_012S18_L22-08_300k
This segment is probably the most critical one for the purpose of understanding what the Poisson process really is
and how it behaves.
There will be almost no mathematical formulas.
But the segment will be quite dense in terms of conceptual reasoning.
So pay a lot of attention.
In a nutshell, we will argue that the Poisson process has memorylessness properties that are entirely similar to
those that we have seen for the Bernoulli process.
This should not be surprising, since the Poisson process can be thought of as a limiting case of the Bernoulli
process.
We will reason through these properties, not in the style of a formal mathematical proof, but with an intuitive
argument.
But I would like to assure you that the intuitive argument can be translated into a rigorous proof.
The first property is the following.
The process starts at time 0.
You come in and start watching at let's say time 7.
Or more generally, instead of time 7, suppose that you come in and start watching at some time, little t.
The important thing here is that little t is a constant.
It's a deterministic number.
Starting at that time, what will you see?
Well, the original process was Poisson.
This means that disjoint intervals in the original process are independent.
Therefore, disjoint intervals in the process that you will be seeing will also be independent.
Furthermore, during any little interval of length delta in the process that you see will still have probability lambda
times delta, approximately, of seeing and arrival.
Therefore, what you see also satisfies the properties of a Poisson process, and is itself a Poisson process.
Second, the original process was Poisson.
So different intervals are independent.
So whatever happens in this interval is independent from whatever happens in that interval.
But that interval corresponds to the future of the process, and therefore, the future of the process, what you get to
see, is independent from the past history.
And so the conclusion is that the process that you get to see is a Poisson process, which is independent of the
history until the time that you started watching.
And we say, therefore, that what you see is a fresh starting process.
The Poisson process starts fresh at time t.
We have the fresh start property.
And similar to the language we use for the Bernoulli process, the fresh start property means that you see a
process that's independent of the past and which has the same statistical properties as if this was time 0, as if the
process was just starting right now.
One consequence of this fresh start property is the following.
You start watching at time t.
And you're interested in the time it takes until the next arrival.
What are the properties of this random variable?
Well, since you have a fresh starting Poisson process at this time, this is the time until the first arrival in this fresh
starting Poisson process.
And the time until the first arrival in a process that is just starting, we know that it has an exponential distribution.
So this is going to be an exponential random variable with the same parameter, lambda.
Furthermore, because the process starts fresh, whatever happens in the future is independent from the past.
And so this random variable, the remaining time, is independent of whatever happened in the past until time t.
Now let us look at a somewhat different situation.
You start watching the process at time T1.
Time T1 is the time of the first arrival.
And you start watching from here on.
What is it that you're going to see?
Suppose that the first arrival happens, let's say, at time equal to 3.
So we're conditioning on this event.
In that case, you start watching the process at time 3.
And you also know that the first arrival happened at time 3.
But this fact about the first arrival happening at time 3 belongs to the history of the process until time 3.
This is information about the past, and does not affect what is going to happen after time 3.
The process after time 3 will be independent from the history until time 3 and whatever happened until that time.
So starting at that particular time 3, what you see is a Poisson process that is independent from the past.
Now, this argument is valid even if I were to use here a 3.5 or 3.4 or 3.7.
No matter when this first arrival occurred, what I see starting from this time is a Poisson process which is
independent from the past.
At the time of the first arrival, the process just starts fresh.
As a consequence of this, and by repeating the argument that we carried out for the remaining time until the next
arrival up here, we can repeat this argument and argue that the time until the next arrival in this fresh starting
process, this will also be an exponential random variable.
Now, this time until the next arrival is the difference between the second arrival time and the first arrival time.
And we denote it by T2.
What we just argued is that this time until the next arrival is going to be an exponential random variable.
And also, it is independent from the past.
And in particular, it is independent from T1.
So the time until the second arrival, starting from the first arrival, the second inter-arrival time is a random variable
that has an exponential distribution that is the same distribution as that of T1, and is independent from T1.
Now we can extend this argument and look at the kth inter-arrival time.
For example, if the arrival numbered k minus 1 occurred here, and the k arrival occurs here, this difference, here
we denote it by Tk, and by arguing in a similar way that the process starts fresh at this particular time, the time
until the next arrival will also be an exponential random variable with the same distribution.
And furthermore, will be independent from the past history, and therefore, independent from the earlier inter-
arrival times.
And this has lots of important implications.
For example, the time until the kth arrival, which is the sum of the first k inter-arrival times, is the sum of
independent, identically distributed, exponential random variables.
In particular, this means that we can find the PDF of Yk by convolving the exponential PDF of these inter-arrival
times, convolving this exponential PDF with itself k times.
And this is indeed one way to find the PDF of Yk.
But fortunately for us, we were able to find it with a much simpler argument.
And we already know what it is.
But this property here is also useful for finding the mean and the variance of Yk.
The mean of the sum is the sum of the means.
And since the random variables are independent, the variance of the sum is the sum of the variances.
We know what is the mean and the variance of an exponential.
And so by multiplying that by k, we obtain the mean of the kth arrival time and the variance of the kth arrival time.
And so we now know the mean and variance of the Erlang PDF of order k.
A second implication of this property is more theoretical, more conceptual.
Recall that we defined the Poisson process in terms of an independence assumption and an assumption on the
probability of arrivals during a small interval.
But we could have defined the Poisson process as follows.
Consider a sequence of independent, identically distributed exponentials.
Call them Tk.
And use these to define the arrival times.
This is a way of constructing a process.
What we argued in this segment is that a Poisson process under the original definition satisfies this new definition.
One can complete the argument to show that the two definitions are equivalent.
It is possible to argue that if we define an arrival process in this manner, this arrival process will also satisfy the
basic properties of the Poisson process.
This argument can indeed be carried out, but we will not go through it.
A final implication, which is a little more practical.
If you want to simulate the Poisson process, how would you do it?
Given what we now know, the most natural way is the following.
We generate independent, identically distributed, exponential random variables, using for example a random
number generator.
And then use these exponential random variables to construct the values of the inter arrival times.
And this way, construct a complete time history of the Poisson process.

---
