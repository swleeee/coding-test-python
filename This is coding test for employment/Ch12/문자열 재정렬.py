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
data = list(input())

data.sort()
# print(data)

count = 0
new_data=""

for s in data:
    # 숫자인 경우
    if(ord(s) < 65):
        count += int(s)

    # 알파벳 대문자인 경우
    else:
        new_data += s
    # print(ord(s))
# print(count)
print(new_data + str(count))

## 풀이
# data = input()
# result = []
# value = 0

# # 문자를 하나씩 확인하며
# for x in data:
#     # 알파벳인 경우 결과 리스트에 삽입
#     if x.isalpha():
#         result.append(x)
#     # 숫자는 따로 더하기
#     else:
#         value += int(x)

# # 알파벳을 오름차순으로 정렬
# result.sort()

# # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
# if value != 0:
#     result.append(str(value))

# # 최종 결과 출력(리스트를 문자열로 변환하여 출력)
# print(''.join(result))




end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END") 