n = int(input())
cnt = 0
for _ in range(n):
    a, b, c, d = map(int,input().split())
    cnt += 1000 <= a or 1600 <= b or 1500 <= c or 1 <= d <= 30
print(cnt)