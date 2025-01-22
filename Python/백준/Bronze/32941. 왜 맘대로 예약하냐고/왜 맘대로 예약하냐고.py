t,x=map(int,input().split())
n=int(input())
flag=1
for i in range(n):
    k=int(input())
    *a,=map(int,input().split())
    if x not in a:flag=0
print("YNEOS"[1-flag::2])