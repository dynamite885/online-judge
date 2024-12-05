import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, ans, right, left;
    static ArrayList<long[]> arr;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr.add(new long[] {Long.parseLong(st.nextToken()), Long.parseLong(st.nextToken())});
        }
        arr.sort((o1, o2) -> (o1[0] > o2[0] ? 1:-1));
        for (long[] is : arr) {
            long a = is[0];
            long d = is[1];
            if (d == 1) right++;
            else if (d == 0) ans += right*2;
            else ans += right;
        }
        
        Collections.reverse(arr);
        for (long[] is : arr) {
            long a = is[0];
            long d = is[1];
            if (d == -1) left++;
            else if (d == 0) ans += left*2;
        }
        System.out.println(ans);
    }
}