import sys
input = sys.stdin.readline

# n = int(input())
# maps = [list(map(str, input().split())) for _ in range(n)]

# data = [[0] * n for _ in range(n)]

# print("maps | data : ", maps, data)

# result = True

# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def watch(x, y, d):
#     global result
#     if d == -1:
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx >= 0 and nx < n and ny >= 0 and ny < n:
#                 if data[nx][ny] == 'X':
#                     watch(nx, ny, i)
#                 elif data[nx][ny] == 'S':
#                     result = False
#                     break
#                 else:
#                     continue
#     else:
#         nx = x + dx[d]
#         ny = y + dy[d]

#         if nx >= 0 and nx < n and ny >= 0 and ny < n:
#             if data[nx][ny] == 'X':
#                 watch(nx, ny, d)
#             elif data[nx][ny] == 'S':
#                 result = False
                        

# def dfs(count):
#     global result
#     if count == 3:
#         result = True
#         for i in range(n):
#             for j in range(n):
#                 data[i][j] = maps[i][j]

#         for i in range(n):
#             for j in range(n):
#                 if data[i][j] == 'T':
#                     watch(i, j, -1)

#     else:
#         for i in range(n):
#             for j in range(n):
#                 if maps[i][j] == 'X':
#                     maps[i][j] = 'O'
#                     count += 1                    

#                     dfs(count)
#                     if result == True:
#                         break                    

#                     maps[i][j] = 'X'
#                     count -= 1


# dfs(0)
# print("result : ", result)



### 풀이
from itertools import combinations

n = int(input()) # 복도의 크기
board = [] # 복도 정보 (N x N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))

    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
        
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))

# 특정 방향으로 감시를 진행(학생 발견 : True, 학생 미발견 : False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y >= n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1

    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1

    return False


# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False


find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    print("data : ", data)
    # 장애물 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break

    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('No')