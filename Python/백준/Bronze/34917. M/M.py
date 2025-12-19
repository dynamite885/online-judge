for n in[*map(int,open(0))][1:]:
    for i in range(n):
        for j in range(n):
            print(end='.#'[j==0 or j==n-1 or n//2-i==abs(n//2-j)::2])
        print()