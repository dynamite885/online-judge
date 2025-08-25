dy=[-1,-1,-1,0,0,1,1,1]
dx=[-1,0,1,-1,1,-1,0,1]
n=int(input())
a=[input()for _ in range(n)]
b=[input()for _ in range(n)]
c=[[]for _ in range(n)]

def check(x,y):
    return n > x >= 0 <= y < n
isDie=False
for y in range(n):
    for x in range(n):
        if b[y][x]=='.':
            c[y]+='.'
            continue
        if a[y][x]=='*':
            isDie=True
        cnt=0
        for d in range(8):
            ny = y+dy[d]
            nx = x+dx[d]
            if check(ny,nx) and a[ny][nx]=='*':
                cnt+=1
        c[y]+=[str(cnt)]
if isDie:
    for i in range(n):
        for j in range(n):
            if a[i][j]=='*':
                c[i][j]='*'
for i in c:
    print(''.join(i))