a=[[*map(int,input().split()),i+1]for i in range(int(input()))]
a.sort()
for i,j in zip(a,a[1:]):print(i[2],j[2])