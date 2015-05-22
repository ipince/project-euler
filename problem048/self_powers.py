#!/usr/bin/python

def solve(limit, mod):
  return reduce(lambda x, y: x + y % mod, [pow(x, x, mod) for x in range(1, limit + 1)])

print solve(1000, 10000000000)
