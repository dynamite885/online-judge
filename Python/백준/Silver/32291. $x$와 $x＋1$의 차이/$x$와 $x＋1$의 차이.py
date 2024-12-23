x=int(input())+1
a={1}
for i in range(1,int(x**.5+1)):
    if x%i==0:a|={i,x//i}
print(*sorted([*a])[:-1])