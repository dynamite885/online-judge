a=[8*[0]for _ in' '*8]
R='12345678'
C='ABCDEFGH'
dr=[-1,-1,-1,0,0,1,1,1]
dc=[-1,0,1,-1,1,-1,0,1]
d=['LB','B','RB','L','R','LT','T','RT']
k,s,n=input().split()
n=int(n)
a[R.index(k[1])][C.index(k[0])] = 1
a[R.index(s[1])][C.index(s[0])] = 2
for _ in' '*n:
    nd=d.index(input())
    kr,kc=R.index(k[1]),C.index(k[0])
    sr,sc=R.index(s[1]),C.index(s[0])
    nr=kr+dr[nd]
    nc=kc+dc[nd]
    if 0<=nr<8 and 0<=nc<8:
        if a[nr][nc] == 2:
            nr=sr+dr[nd]
            nc=sc+dc[nd]
            if 0<=nr<8 and 0<=nc<8 and a[nr][nc] == 0:
                a[nr][nc] = 2
                a[sr][sc] = 1
                a[kr][kc] = 0
                k = C[sc]+R[sr]
                s = C[nc]+R[nr]
        else:
            a[nr][nc] = 1
            a[kr][kc] = 0
            k = C[nc]+R[nr]
print(k)
print(s)