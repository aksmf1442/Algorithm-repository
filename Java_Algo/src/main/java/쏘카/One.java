package 쏘카;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class One {

    public static void main(String[] args) {
        int n = 5;
        int k = 4;
        int[][] paths = new int[][]{{1, 5, 1, 1}, {1, 2, 4, 3}, {1, 3, 3, 2}, {2, 5, 2, 1},
            {2, 4, 2, 3}, {3, 4, 2, 2}};

        int[] distance = new int[n];
        int[] bonus = new int[n];
        distance[0] = 0;
        bonus[0] = 0;

        for (int i = 0; i < n; i++) {
            distance[i] = (int) Double.POSITIVE_INFINITY;
        }

        PriorityQueue<Node> queue = new PriorityQueue<>((a, b) -> a.distance - b.distance);
        queue.add(new Node(0, 0, 0));

        List<ArrayList<Node>> vertexs = new ArrayList<>();

        for (int i =0; i < n; i++) {
            vertexs.add(new ArrayList<>());
        }

        for (int[] path : paths) {
            vertexs.get(path[0] - 1).add(new Node(path[2], path[3], path[1] - 1));
            vertexs.get(path[1] - 1).add(new Node(path[2], path[3], path[0] - 1));
        }

        while (queue.size() != 0) {
            Node node = queue.poll();
            if (node.distance > distance[node.node]) {
                continue;
            }

            for (Node v : vertexs.get(node.node)) {
                if (node.distance + v.distance > distance[v.node]) {
                    continue;
                }

                if (node.distance + v.distance == distance[v.node] && node.bonus + v.bonus <= bonus[v.node]) {
                    continue;
                }

                distance[v.node] = node.distance + v.distance;
                bonus[v.node] = node.bonus +  v.bonus;
                queue.add(new Node(distance[v.node], bonus[v.node], v.node));
            }
        }

        System.out.println("distance = " + distance[k-1]);
        System.out.println("bonus = " + bonus[k-1]);

    }
}

class Node {

    int distance;
    int bonus;
    int node;

    Node(int distance, int bonus, int node) {
        this.distance = distance;
        this.bonus = bonus;
        this.node = node;
    }

}
