input = open(0).readline
I = lambda:map(int, input().split())
r, c, q = I()
a = [[0] * (c + 1)] + [[0, *I()] for _ in range(r)]

for i in range(r):
    for j in range(c):
        a[i + 1][j + 1] += a[i + 1][j] + a[i][j + 1] - a[i][j]

for _ in range(q):
    r1, c1, r2, c2 = I()
    r1 -= 1
    c1 -= 1
    s = a[r2][c2] - a[r2][c1] - a[r1][c2] + a[r1][c1]
    t = (r2 - r1) * (c2 - c1)
    print(s // t)