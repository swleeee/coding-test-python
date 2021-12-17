import sys
input = sys.stdin.readline
from collections import deque

# N = 5 
board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0,0,0,0,0]]
# robot = [(0, 0), (0, 1)]


# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def solution(board):
#     q = deque()
#     q.append(robot)

#     while q:
#         left, right = q.popleft()

#         for i in range(4):
#             left[0] += dx[i]
#             left[1] += dy[i]
#             right[0] += dx[i]
#             right[1] += dy[i]

#             if 0 <= left[0] < N and 0 <= right[0] < N and 0 <= left[1] < N and 0 <= right[1] < N and 


### 풀이

def get_next_pos(pos, board):
    next_pos = [] # 반환 결과(이동 가능한 위치들)
    pos = list(pos) # 현재 위치 정보를 리스트로 변환(집합 -> 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]

        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})

    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
            if board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})

    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos

def solution(board):
    # 맵의 외각에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    # BFS
    q = deque()
    visited=[] 
    pos = {(1,1), (1,2)} # 시작 위치 설정
    q.append((pos, 0)) # 큐에 삽입한 뒤에
    visited.append(pos) # 방문 처리

    while q:
        pos, cost = q.popleft()
        if (n,n) in pos:
            return cost

        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)

    return 0


print(solution(board))