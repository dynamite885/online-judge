for a,b,c,d in map(lambda x:map(int,x.split()),[*open(0)][:-1]):
 A=B=C=D=t=0
 while[a,b,c,d]!=[A,B,C,D]:t+=1;A,B,C,D=a,b,c,d;a,b,c,d=map(abs,[A-B,B-C,C-D,D-A])
 print(t-2)