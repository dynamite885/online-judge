from collections import deque
a, b, c, d = map(int, input().split())
visited = set()
q = deque()
q.append((0, 0))
visited.add((0, 0))
cnt = 0
while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        if (x, y) == (c, d):
            print(cnt)
            exit()
        nxt = {(a, y), (x, b), (0, y), (x ,0), (min(a, x + y), max(0, x + y - a)), (max(0, x + y - b), min(b, x + y))}
        nxt -= visited
        visited |= nxt
        q.extend([*nxt])
    cnt += 1
print(-1)