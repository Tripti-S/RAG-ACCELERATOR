# 0B73394616A1Df985F43Adfe64810Bed Vesusak1Hbk

---

MITOCW | MITRES6_012S18_L26-06_300k
In this video, we are going to calculate interesting quantities that have to do with the short-term behavior of
Markov chains as opposed to those dealing with long-term steady-state behaviors.
But first, let us introduce the notion of absorbing state.
As indicated in this definition, an absorbing state is a recurrent state from which you cannot escape once you get
to it.
The transition probabilities from k to k is 1.
So in some sense, you get absorbed by the state.
For example, consider this transition probability graph.
States 4 and 5 are both absorbing states.
Indeed, when you get to 4, you stay in 4.
Or when you get to 5, you stay in 5.
State 1, 2, and 3 are transient states.
So if the Markov chain initially started in 4, then it will stay in 4 forever.
If it started in 5, it's going to stay in 5 forever.
But what if the Markov chain started in either 1, 2, or 3?
Eventually, after some moving around, you will either make that transition to state 4 and get absorbed by it, or
you're going to do that transition and get to 5 and get absorbed by the state 5.
So the question is, are you going to end up in 4, or are you going to end up in 5?
Well, we don't know for sure.
These correspond to random events.
But can we say anything about their probabilities?
Well, let us try to calculate the probability that you end up in 4 as an example.
First, it seems plausible that this probability of ending in 4 will depend on where you started.
If you start in 2, you probably have more chances of getting to 4 than if you started from 3.
Because if you start from 2, at the next step you have immediately the chance of getting to 4.
But if you start from 3, there is some chance that you will go to 5 and never go to 4, or you will have to go through
2 in order to get to 4 anyway.
So it looks like the probability of reaching 4, given you started from 2, will be bigger than if you started from 3.
Now, from 1, it's unclear.
Let us be systematic then.
Let us consider all possible probabilities to end up in 4 depending on the initial state.
So let us ask this question, what is the probability, a of i, that the chain eventually settles in 4 given that it started
in i?
So in other words, a of i is the probability that you end up in 4 given that you started in i.
Now, the answer to that question is very easy for some cases.
If you start in 4, the probability that you end up in 4 is 1.
And if you start in 5, the probability that you end up in 4 is 0.
There is no way that you can go from 5 to 4.
What about the other cases?
Well, it's not so clear.
Let us consider, for example, that you started from 2.
What could happen next?
Well, from state 2, let's build a tree.
You can either, with a probability 0.2, go to 4.
Or with a probability 0.8, you will go to 1.
Now, in the first case, you're done.
You reach 4.
But in the second case, you arrive in 1.
And what happens next?
You don't know.
But what you know is that from that state, either eventually you go and get trapped in 5, or you go and eventually
get trapped in 4.
What are the probabilities of these events?
Well, we don't know.
But one of them has been defined before.
This represents the probability of ending up in 4 given that you start in 1, and that has been defined here.
This is nothing else than a1.
So the overall probability of interest for us, which is a of 2, using the total probability theorem, you can enumerate
all options.
It's with probability 0.2 you will go to 4.
And then the probability of going to 4 given that you started in 4 is a4 plus 0.8 times a1.
Now, a of 4 is, of course, 1, as we have discussed before.
So we get the relation between a2 and a of 1.
Now, of course, you can do the same thing for the other state.
For example, if you started from 1, what can happen next?
Well, you can go to 2 with a probability 0.6.
Once you're in 2, you're asking yourself, what is the probability of reaching 4?
Well, by definition, it's a2.
Or from 1, you go to 3 with a probability 0.4.
And given that you have done that, what is the probability that eventually you reach 4?
It's a3.
If initially you start with a3, what can happen next?
Again, with probability 0.3, you will end up in state 2.
And there, a of 2 is the probability of interest.
Or with a probability 0.5, you go to state 1.
And in that case, you get a of 1.
And finally, with a probability 0.2, you get trapped in 5.
All right?
You can write if you want, but 0.2, and you get trapped in 5.
But we know that a of 5 is 0, so this term will disappear.
So in the end, you get a system here.
After you replace a4 by 1 and a5 by 0, you get a system of three linear equations with three unknown.
And it is easy to solve.
I will not do that.
You can do it yourself.
But here are the results.
You will get a of 1 equals 18/28, a of 2 will be 20/28, and a of 3 will be 15/28.
Now I expressed them so that we can compare them easily.
And as a sanity check, you can verify that indeed the probability starting from 2 will be larger than the probability
starting from 3.
And it turns out that a of 1 will be in between the other two.
So these probabilities are consistent with our previous intuitions.
As an aside, note that you could have written a system of five linear equations with five unknown, the five
unknown corresponding to the five states possible.
In fact, we had our five equations here.
Here was one, another one here, and 1, 2, 3, so 3 plus 2, 5.
Of course, this one was easy.
It was a4 equals 1 and a5 equals 0 that you can replace then there, and you get a limited or restricted or smaller
system of three equations with three unknown.
Now, what if you had been interested instead in finding the probability b of i that the chain eventually settles in 5
given you started in i.
How to do that?
Well, you can repeat exactly all this calculation that we have done, but looking at 5 as the state of interest.
But of course, you don't have to do this.
For any state i, given that you started in i, you will eventually with probability 1 end up in either 4 or 5.
So you have a of i plus b of i equals 1 for all possible i.
So once you have calculated a1, a2, a3, a4, and a5, you get b1, b2, b3, b4, and b5 by using this formula.
To sum up, in general, the calculation of the probabilities to reach a given absorbing state s starting from any
state i of a general Markov chain with m states-- so let's assume that you have m states-- will be the unique
solution of a system of m equations with m unknowns, with the additional conditions that a of s equals 1 and a of s
prime equals 0 for the other absorbing states.
Now, going back to the following question that we posed at the end of the review on steady-state behavior, we
had this diagram, and we wanted to know which recurrent class this chain would end up if it started in one of these
transient states.
Well, we can now answer this question.
For the purpose of this calculation, the trick is simply to think of a recurrent class as one big absorbing state and
go through the calculation as we have done here.
So think about this class, for example, as being one big state, an absorbing state.
And now forget about the inside and calculate the probability that you end up in this class as the probability of
reaching this absorbing state given that you started in 1, 2, and 4, and you do the same kind of calculation.

---
