import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();
    static int N, A, mid;
    static PriorityQueue<Integer> pq1;
    static PriorityQueue<Integer> pq2;
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        pq1 = new PriorityQueue<>((a,b) -> b - a);
        pq2 = new PriorityQueue<>();

        pq1.offer(-100000);
        pq2.offer(100000);
        mid = -100000;
        for (int i = 0; i < N; i++) {
            A = Integer.parseInt(br.readLine());
            pq2.offer(A);
            pq1.offer(pq2.poll());
            if (pq1.size() + 1 > pq2.size()) {
                pq2.offer(pq1.poll());
            }
            mid = pq2.peek();
            sb.append(mid).append("\n");
        }
        System.out.print(sb);
    }
}