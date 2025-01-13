n,*a=map(int,open(0))
l=r=x=y=0
for i in range(n):
    if x<a[i]:l+=1
    if y<a[~i]:r+=1
    x=max(a[i],x)
    y=max(a[~i],y)
print(l,r)