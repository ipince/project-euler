#!/usr/bin/pyhon

# Solution for Project Euler problem 23, "Non-abundant sums".
# http://projecteuler.net/problem=23

from itertools import product

import math

BOUND = 28123

def solve():
  abundants = []
  sums = set()
  for n in xrange(1, BOUND + 1):
    if abundant(n):
      abundants.append(n)
  for i in xrange(len(abundants)):
    for j in xrange(i, len(abundants)):  # optimization
      s = abundants[i] + abundants[j]
      if s <= BOUND:
        sums.add(s)
  return ((BOUND * (BOUND + 1)) / 2) - sum(sums)

def abundant(n):
  small_divs = [d for d in xrange(1, int(math.sqrt(n) + 1)) if n % d == 0]
  s = reduce(lambda s, d: s + d + n / d if d != n / d else s + d, small_divs)
  return s > n

print solve()
