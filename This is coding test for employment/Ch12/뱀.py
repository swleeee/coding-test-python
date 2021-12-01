

# n = int(input())
# maps = [[0] * n for _ in range(n)]
# k = int(input())
# apple_list = [list(map(int, (input().split()))) for _ in range(k)]
# for i in range(k):
#     # apple = list(map(int, input().split()))
#     # print(apple_list[i][0])
#     maps[apple_list[i][0]-1][apple_list[i][1]-1] = 2
# a = int(input())
# move_list = [list(map(str, (input().split()))) for _ in range(a)]
# move_list= dict(move_list)

# # print(apple_list)
# maps[0][0] = 1
# time = 0 
# print(maps)
# print(move_list)
# length = 1
# location_list = [[0, 0]]
# x, y = 0, 0


# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]

# direction = 2

# # print(str(3) in move_list)
# # print(move_list.get(str(3)))


# def check_direction(d):
#     global direction
#     print("c", direction)

#     if(d == "L"):
#         direction -= 1
#     else:
#         direction += 1

#     if(direction == -1):
#         direction = 3
#     if(direction == 4):
#         direction = 0;

# while True:
#     print("b", time, maps, x, y, direction)
#     if(str(time) in move_list):
#         check_direction(move_list.get(str(time)))


#     print("d", x, y, direction)


#     nx = x+dx[direction]
#     ny = y+dy[direction]
#     time += 1

#     print("e", nx, ny, direction)
    

#     if((nx > n-1 or nx < 0) or (ny > n-1 or ny < 0)):
#         break


#     if(maps[nx][ny] == 2):
#         length += 1
#         location_list.append([nx, ny])
#         maps[nx][ny] = 1

#     elif(maps[nx][ny] == 1):
#         break
#     else:
#         location_list.append([nx, ny])
#         maps[location_list[0][0]][location_list[0][1]] = 0
#         del location_list[0]
#         maps[nx][ny] = 1
    

#     x = nx
#     y = ny

# print(time)








### 풀이
n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보 (꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0

            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))

        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break

        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
