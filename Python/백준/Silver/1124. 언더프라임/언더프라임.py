a,b=map(int,input().split())
arr=[0]*-~b
p=set()
for n in range(2,b+1):
    if arr[n]==0:
        p.add(n)
        t=n
        while t<=b:
            for i in range(t,b+1,t):
                arr[i]+=1
            t*=n
cnt=0
for i in range(a,b+1):
    cnt+=arr[i]in p
print(cnt)