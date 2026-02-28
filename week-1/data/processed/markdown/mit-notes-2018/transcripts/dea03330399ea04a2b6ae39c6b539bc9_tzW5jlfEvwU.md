# Dea03330399Ea04A2B6Ae39C6B539Bc9 Tzw5Jlfevwu

---

MITOCW | MITRES6_012S18_L22-04_300k
The definition of the Poisson process gives us information about the probability that we get k arrivals during an
interval of length delta when delta is a very small number.
How can we find the probability of k arrivals during an interval of some general length tau, where tau is no longer
a small number?
In particular, we're interested in the random variable denoted N sub tau, which stands for the number of arrivals
during an interval of length tau.
And we wish to find the PMF of this random variable, the probability that N sub tau is equal to k, and which is what
we have been denoting by this particular notation in the context of the Poisson process.
Now if, instead of the Poisson model, we had for the Bernoulli process model, we would know the answer.
S, the number of successes, or number of arrivals in n slots, has a PMF which is given by the binomial formula.
Can we somehow use what we know about the Bernoulli process to find the answer for the Poisson process?
The answer is yes, and it involves a limiting argument of the following kind.
We take the interval from 0 to t and divide it into a very large number of intervals, so many of them, where each
one of the intervals has a length of delta, where delta is a small number.
And to push the analogy with the Bernoulli process, we will be calling those little intervals as slots.
Now during each slot, we may get zero arrivals, one arrival, but there's also the possibility that there may be two
arrivals, or even more than two arrivals, happening during one of the slots.
Because of this, the picture that we have here is not quite the same as for the Bernoulli process because in the
Bernoulli process, each one of the slots will get only 0 or 1.
So the source of the discrepancy between the two models is that here, a slot may obtain two or more arrivals.
But how likely is this?
Let us look at the probability that some slot, that is, any one of the slots, contains two or more arrivals.
That is, we're dealing with the union of the events that slot i has two or more arrivals.
This event is the union of these events and, therefore, the probability of this event is less than or equal than the
sum of the probabilities of the constituents events.
This is an inequality that we have seen at some point in the past.
And we're calling it to the union bound.
Now what is this summation?
i ranges over the different slots.
And we have tau over delta slots, so there's so many terms that are being summed.
Now, during any particular slot, the probability of two or more arrivals is of order delta squared, according to the
definition of the Poisson process.
And this quantity converges to 0 when we let delta become smaller and smaller.
So this means that the discrepancy between the Poisson and the Bernoulli model, which was due to the possibility
that we might get two or more arrivals during one of those slots, this discrepancy is something that happens with
negligible probability.
In other words, the probability that we get k arrivals in the Poisson model is approximately the same as the
probability that k slots have an arrival.
Since we're neglecting the possibility that some slot has two or more arrivals, this means that the number of
arrivals in the Poisson model will be the same as the number of slots that get an arrival.
This approximate equality becomes more and more exact as we let delta go to zero.
But now what is this quantity?
The probability that k slots have an arrival is something that we can calculate using the binomial probabilities.
Each one of the slots has a certain probability of having an arrival.
And different slots are independent of each other by the defining properties of the Poisson process.
Therefore, this approximation that we have developed satisfies the properties of the Bernoulli process.
We have a certain probability that each slot gets an arrival.
And we have independence across slots.
This means that we can use now the PMF that's associated with the Bernoulli model to calculate this quantity and
then take the limit, as delta goes to 0, to obtain a formula for the PMF for the Poisson process.
In more detail, what we have is the number of arrivals, which is approximately the same as the number of slots
that have an arrival, obeys a binomial distribution in the limit as delta goes to 0-- a binomial distribution in which
the probability of arrival during each one of the slots is approximately lambda delta and the number of slots goes
to infinity.
And this happens in a way so that the product of the two, n times p, is equal to-- this term times this term gives us
a lambda times tau.
This term times this term gives us something that's order of delta.
So it's negligible.
So we have this equality, and so this is approximately lambda tau with the approximation becoming more and
more exact as we let delta go to zero.
So all we need to do is to take the formula for the Bernoulli process.
Use these values of p and n and take the limit.
But this is a problem that we have already encountered and have analyzed.
If we let n go to infinity, p goes to 0 so that their product stays constant, we have shown that the binomial PMF
converges to the so-called Poisson PMF that takes this form.
Notice one small difference-- n times p here is equal to lambda, whereas here, n times p is equal to lambda t.
This means that we need to apply this formula, but with lambda replaced by lambda t, and this gives us the final
answer.
This is the probability of k arrivals during a time interval of lenght t in the Poisson process.
And this is a so-called Poisson PMF with parameter lambda tau.
To summarize, our strategy was to argue that the Poisson process is increasingly accurately described by a
Bernoulli process if we discretize time in a very fine discretization.
And the approximation becomes exact in the limit when the discretization is very fine.
So we took the corresponding binomial formula for the Bernoulli process and took the limit to that's associated
with the parameters that we would obtain if we have a very fine discretization.
And this gave us the final formula.

---
