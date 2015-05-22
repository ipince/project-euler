#!/usr/bin/pyhon

# Solution for Project Euler problem 42, "Coded triangle numbers".
# http://projecteuler.net/problem=42

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solve():
  words = load_words()
  trinums = triangles(9 * pow(10, len(max(words))))
  count = 0
  for w in words:
    if wordsum(w) in trinums:
      count += 1
  return count

def load_words():
  words = open('words.txt').read()
  return words.replace('"', '').split(',')

def triangles(bound):
  inc = 2
  t = set()
  last = 1
  while True:
    if last > bound:
      break
    t.add(last)
    last += inc
    inc += 1
  return t

def wordsum(word):
  return sum([ALPHA.index(c) + 1 for c in word])

print solve()
