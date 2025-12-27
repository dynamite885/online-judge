a,b=map(int,input().split(':'))
c,d=map(int,input().split(':'))
x=a*60+b
y=c*60+d
t=abs(x-y)
print(min(720-t,t)*6)