import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static ArrayList<int[]>[] graph;
    static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N+1];
        for(int i=1; i<=N; i++) graph[i] = new ArrayList<>();

        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            graph[a].add(new int[]{b, d});
            graph[b].add(new int[]{a, d});
        }

        int[] foxDist = dijkstraFox();
        int[] wolfDist = dijkstraWolf();

        int answer = 0;
        for(int i=1; i<=N; i++) {
            if(foxDist[i] < wolfDist[i]) answer++;
        }

        System.out.println(answer);
    }

    // 여우 다익스트라 (일반)
    static int[] dijkstraFox() {
        int[] dist = new int[N+1];
        Arrays.fill(dist, INF);
        dist[1] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[]{1, 0});

        while(!pq.isEmpty()) {
            int[] cur = pq.poll();
            int node = cur[0];
            int cost = cur[1];
            if(dist[node] < cost) continue;

            for(int[] nxt : graph[node]) {
                int nextNode = nxt[0];
                int nd = nxt[1] * 2; // 여우는 d*2 로 시간 계산
                int ncost = cost + nd;
                if(dist[nextNode] > ncost) {
                    dist[nextNode] = ncost;
                    pq.offer(new int[]{nextNode, ncost});
                }
            }
        }

        return dist;
    }

    // 늑대 다익스트라 (상태 2개: 0=빠른 상태(다음은 느린 상태), 1=느린 상태(다음은 빠른 상태))
    static int[] dijkstraWolf() {
        int[][] dist = new int[N+1][2];
        for(int i=1; i<=N; i++) Arrays.fill(dist[i], INF);
        dist[1][0] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[2]));
        pq.offer(new int[]{1, 0, 0});

        while(!pq.isEmpty()) {
            int[] cur = pq.poll();
            int node = cur[0];
            int state = cur[1];
            int cost = cur[2];

            if(dist[node][state] < cost) continue;

            for(int[] nxt : graph[node]) {
                int nextNode = nxt[0];
                int d = nxt[1];
                int ncost;

                if(state == 0) {
                    // 빠른 상태 (여우 시간의 절반): 늑대 시간 = d
                    ncost = cost + d;
                } else {
                    // 느린 상태 (여우 시간의 2배): 늑대 시간 = d * 4
                    ncost = cost + d * 4;
                }

                int nextState = 1 - state;
                if(dist[nextNode][nextState] > ncost) {
                    dist[nextNode][nextState] = ncost;
                    pq.offer(new int[]{nextNode, nextState, ncost});
                }
            }
        }

        int[] ans = new int[N+1];
        for(int i=1; i<=N; i++) {
            ans[i] = Math.min(dist[i][0], dist[i][1]);
        }
        return ans;
    }
}
