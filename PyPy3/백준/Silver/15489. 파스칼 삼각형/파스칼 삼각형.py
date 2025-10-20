import math
r, c, w = map(int, input().split())
total = 0
for i in range(w):
    row = r + i
    for j in range(i + 1):
        total += math.comb(row - 1, c - 1 + j)
print(total)