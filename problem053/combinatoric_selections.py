#!/usr/bin/python

# Solution for Project Euler problem <num>, "<title>".
# http://projecteuler.net/problem=<num>

import sys; sys.path.insert(0, '..')

def solve(bound=101, thresh=1000000):
  total = 0
  for n in range(1, bound):
    for k in range(n):
      if combinations(n, k) > thresh:
        # print n, k, combinations(n, k)
        total += 1
  return total

# TODO(ipince): memoize
cache = {}
def combinations(n, k):
  if k == 0 or k == n: return 1
  if (n, k) in cache: return cache[(n, k)]
  ret = combinations(n - 1, k - 1) + combinations(n - 1, k)
  cache[(n, k)] = ret
  return ret

print solve()
