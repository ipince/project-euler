#!/usr/bin/pyhon

# Solution for Project Euler problem <num>, "<title>".
# http://projecteuler.net/problem=<num>

def solve():
  n = 285  # starting point
  while True:
    n += 2
    triang = triangular(n)
    if search(triang, n):
      return triang

def triangular(n):
  return n * (n + 1) / 2

def pentagonal(n):
  return n * (3 * n - 1) / 2

def search(target, n):
  # search for pentagonal that equals target
  hi = n
  lo = 1
  while hi - lo > 0:
    mid = (hi + lo) / 2
    pent = pentagonal(mid)
    if pent > target:
      hi = mid
    elif pent < target:
      lo = mid + 1
    else:
      return mid
  return None

print solve()
