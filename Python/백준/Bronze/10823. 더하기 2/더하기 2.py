a=0
s=''
for i in open(0).read():
 if'0'<=i<='9':s+=i
 else:
  if i==',':
   a+=int(s)
   s=''
print(a+int(s))