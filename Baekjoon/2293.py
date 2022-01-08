import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array = []

for _ in range(n):
    array.append(int(input()))

dp = [0] * (k+1)
# dp = [0 for i in range(k + 1)]
dp[0] = 1

for i in array:
    for j in range(1, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

# print("dp : ", dp)
print(dp[k])