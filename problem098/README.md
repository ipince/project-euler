# Problem 98: Anagramic Squares - Solution

Problem statement here.

Spoiler alert: Solution below.

My solution to this problem doesn't involve any special tricks. It's plain old brute force, but with some small optimizations along the way. Judging the problem statement, I didn't think any math would yield a simple solution, the search space seemed small enough (a list of 2,000 words and their possible combinations), and the problem itself explicitly says "find all the square anagram word pairs", so brute force it is!

## Finding the word anagrams

First we restrict our search to real word anagrams. Instead of checking all n-choose-2 pairs (just under 2 million of them), we hash all the words into a hash map. The key or hash for a word is the word itself with its characters sorted. The value is a list of the words with the same hash (anagrams!). The collisions in this hashing scheme yields the set of anagrams. We can find all anagrams in linear time, O(n).

The code is in `find_anagrams()`.

## Finding a mapping for a word

We have a list of anagram word "sets" (there can be more than two words in a set, all pairwise anagramic). We define a "mapping" as a map from characters to digits. A mapping is "valid" for a word if: (a) it is injective (different characters map to different digits), (b) when applied to the word, it yields a square number with the same number of digits as the length of the word (no leading zeros). The general strategy now is to find a valid mapping for a word in an anagram word set, and then check if the mapping is also valid for any other word in the set.

The space of possible mappings is huge; the space of square numbers of a given length is relatively small. For example, a word of 10 characters can have 10^10 possible mappings (well, a little less since we can't have repeated digits); there are only 68,377 square numbers that are 10 digits long. Thus, we start by getting all square numbers of a given length and then try to find a mapping that would map a word to it, and maintaining the other properties that would make the mapping "valid" for the word.

The `get_squares()` function gets us the square number candidates to find mappings for. It uses a neat little trick to avoid having to multiply numbers together to find the squares. Instead, it just adds consecutive odd numbers to the previous squares. You can read about why that works here: http://betterexplained.com/articles/surprising-patterns-in-the-square-numbers-1-4-9-16/. This function gets called multiple times, so we memoize it to improve performance a bit.

The `get_mapping()` function find a valid mapping from a given word to a given square. Note that sometimes no such mapping exists.

## Checking a mapping against a word

We now have a word and a valid mapping for it. We just need to check if the mapping is also valid for any other word in the anagram word set. The `check_mapping` function checks a mapping for validity by generating the mapped number from the word. We then iterate through other words in the word set and check the mapping (in `largest_anagram_square`). We put all the resulting squares in a set so that we can output the largest square (if any) after the iterations.

## Putting it all together

All the pieces are there now. The last step is to find the largest square we can form. To do so, we iterate through our anagram sets from largest to smallest, keeping track of the largest square we've seen so far (if any). While iterating, if we have seen a square (our candidate) and our anagram word sets decrease in size, then we can stop, since we know all squares we'll see in the future must be smaller than our candidate. So in fact, we disobeyed the problem statement because we never found _all_ the square anagram word pairs. This is what happens under the `solve()` function.

And that's it!

This solution runs in 560ms without square number memoization and in 480 ms with memoization. Not very fast, but good enough. More optimizations can be made, but aren't worth it for me. Oh, and the solution is 18769, coming from BOARD (17689) and BROAD (18769).

