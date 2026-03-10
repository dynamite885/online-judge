input = open(0).readline
n, m, q = map(int, input().split())
a = [input() for _ in range(n)]

ans = [0] * (n + 1)
for j in range(m):
    d = 0
    for i in range(n-1, -1, -1):
        if a[i][j] == '.': d += 1
        elif a[i][j] == '*': ans[min(d, n)] += 1

for i in range(n): ans[i+1] += ans[i]

for _ in range(q):
    t = int(input())
    print(ans[min(t, n)])