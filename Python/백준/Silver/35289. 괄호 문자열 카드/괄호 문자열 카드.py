a,b,c,d,e,f=map(int,input().split())
p=min(b,d)
rb,rd=b-p,d-p
q=min(rb,c//2)+min(rd,a//2)
c-=min(rb,c//2)*2
a-=min(rd,a//2)*2
r=min(a,c)
if max(p,q,r)==0:f=0
print(r*2+p*4+q*4+e*2+f*2)