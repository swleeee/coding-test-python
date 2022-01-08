import sys
input = sys.stdin.readline

n = int(input())
dp = [[0] * 10 for _ in range(n)]
dp[0] = [1] * 10

for i in range(1, n):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])

# print("dp : ", dp)
print(sum(dp[n-1]) % 10007)


### 괜찮은 풀이
n = int(input())

dp = [[1]*(10) for _ in range(n+1)]

for i in range(2,n+1): # 첫자리 경우 1
    for j in range(1,10): # 0 = 1
        dp[i][j]=dp[i-1][j]+dp[i][j-1]  ### 이 부분!

print(sum(dp[n])%10007)