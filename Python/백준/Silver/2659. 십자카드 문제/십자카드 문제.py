s = set()
for i in range(1111, 10000):
    t = str(i)
    if '0' in t:continue
    L = [t]
    for _ in range(4):
        t = t[1:] + t[0]
        L += [t]
    s.add(min(L))

a = input().replace(' ', '')
L = [a]
for _ in range(4):
    a = a[1:] + a[0]
    L += [a]
a = min(L)

s = sorted(s)
print(s.index(a) + 1)