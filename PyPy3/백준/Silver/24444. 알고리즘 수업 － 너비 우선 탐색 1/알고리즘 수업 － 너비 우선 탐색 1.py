from collections import deque
N,*a=open(0)
N,M,R=map(int,N.split())
adj=[[] for _ in range(N+1)]
for i in a:
    u,v=map(int,i.split())
    adj[u].append(v)
    adj[v].append(u)
visit=[0]*(N+1)
order=[0]*(N+1)
def bfs(start):
    queue=deque([start])
    visit[start]=1
    cnt=1
    order[start]=cnt
    while queue:
        node=queue.popleft()
        for i in sorted(adj[node]):
            if not visit[i]:
                visit[i]=1
                cnt+=1
                order[i]=cnt
                queue.append(i)
bfs(R)
print(*order[1:], sep='\n')