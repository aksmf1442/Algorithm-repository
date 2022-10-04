package 백준레벨별알고리즘.실버4;

import java.util.List;
import java.util.Scanner;

/**
 * goal: N이 주어졌을 때 1보다 크거나 같고, N보다 작거나 같은 한수(등차수열 이루는 수)의 개수 구하기
 */
public class 한수 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int result = n < 10 ? n : 9;

        for (int i = 10; i <= n; i++) {
            String[] st = String.valueOf(i).split("");
            int distance = Integer.parseInt(st[1]) - Integer.parseInt(st[0]);
            boolean check = true;

            for (int j = 2; j < st.length; j++) {
                int value = Integer.parseInt(st[j]) - Integer.parseInt(st[j - 1]);
                if (value != distance) {
                    check = false;
                    break;
                }
            }
            if (check) {
                result += 1;
            }
        }
        System.out.println(result);
    }
}
