n,*a=open(0)
n,q=map(int,n.split())
i=t=0
m=1e20
for s in a:
    i+=1
    p,k,c=map(int,s.split())
    x=-(-q//k)-1
    x=x*-~x//2
    if x*c+p<m:
        m=x*c+p
        t=i
print(t,m)