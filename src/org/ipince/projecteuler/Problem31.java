package org.ipince.projecteuler;

import java.util.Arrays;
import java.util.List;

/**
 * Use a recursive strategy.
 */
public class Problem31 {

    public static void main(String[] args) {
        List<Integer> sortedParts = Arrays.asList(200, 100, 50, 20, 10, 5, 2, 1);
        System.out.println(countWays(200, sortedParts, 0));
    }

    private static int countWays(int goal, List<Integer> sortedParts, int partialResult) {
        if (sortedParts.isEmpty() || partialResult > goal) {
            return 0;
        } else if (goal == partialResult) {
            return 1;
        }
        int newPartialResult = partialResult + sortedParts.get(0);
        if (newPartialResult <= goal) {
            // We can keep using the max part normally, OR we can stop using.
            return countWays(goal, sortedParts, newPartialResult)
                    + countWays(goal, sortedParts.subList(1, sortedParts.size()), partialResult);
        } else if (newPartialResult > goal) {
            // We maxed out on using the max part. Let's try building the difference with the rest of parts.
            return countWays(goal, sortedParts.subList(1, sortedParts.size()), partialResult);
        }
        return 0;
    }

}
