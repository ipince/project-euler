package org.ipince.projecteuler;

public class Problem9 {

    public static void main(String[] args) {
        int sum = 1000;
        for (int a = 1; a <= sum; a++) {
            int a2 = a * a;
            for (int b = a; b <= sum - a; b++) {
                int c = 1000 - b - a;
                int b2 = b * b;
                int c2 = c * c;
                if (a2 + b2 == c2) {
                    System.out.println("Triplet is (" + a + ", " + b + ", " + c
                            + "). Product is: " + (a * b * c));
                    break;
                }
            }
        }
    }

}
