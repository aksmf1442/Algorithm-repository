package 연습;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.stream.Collectors;

public class 완주하지못한선수 {
    static int result = 0;

    public static void main(String[] args) {
        int[] numbers = {1, 1, 1, 1, 1};
        int target = 3;
        dfs(new ArrayList<String>(), numbers.length, numbers, target);
    }

    private static void dfs(ArrayList<String> strings, int length, int[] numbers, int target) {
        if (strings.size() == length) {
            if (calculate(numbers, strings) == target) {
                result += 1;
            }
            return;
        }

        strings.add("+");
        dfs(new ArrayList<>(strings), length, numbers, target);
        strings.remove(strings.size() - 1);

        strings.add("-");
        dfs(new ArrayList<>(strings), length, numbers, target);
        strings.remove(strings.size() - 1);
    }

    private static int calculate(int[] numbers, ArrayList<String> strings) {
        int result = 0;
        for (int i : numbers) {
            String type = strings.remove(0);
            if (type.equals("+")) {
                result += i;
            }

            if (type.equals("-")) {
                result -= i;
            }
        }
        return result;
    }


}
