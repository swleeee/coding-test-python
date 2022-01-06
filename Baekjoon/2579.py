import sys
input = sys.stdin.readline

n = int(input())
array = [0] * 301
dp = [0] * 301
for i in range(n):
    array[i] = (int(input()))

# array.reverse()



dp[0] = array[0]
dp[1] = array[0] + array[1]
dp[2] = max(array[0] + array[2], array[1] + array[2])

for i in range(3, n):
    dp[i] = max(dp[i-2], dp[i-3] + array[i-1]) + array[i]
# dp[1] = array[1]

# print("array | dp : ", array, dp)
# print("dp : ", dp)
print(dp[n-1])