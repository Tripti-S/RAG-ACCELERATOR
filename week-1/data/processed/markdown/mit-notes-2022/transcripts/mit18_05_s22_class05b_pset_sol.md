# Mit18 05 S22 Class05B Pset Sol

---

Class 5b in-class problems, 18.05, Spring 2022
Board questions
Problem 1.
I’ve noticed that taxis drive past 77 Mass. Ave. on the average of once every 10 minutes.
Suppose time spent waiting for a taxi is modeled by an exponential random variable
1
𝑋 ∼ Exponential(1/10); 𝑓(𝑥) = e−𝑥/10
10
(a) Sketch the pdf of this distribution
(b) Shade the region which represents the probability of waiting between 3 and 7 minutes
(c) Compute the probability of waiting between between 3 and 7 minutes for a taxi
(d) Compute and sketch the cdf.
Solution: Sketches for (a), (b), (d)
𝑃(3<𝑋<7)
0.1 𝐹(𝑥)=1−e−𝜆𝑥
1
𝑓(𝑥)=𝜆e−𝜆𝑥
𝑥 𝑥
2 4 6 8 10121416 2 4 6 8 10 12 14 16
(c)
7 1 7
(3 < 𝑋 < 7) = ∫ e−𝑥/10 𝑑𝑥 = −e−𝑥/10∣ = e−3/10 − e−7/10 ≈ 0.244
10 3
3
Problem 2. Gallery of distributions
Open the Gallery of probability distributions applet at
https://mathlets.org/mathlets/probability-distributions/
(a) For the standard normal distribution N(0, 1) how much probability is within 1 of the
mean? Within 2? Within 3?
(b) For N(0, 32) how much probability is within 𝜎 of the mean? Within 2𝜎? Within 3𝜎.
(c) Does changing 𝜇 change your answer to problem 2?
(d) Use the applet to find the median of the exp(0.5) distribution.
(The median is the value of 𝑥 where half the probability is below 𝑥 and half above.)
Solution: (a) Using the applet:
𝑃(−1 ≤ 𝑍 ≤ 1) = 0.683, 𝑃(−2 ≤ 𝑍 ≤ 2) = 0.954, 𝑃(−3 ≤ 𝑍 ≤ 3) = 0.997.
(b) We set 𝜎 = 3 in the app. Since the mean is 0, the range within 𝜎 of the mean is [−3, 3].
Likewise within 2𝜎 of the mean has range [−6, 6], and 3𝜎 has range [−9, 9].
1
18.05 class 5b problems, Spring 2022 2
Let 𝑋 ∼ N(0, 32). According to the applet
𝑃 (−𝜎 ≤ 𝑋 ≤ 𝜎) = 0.683, 𝑃 (−2𝜎 ≤ 𝑋 ≤ 2𝜎) = 0.954, 𝑃 (−3𝜎 ≤ 𝑋 ≤ 3𝜎) = 0.997.
These are the same probabilities as in part (a).
(c) No, changing 𝜇 does not change the probability of being in a given range around the
mean. The range with 𝜎 of the mean is [𝜇 − 𝜎,𝜇 + 𝜎] and
𝑃(𝜇−𝜎 ≤ 𝑋 ≤ 𝜇+𝜎) = 𝑃(−𝜎 ≤ 𝑋−𝜇 ≤ 𝜎) = 0.683.
(d) The median is the value 𝑞, where 𝑃(𝑋 ≤ 𝑞) = 0.50. Using the applet for exp(0.5), we
set the left edge of the probability interval at 0 and adjust the right edge until we get 0.50
probability. The applet shows that 𝑞 is somewhere between 1.35 and 1.40.
Problem 3. Manipulating random variables
(a) Suppose 𝑋 ∼ uniform(0,2). If 𝑌 = 4𝑋, find the range, pdf and cdf of 𝑌 .
(b) Suppose 𝑋 ∼ uniform(0,2). If 𝑌 = 𝑋3, find the range, pdf and cdf of 𝑌 .
(c) Suppose 𝑍 ∼ Norm(0, 1) (standard normal). Find the range, pdf and cdf of 𝑌 = 3𝑍+2.
(a) Solution: Range of 𝑋 is [0,2]. Uniform means, for 𝑥 in this range
𝐹 (𝑥) = 𝑃(𝑋 ≤ 𝑥) = 𝑥/2.
𝑋
Range of 𝑌 is [0,8]. For 𝑦 in this range
𝑦
𝐹 (𝑦) = 𝑃(𝑌 ≤ 𝑦) = 𝑃(4𝑋 ≤ 𝑦) = 𝑃(𝑋 ≤ 𝑦/4) = .
𝑌 8
1
𝑓 (𝑦) = 𝐹 ′(𝑦) =
𝑌 8
(b) Solution: Range of 𝑋 is [0,2]. Uniform means, for 𝑥 in this range
𝐹 (𝑥) = 𝑃(𝑋 ≤ 𝑥) = 𝑥/2.
𝑋
Range of 𝑌 is [0,8]. For 𝑦 in this range
𝑦1/3
𝐹 (𝑦) = 𝑃(𝑌 ≤ 𝑦) = 𝑃(𝑋3 ≤ 𝑦) = 𝑃(𝑋 ≤ 𝑦1/3) = .
𝑌 2
1
𝑓 (𝑦) = 𝐹 ′(𝑦) = 𝑦−2/3
𝑌 6
(c) Solution: The standard normal has range (−∞, ∞), and pdf and cdf
1
𝜙(𝑧) = √ e−𝑧2/2, Φ(𝑧).
2𝜋
There is no closed form formula for Φ(𝑧) so we leave it as is. We compute its values using
a table (really using a computer).
18.05 class 5b problems, Spring 2022 3
𝑌 has range (−∞, ∞). We manipulate the cdf of 𝑌 using its definition as a probability.
𝑦−2 𝑦 −2
𝐹 (𝑦) = 𝑃(𝑌 ≤ 𝑦) = 𝑃(3𝑍 +2 < 𝑦) = 𝑃 (𝑍 < ) = Φ( ).
𝑌 3 3
That’s the best we can do for the cdf. For the pdf we take a derivative. (We’ll need to use
the chain rule.)
1 𝑦 −2
𝑓 (𝑦) = 𝐹′ (𝑦) = 𝜙( ) .
𝑌 𝑌 3 3
We do have a formula for 𝜙(𝑧). So
1
𝑓 (𝑦) = √ e−(𝑦−2)2/18.
𝑌
3 2𝜋
Note: this is the pdf for 𝑁(5, 32). So
𝑌 ∼ 𝑁(5,32).
That is, scaling and shifting a standard normal random variable produces another normal
random variable.
MIT OpenCourseWare
https://ocw.mit.edu
18.05 Introduction to Probability and Statistics
Spring 2022
For information about citing these materials or our Terms of Use, visit: https://ocw.mit.edu/terms.

---
