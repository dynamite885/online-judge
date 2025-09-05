from collections import deque
input = open(0).readline
n,m = map(int,input().split())
a = [[*map(int,input().split())] for _ in range(n)]
b = [[*map(int,input().split())] for _ in range(n)]
diff = -1
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            if diff == -1:
                diff = b[i][j]
            elif diff != b[i][j]:
                print('NO')
                exit()
if diff == -1:
    print('YES')
    exit()

c = [[+(a[i][j] != b[i][j]) for j in range(m)]for i in range(n)]
v = [[0]*m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def check(x,y):
    return 0 <= x < m and 0 <= y < n

def bfs(x,y,num):
    q = deque()
    q.append([x,y])
    v[y][x] = 1

    while q:
        x,y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if check(nx,ny) and a[ny][nx] == num and v[ny][nx] == 0:
                q.append([nx,ny])
                v[ny][nx] = 1

for i in range(n):
    for j in range(m):
        if c[i][j]:
            bfs(j,i,a[i][j])
            if sum(sum([[c[i][j]^v[i][j] for j in range(m)] for i in range(n)],[])) == 0:
                print('YES')
            else:
                print('NO')
            exit()