n,l=map(int,input().split())
for i in range(l,101):
    *a,=range(i)
    k=n-sum(a)
    if k<0:break
    if k%i==0:
        print(*range(k//i,k//i+i))
        exit()
print(-1)