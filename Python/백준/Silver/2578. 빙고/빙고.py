arr=[[*map(int,input().split())]for _ in range(5)]
x=0

def check():
    cnt=[0]*12
    for i in range(5):
        for j in range(5):
            if arr[i][j]==-1:
                cnt[i]+=1
                cnt[5+j]+=1
                if i==j:
                    cnt[10]+=1
                if i+j==4:
                    cnt[11]+=1
            if 3<=cnt.count(5):
                exit(print(x))

order=sum([[*map(int,input().split())]for _ in range(5)],[])

for n in order:
    x+=1
    for i in range(5):
        for j in range(5):
            if n==arr[i][j]:
                arr[i][j]=-1
    check()