import sys
input = sys.stdin.readline

# n = int(input())
# array = [0] * 10001
# dp = [0] * 10001

# for i in range(n):
#     array[i] = int(input()) 

# dp[0] = array[0]
# dp[1] = array[0] + array[1]
# dp[2] = max(array[0], array[1]) + array[2]

# for i in range(3, n):
#     # print("aaa : ", i, max(dp[0:i-2]))
#     # a = max(dp[0:i-2])
#     # b = max(dp[0:i-3])
#     # b = max(dp[0:0])
#     # print("a | b : ", a, b)
#     # dp[i] = max(a, b)
#     dp[i] = max(max(dp[:i-1]), max(dp[:i-2]) + array[i-1]) + array[i]
#     # dp[i] = max(dp[i-2], dp[i-3] + array[i-1]) + array[i]
#     # print("aaa : ", i, dp[0:n])

# # print("dp : ", dp)
# print(max(dp))




### 괜찮은 풀이
import sys
input = sys.stdin.readline

n = int(input())
wines = [0] + [int(input()) for _ in range(n)] + [0]

dp = [0] * (n + 2)
dp[1] = wines[1]
dp[2] = dp[1] + wines[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + wines[i - 1] + wines[i], dp[i - 2] + wines[i])
    print("AAA : ", i, dp[i-1], dp[i])
    dp[i] = max(dp[i - 1], dp[i])

print("dp : ",dp)
print(dp[n])