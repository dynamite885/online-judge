rows = [
    [[0,0,0],
    [0,0,0],
    [0,0,0]],

    [[1,1,1],
    [0,0,0],
    [0,0,0]],

    [[0,0,0],
    [1,1,1],
    [0,0,0]],

    [[0,0,0],
    [0,0,0],
    [1,1,1]]
]
cols = [
    [[0,0,0],
    [0,0,0],
    [0,0,0]],

    [[1,0,0],
    [1,0,0],
    [1,0,0]],

    [[0,1,0],
    [0,1,0],
    [0,1,0]],

    [[0,0,1],
    [0,0,1],
    [0,0,1]]
]
x1 = [
    [[0,0,0],
    [0,0,0],
    [0,0,0]],

    [[1,0,0],
    [0,1,0],
    [0,0,1]]
]
x2 = [
    [[0,0,0],
    [0,0,0],
    [0,0,0]],

    [[0,0,1],
    [0,1,0],
    [1,0,0]]
]

def sumarrs(*arrs):
    r = [[0,0,0]for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for a in arrs:
                r[i][j] += a[i][j]
                r[i][j] %= 2
    return r

def check(a):
    a = sum(a,[])
    return +(all(a)) or 1 - any(a)

def solve(a):
    for i in range(4):
        for j in range(4):
            for k in range(2):
                for l in range(2):
                    b = rows[i]
                    c = cols[j]
                    d = x1[k]
                    e = x2[l]
                    r = sumarrs(a,b,c,d,e)
                    if check(r):
                        print(sum(f!=0 for f in[i,j,k,l]))
                        return
    print(-1)

t = int(input())

for _ in range(t):
    a = [[*map(lambda x:"HT".find(x), input().split())]for _ in range(3)]
    solve(a)