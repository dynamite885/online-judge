n,*a=map(int,open(0))
s={*a}
m=0
for i in sorted(a):
    c=sum([i+j in s for j in range(5)])
    m=max(m,c)
print(5-m)