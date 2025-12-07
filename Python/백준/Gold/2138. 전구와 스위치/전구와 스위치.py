n = int(input())
s = []
for i, j in zip(input(), input()):
    s += [int(i)^int(j)]

a = [0] * (n + 1)
b = [0] * (n + 1)
b[0] = 1

for i in range(n - 1):
    a[i + 1] = a[i - 1]^a[i]^s[i]
    b[i + 1] = b[i - 1]^b[i]^s[i]

ans = []
if sum(a[-3:])%2 == s[-1]:
    ans += [sum(a)]
if sum(b[-3:])%2 == s[-1]:
    ans += [sum(b)]

if ans:
    print(min(ans))
else:
    print(-1)