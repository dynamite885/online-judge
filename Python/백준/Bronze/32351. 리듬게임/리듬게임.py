a,*b=open(0)
n,s,k=map(eval,a.split())
ans=t=0
for i in b:
    x,y=map(eval,i.split())
    ans+=(x-1-t)*(60/s)*4
    t=x-1
    s=y
ans+=(n-t)*(60/s)*4
print(f'{ans:.12f}')