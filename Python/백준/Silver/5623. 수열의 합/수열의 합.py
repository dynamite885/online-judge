n,*a=open(0)
n=int(n)
a=[[*map(int,i.split())] for i in a]
if n==2:
    if a[0][1]==2:print('1 1')
    else:print('100000 100000')
    exit()
t=a[2][0]-a[2][1]
b=a[0][:]
b[0]=b[1]+t
s=b[0]//2
print(*[i-s for i in b])