n,k,*a=map(int,open(s:=0).read().split())
d=-(13**9)
t=k
for i in range(n):
    if k:k-=1
    else:
        d=max(d,s)
        s-=a[i-t]
    s+=a[i]
print(max(d,s))