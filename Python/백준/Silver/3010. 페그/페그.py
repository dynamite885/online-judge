*a,=open(0)
print(sum((i+j).count('oo.')+(i+j).count('.oo')for i,j in zip(a,map(''.join,zip(*a)))))