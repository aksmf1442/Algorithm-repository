package implementation;

import java.util.Scanner;

public class Ipt1 {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int x = 0;
    int y = 0;
    int count = 0;
    while (count < n) {
      String d = sc.next();
      if (d.equals("R") && (y + 1) < n) {
        y += 1;
        count += 1;
      } else if (d.equals("L") && (y - 1) >= 0) {
        y -= 1;
        count += 1;
      } else if (d.equals("U") && (x - 1) >= 0) {
        x -= 1;
        count += 1;
      } else if (d.equals("D") && (x + 1) < n) {
        x += 1;
        count += 1;
      }
    }
    System.out.printf("%d %d\n", x + 1, y + 1);
  }

}
