# Project Euler Problem 206: Concealed Square

Problem statement: http://projecteuler.net/problem=206

## Solution (python)

Idea: exhaustive search, but reducing the search space to something manageable.
I attempted to do this with pencil + paper, but could not constrain the space
enough.

First, we find upper and lower bounds for the root. That still leaves a search
space (upper - lower) of about 375M numbers. That space is too large to run a
search on.

Now, notice that the target, `1_2_3_4_5_6_7_8_9_0`, ends in `0`, which means `2`
and `5` are prime factors of it. But the target is a square, so all of its
factors' exponents must be even. Therefore the target is of the form
`1_2_3_4_5_6_7_8_900`.

Next, notice that the only numbers whose square ends in `900` must end in `30`
or `70`.

With that in mind, we can reduce the initial search space by a factor of 100,
leaving a manageable space of ~4M, which we just search over with a script.
