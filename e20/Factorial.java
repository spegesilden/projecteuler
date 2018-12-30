import java.math.BigInteger;

public class Factorial {
    public static void main(String[] args) {
        //System.out.println(factorial(new BigInteger("100")));
        String s = factorial(new BigInteger("100")).toString();
        int result = 0;

        for (int i = 0; i < s.length(); i++) {
            result += ((int) (s.charAt(i) - '0'));
        }

        System.out.println(result);
    }

    public static BigInteger factorial(BigInteger n) {
         if (n.equals(new BigInteger("1"))) return new BigInteger("1");
         return n.multiply(factorial(n.subtract(new BigInteger("1"))));
    }
}
