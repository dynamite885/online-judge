n=r=len(s:=input())
while r>n/r or n%r>0:r-=1
print(''.join(s[i::r]for i in range(r)))