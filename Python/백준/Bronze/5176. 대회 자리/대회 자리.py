input=open(0).readline
k=int(input())
for _ in range(k):
    p,m=map(int,input().split())
    s=set()
    for _ in range(p):
        x=int(input())
        s.add(x)
    print(p-len(s))