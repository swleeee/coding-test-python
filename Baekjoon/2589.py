import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
# maps = [list(map(str, input())) for _ in range(N)]
# copy_maps 

maps = []
# copy_maps = []

# treasure = []

for i in range(N):
    maps.append(list(map(str, input().rstrip())))
    # copy_maps.append(maps[i][:])
    # for j in range(M):
    #     if maps[i][j] == 'L':
    #         treasure.append((i, j))

    # for j in range(M):

# print("maps : ", maps)
# print("copy_maps : ", copy_maps)
# print("treasure : ", treasure)

# print("aaa : ", list(combinations(treasure, 2)))
# maps[0][0] = 'X'

# print("copy_maps : ", copy_maps, maps)
# print("maps : ", maps)

# count = 0
# min_value = 10**4
result = 0

q = deque()


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    # global count
    # global min_value
    # maps[x][y]
    
    q.append((x, y))
    # maps[x][y] = 'W'
    count = [[0]*M for _ in range(N)]
    count[x][y] = 1 

    c = 0
    

    while q:        
        # print("q : ", q)
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == "L" and count[nx][ny] == 0:
                # c += 1
                    count[nx][ny] = count[x][y] + 1
                    c = max(c, count[nx][ny])
                    q.append((nx, ny))
                # print("count :", nx, ny, c)
                
    return c-1


for i in range(N):
    for j in range(M):
        if maps[i][j] == "L":
            result = max(result, bfs(i, j))

print(result)