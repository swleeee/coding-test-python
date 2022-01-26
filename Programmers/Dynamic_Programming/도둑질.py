def solution(money):
    answer = 0
    l = len(money)
    dp = [[0] * l for _ in range(2)]
    
    dp[0][0], dp[1][0], dp[0][1], dp[1][1] = money[0], 0, max(money[0], money[1]), money[1]
    
    for i in range(2, l):
        if i == l-1:
            dp[0][i] = max(dp[0][i-2], dp[0][i-1])
            # dp[1][i] = max(money[i] + dp[1][i-2], dp[1][i-1])
        else:
            dp[0][i] = max(money[i] + dp[0][i-2], dp[0][i-1])
        dp[1][i] = max(money[i] + dp[1][i-2], dp[1][i-1])

    print("dp : ", dp)
    answer = max(dp[0][l-1], dp[1][l-1])

    return answer

# money = [1, 1, 4, 1, 4]
## 8

# money =  [1, 2, 3, 1]
## 4

money = [1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000]
# 3000

# money = [1000, 1, 0, 1, 2, 1000, 0]
## 2001

print(solution(money))
