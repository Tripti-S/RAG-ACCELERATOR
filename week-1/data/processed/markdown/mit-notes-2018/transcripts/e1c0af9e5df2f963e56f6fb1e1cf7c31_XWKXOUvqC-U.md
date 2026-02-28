# E1C0Af9E5Df2F963E56F6Fb1E1Cf7C31 Xwkxouvqc-U

---

MITOCW | MITRES6_012S18_L23-03_300k
We will now study what happens when we merge independent Poisson processes.
The story as well as the final conclusion is going to be similar to what happened for the case where we merged
independent Bernoulli processes.
In particular, we will see that the merged process will also be Poisson.
What is the story?
Suppose that you have two light bulbs.
One of them is red and flashes at random times that are described according to a Poisson process with a certain
rate, lambda1.
The other light bulb is green, flashes also as a Poisson process with a certain rate.
Furthermore, we assume that the two light bulbs are independent of each other.
If you're color blind so that the only thing that you see is flashes but without being able to tell the color, what kind
of process are you going to see?
Well, you will see a Poisson process also, and at this point, you can probably guess what the arrival rate is going
to be for this Poisson process.
It should be the sum of these two arrival rates of the processes that you started with.
So this will be our final conclusion, but we want to verify that this is indeed the correct conclusion.
So let us look at the situation in some more detail.
We have the two processes, two arrival processes-- the red one and the green one-- and the merged process is
formed by recording an arrival at any time where either of the two processes that you started with records an
arrival.
Let us now look at the time interval and think about the number of arrivals in the merged process during this time
interval.
What is that the number?
That number is equal to the number of arrivals that you have in the first process plus the number of arrivals that
you have in the second process.
Let's call those numbers N1 and N2 so that what we have here is N1 plus N2.
Now, N1 is a Poisson random variable because this is a Poisson process.
Similarly, N2 is a Poisson random variable.
We assume that these two processes are independent.
Therefore, N1 plus N2 is the sum of independent Poisson random variables, and therefore, N1 plus N2 is also a
Poisson random variable.
This is reassuring.
It's a good piece of evidence that the blue process is a Poisson process, but this is not enough.
To argue that it is a Poisson process, we need to check the defining properties of a Poisson process.
One defining property is the independence property.
If we take disjoint intervals, the number of arrivals here is independent, or should be independent, from the
number of arrivals there.
The argument here is exactly the same as for the Bernoulli case, so we will not go through it in any detail.
We just notice that whatever happens during that time has to do with whatever happens during those times in the
two processes that we started with.
And similarly, what happens in these times has to do with what happens in these two processes during those
times.
Because for each one of the two processes that we start with, we have the Poisson assumption so that this
interval is independent from that interval in the sense that arrivals here and arrivals there are independent.
So because of this, whatever happens during those times has nothing to do with whatever happens in those
times, so number of arrivals here is independent from the number of arrivals there.
The other property that we need to check is that the probability of recording an arrival during a small time interval
of length delta, that this probability has the right scaling properties, that it is linear in delta, in the length of this
interval, and that the probability of two or more arrivals here is negligible.
To see what happens during a typical interval in the merged process, we need to consider what is going to
happen during that typical interval in the other two processes and consider all the possible combinations.
During a little interval, the red process is going to have zero arrivals with this probability, one arrival with this
probability, and two or more arrivals with this probability, which is negligible.
Actually here, we're ignoring terms of order delta squared.
These are the correct expressions if we only focus on terms that are either constants or linear in delta.
We are ignoring terms that are of order delta square or higher.
And similarly for the green process, we have these probabilities for the number of arrivals that may happen during
a small interval.
For the merged process, we will have zero arrivals if and only if we have zero arrivals in the red process and zero
arrivals in the green process.
The probability of these two events happening, because we assume that the two processes that we started with
are independent, is going to be the product of the probabilities of zero arrivals in one process times zero arrivals
in the other process.
We multiply those two terms, and if we throw away the term delta squared, which is negligible, we see that this
event is going to happen with probability 1 minus lambda1 plus lambda2 times delta.
What's the probability that we get one arrival?
This is an event that can happen in two ways.
We could have one arrival in the red process and zero arrivals in the green process, and this combination
happens with this probability.
Alternatively, we could have one arrival in the green process and zero arrivals in the red process.
This is this event and it happens with this probability.
Having one arrival in the blue process can happen either this way or that way, so the probability of one arrival will
be the sum of these two probabilities.
And if we throw away terms that are order of delta squared, what we're left with is just lambda1 plus lambda2
times delta.
Finally, there's the possibility that the blue process is going to have two or more arrivals.
This happens if we have one red and one green arrival, which happens with this probability, or if anyone of the
processes has two or more arrivals, which would be terms here, here, and these would be the scenarios.
But we notice that each one of these scenarios has probability that's order of delta squared.
This term also has probability of order delta squared, so overall, the possibility that the blue process has two or
more arrivals-- this is something that has probability that's of order delta squared.
So during a typical small interval, there is probability proportional to the length of the interval of having one arrival,
and lambda1 plus lambda2 is the factor of this proportionality, and the remaining probability is assigned to the
event that there are zero arrivals.
There's essentially negligible probability of having two or more arrivals, but this together with the independence
assumption is exactly what comes in the definition of a Poisson process with an arrival rate equal to this number.
And so we have established that the merged process is a Poisson process whose rate is the sum of the rates of
the processes that we started from.

---
