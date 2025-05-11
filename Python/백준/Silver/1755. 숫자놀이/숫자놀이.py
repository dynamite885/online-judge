a=["zero","one","two","three","four","five","six","seven","eight","nine"]
m,n=map(int,input().split())
def f(x):
    s=''
    for i in str(x):
        s+=a[int(i)]
    return s
t=sorted((i for i in range(m,n+1)),key=lambda x:f(x))
for i in range(len(t)):
    print(t[i],end=' \n'[i%10==9])