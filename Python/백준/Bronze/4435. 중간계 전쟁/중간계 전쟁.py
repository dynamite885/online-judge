I=lambda:map(int,input().split())
for i in range(int(input())):
 a,b,c,d,e,f=I()
 A,B,C,D,E,F,G=I()
 x=a+2*b+3*c+3*d+4*e+10*f
 y=A+2*B+2*C+2*D+3*E+5*F+10*G
 print(f"Battle {i+1}: {['No victor on this battle field','Good triumphs over Evil','Evil eradicates all trace of Good'][(x>y)-(x<y)]}")