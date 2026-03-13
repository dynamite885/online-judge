n,k=map(int,input().split())
*a,=input()
cnt=0
for i in range(n):
    if a[i]!='P':continue
    for j in range(max(0,i-k),min(i+k+1,n)):
        if a[j]=='H':
            cnt+=1
            a[j]=''
            break
print(cnt)