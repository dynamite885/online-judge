I=lambda:[*map(int,input().split())]
n,m=I()
a=I()
b=I()
for i in range(n):
    for j in range(m):a[i]=b[j]=a[i]^b[j]
print(a[-1])