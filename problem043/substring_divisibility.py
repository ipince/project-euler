#!/usr/bin/python

# Solution for Project Euler problem <num>, "<title>".
# http://projecteuler.net/problem=<num>

from itertools import permutations

def solve():
  s = 0
  for n in permutations('0123456789'):
    if n[0] == '0': continue
    # ordered from 17 -> 2 to optimize; saves 30% of time
    if int(''.join(n[7:10])) % 17 != 0: continue
    if int(''.join(n[6:9])) % 13 != 0: continue
    if int(''.join(n[5:8])) % 11 != 0: continue
    if int(''.join(n[4:7])) % 7 != 0: continue
    if int(''.join(n[3:6])) % 5 != 0: continue
    if int(''.join(n[2:5])) % 3 != 0: continue
    if int(''.join(n[1:4])) % 2 != 0: continue
    s += int(''.join(n))
  return s

print solve()
