a=[0]*10
n,m=map(int,input().split())
for i in range(n,m+1):
 for j in str(i):a[int(j)]+=1
print(*a)