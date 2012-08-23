package org.ipince.projecteuler;

public class Problem33 {

    public static void main(String[] args) {
        double product = 1;
        for (int d = 11; d <= 99; d++) {
            for (int n = 10; n < d; n++) {
                double value = 1.0 * n / d;
                String numerator = n + "";
                String denominator = d + "";
                String numerTens = numerator.substring(0, 1);
                String numerOnes = numerator.substring(1);
                String denomTens = denominator.substring(0, 1);
                String denomOnes = denominator.substring(1);
                double otherValue = 1; // all values must be < 1.
                if (numerTens.equals(denomOnes)) {
                    // Check if fractions agree.
                    otherValue = Integer.valueOf(numerOnes) * 1.0 / Integer.valueOf(denomTens);
                } else if (numerOnes.equals(denomTens)) {
                    otherValue = Integer.valueOf(numerTens) * 1.0 / Integer.valueOf(denomOnes);
                }
                if (value == otherValue) {
                    product *= value;
                    System.out.println(numerator + " / " + denominator);
                    System.out.println(value);
                    System.out.println(otherValue);
                }
            }
        }
        System.out.println("Product of fractions is: " + product);
    }

}
