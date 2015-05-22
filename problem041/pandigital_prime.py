#!/usr/bin/python

# Solution for Project Euler problem 41, "Pandigital prime".
# http://projecteuler.net/problem=41

import sys; sys.path.insert(0, "..")

from itertools import permutations
from util.euler import is_prime

def solve():
  for d in range(7, 0, -1):  # optimization: skip 9- and 8-digit numbers
    for candidate in permutations(reversed(range(1, d + 1))):
      p = reduce(lambda t, x: 10 * t + x, candidate)
      if is_prime(p):
        return p

print solve()
