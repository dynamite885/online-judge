from collections import*
N,M,*A=map(int,open(0).read().split())
d=deque(range(1,N+1))
ans=0
for i in A:
    cnt=0
    while d[0]!=i:
        d.append(d.popleft())
        cnt+=1
    ans+=min(cnt,len(d)-cnt)
    d.popleft()
print(ans)