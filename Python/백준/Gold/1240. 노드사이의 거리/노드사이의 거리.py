n,m=map(int,input().split())
d={}
for i in' '*~-n:
    u,v,w=map(int,input().split())
    if u not in d:d[u]=[]
    if v not in d:d[v]=[]
    d[u]+=[(v,w)]
    d[v]+=[(u,w)]
def bfs(s,e):
    q=[[s,0]]
    v=[0]*(n+1)
    v[s]=1
    while q:
        t,c=q.pop(0)
        if t==e:return c
        for i in d[t]:
            if not v[i[0]]:
                v[i[0]]=1
                q+=[[i[0],c+i[1]]]

for i in' '*m:
    a,b=map(int,input().split())
    print(bfs(a,b))