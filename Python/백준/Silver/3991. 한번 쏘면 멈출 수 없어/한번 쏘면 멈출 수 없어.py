h,w,c,*a=map(int,open(0).read().split())
s=''
while c:s+=str(c)*a.pop();c-=1
for i in range(h):print(s[i*w:i*w+w][::[1,-1][i%2]])