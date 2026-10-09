import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class UserReport {

    public static String readFile(String path) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(path));
        String result = "";
        String line;
        while ((line = reader.readLine()) != null) {
            result += line + "\n";
        }
        return result;
    }

    public static boolean isSameUser(String a, String b) {
        return a == b;
    }

    public static List<String> findDuplicates(List<String> names) {
        List<String> dups = new ArrayList<>();
        for (int i = 0; i < names.size(); i++) {
            for (int j = 0; j < names.size(); j++) {
                if (i != j && names.get(i).equals(names.get(j)) && !dups.contains(names.get(i))) {
                    dups.add(names.get(i));
                }
            }
        }
        return dups;
    }
}
