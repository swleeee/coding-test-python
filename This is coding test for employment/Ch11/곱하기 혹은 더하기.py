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
data = list(map(int, input()))
data.sort()
count = data[0]

for i in range(len(data)-1):
    if(data[i] == 0 or data[i] == 1):
        count += data[i+1]
    else:
        count *= data[i+1]

print(count)

    


## 풀이

# data = input()

# # 첫 번째 문자를 숫자로 변경하여 대입
# result = int(data[0])

# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num

# print(result)


end_time = time.time()
print(end_time)  
print("time :", end_time - start_time)
memory_usage("END")