public class Triplet {
    public static void main(String[] args) {
        //int a = 0;
        //int b = 0;
        double product = 1;
        boolean condition = true;

        for (int a = 1; a < 1000 && condition; a++) {
            for (int b = 1; b < 1000 && condition; b++) {
                double c = Math.sqrt(a*a + b*b);

                if ((a + b + c) == 1000) {
                    product = ((double)a)*((double)b)*c;
                    System.out.println(a + " " + b + " " + c);
                    condition = false;
                }
            }
        }

        System.out.println(product);
    }
}
