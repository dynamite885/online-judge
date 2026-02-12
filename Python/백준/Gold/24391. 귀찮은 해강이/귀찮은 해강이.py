import sys
sys.setrecursionlimit(10**6)
input = open(0).readline
n, m = map(int, input().split())
*parent, = range(n + 1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = sorted([find(a), find(b)])
    parent[b] = a

for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

t, *a = map(int, input().split())
cnt = 0
for i in a:
    cnt += find(t) != find(i)
    t = i

print(cnt)