package 쏘카;

import java.util.LinkedList;
import java.util.Queue;

public class Two {

    public static void main(String[] args) {
//        String[][] map3d = new String[][]{{"XXXXX", "OOSXO", "OOXOO"}, {"XEOOO", "OXXXO", "OOOOX"}};
        String[][] map3d = new String[][]{{"SXE"}};
        Location start = null;
        Location end = null;
        int X = map3d.length;
        int Z = map3d[0].length;
        int Y = map3d[0][0].length();
        int[][][] distance = new int[X][Z][Y];

        for (int i = 0; i < X; i++) {
            for (int j = 0; j < Z; j++) {
                for (int k = 0; k < Y; k++) {
                    if (map3d[i][j].charAt(k) == 'S') {
                        start = new Location(i, k, j);
                        distance[i][j][k] = 0;
                        continue;
                    }

                    if (map3d[i][j].charAt(k) == 'E') {
                        end = new Location(i, k, j);
                    }

                    distance[i][j][k] = -1;
                }
            }
        }

        int result = bfs(distance, map3d, start, end);

        for (int i = 0; i < X; i++) {
            for (int j = 0; j < Z; j++) {
                for (int k = 0; k < Y; k++) {
                    System.out.print(distance[i][j][k] + " ");
                }
                System.out.println();
            }
        }

        System.out.println("result = " + result);
    }

    private static int bfs(int[][][] distance, String[][] map3d, Location start, Location end) {
        int[] dx = {1, -1, 0, 0, 0, 0};
        int[] dy = {0, 0, 1, -1, 0, 0};
        int[] dz = {0, 0, 0, 0, 1, -1};
        Queue<Location> queue = new LinkedList<>();
        queue.add(start);
        boolean isEnd = false;

        while (queue.size() != 0) {
            Location node = queue.poll();
            for (int i = 0; i < 6; i++) {
                int nx = node.x + dx[i];
                int nz = node.z + dz[i];
                int ny = node.y + dy[i];

                if (nx < 0 || ny < 0 || nz < 0 || nx >= distance.length
                    || ny >= distance[0][0].length || nz >= distance[0].length) {
                    continue;
                }

                if (distance[nx][nz][ny] != -1) {
                    continue;
                }

                if (isX(nx, ny, nz, map3d)) {
                    continue;
                }

                distance[nx][nz][ny] = distance[node.x][node.z][node.y] + 1;
                queue.add(new Location(nx, ny, nz));

                if (map3d[nx][nz].charAt(ny) == 'E') {
                    isEnd = true;
                    break;
                }
            }
            if (isEnd) {
                break;
            }
        }

        return distance[end.x][end.z][end.y];
    }

    private static boolean isX(int nx, int ny, int nz, String[][] map3d) {
        if (map3d[nx][nz].charAt(ny) == 'X') {
            return true;
        }
        return false;
    }
}

class Location {
    int x;
    int y;
    int z;

    public Location(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }
}
