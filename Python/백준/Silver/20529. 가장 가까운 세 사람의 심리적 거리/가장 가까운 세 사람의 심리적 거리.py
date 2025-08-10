from collections import Counter
input = open(0).readline

def f(x,y):
    return len({*x,*y})-4

for _ in range(int(input())):
    input()
    count = Counter(input().split())

    if 3<=max(count.values()):
        print(0)
        continue
    
    mbti = []
    for k,v in count.items():
        mbti += [k]*min(v,2)
    n=len(mbti)
    ans = 8

    for i in range(n):
        A = mbti[i]
        for j in range(i+1,n):
            B = mbti[j]
            for k in range(j+1,n):
                C = mbti[k]
                dist = f(A,B)+f(B,C)+f(A,C)
                if dist<ans:
                    ans = dist 
    print(ans)