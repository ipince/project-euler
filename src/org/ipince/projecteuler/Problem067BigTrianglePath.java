package org.ipince.projecteuler;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Problem067BigTrianglePath {

    private static final String DIR = System.getProperty("user.dir");
    private static final String FILENAME = "problem67-triangle.txt";
    private static final String PATH = DIR + "/src/org/ipince/projecteuler/"
        + FILENAME;

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(PATH));
        StringBuilder contentBuilder = new StringBuilder();
        int depth = 0;
        while (scanner.hasNextLine()) {
            contentBuilder.append(scanner.nextLine()).append("\n");
            depth++;
        }
        int[][] triangle = populateTriangle(initTriangle(depth), contentBuilder.toString());
        int[][] maxSums = findAllMaxSums(triangle);
        System.out.println(maxSums[depth - 1]);
        List<Integer> lastRow = new ArrayList<Integer>();
        for (int val : maxSums[depth - 1]) {
            lastRow.add(val);
        }
        Collections.sort(lastRow);
        System.out.println(lastRow.get(lastRow.size()-1));
        System.out.println(Arrays.toString(maxSums[depth - 1]));
    }
    
    private static int[][] findAllMaxSums(int[][] triangle) {
        int[][] currentSums = initTriangle(triangle.length);
        for (int row = 0; row < triangle.length; row++) {
            for (int col = 0; col < triangle[row].length; col++) {
                findMaxSum(triangle, currentSums, row, col);
            }
        }
        return currentSums;
    }
    
    private static void findMaxSum(int[][] triangle, int[][] currentSums,
        int row, int col) {
        if (row == 0) {
            currentSums[row][col] = triangle[row][col];
        } else if (col == 0) {
            // At LHS edge.
            currentSums[row][col] =
                currentSums[row - 1][0] + triangle[row][col];
        } else if (col == triangle[row].length - 1) {
            // At RHS edge.
            currentSums[row][col] =
                currentSums[row - 1][col - 1] + triangle[row][col];
        } else {
            currentSums[row][col] =
                Math.max(currentSums[row - 1][col - 1],
                         currentSums[row - 1][col]) +
                triangle[row][col];
        }
    }

    public static int[][] initTriangle(int depth) {
        int[][] triangle = new int[depth][];
        for (int i = 0; i < depth; i++) {
            triangle[i] = new int[i + 1];
        }
        return triangle;
    }

    public static int[][] populateTriangle(int[][] triangle, String data) {
        // populate triangle
        Scanner scanner = new Scanner(data);
        int row = 0;
        while (scanner.hasNextLine()) {
            String[] nums = scanner.nextLine().split(" ");
            for (int col = 0; col < nums.length; col++) {
                triangle[row][col] = Integer.valueOf(nums[col]);
            }
            row++;
        }
        return triangle;
     }
}
