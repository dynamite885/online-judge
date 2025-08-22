for i in[*open(0)][:-1]:
    g,t,a,d=map(int,i.split())
    p=g*t*~-t//2
    q=g*a+d
    r=2**(q-1).bit_length()
    print(f"{g}*{a}/{t}+{d}={p+r-1}+{r-q}")