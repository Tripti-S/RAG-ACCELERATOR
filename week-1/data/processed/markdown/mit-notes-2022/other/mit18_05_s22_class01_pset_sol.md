# Mit18 05 S22 Class01 Pset Sol

---

Class 1 in-class problems, 18.05, Spring 2022
Concept questions
Concept question 1. Poker hands
The probability of a one-pair hand is:
(1) less than 5%
(2) between 5% and 10%
(3) between 10% and 20%
(4) between 20% and 40%
(5) greater than 40%
Solution: We will do this later. Perhaps surprisingly the answer is greater than 40%
Concept question 2. DNA
1. DNA is made of sequences of nucleotides: A, C, G, T.
How many DNA sequences of length 3 are there?
(i) 12 (ii) 24 (iii) 64 (iv) 81
Solution: 1. (iii) 4×4×4 = 64
Concept question 3. DNA
2. How many DNA sequences of length 3 are there with no repeats?
(i) 12 (ii) 24 (iii) 64 (iv) 81
Solution: (ii) 4×3×2 = 24
Board questions
Board question 1. Inclusion/Exclusion
A band consists of singers and guitar players:
7 people sing, 4 play guitar, 2 do both
How many people are in the band?
Solution: In set notation, let 𝐵 be entire band, 𝑆 the singers, 𝐺 the guitar players. We
know 𝐵 = 𝑆 ∪𝐺, so
|𝐵| = |𝑆 ∪𝐺| = |𝑆|+|𝐺|−|𝑆 ∩𝐺| = 7+4−2 = 9 .
Board question 2. Rule of product
There are 5 Competitors in an Olympics 100m final.
How many ways can gold, silver, and bronze be awarded?
Solution: 5×4×3.
There are 5 ways to pick the winner. Once the winner is chosen there are 4 ways to pick
second place and then 3 ways to pick third place.
1
18.05 class 1 problems, Spring 2022 2
Board question 3.
I won’t wear green and red together; I think black or denim goes with anything; Here is my
wardrobe.
Shirts: 3B, 3R, 2G; sweaters 1B, 2R, 1G; pants 2D,2B.
© Source unknown. All rights reserved. This content is excluded from our Creative
Commons license. For more information, see https://ocw.mit.edu/fairuse.
How many different outfits can I wear?
Solution: Suppose we choose shirts first. Depending on whether we choose red compatible
or green compatible shirts there are different numbers of sweaters we can choose next. So
we split the problem up before using the rule of product. A multiplication tree is an easy
way to present the answer.
3 3 2
Shirts 𝑅 𝐵 𝐺
3 4 2
Sweaters 𝑅,B 𝑅,B,G B,G
4 4 4
Pants
𝐵,𝐷 𝐵,𝐷 𝐵,𝐷
Multiplying down the paths of the tree:
Number of outfits = (3×3×4)+(3×4×4)+(2×2×4) = 100
Board question 4.
(a) Count the number of ways to get exactly 3 heads in 10 flips of a coin.
(b) For a fair coin, what is the probability of exactly 3 heads in 10 flips?
Solution: (a) We have to ’choose’ 3 out of 10 flips for heads: (10).
3
(b) There are 210 possible outcomes from 10 flips (this is the rule of product). For a fair
coin each outcome is equally probable so the probability of exactly 3 heads is
(10) 120
3 = = 0.117
210 1024
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
