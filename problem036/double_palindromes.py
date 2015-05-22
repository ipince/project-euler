#!/usr/bin/pyhon

# Solution for Project Euler problem 36, "Double-base palindromes".
# http://projecteuler.net/problem=36

def solve(bound):
  palindromes10 = [n for n in xrange(1, bound + 1) if str(n) == str(n)[::-1]]
  double_palindromes = []
  for p in palindromes10:
    if bin(p)[2:] == bin(p)[2:][::-1]:
      double_palindromes.append(p)
  return sum(double_palindromes)

print solve(1000000)
