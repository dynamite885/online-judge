N,*A = map(int,open(0).read().split())
dp = []
pos = [0]*N
trace = []

for i in range(N):
    p = 0
    q = len(dp)
    while p < q:
        m = (p+q)>>1
        if dp[m] < A[i]:
            p = m + 1
        else:
            q = m
    if p==len(dp):
        dp += [A[i]]
        trace += [i]
    else:
        dp[p] = A[i]
        trace[p] = i
    pos[i] = p

ans = []
idx = len(dp) - 1

for i in range(N-1,-1,-1):
    if pos[i]==idx:
        ans += [A[i]]
        idx -= 1
    if idx < 0:
        break

print(len(dp))
print(*ans[::-1])