t = int(input())
for _ in range(t):
    input()
    a, b, c, d = map(int,input().split())
    a, b, c = sorted([a, b, c])
    x = c - b
    y = c - a + b - a
    if d <= x:
        c -= d
    elif d <= y:
        k = b + c - d
        b = c = k // 2
        c += k % 2
    else:
        k = a + b + c - d
        a = b = c = k // 3
        if k % 3 == 1:
            c += 1
        elif k % 3 == 2:
            b += 1
            c += 1
    print(a * b * c)