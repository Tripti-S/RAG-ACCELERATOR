# 0Efce5573E22478Ef2Bde873D509D4Ac Ubqcqfh33G0

---

MITOCW | MITRES6_012S18_L03-07_300k
Suppose I have a fair coin which I toss multiple times.
I want to model a situation where the results of previous flips do not affect my beliefs about the likelihood of heads
in the next flip.
And I would like to describe this situation by saying that the coin tosses are independent.
You may say, we already defined the notion of independent events.
Doesn't this notion apply?
Well not quite.
We defined independence of two events.
But here, we want to talk about independence of a collection of events.
For example, we would like to say that the events, heads in the first toss, heads in the second toss, heads in the
third toss, and so on, are all independent.
What is the right definition?
Let us start with intuition.
We will say that a family of events are independent if knowledge about some of the events doesn't change my
beliefs, my probability model, for the remaining events.
For example, if I want to say that events A1, A2 and so on are independent, I would like relations such as the
following to be true.
The probability that event A3 happened and A4 does not happen remains the same even if I condition on some
information about some other events.
Let's say if I tell you that A1 happens or that both A2 happened and A5 did not happen.
The important thing to notice here is that the indices involved in the event of interest are distinct from the indices
associated with the events on which I'm given some information.
I'm given some information about the events A1, A2, and A5, what happened to them.
And this information does not affect my beliefs about something that has to do with events A3 and A4.
I would like all relations of this kind to be true.
This could be one possible definition, just saying that the family of events are independent if and only if any
relation of this type is true.
But such a definition would not be aesthetically pleasing.
Instead, we introduce the following definition, which mimics or parallels our earlier definition of independence of
two events.
We will say that a collection of events are independent if you can calculate probabilities of intersections of these
events by multiplying individual probabilities.
And this should be possible for all choices of indices involved and for any number or events involved.
Let us translate this into something concrete.
Consider the case of three events, A1, A2, and A3.
Our definition requires that we can calculate the probability of the intersection of two events by multiplying
individual probabilities.
And we would like all of these three relations to be true, because this property should be true for any choice of the
indices.
What do we have here?
This relation tells us that A1 and A2 are independent.
This relation tells us that A1 and A3 are independent.
This relation tells us that A2 and A3 are independent.
We call this situation pairwise independence.
But the definition requires something more.
It requires that the probability of three-way intersections can also be calculated the same way by multiplying
individual probabilities.
And this additional condition does make a difference, as we're going to see in a later example.
Is this the right definition?
Yes.
One can prove formally that if the conditions in this definition are satisfied, then any formula of this kind is true.
In particular, we also have relations such as the following.
The probability of event A3 is the same as the probability of event A3, given that A1 and A2 occurred.
Or the probability of A3, given that A1 occurred but A2 didn't.
Or we can continue this similarly, the probability of A3 given that A1 did not occur, and A2 occurred, and so on.
So any kind of information that I might give you about events A1 and A2-- which one of them occurred and which
one didn't-- is not going to affect my beliefs about the event A3.
The conditional probabilities are going to be the same as the unconditional probabilities.
I told you that this definition implies that all relations of this kind [are] true.
This can be proved.
The proof is a bit tedious.
And we will not go through it.

---
