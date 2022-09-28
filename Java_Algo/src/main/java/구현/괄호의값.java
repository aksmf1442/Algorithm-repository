package 구현;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

/**
 * goal: 주어진 기준에 따른 값 구하기 풀이방법 1. '('가 오면 sg에 +1을 하고, '['가 오면 bg에 +1을 한다. 2. ']'가 왔을 때
 */
public class 괄호의값 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Stack<String> stack = new Stack<>();
        int ans = 0;
        int tmp = 1;
        String[] arr = br.readLine().split("");
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals("(")) {
                stack.push(arr[i]);
                tmp *= 2;
            }

            if (arr[i].equals("[")) {
                stack.push(arr[i]);
                tmp *= 3;
            }

            if (arr[i].equals(")")) {
                if (stack.empty() || stack.peek().equals("[")) {
                    ans = 0;
                    break;
                }
                if (arr[i - 1].equals("(")) {
                    ans += tmp;
                }
                stack.pop();
                tmp /= 2;
            }

            if (arr[i].equals("]")) {
                if (stack.empty() || stack.peek().equals("(")) {
                    ans = 0;
                    break;
                }

                if (arr[i - 1].equals("[")) {
                    ans += tmp;
                }
                stack.pop();
                tmp /= 3;
            }
        }
        if (stack.empty()) {
            bw.write(String.valueOf(ans));
        } else {
            bw.write("0");
        }
        bw.flush();

        bw.close();
    }
}
