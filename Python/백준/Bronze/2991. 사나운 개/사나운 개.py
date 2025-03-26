I=lambda:map(int,input().split())
a,b,c,d=I()
for i in I():print((~-i%(a+b)<a)+(~-i%(c+d)<c))