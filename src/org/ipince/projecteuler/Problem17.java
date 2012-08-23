package org.ipince.projecteuler;

public class Problem17 {

    public static void main(String[] args) {
        String allNumbers = "";
        for (int i = 1; i <= 1000; i++) {
            allNumbers += getWords("" + i);
        }
        allNumbers = allNumbers.replaceAll("-", "");
        allNumbers = allNumbers.replaceAll(" ", "");
        System.out.println("Num letters is: " + allNumbers.length());
    }

    // Requires 1 <= n <= 1000.
    private static String getWords(String decimal) {
        int length = decimal.length();
        if (length == 1) {
            int digit = Integer.valueOf(decimal);
            switch (digit) {
            case 0: return ""; // Since "0" is not a valid input.
            case 1: return "one";
            case 2: return "two";
            case 3: return "three";
            case 4: return "four";
            case 5: return "five";
            case 6: return "six";
            case 7: return "seven";
            case 8: return "eight";
            case 9: return "nine";
            }
        } else if (length == 2) {
            if ("0".equals(decimal.substring(0, 1))) {
                return getWords(decimal.substring(1));
            } else if ("1".equals(decimal.substring(0, 1))) {
                int ones = Integer.valueOf(decimal.substring(1));
                switch (ones) {
                case 0: return "ten";
                case 1: return "eleven";
                case 2: return "twelve";
                case 3: return "thirteen";
                case 4: return "fourteen";
                case 5: return "fifteen";
                case 6: return "sixteen";
                case 7: return "seventeen";
                case 8: return "eighteen";
                case 9: return "nineteen";
                }
            } else { // 2, ..., 9
                int tens = Integer.valueOf(decimal.substring(0, 1));
                String tensWords = "";
                switch (tens) {
                case 2: tensWords = "twenty-"; break;
                case 3: tensWords = "thirty-"; break;
                case 4: tensWords = "forty-"; break;
                case 5: tensWords = "fifty-"; break;
                case 6: tensWords = "sixty-"; break;
                case 7: tensWords = "seventy-"; break;
                case 8: tensWords = "eighty-"; break;
                case 9: tensWords = "ninety-"; break;
                }
                return tensWords + getWords(decimal.substring(1));
            }
        } else if (length == 3) {
            String restWords = getWords(decimal.substring(1));
            if ("0".equals(decimal.substring(0, 1))) {
                return restWords;
            }
            return getWords(decimal.substring(0, 1)) + " hundred"
            + (restWords.isEmpty() ? "" : " and " + restWords);
        } else { // length == 4
            String restWords = getWords(decimal.substring(1));
            return getWords(decimal.substring(0, 1)) + " thousand"
            + (restWords.isEmpty() ? "" : " and " + restWords);
        }
        return null;
    }
}
