import math
for i in[*open(0)][:-1]:
    a,b=map(int,i.split())
    print(f'{a}+{b}{"!"*(a+b!=math.comb(a+b,a))}={a+b}')