import math
n=int(input())
if n<4:exit(print(n))
print(pow(3,n//3-1,10007)*[3,4,6][n%3]%10007)