import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int N, R, Q, visited[], count[];
    static ArrayList<Integer>[] adj;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());
        adj = new ArrayList[N + 1];
        visited = new int[N + 1];
        count = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            count[i] = 1;
        }

        for (int i = 0; i < N + 1; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int U = Integer.parseInt(st.nextToken());
            int V = Integer.parseInt(st.nextToken());
            adj[U].add(V);
            adj[V].add(U);
        }
        visited[R] = 1;
        dfs(R);

        for (int i = 1; i <= Q; i++) {
            int q = Integer.parseInt(br.readLine());
            sb.append(count[q]).append("\n");
        }
        System.out.print(sb);
    }

    public static void dfs(int v) {
        for (Integer i : adj[v]) {
            if (visited[i] == 0) {
                visited[i] = 1;
                dfs(i);
                count[v] += count[i];
            }
        }
    }
}