# [Problem 12](http://projecteuler.net/problem=12): Highly divisible triangular number

**NOTE: Spoilers below!**

---

**Difficulty**: Easy

**Idea:**
Exhaustive search, no optimizations.

## Solution (Python)

Nothing special to see here. The script iterates through all triangular numbers and calculates the number of divisors for each.
Calculating the number of divisors of `n` is fast, since we only need to check from `1` until `sqrt(n)`.

--

The solution runs in **6.5 seconds** (slow, but good enough given solution was easy) and returns the answer **76576500**.

