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

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
count = 0
sub_count = 0    

# n개의 볼링공을 2명이서 선택할 수 있는 경우의 수 (중복 제외)
def calCount(n):
    return int((n * (n-1))/2)

for i in range(n-1):
    # 같은 무게의 볼링공 개수 세기
    if(data[i] == data[i+1]):
        sub_count += 1
    else:
        # 같은 무게의 볼링공 경우의 수 계산하여 미리 빼기
        if(sub_count):
            count += -calCount(sub_count+1)            
            sub_count = 0

# 마지막 볼링공이 같은 무게일 경우 추가적으로 계산하여 빼기
if(sub_count):
    count += -calCount(sub_count+1)

# 경우의 수 계산
count += calCount(n)      
print(count)


## 풀이
# n, m = map(int, input().split())
# data = list(map(int, input().split()))

# # 1부터 10까지의 무게를 담을 수 있는 리스트
# array = [0] * 11

# for x in data:
#     # 각 무게에 해당하는 볼링공의 개수 카운트
#     array[x] += 1

# result = 0
# # 1부터 m까지의 각 무게에 대하여 처리
# for i in range(1, m + 1):
#     n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
#     result += array[i] * n # B가 선택하는 경우의 수와 곱하기

# print(result)


end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END")