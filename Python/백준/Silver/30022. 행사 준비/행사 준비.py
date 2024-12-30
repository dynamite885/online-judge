n,*r=open(0)
n,a,b=map(int,n.split())
r=[[*map(int,i.split())]for i in r]
r.sort(key=lambda x:x[0]-x[1])
c=0
for i,j in r:
    if a:
        a-=1
        c+=i
    else:
        c+=j
print(c)