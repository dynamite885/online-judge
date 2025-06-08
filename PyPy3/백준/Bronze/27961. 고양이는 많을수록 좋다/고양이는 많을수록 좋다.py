b=bin(n:=int(input()))
print(len(b)-2+('1'in b[3:])-(n==0))