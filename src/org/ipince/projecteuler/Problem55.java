package org.ipince.projecteuler;

import java.math.BigInteger;

public class Problem55 {

    private static final int UPPER_BOUND = 10000;
    private static final int MAX_ATTEMPTS = 31;

    public static void main(String[] args) {
        int count = 0;
        outer:
            for (int i = 0; i < UPPER_BOUND; i++) {
                BigInteger current = BigInteger.valueOf(i);
                for (int t = 0; t < MAX_ATTEMPTS; t++) {
                    current = current.add(reverse(current));
                    if (isPalindrome(current)) {
                        continue outer;
                    }
                }
                count++;
            }
        System.out.println(count);
    }

    private static boolean isPalindrome(BigInteger n) {
        String str = n.toString();
        String reverse = reverse(str);
        return str.equals(reverse);
    }

    private static BigInteger reverse(BigInteger n) {
        String reversedStr = reverse(n.toString());
        BigInteger reverse = BigInteger.ZERO;
        for (int i = 0; i < reversedStr.length(); i++) {
            reverse = reverse.add(BigInteger.TEN.pow(reversedStr.length() - i - 1).multiply(
                    BigInteger.valueOf(Integer.valueOf(reversedStr.charAt(i) + ""))));
        }
        return reverse;
    }

    private static String reverse(String str) {
        String reverse = "";
        for (int i = 0; i < str.length(); i++) {
            reverse += str.charAt(str.length() - i - 1);
        }
        return reverse;
    }
}
