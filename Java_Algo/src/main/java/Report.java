import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

// 신고 결과 받기
public class Report {
    public static HashMap<String, HashSet<String>> reportUser = new HashMap<>();
    public static HashMap<String, HashSet<String>> reportedUser = new HashMap<>();

    public static void main(String[] args) {
        String[] id_list = {"muzi", "frodo", "apeach", "neo"};
        String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
        int k = 2;

        System.out.println(solution(id_list, report, k));
    }

    public static int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        for (int i = 0; i < report.length; i++) {
            String[] user = report[i].split(" ");
            String reportUser = user[0];
            String reportedUser = user[1];
            reportUser(reportUser, reportedUser);
        }

        ArrayList<String> bannedUsers = getBannedUser(id_list, k);

        for (int i = 0; i < id_list.length; i++) {
            String user = id_list[i];
            if (Report.reportUser.get(user) == null) {
                continue;
            }
            for (String reportedUser: Report.reportUser.get(user)) {
                if (bannedUsers.contains(reportedUser)) {
                    answer[i] += 1;
                }
            }
        }

        return answer;
    }

    private static ArrayList<String> getBannedUser(String[] id_list, int k) {
        ArrayList<String> result = new ArrayList<>();
        for (String user : id_list) {
            int size = Report.reportedUser.get(user) == null ? 0 : Report.reportedUser.get(user).size() ;
            if (size >= k) {
                result.add(user);
            }
        }

        return result;
    }

    // 유저 신고하기
    public static void reportUser(String reportingUser, String reportedUser) {
        HashSet<String> reportedUsers = Report.reportUser.get(reportingUser);
        if (reportedUsers == null) {
            reportedUsers = new HashSet<>();
        }
        reportedUsers.add(reportedUser);
        Report.reportUser.put(reportingUser, reportedUsers);
        HashSet<String> reportingUsers = Report.reportedUser.get(reportedUser);
        if (reportingUsers == null) {
            reportingUsers = new HashSet<>();
        }
        reportingUsers.add(reportingUser);
        Report.reportedUser.put(reportedUser, reportingUsers);
    }
}
