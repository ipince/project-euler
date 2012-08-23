package org.ipince.projecteuler;

public class Problem6 {

    public static void main(String[] args) {
        int sum = 0;
        int sumOfSquares = 0;
        for (int i = 1; i <= 100; i++) {
            sum += i;
            sumOfSquares += i * i;
        }
        System.out.println("Sum of squares - square of sum = "
                + (sum * sum - sumOfSquares));
    }

}
