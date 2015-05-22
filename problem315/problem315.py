#!/usr/bin/python

from collections import defaultdict

class Segment:
  TOP_HOR = 1
  TOP_LEFT = 2
  TOP_RIGHT = 3
  MIDDLE_HOR = 4
  BOTTOM_LEFT = 5
  BOTTOM_RIGHT = 6
  BOTTOM_HORIZO = 7  # cool ladder!

NUMBERS = {
  1: {Segment.TOP_RIGHT, Segment.BOTTOM_RIGHT},
  2: {Segment.TOP_HOR, Segment.TOP_RIGHT, Segment.MIDDLE_HOR, Segment.BOTTOM_LEFT, Segment.BOTTOM_HORIZO},
  3: {Segment.TOP_HOR, Segment.TOP_RIGHT, Segment.MIDDLE_HOR, Segment.BOTTOM_RIGHT, Segment.BOTTOM_HORIZO},
  4: {Segment.TOP_LEFT, Segment.TOP_RIGHT, Segment.MIDDLE_HOR, Segment.BOTTOM_RIGHT},
  5: {Segment.TOP_HOR, Segment.TOP_LEFT, Segment.MIDDLE_HOR, Segment.BOTTOM_RIGHT, Segment.BOTTOM_HORIZO},
  6: {Segment.TOP_HOR, Segment.TOP_LEFT, Segment.MIDDLE_HOR, Segment.BOTTOM_LEFT, Segment.BOTTOM_RIGHT, Segment.BOTTOM_HORIZO},
  7: {Segment.TOP_LEFT, Segment.TOP_HOR, Segment.TOP_RIGHT, Segment.BOTTOM_RIGHT},
  8: {Segment.TOP_HOR, Segment.TOP_LEFT, Segment.TOP_RIGHT, Segment.MIDDLE_HOR, Segment.BOTTOM_LEFT, Segment.BOTTOM_RIGHT, Segment.BOTTOM_HORIZO},
  9: {Segment.TOP_HOR, Segment.TOP_LEFT, Segment.TOP_RIGHT, Segment.MIDDLE_HOR, Segment.BOTTOM_RIGHT, Segment.BOTTOM_HORIZO},
  0: {Segment.TOP_HOR, Segment.TOP_LEFT, Segment.TOP_RIGHT, Segment.BOTTOM_LEFT, Segment.BOTTOM_RIGHT, Segment.BOTTOM_HORIZO},
}

def saved_transitions(n):
  if n < 10:
    return 0
  dsum = digitsum(n)
  return 2 * overlap(dsum, n) + saved_transitions(dsum)

def digitsum(n):
  return sum(map(int, str(n)))

def overlap(n1, n2):
  digit_pairs = zip(reversed(map(int, str(n1))), reversed(map(int, str(n2))))
  return sum(map(lambda (a, b): len(NUMBERS[a].intersection(NUMBERS[b])), digit_pairs))

def primes(lower, upper):
  sieve = defaultdict(lambda: True)
  primes = list()
  if lower < 2:
    primes.append(2)
  for p in xrange(3, upper, 2): # odd numbers
    if sieve[p]:
      if p >= lower:
        primes.append(p)
      m = p
      while m < upper:
        m += p
        sieve[m] = False
  return primes

def solve():
  ps = primes(10000000, 20000000)
  print sum(map(saved_transitions, ps))

