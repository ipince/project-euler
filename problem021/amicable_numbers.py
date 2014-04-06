#!/usr/bin/python

# Solution for Project Euler problem 21, "Amicable numbers".
# http://projecteuler.net/problem=21

def solve(limit):
  total = 0
  for x in xrange(1, limit):
    dx = sum(divisors(x))
    if dx != x and sum(divisors(dx)) == x:
      total += x
  return total

def divisors(n):
  return [d for d in xrange(1, n) if n % d == 0]

print solve(10000)
