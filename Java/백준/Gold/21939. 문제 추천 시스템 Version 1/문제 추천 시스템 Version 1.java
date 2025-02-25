import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int N, M, P, L;
    static NavigableMap<Integer, SortedSet<Integer>> map;
    public static void main(String[] args) throws IOException {
        map = new TreeMap<>();

        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            P = Integer.parseInt(st.nextToken());
            L = Integer.parseInt(st.nextToken());
            map.putIfAbsent(L, new TreeSet<>());
            map.get(L).add(P);
        }
        M = Integer.parseInt(br.readLine());
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            if (s.equals("recommend")) {
                int x = Integer.parseInt(st.nextToken());
                if (x == 1) {
                    sb.append(map.lastEntry().getValue().last()).append("\n");
                } else {
                    sb.append(map.firstEntry().getValue().first()).append("\n");
                }
            } else if (s.equals("add")) {
                P = Integer.parseInt(st.nextToken());
                L = Integer.parseInt(st.nextToken());
                map.putIfAbsent(L, new TreeSet<>());
                map.get(L).add(P);
            } else if (s.equals("solved")) {
                P = Integer.parseInt(st.nextToken());
                for (Map.Entry<Integer, SortedSet<Integer>> entry : map.entrySet()) {
                    if (entry.getValue().contains(P)) {
                        entry.getValue().remove(P);
                        L = entry.getKey();
                        break;
                    }
                }
                if (map.get(L).isEmpty()) {
                    map.remove(L);
                }
            }
        }
        System.out.print(sb.toString());
    }
}