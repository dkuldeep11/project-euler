package p2;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by kuldeed on 10/21/16.
 */
public class Problem2 {

    public static void main(String[] args) {
        System.out.println("anwser = " + ans(4000000));
    }

    public static Integer ans(int n) {

        Integer ans = 2;
        /*
        following chunk is fibonacci DP
         */
        List<Integer> seq = new ArrayList<Integer>();
        seq.add(0);
        seq.add(1);
        seq.add(2);

        int i = 3;

        while(true) {

            int a = seq.get(i-1) + seq.get(i-2);
            System.out.println(i + " = " + a);

            if (a > n) {
                break;
            }

            seq.add(a);
            i++;

            if (a%2 == 0) {
                ans += a;
            }
        }

        System.out.println("seq - " + seq);
        return ans;
    }
}
