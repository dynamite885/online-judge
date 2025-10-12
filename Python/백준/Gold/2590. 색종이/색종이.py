a, b, c, d, e, f = map(int, open(0))
A = B = 0 # 남는 공간
x = (c + 3) // 4 + d + e + f
C = -c % 4
B += [0, 1, 3, 5][C]
A += e * 11 + C * 9 - B * 4
B += d * 5

t = min(b, B)
b -= t
B -= t

if 0 < B:
    A += B * 4
else:
    x += (b + 8) // 9
    A += (-b % 9) * 4

t = min(a, A)
a -= t
A -= t
x += (a + 35) // 36
    
print(x)