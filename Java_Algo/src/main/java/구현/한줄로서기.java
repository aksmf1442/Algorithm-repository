package 구현;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * goal: 줄을 어떻게 서야하는지 출력 조건 1. 사람들은 자기보다 큰 사람이 왼쪽에 몇 명인지만 기억함 2. idx+1이 키라고 생각하면 된다.
 */

/**
 * 풀이 순서 1. 키가 큰 순서대로 뽑아서 값을 넣은 list안의 키를 자신의 앞에 키 큰 사람의 수를 비교하고 add
 */
public class 한줄로서기 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        String[] waitPeople = br.readLine().split(" ");

        List<String> lst = new ArrayList<>();

        for (int i = waitPeople.length - 1; i >= 0; i--) {
            int man = Integer.parseInt(waitPeople[i]);
            int currentHeight = i + 1;

            if (man == 0) {
                lst.add(0, String.valueOf(currentHeight));
                continue;
            }

            for (int j = 0; j < lst.size(); j++) {
                int height = Integer.parseInt(lst.get(j));
                if (height > currentHeight) {
                    man -= 1;
                }

                if (man == 0) {
                    lst.add(j + 1, String.valueOf(currentHeight));
                    break;
                }
            }

            if (man > 0) {
                lst.add(String.valueOf(currentHeight));
            }
        }
        bw.write(String.join(" ", lst));
        bw.flush();

        bw.close();
    }
}
