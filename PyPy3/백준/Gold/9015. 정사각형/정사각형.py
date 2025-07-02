import sys
input = sys.stdin.readline

OFFSET = 10000

def pointToHash(x,y):
    return (x+OFFSET) + (y+OFFSET) * OFFSET * 10

def check(x,y):
    if -OFFSET <= x <= OFFSET >= y >= -OFFSET:
        return pointToHash(x,y)
    return -1

def solve():
    N = int(input())
    P = []
    H = set()

    result = 0

    for i in range(N):
        x,y = map(int,input().split())
        P += [[x,y]]
        h = pointToHash(x,y)
        H.add(h)
    
    for i in range(N-1):
        x1,y1 = P[i]
        for j in range(i+1,N):
            x2,y2 = P[j]
            dx = x1-x2
            dy = y1-y2

            area = dx*dx + dy*dy

            if area <= result:continue

            x3_1 = x2-dy
            x3_2 = x2+dy
            y3_1 = y2+dx
            y3_2 = y2-dx

            x4_1 = x1-dy
            x4_2 = x1+dy
            y4_1 = y1+dx
            y4_2 = y1-dx

            if check(x3_1,y3_1) in H and check(x4_1,y4_1) in H or check(x3_2,y3_2) in H and check(x4_2,y4_2) in H:
                result = max(result, area)
    print(result)

T=int(input())
for _ in range(T):
    solve()