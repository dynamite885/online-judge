a=eval(input().replace(*' *'))
b=pow(3,a//3-1,m:=10**9+7)
print([b*[3,4,6][a%3]%m,1][a<2])