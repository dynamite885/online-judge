n=int(input())
q=input()
a=[n*[0]for _ in' '*n]
x=y=nx=ny=0
for i in q:
    if i=='U':ny=y-1
    elif i=='D':ny=y+1
    elif i=='L':nx=x-1
    elif i=='R':nx=x+1
    ny=max(0,min(n-1,ny))
    nx=max(0,min(n-1,nx))
    if y!=ny:a[y][x]|=1;a[ny][nx]|=1
    if x!=nx:a[y][x]|=2;a[ny][nx]|=2
    x,y=nx,ny
for line in a:print(*['.|-+'[i]for i in line],sep='')