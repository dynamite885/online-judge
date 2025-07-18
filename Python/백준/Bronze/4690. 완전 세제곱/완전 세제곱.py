for a in range(2,101):
    A=a*a*a
    for b in range(2,a-2):
        B=b*b*b
        for c in range(b+1,a-1):
            C=c*c*c
            if A<=B+C:break
            for d in range(c+1,a):
                D=d*d*d
                if A<B+C+D:break
                if A==B+C+D:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")