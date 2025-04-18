X,*a=map(int,open(0).read().split())
print('YNeos'[X!=sum(i*j for i,j in zip(a[1::2],a[2::2]))::2])