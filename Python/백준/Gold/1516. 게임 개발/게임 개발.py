from collections import deque
N = int(input())
indegree = [0]*(N+1)
T = [0]*(N+1)
dp = [0]*(N+1)
adj = [[]for _ in range(N+1)]
d = deque()

for v in range(1,N+1): # u -> v
    t,*a,_ = map(int, input().split())
    T[v] = t
    dp[v] = t
    indegree[v] = len(a)
    for u in a:
        adj[u].append(v)
    if indegree[v] == 0:
        d.append(v)

while d:
    u = d.popleft()
    for v in adj[u]:      # u에서 갈 수 있는 노드
        indegree[v] -= 1  # v의 진입 차수 감소
        dp[v] = max(dp[v], dp[u] + T[v]) # v의 최대 시간 갱신
        if indegree[v] == 0:  # v의 진입 차수가 0이 되면
            d.append(v)       # 큐에 추가

print(*dp[1:],sep='\n')