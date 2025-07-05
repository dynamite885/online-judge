N,M,K = map(int,input().split())
matrix = [[*map(int,input().split())]for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dice = [1,6,4,3,2,5]
score = 0
cnt = 0
def check(x,y):
    return 0<=x<M and 0<=y<N

def roll(dir):
    global dice
    상, 하, 좌, 우, 앞, 뒤 = dice
    if dir==0: #오른쪽
        dice = [좌, 우, 하, 상, 앞, 뒤]
    elif dir==1: #아래
        dice = [앞, 뒤, 좌, 우, 하, 상]
    elif dir==2: #왼쪽
        dice = [우, 좌, 상, 하, 앞, 뒤]
    elif dir==3: #위
        dice = [뒤, 앞, 좌, 우, 상, 하]
    else:print("아무 일도 일어나지 않았다(!?)")

def dfs(x,y,t):
    global cnt
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if check(nx,ny) and matrix[ny][nx]==t and visit[ny][nx]==0:
            cnt += 1
            visit[ny][nx] = 1
            dfs(nx,ny,t)

x = y = 0
dir = 0

while K:
    K-=1
    if not check(x+dx[dir], y+dy[dir]):
        dir = (dir+2)%4
    x += dx[dir]
    y += dy[dir]
    roll(dir)
    visit = [[0]*M for _ in range(N)]
    cnt = 1
    target = matrix[y][x]
    visit[y][x] = 1
    dfs(x,y,target)
    score += target*cnt
    if dice[1]>target:
        dir = (dir+1)%4
    elif dice[1]<target:
        dir = (dir+3)%4
print(score)