package p1;

/**
 * Created by kuldeed on 10/21/16.
 */
public class Problem1 {
    public static void main(String[] args) {
        System.out.println("answer = " + ans(1000));
    }

    public static int ans(int n) {

        n--;
        int total = 0;

        float a1 = 3;
        int n1 = (int) (n/a1);
        System.out.println("n1 = " + n1);
        float s1 = n1 * (a1 + (n1-1)*(a1/2));
        System.out.println("3s = " + s1);

        float a2 = 5;
        int n2 = (int)(n/a2);
        System.out.println("n2 = " + n2);
        float s2 = n2 * (a2 + (n2-1)*(a2/2));
        System.out.println("5s = " + s2);

        float a3 = 15;
        int n3 = (int)(n/a3);
        System.out.println("n3 = " + n3);
        float s3 = n3 * (a3 + (n3-1)*(a3/2));
        System.out.println("15s = " + s3);

        return (int)(s1 + s2 - s3);
    }
}
