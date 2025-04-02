while 1:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:break
    if a-b==b-c:print("AP",c+b-a)
    else:print("GP",c*b//a)