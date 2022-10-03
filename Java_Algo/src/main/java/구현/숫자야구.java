package 구현;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * goal: 정답의 경우의 수 구하기 풀이 순서
 * 1. 숫자 야구에서 나올 수 있는 모든 경우의 수를 구하기
 * 2. 불가능한 숫자 제거(입력 받은 값의 s, b의 개수가 같지 않을
 * 경우 제거)
 */


public class 숫자야구 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        List<BaseBall> inputData = inputDataForBaseBallGame(n, br);

        bw.write(String.valueOf(playBaseBall(inputData)));
        bw.flush();

        bw.close();
    }

    private static int playBaseBall(List<BaseBall> inputData) {
        int result = 0;
        for (int num = 123; num <= 987; num++) {
            if (hasZeroOrSameNum(num)) {
                continue;
            }

            int casePassCount = 0;

            for (BaseBall target : inputData) {
                BaseBall baseBall = BaseBall.createBaseBallWithNum(num);
                baseBall.countStrikeAndBall(target);
                if (baseBall.strike == target.strike && baseBall.ball == target.ball) {
                    casePassCount++;
                }
            }

            if (casePassCount == inputData.size()) {
                result++;
            }
        }
        return result;
    }

    private static boolean hasZeroOrSameNum(int num) {
        String sNumber = String.valueOf(num);
        Set<Character> chars = new HashSet<>();
        for (int i = 0; i < sNumber.length(); i++) {
            chars.add(sNumber.charAt(i));
        }

        return chars.contains('0') || chars.size() != 3;
    }

    private static List<BaseBall> inputDataForBaseBallGame(int n, BufferedReader br)
        throws IOException {
        List<BaseBall> inputData = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            int s = Integer.parseInt(input[1]);
            int b = Integer.parseInt(input[2]);
            String answer = input[0];
            inputData.add(new BaseBall(answer, s, b));
        }
        return inputData;
    }

}

class BaseBall {

    String answer;
    int strike;
    int ball;

    public BaseBall(String answer, int strike, int ball) {
        this.answer = answer;
        this.strike = strike;
        this.ball = ball;
    }

    public static BaseBall createBaseBallWithNum(int num) {
        return new BaseBall(String.valueOf(num), 0, 0);
    }

    public void countStrikeAndBall(BaseBall target) {
        countStrike(target);
        countBall(target);
    }

    private void countBall(BaseBall target) {
        for (int i = 0; i < 3; i++) {
            if (this.answer.charAt(i) == target.answer.charAt((i + 1) % 3)
                || this.answer.charAt(i) == target.answer.charAt((i + 2) % 3)) {
                this.ball++;
            }
        }
    }

    private void countStrike(BaseBall target) {
        for (int i = 0; i < 3; i++) {
            if (target.answer.charAt(i) == this.answer.charAt(i)) {
                this.strike++;
            }
        }
    }
}
