n,m,*x=map(int,open(0).read().split())
a=x[:n]
b=x[n:]
k=[]
t=1
for i in a:k.insert(i-1,t);t+=1
l=[]
t=0
for i in b:l.insert(i-1,k[m-1::-1][t]);t+=1
print(*l[:3])