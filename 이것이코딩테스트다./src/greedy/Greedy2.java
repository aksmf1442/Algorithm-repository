package greedy;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Greedy2 {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int m = scanner.nextInt();
    int k = scanner.nextInt();
    Integer[] data = new Integer[n];
    for (int i = 0; i < n; i++) {
      data[i] = scanner.nextInt();
    }
    Arrays.sort(data, Collections.reverseOrder());
    // 가장 큰 수가 더해지는 횟수 계산
    int cnt = (m / (k + 1)) * k;
    cnt += m % (k + 1);

    int answer = 0;
    answer += cnt * data[0];
    answer += (m - cnt) * data[1];
    System.out.println(answer);
  }
}
