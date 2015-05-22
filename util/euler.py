# Handy functions for Project Euler problems.

import math

from collections import defaultdict

def memoize(f):
  class memodict(dict):
    def __missing__(self, key):
      ret = self[key] = f(key)
      return ret
  return memodict().__getitem__

# Divisibility
def divisors(n):
  return [d for d in xrange(1, n) if n % d == 0]

# Primes

def primes(lower, upper):
  """Uses a sieve to return all primes between |lower| and |upper|.
  """
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

@memoize
def is_prime(n):
  return n > 1 and all([n % d for d in xrange(2, int(math.sqrt(n) + 1))])

def prime_divisors(n, primes=None):
  if primes:
    return [p for p in primes if n % p == 0]
  else:
    return [d for d in divisors(n) if is_prime(d)]

