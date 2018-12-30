import java.util.Scanner;
import java.io.*;

public class LargeSum {
    public static void main(String[] args) {
        String result = "";
        String[] numbers = new String[100];

        try {
            Scanner in = new Scanner(new File("numbers.txt"));

            int i = 0;

            while (in.hasNextLine()) {
                String line = in.nextLine();
                numbers[i] = line;
                i++;
            }

            in.close();
        }
        catch (FileNotFoundException e) { System.out.println("File was not found"); }

        result = sum(numbers[0],numbers[1]);

        for (int i = 2; i <= 99; i++) {
            result = sum(result, numbers[i]);
        }

        System.out.println(result);

        //System.out.println(sum("666","99"));
    }

    public static String sum(String n1, String n2) {
        String result = "";

        int remainder = 0;

        int max = Math.max(n1.length(), n2.length());

        for (int i = 0; i < max; i++) {
            int i1 = 0;
            int i2 = 0;

            if (n1.length() == max) {
                if (n2.length() - 1 - i < 0) {
                    i1 = Integer.parseInt((n1.charAt(n1.length()-1-i) + ""));
                    i2 = 0;
                }
                else {
                    i1 = Integer.parseInt((n1.charAt(n1.length()-1-i) + ""));
                    i2 = Integer.parseInt((n2.charAt(n2.length()-1-i) + ""));
                }
            }
            else {
                if (n2.length() - 1 - i < 0) {
                    i1 = 0;
                    i2 = Integer.parseInt((n2.charAt(n2.length()-1-i) + ""));
                }
                else {
                    i1 = Integer.parseInt((n1.charAt(n1.length()-1-i) + ""));
                    i2 = Integer.parseInt((n2.charAt(n2.length()-1-i) + ""));
                }
            }

            int r = 0;

            if (remainder > 0) {
                if (i1+i2+remainder <= 9) {
                    r = i1 + i2 + remainder;
                    remainder = 0;
                }
                else if (i == n1.length() - 1 ) {
                    r = (i1 + i2 + remainder);
                }
                else {
                    r = ((i1 + i2 + remainder) % 10);
                    remainder = 1;
                }
            }
            else {
                if (i1+i2 <= 9) {
                    r = i1 + i2;
                }
                else if (i == n1.length() - 1) {
                    r = i1 + i2;
                }
                else {
                    r = ((i1 + i2) % 10);
                    remainder = 1;
                }
            }

            result = r + result;
        }

        return result;
    }
}
