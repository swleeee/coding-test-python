import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
region = []

max_height = 1
max_area = 0

for i in range(n):
    region.append(list(map(int, input().split())))

    for j in range(n):
        if max_height < region[i][j]:
            max_height = region[i][j]


# print("region | max_height : ", region, max_height)


rain_region = [[0] * n for _ in range(n)]

# print("rain_region : ", rain_region)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    rain_region[x][y] = 0

    q = deque()
    q.append((x, y))

    # count += 1

    while q:
        pos_x, pos_y = q.popleft()

        for i in range(4):
            nx = pos_x + dx[i]
            ny = pos_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and rain_region[nx][ny] == 1:
                q.append((nx, ny))
                rain_region[nx][ny] = 0
                # count += 1



def sink(h):
    for i in range(n):
        for j in range(n):
            if region[i][j] <= h:
                rain_region[i][j] = 0
            else:
                rain_region[i][j] = 1

for h in range(max_height + 1):
    # print("sink : ", h)
    sink(h)
    
    count = 0

    for i in range(n):
        for j in range(n):
            if rain_region[i][j] == 1:
                count += 1
                bfs(i, j)

    max_area = max(max_area, count)

# print("max_area : ", max_area)
print(max_area)

