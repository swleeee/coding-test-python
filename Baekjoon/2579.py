import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

dp = [0] * (n+3)
array.reverse()

print("array | dp : ", array, dp)

dp[0] = array[0]
# dp[1] = array[1]

for i in range(1, n):
    if i==1 or i==2:
        dp[i] = array[i] + dp[0]
    else:
        if dp[i] != -1:
            # dp[i] = array[i] + max(dp[i-1], dp[i-2])
            if dp[i-1] > dp[i-2]:
                dp[i] = array[i] + dp[i-1]
                dp[i+1] = -1
            else:
                dp[i] = array[i] + dp[i-2]
                dp[i+1] = 0
                dp[i+2] = -1
            
            
        else:
            dp[i] = array[i] + dp[i-2]

print("dp : ", dp)

print(max(dp))