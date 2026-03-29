t=-1
for i in map(int,[*open(a:=0)][1].split()):
    if i-t!=1:a+=i
    t=i
print(a)