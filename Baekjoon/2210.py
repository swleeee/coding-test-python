import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

data = [list(map(str, input().split())) for _ in range(5)]

# print(data)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = []
word = ""

def dfs(x, y, word):
    global result
    # print("x, y", x, y)

    # word += data[x][y]
    
    if len(word) == 6:
        if word not in result:
            result.append(word) 
        # print("result1", result, x, y)
        # word = ""

        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # print("nx, ny", nx, ny)

        if (nx >= 0 and nx < 5 and ny >= 0 and ny < 5):
            dfs(nx, ny, word + data[nx][ny])
    


for i in range(5):
    for j in range(5):
        # print("i, j", i, j)
        dfs(i, j, data[i][j])
        # print("count", count)


# print("word", word)
# print("result", result)
print(len(result))