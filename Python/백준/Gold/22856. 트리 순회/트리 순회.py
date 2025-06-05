n,*t=open(0)
n=int(n)
adj=[[]for _ in' '*-~n]
for i in t:
    a,b,c=map(int,i.split())
    adj[a]+=[b,c]
cnt=0
u=1
while 1:
    L,R=*adj[u],
    if R==-1:break
    u=R
    cnt+=1
print((n-1)*2-cnt)