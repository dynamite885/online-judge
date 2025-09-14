n,*a=map(int,open(r:=0).read().split())
t=2
for i in range(max(a)+1):
    s=a.count(i)
    if s in[1,2]and s<=t:r+=t==2;
    else:exit(print(0))
    t=s
print(2**r)