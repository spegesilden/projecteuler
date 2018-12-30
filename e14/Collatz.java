public class Collatz {
    public static void main(String[] args) {
        int maxCol = 0;

        //int n = 1;
        //long col = 4;

        //while (col != 1) {
        //    col = collatz(col);
        //    System.out.print(" " + col);
        //    n++;
        //}
        //System.out.print("\n");
        //System.out.println(n);

        for (long i = 2; i <= 1000000; i++) {
            int n = 1;

            long col = i;

            while (col != 1) {
                col = collatz(col);
                //System.out.print(" " + col);
                n++;
            }
            //System.out.print("\n");
            
            if (maxCol < n) {
                System.out.println(i + " " + n);
            }

            maxCol = Math.max(n, maxCol);

            //System.out.println(i + " " + maxCol);
        }

        System.out.println(maxCol);
    }

    public static long collatz(long n) {
        if (n % 2 == 0) return n/2;
        return 3*n+1;
    }
}
