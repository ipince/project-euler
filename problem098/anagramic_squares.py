#!/usr/bin/python

# Solution for Project Euler problem 98, "Anagramic Squares".
# http://projecteuler.net/problem=98

import math

def solve():
  anagrams = find_anagrams(load_words('words.txt'))
  anagrams = sorted(anagrams, key=lambda l: -len(l[0]))
  candidate = None
  while anagrams:
    wordset = anagrams.pop(0)
    if len(wordset[0]) < len(str(candidate)):
      return candidate
    largest = largest_anagram_square(wordset)
    if largest and largest > candidate:
      candidate = largest
  return None

def load_words(filename):
  """Loads a list of words from a file
  """
  content = open(filename).read()
  content = content.replace('"', '')
  content = content.replace('\n', '')
  words = content.split(',')
  return words

def find_anagrams(words):
  """Returns a list of anagram sets. Each anagram set is a list of the words in the set
  """
  canonicals = dict()
  for word in words:
    canonical = ''.join(sorted(word))
    if canonical not in canonicals:
      canonicals[canonical] = list()
    canonicals[canonical].append(word)
  anagrams = [value for value in canonicals.itervalues() if len(value) > 1]
  return anagrams

def largest_anagram_square(wordset):
  """Finds the largest anagramic square in the word set, if any.
  """
  solutions = set()
  squares = get_squares(len(wordset[0]))
  for word in wordset:
    for sq in squares:
      mapping = get_mapping(word, sq)
      if mapping:
        for w in wordset:
          if w == word:
            continue # ignore the word we used to get mapping with
          candidate = check_mapping(w, mapping, squares)
          if candidate:
            print 'Found match! Words are %s (%d), %s (%d). Mapping is %s' % (word, sq, w, candidate, mapping)
            solutions.add(candidate)
            solutions.add(sq)
  if solutions:
    return max(solutions)
  return None

sq_cache = {}
def get_squares(length):
  """Returns a sorted list of squares of <length> digits.
  """
  if length in sq_cache:
    return sq_cache[length]
  lower = 10**(length-1)
  upper = 10**length

  squares = list()
  sqrt_lower = int(math.sqrt(lower))
  sq = sqrt_lower**2
  diff = (sqrt_lower+1)**2 - sq
  while sq < upper:
    if sq >= lower:
      squares.append(sq)
    sq += diff
    diff += 2

  sq_cache[length] = squares
  return squares

def get_mapping(word, square):
  """Returns a valid mapping that maps the word to the square, if any exists.
  """
  sq_str = str(square)
  assert len(word) == len(sq_str)
  mapping = dict()
  for i in xrange(len(word)):
    if word[i] not in mapping:
      mapping[word[i]] = sq_str[i]
    elif mapping[word[i]] != sq_str[i]:
      return None
  if len(set(mapping.values())) < len(mapping.keys()):
    return None
  return mapping

def check_mapping(word, mapping, squares):
  """Checks if a mapping is valid for a word. Returns the square number it maps the word to if it is valid.
  """
  sq = int(reduce(lambda x, y: x + str(mapping[y]), word, ''))
  if sq in squares:
    # Note: no need to check for leading zeros since squares should only
    # contain square numbers with the right number of digits.
    return sq
  return None

print solve()
