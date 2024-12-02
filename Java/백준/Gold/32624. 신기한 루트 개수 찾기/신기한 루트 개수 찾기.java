import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, A, B, visited[], ans;
    static ArrayList<Integer>[] adj;
    static boolean flag;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        A = Integer.parseInt(st.nextToken())-1;
        B = Integer.parseInt(st.nextToken())-1;
        visited = new int[N];
        adj = new ArrayList[N];
        for (int i = 0; i < N; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int i = 0; i < N-1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken())-1;
            int v = Integer.parseInt(st.nextToken())-1;
            adj[u].add(v);
            adj[v].add(u);
        }
        flag = false;
        visited[A] = 1;
        dfs(A);
        System.out.println(ans-1);
    }

    private static void dfs(int v) {
        if (v == B) {
            flag = true;
            return;
        }
        for (Integer i : adj[v]) {
            if (visited[i] == 0) {
                visited[i] = 1;
                ans++;
                dfs(i);
                if (v == A) {
                    if (flag) {
                        return;
                    } else {
                        ans = 0;
                    }
                }
            }
        }
    }
}