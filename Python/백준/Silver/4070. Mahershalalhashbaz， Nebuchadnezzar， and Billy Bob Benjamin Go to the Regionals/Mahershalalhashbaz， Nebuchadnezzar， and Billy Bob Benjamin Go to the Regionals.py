cnt=1
while 1:
    n,k=map(int,input().split())
    if n+k<1:break
    a=[len(input())for _ in range(n)]
    a.sort()
    f=0
    for i in range(n//k):
        b=a[i*k:i*k+k]
        t=sum(b)/k
        f=max(f,t+2<max(b)or min(b)<t-2)
    print(f'Case {cnt}:','yneos'[f::2])
    print()
    cnt+=1