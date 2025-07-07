A,a,B,b,P=map(int,input().split())
f=A+B<=P or A<=b<B<=P or B<=a<A<=P
print('YNeos'[1-f::2])