package 아이포트폴리오;

import java.util.Arrays;
import java.util.List;
//1트: 효율성 문제로 실패

//1. O(n)으로 풀어야 함
//2.
public class One {

    // 1트
//    public static void main(String[] args) {
//        int answer = 0;
//        int n = 25;
//        int[] doors = new int[n];
//        Arrays.fill(doors, 1);
//        for (int i = 2; i <= n; i++) {
//            for (int j = i-1; j < n; j += i) {
//                doors[j] = doors[j] == 0 ? 1: 0;
//            }
//        }
//
//        System.out.println("doors = " + Arrays.stream(doors)
//            .reduce(Integer::sum).getAsInt());
//    }

    //2트
//    public static void main(String[] args) {
//        int n = 24;
//
//        int stop = 3;
//        int count = 0;
//        int result = 1;
//
//        for (int i = 1; i <= n; i++) {
//            if (count == stop) {
//                result += 1;
//                stop += 2;
//                count = 0;
//            }
//            count += 1;
//        }
//        System.out.println("result = " + result);
//    }

    //3트(일단 여기까지)
    public static void main(String[] args) {
        int n = 100000000;

        int plus = 3;
        int value = 1;
        int result = 0;

        while (value <= n) {
            result += 1;
            value += plus;
            plus += 2;
        }

        System.out.println("result = " + result);
    }
}
