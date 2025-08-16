input=open(0).readline

n,k,d = map(int,input().split())
rules = []
for _ in range(k):
    a,b,c = map(int,input().split())
    rules += [[a,b,c]]

def getSum(idx):
    sum = 0
    for a,b,c in rules:
        sum += max(min(b,idx)-a, -1) // c + 1
    return sum

left = 1
right = n

while left<right:
    mid = left + right >> 1
    sum = getSum(mid)
    if sum < d:
        left = mid + 1
    elif sum >= d:
        right = mid
print(left)