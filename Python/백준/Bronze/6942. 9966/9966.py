n,m=map(int,open(0))
c=0
for i in range(n,m+1):
    a=str(i)
    if {*a}&{'2','3','4','5','7'}:
        continue
    b=a[::-1].replace('6','_').replace('9','6').replace('_','9')
    if a==b:
        c+=1
print(c)