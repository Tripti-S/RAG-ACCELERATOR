# 31D18Feca481D4Bf803F32Fd9E3Ef8Be Ajxfyfqs2Mc

---

MITOCW | MITRES6_012S18_L03-08_300k
We will now consider an example that illustrates the difference between the notion of independence of a collection
of events and the notion of pairwise independence within that collection.
The model is simple.
We have a fair coin which we flip twice.
So at each flip, there is probability 1/2 of obtaining heads.
Furthermore, we assume that the two flips are independent of each other.
Let H1 be the event that the first coin toss resulted in heads, which corresponds to this event in this diagram.
Let H2 be the event that the second toss resulted in heads, which is this event in the diagram-- the two ways that
we can have the second toss being heads.
Now, we're assuming that the tosses are independent.
So the event heads-heads has a probability which is equal to the probability that the first toss resulted in heads--
that's 1/2-- times the probability that the second toss resulted in heads, which is 1/2.
So the product is 1/4.
We have probability 1/4 for this outcome.
Now, the total probability of event H1 is 1/2, which means that the probability of what remains should be 1/4, so
that the sum of these two numbers is 1/2.
By the same argument, the probability of this outcome, tails-heads , should be 1/4.
We have a total of 3/4.
So what's left is 1/4.
And that's going to be the probability of the outcome tails-tails .
Let us now introduce a new event, namely the event that the two tosses had the same result.
So this is the event that we obtain either heads heads or tails-tails.
Schematically, event C corresponds to this blue region in the diagram.
Is this event C independent from the events H1 and H2?
Let us first look for pairwise independence.
Let's look at the probability that H1 occurs and C occurs as well.
So the first toss resulted in heads.
And the two tosses had the same result.
So this is the same as the probability of obtaining heads followed by heads.
And this corresponds to just this outcome that has probability 1/4.
How about the product of the probabilities of H1 and of C?
Is it the same?
Well, the probability of H1 is 1/2.
And the probability of C-- what is it?
Event C consists of two outcomes.
Each one of these outcomes has probability 1/4.
So the total is, again, 1/2.
And therefore, the product of these probabilities is 1/4.
So we notice that the probability of the two events happening is the same as the product of their individual
probabilities, and therefore, H1 and C are independent events.
By the same argument, H2 and C are going to be independent.
It's a symmetrical situation.
H1 and H2 are also independent from each other.
So we have all of the conditions for pairwise independence.
Let us now check whether we have independence.
To check for independence, we need to also look into the probability of all three events happening and see
whether it is equal to the product of the individual probabilities.
So the probability of all three events happening-- this is the probability that H1 occurs and H2 occurs and C
occurs.
What is this event?
Heads in the first toss, heads in the second toss, and the two tosses are the same-- this happens if and only if the
outcome is heads followed by heads.
And this has probability 1/4.
On the other hand, if we calculate the probability of H1 times the probability of H2 times the probability of C, we
get 1/2 times 1/2 times 1/2, which is 1/8.
These two numbers are different.
And therefore, one of the conditions that we had for independence is violated.
So in this example, H1, H2, and C are pairwise independent, but they're not independent in the sense of an
independent collection of events.
How are we to understand this intuitively?
If I tell you that event H1 occurred and I ask you for the conditional probability of C given that H1 [occurred], what
is this?
This is the probability that we obtain, given that the first event is heads, the first result is heads, the only way that
you can have the two tosses having the same result is going to be in the second toss also resulting in heads.
And since H2 and H1 are independent, this is just the probability that we have heads in the second toss.
And this number is 1/2.
And 1/2 is also the same as the probability of C. That's another way of understanding the independence of H1 and
C.
Given that the first toss resulted in heads, this does not help you in any way in guessing whether the two tosses
will have the same result or not.
The first one was heads, but the second one could be either heads or tails with equal probability.
So event H1 does not carry any useful information about the occurrence or non-occurrence of event C. On the
other hand, if I were to tell you that both events, H1 and H2, happened, what would the conditional probability of C
be?
If both H1 and H2 occurred, then the results of the two coin tosses were identical, so you know that C also
occurred.
So this probability is equal to 1.
And this number, 1, is different from the unconditional probability of C, which is 1/2.
So we have here a situation where knowledge of H1 having occurred does not help you in making a better guess
on whether C is going to occur.
H1 by itself does not carry any useful information.
But the two events together, H1 and H2, do carry useful information about C.
Once you know that H1 and H2 occurred, then C is certain to occur.
So your original probability for C, which was 1/2, now gets revised to a value of 1.
So H1 and H2 carry information relevant to C. And therefore, C is not independent from these two events
collectively.
And we say that events H1.
H2, and C are not independent.

---
