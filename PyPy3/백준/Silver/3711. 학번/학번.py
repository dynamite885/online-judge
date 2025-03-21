for _ in' '*int(input()):
    g=int(input())
    a=[]
    for _ in' '*g:a+=[int(input())]
    m=g
    while 1:
        b={*[i%m for i in a]}
        if len(b)==g:break
        m+=1
    print(m)