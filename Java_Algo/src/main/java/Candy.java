import java.util.Scanner;

public class Candy {
    static int result = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < t; i++) {
            oneCycle(sc);
            System.out.println(result);
            result = 0;
        }

    }

    private static void oneCycle(Scanner sc) {
        int n = Integer.parseInt(sc.nextLine());
        String[] candidate = sc.nextLine().split(" ");
        int[] c = new int[candidate.length];
        for (int j = 0; j < n; j++) {
            c[j] = Integer.parseInt(candidate[j]);
        }
        addCandy(n, c);
        if (validateCandy(n, c)) {
            return;
        }
        lotateCandy(n, c);
    }

    private static void lotateCandy(int n, int[] c) {
        for (int i = 0; i < n; i++) {
            c[i] = c[i] / 2;
        }

        int[] temp = c.clone();
        for (int i = 0; i < n - 1; i++) {
            if (i == 0) {
                temp[i] += c[n-1];
            }
            temp[i+1] += c[i];
        }

        c = temp;
        addCandy(n, c);


        if (!validateCandy(n, c)) {
            lotateCandy(n, c);
        }
        result += 1;
    }

    private static void addCandy(int n, int[] c) {
        for (int i = 0; i < n; i++) {
            if (c[i] % 2 == 1) {
                c[i] += 1;
            }
        }
    }

    private static boolean validateCandy(int n, int[] c) {
        int num = c[0];
        boolean check = true;
        for (int i = 0; i < n; i++) {
            if (num != c[i]) {
                check = false;
                break;
            }
        }

        return check;
    }


}
