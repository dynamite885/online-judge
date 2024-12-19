import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, K, map[][], x, y;
    static int dx[] = {0, 1, 0, -1};
    static int dy[] = {1, 0, -1, 0};
    static String order;
    
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        map = new int[1001][1001];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken()) + 500;
            y = Integer.parseInt(st.nextToken()) + 500;
            map[y][x] = 1;
        }
        order = br.readLine();
        x = 500;
        y = 500;
        int d = 0;
        for (char c : order.toCharArray()) {
            switch (c) {
            case 'U':
                d=0;
                break;
            case 'R':
                d=1;
                break;
            case 'D':
                d=2;
                break;
            case 'L':
                d=3;
                break;
            }
            int nx = x + dx[d];
            int ny = y + dy[d];
            if (map[ny][nx] == 0) {
                x = nx;
                y = ny;
            }
        }
        System.out.println((x-500) + " " + (y-500));
    }
}