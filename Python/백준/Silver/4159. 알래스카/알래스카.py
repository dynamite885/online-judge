while n:=int(input()):
    a=sorted([int(input())for _ in' '*n])
    b=[]
    f=t=0
    for i in a:b+=[2844-i]
    a+=b
    a.sort()
    for i in a:
        if 200<i-t:f=1
        t=i
    print('IM'*f+'POSSIBLE')