import java.util.*;

public class Triangular {
    public static void main(String[] args) {
        int n = 0;
        int i = 1;
        boolean condition = true;

        while (condition) {
            n += i;
            int div1;
            int div2;

            if (i % 2 == 0) {
                div1 = numberOfDivisors((i/2));
                div2 = numberOfDivisors(i+1);
            }
            else {
                div1 = numberOfDivisors(i);
                div2 = numberOfDivisors((i+1)/2);
            }

            System.out.println(n + ": " + (div1*div2));

            if ((div1*div2) >= 500) condition = false;


            i++;
        }

        System.out.println(n);
    }

    public static int numberOfDivisors(int n) {
        List<Integer> primes = new ArrayList<>();
        List<Integer> divisors = new ArrayList<>();
        int result = 1;

        for (int i = 1; i <= n; i++) {
            if (isPrime(i, primes)) {
                primes.add(i);
                if (n % i == 0) divisors.add(i);
            }
        }

        for (Integer p: divisors) {
            result *= (mult(n,p)+1);
        }

        return result;
    }

    public static int mult(int n, int m) {
        int i = 0;

        while (n % m == 0) {
            i++;
            n = n/m;
        }
        
        return i;
    }

    public static boolean isPrime(int n, List<Integer> primes) {
        if (n < 2) return false;

        for (Integer p: primes) {
            if (n % p == 0) return false;
        }

        return true;
    }
}
