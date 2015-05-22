#!/usr/bin/python

# Solution for Project Euler problem <num>, "<title>".
# http://projecteuler.net/problem=<num>

import sys; sys.path.insert(0, '..')

from util.euler import prime_divisors
from util.euler import primes

def solve():
  lower = 2 * 3 * 5 * 7
  goal = 4

  ps = primes(1, 100000)
  print len(ps)
  print 'done'

  print prime_divisors(644, ps)

  consecutive = []
  curr = lower
  while True:
    if len(prime_divisors(curr, ps)) >= goal:
      # print "%d -> %s" % (curr, prime_divisors(curr))
      consecutive.append(curr)
    else:
      consecutive = []
    if len(consecutive) is goal:
      break
    curr += 1

  return consecutive

print solve()
