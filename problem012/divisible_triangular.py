#!/usr/bin/python

# Solution for Project Euler problem 12, "Highly divisible triangular number".
# http://projecteuler.net/problem=12

import math

def solve(thresh):
  inc = 2
  triangular = 1
  while True:
    if num_divisors(triangular) > thresh:
      return triangular
    triangular += inc
    inc += 1

def num_divisors(n):
  s = 0
  for d in xrange(1, int(math.sqrt(n)) + 1):
    s += 1 if n % d == 0 else 0
  return 2*s

print solve(500)
