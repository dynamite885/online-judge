input = open(0).readline
I = lambda:map(int, input().split())
t = int(input())
for _ in range(t):
    n, m = I()
    a = sorted(I())
    b = sorted(I()) + [float('inf')]
    p = q = ans = 0
    while p < n:
        if a[p] <= b[q]:
            p += 1
            ans += q
        else:
            q += 1
    print(ans)