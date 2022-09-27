package 구현;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 점프왕젤리 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        int[][] board = new int[n][n];
        boolean[][] visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = sc.nextInt();
                visited[i][j] = false;
            }
        }

        bfs(board, visited);
    }

    private static void bfs(int[][] board, boolean[][] visited) {
        int len = board.length;
        boolean success = false;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0});

        while (!q.isEmpty()) {
            int[] focus = q.poll();
            int r = focus[0], c = focus[1];
            visited[r][c] = true;

            if (board[r][c] == -1) {
                success = true;
                break;
            }

            int bottom = r + board[r][c], right = c + board[r][c];

            if (bottom < len && !visited[bottom][c]) {
                q.add(new int[]{r + board[r][c], c});
                visited[bottom][c] = true;
            }

            if (right < len && !visited[r][right]) {
                q.add(new int[]{r, c + board[r][c]});
                visited[r][right] = true;
            }
        }

        if (success) {
            System.out.println("HaruHaru");
        } else {
            System.out.println("Hing");
        }
    }
}
