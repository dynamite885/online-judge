while 1:
    n=int(input())
    if n==-1:break
    r=k=0
    for _ in range(n):
        s,t=map(int,input().split())
        r+=s*(t-k)
        k=t
    print(r,'miles')