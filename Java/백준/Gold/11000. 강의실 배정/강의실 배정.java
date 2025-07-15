import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, S, T;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] == b[0])
                return a[1] - b[1];
            return a[0] - b[0];
        });

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            S = Integer.parseInt(st.nextToken());
            T = Integer.parseInt(st.nextToken());
            pq.add(new int[]{S, T});
        }

        int cnt = 0;
        SortedMap<Integer, Integer> map = new TreeMap<>();

        while (!pq.isEmpty()) {
            int[] lecture = pq.poll();
            S = lecture[0];
            T = lecture[1];
            if (map.isEmpty()) {
                map.put(T, 1);
                cnt++;
                continue;
            }
            int K = map.firstKey();
            if (K <= S && 0 < K) {
                map.put(K, map.get(K) - 1);
                if (map.get(K) == 0) {
                    map.remove(K);
                }
            } else {
                cnt++;
            }
            map.putIfAbsent(T, 0);
            map.put(T, map.get(T) + 1);
        }
        System.out.println(cnt);
    }
}