input=open(0).readline
w='S P R S'
l='S R P S'
t=int(input())
for _ in range(t):
    n=int(input())
    k=0
    for _ in range(n):
        s=input().strip()
        k+=s in w
        k-=s in l
    print(['TIE','Player 2','Player 1'][(k<0)-(k>0)])