n,*a=map(int,open(0).read().split())
b=[[1,1]for _ in range(n)]
for i in range(n-1):
    if a[i]<a[i+1]:b[i+1][0]=b[i][0]+1
for i in range(n-1,0,-1):
    if a[i]<a[i-1]:b[i-1][1]=b[i][1]+1
print(max([sum(i)for i in b])-1)