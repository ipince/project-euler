#!/usr/bin/python

# Solution for Project Euler problem <num>, "<title>".
# http://projecteuler.net/problem=<num>

from collections import defaultdict

import sys; sys.path.insert(0, '..')

from util.euler import is_prime
from itertools import islice

UPPER_PRIME = 3944  # see README for how this is calculated.

def solve():
  ps = primes(1, UPPER_PRIME)
  for l in xrange(len(ps), 1, -1):
    s = sum(ps[-l:])
    for i in xrange(len(ps) - l, -1, -1):
      #print s
      if s < 1000000 and is_prime(s):
        return s
      s = s + ps[i - 1] - ps[i + l - 1]

def solve2():
  ps = primes(1, UPPER_PRIME)
  for l in xrange(len(ps), 1, -1):
    for i in xrange(len(ps) - l, -1, -1):
      p = sum(ps[i:i+l])
      #print '%s -> %s' % (ps[i:i+l], p)
      if p < 1000000 and is_prime(p):
        return p

def solve3():
  ps = primes(1, UPPER_PRIME)
  for l in xrange(len(ps), 1, -1):
    for i in xrange(len(ps) - l + 1):
      p = sum(ps[i:i+l])
      #print '%s -> %s' % (ps[i:i+l], p)
      if p < 1000000 and is_prime(p):
        return p

def primes(lower, upper):
  sieve = defaultdict(lambda: True)
  primes = list()
  if lower < 2:
    primes.append(2)
  for p in xrange(3, upper, 2): # odd numbers
    if sieve[p]:
      if p >= lower:
        primes.append(p)
      m = p 
      while m < upper:
        m += p
        sieve[m] = False
  return primes

print solve3()
