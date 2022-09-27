package 아이포트폴리오;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

//1. NXN Board에서 물건이 놓여있지 않은 곳에는 먼지가 쌓여있음
//2. 물건이 놓인 칸은 -1, 먼지는 0이상의 정수
//3. go할 때 이동해야 할 칸이 인덱스를 벗어나거나 물건이 놓여있다면(0 이상의 정수라면) 이동하지 않고 다음 명령
//4. 한 번 방문한 칸을 또 방문 가능하지만 청소해야할 먼지는 없음
//5. 로봇 청소기는 북쪽 방향을 바라보고 시작

// 해결이 안됬던 이유는 맨 처음 로봇청소기가 있던 자리를 청소 안하고 진행해서..
public class Two {

    public static void main(String[] args) {
        int[][] office = {{5, -1, 4}, {6, 3, -1}, {2, -1, 1}};
        String[] move = {"go", "go", "right", "go", "right", "go", "left", "go"};
        int n = office.length;
        int r = 1;
        int c = 0;
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};
        int idx = 0;
        int result = 0;
        Queue<String> queue = new LinkedList<>(Arrays.asList(move));
        // 현재 칸 청소
        result += office[r][c];
        office[r][c] = 0;
        while (!queue.isEmpty()) {
            String direction = queue.poll();
            if (direction.equals("go")) {
                int nx = dx[idx] + r;
                int ny = dy[idx] + c;

                // 칸을 벗어나서 패스
                if (nx < 0 || ny < 0 || nx >= n || ny >= n) {
                    continue;
                }

                // 물건이 놓여 있을 경우 패스
                if (office[nx][ny] == -1) {
                    continue;
                }

                if (office[nx][ny] > 0) {
                    result += office[nx][ny];
                    office[nx][ny] = 0;
                }

                r = nx;
                c = ny;
            }

            if (direction.equals("right")) {
                idx = Math.abs((idx + 1) % 4);
            }

            if (direction.equals("left")) {
                idx = idx - 1 == -1 ? 3 : idx - 1;
            }
        }
        System.out.println("result = " + result);
    }
}
