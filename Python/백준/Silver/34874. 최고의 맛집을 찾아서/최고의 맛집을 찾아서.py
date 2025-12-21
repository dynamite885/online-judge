x,*y=open(0)
n,m=map(int,x.split())
a=[[*map(int,i.split())]for i in y]
b=[max(i)for i in a]
for j in range(m):
    cnt=0
    for i in range(n):
        cnt+=a[i][j]<b[i]
    print(cnt,end=' ')