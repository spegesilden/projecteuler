import java.math.BigInteger;

public class Power {
    public static void main(String[] args) {
        BigInteger b = BigInteger.valueOf(2).pow(1000);
        String number = b.toString();
        int result = 0;

        for (int i = 0; i < number.length(); i++) {
            result += (int) (number.charAt(i) - '0');
        }

        System.out.println(result);
    }
}
