a=[]
while'X'not in(s:=input()):a+=[s]
a.sort()
while'X'not in(s:=input()):
    f=1
    for i in a:
        if sorted(i)==sorted(s):print(i);f=0
    if f:print("NOT A VALID WORD")
    print('******')