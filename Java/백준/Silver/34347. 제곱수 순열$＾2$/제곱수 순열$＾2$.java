import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            if (N == 2) {
                sb.append("YES\n");
                sb.append("1 2\n");
                sb.append("1 2\n");
            } else if (N == 4) {
                sb.append("YES\n");
                sb.append("1 2 3 4\n");
                sb.append("1 2 4 3\n");
            } else {
                sb.append("NO\n");
            }
        }
        System.out.print(sb);
    }
}