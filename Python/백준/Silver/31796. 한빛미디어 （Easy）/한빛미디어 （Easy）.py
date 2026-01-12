c=t=0
for i in sorted(map(int,[*open(0)][1].split()))[::-1]:
    if t<1 or i<=t//2:c+=1;t=i
print(c)