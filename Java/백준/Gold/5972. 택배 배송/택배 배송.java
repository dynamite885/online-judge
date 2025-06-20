import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, M, a, b, c;
    static int[] dist;
    static ArrayList<ArrayList<int[]>> adjList;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        dist = new int[N];
        adjList = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            dist[i] = Integer.MAX_VALUE;
            adjList.add(new ArrayList<>());
        }
        dist[0] = 0;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken()) - 1;
            b = Integer.parseInt(st.nextToken()) - 1;
            c = Integer.parseInt(st.nextToken());
            adjList.get(a).add(new int[] { b, c });
            adjList.get(b).add(new int[] { a, c });
        }

        dijkstra(0);
        System.out.println(dist[N - 1]);
    }

    public static void dijkstra(int start) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        pq.add(new int[] {start, 0});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int u = cur[0];
            int curDist = cur[1];
            if (dist[u] < curDist) continue;

            for (int[] adj : adjList.get(u)) {
                int v = adj[0];
                int w = adj[1];
                if (dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;
                    pq.add(new int[] {v, dist[v]});
                }
            }
        }
    }
}