input = open(0).readline
I = lambda:map(int, input().split())
idx = 0
m, n = I()
castle = [[*I()] for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
size = []

delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]    # 서북동남

def dfs(r, c):
    for d in range(4):
        dr, dc = delta[d]
        nr, nc = r + dr, c + dc
        if castle[r][c] & 2**d == 0 and visited[nr][nc] == -1:
            visited[nr][nc] = idx
            size[-1] += 1
            dfs(nr, nc)

for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            size += [1]
            visited[i][j] = idx
            dfs(i, j)
            idx += 1

r1 = max(size)
r2 = 0

for i in range(n):
    for j in range(m-1):
        a, b = visited[i][j], visited[i][j+1]
        if a != b:
            r2 = max(r2, size[a] + size[b])
for i in range(n-1):
    for j in range(m):
        a, b = visited[i][j], visited[i+1][j]
        if a != b:
            r2 = max(r2, size[a] + size[b])

print(len(size), r1, r2)