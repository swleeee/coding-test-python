# import sys
# input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

# print("graph : ", graph)

count = 0
result = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    area = 1
    graph[x][y] = 2


    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                area += 1
                graph[nx][ny] = 2
                q.append((nx, ny))

            

        # print("pos : ", x, y)

    # print("area : ", area)
    result.append(area)
        



for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count += 1
            bfs(i, j)


print(count)
result.sort()
for c in result:
    print(c)