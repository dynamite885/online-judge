import math
n,x,*a=map(int,open(0).read().split())
t=n*100
s=t-sum(a)
y=100-x
r=math.ceil((s*100/y-t)/100)
print(max(0,r))