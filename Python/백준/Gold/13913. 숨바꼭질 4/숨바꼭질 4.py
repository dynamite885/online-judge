from collections import deque
n,k = map(int,input().split())
tm = [1e6]*100010
par = [-1]*100010
tm[n] = 0
q = deque()
q.append(n)

while q:
    cur = q.popleft()
    if cur == k:
        ans = tm[cur]
        break
    t = tm[cur]+1
    for nxt in [cur*2, cur-1, cur+1]:
        if 0<=nxt<=1e5 and t<tm[nxt]:
            q.append(nxt)
            tm[nxt] = t
            par[nxt] = cur

print(ans)
ansArr = []
while 0<=k:
    ansArr += [k]
    k = par[k]
print(*ansArr[::-1])