import java.io.*;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static StringBuilder sb = new StringBuilder();

    static int N, cnt;
    static String S;

    public static void main(String[] args) throws IOException {
        N = Integer.parseInt(br.readLine());
        S = br.readLine();
        Pattern p1 = Pattern.compile("P[^P]*?R[^R]*?S");
        Pattern p2 = Pattern.compile("R[^R]*?S[^S]*?P");
        Pattern p3 = Pattern.compile("S[^S]*?P[^P]*?R");
        Matcher m1 = p1.matcher(S);
        Matcher m2 = p2.matcher(S);
        Matcher m3 = p3.matcher(S);
        while (m1.find() | m2.find() | m3.find()) cnt++;
        System.out.println(N - 3*cnt);
    }
}