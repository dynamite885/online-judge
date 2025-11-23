r=s=t=0
for i in map(int,[*open(0)][1].split()):s=1+s*(t<i);r+=s;t=i
print(r)