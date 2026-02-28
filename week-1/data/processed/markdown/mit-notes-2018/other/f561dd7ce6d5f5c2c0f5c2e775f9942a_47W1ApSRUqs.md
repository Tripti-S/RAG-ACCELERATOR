# F561Dd7Ce6D5F5C2C0F5C2E775F9942A 47W1Apsruqs

---

MITOCW | MITRES6_012S18_S01-01_300k
In this segment, we will talk about sets.
I'm pretty sure that most of what I will say is material that you have seen before.
Nevertheless, it is useful to do a review of some of the concepts, the definitions, and also of the notation that we
will be using.
So what is a set?
A set is just a collection of distinct elements.
So we have some elements, and we put them together.
And this collection, we call it the set S.
More formally, how do we specify a set?
We could specify a set by listing its elements, and putting them inside braces.
So this is a set that consists of four elements, the letters, a, b, c, d.
Another set could be the set of all real numbers.
Notice a distinction here-- the first set is a finite set.
It has a finite number of elements, whereas the second set is infinite.
And in general, sets are of these two kinds.
Either they're finite, or their infinite.
A piece of notation now.
We use this notation to indicate that a certain object x is an element of a set S. We read that as x belongs to S.
If x is not an element of S, then we use this notation to indicate it, and we read it as x does not belong to S.
Now, one way of specifying sets is as follows.
We start with a bigger set-- for example, the set of real numbers-- and we consider all of those x's that belong to
that big set that have a certain property.
For example, that the cosine of this number is, let's say, bigger than 1/2.
This is a way of specifying a set.
We start with a big set, but we then restrict to those elements of that set that satisfy a particular property.
One set of particular interest is the following.
Sometimes in some context, we want to fix a collection of all possible objects that we might ever want to consider,
and that collection will be a set.
We denote it usually by omega, and we call it the universal set.
So having fixed a universal set, we will only consider smaller sets that lie inside that big universal set.
And once we have a universal set, we can talk about the collection of all objects, or elements, that belong to our
universal set, but do not belong to the set S. So that would be everything outside the set S.
Everything outside the set S, we denote it this way, and we call it the complement of the set S. And it is defined
formally as follows-- an element belongs to the complement of S if x is an element of our universal set, and also x
does not belong to S. Notice that if we take the complement of the complement-- that is, anything that does not
belong to the green set-- we get back the red set.
So what this is saying is that the complement of the complement of a set is the set itself.
Another set of particular interest is the so-called empty set.
The empty set is a set that contains no elements.
In particular, if we take the complement of the universal set-- well, since the universal set contains everything,
there is nothing in its complement, so its complement is going to be the empty set.
Finally, one more piece of notation.
Suppose that we have two sets, and one set is bigger than the other.
So S is the small set here, and T is the bigger set.
We denote this relation by writing this expression, which we read as follows-- S is a subset of the set T.
And what that means is that if x is an element of S, then such an x must be also an element of T. Note that when
S is a subset of T, there is also the possibility that S is equal to T. One word of caution here-- the notation that
we're using here is the same as what in some textbooks is written this way-- that is, S is a subset of T, but can
also be equal to T. We do not use this notation, but that's how we understand it.
That is, we allow for the possibility that the subset is equal to the larger set.
Now when we have two sets, we can talk about their union and their intersection.
Let's say that this is set S, and this is set T. The union of the two sets consists of all elements that belong to one
set or the other, or in both.
The union is denoted this way, and the formal definition is that some element belongs to the union if and only if
this element belongs to one of the sets, or it belongs to the other one of the sets.
We can also form the intersection of two sets, which we denote this way, and which stands for the collection of
elements that belong to both of the sets.
So formally, an element belongs to the intersection of two sets if and only if that element belongs to both of them.
So x must be an element of S, and it must also be an element of T.
By the way, we can also define unions and intersections of more than two sets, even of infinitely many sets.
So suppose that we have an infinite collection of sets.
Let's denote them by Sn.
So n ranges over, let's say, all of the positive integers.
So pictorially, you might think of having one set, another set, a third set, a fourth set, and so on, and we have an
infinite collection of such sets.
Given this infinite collection, we can still define their union to be the set of all elements that belong to one of those
sets Sn that we started with.
That is, an element is going to belong to that union if and only if this element belongs to some of the sets that we
started with.
We can also define the intersection of an infinite collection of sets.
We say that an element x belongs to the intersection of all these sets if and only if x belongs to Sn for all n.
So if x belongs to each one of those Sn's, then we say that x belongs to their intersection.
Set operations satisfy certain basic properties.
One of these we already discussed.
This property, for example, is pretty clear.
The union of a set with another set is the same as the union if you consider the two sets in different orders.
If you take the union of three sets, you can do it by forming, first, the union of these two sets, and then the union
with this one; or, do it in any alternative order.
Both expressions are equal.
Because of this, we do not really need the parentheses, and we often write just this expression here, which is the
same as this one.
And the same would be true for intersections.
That is, the intersection of three sets is the same no matter how you put parentheses around the different sets.
Now if you take a union of a set with a universal set, you cannot get anything bigger than the universal set, so you
just get the universal set.
On the other hand, if you take the intersection of a set with the universal set, what is left is just the set itself.
Perhaps the more complicated properties out of this list is this one and this one, which are sort of a distributive
property of intersections and unions.
And I will let you convince yourselves that these are true.
The way that you verify them is by proceeding logically.
If x is an element of this, then x must be an element of S, and it must also be an element of either T or U.
Therefore, it's going to belong either to this set-- it belongs to S, and it also belongs to T-- or it's going to be an
element of that set-- it belongs to S, and it belongs to U.
So this argument shows that this set here is a subset of that set.
Anything that belongs here belongs there.
Then you need to reverse the argument to convince yourself that anything that belongs here belongs also to the
first set, and therefore, the two sets are equal.
Here, I'm using the following fact-- that if S is a subset of T, and T is a subset of S, this implies that the two sets
are equal.
And then you can use a similar argument to convince yourselves about this equality, as well.
So this is it about basic properties of sets.
We will be using some of these properties all of the time without making any special comment about them.

---
