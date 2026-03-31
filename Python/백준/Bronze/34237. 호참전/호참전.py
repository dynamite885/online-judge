input=open(0).readline

n,m=map(int,input().split())
w=[[*map(int,input().split())]for _ in range(n)]
for _ in range(m):
    g,x,y=map(int,input().split())
    cnt=0
    for a,b in w:
        if g<a+b:continue
        if a<x or b<y:continue
        cnt+=1
    print(cnt)