public class Pal {
    public static void main(String[] args) {
        //int a = 99;
        //int b = 99;
        int maximum = 0;

        for (int a = 100; a < 1000; a++) {
            for (int b = 100; b < 1000; b++) {
                int p = a*b;
                if (isPal(p) && maximum <= p) {
                    maximum = p;
                    System.out.println(p + " " + isPal(p));
                }
            }
        }

        System.out.println(maximum);
    }

    public static boolean isPal(int n) {
        String a = Integer.toString(n);

        for (int i  = 0; i <= (a.length()/2); i++) {
            if (a.charAt(i) != a.charAt(a.length() - i - 1)) return false;
        }
        return true;
    }
}
