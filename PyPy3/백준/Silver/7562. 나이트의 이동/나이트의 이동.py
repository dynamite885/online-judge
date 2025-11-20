from collections import deque

delta = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]

def bfs(size, start, end):
    r, c = start
    board = [size * [float('inf')] for _ in range(size)]
    q = deque()
    q.append((r, c, 0))
    board[r][c] = 0
    while q:
        r, c, d = q.popleft()
        if (r, c) == end:
            return d
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < size and 0 <= nc < size and d + 1 < board[nr][nc]:
                board[nr][nc] = d + 1
                q.append((nr, nc, d + 1))
    return -1

t = int(input())
for _ in range(t):
    size = int(input())
    start = *map(int, input().split()),
    end = *map(int, input().split()),
    print(bfs(size, start, end))