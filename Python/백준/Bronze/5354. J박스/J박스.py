for _ in' '*int(input()):
    n=int(input())
    for i in range(n):
        for j in range(n):
            print(end='J#'[i*j*(n-i-1)*(n-j-1)<1])
        print()
    print()