#!/usr/bin/pyhon

# Solution for Project Euler problem <num>, "<title>".
# http://projecteuler.net/problem=<num>

import math

# TODO: optimize! can't have 0,2,4,6,8 in its digits. or 5!

def solve(limit):
  candidate = 11
  count = 0
  total = 0
  while True:
    s = str(candidate)
    if all([is_prime(int(s[i:])) for i in xrange(len(s))]) and \
       all([is_prime(int(s[:i+1])) for i in xrange(len(s))]):
      count += 1
      print 'truncatable prime: %d' % candidate
      total += candidate
    if count >= limit:
      break
    candidate += 2
  return total

def is_prime(n):
  return n > 1 and all([n % d for d in xrange(2, int(math.sqrt(n) + 1))])

print solve(11)
