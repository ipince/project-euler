package org.ipince.projecteuler;

import java.math.BigInteger;

public class Problem16 {

    public static void main(String[] args) {
        BigInteger two = BigInteger.valueOf(2);
        BigInteger current = two.pow(1000);
        int sum = 0;
        int length = current.toString().length();
        for (int i = 0; i < length; i++) {
            sum += current.mod(BigInteger.valueOf(10)).intValue();
            current = current.divide(BigInteger.valueOf(10));
        }
        System.out.println("Sum of digits is: " + sum);
    }

}
