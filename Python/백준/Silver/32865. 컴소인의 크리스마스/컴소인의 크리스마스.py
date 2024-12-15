n,*a=map(int,open(0))
if sum(a)!=n-1:exit(print(-1))
b=[[i,a[i]]for i in range(n)]
b.sort(key=lambda x:x[1])
p=q=c=0
for i in range(n):
    if b[i][1]:q=i;break
while p<n:
    if c%2:
        print(b[q][0]+1)
        b[q][1]-=1
        if b[q][1]==0:q+=1
    else:
        print(b[p][0]+1);p+=1
    c+=1