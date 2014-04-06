# [Problem 19](http://projecteuler.net/problem=19): Counting Sundays

**NOTE: Spoilers below!**

---

**Idea:**
Count the Sundays manually, with pencil and paper (or a keyboard and vim).

## Solution (Pencil + Paper)

- 365 modulo 7 is 1. So, for example, if Jan 1st, falls on a Monday on a non-leap year, then next year Jan 1st will be a Tuesday.
- If the year is a leap year, of course, then Jan 1st would be a Wednesday.
- From 1901 to 2000, we only have to care about leap years than are divisible by 4. The century and 400 years rule do not apply in this timeframe. (2000 is divisible by 400, so it is a leap year, as expected if the divisible-by-4 rule had no exceptions.
- We should look at 4-year intervals then. Moreover, let's look at how many 4-year intervals we need in order for a loop to happen. Now, if Jan 1st was a Monday on year1, then it'll fall on Tues, Weds, Fri, on years 2, 3, and 4, respectively. Going forward, Jan 1st will land on Sat, Sun, Mon, Weds; Thurs, Fri, Sat, Mon; Tues, Weds, Thurs, Sat; Sun, Mon, Tues, Thurs; Fri, Sat, Sun, Tues; Weds, Thurs, Fri, Sun; Mon... aha! So, after 7 4-year periods, we're back were we started. And we had 4 Mondays, 4 Tuesdays, ..., 4 Sundays(!) fall on Jan 1st. The same should happen for Feb, March, etc.
- Now we just have to find how many 28 year periods fit from 1901 to 2000. Three of those fit wholly. For the remainder 16 years, how many Jan 1st's were Sundays? Since the 28 year periods are symmetrical, it suffices to count the first 16 years.
- In the first 16 years, given that Jan 1, 1900 was a Monday, we have: Tues (1901), Weds, Thurs, Fri (1904 leap), Sun, Mon, Tues, Weds (1908 leap), Fri, Sat, Sun, Mon (1912 leap), Weds, Thurs, Fri, Sat (1916 leap). Thus, we have 2 Sundays.
- Taken together, we have 6 Sundays falling on Jan 1st from 1901 to 2000.
- We need to repeat the first-16-years analysis for Feb thru December though, since it is not symmetrical like the 28-year periods are.
- Feb 1st is 31 days after Jan 1st. 31 modulo 7 is 3. So Feb 1st was Sunday whenever Jan 1st was Thurs, which was twice.
- March is the same as Feb, except in 1904, 1908, and 1912. Thus, in total, we have 2 + 1 (1908), totalling 3. Let's write down the days of the week for March, since computing onwards with the February optional shifts can be confusing: Fri (1901), Sat, Sun, Tues (1904 leap), Weds, Thurs, Fri, Sun (1908 leap), Mon, Tues, Weds, Fri (1912 leap), Sat, Sun, Mon, Weds (1916 leap).
- April is 31 days after March, meaning March's Thursdays become April's Sundays. So we have 1 here.
- May is 31+30 after March (which is 5 modulo 7), so March's Tuesdays become May's Sundays. So we have 2 here.
- Similarly: June, 5+3 mod 7 = 1 off March, so that's 2; July, 1+2 mod 7, so that's 1; Aug, 3+3 mod 7, so that's 2; Sep, 6+3 mod 7, so that's 3; Oct, 2+2 mod 7, so that's 3; Nov, 4+3 mod 7, so that's 3; and Dec, 0+2 mod 7, so that's 3.
- Thus, in the first 16 years we have 2 + 2 + 3 + 1 + 2 + 2 + 1 + 2 + 3 + 3 + 3 + 3 = 27.
- Adding the 3 28-year periods, that yield 4 Sundays on the first of each month, totals 27 + 3 * 4 * 12 = 171.

--

The solution took some 30 mins and yields returns the answer <answer>.
