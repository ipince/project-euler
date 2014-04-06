#!/usr/bin/python

# Solution for Project Euler problem 29, "Distinct powers".
# http://projecteuler.net/problem=29

from itertools import product

def solve():
  s = set()
  for (a, b) in product(xrange(2, 101), xrange(2, 101)):
    s.add(pow(a, b))
  return len(s)

print solve()
