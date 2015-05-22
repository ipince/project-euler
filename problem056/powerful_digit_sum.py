#!/usr/bin/python

# Solution for Project Euler problem <num>, "<title>".
# http://projecteuler.net/problem=<num>

def solve():
  sums = list()
  for a in range(100):
    for b in range(100):
      sums.append(sum(map(int, str(a ** b))))
  return max(sums)

print solve()
