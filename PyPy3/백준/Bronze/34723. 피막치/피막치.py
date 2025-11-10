a,b,c,x=map(int,open(0).read().split())
r=10**12
for i in range(1,a+1):
    for j in range(1,b+1):
        for k in range(1,c+1):
            r=min(r,abs((i+j)*(j+k)-x))
print(r)