r,b=map(int,input().split())
for i in range(2,r//2+1):
    if r+b==~i*~(r//2-i):
        exit(print(r//2-i+1,i+1))