from collections import deque

def bfs(start, end):
    visited = {start}
    q = deque()
    q.append((start, []))

    while q:
        cur, s = q.popleft()
        if cur == end:
            return ''.join(s)
        for nxt, cmd in [
            (cur * 2, 'D'), 
            (cur - 1, 'S'), 
            (cur * 10 + cur // 1000, 'L'),
            (cur // 10 + cur * 1000, 'R')
            ]:
            nxt %= 10000
            if nxt in visited:continue
            visited.add(nxt)
            ns = s + [cmd]
            q.append((nxt, ns))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(bfs(a, b))