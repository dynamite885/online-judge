N,m,M,T,R=map(int,input().split())
t=0
a=m
while N:
    t+=1
    if a+T<=M:
        a+=T
        N-=1
    else:
        if a==m:exit(print(-1))
        a-=R
        if a<m:
            a=m
print(t)