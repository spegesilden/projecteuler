import java.util.*;

public class Smallest {
    public static void main(String[] args) {
        List<Integer> primes = new ArrayList<>();
        int a = 1;

        for (int i = 0; i <= 20; i++) {
            if (isPrime(i)) primes.add(i);
        }

        for (Integer p: primes) {
            int maxmult = 0;

            for (int i = 2; i <= 20; i++) {
                int m = mult(i,p);

                if (m > maxmult) maxmult = m;
            }

            a = a * exp(p,maxmult);
        }

        System.out.println(a);
    }

    public static int mult(int n, int m) {
        int i = 0;

        while (n % m == 0) {
            //System.out.println(n);
            i++;
            n = n/m;
        }
        
        return i;
    }

    public static int exp(int n, int m) {
        int result = 1;

        for (int i = 0; i < m; i++) {
            result = result * n;
        }

        return result;
    }

    public static boolean isPrime(int n) {
        if(n < 2) {
            return false;
        }

        for(int i = 2; i < n; i++) {
            if(n % i == 0) {
                return false;
            }
        }

        return true;
    }
}
