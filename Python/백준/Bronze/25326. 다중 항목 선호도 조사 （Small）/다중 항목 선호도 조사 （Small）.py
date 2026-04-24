input=open(0).readline
n,m=map(int,input().split())
a=[input().split()for _ in range(n)]
for _ in range(m):
    cnt=0
    x,y,z=input().split()
    for i,j,k in a:
        cnt+=(x=="-" or i==x)*(y=="-" or j==y)*(z=="-" or k==z)
    print(cnt)