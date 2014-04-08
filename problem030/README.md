# [Problem 30](http://projecteuler.net/problem=30): Digit fifth powers

**NOTE: Spoilers below!**

---

**Idea:**
Search the space, but (a) find a reasonable upper bound and (b) search the set of possible fifth power sums instead of
searching linearly from 1 to n.

## Solution (Python)

The problem statement says "find the sum of *all* the numbers". That alone hints that there must be a bound
with which we can restrict our search. Otherwise we would never finish searching. Let's look for a number `n`
after which we no longer have to search.

### Finding an upper bound

One thing to note is that no matter how many digits a number has, its fifth power digit sum may be small (e.g. 100000
has a fifth power digit sum of 1). So it is reasonable to think that a number of `d` digits could have a fifth power
digit sum equal to itself, no matter how large `d` is. Except the fifth power digit sum itself is bounded, and it turns
out the bound is relatively small. For a number `n` of `d` digits, its fifth power digit sum (let's call it `f(n)`) is
bounded by `9^5 * d`. When `d = 7`, `f(n) <= 413,343`, which is 6 digits long! That means that `f(n)` will never equal
`n` when `d >= 7`. In fact, when `d = 6`, `f(n) <= 354,294`. So we can safely exclude any `n > 354,294` from our search.

We can even go further and say that, given the new constraint of `n <= 354,294`, the largest `f(n)` could ever be is
`3^5 + 9^5 * 5 = 295,488`, finding a new bound for `n`. And we can keep doing this to lower the bound (ever so slightly).
However, we've reduced our search space enough that this is not necessary, especially if we search the space in a smart
way.

### Searching the bounded space

Instead of searching linearly from `n = 1` to `n = 354,294`, notice that the range (or image) of `f(n)` is actually much
smaller because `f` is not injective. That is, many inputs map to the same output, such as `f(12) = f(21) = f(201)`. So,
let's just iterate over all `m` such that `f(n) = m` for some `n`. And then we'll just check if `m = n`.

How do we find such `m`s? Well, every `f(n)` is of the form `0^5 * k0 + 1^5 * k1 + ... + 9^5 * k9` where each `ki` is the
number of times the digit `i` appears in `n`. If the number `n` has `d` digits, then the number of values for `f(n)` is equal
to the number of ways in which we can choose `d` digits from 10 possibilities, while allowing repetitions (e.g. can choose
digit `3` twice). This is a well known computation in combinatorics (combinations with repetitions), for which the calculation
in this case is `(10 + d - 1)-choose-d`. You can read more about that [here](http://www.mathsisfun.com/combinatorics/combinations-permutations.html). Searching this way reduces our space
quite a bit. For example, there are almost 900,000 numbers with 6 digits, but `15-choose-6` is only 5,005.

Python's itertools allows us to enumerate all such combinations very easily by using `combinations_with_replacement`. And we need
to do this for every `d` from 1 onto 6 (since our upper bound has 6 digits). We are iterating over tuples of sorted digits, so
to check if `m = n`, what we do is check if there exists some arrangement of the digits in that tuple that, when concatenated,
yields `n`. To do so, we cheat a little bit and just see if, when sorted and converted into a tuple, `n`'s tuple is the same as
`m`'s tuple. Note that this is not 100% correct since we can find a number whose first digit is 0 and we would count it as valid
when it shouldn't be. But, this is good enough for this particular problem.

--

The solution runs in **160ms**, prints out each number that meets the criteria, as well as their final sum of **443839**.

