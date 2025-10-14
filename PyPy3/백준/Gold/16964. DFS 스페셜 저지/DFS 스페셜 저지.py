input = open(0).readline
n = int(input())
s = set()
for _ in range(n - 1):
    u, v = map(int, input().split())
    if v < u:
        u, v = v, u
    s.add((u, v))
order = [*map(int, input().split())]
if order[0] != 1:
    print(0)
    exit()
skip = [1] * n
p, q = 0, 1
while s:
    if p < 0 or n <= q:
        print(0)
        exit()
    start, end = order[p], order[q]
    if end < start:
        start, end = end, start
    node = (start, end)
    if node in s:
        s.remove(node)
        p = q
        q += 1
    else:
        skip[q] += skip[p]
        p -= skip[p]
print(1)