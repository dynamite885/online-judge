n,m=map(int,input().split())
*a,=map(int,input().split())
for j in range(m):
    l,h=map(int,input().split())
    t=max(a)
    if t!=a[h-1]:a[l-1]-=1
print(*a)