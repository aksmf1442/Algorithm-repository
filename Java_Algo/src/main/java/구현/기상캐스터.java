package 구현;

import java.util.Scanner;

public class 기상캐스터 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int H = sc.nextInt();
        int W = sc.nextInt();

        char[][] city = new char[H][W];
        int[][] times = new int[H][W];

        for (int i = 0; i < H; i++) {
            String str = sc.next();
            for (int j = 0; j < W; j++) {
                city[i][j] = str.charAt(j);
                times[i][j] = -1;
            }
        }

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (city[i][j] == 'c') {
                    times[i][j] = 0;
                } else {
                    if (j-1 >= 0 && times[i][j-1] != -1) {
                        times[i][j] = times[i][j-1] + 1;
                    }
                }
            }
        }

        for (int[] lst : times) {
            for (int i : lst) {
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }
}
