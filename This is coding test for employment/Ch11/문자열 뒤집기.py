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

data = input()

num = int(data[0])
count = 0
result = 0

for i in range(len(data)-1):
    if(data[i] != data[i+1]):
        count += 1 # 0 => 1, 1 => 0 계산
    
# 총 뒤집은 횟수 = count를 2로 나눈 몫과 나머지
result += count // 2
result += count % 2

print(result)
    


## 풀이
# data = input()
# count0 = 0 # 전부 0으로 바꾸는 경우
# count1 = 0 # 전부 1로 바꾸는 경우

# # 첫 번째 원소에 대해서 처리
# if data[0] == '1':
#     count0 += 1
# else:
#     count1 += 1

# # 두 번째 원소부터 모든 원소를 확인하며
# for i in range(len(data)-1):
#     if data[i] != data[i+1]:
#         # 다음 수에서 1로 바뀌는 경우
#         if data[i + 1] == '1':
#             count0 += 1
#         else:
#             count1 += 1

# print(min(count0, count1))

end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END")