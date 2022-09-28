package 구현;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;

/**
 * goal: n, m의 값들을 모두 똑같이 하기
 * 가능한 작업은 아래와 같음
 * 1. 가장 위에 있는 블록을 제거하여 인벤에 넣기 - 소요 시간 2초
 * 2. 인벤토리에서 블록 하나를 꺼내어 i, j의 가장 위에 있는 블록 위에 놓기 - 소요 시간 1초
 * 단, -1값을 존재할 수가 없고, 땅의 높이는 256을 초과할 수 없다. 또한 시작할 떄 인벤토리에 B개의 블록이 들어있다.
 */

/**
 * 풀이 방법
 * 1. 그대로 두기, 1번 사용, 2번 사용 3가지 중 하나를 dfs로 선택해서 해보면 될듯.
 * 2. 그러면 시간복잡도는 어떻게 될지 생각해보면? -> 3 * 25000(500 * 500) * 500 = 3750000 -> 가능
 */
public class MainCraft {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] nmb = br.readLine().split(" ");
        int n = Integer.parseInt(nmb[0]);
        int m = Integer.parseInt(nmb[1]);
        int b = Integer.parseInt(nmb[2]);

        int[][] ground = new int[n][m];

        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int i = 0; i < ground.length; i++) {

            String[] groundRow = br.readLine().split(" ");

            for (int j = 0; j < m; j++) {
                int value = Integer.parseInt(groundRow[j]);
                ground[i][j] = value;

                max = Math.max(max, value);
                min = Math.min(min, value);
            }
        }

        int answerSeconds = Integer.MAX_VALUE; // 시간
        int answerHeight = -1; // 층

        for (int i = min; i <= max; i++) { // 최소층 부터 최대층 까지

            int seconds = 0;
            int inventory = b;

            for (int j = 0; j < ground.length; j++) {
                for (int k = 0; k < ground[j].length; k++) {
                    int diff = ground[j][k] - i;

                    if(diff > 0) { // 제거해야 함
                        seconds += Math.abs(diff) * 2;
                        inventory += Math.abs(diff);
                    }else if(diff < 0){ // 추가해야 함
                        seconds += Math.abs(diff);
                        inventory -= Math.abs(diff);
                    }
                }
            }

            if(inventory >= 0) {
                if(seconds <= answerSeconds) { // == 가 포함되어야 함 ㅇ그렇지 않으면 최대 높이를 판별 하지 못함
                    answerSeconds = seconds;
                    answerHeight = i;
                }
            }
        }

        bw.write(answerSeconds + " " + answerHeight);
        bw.flush();

        bw.close();
    }
}
