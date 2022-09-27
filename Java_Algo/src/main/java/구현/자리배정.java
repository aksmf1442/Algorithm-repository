package 구현;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class 자리배정 {

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int C = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());
        int TOTAL = C * R;

        int num = Integer.parseInt(br.readLine());

        if (num > TOTAL) {
            System.out.println(0);
            return;
        }

        int[][] arr = new int[C][R];
        int[] dx = new int[]{0, 1, 0, -1};
        int[] dy = new int[]{1, 0, -1, 0};
        int idx = 0;
        int value = 1;
        arr[0][0] = value++;
        int x = 0, y = 0;

        int[] result = new int[2];
        while (value <= TOTAL) {
            int nx = x + dx[idx];
            int ny = y + dy[idx];

            if (nx >= C || ny >= R || nx < 0 || ny < 0 || arr[nx][ny] != 0) {
                idx = (idx + 1) % 4;
                continue;
            }

            arr[nx][ny] = value;

            if (value == num) {
                result[0] = nx + 1;
                result[1] = ny + 1;
                break;
            }

            value++;
            x = nx;
            y = ny;
        }

        if (result[0] == 0 && result[1] == 0) {
            result[0] +=1;
            result[1] +=1;
        }

        bw.write(result[0] + " " + result[1]);
        bw.flush();
        br.close();
        bw.close();
    }
}
