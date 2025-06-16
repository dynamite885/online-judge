n=int(input())
arr=[input()for _ in range(n)]
for i in range(n):
    for j in range(n):
        c=arr[i][j]
        if c=='.':continue
        if j+2<n and c==arr[i][j+1] and c==arr[i][j+2]:
            exit(print(c))
        if i+2<n and c==arr[i+1][j] and c==arr[i+2][j]:
            exit(print(c))
        if i+2<n and j+2<n and c==arr[i+1][j+1] and c==arr[i+2][j+2]:
            exit(print(c))
        if i+2<n and j-2>=0 and c==arr[i+1][j-1] and c==arr[i+2][j-2]:
            exit(print(c))
print('ongoing')