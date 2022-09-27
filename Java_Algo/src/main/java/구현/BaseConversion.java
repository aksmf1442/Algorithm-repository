package 구현;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class BaseConversion {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int num = sc.nextInt();

        int candidate = 0;
        for (int i = num - 1; i >= 0; i--) {
            int value = sc.nextInt();
            candidate += i == 0 ? value : Math.pow(a, i) * value;
        }

        List<Integer> lst = new ArrayList<>();
        while (candidate / b != 0) {
            int value = candidate % b;
            candidate = candidate / b;
            lst.add(value);
        }

        lst.add(candidate);

        while (!lst.isEmpty()) {
            System.out.print(lst.remove(lst.size() - 1) + " ");
        }
    }
}
