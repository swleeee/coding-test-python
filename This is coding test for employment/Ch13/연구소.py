# import sys
# from itertools import combinations
# from collections import deque
# input = sys.stdin.readline

# N, M = map(int, input().split())
# maps = [list(map(int, input().split())) for _ in range(N)]  
# virus = []
# empty = []
# empty_value = 0

# # print(maps)
# current_maps = []

# for i in range(N):
#     for j in range(M):
#         if maps[i][j] == 2:
#             virus.append((i, j))
#         elif maps[i][j] == 0:
#             empty.append((i, j))
#             empty_value += 1

# # print("virus", virus)
# # print("empty", empty)
# # print("empty_list", list(combinations(empty, 3)))
# empty_list = list(combinations(empty, 3))
# # print("current_maps", current_maps)

# q = deque()
# max_value = 0
# value = 0

# def check(x, y):
#     global current_maps
#     global q
#     global value

#     if(x < N and y < M and x > -1 and y > -1):
#         if(current_maps[x][y] == 0):
#             current_maps[x][y] = 2
#             value += 1
#             q.append((x, y))
#             return True
#         else:
#             return False        
#     return False


# def bfs():
#     global value
    
#     for sub_virus in virus:
#         # print("sub_virus", sub_virus)
#         q.append(sub_virus)
#         while q:
#             now = q.popleft()
#             # print("now", now, now[0], now[1])
#             # print(check(now[0]+1, now[1], value))
#             check(now[0]+1, now[1])                
#             check(now[0], now[1]-1)
#             check(now[0]-1, now[1])
#             check(now[0], now[1]+1)            
#             # print("q", q, value)

# def calc(case):
#     global max_value
#     global empty_value
#     global value 
#     # print("case", case)
#     for sub_case in case:
#         # print("sub_case", sub_case)
#         # print(sub_case[0], sub_case[1])
#         current_maps[sub_case[0]][sub_case[1]] = 1        
#     # print("current", current_maps)
#     value = 0
#     bfs()
#     # print("aaaaaaaaaaaaaaaa", max_value, empty_value, value)
#     max_value = max(max_value, empty_value - value - 3)
#     # print("bbbbbbbbbbbbbbbb", max_value)

# for case in empty_list:
#     # print("case", case)    
#     current_maps=[]
#     current_maps = [item[:] for item in maps]
#     # print("ddd", current_maps)        
#     calc(case)                    

# print(max_value)





### 풀이
n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# DFS를 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        
        # d안전 영역의 최댓값 계산
        result = max(result, get_score())
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1

                dfs(count)

                data[i][j] = 0
                count -= 1


dfs(0)
print(result)




        