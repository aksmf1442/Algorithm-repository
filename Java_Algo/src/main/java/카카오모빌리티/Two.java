package 카카오모빌리티;

import java.util.Arrays;

public class Two {

    public static void main(String[] args) {
        int[] T = {0, 0, 0, 0, 2, 3, 3};
        int[] A = {2, 5, 6};
        boolean[] learnedSkill = new boolean[T.length];
        Arrays.fill(learnedSkill, false);
        int count = 0;

        for (int skill : A) {
            while (!learnedSkill[skill]) {
                learnedSkill[skill] = true;
                count += 1;
                skill = T[skill];
            }
        }
        System.out.println("count = " + count);
    }
}
