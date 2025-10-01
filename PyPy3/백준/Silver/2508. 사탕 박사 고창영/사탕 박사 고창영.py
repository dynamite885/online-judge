input=open(0).readline
t=int(input())
for _ in range(t):
    input()
    n,m=map(int,input().split())
    s=[input()for _ in range(n)]+[' '*-~m]
    print(''.join(s).count(">o<")+''.join(sum(zip(*s),())).count("vo^"))