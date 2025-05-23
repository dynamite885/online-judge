n=int(input())
for i in range(n):
    k,w=map(int,input().split())
    c=k
    s1=input()
    for j in range(w-1):
        s2=input()
        t=0
        while not s2.startswith(s1[t:]):t+=1
        s1=s2
        c+=t
    print(c)