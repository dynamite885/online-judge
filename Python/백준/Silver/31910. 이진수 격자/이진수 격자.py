n=int(input())
a=[[0]*-~n]+[[0]+[*map(int,input()[::2])]for _ in' '*n]
R=range(1,n+1)
for i in R:
    for j in R:a[i][j]+=max(a[i-1][j],a[i][j-1])<<1
print(a[n][n])