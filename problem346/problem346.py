#!/usr/bin/python

import math

def repunit_base(n, base):
  if n < base:
    return n == 1
  d = n % base
  if d == 1:
    return repunit_base(n / base, base)
  else:
    return False

def naive_solve():
  total = 1  # include 1, since it's special
  for n in xrange(2, 10000):
    for base in xrange(2, n - 1):
      if repunit_base(n, base):
        total += n
        break
  return total

def naive2_solve():
  total = 1
  for n in xrange(2, 10000):
    for k in xrange(3, int(math.log(n, 2)) + 2):
      if repunitable(n, k):
        total += n
        break
  return total

def solve(bound):
  repunits = set()
  repunits.add(1)
  for b in xrange(2, int(math.sqrt(bound)) + 1):
    l = 3
    while True:
      candidate = unipoly(b, l)
      if candidate < bound:
        repunits.add(candidate)
      else:
        break
      l += 1
  return sum(repunits)

def repunitable(n, k):
  # finds solution for x^(k-1) + x^(k-2) + ... + x + 1 = n
  hi = n / 2
  lo = 1
  while hi - lo > 1:
    mid = (lo + hi) // 2
    val = unipoly(mid, k)
    if val > n:
      hi = mid
    elif val < n:
      lo = mid
    else:
      return mid

def unipoly(x, k):
  s = 1
  for i in xrange(k-1):
    s = s*x + 1
  return s

print solve(1000000000000)
