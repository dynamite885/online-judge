for _ in' '*int(input()):
    s=input()
    a=''
    for i in s:
        b=s+a
        if b==b[::-1]:print(b);break
        a=i+a