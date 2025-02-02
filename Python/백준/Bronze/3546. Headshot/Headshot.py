*s,=map(int,input())
t=s[-1]
a=b=0
for i in s:
 if t<1:a+=i;b+=1-i
 t=i
print("RESOQHTUOAAOTLTE"[1+(0<a<b)-(a>b)::3])