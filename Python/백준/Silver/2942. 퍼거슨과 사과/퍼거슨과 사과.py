import math
r,g=map(int,input().split())
d=math.gcd(r,g)
A=[]
k=d
for i in range(1,int(d**.5)+1):
    if d%i==0:A+=[*{i,d//i}]
for i in sorted(A):
    print(i,r//i,g//i)