n,m,k,*d=map(int,open(0).read().split())
a=sorted(zip(d,range(1,n+1)))[::-1]
p=[]
ans=[]
for i in range(k):
    if not p:
        if a:*p,=a.pop()
        elif m:m-=1;ans+=[0];continue
        else:exit(print(-1))
    if p[0]-1:
        p[0]-=1
        if m:
            m-=1
            ans+=[0]
        else:
            exit(print(-1))
    else:
        ans+=[p[1]]
        p=[]
print(*ans)