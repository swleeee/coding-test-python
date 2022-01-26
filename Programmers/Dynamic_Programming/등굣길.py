def solution(m, n, puddles):
    m, n = n, m
    answer = 0
    dp = [[0] * m for _ in range(n)]

    x_pool = m
    y_pool = n

    for x, y in puddles:
        dp[x-1][y-1]= -1
        if x == 1:
            x_pool = min(x_pool, y-1)
        if y == 1:
            y_pool = min(y_pool, x-1)

    for i in range(n):
        for j in range(m):
            if i == 0 or j==0:
                if i >= y_pool or j >= x_pool:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1
                # if dp[i][j] == -1:
                #     dp[i][j] = 0
                # else:
                #     dp[i][j] = 1
                
            else:
                if dp[i][j] == -1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

    print("dp : ", dp)
    answer = dp[n-1][m-1] % 1000000007
    return answer

# m = 4
# n = 3
# puddles = [[2,2]]
## 4

m = 4
n = 3
puddles = [[2,1], [1, 2]]

# m = 4
# n = 5
# puddles = [[3,2], [5,1]]
## 16?


print(solution(m, n, puddles))