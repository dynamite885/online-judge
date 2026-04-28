import math
for i in[*open(0)]:
    a,b=map(int,i.split())
    if a==b==0:exit()
    l=math.lcm(a,b)
    print((l//a)*(l//b))