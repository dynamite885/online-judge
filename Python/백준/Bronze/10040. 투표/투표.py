n,m,*a=map(int,open(0).read().split())
b=[0]*n
for j in range(m):
    for i in range(n):
        if a[i]<=a[n+j]:
            b[i]+=1
            break
print(b.index(max(b))+1)