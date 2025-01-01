import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static final int MOD = 1000000007;
    static int N, M;
    static long dp[][], ans;
    
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        dp = new long[M][26];
        for (int i = 0; i < 26; i++) {
            dp[0][i] = 1;
        }
        for (int i = 1; i < M; i++) {
            for (int j = 0; j < 26; j++) {
                for (int k = 0; k < 26; k++) {
                    if (N <= Math.abs(j-k)) {
                        dp[i][j] += dp[i-1][k];
                        dp[i][j] %= MOD;
                    }
                }
            }
        }
        for (int i = 0; i < 26; i++) {
            ans += dp[M-1][i];
            ans %= MOD;
        }
        
        System.out.println(ans);

    }
}