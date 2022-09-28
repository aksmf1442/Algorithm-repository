package 구현;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;

/**
 * goal: 트럭이 다리를 건너는 최단시간을 출력
 */
public class 트럭 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputValue = br.readLine().split(" ");
        int n = Integer.parseInt(inputValue[0]); // 트럭의 수
        int w = Integer.parseInt(inputValue[1]); // 다리의 길이
        int l = Integer.parseInt(inputValue[2]); // 다리의 최대 하중

        Queue<Integer> bridge = new LinkedList<>();

        for (int i = 0; i < w; i++) {
            bridge.add(0);
        }

        String[] arr = br.readLine().split(" ");
        Queue<Integer> trucks = new LinkedList<>();
        int result = 0;

        for (int i = 0; i < arr.length; i++) {
            trucks.add(Integer.valueOf(arr[i]));
        }

        while (bridge.size() != 0) {
            result += 1;
            bridge.poll();
            if (trucks.size() != 0) {
                Integer truck = trucks.peek();
                if (validateBridge(bridge, truck, l)) {
                    bridge.add(trucks.poll());
                } else {
                    bridge.add(0);
                }
            }
        }

        bw.write(String.valueOf(result));
        bw.flush();

        bw.close();
    }

    private static boolean validateBridge(Queue<Integer> bridge, int truck, int l) {
        Integer hap = bridge.stream().reduce((a, b) -> a + b)
            .get();
        if (hap + truck > l) {
            return false;
        }
        return true;
    }
}
