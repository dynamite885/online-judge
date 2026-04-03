n,*a=map(int,open(0).read().split())
t=a[0]
s=0
for i in a:
    s=max(s,i-t)
    t=min(i,t)
print(s)