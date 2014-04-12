# [Problem 206](http://projecteuler.net/problem=206): Concealed Square

**NOTE: Spoilers below!**

---

**Difficulty:** Easy.

**Idea:**
Exhaustive search, but reducing the search space to something manageable.
I attempted to do this with pencil + paper, but could not constrain the space
enough.

## Solution (Python)

First, we find strict upper and lower bounds, the roots of `1020304050607080900` and `1929394959697989990`.
That still leaves a search space (upper - lower) of about 375M numbers. We want to constrain that space further.

Now, notice that the target, `1_2_3_4_5_6_7_8_9_0`, ends in `0`, which means `2`
and `5` are prime factors of it. But the target is a square, so all of its
factors' exponents must be even. Therefore the target is of the form
`1_2_3_4_5_6_7_8_900`.

Next, notice that the only numbers whose square ends in `900` must end in `30`
or `70`.

With that in mind, we can reduce the initial search space by a factor of 100 (we only need to check 2 numbers out of every 100), leaving a manageable space of ~4M, which we just search over with a script.

--

This solution runs in **6.5** seconds and spits out the answer of **1389019170**. The answer is near the upper bound of our search. If we run the search starting from the upper bound instead of the lower one, the script runs in **60ms**.
