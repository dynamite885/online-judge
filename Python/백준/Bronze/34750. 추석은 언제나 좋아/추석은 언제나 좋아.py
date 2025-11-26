n=int(input())
m=n//20
if n<100000:print(m,m*19)
elif n<500000:print(m*2,m*18)
elif n<1000000:print(m*3,m*17)
else:print(m*4,m*16)