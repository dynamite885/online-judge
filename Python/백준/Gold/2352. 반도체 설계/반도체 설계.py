n=int(input())
a=[*map(int,input().split())]
r=[]

for x in a:
    p=0
    q=len(r)
    while p<q:
        m=(p+q)//2
        if r[m]<x:
            p=m+1
        else:
            q=m
    if q==len(r):
        r+=[x]
    else:
        r[q]=x

print(len(r))