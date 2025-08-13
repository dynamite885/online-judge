n,k=map(int,open(0))
arr=[0]*(n+1)
i=2
t=1
while i<=n:
    if k<i:
        t=-1
    if arr[i]==0:
        l=len(arr[i::i])
        arr[i::i]=[t]*l
    i+=1
print(n-arr.count(-1))