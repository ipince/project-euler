# [Problem <num>](<url>): <title>

**NOTE: Spoilers below!**

---

**Idea:**
<Idea>

## Solution (Pencil and paper)

numbers of 1 digit take 9 positions (1-9)
numbers of 2 digits take 180 positions (10-99)
in general, numbers of d digits take d * ((10^d - 1) - 10^(d-1) + 1) positions

thus, the number of positions taken by numbers of d digits are:
1 -> 9
2 -> 180
3 -> 2,700
4 -> 36,000
5 -> 450,000
6 -> 5,400,000
7 -> 63,000,000

d1 = 1
d10 = 10 = 1
d100 = ((100-9)/2)th 2-digit num = 10 + (100-9)/2 = 55 + 1/2 => offset 0 => 5
d1000 = ((1000-180-9)/3)th 3-digit num = 100 + (100-180-9)/3 = 370 + 1/3 => offset 0 => 3
d10000 = 1000 + (10000-2700-180-9)/4 = 1777 + 3/4 => offset 2 => 7
d100000 = 10000 + (100000-36,000-2,700-180-9)/5 = 1,222 + 1/5 => offset 0 => 1
d1000000 = 

ans => 210

--

The solution runs in <time> and returns the answer <answer>.

