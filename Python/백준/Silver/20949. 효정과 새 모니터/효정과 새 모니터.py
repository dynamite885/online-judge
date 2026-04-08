n,*a=open(0)
n=int(n)
b=[]
for i in range(n):
    w,h=map(int,a[i].split())
    b+=[[w*w+h*h,i+1]]
b.sort(key=lambda x:-x[0])
for i,j in b:print(j)