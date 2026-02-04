n=int(input())+2
for i in range(n):
    for j in range(n):
        print(end=" @"[i*j*(n-1-i)*(n-1-j)<1])
    print()