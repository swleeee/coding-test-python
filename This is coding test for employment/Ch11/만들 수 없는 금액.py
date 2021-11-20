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

n = int(input())
data = list(map(int, input().split()))
data.sort()
count = 0
result = 0

# 첫 번째 요소의 값이 1이 아니라면 최소값은 무조건 1임
if data[0] != 1:
    result = 1
else:    
    for i in range(len(data)-1):        
        count += data[i]
        # 현재 인덱스까지의 총 합이 다음 요소의 값-1 보다 작을 경우 현재 인덱스까지의 총 합+1이 최소값이 됨
        if(count+1 < data[i+1]):
            result = count+1
            break

# 각 동전으로 최대 금액을 만들 경우 동전의 총 합+1이 최소값이 됨
if(result==0):
    result += count + data[n-1] + 1

print(result)
    


## 풀이
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# target = 1
# for x in data:
#     # 만들 수 없는 금액을 찾았을 때 반복 종료
#     if target < x:
#         break
#     target += x

# print(target)


end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END")