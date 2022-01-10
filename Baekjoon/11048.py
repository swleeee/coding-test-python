import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
# print("array | dp : ", array, dp)
# dp[0][0] = array[0][0]

for i in range(n):
    for j in range(m):        
        if i==0 and j==0:
            left_up = 0
            left = 0
            up = 0
        elif i==0 and j!=0:
            left = dp[i][j-1]
            left_up = 0
            up = 0
        elif j==0 and i!=0:
            up = dp[i-1][j]
            left_up = 0
            left = 0
        else:
            left = dp[i][j-1]
            up = dp[i-1][j]
            left_up = dp[i-1][j-1]

        
        dp[i][j] = max(left, up, left_up)  + array[i][j]

# print("dp : ", dp)            
print(dp[n-1][m-1])