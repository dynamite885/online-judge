def toMinute(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m

input = open(0).readline
n, m = map(int, input().split())
v = {}
for _ in range(n):
    name, day, start, end = input().split()
    day = int(day) - 1
    if name not in v:
        v[name] = [[0, 0] for _ in range(m // 7)]
    time = toMinute(end) - toMinute(start)
    v[name][day // 7][0] += 1
    v[name][day // 7][1] += time

ans = []
for name, t in v.items():
    if all(4 < x and 3600 <= y for x, y in t):
        ans += [name]

if ans:
    print(*sorted(ans))
else:
    print(-1)