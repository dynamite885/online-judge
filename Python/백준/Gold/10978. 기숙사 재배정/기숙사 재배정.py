import math
dp=[[0]*21 for _ in range(21)]
dp[0][0] = 1
for i in range(1,21):
    dp[i][0] = dp[i-1][0]*i
    f = math.factorial(i)
    for j in range(1,i-1):
        dp[i][j] = math.comb(i,j)*dp[i-j][-1]
    dp[i][-2] = 1
    dp[i][-1] = f-sum(dp[i][1:-1])

for i in[*open(0)][1:]:
    print(dp[int(i)][-1])