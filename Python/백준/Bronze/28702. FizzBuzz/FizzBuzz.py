ans=-1
a=input()
b=input()
c=input()
if a<='A':a=int(a);ans=a+3
if b<='A':b=int(b);ans=b+2
if c<='A':c=int(c);ans=c+1
if ans%3==0==ans%5:print('FizzBuzz');exit()
if ans%3==0:print('Fizz');exit()
if 0==ans%5:print('Buzz');exit()
print(ans)