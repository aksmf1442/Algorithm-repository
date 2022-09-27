import java.util.ArrayList;
import java.util.Scanner;

public class GF {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            String[] input = sc.nextLine().split(" ");
            int n = Integer.parseInt(input[0]);
            int m = Integer.parseInt(input[1]);
            if (n == 0 && m == 0) {
                break;
            }
            int[] candidate = new int[10001];

            for (int i = 0; i < n;  i++) {
                String[] temp = sc.nextLine().split(" ");
                for (int j = 0; j < m; j++) {
                    int a = Integer.parseInt(temp[j]);
                    candidate[a] += 1;
                }
            }
            int maxValue = max(candidate);
            int secondValue = 0;
            for (int i = 0; i < candidate.length; i++) {
                if (candidate[i] == maxValue) {
                    continue;
                }
                secondValue = Math.max(secondValue, candidate[i]);
            }

            ArrayList result = new ArrayList();
            for (int i = 0; i < candidate.length; i++) {
                if (candidate[i] == secondValue) {
                    System.out.printf("%d ", i);
                }
            }
            System.out.println();

        }
    }

    public static int max(int[] temp) {
        int result = 0;
        for (int i =0; i < temp.length; i++) {
            result = Math.max(result, temp[i]);
        }

        return result;
    }
}
