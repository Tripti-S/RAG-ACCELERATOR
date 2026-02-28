# 59756168E3Edee41C2603B7Eba4Dcf3B Ljuvb-Sxzoo

---

MITOCW | MITRES6_012S18_L22-06_300k
We will now go through a very simple example, in which we just get to use the formulas that we have available.
The Poisson process is a pretty good model of email arrivals at least during a limited part of the day.
For example, during daytime, emails may be arriving as a Poisson crosses with a certain rate.
But then during night time, they may be arriving as a Poisson process with a different rate.
Nevertheless, the assumption that we will make is that, at least for this problem, that emails arrive as a Poisson
process with a fixed rate of five messages per hour.
What is the mean and the variance of the number of emails received during a day?
Well, we have formulas for the mean and the variance.
And in this problem, we have a lambda equal to 5, and tau consists of 24 hours.
So the answer is 5 times 24.
And this answer applies to both of the mean and the variance, because for the Poisson random variable, these
are the same.
What is the probability that we get one new message in the next hour?
This has to do with the PMF of the number of arrivals during the next hour, and that PMF is given by the Poisson
probabilities.
We're asking for the probability of one new message, so that k is equal to 1, in the next hour, so that tau is equal
to 1.
So we're looking for this expression here.
And using also that lambda is equal to 5, we enter those numbers into this formula.
And what we obtained is 5 times e to the minus 5.
Finally, what is the probability that during each of the next three hours, you'll obtain two messages.
So this is an event which is actually the intersection of three events, the event of two messages in this hour, two
messages in this hour, and two messages in that hour.
For the Poisson process, we have assumed that different time intervals are independent of each other.
So what we need to do is to multiply the probability of two messages in this hour with the probability of two
messages in that hour, and the probability of two messages in that power.
On the other hand, for each one of the hours, the probability's going to be the same, so it's enough to take the
probability of two messages during this hour, which is in our notation this quantity, and multiply it with itself three
times, so we get the third power of this.
Now this expression is equal to the following.
Lambda times tau is 5.
k is equal to 2, so we get 5 squared.
Then we have an e to the minus 5 term.
And k is equal to 2, so we're dividing by 2.
And we take the third power of this.

---
