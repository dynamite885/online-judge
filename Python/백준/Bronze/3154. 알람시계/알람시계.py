t=int(input().replace(':',''))
a=[10,0,1,2,3,4,5,6,7,8]
f=lambda s:s%2400-s%100+s%100%60==t
g=lambda p,q:abs(a[p]//3-a[q]//3)+abs(a[p]%3-a[q]%3)
R=range(10)
x=99
y=-1
for i in R:
    for j in R:
        for k in R:
            for l in R:
                w=g(i,j)+g(j,k)+g(k,l)
                if f(z:=i*1000+j*100+k*10+l)and x>w:
                    y=z
                    x=w
s='%04d'%y
print(s[:2]+':'+s[2:])