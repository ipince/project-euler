# [Problem 21](http://projecteuler.net/problem=21): Amicable numbers

**NOTE: Spoilers below!**

---

**Difficulty:** Easy

**Idea:**
Exhaustive search, no optimizations.

## Solution (Python)

The script simply iterates through all integers and calculates the sum of their divisors to check if the number if amicable.
The divisor sum calculation can be further optimized (no need to check all integers below `n`!), but it did not seem
worth the trouble since the solution finished in a reasonable time for the problem's limit of 10000.

--

The solution runs in **6.7 seconds** and returns the answer **31626**.

