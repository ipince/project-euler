package org.ipince.projecteuler;

import java.util.HashSet;
import java.util.Set;

public class Problem32 {

    public static void main(String[] args) {
        int sum = 0;
        // Note: limits for for loops chosen almost arbitrarily.
        for (int p = 1; p < 8000; p++) {
            for (int m1 = 1; m1 < 1000; m1++) {
                if ((p % m1) == 0) {
                    int m2 = p / m1;
                    if (isPandigital(m1, m2, p)) {
                        System.out.println(m1 + " * " + m2 + " = " + p);
                        sum += p;
                        break;
                    }
                }
            }
        }
        System.out.println("Sum is: " + sum);
    }

    private static boolean isPandigital(int m1, int m2, int p) {
        String concat = (m1 + "").concat(m2 + "").concat(p + "");
        if (concat.length() != 9) {
            return false;
        }
        Set<String> digitsUsed = new HashSet<String>();
        for (int i = 0; i < concat.length(); i++) {
            digitsUsed.add(concat.charAt(i) + "");
        }
        return digitsUsed.size() == 9 && !digitsUsed.contains("0");
    }

}
