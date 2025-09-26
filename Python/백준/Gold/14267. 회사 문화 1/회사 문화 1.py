import sys
sys.setrecursionlimit(8**8)
input = open(0).readline
n,m = map(int,input().split())
par = *map(int,input().split()),
adj = [[]for _ in range(n)]
for i in range(n):
    if i:adj[par[i]-1] += [i]
ans = [0]*n
def dfs(cur):
    for nxt in adj[cur]:
        ans[nxt] += ans[cur]
        dfs(nxt)

for _ in range(m):
    i,w = map(int,input().split())
    ans[i-1] += w
dfs(0)

print(*ans)