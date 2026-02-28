# 8D15Ee752050De0Caa9Faf9Ab78D8521 Mvgubqzzulm

---

MITOCW | MITRES6_012S18_L22-10_300k
In this segment, we go through an example to get some practice with Poisson process calculations.
The example is as follows.
You go fishing and fish are caught according to a Poisson process with an arrival rate-- that is the rate at which
fish are caught-- of 0.6 fish per hour.
You will fish for two hours no matter what.
And if during those two hours you have caught at least one fish, then you stop.
As in this scenario, in which you have caught three fish during the first two hours, and then you stop.
Otherwise, you will continue until you catch one fish.
And at that time, you will stop.
We will answer a few questions and we will write down the answers to these questions in terms of the notation that
we have introduced.
And here, for reference, we have all of the formulas that we have developed so far.
The first question is, what is the probability that you get to fish for more than two hours?
Well, you get to fish for more than two hours if and only if you didn't catch any fish during the first two hours.
So this is the probability of catching zero fish in the first two hours.
And we can use this formula.
Substitute k equal to 0, tau equal to 2, lambda equal to 0.6.
Plug in the numbers and obtain a numerical answer.
We will not bother [with] the numerical answers, we will just be writing down the expressions that give us the
answers.
Now, in this question we could have a different approach.
You will fish for more than two hours if and only if there are no arrivals during the first two hours, which means that
the first arrival in the Poisson process of fishing happens after time 2.
So we're talking about the event that the first arrival, T1, is bigger than 2.
And we're looking into the probability of this event, which is the integral of the density of the first arrival time.
And the integral is taken over the range of values of interest-- larger than 2.
That is, from 2 to infinity.
We know that this density is exponential, so we can write down this integral and evaluate it.
So notice the difference between these two approaches.
Here we think in terms of the random variables that correspond to the number of arrivals during a certain time
interval.
Here we're reasoning in terms of inter-arrival times.
And more generally, for Poisson process problems, an event of interest sometimes can be expressed in terms of
number of arrivals.
Or sometimes it can be expressed in terms of arrival and inter-arrival times.
Or sometimes both approaches are possible.
But usually one of the two approaches will be simpler than the other.
For example, here we already have a formula, whereas here we would need to evaluate an integral.
Here is now our next question, which is a little bit more complicated.
What is the probability that you get to fish for more than two hours, and also you get to fish for less than five
hours?
This is the scenario, again, that you fish for more than two hours, which means that no fish were caught during the
first two hours.
And then you continue fishing.
And by time 5 you have already caught your fish and you have left.
Now, it is convenient of thinking about the Poisson process as follows.
Think about the Poisson process of catching fish at the rate of 0.6 per hour as going on forever.
So there's a fisherman who fishes forever, except that this fisherman at either this time, under this scenario, or at
that time, under this scenario, raises a flag and says, OK, this is the time I should be stopping.
So even though the fisherman will stop fishing at this time, we can imagine the Poisson process keeps going on.
With this way of thinking, the fact that you stopped fishing before time 5 is the event and that the number of fish
caught, or the number of Poisson arrivals during the interval from 2 to 5 is at least equal to 1, larger than or equal
to 1.
So the event of interest consists of the intersection of two events, zero fish caught during the first two hours--
which has this probability-- and at least one arrival in the Poisson process between times 2 and 5-- this is a time
interval of length 3.
And having at least one arrival is 1 minus the probability of 0 arrivals in a time interval of length 3.
Notice that I'm multiplying those two probabilities here.
Why am I doing this?
In a Poisson process, whatever happens in disjoint time intervals are independent events.
So an event having to do with this interval-- the event that no fish were caught-- and the event that has to do with
this interval-- at least one fish caught, at least one arrival during this time interval-- these two events are
independent.
And this is why we can multiply their probabilities.
Now, let us think of the alternative approach, a different way of describing this event using arrival and inter-arrival
times.
What is this event?
This is the event that no arrival happened until this time, but an arrival happened before time 5.
So this is the event that the first arrival happens after time 2, but before time 5.
And we're looking at the probability of this event, which we can find by integrating the PDF of the first arrival time
from 2 until 5.
The next question is, what is the probability that we catch at least two fish?
Under this scenario, we catch one fish and we stop.
Therefore, this scenario must have materialized.
The event of catching at least two fish is the scenario that from time from 0 until 2, we caught at least two fish.
So we're talking about the probability of catching at least two fish, which is the probability of catching k fish during
a time interval of length 2, where k can be anything from 2 to infinity.
So this is the probability that the number of fish caught during these two time units is at least equal to 2.
And an alternative way of writing this expression so that we do not have to evaluate an infinite sum, it is 1 minus
the probability of catching 0 fish, and minus the probability of catching 1 fish.
If we were to write this in terms of arrival and inter-arrival times, we will catch at least two fish if and only if by the
time we stop-- which will be time 2-- we've had 2 arrivals, which means that the second arrival time happened
before time 2.
So we're looking into the probability that the second arrival time happened before time 2, which is the integral from
0 to 2 of the density of the second arrival time.
We have a formula for this density given by the Erlang PDF.
So we could take this expression, plug it in here, evaluate the integral, and obtain the same answer as we would
have obtained here.
Clearly, in this case as well, this first approach would be a simpler one because these probabilities are already
available to us.
The next question is the following.
Suppose that you already fished for three hours.
This is something that can only happen under the second scenario.
So no fish have being caught until time 2.
You continue.
No fish were caught until time 3.
And given that this event has occurred, what is the expected value of the future fishing time?
The expected value until a fish gets caught for the first time?
Well, the Poisson process starts fresh at time 3, no matter what happened in the past, no matter what information
we're given in the past.
Now you're sitting at time 3 and looking into the future.
You have a fresh starting Poisson process, as if this was the initial time.
Starting from this time, the time until the first arrival is going to have an exponential distribution with parameter
lambda, and the expected value of this distribution is equal to 1 over lambda.
Finally, let's look at a different type of question.
What is the expected value of the total time that you get to fish?
Let us introduce here some notation.
Let us call the total fishing time capital F.
And the total fishing time consists of two pieces.
There's a time until time 2 that you will be fishing no matter what.
And then there's going to be the remaining fishing time after time 2.
So now let's look at the expectation of the remaining fishing time after time 2.
Here there are two scenarios.
In the first scenario, you stop.
In the second scenario, you continue.
And we will take into account these two scenarios by using the total expectation theorem.
The first scenario happens with some probability.
This is the probability that you stop fishing at time 2.
And in that case, your remaining fishing time is going to be equal to 0 because you do not continue under that
scenario.
But there's the other scenario that you get to fish for more than 2 time units.
And then we multiply this term with the conditional expectation of the remaining fishing time, given that you got to
fish for more than 2 times units.
So what is this term?
The probability that you get to fish for more than 2 time units, this is the probability that no fish were caught during
the first time units.
This is the probability of the second scenario.
And then we have this conditional expectation.
Given that you didn't catch anything and, therefore, you will be continuing fishing, what is the expected amount of
time-- F minus 2-- that you will be fishing?
Now the Poisson process starts fresh at time 2.
So looking into the future, we're faced with a Poisson process and we're asking for the expected time until the first
arrival.
And this time has an expected value equal to 1 over lambda.
Our last question is of a similar type.
What is the expected number of fish you're going to catch?
Once more, we will break this into two pieces.
Number of fish caught during the first two hours, and number of fish caught during the remaining hours.
During the first two hours, the expected number of fish that you catch is given by this formula.
It is equal to lambda tau-- and in our case lambda is 0.6 and tau is equal to 2-- plus the expected number of fish
that are caught afterwards.
What is this expected value?
Again, we think in terms of the total expectation theorem.
There's one scenario that has a certain probability, and under that scenario you do not catch any fish.
So that doesn't give us any contribution.
Then there is this scenario, the second one, that has this probability of occurring.
The probability of catching no fish here, so that the second scenario materializes.
And if that second scenario materializes, how many fish are you going to catch after time 2?
It's going to be one fish with certainty.
And this is the final answer to this question.
Notice that in answering both of these questions we used the divide and conquer strategy twice.
We first divided the time horizon into two pieces and dealt separately with each one of the pieces.
And then in order to deal with this second piece-- the time after time 2-- we used divide and conquer into the two
different scenarios and using the total expectation theorem.

---
