public class Number {
    public static void main(String[] args) {
        //String result = "";

        //result = valueOfString("115");

        //System.out.println(result + " " + result.length());

        int result = 0;

        for (int i = 1; i <= 1000; i++) {
            String s = String.valueOf(i);

            //System.out.println(valueOfString(s));

            result += valueOfString(s).length();
        }

        System.out.println(result);
    }

    public static String valueOfString(String s) {
        String result = "";
        int n = Integer.parseInt(s);

        if (n < 20) result += belowTwentyString(s);
        else if (s.length() == 2) {
            char d1 = s.charAt(0);
            char d0 = s.charAt(1);

            if (d1 == '0') result += valueOfString(d0+"");
            else if (d1 == '1') {
                String lastTwoDigits = (d1 + "") + (d0 + "");
                //System.out.println(lastTwoDigits + " " + valueOfString(lastTwoDigits));
                result += valueOfString(lastTwoDigits);
            }
            else if (d1 == '2') result += "TWENTY" + valueOfString(d0 + "");
            else if (d1 == '3') result += "THIRTY" + valueOfString(d0 + "");
            else if (d1 == '4') result += "FORTY" + valueOfString(d0 + "");
            else if (d1 == '5') result += "FIFTY" + valueOfString(d0 + "");
            else if (d1 == '6') result += "SIXTY" + valueOfString(d0 + "");
            else if (d1 == '7') result += "SEVENTY" + valueOfString(d0 + "");
            else if (d1 == '8') result += "EIGHTY" + valueOfString(d0 + "");
            else if (d1 == '9') result += "NINETY" + valueOfString(d0 + "");
        }
        else if (s.length() == 3) {
            char d2 = s.charAt(0);
            char d1 = s.charAt(1);
            char d0 = s.charAt(2);

            if (d2 == '0' && (d1 != '0' || d0 != '0')) result += "AND";
            else if (d2 != '0' && (d1 != '0' || d0 != '0')) {
                String last = ((d1 + "") + (d0 + ""));
                //System.out.println(last + " " + belowTwentyString(last));
                result += belowTwentyString(d2 + "") + "HUNDRED" + "AND" + valueOfString(last);
            }
            else if (d2 != '0') result += belowTwentyString(d2 + "") + "HUNDRED";
        }
        else if (s.length() == 4) {
            result += "ONETHOUSAND";
        }

        return result;
    }

    public static long valueOf(String n) {
        long result = 0;

        if (n.length() <= 2){
            result += belowTwenty(n);
        }
        if (n.length() > 2) {
            if (n.charAt( n.length() - 2) == '0') {
                String lastTwoDigits = (n.charAt(n.length() - 2) + "") + (n.charAt(n.length() - 1) + "");
                result += belowTwenty(lastTwoDigits);
            }

            for (int i = n.length() - 3; i >= 0; i--) {
                char d = n.charAt(i);

                if (n.length() - i == 2) result += digit(d) + 7;
                else if (n.length() - i == 3) result += digit(d) + 8;
            }
        }

        return result;
    }

    public static long belowTwenty(String s) {
        long result = 0;
        int n = Integer.parseInt(s);

        if (n == 1) result += 3;
        else if (n == 2) result = 3;
        else if (n == 3) result = 5;
        else if (n == 4) result = 4;
        else if (n == 5) result = 4;
        else if (n == 6) result = 3;
        else if (n == 7) result = 5;
        else if (n == 8) result = 5;
        else if (n == 9) result = 4;
        else if (n == 10) result = 3;
        else if (n == 11) result = 6;
        else if (n == 12) result = 6;
        else if (n == 13) result = 8;
        else if (n == 14) result = 8;
        else if (n == 15) result = 7;
        else if (n == 16) result = 7;
        else if (n == 17) result = 9;
        else if (n == 18) result = 8;
        else if (n == 19) result = 8;

        return result;
    }

    public static String belowTwentyString(String s) {
        String result = "";
        int n = Integer.parseInt(s);

        if (n == 1) result += "ONE";
        else if (n == 2) result = "TWO";
        else if (n == 3) result = "THREE";
        else if (n == 4) result = "FOUR";
        else if (n == 5) result = "FIVE";
        else if (n == 6) result = "SIX";
        else if (n == 7) result = "SEVEN";
        else if (n == 8) result = "EIGHT";
        else if (n == 9) result = "NINE";
        else if (n == 10) result = "TEN";
        else if (n == 11) result = "ELEVEN";
        else if (n == 12) result = "TWELVE";
        else if (n == 13) result = "THIRTEEN";
        else if (n == 14) result = "FOURTEEN";
        else if (n == 15) result = "FIFTEEN";
        else if (n == 16) result = "SIXTEEN";
        else if (n == 17) result = "SEVENTEEN";
        else if (n == 18) result = "EIGHTEEN";
        else if (n == 19) result = "NINETEEN";

        return result;
    }

    public static long digit(char d) {
        long result = 0;

        if (d == '1') result += 3;
        else if (d == '2') result = 3;
        else if (d == '3') result = 5;
        else if (d == '4') result = 4;
        else if (d == '5') result = 4;
        else if (d == '6') result = 3;
        else if (d == '7') result = 5;
        else if (d == '8') result = 5;
        else if (d == '9') result = 4;

        return result;
    }
}
