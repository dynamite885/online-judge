n,*a = map(int,open(0).read().split())
k = [0]*50000
cnt = 0
for i in range(n):
    cnt += k[-a[i]]
    for j in range(i):
        k[a[i]+a[j]] += 1
print(cnt)