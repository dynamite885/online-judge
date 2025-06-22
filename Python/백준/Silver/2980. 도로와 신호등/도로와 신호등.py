N,L=map(int,input().split())
t=p=0
while N:
    N-=1
    D,R,G=map(int,input().split())
    k=R+G
    t+=D-p
    p=D
    if t%k<R:t+=R-t%k
print(t+L-p)