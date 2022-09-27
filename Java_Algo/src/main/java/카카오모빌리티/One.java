package 카카오모빌리티;

public class One {

    public static void main(String[] args) {
//        String S = "John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker";
        String S = "John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker";
        String C = "Example";

        String[] names = S.split(", ");
        StringBuilder result = new StringBuilder();
        for (String name : names) {
            String[] splitName = name.split(" ");
            result.append(name);
            result.append(" ");
            if (splitName.length == 3) {
                String firstName = String.valueOf(splitName[0].charAt(0));
                String middleName = String.valueOf(splitName[1].charAt(0));
                String lastName =
                    splitName[2].contains("-") ? splitName[2].replace("-", "") : splitName[2];

                if (lastName.length() > 8) {
                    lastName = lastName.substring(0, 8);
                }

                String emailName = (firstName + middleName + lastName).toLowerCase();
                emailName = validateEmailName(emailName, result);
                String email = createEmail(emailName, C).toLowerCase();
                result.append(email);
                continue;
            }

            String firstName = String.valueOf(splitName[0].charAt(0));
            String lastName =
                splitName[1].contains("-") ? splitName[1].replace("-", "") : splitName[1];

            if (lastName.length() > 8) {
                lastName = lastName.substring(0, 8);
            }

            String emailName = (firstName + lastName).toLowerCase();
            emailName = validateEmailName(emailName, result);
            String email = createEmail(emailName, C).toLowerCase();
            result.append(email);
        }
        System.out.println("result.substring(0, result.length() - 2) = " + result.substring(0,
            result.length() - 2));
    }

    private static String validateEmailName(String email, StringBuilder result) {
        System.out.println("email = " + email);
        int emailCount = result.toString().split(email).length;
        if (emailCount > 1) {
            return email + emailCount;
        }
        return email;
    }

    private static String createEmail(String emailName, String c) {
        return "<" + emailName + "@" + c + ".com>, ";
    }
}
