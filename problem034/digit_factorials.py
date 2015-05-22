#!/usr/bin/python

# Solution for Project Euler problem 34, "Digit factorials".
# http://projecteuler.net/problem=34

from itertools import combinations_with_replacement
import math

DIGITS = '0123456789'

def solve(bound):
  factorials = [math.factorial(n) for n in range(1, 10)]
  total = 0
  for d in xrange(1, bound + 1):
    for digs in combinations_with_replacement(DIGITS, d):
      s = sum(map(lambda n: math.factorial(int(n)), digs))
      if s is not 1 and s is not 2 and tuple(sorted(str(s))) == digs:
        print str(digs) + ' -> ' + str(s)
        total += s
  return total

print solve(7)
