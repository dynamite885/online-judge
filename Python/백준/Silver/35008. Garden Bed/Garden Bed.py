n,*a,=map(int,open(0).read().split())
s=sum(a)
r=[]
for m in range(1,2**~-n):t=sum([x for i,x in enumerate(a)if(1<<i)&m]);r+=[t*(s-t)]
print(min(r),max(r))