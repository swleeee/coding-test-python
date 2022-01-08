import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    dp[0][0], dp[1][0] = array[0][0], array[1][0]

    if n>1:
        for j in range(1, n):
            if j==1:
                dp[0][j] = dp[1][j-1] + array[0][j]
                dp[1][j] = dp[0][j-1] + array[1][j]
            else:
                dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + array[0][j]
                dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + array[1][j]

    # print("n | array | dp : ", n, array, dp)
    # print("dp : ", dp)
    print(max(max(dp[0]), max(dp[1])))


### 괜찮은 풀이
t = int(input())
for _ in range(t):
    n = int(input())
    cache = [[0] + list(map(int, input().split())) for _ in range(2)]

    for i in range(2, n + 1, 1):
        cache[0][i] += max(cache[1][i - 2], cache[1][i - 1])
        cache[1][i] += max(cache[0][i - 2], cache[0][i - 1])

    print(max(cache[0][n], cache[1][n]))
