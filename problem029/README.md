# [Problem 29](http://projecteuler.net/problem=29): Distinct powers

**NOTE: Spoilers below!**

---

**Difficulty:** Easy.

**Idea:**
Brute force.

## Solution (Python)

The script iterates through all permutations of `a, b` and adds the power to a set, which de-duplicates by definition.
Uses `itertools` for easy iteration, though it can also be achieved by a simple nested loop.

--

The solution runs in **44ms** and returns the answer **9183**.

