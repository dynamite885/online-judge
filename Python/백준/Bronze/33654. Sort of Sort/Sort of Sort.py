t,*a,=map(int,[*open(0)][1].split())
b=[t]
for i in a:
    if b[-1]<=i:b+=[i]
print(*b)