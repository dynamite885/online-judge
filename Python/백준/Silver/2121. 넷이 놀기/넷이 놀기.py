input = open(0).readline
n = int(input())
a, b = map(int, input().split())
s = set()
for _ in range(n):
    x, y = map(int, input().split())
    s.add((x, y))
cnt = 0
for x, y in s:
    cnt += (x + a, y) in s and (x, y + b) in s and (x + a, y + b) in s
print(cnt)