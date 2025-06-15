import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	static int N, M, parents[], ans, cnt;
	static ArrayList<int[]> arr;

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());
		parents = new int[N];
		for (int i = 0; i < N; i++) {
			parents[i] = i;
		}
		arr = new ArrayList<>();

		int a, b, w;
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken())-1;
			b = Integer.parseInt(st.nextToken())-1;
			w = Integer.parseInt(st.nextToken());
			arr.add(new int[] { a, b, w });

		}
		Collections.sort(arr, new Comparator<int[]>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				return o1[2] - o2[2];
			}

		});
		
		for (int[] is : arr) {
			if (union(is[0], is[1])) {
				ans += is[2];
				cnt++;
				if (cnt == N-1) break;
			}
		}

		System.out.println(ans);
	}
	
	private static int find(int a) {
		if (a == parents[a]) return a;
		return parents[a] = find(parents[a]);
	}
	
	private static boolean union(int a, int b) {
		a = find(a);
		b = find(b);
		if (a == b) return false;
		parents[b] = a;
		return true;
	}
}