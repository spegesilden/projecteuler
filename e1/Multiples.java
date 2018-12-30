public class Multiples {
    public static void main(String[] args) {
        int result = 0;

        for (int i = 1; i < 1000; i++) {
            if (isMultiple(i)) {
                result += i;
            }
        }

        System.out.println(result);
    }
    
    public static boolean isMultiple(int n) {
        if (n % 3 == 0 || n % 5 == 0) return true;
        return false;
    }
}
