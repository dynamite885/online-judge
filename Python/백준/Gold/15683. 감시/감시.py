from itertools import*
n,m = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cctvType = [[], [0], [0,2], [0,1], [0,1,2], [0,1,2,3]]
cctvPos = []
for i in range(n):
    for j in range(m):
        if 0<arr[i][j]<6:
            cctvPos += [[i,j]]
cctvCnt = len(cctvPos)
cctvDir = [0]*cctvCnt
min = 1e9

for i in product(range(4), repeat=cctvCnt):
    cctvDir = list(i)
    visited = [[0]*m for _ in range(n)]
    for j in range(cctvCnt):
        x, y = cctvPos[j]
        for k in cctvType[arr[x][y]]:
            k = (k + cctvDir[j]) % 4
            nx, ny = x, y
            while 0<=nx<n and 0<=ny<m and arr[nx][ny]!=6:
                visited[nx][ny] = 1
                nx += dx[k]
                ny += dy[k]
    cnt = 0
    for j in range(n):
        for k in range(m):
            if not visited[j][k] and arr[j][k]==0:
                cnt += 1
    if min > cnt:
        min = cnt
print(min)