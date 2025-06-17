n,m = map(int, input().split())
arr = [[*map(int,input().split())]for _ in range(n)]
valueArr = [[[None,None,None]for _ in range(m)] for _ in range(n)]
valueArr[0][0][0] = arr[0][0]
for i in range(n):
    for j in range(m):
        if 0<j:
            valueArr[i][j][0] = max([x for x in valueArr[i][j-1][:2] if x is not None], default=0) + arr[i][j]
        if 0<i:
            valueArr[i][j][1] = max([x for x in valueArr[i-1][j][:3] if x is not None], default=0) + arr[i][j]
    for j in range(m-1,-1,-1):
        if 0<i and j<m-1:
            valueArr[i][j][2] = max([x for x in valueArr[i][j+1][1:3] if x is not None], default=0) + arr[i][j]
print(max([x for x in valueArr[n-1][m-1] if x is not None], default=0))