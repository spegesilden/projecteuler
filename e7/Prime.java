import java.util.*;

public class Prime {
    public static void main(String[] args) {
        List<Integer> primes = new ArrayList<>();
        int i = 1;

        while (primes.size() <= 10000) {
            i++;
            if (isPrime(i)) primes.add(i);
        }

        System.out.println(primes.size() + " " + primes.get(primes.size()-1));
    }

    public static boolean isPrime(int n) {
        if(n < 2) {
            return false;
        }

        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }

        return true;
    }
}
