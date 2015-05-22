#!/usr/bin/python

# Solution for Project Euler problem <num>, "<title>".
# http://projecteuler.net/problem=<num>

import sys; sys.path.insert(0, '..')

import math

from itertools import count
from util.euler import is_prime

def solve():
  for comp in count(3, 2):
    if is_prime(comp):
      continue
    holds = False
    for s in xrange(1, int(math.sqrt(comp / 2 + 1) + 1)):
      diff = comp - 2 * s * s
      if is_prime(diff):
        holds = True
        break
    if not holds:
      return comp

print solve()
