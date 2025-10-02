k=[1,3,0]
a=b=c=0
for i,j in zip(input()[::2],input()[::2]):a+=k[t:=(j<i)-(i<j)];b+=k[-t];c=t or c
print(a,b,'DAB'[(b<a)-(a<b)or c])