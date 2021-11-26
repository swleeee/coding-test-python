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
# # data = list(input())
# data = input()
# before = 0
# min_value = 10000
# c = ""
# count = 1
# total_count = 0

# for i in range(len(data)):
#     for j in range(0, len(data), i+1):
#         # print("<0>", i, j)
#         j += i+1
#         if(j>before):
#             # print(i, j, data[before:j])
#             print("<1>", data[before:j], count, total_count)
#             if (c == data[before:j]):
#                 total_count += (len(data[before:j]))
#                 count += 1
#             else:
#                 total_count += (len(data[before:j]))
#                 if(count != 1):
#                     total_count = total_count -(count * len(c)) + len(c) + 1
#                     count = 1
#                 c = data[before:j]    

#         before = j
#     before=0
#     print("<2>", total_count)
#     min_value = min(min_value, total_count)
#     total_count = 0
#     count = 1
#     c = ""
# print(min_value)

## 풀이

data = input()

def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed= ""
        prev = s[0:step]
        count = 1
        # 단위 (step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1

            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer

print(solution(data))


end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END") 
