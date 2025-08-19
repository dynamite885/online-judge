A=B=0
for i in[*open(0)][1:]:
    a,b=map(int,i.split())
    A+=a>b
    B+=a<b
print(A,B)