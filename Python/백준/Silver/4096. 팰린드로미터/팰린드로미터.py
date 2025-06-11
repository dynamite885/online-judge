while'0'<(s:=input()):
    n=int(s)
    l=len(s)
    c=0
    while n!=int(f'{n:0{l}d}'[::-1]):
        n+=1
        c+=1
    print(c)