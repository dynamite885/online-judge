while 1:
    a,b=map(int,input().split())
    if a+b<1:break
    cnt=0
    c=0
    while a+b:
        c=(a%10+b%10+c)//10
        a//=10
        b//=10
        cnt+=c
    print(cnt)