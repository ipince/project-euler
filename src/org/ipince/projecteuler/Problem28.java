package org.ipince.projecteuler;

// TODO(ipince): explain and find paper and pencil solution.
public class Problem28 {

    public static void main(String[] args) {
        int spiralLength = 1001; // must be odd
        int sum = 0;
        for (int k = 1; k <= spiralLength / 2; k++) {
            sum += 4 * k * k + k + 1;
        }
        sum = 4 * sum + 1;
        System.out.println(sum);
    }

}
