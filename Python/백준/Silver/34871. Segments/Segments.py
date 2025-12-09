input = open(0).readline
n, q = map(int, input().split())
maxl = 0
minr = 1e9

for _ in range(n):
    l, r, y = map(int, input().split())
    maxl = max(maxl, l)
    minr = min(minr, r)

for _ in range(q):
    t = int(input())
    print(max(0, maxl - t, t - minr))