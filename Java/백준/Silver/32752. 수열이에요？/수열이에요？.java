import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, L, R, arr[], arr2[], ans;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        L = Integer.parseInt(st.nextToken())-1;
        R = Integer.parseInt(st.nextToken());
        arr = new int[N];
        arr2 = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            arr2[i] = arr[i];
        }
        Arrays.sort(arr);
        Arrays.sort(arr2, L, R);
        ans = 1;
        for (int i = 0; i < N; i++) {
            if (arr[i] != arr2[i]) {
                ans = 0;
                break;
            }
        }
        System.out.println(ans);
    }
}