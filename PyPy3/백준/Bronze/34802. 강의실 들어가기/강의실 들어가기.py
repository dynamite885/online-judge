def f():
    a,b,c = map(int,input().split(':'))
    return a*3600+b*60+c

x = f()
y = f()
t, k = map(int,input().split())
print(+(t//100*(100-k)<=y-x))