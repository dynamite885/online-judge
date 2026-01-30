n,m=map(int,input().split())
for i in range(n):print(*(1+j%(m//2)+m//2*i%(n*m//4)for j in range(m)))