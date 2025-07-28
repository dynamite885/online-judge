def f(s):
    r=[]
    t=''
    for c in s:
        if'1'<c<':':r+=[t]*(int(c)-1)
        else:r+=[c]
        t=c
    return r
s=input()
x,y=s.split('+')
y,z=y.split('=')
R=range(1,11)
for i in R:
    for j in R:
        left=sorted([*f(x*i),*f(y*j)])
        for k in R:
            if left==sorted(f(z*k)):exit(print(i,j,k))