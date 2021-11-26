import time 
import psutil
start_time = time.time()
print(start_time)

def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")


## 
# n, m = map(int, input().split())
# x, y, d = map(int, input().split())
# maps = []
# maps = [0] * n
# for i in range(n):
        
#     # for j in range(m):
#     maps[i] = list(map(int, input().split()))
#     # print("maps", i, maps)
# # print(maps)

# count = 0
# sub_count = 0

# while True:
#     if(maps[x][y] == 0):
#         maps[x][y] = 1
#         sub_count = 0
#         count += 1
#     else:
#         sub_count += 1

#     if(sub_count == 4):    
#         break

#     if(d==0):
#         if(maps[x-1][y] == 0):
#             x -= 1            
#         else:
#             d = 3
#     elif(d==3):
#         if(maps[x][y-1] == 0):
#             y-=1
#         else:
#             d = 2
#     elif(d==2):
#         if(maps[x+1][y] == 0):
#             x+=1
#         else:
#             d = 1
#     else:
#         if(maps[x][y+1] == 0):
#             y+=1
#         else:
#             d = 0
    

# print(count)
## 풀이
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X, Y, 방향 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction # direction 변수가 함수 바깥에서 선언된 전역변수 이기 때문에 global 사용
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x, y = nx, ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)

end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END") 