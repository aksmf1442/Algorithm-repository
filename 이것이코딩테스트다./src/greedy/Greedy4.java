package greedy;

import java.util.Scanner;

public class Greedy4 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = sc.nextInt();
    int answer = 0;
    while (n > 1) {
      answer += 1;
      answer += (n % k);
      n /= k;
    }
    System.out.println(answer);
  }
}
