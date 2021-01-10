package greedy;

import java.util.Scanner;

public class Greedy3 {

  public static void main(String[] args) {
    int answer = 0;
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();
    for(int i = 0; i < n; i++){
      int tmp = 10001;
      for (int j = 0; j < m; j++){
        tmp = Math.min(tmp, sc.nextInt());
      }
      answer = Math.max(answer, tmp);
    }
    System.out.println(answer);
  }
}
