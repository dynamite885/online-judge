n, m, k = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(k)]
d = {}
delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def dfs(cur):
    global s
    if s not in d:
        d[s] = 0
    d[s] += 1
    if len(s) == 5:
        return

    r, c = cur
    for dr, dc in delta:
        nr = r + dr
        nc = c + dc
        nr %= n
        nc %= m
        s += a[nr][nc]
        dfs((nr, nc))
        s = s[:-1]

for i in range(n):
    for j in range(m):
        s = a[i][j]
        dfs((i, j))

for i in b:
    print(d.get(i, 0))