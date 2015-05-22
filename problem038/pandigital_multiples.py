#!/usr/bin/python

# Solution for Project Euler problem <num>, "<title>".
# http://projecteuler.net/problem=<num>

from itertools import count

def solve():
  matches = list()
  for m in range(2, 10):
    for n in count():
      p = concat_product(n, m)
      if p < 100000000: continue
      if p >= 1000000000: break
      if is_pandigital(p, 9):
        matches.append(p)
  print matches
  return max(matches)

def concat_product(n, m):
  tup = tuple(range(1, m + 1))
  prods = map(lambda x: n * x, tup)
  return int(''.join(map(str, prods)))

def is_pandigital(n, d):
  return ''.join(sorted(str(n))) == '123456789'[:d]

print solve()
