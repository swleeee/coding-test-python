import time 
import psutil
start_time = time.time()
# print(start_time)

def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")


## 
n = list(map(int, input()))
left_count = 0
right_count= 0 
middle = int(len(n)/2)
length = int(len(n))
# print(middle)

# print(sum(n[0:int(len(n)/2)]))
left_count = sum(n[0:int(len(n)/2)]) 
# print(sum(n[int(len(n)/2):int(len(n))]))
right_count= sum(n[int(len(n)/2):int(len(n))])

if(left_count == right_count):
    print("LUCKY")
else:
    print("READY")
# print(n[0:2])
# print(n[0])


## 풀이
# n = input()
# length = len(n) # 점수값의 총 자릿수
# summary = 0

# # 왼쪽 부분의 자릿수 합 더하기
# for i in range(length // 2):
#     summary += int(n[i])

# # 오른쪽 부분의 자릿수 합 빼기
# for i in range(length // 2, length):
#     summary -= int(n[i])

# # 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
# if summary == 0:
#     print("LUCKY")
# else:
#     print("READY")


end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END") 