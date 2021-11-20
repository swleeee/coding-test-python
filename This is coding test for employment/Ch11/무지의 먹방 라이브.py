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

# def solution(food_times, k):
#     answer = 0
#     i = 0
#     count = 0
#     while k >= 0:
#         # print(i)
#         # print("==")
#         # print(k)        
#         if(i == len(food_times)):
#             i = i % len(food_times) 
        
#         if(food_times[i] != 0):      
#             count = 0
#             if(k==0):
#                 i -= 1
#                 if(i==-1):
#                     i = len(food_times)-1
#                     print("==")
#                     print(i)
#                 # break
#             else:
#                 food_times[i] -= 1
#             k -= 1
#         else:
#             count += 1
#             if count == len(food_times):
#                 i = -2
#                 break
#         #     k -= 1
#         i += 1
        
#     if(i == len(food_times)):
#         i = i % len(food_times) 
#     print(i)
#     # print((i) % len(food_times))
#     print(i+1)
#     answer = i+1
            
        
#     return answer


## 풀이
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간

    length = len(food_times) # 남은 음식의 개수
    count = 0
    print("q", q)
    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        print(sum_value + ((q[0][0] - previous) * length))
        count+=1
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -= 1 # 다 먹은 음식 제외
        
        print("count : ", count)
        print("previous : ", previous)
        print("heapq : ", heapq)
        print("length : ", length)
        print("now : ", now)
        print("sum_value : ", sum_value)

        previous = now # 이전 음식 시간 재설정
        print("=======================")

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    print(sum_value + ((q[0][0] - previous) * length))
    result = sorted(q, key = lambda x: x[1]) # 음식의 번호 기준으로 정렬
    print(result)
    return result[(k - sum_value) % length][1]

print(solution([8,6,4], 15))


end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END")