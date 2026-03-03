n=int(input())
s=m=l=0
for _ in range(n):
    z,k=input().split()
    k=int(k)
    if z=="S":s+=k
    elif z=="M":m+=k
    else:l+=k
print(-(s//-6+m//-8+l//-12))