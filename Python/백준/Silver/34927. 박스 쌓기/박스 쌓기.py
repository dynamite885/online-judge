a=b=0
for i in sorted(map(int,[*open(0)][1].split())):
 if a<=i:a+=i;b+=1
print(b)