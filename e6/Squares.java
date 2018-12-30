public class Squares {
    public static void main(String[] args) {
        int sum = 50*101*50*101;
        int squareSum = 0;

        for (int i = 1; i <= 100; i++) {
            squareSum += i*i;
        }

        System.out.println((squareSum));
        System.out.println((sum));
        System.out.println((sum-squareSum));
    }
}
