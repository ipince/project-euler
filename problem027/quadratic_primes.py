#!/usr/bin/pyhon

# Solution for Project Euler problem 27, "Quadratic primes".
# http://projecteuler.net/problem=27

from collections import defaultdict
import math

def solve(bound):
  bs = primes(1, bound)
  max_count = 0
  product = None
  for a in xrange(-bound + 1, bound):
    for b in bs:
      b = -b
      c = count(a, b)
      if c > max_count:
        max_count = c
        print "%d, %d -> %d" % (a, b, c)
        product = a * b
      b = -b
      c = count(a, b)
      if c > max_count:
        max_count = c
        print "%d, %d -> %d" % (a, b, c)
        product = a * b
  return product

def count(a, b):
  count = 0
  for n in xrange(abs(b)):  # ends at b^2 + ab + b
    p = n * n + a * n + b
    if is_prime(p):
      count += 1
    else:
      break
  return count

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

def is_prime(n):
  return n > 1 and all([n % d for d in xrange(2, int(math.sqrt(n) + 1))])

print solve(1000)
