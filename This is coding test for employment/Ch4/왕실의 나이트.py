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
s = list(input())
move_types=['L', 'R', 'U', 'D']
dy = [0, 0, -2, 2]
dx = [-2, 2, 0, 0]

# s[0] = ord(s[0])-96
# s[1] = int(s[1])
x, y = ord(s[0])-96, int(s[1])
# print(s)
# print(ord(s[0]))

count = 0
for i in range(len(move_types)):
    if(dx[i] != 0):
        if(x + dx[i] > 0 and x + dx[i] < 8):
            if(y - 1 > 0):
                count +=1
            if(y + 1 < 8):
                count +=1
        else:
            continue
    if(dy[i] != 0):
        if(y + dy[i] > 0 and y + dy[i] < 8):
            if(x - 1 > 0):
                count +=1
            if(x + 1 < 8):
                count +=1
        else:
            continue

print(count)
    

## 풀이
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a'))+1

# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row <=8 and next_column >= 1 and next_column <= 8:
#         result += 1

# print(result)



end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END") 