n,m = map(int,input().split())
arr = [input()for _ in range(n)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
visit = [[0]*m for _ in range(n)]
c = ''

def check(x,y):
    return 0<=x<m and 0<=y<n

def dfs(x,y,prvX,prvY):
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if check(nx,ny) and arr[ny][nx]==c and not (prvX==nx and prvY==ny):
            if visit[ny][nx]:
                exit(print('Yes'))
            else:
                visit[ny][nx] = 1
                dfs(nx,ny,x,y)

for x in range(m):
    for y in range(n):
        if visit[y][x]==0:
            c = arr[y][x]
            visit[y][x] = 1
            dfs(x,y,-1,-1)
print('No')