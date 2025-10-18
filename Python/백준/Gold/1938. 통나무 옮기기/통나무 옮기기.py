from collections import deque

n = int(input())
a = [[*input()] for _ in range(n)]
# visited[r][c][0]: 가로, visited[r][c][1]: 세로
visited = [[[0, 0] for j in range(n)] for _ in range(n)]
B = E = 0
start = end = None
for r in range(n):
    for c in range(n):
        match a[r][c]:
            case 'B':
                B += 1
                if B < 3:
                    start = (r, c, r - start[0] if start else None)
            case 'E':
                E += 1
                if E < 3:
                    end = (r, c, r - end[0] if end else None)

def check(r, c, d):
    if d == 0:
        return 0 <= r < n and  1 <= c < n - 1 and '1' not in (a[r][c - 1], a[r][c], a[r][c + 1])
    else:
        return 1 <= r < n - 1 and  0 <= c < n and '1' not in (a[r - 1][c], a[r][c], a[r + 1][c])
    
def checkTurn(r, c):
    return 1 <= r < n - 1 and 1 <= c < n - 1 and '1' not in a[r - 1][c - 1:c + 2] + a[r][c - 1:c + 2] + a[r + 1][c - 1:c + 2]

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

q = deque()
q.append(start)
r, c, d = start
visited[r][c][d] = 1
cnt = 0
while q:
    for _ in range(len(q)):
        r, c, d = q.popleft()
        if (r, c, d) == end:
            print(cnt)
            exit()
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if check(nr, nc, d) and visited[nr][nc][d] == 0:
                visited[nr][nc][d] = 1
                q.append((nr, nc, d))
        nd = 1 - d
        if checkTurn(r, c) and visited[r][c][nd] == 0:
            visited[r][c][nd] = 1
            q.append((r, c, nd))
    cnt += 1
print(0)