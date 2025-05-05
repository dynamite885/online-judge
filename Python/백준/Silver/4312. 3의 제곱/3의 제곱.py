while n:=int(input()):
    n-=1;r=1
    print(end='{')
    while n:
        i=n%2;n//=2
        if i:
            print(' '+str(r),end='')
            if n:print(end=',')
        r*=3
    print(' }')