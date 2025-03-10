import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int a, b;
    static int N, M;
    static int u, v;

    static int[] dist;
    static ArrayList<Integer>[] adjList;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        a = Integer.parseInt(st.nextToken()) - 1;
        b = Integer.parseInt(st.nextToken()) - 1;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        dist = new int[N];
        for (int i = 0; i < N; i++) dist[i] = -1;

        adjList = new ArrayList[N];
        for (int i = 0; i < N; i++) adjList[i] = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken()) - 1;
            v = Integer.parseInt(st.nextToken()) - 1;
            adjList[u].add(v);
            adjList[v].add(u);
        }
        bfs(a);
        System.out.println(dist[b]);
    }

    static void bfs(int a) {
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        dist[a] = 0;
        queue.add(a);
        while (!queue.isEmpty()) {
            int u = queue.poll();
            for (int v : adjList[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    queue.add(v);
                }
            }
        }
    }
}