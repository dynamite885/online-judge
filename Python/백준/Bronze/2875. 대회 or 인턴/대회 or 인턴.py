n,m,k=map(int,input().split())
t=min(n//2,m)
k-=n+m-t*3
if 0<k:t-=(k+2)//3
print(t)