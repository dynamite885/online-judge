n=int(input())
a=[eval('""'+"+input()"*5)for _ in' '*n]
d=36
for i in range(n-1):
 for j in range(i+1,n):
  s=sum(a[i][k]!=a[j][k]for k in range(35))
  if s<d:d=s;b=[i+1,j+1]
print(*b)