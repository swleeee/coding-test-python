import sys
input = sys.stdin.readline
from collections import deque

normal_area = []
weakness_area = []


n = int(input())
for i in range(n):
    normal_area.append(list(map(str, input().rstrip())))
    weakness_area.append(normal_area[i][:])
    for j in range(n):
        if weakness_area[i][j] == "G":
            weakness_area[i][j] = "R"


# print("normal_area : ", normal_area)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, graph, color):

    graph[x][y] = 'X'
    q = deque()
    q.append((x, y, color))

    

    while q:
        # print("q : ", q)
        pos_x, pos_y, color = q.popleft()

        for i in range(4):
            nx = pos_x + dx[i]
            ny = pos_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color: 
                graph[nx][ny] = 'X'
                q.append((nx, ny, color))



normal_count = 0
weakness_count = 0

for i in range(n):
    for j in range(n):
        if normal_area[i][j] != 'X':
            normal_count += 1
            bfs(i, j, normal_area, normal_area[i][j])
        if weakness_area[i][j] != 'X':
            weakness_count += 1
            bfs(i, j, weakness_area, weakness_area[i][j])
        

# print("weakness_area : ", weakness_area)
# print("count : ", normal_count, weakness_count)
print(normal_count, weakness_count)