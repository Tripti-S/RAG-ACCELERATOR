# Dd7E83E4Fc853E4D5F93D1A9D578621B L6Yyhav1Agc

---

MITOCW | MITRES6_012S18_L24-06_300k
Let us now illustrate, with an example, the calculations of n step transition probabilities that we have just
discussed.
In this example, we are given a two state Markov chain, and as part of the input, the one step transition
probabilities between these two states.
So, given that you are in state one, the probability that you will next go to state two is 0.5, and the probability that
you will stay in state one is 0.5.
And, given that you are in state two, the probability that you will next go to state one is 0.2, and the probability that
you will stay in state two is 0.8.
Now, suppose that you start in state one, and you would like to calculate the probability of being in state one after
n transitions, or after n steps.
With our notation here, this is r11 of n.
That probability can happen in two ways.
After n minus 1 steps, you end up in state one, and then for the last transition, you stay in state one, or after the
first n minus 1 transition, you end up in state two, and then you transition back to state one.
Assuming that you start again in state one, and you would like to calculate the probability that you end up in state
two after n steps, you could apply the same logic, but these are probabilities.
And given that you started in state one, after n steps, you will either be in state one or in state two.
So r12 of n is simply 1 minus r11 of n.
And this system of two recursions is enough to propagate r11 of n and r12 of n as a function of n.
Let us do it and fill the blanks here.
As indicated before, the case for n equals 0 or n equals 1 are simple and do not require the use of the recursions
here.
So for example, for n equals 0, r11 of 0 will simply be 1, and so as a result, r12 of 0 will be 0.
And again, r22 of 0 will be 1, and as a result, r21 of 0 will be 0.
For n equals 1, these are the simple one step transition probabilities.
So you have 0.5 here, and 0.5 here, and r21 here are 0.2 and 0.8.
The next cases for n equals 2 become more interesting.
So, to reach n equals 2, r11 of 2, two options again.
You can go this way with a probability 0.5, or you can go from that to here with a probability 0.2.
So here, we obtain total probability of 0.25, here, a probability of 0.10, and when you sum these two probabilities,
you obtain 0.35, which is r11 of 2.
As a result, you get 0.65 for r12 of 2.
Then you can follow the same process for n equals 3, n equals 4, et cetera, et cetera.
I will not do it here, but this would be an interesting exercise for you to do the next several steps, perhaps within
an Excel spreadsheet.
But suppose that I tell you the number for n equals 100 and I tell you that the number that you obtain here is
about 2/7.
So as a result, the numbers that you are going to have here is about 5/7.
Let us then apply this simple recursion in order to find the values here for n equals 101.
r11 of 101 will be 2/7 times 0.5 plus 5/7 times 0.2.
Will be 1/7 for the first one plus 1/7 for the second one, and so we obtain again 2/7.
And if you do the same calculation, you will end up with 5/7 here.
This is an interesting fact.
When the system starts in state one, the probability that I find myself in state one after a long period of time
seems to converge to a constant value, in that case, to the constant value of 2/7.
Assume now that you want to do the same calculation for r21 and r22.
In other words, you start in state two and you are interested in knowing the evolution of these r21 of n and r22 of n
as a function of n.
Again, I will let you do it, but I can tell you that these probabilities will also seem to converge to a constant, and in
fact, will converge to something that is exactly the same, 2/7 here and 5/7 here.
This is a second interesting fact.
Irrespective of where we started, either from state one or from state two, the probability of being in a state one
after a long period of time seems to converge to the same constant, 2/7.
So in some sense, for that particular example, the importance of the initial state vanishes as time goes by and
does not influence long term probabilities of being in any of the two states.
Note that this is not true at the beginning starting at state two.
The picture, after a few transitions, will look different than if you had started from state one.
So the initial state does tell you something at the beginning, but this vanishes as time goes by.
We describe these convergence properties by saying that the Markov chain eventually enters a steady state.
What does this really mean?
Does it mean that the state of the Markov chain itself becomes steady and eventually stops at a given place?
No.
The state of the system will keep jumping forever.
What becomes steady are the probabilities that describe Xn.
After the Markov chain enters steady state, then, at any time, if you take a photo of the system and ask, what is
the probability that the chain will be in state one on that picture, it will be 2/7.
By the way, the steady state of being in state two is greater than the steady state of being in state one.
Does it make sense?
Yes.
State two is a little bit more sticky than state one in the following sense.
When you get to state two, the probability that you remain in state two, which is 0.8, is greater than the
corresponding probability for state one, which is 0.5.
So to conclude, this Markov chain has exhibited some nice long term properties.
Is this always the case for any Markov chains?
Let us see.

---
