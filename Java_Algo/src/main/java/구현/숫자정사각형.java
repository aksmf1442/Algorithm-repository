package 구현;

import java.util.Scanner;

public class 숫자정사각형 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        final int MIN = Math.min(n, m);
        int[][] arr = new int[n][m];
        int maxArea = 0;

        for (int i = 0; i < n; i++) {
            String str = sc.next();
            for (int j = 0; j < m; j++) {
                arr[i][j] = str.charAt(j);
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < MIN; k++) {
                    if (i + k < n && j + k < m) {
                        if (arr[i][j] == arr[i][j + k] && arr[i][j] == arr[i + k][j]
                            && arr[i][j] == arr[i + k][j + k]) {
                            maxArea = Math.max(maxArea, (k + 1) * (k + 1));
                        }
                    }
                }
            }
        }
        System.out.println(maxArea);
    }
}
