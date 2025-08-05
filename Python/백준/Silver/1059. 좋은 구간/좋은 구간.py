l,*s,n=map(int,open(0).read().split())
s+=[0]
a=n-max(i for i in s if i<=n)
b=min(i for i in s if n<=i)-n
print(max(a*b-1,0))