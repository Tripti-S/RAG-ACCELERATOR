# B055F97Edfbcec06C9092C2E0A6Af712 W423Ypsuhf0

---

MITOCW | MITRES6_012S18_L03-03_300k
In the previous example, we had a model where the result of the first coin toss did not affect the probabilities of
what might happen in the second toss.
This is a phenomenon that we call independence and which we now proceed to define.
Let us start with a first attempt at the definition.
We have an event, B, that has a certain probability of occurring.
We are then told that event A occurred, but suppose that this knowledge does not affect our beliefs about B in the
sense that the conditional probability remains the same as the original unconditional probability.
Thus, the occurrence of A provides no new information about B. In such a case, we may say that event B is
independent from event A.
If this is indeed the case, notice that the probability that both A and B occur, which is always equal by the
multiplication rule to the probability of A times the conditional probability of B given A. So this is a relation that's
always true.
But if we also have this additional condition, then this simplifies to the probability of A times the probability of B.
So we can find the probability of both events happening by just multiplying their individual probabilities.
It turns out that this relation is a cleaner way of the defining formally the notion of independence.
So we will say that two events, A and B, are independent if this relation holds.
Why do we use this definition rather than the original one?
This formal definition has several advantages.
First, it is consistent with the earlier definition.
If this equality is true, then the conditional probability of event B given A, which is the ratio of this divided by that,
will be equal to the probability of B. So if this relation holds, then this relation will also hold, and so this more formal
definition is consistent with our earlier intuitive definition.
A more important reason is that this formal definition is symmetric with respect to the roles of A and B. So instead
of saying that B is independent from A, based on this definition we can now say that events A and B are
independent of each other.
And in addition, since this definition is symmetric and since it implies this condition, it must also imply the
symmetrical relation.
Namely, that the conditional probability of A given B is the same as the unconditional probability of A.
Finally, on the technical side, conditional probabilities are only defined when the conditioning event has non-zero
probability.
So this original definition would only make sense in those cases where the probability of the event A would be
non-zero.
In contrast, this new definition makes sense even when we're dealing with zero probability events.
So this definition is indeed more general, and this also makes it more elegant.
Let us now build some understanding of what independence really is.
Suppose that we have two events, A and B, both of which have positive probability.
And furthermore, these two events are disjoint.
They do not have any common elements.
Are these two events independent?
Let us check the definition.
The probability that both A and B occur is zero because the two events are disjoint.
They cannot happen together.
On the other hand, the probability of A times the probability of B is positive, since each one of the two terms is
positive.
And therefore, these two expressions are different from each other, and therefore this equality that's required by
the definition of independence does not hold.
The conclusion is that these two events are not independent.
In fact, intuitively, these two events are as dependent as Siamese twins.
If you know that A occurred, then you are sure that B did not occur.
So the occurrence of A tells you a lot about the occurrence or non-occurrence of B.
So we see that being independent is something completely different from being disjoint.
Independence is a relation about information.
It is important to always keep in mind the intuitive meaning of independence.
Two events are independent if the occurrence of one event does not change our beliefs about the other.
It does not affect the probability that the other event also occurs.
When do we have independence in the real world?
The typical case is when the occurrence or non-occurrence of each of the two events A and B is determined by
two physically distinct and non-interacting processes.
For example, whether my coin results in heads and whether it will be snowing on New Year's Day are two events
that should be modeled as independent.
But I should also say that there are some cases where independence is less obvious and where it happens
through a numerical accident.
You can now move on to answer some simple questions where you will have to check for independence using
either the mathematical or intuitive definition.

---
