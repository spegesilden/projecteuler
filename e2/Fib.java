public class Fib {
    public static void main(String[] args) {
        int result = 2;
        int fib1 = 1;
        int fib2 = 2;
        int tmp;

        while (fib2 <= 4000000) {
            tmp = fib2;
            fib2 = fib1 + fib2;
            fib1 = tmp;

            System.out.println(fib2);

            if (fib2 % 2 == 0) result += fib2;
        }

        //System.out.println(fib2);
        //result -= fib2;

        System.out.println(result);
    }
}
