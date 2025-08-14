from collections import deque
input = open(0).readline

n,m = map(int,input().split())
indegree = [0]*(n+1)
adj = [[]for _ in range(n+1)]

for _ in range(m):
    _,*a = map(int,input().split())
    for i in range(len(a)-1):
        adj[a[i]] += [a[i+1]]
        indegree[a[i+1]] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

ans = []
while q:
    cur = q.popleft()
    ans += [cur]
    n -= 1
    for nxt in adj[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

if n==0:
    print(*ans,sep='\n')
else:
    print(0)