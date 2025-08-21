n,*a = map(int,open(0))
s = []
cnt = 1
idx = 0
ans = []

while idx < n:
    if s and s[-1] == a[idx]:
        s.pop()
        ans += ['-']
        idx += 1
    elif cnt <= n:
        s += [cnt]
        ans += ['+']
        cnt += 1
    else:
        print('NO')
        exit()

print(*ans,sep='\n')
