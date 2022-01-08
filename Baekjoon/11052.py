import sys
input = sys.stdin.readline

# n = int(input())
# array = list(map(int, input().split()))
# dp = [0] * 10000
# dp[0] = array[0]

# # if n >= 2:
#     # dp[1] = max(dp[0] * 2, array[1])

# for i in range(0, n//2):
#     for j in range(i, n):
#         # if i + j == n:
#         if i+j+1 < n:
#             dp[i+j+1] = max(dp[i] + dp[j], array[i+j+1], dp[i+j+1]) 

#     # print("dp : ", dp[:n])
    
# # print("dp : ", dp[:n])
# print(dp[n-1])
    


###### 괜찮은 풀이

n = int(input())
card = [0]
card += list(map(int,input().split()))

dp = [0] * (n+1)
dp[1] = card[1]
dp[2] = max(card[2], card[1] * 2)

for i in range(3, n+1):
    dp[i] = card[i]
    for j in range(1, i//2 +1):
        dp[i] = max(dp[i], dp[j]+ dp[i-j])
print(dp[n])