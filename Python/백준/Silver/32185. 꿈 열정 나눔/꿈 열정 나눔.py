n,k,*a=open(0)
n,m=map(int,n.split())
f=lambda s:eval(s.replace(*' +'))
t=f(k)
b=[[f(a[i]),i+1]for i in range(n)]
b.sort(key=lambda x:-x[0])
print(0,end=' ')
m-=1
i=0
while m:
    if i==n:break
    if b[i][0]<=t:print(b[i][1],end=' ');m-=1
    i+=1