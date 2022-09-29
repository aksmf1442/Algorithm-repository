package 구현;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

/**
 * goal: 참외의 총 개수 구하기
 * 1. 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
 * 2. 30
 */
public class 참외밭 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int k = Integer.parseInt(br.readLine());

        int maxX = Integer.MIN_VALUE;
        int maxY = Integer.MIN_VALUE;
        int x = 0;
        int y = 0;

        int[] dist = new int[6];

        for (int i = 0; i < 6; i++) {
            String[] value = br.readLine().split(" ");
            dist[i] = Integer.parseInt(value[1]);
            if (value[0].equals("1") || value[0].equals("2")) {
                if (maxX < dist[i]) {
                    maxX = dist[i];
                    x = i;
                }
            } else {
                if (maxY < dist[i]) {
                    maxY = dist[i];
                    y = i;
                }
            }
        }

        int square = maxX * maxY;
        int ms = dist[(y + 3) % 6] * dist[(x + 3) % 6];

        bw.write(String.valueOf((square - ms) * k));
        bw.flush();

        bw.close();
    }
}
