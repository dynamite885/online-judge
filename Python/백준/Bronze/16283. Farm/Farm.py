a, b, n, w = map(int, input().split())
ans = []
for i in range(1, n):
    if a * i + b * (n - i) == w:
        ans += [(i, n - i)]

if len(ans) == 1:
    print(*ans[0])
else:
    print(-1)