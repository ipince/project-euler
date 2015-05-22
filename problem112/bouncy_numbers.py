#!/usr/bin/python

def bouncy(n):
  digs = str(n)
  diffs = [int(x) - int(digs[i - 1]) for i, x in enumerate(digs)][1:]
  increasing = all(map(lambda x: x >= 0, diffs))
  decreasing = all(map(lambda x: x <= 0, diffs))
  return not increasing and not decreasing

def solve(thresh):
  x = 1
  total = 0
  bouncies = 0
  while True:
    if bouncy(x):
      bouncies += 1
    total += 1
    pct = bouncies * 1.0 / total
    if pct > thresh:
      return x - 1
    x += 1

print solve(0.99)
