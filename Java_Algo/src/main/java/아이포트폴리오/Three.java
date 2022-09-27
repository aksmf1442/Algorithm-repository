package 아이포트폴리오;

import java.util.Arrays;
import java.util.List;

//1 : 1, 2: 2, 3: 3, 4:1, 5: 2, 6:
public class Three {

    public static void main(String[] args) {
        int n = 15;
        int[] arr = new int[100001];
        Arrays.fill(arr, 0);
        int idx = 2;
        while (Math.pow(idx, 2) <= 100000) {
            int value = (int) Math.pow(idx, 2);
            arr[value] = 1;
            int count = 2;
            for (int i = value * 2; i <= 100000; i += value) {
                if (arr[i] != 0) {
                    arr[i] = Math.min(arr[i], count + 1);
                } else {
                    arr[i] = count + 1;
                }
                count++;
            }
            idx += 1;
        }


    }
}
