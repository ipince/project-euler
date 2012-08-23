package org.ipince.projecteuler;

import java.math.BigInteger;

public class Problem14 {

    private static final int ONE_MILLION = 1000000;
    private static final Integer[] COLLATZ_LENGTHS = new Integer[ONE_MILLION];
    private static final BigInteger TWO = BigInteger.valueOf(2);
    private static final BigInteger THREE = BigInteger.valueOf(3);

    // k is saved at array[k - 1]
    public static void main(String[] args) {
        for (int i = 1; i < ONE_MILLION; i++) {
            countCollatzLength(BigInteger.valueOf(i));
        }

        // Find biggest number in array.
        int max = 0;
        int seed = 0;
        for (int i = 1; i < COLLATZ_LENGTHS.length; i++) {
            if (COLLATZ_LENGTHS[i] != null) {
                if (COLLATZ_LENGTHS[i] > max) {
                    max = COLLATZ_LENGTHS[i];
                    seed = i + 1;
                }
            }
        }
        System.out.println("Largest length is: " + max + ", with seed: " + seed);
    }

    // Require n > 0
    private static int countCollatzLength(BigInteger n) {
        int index = n.compareTo(BigInteger.valueOf(ONE_MILLION)) < 0 ? n.intValue() : -1;
        if (index > 0 && COLLATZ_LENGTHS[index - 1] != null) {
            return COLLATZ_LENGTHS[index - 1];
        }
        int length;
        if (n.equals(BigInteger.ONE)) {
            length = 1;
        } else {
            if (n.mod(TWO).equals(BigInteger.ZERO)) {
                length = 1 + countCollatzLength(n.divide(TWO));
            } else {
                length = 1 + countCollatzLength(n.multiply(THREE).add(BigInteger.ONE));
            }
        }
        if (index > 0) {
            COLLATZ_LENGTHS[index - 1] = length;
        }
        return length;
    }
}
