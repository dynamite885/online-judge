n, t, *a = map(int, open(0).read().split())
print(t, end=' ')
s = t
for i in range(n - 1):
    nxt = a[i] * (i + 2) - s
    s += nxt
    print(nxt, end=' ')
    t = i