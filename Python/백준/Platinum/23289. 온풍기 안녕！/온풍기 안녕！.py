input = open(0).readline
R,C,K = map(int,input().split())
heaterArr = []
checkArr = []
chocoCnt = 0
dr = [-1,0,1,0]
dc = [0,1,0,-1]
dirMap = {1:1, 2:3, 3:0, 4:2}
matrix = [[0]*C for _ in range(R)]
for i in range(R):
    row = *map(int,input().split()),
    for j in range(C):
        if 0<row[j]<5:
            d = dirMap[row[j]]
            heaterArr += [[i,j,d]]
        elif row[j] == 5:
            checkArr += [[i,j]]

wallMap = [[0]*C for _ in range(R)]
W = int(input())
for i in range(W):
    x,y,t = map(int,input().split())
    x -= 1
    y -= 1
    if t:
        wallMap[x][y] |= 2
        wallMap[x][y+1] |= 8
    else:
        wallMap[x][y] |= 1
        wallMap[x-1][y] |= 4

visit = [[0]*C for _ in range(R)]

def check(r,c):return 0<=r<R and 0<=c<C

def checkMove(r,c,d):
    nr = r + dr[d]
    nc = c + dc[d]
    return check(nr,nc) and wallMap[r][c]&(2**d)==0
    

def heat(r,c,d,t):
    if t==0:return
    global matrix
    matrix[r][c] += t
    visit[r][c] = 1
    leftDir = (d+3)%4
    rightDir = (d+1)%4

    nr = r + dr[d]
    nc = c + dc[d]
    if checkMove(r,c,d) and visit[nr][nc]==0:
        heat(nr,nc,d,t-1)

    nr = r + dr[leftDir]
    nc = c + dc[leftDir]
    if checkMove(r,c,leftDir):
        nnr = nr + dr[d]
        nnc = nc + dc[d]
        if checkMove(nr,nc,d) and visit[nnr][nnc]==0:
            heat(nnr,nnc,d,t-1)

    nr = r + dr[rightDir]
    nc = c + dc[rightDir]
    if checkMove(r,c,rightDir):
        nnr = nr + dr[d]
        nnc = nc + dc[d]
        if checkMove(nr,nc,d) and visit[nnr][nnc]==0:
            heat(nnr,nnc,d,t-1)

def printMatrix(): # 디버깅용
    for i in matrix:
        print(i)
    print()

while 1:
    # 온풍기 작동
    for r,c,d in heaterArr: 
        visit = [[0]*C for _ in range(R)]
        nr = r + dr[d]
        nc = c + dc[d]
        heat(nr,nc,d,5)
    
    # 온도 조절
    tmpMatrix = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            diffSum = 0
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if checkMove(r,c,d):
                    diff = matrix[nr][nc]-matrix[r][c]
                    if diff<0:
                        diffSum += -(-diff//4)
                    else:
                        diffSum += diff//4
            tmpMatrix[r][c] = matrix[r][c]+diffSum
    matrix = [row[:]for row in tmpMatrix]

    # 온도 감소
    for r in range(R):
        for c in range(C):
            if r*c*(R-r-1)*(C-c-1)==0:
                matrix[r][c] = max(matrix[r][c]-1,0)

    # 초콜릿 먹기
    chocoCnt += 1
    if 100<chocoCnt:break

    # 온도 검사
    flag = 1
    for r,c in checkArr:
        if matrix[r][c]<K:
            flag = 0
            break
    if flag:
        break

print(min(chocoCnt,101))