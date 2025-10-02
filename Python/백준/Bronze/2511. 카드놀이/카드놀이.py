a=b=c=0
for i,j in zip(input()[::2],input()[::2]):a+=[1,3,0][t:=(j<i)-(i<j)];b+=[1,3,0][-t];c=t or c
print(a,b,'DAB'[(b<a)-(a<b)or c])