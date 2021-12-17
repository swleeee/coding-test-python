import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline

N, M, K = map(int, input().split())

paper = [[0] * M for _ in range(N)]

# print("paper : ", paper)

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    # (2, 0) (4, 4)
    # (1, 4) (3, 0)
    # (1, 0) (3, 4)
    for i in range(N-x2, N-x1):
        for j in range(y1, y2):
            paper[i][j] = 1


# print("paper : ", paper)

# result = [0] * K
result = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0
area = 0


def dfs(x, y):
    global area
    # print("x | y : ", x, y, area)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and paper[nx][ny] == 0:
            paper[nx][ny] = 1
            area += 1
            dfs(nx, ny)
    # return area




for i in range(N):
    for j in range(M):
        # print(i, j, N, M)
        if paper[i][j] == 0:
            count += 1
            paper[i][j] = 1
            area = 1
            dfs(i, j)
            # result[count-1] = area
            result.append(area)
            # print("count | area : ", count, area)

result.sort()

print(count)
for num in result:
    print(num, end=" ")