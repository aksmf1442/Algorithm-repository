package 카카오모빌리티;


public class Three {

    public static void main(String[] args) {
//        int[] A = {7, -5, -5, -5, 7, -1, 7};
        int[] A = {1, 2,1,2};
        int result = 1;
        int odd = A[0];
        int even = A.length > 1 ? A[1] : 0;

        int count = 2;
        for (int i = 2; i < A.length; i++) {
            if (i % 2 == 0) {
                if (odd == A[i]) {
                    count += 1;
                    result = Math.max(result, count);
                } else {
                    count = 2;
                    odd = A[i];
                }
            }

            if (i % 2 != 0) {
                if (even == A[i]) {
                    count += 1;
                    result = Math.max(result, count);
                } else {
                    count = 2;
                    even = A[i];
                }
            }
        }

        System.out.println("result = " + result);
    }

}
