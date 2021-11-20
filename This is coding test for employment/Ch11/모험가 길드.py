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
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()
# count = 0
# j = 0
# # while i < n:
# #     if(i+data[i] > n):
# #         break
# #     else:
# #         count += 1

# for i in range(n):
#     if(data[i]-1 == j):
#         count += 1
#         j = 0
#     else:
#         j += 1   
    
# print(count)



## 풀이
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# result = 0 # 총 그룹의 수
# count = 0 # 현재 그룹에 포함된 모험가의 수

# for i in data:  
#     count += 1 # 현재 그룹에 해당 모험가를 포함시키기
#     if count >= i:
#         result += 1 # 총 그룹의 수 증가시키기
#         count = 0
  
# print(result)


end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END") 