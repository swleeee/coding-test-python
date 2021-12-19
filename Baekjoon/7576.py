import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())

# box = [list(map(int, input().split())) for _ in range(N)]

tomato = deque()
# empty = []

box = []
for i in range(N):
    box.append(list(map(int, input().split())))

    for j in range(M):
        if box[i][j] == 1:
            tomato.append((i, j, 0))
        # elif box[i][j] ==


# print("box : ", box)
# print("tomato : ", tomato)



dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# count = 0
result = 0

while tomato:
    x, y, count = tomato.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            tomato.append((nx, ny, count+1))
            box[nx][ny] = 1

    result = count

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            result = -1
            break

# print("result : ", result)
print(result)


    
    
