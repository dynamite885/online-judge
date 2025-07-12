import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int n, d, c, a, b, s;
    static int[] dist;
    static ArrayList<ArrayList<int[]>> adjList;

    public static void main(String[] args) throws IOException {
        int tc = Integer.parseInt(br.readLine());
        for (int i = 0; i < tc; i++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            d = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken()) - 1;

            adjList = new ArrayList<>();
            dist = new int[n];

            for (int j = 0; j < n; j++) {
                dist[j] = Integer.MAX_VALUE;
                adjList.add(new ArrayList<>());
            }

            dist[c] = 0;

            for (int j = 0; j < d; j++) {
                st = new StringTokenizer(br.readLine());
                a = Integer.parseInt(st.nextToken()) - 1;
                b = Integer.parseInt(st.nextToken()) - 1;
                s = Integer.parseInt(st.nextToken());
                adjList.get(b).add(new int[] { a, s });
            }
            dijkstra(c);
            int cnt = 0;
            int max = 0;
            for (int j = 0; j < n; j++) {
                if (dist[j] < Integer.MAX_VALUE) {
                    cnt++;
                    max = Math.max(max, dist[j]);
                }
            }

            sb.append(cnt).append(" ").append(max).append("\n");
        }
        System.out.print(sb.toString());
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