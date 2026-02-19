n,m=map(int,input().split())
a=[input()for _ in range(n)]
for i in range(n):
    for j in range(m):
        print(end=min(a[i-1][j-1]+a[i-1][j]+a[i][j-1]+a[i][j]))
    print()