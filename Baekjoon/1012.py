import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

T = int(input())
field = [0] * T
for i in range(T):
    N, M, K = map(int, input().split())
    field[i] = [[0] * M for _ in range(N)]
    for j in range(K):
        x, y = map(int, input().split())
        field[i][x][y] = 1
    # field[i] = [list(map(int, input().split())) for _ in range(K)]

# print("field : ", field)

result = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(t, x, y):
    global result
    # print("field[t] : ", field[t])
    if field[t][x][y] == 1:
        field[t][x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            
            if nx >= 0 and nx < len(field[t]) and ny >= 0 and ny < len(field[t][0]):
                # print("dfs! : ", x, y)
                if(field[t][nx][ny] == 1):
                    dfs(t, nx, ny)
                # result -= 1
        return True
    return False


for t in range(T):
    for i in range(len(field[t])):        
        for j in range(len(field[t][0])):
            # print("ddd", t, len(field[t]), len(field[t][0]))
            # print("count : ", count, i, j)
            if (field[t][i][j]) == 1:
                # print("t | i | j : ", t, i, j)
                result += 1
                dfs(t, i, j)

    # print("result : ", result)
    print(result)
    result = 0