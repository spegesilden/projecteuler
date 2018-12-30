import java.util.*;

public class Primes {
    public static void main(String[] args) {
        List<Integer> primes = new ArrayList<>();

        for (int n = 1; n <= 2000000; n++) {
            //if (isPrime(n, primes)) primes.add(n);
            if (isPrime(n)) primes.add(n);
        }

        long sum = 0;

        for (Integer p: primes) {
            //System.out.println(p);
            sum += p;
        }

        System.out.println(primes.size() + " " + sum);
    }

    public static boolean isPrime(int n, List<Integer> primes) {
        if (n < 2) return false;

        for (Integer p: primes) {
            if (n % p == 0) return false;
        }

        return true;
    }

    public static boolean isPrime(int n) {
        if (n < 2) return false;

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }

        return true;
    }
}
