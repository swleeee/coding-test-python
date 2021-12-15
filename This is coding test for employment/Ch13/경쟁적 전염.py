import sys
input = sys.stdin.readline

# N, K = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(N)]

# S, X, Y = map(int, input().split())



# loc_list = [0] * N


# for i in range(N):
#     for j in range(N):
#         if data[i][j] != 0:
#             loc_list[data[i][j]-1] = (i,j)


# print("loc_list", loc_list)

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def dfs(x, y, count):
#     print("x, y", x, y)

#     for i in range(count):
#         for j in range(4):
#             nx = x + dx[j]
#             ny = y + dy[j]

#             if (nx >= 0 and nx < N and ny >=0 and ny < N):
#                 if data[nx][ny] != data[x][y]:
#                     if data[nx][ny] == 0:
#                         data[nx][ny] = data[x][y]                    
#                         dfs(nx, ny, count-1)
#                 else:
#                     dfs(nx, ny, count-1)
#     # if S == 0:

# s = S

# while(s > 0):
#     print("s S", s, S)
#     for case in loc_list:
#         dfs(case[0], case[1], S-s+1)
#     s-=1

# print("data", data)

# print(data[X-1][Y-1])


### 풀이
from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
            data.append((graph[i][j], 0, i, j))


print("data 전 : ", data)
# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
print("data 후 : ", data)
q = deque(data)

print("q : ", q)

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# bfs
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지났거나, 큐가 빌 때까지 반복
    if s == target_s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x - 1][target_y-1])


