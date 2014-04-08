#!/usr/bin/python

# Solution for Project Euler problem 30, "Digit fifth powers".
# http://projecteuler.net/problem=30

from itertools import combinations_with_replacement

DIGITS = '0123456789'

def solve(bound, exp):
  total = 0
  for d in xrange(1, bound + 1):
    for digs in combinations_with_replacement(DIGITS, d):
      s = powersum(digs, exp)
      if s is not 1 and s is not 0 and tuple(sorted(str(s))) == digs:
        print str(digs) + ' -> ' + str(powersum(digs, exp))
        total += s
  return total

def powersum(digs, exp):
  return sum(map(lambda d: pow(int(d), exp), digs))

print solve(6, 5)
