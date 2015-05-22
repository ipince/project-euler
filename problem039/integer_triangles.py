#!/usr/bin/pyhon

# Solution for Project Euler problem <num>, "<title>".
# http://projecteuler.net/problem=<num>

# ref: http://mathworld.wolfram.com/PythagoreanTriple.html

from collections import defaultdict

import ast

def solve(limit):
  triplets = load_triplets()
  sums = defaultdict(list)
  for (a, b, c) in triplets:
    k = 1
    while True:
      s = (a + b + c) * k
      if s <= limit:
        sums[s].append((k * a, k * b, k * b))  # no need to keep, but nice
      else:
        break
      k += 1
  m = max(sums.iteritems(), key=lambda (k, v): len(v))
  print m
  return m[0]

def load_triplets():
  text = open('triplets.txt').read()
  return ast.literal_eval('[' + ','.join(text.split()) + ']')

print solve(1000)
