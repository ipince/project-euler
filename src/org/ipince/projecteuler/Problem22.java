package org.ipince.projecteuler;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Problem22 {

    private static final String DIR = System.getProperty("user.dir");
    private static final String FILENAME = "names.txt";
    private static final String PATH = DIR + "/src/org/ipince/projecteuler/" + FILENAME;

    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File(PATH));
        String allNames = scanner.next();
        String[] nameArray = allNames.split(",");
        List<String> names = Arrays.asList(nameArray);
        Collections.sort(names);
        int sum = 0;
        for (int i = 0; i < names.size(); i++) {
            int nameScore = 0;
            for (char c : names.get(i).toCharArray()) {
                if (c != '"') {
                    nameScore += c - 'A' + 1;
                }
            }
            sum += (i + 1) * nameScore;
        }
        System.out.println(sum);
    }

}
