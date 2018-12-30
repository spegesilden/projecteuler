public class Prime {
    public static long largest_prime_factor(long p) {
        for (long i = 2; i < p; ++i) {
            if (p % i == 0) {
                System.out.println(i + " is a factor");
                return largest_prime_factor(p / i);
            }
        }
        return p;
    }

    public static void main(String[] args) {
        long i = Long.parseLong(args[0]);
        System.out.println(largest_prime_factor(i));
    }
}
