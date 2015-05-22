#!/usr/bin/pyhon

# Solution for Project Euler problem <num>, "<title>".
# http://projecteuler.net/problem=<num>

def solve():
  x = 1
  while True:
    if check(x):
      return x
    x += 1

def check(x):
  k = sorted(str(x))
  return all([sorted(str(n * x)) == k for n in range(2, 7)])

print solve()
