n,*a = map(int,open(0).read().split())
arr = []
for i in range(n):
    p = 0
    q = len(arr)
    while p < q:
        m = p+q>>1
        if arr[m] < a[i]:
            p = m+1
        else:
            q = m
    if p == len(arr):
        arr += [a[i]]
    else:
        arr[p] = a[i]
print(n-len(arr))