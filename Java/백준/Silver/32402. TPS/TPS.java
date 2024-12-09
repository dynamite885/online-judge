import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, dir, x, y;
    static int dx[] = {0, 1, 0, -1};
    static int dy[] = {1, 0, -1, 0};
    static String str;
    
    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            str = br.readLine();
            switch (str) {
            case "MR":
                dir++;
                dir %= 4;
                break;
            case "ML":
                dir += 3;
                dir %= 4;
                break;
            case "W":
                x += dx[dir];
                y += dy[dir];
                break;
            case "A":
                x += dx[(dir+3)%4];
                y += dy[(dir+3)%4];
                break;
            case "S":
                x += dx[(dir+2)%4];
                y += dy[(dir+2)%4];
                break;
            case "D":
                x += dx[(dir+1)%4];
                y += dy[(dir+1)%4];
                break;
            }
            System.out.println(x + " " + y + " " + (x-dx[dir]) + " " + (y-dy[dir]));
        }
    }
}