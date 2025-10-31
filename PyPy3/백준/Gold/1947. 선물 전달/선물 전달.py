n = int(input())
m = 10**9
a = [0, 1]
for _ in range(n):
    a += [(a[-1] + a[-2]) * len(a) % m]
print(a[-3])