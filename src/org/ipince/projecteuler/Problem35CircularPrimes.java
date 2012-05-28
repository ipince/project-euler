package org.ipince.projecteuler;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * TODO(ipince): copy problem statement and reference it here. running time?
 */
public class Problem35CircularPrimes {

    private static int NUM_CIRCULAR_PRIMES = 0;

    public static void main(String[] args) {
        long start = System.currentTimeMillis();
        // Need to c
        precalculatePrimesUntil(1000); // sqrt 1000,000
        System.out.println(PRIMES.size() + " under 1000");
        System.out.println("Primes are: " + PRIMES);
        System.out.println("Elapsed: " + (System.currentTimeMillis() - start)
                + "ms");
        isCircularPrime(new Integer[] { 2 });
        for (int i = 1; i < 1000000; i++) {
            countCircularPrime(i);
        }
        System.out.println("Num circular primes: " + NUM_CIRCULAR_PRIMES);
    }

    // NOTE: never makes sense to check a number whose digits are not ascending.

    // Assumes each element in the digits array is 0 <= d <= 9.
    private static boolean isCircularPrime(Integer[] digits) {
        int candidate = 0;
        for (int offset = 0; offset < digits.length; offset++) {
            candidate = 0;
            for (int i = 0; i < digits.length; i++) {
                candidate += digits[(i + offset) % digits.length] * Math.pow(10, digits.length - i - 1);
            }
            System.out.println("Candidate is: " + candidate);
        }
        return false;
    }

    private static void countCircularPrime(int initial) {
        int length = ("" + initial).length();
        int current = initial;
        Set<Integer> rotations = new HashSet<Integer>();
        for (int i = 0; i < length; i++) {
            int lastDigit = current % 10;
            int firstDigits = current / 10;
            current = (int) (lastDigit * Math.pow(10, length - 1) + firstDigits);
            rotations.add(current);
        }
        int minRotation = getMin(rotations);
        if (minRotation != initial) {
            // Should check with min rotation! Feel free to ignore.
            return;
        }
        for (int rotation : rotations) {
            if (!isPrime(rotation)) {
                return;
            }
        }
        // Reached here, we got a (many) circular prime!
        NUM_CIRCULAR_PRIMES += rotations.size();
    }

    private static int getMin(Set<Integer> numbers) {
        int min = Integer.MAX_VALUE;
        for (int i : numbers) {
            min = Math.min(min, i);
        }
        return min;
    }

    private static boolean isPrime(int p) {
        if (p < 2) {
            return false;
        }
        double sqrt = Math.sqrt(p);
        // Check for divisibility against known primes (below sqrt)
        int lastCheckedPrime = 2;
        for (int prime : PRIMES) {
            if (prime < sqrt && (p % prime) == 0) {
                return false;
            }
        }
        // Maybe we don't have enough primes yet, so keep checking numbers.
        for (int d = lastCheckedPrime; d <= sqrt; d++) {
            if ((p % d) == 0) {
                return false;
            }
        }
        return true;
    }

    // Sorted list of known primes.
    private static final List<Integer> PRIMES = new ArrayList<Integer>();

    private static void precalculatePrimesUntil(int upperBound) {
        PRIMES.clear();
        PRIMES.add(2);
        PRIMES.add(3);
        // Check number of the form 6k+1 or 6k+5.
        int upperK = upperBound / 6 + 1;
        int candidate;
        for (int k = 0; k < upperK; k++) {
            candidate = 6 * k + 1;
            if (candidate < upperBound && isPrime(candidate)) {
                PRIMES.add(candidate);
            }
            candidate = 6 * k + 5;
            if (candidate < upperBound && isPrime(candidate)) {
                PRIMES.add(candidate);
            }
        }
    }
}
