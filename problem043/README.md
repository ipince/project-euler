# [Problem <num>](<url>): <title>

**NOTE: Spoilers below!**

---

**Difficulty:** [Easy | Medium | Hard | Really hard]

**Idea:**
<Idea>

## Solution (Pencil + Paper)

* We will use a table to keep track of possible values for each digit. For example, we know that
`d2d3d4` must be divisible by 2, so `d4 = 0, 2, 4, 6, 8`. Thus, we fill out the table as such:

    0  1  2  3  4  5  6  7  8  9
d1  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?
d2  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?
d3  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?
d4  ?  -  ?  -  ?  -  ?  -  ?  -
d5  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?
d6  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?
d7  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?
d8  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?
d9  ?  ?  ?  ?  ?  ?  ?  ?  ?  ?
d10 ?  ?  ?  ?  ?  ?  ?  ?  ?  ?

* We know that `d4d5d6` is divisible by 5, so `d6 = 0, 5`. But if `d6 = 0`, then `d6d7d8 = 0d7d8` is divisible by 11.
There are no multiples of 11 below 100 that have different digits, so `d6` cannot be 0. Thus, `d6 = 5` and we've just
reduced our search space by a factor of 10.
* Multiples of 11 in the 500s are `506, 517, 528, 539, 550, 561, 572, 583, 594`. We can exclude `550` since it repeats
digits. By looking at the tenths and unit digits, we can learn that `d7 != 4` and `d8 != 0`. Filling in the table:

    0  1  2  3  4  5  6  7  8  9
d1  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d2  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d3  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d4  ?  -  ?  -  ?  -  ?  -  ?  -
d5  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d6  -  -  -  -  -  x  -  -  -  -
d7  ?  ?  ?  ?  -  -  ?  ?  ?  ?
d8  -  ?  ?  ?  ?  -  ?  ?  ?  ?
d9  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d10 ?  ?  ?  ?  ?  -  ?  ?  ?  ?

* The multiples of 7 that have `5` as a middle digit are: `056, 154, 252, 259, 350, 357, 455, 553, 651, 658, 756, 854, 952, 959`.
Of those, we can discard `252, 455, 553, 959` for repeating digits and `154, 854` for ending in `4`. Thus, the remaining options
for `d5d6d7` are `056, 259, 350, 357, 651, 658, 756, 952`. Leaving us with:

    0  1  2  3  4  5  6  7  8  9
d1  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d2  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d3  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d4  ?  -  ?  -  ?  -  ?  -  ?  -
d5  ?  -  ?  ?  -  -  ?  ?  -  ?
d6  -  -  -  -  -  x  -  -  -  -
d7  ?  ?  ?  -  -  -  ?  ?  ?  ?
d8  -  ?  ?  ?  ?  -  ?  ?  ?  ?
d9  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d10 ?  ?  ?  ?  ?  -  ?  ?  ?  ?

* Let's revisit the multiples of 11: `506, 517, 528, 539, 561, 572, 583, 594`, from which we can now discard
`539`, too. Thus, `d8 != 9`.

    0  1  2  3  4  5  6  7  8  9
d1  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d2  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d3  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d4  ?  -  ?  -  ?  -  ?  -  ?  -
d5  ?  -  ?  ?  -  -  ?  ?  -  ?
d6  -  -  -  -  -  x  -  -  -  -
d7  ?  ?  ?  -  -  -  ?  ?  ?  ?
d8  -  ?  ?  ?  ?  -  ?  ?  ?  -
d9  ?  ?  ?  ?  ?  -  ?  ?  ?  ?
d10 ?  ?  ?  ?  ?  -  ?  ?  ?  ?

* can use multiples of 17 to show `d9 != 2`.
* multiples of 13: no useful information.

## Solution (Python)

First, we check feasibility by checking that `10!` is just over 3.6M. We can definitely brute force our way through
3.6M operations, provided they're not very expensive.

--

The solution runs in <time> and returns the answer <answer>.

