import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, M, K, S, cnt;
    static HashMap<Integer, Integer> map = new HashMap<>();
    
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N; i++) {
            K = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < K; j++) {
                S = Integer.parseInt(st.nextToken());
                map.put(S, map.getOrDefault(S, 0)+1);
            }
        }
        for (Integer i : map.values()) {
            if (M <= i) cnt++;
        }
        System.out.println(cnt);
    }
}